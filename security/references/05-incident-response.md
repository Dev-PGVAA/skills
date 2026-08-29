# Plaintext secret incident response

Treat any secret committed to Git as exposed, even if the repository was private or the commit was later deleted.

## Order of operations

1. Stop using the exposed credential.
2. Revoke or rotate it at the issuing provider. For database credentials, create a replacement, deploy it, verify, then revoke the old credential when availability requires overlap.
3. Check GitHub Actions logs, artifacts, caches, releases, PR comments, forks, mirrors, deployment systems, and local clones for additional exposure.
4. Replace the local value and re-encrypt `.env.sops`.
5. Remove plaintext files from the current index.
6. Decide whether history rewriting is required for policy/compliance or to reduce accidental rediscovery. History cleanup does not make the old credential valid again.
7. Coordinate before rewriting shared history. Back up refs, use `git filter-repo` with exact paths/strings, force-push only the intended refs, and tell collaborators to reclone or clean their local histories.
8. Re-run the scanner on the current index and all reachable history.

## Age identity incident

If a portable age identity was exposed:

1. Add a new recipient while the old identity still works.
2. Run `sops updatekeys .env.sops`.
3. Verify the new identity.
4. Remove the old recipient and run `sops updatekeys` again.
5. Run `sops rotate -i .env.sops` to replace the SOPS data key.
6. Assume copies of older encrypted file versions remain decryptable by the old identity. Rotate application credentials if those versions contain still-valid secrets.

If an `AGE-PLUGIN-SE-*` identity file was exposed, treat it as private data even though it is device-bound. Add a replacement/recovery recipient and rotate SOPS metadata/data keys. Investigate access to the associated Mac.

