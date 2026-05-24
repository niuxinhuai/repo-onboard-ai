# Repo Onboard AI

[![CI](https://github.com/niuxinhuai/repo-onboard-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/niuxinhuai/repo-onboard-ai/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

[English](README.md)

扫描代码仓库，为新贡献者生成实用的 `ONBOARDING.md`。

Repo Onboard AI 会检测语言分布、顶层目录、可能入口文件和常用命令。默认本地运行，也可以通过 OpenAI-compatible 模型优化导览文案。

## 功能

- 扫描仓库文件，并忽略常见生成目录和依赖目录
- 支持重复传入 `--ignore`，忽略项目里的自定义生成目录
- 检测语言分布和顶层模块
- 建议阅读顺序和可能入口文件
- 根据常见 manifest 推断安装、运行、构建、测试命令
- 支持 `--tree` 输出简化目录树
- 支持 Markdown 和 JSON 输出

## 安装

在包发布到 PyPI 之前，可以直接从 GitHub 安装：

```bash
pipx install git+https://github.com/niuxinhuai/repo-onboard-ai.git
```

也可以使用 pip：

```bash
python3 -m pip install git+https://github.com/niuxinhuai/repo-onboard-ai.git
```

本地开发安装：

```bash
python3 -m pip install -e .
```

也可以从最新 GitHub Release 下载 wheel 和 sdist： https://github.com/niuxinhuai/repo-onboard-ai/releases/latest

## 使用

```bash
repo-onboard-ai --repo .
repo-onboard-ai --repo . --tree
repo-onboard-ai --repo . --output ONBOARDING.md
repo-onboard-ai --repo . --format json
repo-onboard-ai --repo ../some-project --max-files 1200
repo-onboard-ai --repo . --ignore generated --ignore vendor
```

项目里有自定义生成目录时，可以重复使用 `--ignore`，避免导览文档被噪音文件干扰。

可以直接查看生成示例：[`examples/output.md`](examples/output.md) 和 [`examples/output.json`](examples/output.json)。

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

## 发布

推送 tag 后，GitHub Actions 会构建 Python 包并创建 GitHub Release。PyPI 发布默认关闭；若要发布到 PyPI，请先配置 Trusted Publishing，并设置仓库变量 `PUBLISH_TO_PYPI=true`，然后推送 tag：

```bash
git tag v0.1.0
git push origin v0.1.0
```

## License

MIT
