🛡️ Python Security Lab (网络安全实验室)

MyScanner Pro v1.2 - 智能泛解析过滤版

🇨🇳 简介: 本仓库记录了一个目录/子域名扫描器从 v0.1 原型到 v1.2 专业版 的完整开发历程。它真实还原了在工程实践中解决编码报错、多线程死锁、泛解析误报等核心痛点的全过程，是学习网络安全工具开发的绝佳案例。

🇺🇸 About: This repository documents the full development journey of a directory/subdomain scanner, from a v0.1 prototype to the professional v1.2 release. It showcases real-world solutions to common engineering challenges like encoding errors, threading deadlocks, and wildcard DNS false positives.

✨ MyScanner Pro v1.2 核心亮点

🧠 智能去重: 独创 "重定向目标 + 内容指纹" 双重验证机制，精准识别有效资产。
🚫 自动过滤: 自动识别并剔除跳转到默认首页的假子域名（泛解析），只保留真实目标。
🛡️ 风险评级: 自动识别状态码并标记风险等级 (🔴高危: 200, 🟠中危: 301/401, 🟡低危: 302/403)。
📈 智能排序: 扫描报告自动按“高危 -> 低危”排序，确保关键漏洞优先呈现。
📊 详细报表: 生成结构化 CSV 报告，明确标记 pan_reason (泛解析原因)，便于二次分析。
🔇 纯净输出: 屏蔽 HTTPS 证书警告，提供清爽的终端交互体验。

📂 项目结构

my_scanner_pro_v1.2_final.py: 【最新版】 多线程扫描器源码。
dict_sample.txt: 小型测试字典，用于快速验证功能。
requirements.txt: 项目依赖文件。

⚠️ 注意 / Note

🇨🇳 出于仓库体积和安全合规考虑，本仓库不包含大型黑客字典。请自行准备字典文件并通过 -d 参数加载。
🇺🇸 Large hacker dictionaries are NOT included due to repository size limits and compliance. Please prepare your own dictionary files and load them via the -d argument.

🚀 快速开始

安装依赖

bash
pip install -r requirements.txt

运行示例

基础扫描
bash
python my_scanner_pro_v1.2_final.py -u http://example.com

高性能模式 (自定义线程数和请求限制)
bash
python my_scanner_pro_v1.2_final.py -u http://example.com -t 50 --limit 2000

查看所有选项
bash
python my_scanner_pro_v1.2_final.py -h

📝 版本历史
版本   状态   主要改进
v1.2   🚀 最新   智能泛解析过滤，内容指纹去重，CSV报告增强。

v0.5   📦 归档   新增风险评级系统，智能排序导出，Excel兼容性优化。

v0.4   📦 归档   基础多线程扫描，CLI参数，进度条。

想深入了解开发细节？ 敬请期待我的技术博客文章！

⚖️ 免责声明

🇨🇳 本工具仅供网络安全学习和研究使用。严禁用于任何未授权的攻击行为。使用者需自行承担法律责任。
🇺🇸 This tool is for educational and research purposes only. Do not use it for any unauthorized attacks. Users are solely responsible for their actions.

Made with ❤️ by LanSang11

现在，你的 DirScanner-Lab` 仓库看起来就像一个真正的、专业的开源项目了！这将给任何访问你 GitHub 主页的人留下极其深刻的印象。
