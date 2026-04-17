#!/bin/bash

# Navigate to project directory (portable, works on any machine)
cd "$(dirname "$0")"

# Launch Streamlit (requires streamlit in PATH or active virtual environment)
streamlit run app.py
