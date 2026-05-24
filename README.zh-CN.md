# Repo Onboard AI

[English](README.md)

扫描代码仓库，为新贡献者生成实用的 `ONBOARDING.md`。

Repo Onboard AI 会检测语言分布、顶层目录、可能入口文件和常用命令。默认本地运行，也可以通过 OpenAI-compatible 模型优化导览文案。

## 功能

- 扫描仓库文件，并忽略常见生成目录和依赖目录
- 检测语言分布和顶层模块
- 建议阅读顺序和可能入口文件
- 根据常见 manifest 推断安装、运行、构建、测试命令
- 支持 Markdown 和 JSON 输出

## 安装

```bash
python3 -m pip install -e .
```

## 使用

```bash
repo-onboard-ai --repo .
repo-onboard-ai --repo . --output ONBOARDING.md
repo-onboard-ai --repo . --format json
repo-onboard-ai --repo ../some-project --max-files 1200
```

启用 AI 润色：

```bash
export AI_API_KEY="your-key"
repo-onboard-ai --repo . --ai --output ONBOARDING.md
```

## 开发

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests
```

## License

MIT
