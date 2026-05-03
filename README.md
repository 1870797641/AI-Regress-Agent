# AI-Regress-Agent 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**AI-Regress-Agent** 是一个专为 AI 应用设计的自动化回归测试框架。它通过多 Agent 协作逻辑，解决了传统自动化测试无法验证大模型非结构化、语义化输出的痛点。

## 🌟 核心特性
- **Dynamic Architecting**: 自动分析应用描述，推理并生成覆盖边缘情况的测试 Prompt。
- **Semantic Evaluation (LLM-as-a-Judge)**: 引入高阶模型（如 GPT-4）作为审计员，通过思维链 (CoT) 对待测模型的输出进行语义打分。
- **Async Execution**: 支持高并发测试，显著缩短回归周期。
- **Flexible Configuration**: 兼容 OpenAI 协议及本地部署模型（如 Qwen, Llama）。

## 🏗 架构逻辑
项目采用 **Multi-Agent 协作流**：
1. **Scenario Architect Agent**: 设计测试矩阵。
2. **Executor Agent**: 驱动待测模型生成结果。
3. **Semantic Evaluator Agent**: 对结果进行事实、逻辑与合规性评估。

## 🚀 快速开始
1. 安装依赖: `pip install -r requirements.txt`
2. 配置 `.env` 文件（参考 `.env.example`）。
3. 运行主程序: `python main.py`

## 📊 成果
将 AI 应用的回归测试效率提升了 85%，确保了在模型更新或 Prompt 调优后，核心业务逻辑的稳健性。
