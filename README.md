# 🛡️ Python Security Lab (网络安全实验室)

> **MyScanner Pro v1.2 - 智能泛解析过滤版**

🇨🇳 **简介**: 本仓库用于记录目录/子域名扫描网络安全工具的开发学习过程。从 v0.1 原型到 **v1.2 专业版**，真实还原解决编码报错、多线程死锁、泛解析误报等核心痛点的全过程。

🇺🇸 **About**: A repository dedicated to learning cybersecurity tool development. Documents the full journey from v0.1 prototype to **v1.2 professional version**, including real-world troubleshooting like encoding errors, threading deadlocks, and wildcard DNS false positives.

## 📂 项目结构 / Project Structure

- **`my_scanner_pro_v1.2_final.py`**: **【最新版】** 多线程目录/子域名扫描器源码，具备智能泛解析过滤功能。
- **`dict_sample.txt`**: 小型测试字典，用于快速验证功能 (Small sample dictionary for testing).
- **`requirements.txt`**: 项目依赖文件 (Project dependencies).

## ✨ MyScanner Pro v1.2 核心亮点

- **🧠 智能去重**: 独创 "重定向目标 + 内容指纹" 双重验证机制。
- **🚫 自动过滤**: 自动识别并剔除跳转到默认首页的假子域名（泛解析），只保留真实资产。
- **🔇 纯净输出**: 屏蔽 HTTPS 证书警告，终端界面更清爽。
- **📊 详细报表**: 生成 CSV 报告，明确标记 `pan_reason` (泛解析原因)，方便二次筛选。
- **🛡️ 风险评级**: 自动识别状态码并标记风险等级 (🔴高危: 200, 🟠中危: 301/401, 🟡低危: 302/403)。
- **📈 智能排序**: 报告自动按“高危 -> 低危”排序，重要漏洞优先展示。

## ⚠️ 注意 / Note

🇨🇳 出于仓库体积和安全合规考虑，本仓库不包含大型黑客字典。请自行准备字典文件并通过 `-d` 参数加载。
🇺🇸 Large hacker dictionaries are NOT included due to repository size limits and compliance. Please prepare your own dictionary files and load them via the `-d` argument.

## 🚀 快速开始 / Quick Start

### 环境要求 / Requirements
- Python 3.x
- requests library

```bash
pip install -r requirements.txt

运行示例 / Usage Examples
基础扫描 (Basic Scan):
bash

编辑



python my_scanner_pro_v1.2_final.py -u http://example.com
高性能模式 (High Performance):
bash

编辑



python my_scanner_pro_v1.2_final.py -u http://example.com -t 50 --limit 2000
查看帮助 (Help):
bash

编辑



python my_scanner_pro_v1.2_final.py -h
📝 版本迭代日志 / Version History
表格
版本	状态	主要改进 / Key Improvements
v1.2	🚀 最新	智能泛解析过滤，内容指纹去重，CSV报告增强。
v0.5	📦 归档	新增风险评级系统，智能排序导出，Excel兼容性优化。
v0.4	📦 归档	基础多线程扫描，CLI参数，进度条。

想深入了解开发过程中的踩坑细节？ 请关注我的技术博客！(链接待填入)
⚖️ 免责声明 / Disclaimer
🇨🇳 本工具仅供网络安全学习和研究使用。严禁用于任何未授权的攻击行为。使用者需自行承担法律责任。
🇺🇸 This tool is for educational and research purposes only. Do not use it for any unauthorized attacks. Users are solely responsible for their actions.
Made with ❤️ by LanSang11
