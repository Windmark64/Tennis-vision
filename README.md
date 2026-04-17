# Tennis Coach Pro

Tennis Coach Pro — AI-Powered Tennis Technique Analyzer 🎾

I used to wish I had a coach who could break down exactly what I was doing wrong — my footwork, my swing path, my stance — and map out a real path to improvement. Every app I tried was either clunky to use, paywalled before you even started, or gave analysis too generic to be useful.

So I built this.

Tennis Coach Pro lets you upload any training video and get an instant, detailed technical diagnostic report — the kind of feedback you'd expect from a professional coach. No subscriptions. No fluff. Just honest, precise analysis powered by Google Gemini's large vision model, evaluated against USTA NTRP/UTR standards.

Built for tennis learners and enthusiasts who are serious about improving, but don't have a coach in their corner every session. Have fun, and all constructive feedback is welcome. Let's improve this together!


## Overview
`Tennis Coach Pro` analyzes uploaded training videos and returns a detailed technical report aligned to USTA NTRP/UTR-style assessment framing.  
The app supports bilingual output:
- English
- Chinese (中文)

## Features
- 🎥 Upload .mov / .mp4 training clips directly in the browser
- 📊 Deep technical breakdown — swing mechanics, footwork, stance, positioning
- 🌐 Full bilingual support — English & Chinese (中文) in one session
- ⚡ Powered by Google Gemini large vision model
- 🆓 Free to self-host — bring your own API key

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
