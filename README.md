# Web Summarizer Skill for Claude Code

这是一个专为 Claude Code 优化的技能扩展，旨在帮助 Claude 更好地读取、解析并总结网页内容（特别是微信公众号文章）。

## 特性
- **微信深度优化**：内置针对微信公众号文章结构的解析逻辑。
- **科普风格总结**：强制执行专业、严谨的科普写作风格。
- **本地脚本支持**：提供 Python 脚本绕过某些环境下的联网限制。

## 安装方法 (Claude Code)

1. **克隆仓库**到你的本地项目目录：
   ```bash
   git clone https://github.com/ClaireWong86/web-summarizer.git
   ```

2. **告知 Claude** 加载此技能：
   在 Claude Code 终端中输入：
   > "请读取并学习 `./web-summarizer/SKILL.md` 中的指令，今后我发送链接时，请按此规范进行总结。"

## 使用示例

直接在对话中发送：
> "帮我总结一下这个网页：https://mp.weixin.qq.com/s/udSpp7eMqwiRo5yVShRzLw"

Claude 会自动识别 URL，并根据 `SKILL.md` 中的规范进行处理。

## 依赖
- Python 3.x
- `requests`
- `beautifulsoup4`

安装依赖：
```bash
pip install requests beautifulsoup4
```
