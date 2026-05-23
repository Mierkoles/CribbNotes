# Demystifying AI: Separating Architecture from the Hype

**Industry event · May 2026 · SIM Members**

Companion Colab notebooks for the hands-on session by:

- **Ken Garfinkel** — CIO, Broan-NuTone
- **Mark Cribb** — Manager of AI Solutions & Applications, Marcus Theatres

In 75 minutes, you go from the simplest possible machine-learning model to the architectural frontier — and you run the demos yourself.

---

## The notebooks

### Line Fitting — Watch a Model Learn From Data
*Used in Act 1. CPU-only, ~30 seconds to render.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mierkoles/demystifying-ai-may2026/blob/main/line_fitting_colab.ipynb)

A line redraws itself as data grows from 2 to 1,000 points (Phase 1), then gets tilted by anomalies — with a robust alternative algorithm sitting right beside it (Phase 2). Five minutes of pixels that make "training" feel mechanical instead of magical.

### nanoGPT — Train a Transformer From Scratch in ~10 Minutes
*Used in Act 3. Needs free T4 GPU runtime.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mierkoles/demystifying-ai-may2026/blob/main/nanogpt_colab.ipynb)

A ~10-million-parameter character-level transformer trained on Mark Twain's *Tom Sawyer* and *Huckleberry Finn*. Watch the loss fall from random to coherent Twain-style prose. The procedure is the same one that built GPT-4 — 200,000× smaller, four orders of magnitude less data, same procedure.

**Important:** before running, set `Runtime → Change runtime type → T4 GPU → Save`.

---

## How to use

1. Click the **Open in Colab** badge above for whichever notebook
2. Read the welcome cell at the top — it explains what notebooks and Colab are if you've never used either
3. Click `Runtime → Run all` and watch the output

You don't need to read or understand any of the code. Every block is heavily commented for the curious, but the point of each demo is to *watch* the model do its thing.

---

## License

MIT for the demo code. The notebooks pull data from Project Gutenberg (public domain) and a Mark Twain corpus mirrored from Project Gutenberg.

---

*The talk slides and supporting materials are not in this repository — these notebooks are the hands-on artifacts only.*
