# Sales Call Tone Analysis

A Python CLI tool that extracts acoustic functionals from sales-call WAV files using OpenSMILE, summarizes them into a JSON, and generates a human-readable tone analysis via OpenAI’s `o4-mini` model (through LangChain).

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Project Structure](#project-structure)  
4. [Installation & Setup](#installation--setup)  
5. [Configuration](#configuration)  
6. [Running the Analysis](#running-the-analysis)  
7. [Testing the OpenAI & SMILE Setup](#testing-the-openai--smile-setup)  
8. [Extending the Feature Map](#extending-the-feature-map)  
9. [Troubleshooting](#troubleshooting)  
10. [Contributing](#contributing)  
11. [License](#license)  

---

## Features

- **OpenSMILE functionals** via the `opensmile` Python wrapper  
- **Feature summarization** into LLM-friendly JSON  
- **LLM prompt** (o4-mini) through LangChain for a concise tone report  
- **Simple CLI**: `python main.py path/to/your.wav`  
- **Environment-driven**: `.env` file for your API key  
- **Test scripts** to verify both OpenAI and OpenSMILE integration  

---

## Prerequisites

- **Python 3.8+**  
- **git**, **curl** (for config download)  
- **Virtual environment** (strongly recommended)  
- **OpenAI API key** with access to `o4-mini`  
- **Internet connection** (for API calls)  

---

## Project Structure

```text
tone-analysis/
├── __pycache__/             # Python cache files
├── toneEnv/                 # Your Python virtualenv (gitignored)
├── .env                     # Your OpenAI key (gitignored)
├── .gitignore               # Files & folders to ignore
├── feature_summarizer.py    # Maps OpenSMILE outputs → summary dict
├── llm_analyzer.py          # LangChain chain for tone analysis
├── main.py                  # CLI entrypoint orchestrating pipeline
├── open_smile_processor.py  # Wraps the opensmile.Smile API
├── requirements.txt         # pip dependencies
├── test_openai.py           # Quick OpenAI API connectivity test
├── test_smile.py            # Quick OpenSMILE processing test
└── test.wav                 # (Optional) sample audio file
```

---


## Installation & Setup

1. Clone the repository

    ```bash
    git clone https://github.com/<your-username>/sales-call-tone-analysis.git
    cd sales-call-tone-analysis
    ```

2. Create and activate a virtual environment

    ```bash
    python3 -m venv toneEnv
    source toneEnv/bin/activate
    ```

3. Upgrade pip

    ```bash
    pip install --upgrade pip
    ```

4. Install dependencies

    ```bash
    pip install -r requirements.txt
    pip install python-dotenv
    pip install opensmile
    ```

5. Verify installations

    - Check OpenSMILE wrapper:

        ```bash
        python - << 'EOF'
        import opensmile
        print("OpenSMILE wrapper installed")
        EOF
        ```
    - Check python-dotenv:

        ```bash
        python - << 'EOF'
        from dotenv import load_dotenv
        print("python-dotenv installed")
        EOF
        ```
    - Check OpenAI client:

        ```bash
        python - << 'EOF'
        import openai
        print("OpenAI client installed")
        EOF
        ```

## Configuration

1. Create a `.env` file in the project root with your OpenAI key:

    ```ini
    OPENAI_API_KEY=sk-<your-real-openai-key>
    ```

   Make sure `.env` is listed in `.gitignore` so your key is not committed.

2. (Optional) Supply a custom OpenSMILE configuration:

   - Create a `configs/` directory:

        ```bash
        mkdir -p configs
        ```

   - Download the official eGeMAPSv02.conf into `configs/`:

        ```bash
        curl -L \
          https://raw.githubusercontent.com/audeering/opensmile/main/config/gemaps/eGeMAPSv02.conf \
          -o configs/eGeMAPSv02.conf
        ```

   - In `open_smile_processor.py`, modify the initializer to point at your config:

        ```python
        import opensmile

        class OpenSmileProcessor:
            def __init__(self):
                self.smile = opensmile.Smile(
                    feature_set=opensmile.FeatureSet.Custom,
                    config_path="configs/eGeMAPSv02.conf",
                    feature_level=opensmile.FeatureLevel.Functionals
                )
        ```


 ## Running the Analysis

1. Activate your virtual environment:
    ```bash
    source toneEnv/bin/activate
    ```
2. Run the main pipeline:
    ```bash
    python main.py path/to/your_audio_file.wav
    ```
3. Sample output:
    ```
    Features JSON: {
      "mean_pitch_semitone": 32.7,
      "mean_hnr": 8.3,
      "jitter_local": 0.0196,
      ...
    }

    === Tone Analysis Summary ===
    - Pitch Variation: Moderate, centered around 32.7 semitones
    - Pace: Approx. 3.1 voiced segments/sec – a steady pace
    - Loudness: Mean 0.85, range 0.6 – consistent volume
    - Voice Quality: HNR 18.9 dB – clear and resonant voice
    ```

## Testing the OpenAI & SMILE Setup

1. Verify OpenAI integration:
    ```bash
    python test_openai.py
    ```
   Expected:
    ```
    LLM replied: Hello! How can I assist you today?
    ```

2. Verify OpenSMILE integration (in `test_smile.py`):
    ```python
    import opensmile
    df = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals
    ).process_file("test.wav")
    print(df.head())
    ```
    ```bash
    python test_smile.py
    ```
   You should see a pandas DataFrame of acoustic functionals.

## Extending the Feature Map

1. Print available columns in `open_smile_processor.py`:
    ```python
    print("Available columns:", df.columns.tolist())
    ```
2. In `feature_summarizer.py`, update `DEFAULT_FEATURE_MAP`:
    ```python
    DEFAULT_FEATURE_MAP.update({
        'loudness_sma3nz_min': 'loudness_min',
        'loudness_sma3nz_max': 'loudness_max',
        'silenceRate_sma3nz_amean': 'silence_rate',
        'shimmerLocal_sma3nz_amean': 'shimmer_local',
        'spectralFlux_sma3nz_amean': 'spectral_flux',
        # add more as needed
    })
    ```
3. Re-run analysis:
    ```bash
    python main.py test.wav
    ```

## Troubleshooting

- Key not found:
  - Verify `.env` exists with `OPENAI_API_KEY`.
  - Confirm `load_dotenv()` is called before `os.getenv()` in `main.py`.
- Invalid API key (401):
  - Check your key at https://platform.openai.com/account/api-keys.
  - Restart your terminal/IDE after editing `.env`.
- OpenSMILE errors:
  - Ensure `opensmile` is installed in the active environment.
  - Confirm your WAV is valid PCM (16-bit, mono or stereo).
- Module import errors:
  ```bash
  pip install langchain-community python-dotenv opensmile       