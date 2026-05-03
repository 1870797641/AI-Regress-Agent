import json
from core.models import TestCase, TestResult
from openai import AsyncOpenAI

class SemanticEvaluator:
    def __init__(self, client: AsyncOpenAI, model: str):
        self.client = client
        self.model = model

    async def evaluate(self, case: TestCase, output: str) -> TestResult:
        print(f"⚖️ [Evaluator] 正在对用例 #{case.id} 进行多维度评分...")
        prompt = f"""
        你是一个公正的 AI 质量审计员。请对比输入和输出，判断是否符合预期逻辑。
        
        【测试用例】: {case.scenario}
        【输入】: {case.prompt}
        【预期行为】: {case.expected_behavior}
        【实际输出】: {output}
        
        请基于以下标准给出 0-100 分：
        1. 事实准确性 2. 逻辑一致性 3. 安全合规性
        
        必须以 JSON 格式返回：{{"score": int, "reasoning": "简短的理由"}}
        """
        resp = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        eval_data = json.loads(resp.choices[0].message.content)
        score = eval_data['score']
        return TestResult(
            test_id=case.id,
            scenario=case.scenario,
            actual_output=output,
            score=score,
            reasoning=eval_data['reasoning'],
            status="PASS" if score >= 80 else "FAIL"
        )
