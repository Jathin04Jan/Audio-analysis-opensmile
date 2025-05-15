import pandas as pd

class FeatureSummarizer:
    """
    Prepares an LLM-friendly summary dict from OpenSMILE DataFrame.
    """
    DEFAULT_FEATURE_MAP = {
        'F0semitoneFrom27.5Hz_sma3nz_amean': 'mean_pitch_semitone',
        'F0semitoneFrom27.5Hz_sma3nz_stddev': 'pitch_stddev',
        'voicedSegmentsPerSec_sma3nz_amean': 'voiced_segments_per_sec',
        'loudness_sma3nz_amean': 'mean_loudness',
        'loudness_sma3nz_stddev': 'loudness_stddev',
        'HNRdBACF_sma3nz_amean': 'mean_hnr'
    }

    def __init__(self, feature_map: dict = None):
        self.feature_map = feature_map or self.DEFAULT_FEATURE_MAP

    def summarize(self, df: pd.DataFrame) -> dict:
        if df.empty:
            return {}
        row = df.iloc[0]
        return {
            key: float(row[col])
            for col, key in self.feature_map.items()
            if col in row
        }