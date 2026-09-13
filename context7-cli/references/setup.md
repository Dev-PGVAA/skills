# Configure Context7

Setup writes agent configuration and may initiate authentication. Perform it only within the requested project/global scope. Discover the available CLI version and `ctx7 setup --help`, then inspect existing target configuration without exposing credentials. Preserve unrelated MCP servers, settings, and skill files; back up files that will be replaced.

## Choose the actual target

Supported targets vary by version. Current upstream supports Codex, but do not assume an older installed CLI accepts the same flags. Typical shape after confirming help:

```bash
ctx7 setup --mcp --codex --project
```

Use global scope only when requested. CLI+Skills mode and MCP mode write different resources; select based on the user's request and available capabilities. Do not configure other editors because they are auto-detected. Do not use `--yes` to conceal an unresolved target or replacement decision.

## Authentication

Prefer the user's existing authentication or supported OAuth/hidden-input flow. `CONTEXT7_API_KEY` may be supplied through an existing secret environment. Do not paste keys into the command line, write literal keys in chat, or print config containing them. Avoid triggering login when anonymous docs access already satisfies the task.

Setup may generate credentials and write rules/skills as well as an MCP entry; inspect the actual result. Confirm that existing entries survive and test one harmless docs request when the new connection becomes available. A config file written successfully is not proof that the running host has loaded it; identify a required reload without claiming live success.

For removal, inspect `ctx7 remove --help` and the exact resources previously installed. Remove only the requested Context7 scope; do not erase the agent's entire config or unrelated skill directories.

[Official CLI setup and removal](https://github.com/upstash/context7/tree/master/packages/cli), checked 2026-09-12.
