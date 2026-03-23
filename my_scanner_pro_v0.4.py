import requests
import threading
import queue
import time
import os
import sys
import argparse

# --- 全局变量 ---
path_queue = queue.Queue()
print_lock = threading.Lock()
found_count = 0
scanned_count = 0
total_count = 0
stop_flag = False
start_time = 0

def scan_path(target_url, timeout):
    global found_count, scanned_count
    
    while not stop_flag:
        try:
            path = path_queue.get(timeout=0.5)
        except queue.Empty:
            break
        
        try:
            path = path.strip()
            if not path: 
                path_queue.task_done()
                continue

            if path.startswith('/'):
                full_url = f"{target_url}{path}"
            else:
                full_url = f"{target_url}/{path}"
            
            response = requests.get(full_url, timeout=timeout, allow_redirects=False)
            status_code = response.status_code
            
            # 筛选逻辑
            if status_code in [200, 301, 302, 401, 403]:
                with print_lock:
                    print(f"\n[+] 发现: {full_url} (状态码: {status_code}) - 长度: {len(response.content)}")
                    found_count += 1
                    
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except Exception:
            pass
        finally:
            with print_lock:
                scanned_count += 1
                if scanned_count % 500 == 0:
                    elapsed = time.time() - start_time
                    speed = scanned_count / elapsed if elapsed > 0 else 0
                    percent = (scanned_count / total_count * 100) if total_count > 0 else 0
                    sys.stdout.write(f"\r⏳ 进度: {scanned_count}/{total_count} ({percent:.2f}%) | 发现: {found_count} | 速度: {speed:.1f} p/s")
                    sys.stdout.flush()
            
            path_queue.task_done()

def load_dict_to_queue(filename, limit=None, skip_comments=True, skip_special_chars=True):
    """
    直接加载到全局 path_queue，支持限制数量和过滤
    """
    global total_count
    encodings = ['utf-8', 'gbk', 'latin-1']
    
    if not os.path.exists(filename):
        print(f"❌ 错误：找不到字典文件 '{filename}'")
        sys.exit(1)

    print(f"📂 正在加载字典: {filename} ...")
    
    loaded = 0
    skipped = 0
    
    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc, errors='ignore') as f:
                for line in f:
                    if stop_flag: break
                    
                    # 如果达到限制数量，停止加载
                    if limit and loaded >= limit:
                        break

                    path = line.strip()
                    
                    if not path: continue
                    if skip_comments and path.startswith('#'):
                        skipped += 1
                        continue
                    if skip_special_chars and '#' in path:
                        skipped += 1
                        continue
                    if ' ' in path:
                        skipped += 1
                        continue

                    path_queue.put(path)
                    loaded += 1
                    
                    if loaded % 100000 == 0:
                        print(f"   🔄 已加载 {loaded // 10000}0 万条...")

            print(f"✅ 加载完成! 有效路径: {loaded}, 跳过: {skipped} (编码: {enc})")
            total_count = loaded
            return
            
        except UnicodeDecodeError:
            continue
    
    print("❌ 无法识别字典编码。")
    sys.exit(1)

def main():
    global start_time, stop_flag, total_count
    
    parser = argparse.ArgumentParser(
        description='🛡️  Python 多线程目录扫描器 (最终版)',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
示例用法:
  python my_scanner_final.py -u http://target.com
  python my_scanner_final.py -u http://target.com -d dict.txt -t 50 --limit 1000
        """
    )
    parser.add_argument('-u', '--url', required=True, help='目标 URL')
    parser.add_argument('-d', '--dict', default='敏感文件字典.txt', help='字典文件路径')
    parser.add_argument('-t', '--threads', type=int, default=20, help='线程数量')
    parser.add_argument('--timeout', type=float, default=2.0, help='请求超时时间')
    parser.add_argument('--limit', type=int, default=None, help='限制扫描路径数量 (测试用)')
    parser.add_argument('--allow-hash', action='store_true', help='允许包含 "#" 的路径')
    
    args = parser.parse_args()

    # 1. 加载字典 (直接在函数内处理 limit 和过滤)
    load_dict_to_queue(
        args.dict, 
        limit=args.limit,
        skip_comments=True, 
        skip_special_chars=not args.allow_hash
    )

    if total_count == 0:
        print("⚠️  没有可扫描的路径，退出。")
        return

    print("-" * 40)
    print(f"🎯 目标: {args.url}")
    print(f"🧵 线程: {args.threads}")
    print(f"⏱️  超时: {args.timeout}s")
    if args.limit:
        print(f"⚠️  模式: 测试限制 ({args.limit} 条)")
    print("-" * 40)
    print("开始扫描... (Ctrl+C 停止)\n")

    start_time = time.time()
    threads = []

    for i in range(args.threads):
        t = threading.Thread(target=scan_path, args=(args.url, args.timeout))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        path_queue.join()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断，正在停止...")
        stop_flag = True

    end_time = time.time()
    duration = end_time - start_time

    print("\n" + "=" * 40)
    print(f"🏁 扫描结束")
    print(f"⏱️  总耗时: {duration:.2f} 秒")
    print(f"📊 已尝试: {scanned_count}")
    print(f"🎯 发现有效: {found_count}")
    if duration > 0:
        print(f"⚡ 平均速度: {scanned_count / duration:.2f} 路径/秒")
    print("=" * 40)

if __name__ == "__main__":
    main()