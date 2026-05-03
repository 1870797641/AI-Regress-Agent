import asyncio
from typing import List
from core.models import TestResult
from agents.architect import ScenarioArchitect
from agents.evaluator import SemanticEvaluator
from openai import AsyncOpenAI

class RegressionEngine:
    def __init__(self, api_key: str, base_url: str, t_model: str, e_model: str):
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.architect = ScenarioArchitect(self.client, e_model) # Use e_model (usually better) for architecting
        self.evaluator = SemanticEvaluator(self.client, e_model)
        self.target_model = t_model # 待测模型

    async def run(self, app_desc: str) -> List[TestResult]:
        # 1. 生成用例
        cases = await self.architect.generate_cases(app_desc)
        
        # 2. 模拟执行并评估 (并行处理)
        async def run_single_test(case):
            # 模拟执行待测模型
            resp = await self.client.chat.completions.create(
                model=self.target_model,
                messages=[{"role": "user", "content": case.prompt}]
            )
            actual_output = resp.choices[0].message.content
            # 进行语义评估
            return await self.evaluator.evaluate(case, actual_output)

        tasks = [run_single_test(c) for c in cases]
        return await asyncio.gather(*tasks)
