# Introduction Engine

This engine generates introduction variants from a topic and hook type, enforces thesis presence, and scores clarity and promise.

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run tests:
   ```
   python -m pytest test_intro_engine.py
   ```
3. Generate an introduction:
   ```python
   from intro_engine import generate_introduction
   introduction = generate_introduction("climate change", "anecdote")
   print(introduction)
   ```

## Scoring

- **Clarity**: Scored based on word count.
- **Promise**: Scored based on thesis presence.

## Hook Types

- anecdote
- question
- quote
- statistic