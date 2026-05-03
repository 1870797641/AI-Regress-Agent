import json
from core.models import TestCase
from openai import AsyncOpenAI

class ScenarioArchitect:
    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def generate_cases(self, app_desc: str, count: int = 3) -> list[TestCase]:
        print(f"🔍 [Architect] 分析应用需求并生成 {count} 个边缘测试场景...")
        prompt = f"""
        作为资深测试专家，针对以下 AI 应用描述，设计 {count} 个回归测试用例。
        应用描述：{app_desc}
        要求：
        1. 涵盖核心功能和潜在的异常边界。
        2. 预期行为需明确逻辑要点。
        以 JSON 格式返回，根字段为 'cases'，包含 id, scenario, prompt, expected_behavior。
        """
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        data = json.loads(response.choices[0].message.content)
        return [TestCase(**c) for c in data['cases']]
