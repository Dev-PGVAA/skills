# Part 1 — Link Weaver (live suggestions while writing)

Part of graph-surgeon. Works standalone.

## When to run

User is creating or editing a note and wants related links, “what should this connect to”, or automatic wikilink suggestions.

## Inputs (use what exists)

- Current note title + body (or the paragraph under the cursor).
- Optional: list/index of vault note titles (from a file tree, search index, or user paste).
- Optional: existing graph export or backlink list.

If the vault index is missing, say so and work from titles the user provided or from filenames in the open project. Do not hallucinate a 500-note library.

## Procedure

1. **Extract concepts** from the current note: entities, claims, projects, people, decisions, open questions.
2. **Match candidates** against the vault index:
   - exact / near title match
   - synonym and alias match
   - “this note answers a question that note asks” (complementary)
   - “same object, different angle” (needs a see-also, or may be a duplicate — flag)
3. **Score** each candidate: relevance × uniqueness of the connection (prefer non-obvious useful links over linking every keyword).
4. **Propose a short list** (default 5–12), never a dump.

## Output format

```markdown
## Link proposals for «[current note]»

### Outbound (add from this note)
- → [[Note A]] — reason (one line)
- → [[Note B]] — reason

### Inbound (add from other notes toward this one)
- [[Note C]] → this — where to insert / suggested sentence

### Maybe create
- [[New stub: …]] — only if the concept is load-bearing and no note exists

### Do not link
- [title] — why (noise, duplicate, or wrong level)
```

## Rules

- Prefer **one strong reason per link** over many weak keyword matches.
- If two notes are near-duplicates, propose **merge or distinguish**, not a mutual see-also band-aid.
- Respect the user’s link syntax (`[[Wiki]]`, `[text](path)`, block ids).
- If editing, show a **minimal diff**: exact lines to add, not a rewritten essay.
- When the note is still a stub (< ~50 words), suggest a **structure** (sections) before a long link list.
