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

