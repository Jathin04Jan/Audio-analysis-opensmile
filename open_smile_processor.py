import subprocess
import opensmile
import pandas as pd


class OpenSmileProcessor:
    def __init__(self):
        self.smile = opensmile.Smile(
            feature_set=opensmile.FeatureSet.eGeMAPSv02,
            feature_level=opensmile.FeatureLevel.Functionals,
        )

    def extract_features(self, audio_path: str) -> pd.DataFrame:
        # returns a DF of functionals
        df = self.smile.process_file(audio_path)
        if df.empty:
            print("No data processed from the audio file.")
        return df
