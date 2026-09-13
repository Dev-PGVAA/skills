# Documentation lookup

## Resolve the correct package and version

Inspect local manifests and lockfiles when answering a project question. Record the package name, installed version, runtime, and the API uncertainty. Resolve once with a focused query:

```bash
ctx7 library nextjs "app router request cookies" --json
```

The query is optional in current upstream CLI, but useful for disambiguation; installed help takes precedence. A library ID already provided by the user or verified in this session can be reused. Choose the actual publisher and product before considering snippet counts or scores. Those scores rank retrieval; they do not prove authority or compatibility.

Use a version listed by the resolver when it matches the requested version. Do not silently substitute “closest” or latest documentation across a breaking version. If no exact version is indexed, retrieve the relevant official versioned docs or local types/source and explain the gap.

## Query a focused question

```bash
ctx7 docs /vercel/next.js "How are request cookies read in the app router?" --json
```

One question per distinct uncertainty usually gives better evidence. Query interacting features together when their interaction is the issue. Inspect JSON shape before scripting extraction; missing/empty content is not a successful answer even if the command exits zero.

Start with a resolve and one docs query, refine only if a material question remains. Avoid repeating identical requests. On rate limits or server errors, respect retry guidance, use a bounded retry, then fall back to official docs/local source. Do not settle for an unsupported claim merely because a call budget was reached.

## Apply and attribute

Compare examples with installed types and surrounding application conventions. A snippet may omit cleanup, validation, or production setup; retain the needed contract rather than copying blindly. Test the application change using its normal harness when implementation is requested.

Return the concrete API answer, target version, and direct documentation links carried by the retrieved material. If no source URL is returned, say the answer came from Context7 indexing and use official docs to establish precise attribution when needed. Never fabricate a link or a tested result.

## Authoritative references

- [CLI usage](https://github.com/upstash/context7/tree/master/packages/cli)
- [CLI docs command implementation](https://github.com/upstash/context7/blob/master/packages/cli/src/commands/docs.ts)

Checked 2026-09-12. Commands and indexed coverage can change; local help and current official documentation control execution.
