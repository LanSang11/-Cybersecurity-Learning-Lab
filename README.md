🛡️ Python Security Lab (网络安全实验室)

🇨🇳 简介: 本仓库用于记录目录扫描网络安全工具的开发学习过程。从 v0.1 原型到 v0.4 专业版，真实还原解决编码报错、多线程死锁等问题的全过程。
🇺🇸 About: A repository dedicated to learning cybersecurity tool development. Documents the full journey from v0.1 prototype to v0.4 professional version, including real-world troubleshooting like encoding errors and threading deadlocks.

📂 项目结构 / Project Structure

my_scanner_pro_v0.4.py: 最终版多线程目录扫描器源码 (Final multi-threaded scanner source code).
dict_sample.txt: 小型测试字典，用于快速验证功能 (Small sample dictionary for testing).
README.md: 项目说明文档 (Project documentation).

⚠️ 注意 / Note: 
🇨🇳 出于仓库体积和安全合规考虑，本仓库不包含大型黑客字典。请自行准备字典文件并通过 -d 参数加载。
🇺🇸 Large hacker dictionaries are NOT included due to repository size limits and compliance. Please prepare your own dictionary files and load them via the -d argument.

🚀 快速开始 / Quick Start

环境要求 / Requirements
Python 3.x
requests library

bash
pip install requests

运行示例 / Usage Examples

基础扫描 (Basic Scan):
bash
python my_scanner_pro_v0.4.py -u http://example.com

高性能模式 (High Performance):
bash
python my_scanner_pro_v0.4.py -u http://example.com -t 50 --limit 2000

查看帮助 (Help):
bash
python my_scanner_pro_v0.4.py -h

📖 版本迭代日志 / Version History
版本   状态   主要改进 / Key Improvements
v0.1   🐢 原型   单线程实现，基础请求逻辑 (Single-threaded prototype).

v0.2   🐛 修复   解决多编码字典读取崩溃问题 (Fixed UnicodeDecodeError for mixed encodings).

v0.3   🧵 并发   引入多线程，修复队列死锁问题 (Added threading, fixed queue deadlock).

v0.4   🚀 发布   增加 CLI 参数、进度条、智能过滤 (Added CLI, progress bar, smart filtering).

## 📝 更新日志

### v0.5 (2026-03-25)
- ✨ **新增风险评级系统**：自动识别 200/301/403 等状态码并标记为 🔴高危/🟠中危/🟡低危。
- ✨ **新增智能排序导出**：CSV/JSON 报告自动按风险等级从高到低排序，优先展示高危漏洞。
- ✨ **优化 Excel 兼容性**：CSV 导出采用 utf-8-sig 编码，完美解决中文乱码问题。
- 🐛 **修复**：修复了路径中连续斜杠的处理逻辑。

### v0.4 (旧版本)
- 基础多线程扫描功能。
- 支持 CSV/JSON 导出（无排序）。

📝 详细教程 / Detailed Tutorial

想深入了解开发过程中的踩坑细节？请阅读我的博客文章：
[CSDN / 博客园 / FreeBuf / 知乎] (在此处填入你发布文章后的链接)

⚖️ 免责声明 / Disclaimer

🇨🇳 本工具仅供网络安全学习和研究使用。严禁用于任何未授权的攻击行为。使用者需自行承担法律责任。
🇺🇸 This tool is for educational and research purposes only. Do not use it for any unauthorized attacks. Users are solely responsible for their actions.

Made with ❤️ by LanSang11
