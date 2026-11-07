# Agent ticket workflow

[Index](INDEX.md) · [Profile](../docs/endpoint-profile.md) · [Specification](../specification/INDEX.md)

Each `PCIE-NNN.md` is both a work package and its authoritative status record. The YAML-compatible front matter uses JSON values for lists and nullable/string fields so the standard-library CLI needs no YAML dependency. Descriptions include source references, behavior, deliverables, pyuvm tests, ngspice applicability, acceptance criteria and evidence. This backlog plans implementation; unchecked items are not completed functionality.

Start with `python3 tools/tickets.py ready`. Initially PCIE-001 and PCIE-002 are independent entry points. Digital interface work becomes ready after PCIE-001. The selected target is [Tang Nano 20K](../docs/hardware-target.md); board revision, pin mapping, fit and full-duplex feasibility remain to be established. PCIE-041 records resource/timing fit. On documented inability to fit after optimization, the user permits a board-independent core with GW2AR I/O specifications retained for ngspice modeling. PCIE-040/044 are conditional hardware tickets and may receive reviewed not-applicable dispositions on that route; never report their unperformed hardware tests as passing. Digital and electrical-model verification still apply.

Before implementation, an agent must:

1. Read repository AGENTS.md, the profile, the whole ticket, its source files and prerequisite evidence. Use a unique agent ID and select one unowned ticket whose dependencies are `done`.
2. Ensure the planning files are tracked in Git, synchronize the authoritative checkout and preserve unrelated changes. A maintainer must first commit this generated planning baseline; the claim tool intentionally refuses untracked ticket files. It does not commit the user's existing files.
3. On `main`, run `python3 tools/tickets.py claim PCIE-010 --agent agent-name` using the selected ID. The command signs `owner`, `claimed_at`, `base_commit` and claim history, sets `active`, commits **only that ticket file** on `main`, then creates/switches to `ticket/pcie-010/agent-name`. It refuses to run off `main`, with tracked changes, or when the branch already exists, and rolls back the signature if the commit fails. Do not claim PCIE-010 before its dependencies are done; it is a syntax example.
4. Push `main` immediately so every checkout sees the claim before another agent picks work. Never use `git add .` to include unrelated user files. Agents in separate clones must pull `main` before claiming; the local lock cannot coordinate separate clones. Do not concurrently switch branches in one worktree; use separate worktrees and run claims from the worktree that has `main` checked out. A shared Git-common-directory lock serializes claim operations within one repository, including its worktrees.
5. Implement only the claimed scope, using a branch based on prerequisite changes. Add source-cited atomic requirement dispositions and test links. Do not regenerate initial ticket files once lifecycle work begins. If a shared-file conflict or missing prerequisite appears, record it and coordinate instead of silently expanding scope.

States are `todo → active → review → done`. Use `blocked` with the exact blocker, attempted work and next action when progress requires missing input; retain owner/branch. Resume as `active` after resolving it. `deferred` is allowed only for optional functionality with an explicit applicability decision and review; it cannot satisfy a mandatory dependency. A conditional ticket can be `done` after an accepted omit decision and passing absence tests. All baseline tickets are required for project completion; board-independent digital completion is the milestone through PCIE-042 and its prerequisites (including the reference models in PCIE-047/048), excluding PCIE-040 and hardware-dependent portions of PCIE-041. Initial L0 bring-up is PCIE-015, not endpoint completion.

To hand off, update `Evidence and handoff` with implementation paths, actual commands, tool versions, seeds, expected/observed results, requirement IDs, coverage, numerical electrical margins where applicable, remaining limitations and a precise next action. Append signed UTC history for every status/owner change. Keep ownership on handoff until a named replacement signs. Never claim another owner's ticket or erase claim history. Reassignment requires explicit coordination, an appended transfer record, a new owner signature and its own branch.

Before `review`, all applicable acceptance boxes must be checked with evidence, relevant checks must pass, and code changes must run `graphify update .`. Before `done`, a reviewer must verify requirements, results and integration with dependencies and sign the review in history. **`done` means reviewed and merged into `main`**: merge the ticket branch with its final `done` status and history into `main` and push. `tools/tickets.py ready` reads statuses from the current checkout, so run it on an up-to-date `main`; a `done` status that exists only on a ticket branch does not unblock dependents. The implementing agent does not call a task verified because files merely exist. Unavailable tools, board details or companion specifications remain explicit blockers; they do not become passing checks.

Useful commands:

```sh
python3 tools/tickets.py list
python3 tools/tickets.py ready
python3 tools/tickets.py check
python3 tools/deconstruct_spec.py --check
```

Maintain statuses and evidence directly in Markdown; the CLI supplies listing, validation and exclusive claiming. It never fabricates test evidence or automatically marks work done.
