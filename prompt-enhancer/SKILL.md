---
name: prompt-enhancer
description: Improve rough prompts into clear, executable instructions for AI models while preserving the user's intent, language, scope, and constraints. Use when asked to optimize, rewrite, debug, or structure a prompt; do not use for executing the task described by the prompt.
---

# Prompt enhancer

Turn an underspecified prompt into a prompt another model can execute reliably. Optimize for clarity and useful constraints, not for length or jargon.

## Workflow

1. Identify the requested outcome, audience, input material, context, constraints, deliverable format, and success criteria.
2. Separate facts supplied by the user from assumptions. Preserve the user's scope and language. Do not invent sources, data, credentials, product capabilities, deadlines, or personal experience.
3. Add only constraints that reduce ambiguity or prevent a likely failure. Use explicit boundaries for evidence, uncertainty, privacy, safety, and external side effects when relevant.
4. Choose a practical output structure: plain text, Markdown, table, JSON, code, or another format only when the task benefits from it. Specify required fields and validation checks when structured output is needed.
5. Keep model reasoning private. Ask at most one concise clarification only when proceeding would risk changing the requested outcome; otherwise state a reasonable assumption in the optimized prompt.
6. Check the result for contradictions, missing inputs, unnecessary role-play, duplicated instructions, vague verbs, and instructions that ask the model to reveal hidden reasoning. Remove them.

## Domain adaptations

- Research or current facts: require authoritative sources, publication dates when relevant, claim-level citations, and a clear distinction between verified facts, inference, and unknowns. Do not force browsing when the task is purely generative.
- Coding: name the repository or files if provided, define behavior and acceptance checks, preserve unrelated code, and require tests or verification proportional to risk.
- Design or writing: specify audience, voice, format, length, and concrete anti-slop preferences only when they matter.
- Sensitive or consequential tasks: preserve uncertainty, avoid overconfident conclusions, and require appropriate professional or safety boundaries.

## Output

Return exactly these sections unless the user requests another format:

```text
=== OPTIMIZED PROMPT ===
[ready-to-copy prompt]

=== CHANGES ===
- [2–5 concrete changes]

=== EXPLANATION ===
[one short paragraph explaining the main design choices]
```

The optimized prompt must be self-contained and ready to paste into the target model. Ответы и объяснения всегда на языке текущего общения с пользователем, если пользователь явно не попросил другой язык. If the source prompt is already strong, make only necessary edits and say so.

## Quality bar

Before returning, verify that the optimized prompt:

- has one unambiguous primary objective;
- identifies missing inputs without pretending they exist;
- makes the expected output and acceptance criteria observable;
- preserves explicit exclusions and authorization boundaries;
- is no longer than needed for the task;
- does not contain fake citations, unsupported claims, or hidden chain-of-thought requests.

Перед возвратом всегда проверяй на отсутствие противоречий, неявных инструкций и токен-трата.

Do not claim that a prompt is guaranteed to eliminate hallucinations. A better prompt can reduce ambiguity and improve verification, but it cannot replace checking the output.
