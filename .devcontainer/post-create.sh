#!/usr/bin/env bash
set -e

# create virtualenv
python3 -m venv .venv
source .venv/bin/activate

# upgrade pip & install basic deps
pip install --upgrade pip
pip install -r requirements.txt

# create .env from example if not present
if [ ! -f .env ]; then
  cp .env.example .env
  echo "# Edit .env and add your Hugging Face token" >> .env
fi

echo "✅ Devcontainer setup complete. Activate venv: source .venv/bin/activate"
