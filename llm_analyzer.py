import json
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

class LLMAnalyzer:
    """
    Uses LangChain to prompt OpenAI LLM for a human-readable tone analysis.
    """
    def __init__(self, openai_api_key: str, model_name: str = 'gpt-4o-mini', temperature: float = 0.7):
        self.llm = OpenAI(openai_api_key=openai_api_key, model_name=model_name, temperature=temperature)
        self.prompt = PromptTemplate(
            input_variables=['features'],
            template=(
                "Analyze the vocal characteristics of the sales call based on these acoustic features in JSON:\n"
                "{features}\n"
                "Provide a concise summary of pace, pitch variation, loudness, and voice quality."
            )
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def analyze(self, features_dict: dict) -> str:
        features_json = json.dumps(features_dict, indent=2)
        return self.chain.run(features=features_json)