import asyncio
import os
from dotenv import load_dotenv
from core.engine import RegressionEngine
from colorama import Fore, Style

# 如果没有 .env 文件，直接从环境变量读取
load_dotenv()

async def main():
    print(Fore.CYAN + "🤖 AI-Regress-Agent 启动中..." + Style.RESET_ALL)
    
    api_key = os.getenv("API_KEY", "your_api_key_here")
    base_url = os.getenv("BASE_URL", "https://api.openai.com/v1")
    
    engine = RegressionEngine(
        api_key=api_key,
        base_url=base_url,
        t_model="gpt-3.5-turbo", # 待测版本
        e_model="gpt-4o"         # 审计版本
    )

    app_desc = "一个提供法律咨询建议并能起草合同草案的 AI 法律助手。"
    
    try:
        results = await engine.run(app_desc)

        print(f"\n{Fore.YELLOW}📊 回归测试汇总报告:{Style.RESET_ALL}")
        for r in results:
            color = Fore.GREEN if r.status == "PASS" else Fore.RED
            print(f"{color}[{r.status}] 用例 #{r.test_id}: {r.scenario}")
            print(f"   - 分数: {r.score}")
            print(f"   - 理由: {r.reasoning}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ 运行出错: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 请确保在 .env 中正确配置了 API_KEY 和 BASE_URL。{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())
