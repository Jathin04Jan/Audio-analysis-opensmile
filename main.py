# main.py
from open_smile_processor import OpenSmileProcessor
from feature_summarizer import FeatureSummarizer
from llm_analyzer import LLMAnalyzer

def main(audio_file):
    # 1) Extract
    smile = OpenSmileProcessor()
    df = smile.extract_features(audio_file)

    # 2) Summarize
    summarizer = FeatureSummarizer()
    features = summarizer.summarize(df)
    if not features:
        print("No features extracted—check your audio or config.")
        return

    # 3) Analyze
    analyzer = LLMAnalyzer(api_key='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')
    print(analyzer.analyze(features))

if __name__ == '__main__':
    import sys
    main(sys.argv[1])