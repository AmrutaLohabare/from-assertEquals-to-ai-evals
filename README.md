# From assertEquals() to AI Evals

> Same input. Same output. Ten years of my test cases are built on that one rule.
> Then I started learning to test AI.

I'm a Senior SDET with about 10 years of UI, API and performance testing. This repo is my public learning journal as I learn to test AI systems: LLMs, chatbots, RAG pipelines and agents.

For every session I publish:

- **Notes**: what I learned, what I tried, and what confused me
- **Assignments**: prompts, configs, test code and screenshots
- **A write-up** on [Medium](https://medium.com/@amrutalohabare) and a short post on LinkedIn

All assignments are done on open, public platforms and public AI tools. No work code or company systems are used here.

---

## Journey index

| Session | Topic | Key lesson | Notes | Write-up |
|------|-------|------------|-------|----------|
| 1 | What is AI/ML, from a tester's view | An LLM predicts what *sounds* right. It doesn't know what *is* right. | [week-01](./week-01-what-is-ai/) | [Medium](https://medium.com/@amrutalohabare/37fb43b62e14) |
| 2 | Tokens, probabilities and temperature | Temperature changes the words, not whether the bot follows its rules. | [session-02](./session-02-tokens-temperature/) | [Medium](https://medium.com/@amrutalohabare/tokens-set-the-cost-probability-picks-the-word-temperature-decides-the-risk-d87c197e9d50) |
| 3 | AI architecture: what we actually test | _coming soon_ | | |
| 4 | Prompt engineering fundamentals | _coming soon_ | | |
| 5 | Prompt testing: finding where prompts break | _coming soon_ | | |
| 6 | Structured outputs and output validation | _coming soon_ | | |
| 7 | promptfoo: setup, config and first eval | _coming soon_ | | |
| 8 | promptfoo: assertions and LLM-as-judge | _coming soon_ | | |
| 9 | Python foundations for AI testing | _coming soon_ | | |
| 10 | DeepEval: pytest for LLMs | _coming soon_ | | |
| 11 | Hallucination detection | _coming soon_ | | |
| 12 | RAG testing fundamentals | _coming soon_ | | |
| 13 | LLM API testing | _coming soon_ | | |
| 14 | Chatbot UI testing with Playwright | _coming soon_ | | |

---

## What I'm learning to test for

| Problem | What it looks like | How it's tested |
|---------|--------------------|-----------------|
| Hallucination | A confident, well-written, wrong answer | Grounding checks, hallucination metrics |
| Non-determinism | Same input, different output every run | Semantic checks instead of exact matches |
| Prompt injection | Users overriding instructions in plain English | Adversarial prompts, red teaming |

## Tools covered along the way

`promptfoo` · `DeepEval` · `pytest` · `Playwright` · `LangChain` · `OpenAI API`

---

## Follow along

- Medium: [@amrutalohabare](https://medium.com/@amrutalohabare), weekly posts on AI tools for QA engineers
- GitHub: [@AmrutaLohabare](https://github.com/AmrutaLohabare)

If you're a tester moving into AI, star the repo and follow along. Feedback and questions are welcome in Issues.
