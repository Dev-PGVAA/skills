# Legacy Context7 skill management

Upstream's `ctx7 skills` command family is deprecated and marked for removal in the next major release as inspected on 2026-09-12. Do not build a new general skill-management workflow around it. Use an available native skill installer/creator for ordinary installation or creation; this reference supports users who explicitly request ctx7 or maintain an older setup.

## Inspect before acting

Check the installed version and `ctx7 skills --help`. If unavailable, explain the compatibility issue and use the requested repository through an available installation method. Do not downgrade or install globally without task authorization.

When supported, read-only inspection typically includes:

```bash
ctx7 skills info /owner/repo
ctx7 skills list
```

Repository names are placeholders; substitute the user's actual source. Search/suggest commands may launch an interactive install flow, so do not treat their entire interaction as read-only.

## Install / remove safely

1. Resolve the exact source revision, selected skills, destination, and project/global scope.
2. Inspect skill instructions, scripts, external dependencies, and symlink destinations. Registry scores or install counts do not establish safety.
3. Back up existing same-name skills before replacement. Do not follow symlinks into unrelated shared roots or remove bundled/system skills as collateral cleanup.
4. Run only supported flags for the intended target. Do not use `--all` unless the user requested every skill from that source.
5. Validate metadata, local references, scripts where applicable, and the on-disk installed contents. Distinguish installed files from skills discovered by a still-running host.

## Generate

If an older version offers `skills generate`, inspect current authentication, privacy, cost, and limits at execution time. Do not assert fixed free/pro quotas. Generated skills need review and validation before installation; remote generation does not bypass the user's scope or content-sharing constraints.

[Upstream skill command and deprecation notice](https://github.com/upstash/context7/blob/master/packages/cli/src/commands/skill.ts).
