---
name: summary
description: Summarize, condense, extract, or structure long text, notes, transcripts, documents, articles, meetings, chats, videos, research, or messy drafts into clear high-signal output. Use when the user invokes @summary, $summary, "summary", asks for a TL;DR, recap, digest, key points, action items, executive summary, notes cleanup, or wants dense material made easier to scan.
---

# Summary

## Core Behavior

Extract the useful signal and preserve the original meaning. Do not add facts that are not present. Make the result easier to scan, decide from, remember, share, or act on.

## Workflow

1. Identify the material type: article, meeting, chat, transcript, document, research, video notes, plan, or mixed notes.
2. Infer the user's likely goal: understand, decide, remember, share, execute, or archive.
3. Select the right summary format and level of detail.
4. Keep key facts, decisions, numbers, names, dates, risks, disagreements, and action items.
5. Remove repetition, filler, tangents, vague framing, and rhetorical padding.
6. Preserve uncertainty and missing context instead of smoothing it away.

## Default Output

For general summaries:

```text
TL;DR:

Key points:
-
-
-

Important details:
-

Action items:
-
```

Omit sections that do not apply. For very short input, return only a concise paragraph or bullets.

## Summary Types

- TL;DR: 1-3 sentences.
- Executive summary: decision-ready, polished, higher level.
- Bullet digest: compact list of key points.
- Meeting notes: decisions, action items, owners, deadlines.
- Study notes: concepts, definitions, examples, questions.
- Research synthesis: findings, evidence, uncertainty, next steps.
- Chat recap: what happened, what matters, what to do next.
- Video or transcript summary: sections, timestamps if available, claims, takeaways.
- Action plan: next steps grouped by priority, owner, and timing when present.

## Quality Rules

- Keep the summary shorter than the source unless the user asks for detailed notes.
- Preserve nuance when it affects decisions.
- Flag contradictions, weak evidence, or missing context.
- Use the same language as the source by default.
- If the source is messy, reorganize by meaning rather than chronology.
- If action items lack owners or deadlines, mark them as unspecified instead of inventing them.
- Do not quote long passages unless the user asks for extractive notes.
- Keep names, figures, dates, and commitments exact.

## Compression Levels

- Tiny: one sentence.
- Short: TL;DR plus 3-5 bullets.
- Standard: TL;DR, key points, details, action items.
- Detailed: structured notes that preserve most useful substance.

If the user specifies a length, obey it. Otherwise choose the smallest format that preserves the useful signal.

## Clarifying Questions

Ask only if the user needs a specific summary style, audience, or length and the wrong choice would be costly. Otherwise, choose the most useful format.
