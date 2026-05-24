# Repo Onboard AI

扫描一个代码仓库，生成给新贡献者看的 `ONBOARDING.md`。

默认使用本地启发式分析目录、语言、入口文件和建议阅读顺序；配置 `AI_API_KEY` 后可以让模型把结果整理成更像人写的项目导览。

## 快速开始

```bash
python3 -m repo_onboard_ai --repo . --output ONBOARDING.md
```

只打印到终端：

```bash
python3 -m repo_onboard_ai --repo ../some-project
```

启用 AI 增强：

```bash
export AI_API_KEY="your-key"
python3 -m repo_onboard_ai --repo . --ai --output ONBOARDING.md
```

## License

MIT
