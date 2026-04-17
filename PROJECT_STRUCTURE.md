# Project Structure

```text
tennis_analyst/
├── app.py                    # Streamlit app entry point and analysis workflow
├── config.example.py         # Example local config template (do not store real key)
├── Launch_Tennis_Coach.command  # Local launch script
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview and setup guide
├── PROJECT_STRUCTURE.md      # This file
├── LICENSE                   # MIT license
├── videos/                   # Local sample/input videos (git-ignored)
└── __pycache__/              # Python cache files (git-ignored)
```

## Core Components
- `app.py`: handles UI, upload, Gemini video processing, bilingual report parsing, and display.
- `config.example.py`: documents optional fallback local key file pattern.
- `Launch_Tennis_Coach.command`: convenience launcher for local machine setup.

## Git Hygiene
- `config.py`, `videos/`, and cache files are excluded via `.gitignore`.
- Environment-based API key loading is the default secure path.
