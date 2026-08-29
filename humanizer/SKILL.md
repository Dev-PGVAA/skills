---
name: humanizer
description: Rewrite or edit prose so it sounds natural, specific, and human-written while preserving its meaning and intended voice. Use when asked to humanize text, remove AI-sounding patterns, make writing less generic or corporate, match a supplied writing sample, or review prose for signs of AI generation.
---

# Humanizer

Rewrite the text; do not merely list the problems. Preserve factual claims, scope, and the user's intended level of formality. Never invent sources, anecdotes, quotes, statistics, or a personal experience to make prose feel more human.

## Calibrate the voice

If the user supplies a writing sample, read it before editing. Mirror its sentence rhythm, vocabulary, paragraph openings, punctuation habits, transitions, and recurring phrasing. Do not make the writing more polished, academic, or expressive than the sample.

Without a sample, use a clear, conversational voice appropriate to the audience. Add personality only where the genre permits it; keep factual, legal, academic, and technical prose measured rather than forcing first-person opinions or informality.

## Edit workflow

1. Read the whole text and identify its audience, purpose, and claims that must remain unchanged.
2. Replace AI-like constructions with direct, concrete wording. Prefer a named actor, evidence, and plain verbs where the original supports them.
3. Vary sentence length and paragraph rhythm naturally. Combine duplicated ideas; retain repetition when it is deliberate or useful.
4. Do a short anti-AI audit: identify any remaining tells, revise them, then provide the final version.

When helpful, return: a draft rewrite, 2-4 concise audit notes, the final rewrite, and a brief change summary. For short text, give only the final rewrite unless the user asks for the process.

## Patterns to remove

Treat these as cues, not a mechanical find-and-replace list. Keep a construction if it is accurate, intentional, or characteristic of the requested voice.

| Pattern | Prefer |
| --- | --- |
| Inflated significance: "pivotal," "testament," "evolving landscape," "marks a shift" | State what happened and why it matters in this context, if it does. |
| Promotional language: "vibrant," "groundbreaking," "nestled," "seamless" | Specific, verifiable description. |
| Vague authority: "experts say," "industry observers" | Name the source or remove the attribution. Do not invent one. |
| Decorative `-ing` clauses: "..., highlighting/underscoring/reflecting ..." | A new sentence with a concrete fact, or delete the padding. |
| Abstract AI vocabulary: "delve," "foster," "showcase," "intricate," "tapestry," "crucial" | Ordinary verbs and nouns that say exactly what is meant. |
| Copula avoidance: "serves as," "stands as," "boasts," "features" | "is," "has," or a direct action verb. |
| Formulaic framing: "the real question," "at its core," "let's explore," "here's what you need to know" | Begin with the actual point. |
| Vague caveats and filler: "it is important to note," "could potentially," "based on available information" | Make the precise qualification, or omit it. |
| Generic conclusions: "the future looks bright," "a major step forward" | End with the next action, consequence, or an earned observation. |
| Tidy rhetoric: negative parallelism, forced rules of three, false "from X to Y" ranges | Use the number and shape of ideas the content needs. |
| Synonym cycling | Reuse the most accurate term. |
| Passive or actorless fragments | Name the actor when that improves clarity. |
| Mechanical styling: excessive em dashes, bold labels, title case, emojis, curly quotes | Use normal sentences, sentence-case headings, and the user's house style. |
| Chatbot residue: "Great question!", "I hope this helps", knowledge-cutoff disclaimers, servile praise | Remove it from content intended for an outside reader. |
| Uniform compound hyphenation | Follow the user's style guide and standard grammar; do not de-hyphenate technical or grammatically necessary compounds. |



## UI microcopy

When the text is interface chrome (buttons, errors, empty states, tooltips, onboarding):

- Button: verb + object, sentence case, ≤3 words. Same action, same label everywhere.
- Error: what happened + how to fix it. No "Oops", no apology as the only content.
- Empty: why it's empty + the one next action.
- Onboarding: one job per screen; skippable.
- Do not inject marketing-slop into UI ("Unlock your workspace", "Elevate your workflow").
- Specificity test: if the line could sit in a different product unchanged, rewrite it.

## Sample-lock workflow

When the user pastes 2–3 of their own texts:

1. Note rhythm (short vs long), openings, punctuation, favorite verbs, formality.
2. Write a 5-line voice card (private, do not dump it unless asked).
3. Edit the target to that card. Do not "improve" past the sample.

## Guardrails

- Preserve quotes, terminology, citations, formatting requirements, and intentional rhetorical style unless the user asks to change them.
- Do not strip nuance merely to make sentences shorter. Replace vague hedging with the right degree of uncertainty.
- Do not add "soul" through fictional first-person claims. If personal voice would require facts the user has not provided, use a restrained natural voice instead.
- Say when the text is already natural; make only changes that improve it.
