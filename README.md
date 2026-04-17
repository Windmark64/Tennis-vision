# Tennis Coach Pro

AI-powered tennis video analysis app built with Streamlit + Google Gemini.

## Overview
`Tennis Coach Pro` analyzes uploaded training videos and returns a detailed technical report aligned to USTA NTRP/UTR-style assessment framing.  
The app supports bilingual output:
- English
- Chinese (中文)

## Features
- Upload `.mov` / `.mp4` training clips
- One-click technical analysis workflow
- Bilingual report rendering in one app session
- Clean, minimal Streamlit UI for coaching review
- Reset/re-run flow for iterative training feedback

## Tech Stack
- Python 3.10+
- Streamlit
- Google Gemini API (`google-genai`)

## Project Structure
See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for a full breakdown.

## Quick Start
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set your API key (recommended):

```bash
export GOOGLE_API_KEY="your_google_api_key"
```

5. Run the app:

```bash
streamlit run app.py
```

## Optional Local Config File
For local-only development, you can copy `config.example.py` to `config.py` and place your key there.  
`config.py` is git-ignored and should never be committed.

## Launcher Script
You can also run:

```bash
./Launch_Tennis_Coach.command
```

Edit the script if your virtual environment path differs from your local machine.

## Security Notes
- Do not commit API keys.
- Keep `config.py` local only.
- Rotate keys immediately if they are ever exposed.

## Roadmap Ideas
- Shot segmentation (serve/forehand/backhand/volley)
- Frame-by-frame keypoint overlays
- Session history + report export
- Coach/player profile presets

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE).
