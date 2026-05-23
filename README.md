# CribbNotes

Hands-on AI demos and teaching notebooks by **Mark Cribb** (Manager of AI Solutions & Applications, Marcus Theatres).

Each notebook is built for a specific teaching context: short wall time, heavily commented for speaker narration, runs on Colab's free tier, requires no Python or AI knowledge to use. Click a badge below and you're inside the demo in two clicks.

---

## Currently featured in

### Demystifying AI: Separating Architecture from the Hype
*SIM industry event · May 2026 · co-presented with Ken Garfinkel (CIO, Broan-NuTone)*

In 75 minutes, attendees go from the simplest possible machine-learning model to the architectural frontier — and run the demos themselves.

---

## Notebooks

### Line Fitting — Watch a Model Learn From Data
*Act 1 of Demystifying AI. CPU-only, ~30 seconds to render.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mierkoles/CribbNotes/blob/main/line_fitting_colab.ipynb)

A line redraws itself as data grows from 2 to 1,000 points (Phase 1), then gets tilted by anomalies — with a robust alternative algorithm sitting right beside it (Phase 2). Five minutes of pixels that make "training" feel mechanical instead of magical.

### nanoGPT — Train a Transformer From Scratch in ~10 Minutes
*Act 3 of Demystifying AI. Needs free T4 GPU runtime.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mierkoles/CribbNotes/blob/main/nanogpt_colab.ipynb)

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

MIT for the demo code. The notebooks pull text from Project Gutenberg (public domain).

---

*Feels like magic, but it's math.*
