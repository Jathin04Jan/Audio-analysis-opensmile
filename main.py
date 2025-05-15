import argparse
from open_smile_processor import OpenSmileProcessor
from feature_summarizer import FeatureSummarizer
from llm_analyzer import LLMAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()


def main(audio_file: str):
    # 1) Extract acoustic functionals
    smile = OpenSmileProcessor()
    df = smile.extract_features(audio_file)

    # 2) Summarize features
    summarizer = FeatureSummarizer()
    features = summarizer.summarize(df)
    if not features:
        print("No features extracted—check your audio or config.")
        return

    # 3) Generate analysis via LLM
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    print("KEY LOADED:", os.getenv("OPENAI_API_KEY", None))
    analyzer = LLMAnalyzer(api_key)
    analysis = analyzer.analyze(features)


    print("\n=== Tone Analysis Summary ===")
    print(analysis)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sales call tone analysis')
    parser.add_argument('audio_file', type=str, help='Path to WAV file')
    args = parser.parse_args()
    main(args.audio_file)