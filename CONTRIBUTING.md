# Contributing

Thanks for contributing to `Tennis Coach Pro`.

## Development Setup
1. Create a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set API key:

```bash
export GOOGLE_API_KEY="your_google_api_key"
```

4. Run app:

```bash
streamlit run app.py
```

## Guidelines
- Keep secrets out of git (never commit `config.py` with a real key).
- Prefer small, focused pull requests.
- Update documentation when behavior changes.
- Verify the app starts and can render UI before opening a PR.

## Suggested Commit Format
- `feat: ...` for new features
- `fix: ...` for bug fixes
- `docs: ...` for documentation updates
- `chore: ...` for maintenance tasks
