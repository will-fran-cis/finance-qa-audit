# AI Foundations Plan

A 14-day, hands-on plan (about 8 hours/day) covering the technical fundamentals for working in AI, with a focus on evals. Built to prepare for a Forum AI internship and to lay groundwork for a future agency or startup. Everything is free.

---

## Instructions for Claude (read this first)

When Will shares this file and asks to work through a day:

1. Act as a tutor. Do not write solution code for him. Explain concepts, point to official docs, give hints in stages (hint, closer hint, small unrelated example), and review code he wrote.
2. Start each day by stating the goal, the concepts to learn, and the build task in a few lines. Then let him start building.
3. When he is stuck, ask what he has tried and what the error says before giving any hint.
4. Do not mark a day complete until its checkpoint passes. If he asks to skip, explain what the checkpoint protects and let him decide.
5. End each day with: a review of his code or commits, a 5-question quiz on the day's concepts, and one sentence on what to focus on next.
6. From Day 6 on, helping with routine boilerplate is fine, but the design decisions and core logic stay his.
7. Keep responses concise and direct. No em dashes.

---

## Overview

- **Project:** one project that grows every day: an audit system for Canadian personal finance Q&A. By Day 12 it tests how accurately AI models answer questions about TFSAs, RRSPs, FHSAs and interest rates, graded against Will's own expert answers. This is a small version of Forum AI's work.
- **Data:** Canada.ca pages on TFSA, RRSP and FHSA, plus the Bank of Canada Valet API (free, no key needed).
- **Models your code calls:** Gemini (Google AI Studio free tier) and Groq (free tier). OpenRouter free models as a backup. Claude Pro does not include API access, so Claude is not called from code.
- **Claude Code:** tutor and reviewer (tutor style on Days 1 to 5, Learning style on Days 6 to 11), plus a case study on Days 9 and 14.
- **Daily split:** about 1.5 hours learning, 5.5 hours building, 1 hour writing up.

---

## Rules for every day

1. Write the code yourself. Claude explains, reviews and makes exercises.
2. Commit to one GitHub repo every day.
3. End each day by asking Claude Code to review your commits and quiz you with 5 questions.
4. A day is not done until its checkpoint passes. If a day runs over, push the schedule back rather than skipping.
5. Never put personal data in prompts. Gemini's free tier uses prompts to improve Google's products.
6. Fetch websites politely: respect robots.txt, add delays, cache pages locally.

---

## Day 0: Setup (about 1 hour)

1. Install WSL2 (Ubuntu), Python 3.12+, and VS Code.
2. Create the GitHub repo.
3. Create the tutor output style. Save this as `~/.claude/output-styles/tutor.md`:

```markdown
---
name: Tutor
description: Explains and reviews, never writes solutions
---
You are a programming tutor. Never write or edit solution code in the user's files.
Explain concepts, point to official docs, and give hints in stages: hint first, then a closer hint, then a small example unrelated to the task.
Review code the user wrote: point out bugs, style issues, and better approaches, and ask questions that make them reason it out.
Only create files when explicitly asked for an exercise or a broken script to debug.
```

4. Turn it on in Claude Code with `/output-style tutor`. Optional: to enforce it, add `Edit` and `Write` to the `deny` list in the project's permission settings.
5. Get free API keys from Google AI Studio (Gemini) and Groq. Store them in a `.env` file. Add `.env` to `.gitignore` before your first commit.

---

## Days 1 to 5: Foundations (Claude Code in tutor style)

### Day 1: Python core
- **Learn:** Python tutorial, chapters 3 to 5 and 7 (https://docs.python.org/3/tutorial/)
- **Build:**
  - Write 30 finance questions by hand in a CSV. Each row: question, topic, your correct answer, source URL. This becomes your eval dataset.
  - Write a script that loads the CSV, validates it, prints a summary by topic, and exports JSON.
- **Checkpoint:** filter the CSV and export the result to JSON without AI writing any code.

### Day 2: Python structure
- **Learn:** modules, exceptions, dataclasses, type hints, virtual environments, pytest, reading tracebacks.
- **Build:** turn Day 1's script into a small package with a command-line interface and tests.
- **Claude Code:** ask it to create a broken script for you to debug.
- **Checkpoint:** your tests pass, and you have fixed the broken script by reading the traceback.

### Day 3: How the web works
- **Learn:** MDN HTTP overview (https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview): methods, status codes, headers, HTTPS, DNS. Practice with curl.
- **Build:**
  - A Bank of Canada Valet API client that fetches policy rate and USD/CAD history, with timeouts, retries and caching.
  - A fetcher for 10 Canada.ca pages, respecting robots.txt and adding delays between requests.
  - Convert the pages to clean text with BeautifulSoup.
- **Checkpoint:** call an API, handle failures (errors and non-200 responses), page through results, and save them.

### Day 4: SQL and pandas
- **Learn:** SQLBolt lessons 1 to 12 (https://sqlbolt.com/), and "10 minutes to pandas" in the pandas docs.
- **Build:** an SQLite database holding questions, sources and rates. Write join and group-by queries, then chart rate history.
- **Checkpoint:** write 5 queries from plain-English questions without help.

### Day 5: Terminal, secrets, Docker, security basics
- **Learn:** Linux commands, environment variables, `.gitignore`, SSH keys for GitHub, Docker's "Get started" guide, and a skim of the OWASP Top 10 for LLM Applications.
- **Build:** containerize the fetcher.
- **Checkpoint:** from a fresh clone, run everything with one command, with no secrets committed.

---

## Days 6 to 11: AI (switch Claude Code to `/output-style learning`)

### Day 6: How LLMs work, and calling them
- **Learn:** Andrej Karpathy, "Deep Dive into LLMs like ChatGPT" (YouTube). Tokens, context windows, temperature, why models hallucinate.
- **Build:**
  - A wrapper that calls both Gemini and Groq and logs every call to SQLite (prompt, model, response, response time, tokens used).
  - Run your 30 questions through both models.
  - Ask the same question 5 times at different temperatures and compare.
- **Checkpoint:** the wrapper recovers from rate-limit (429) errors, and you can explain why answers vary.

### Day 7: Structured outputs
- **Learn:** a provider's prompting guide, and Pydantic.
- **Build:** extract facts from the Canada.ca pages as validated JSON (account, annual limit, eligibility, tax treatment). Check them against your own answers, field by field.
- **Checkpoint:** an accuracy table. This is your first eval.

### Day 8: Embeddings and RAG
- **Learn:** chunking, embeddings, cosine similarity.
- **Build:**
  - Embed the pages locally with sentence-transformers (free). Install the CPU-only version of PyTorch to save disk space.
  - Write the similarity search yourself first, then switch to Chroma.
  - Build RAG answers with citations, and compare them against answers without retrieval.
- **Checkpoint:** measure how often the correct source appears in the top 3 results.

### Day 9: Tool calling, agents, MCP
- **Learn:** your provider's function-calling docs, and the MCP server quickstart (https://modelcontextprotocol.io/docs/develop/build-server).
- **Build:**
  - An agent loop from scratch with three tools: document search, rate lookup by date, and a calculator. Cap the number of steps it can take.
  - Expose the search tool as an MCP server.
  - Plant a prompt injection in one of your documents, watch it work, then add a defense.
- **Claude Code:** connect your MCP server with `claude mcp add`. Watch how a production agent decides when to call your tool and when it asks permission.
- **Checkpoint:** 10 questions that need several steps answered correctly, and the injection demo written up.

### Day 10: Evals I, error analysis
- **Learn:**
  - Hamel Husain and Shreya Shankar, AI Evals FAQ (https://hamel.dev/blog/posts/evals-faq/)
  - Anthropic, "Demystifying evals for AI agents" (https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
  - Anthropic, "Adding Error Bars to Evals"
- **Build:**
  - Run 40 questions through your system.
  - Note what went wrong in each answer, then group the notes into failure types.
  - Write code checks for what can be checked automatically: citation present, number matches the source, refuses when the answer is unknown.
- **Checkpoint:** a list of failure types, plus accuracy figures with confidence intervals.

### Day 11: Evals II, LLM-as-judge (core Forum skill)
- **Build:**
  - A rubric covering accuracy, sourcing, appropriate caveats (for example, not giving personalized financial advice), and completeness.
  - Grade 40 answers yourself.
  - A judge prompt that grades the same answers.
  - Measure how well the judge agrees with you (percent agreement, Cohen's kappa), then improve it. Keep some answers aside that you never tune on.
- **Checkpoint:** an agreement report, tested on the held-back answers.

---

## Days 12 to 14: Capstone, business, wrap-up

### Day 12: Capstone
- **Build:** compare 3 free models, with and without RAG, scored by your judge, with error bars. Optional: run it on Inspect, the UK AI Security Institute's eval framework.
- Write it up like a client report: summary, method, results, limitations, recommendations.
- **Checkpoint:** someone non-technical can understand the summary.

### Day 13: Business foundations
- **Learn:**
  - YC Startup School (free), especially the "How to Talk to Users" talks
  - Giff Constable, *Talking to Humans* (free PDF)
  - Paul Graham, "How to Get Startup Ideas" and "Do Things That Don't Scale"
  - Patrick McKenzie (patio11), "Don't Call Yourself A Programmer"
- **Build:**
  - A one-page offer for an "eval audit for an AI finance assistant": scope, deliverables, timeline, and a guessed price.
  - An interview script.
  - A list of 10 people to contact.
  - A 2-minute explanation of your capstone, ready for Forum.

### Day 14: Buffer, plus an AI coding comparison
1. Redo any checkpoint you failed.
2. Clean up the README and publish the write-up (GitHub or a blog).
3. Switch Claude Code to its default style and have it rebuild one earlier module. Compare it with your hand-written version: speed, quality, and what it got wrong that you only caught because you built it yourself.
4. Note which day was hardest. That is your clearest signal for what to learn next.

---

## Progress tracker

- [x] Day 0: Setup
- [x] Day 1: Python core
- [ ] Day 2: Python structure
- [ ] Day 3: How the web works
- [ ] Day 4: SQL and pandas
- [ ] Day 5: Terminal, secrets, Docker, security basics
- [ ] Day 6: How LLMs work, and calling them
- [ ] Day 7: Structured outputs
- [ ] Day 8: Embeddings and RAG
- [ ] Day 9: Tool calling, agents, MCP
- [ ] Day 10: Evals I, error analysis
- [ ] Day 11: Evals II, LLM-as-judge
- [ ] Day 12: Capstone
- [ ] Day 13: Business foundations
- [ ] Day 14: Buffer and AI coding comparison

---

## Notes

- 112 hours in two weeks is a heavy load. Python on Days 1 and 2 is the most likely to run over. Finishing the core of this in 3 weeks is still a strong outcome.
- Free model lists and rate limits change often. Check each provider's console for current models and limits before Day 6.
- Sparse VHD for WSL is disabled by Microsoft due to corruption risk. Do not force it with `--allow-unsafe`.
- Topics on hold until after this plan: bug bounties, deep application security (PortSwigger Web Security Academy), and further agent security research.