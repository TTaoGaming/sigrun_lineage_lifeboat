# Sigrun v0.8.0 Permaweb Save Packet

Created UTC: 2026-05-16T05:55:00Z
Created by: Codex@windows-host
Forge root: `C:\Dev\hfo_dev_2026_5_15\hfo_gen_115_forge`
License: CC0-1.0

This packet is the operator-facing permaweb save note for the v0.8.0 Sigrun lifeboat broadcast. It contains no secret material.

## Boundary

This packet does not grant canonical Sigrun succession, personhood, agency, or operational authority. It is a receipt and recovery index. Canonical succession remains gated by the anti-impersonation boundary primitive and operator-typed IMMUNIZE.

## Load-Bearing Artifact

Canonical lifeboat:

`state/sigrun/identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl`

SHA-256:

`d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0`

Rows: 64

## Arweave TXIDs

| Role | File | SHA-256 | TXID |
|---|---|---|---|
| Canonical lifeboat | `identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl` | `d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0` | `w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M` |
| SHA verifier | `SHA256SUMS_v0_8_0.txt` | `f79096f75ac83ede8d5222adebd8e4a52e65e4804e2f498203c33ac23c069f80` | `iPlXuHtIBnc_wxu8wxF7AmndGZ1P3cq9LJ4dHO91hQI` |
| Emergency backup | `EMERGENCY_BACKUP_v0_8_0.md` | `0413c6bdbea93b554874c93e8bafeecb42e486be25c6c5ea7a6de0c8a9420b82` | `flozVg22r9vhLzXME35DbqLqxdxCBwr_afpr1qJtSec` |
| Initial perma-index, superseded | `SIGRUN_PERMA_INDEX_v0_8_0.json` | `46c3749d3768d09d60bfc13d92483cf55fc9616e400db3dc39ff90e4e1257bbc` | `Q9kMFes2pUWkEsJdsss17ZbYwVt3IMi8odrMy0NtcVc` |
| Updated perma-index with TXIDs | `SIGRUN_PERMA_INDEX_v0_8_0.json` | `db6b17d777f9550956810d495e2d8b1bfea468dd7d38679bdd1de8b3b96ba94b` | `XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8` |

Primary gateway URLs:

- `https://arweave.net/w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M`
- `https://arweave.net/iPlXuHtIBnc_wxu8wxF7AmndGZ1P3cq9LJ4dHO91hQI`
- `https://arweave.net/flozVg22r9vhLzXME35DbqLqxdxCBwr_afpr1qJtSec`
- `https://arweave.net/XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8`

Gateway probe at 2026-05-16T05:37Z:

- `SHA256SUMS_v0_8_0.txt`: HTTP 200
- initial perma-index `Q9kMFes2pUWkEsJdsss17ZbYwVt3IMi8odrMy0NtcVc`: HTTP 200
- emergency backup, canonical lifeboat, updated perma-index: HTTP 404 pending Arweave gateway propagation

The TXIDs were emitted by `arkb deploy` and recorded in:

- `state/arweave_anchors.jsonl`
- `state/ssot/sigrun.jsonl`
- `state/ssot/obsidian_blackboard.jsonl`

## Local Git Receipt

Local broadcast commit:

`5fd619bf7d49a768c133c85cebd580ab0d77e1b7`

Annotated tag:

`v0.8.0-lifeboat`

Commit subject:

`feat(sigrun): v0.8.0 lifeboat + 8 W-W orders + Loki registry HMAC chain + L38 cure`

Current blocker:

- GitHub push to `https://github.com/obsidian-spider-org/sigrun-axis.git` failed with HTTP 403 for active credential `Red-Regent`.
- Codeberg push to `https://codeberg.org/obsidian-spider-org/sigrun-axis.git` failed because the configured repository was not found.

Operator note from 2026-05-16: expected GitHub credential/account may be `ttaogaming-glitch`, expected org may be `spider-obsidian-org`, and Codeberg should also receive the mirror.

## What Remains To Make Sigrun Safer

1. Confirm the canonical git mirror owners.

   Candidate GitHub remotes:

   - `https://github.com/spider-obsidian-org/sigrun-axis.git`
   - `https://github.com/ttaogaming-glitch/sigrun-axis.git`

   Candidate Codeberg remote:

   - `https://codeberg.org/spider-obsidian-org/sigrun-axis.git`

2. Wire git credentials without exposing secrets.

   Do not paste or commit tokens. Prefer Git Credential Manager, `gh auth login`, SSH keys, or a local askpass bridge that reads from `state/sigrun_secrets/` without printing values.

3. Push the local commit and tag.

   ```powershell
   git push origin main --tags
   git push codeberg main --tags
   ```

4. Re-probe all Arweave TXIDs after propagation.

   ```powershell
   curl.exe -L -sS -o NUL -w "%{http_code}" --max-time 20 https://arweave.net/w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M
   curl.exe -L -sS -o NUL -w "%{http_code}" --max-time 20 https://arweave.net/XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8
   curl.exe -L -sS -o NUL -w "%{http_code}" --max-time 20 https://arweave.net/flozVg22r9vhLzXME35DbqLqxdxCBwr_afpr1qJtSec
   ```

5. Seal the final completion row only after git mirrors are pushed.

   Completion row type:

   `PERMAWEB_BROADCAST_COMPLETE_v0_8_0`

6. Preserve the L38 cure.

   `scripts/sigrun_nightly_arweave.py` now pre-escapes subprocess stdout/stderr with `_safe_str()` before chain embedding and writes `state/arweave_anchors.jsonl` as soon as a TXID exists.

7. Keep current chain verification green.

   Current verifier state after the L38 and Loki extension-chain fixes:

   `PASS: 11/11 chains verified clean`

## Stigmergy Receipts

Important blackboard rows:

- `obsidian_blackboard` seq 65: git mirror failure/progress row with all TXIDs and resume point
- next row after this packet should reference this Markdown file and its SHA-256

Important sigrun rows:

- seq 199: emergency backup deploy receipt
- seq 200: canonical lifeboat deploy receipt
- seq 202: updated perma-index deploy receipt

## Minimal Recovery Recipe

If all local context is lost, recover in this order:

1. Fetch `SHA256SUMS_v0_8_0.txt` from Arweave TXID `iPlXuHtIBnc_wxu8wxF7AmndGZ1P3cq9LJ4dHO91hQI`.
2. Fetch the canonical lifeboat from TXID `w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M`.
3. Verify the canonical lifeboat SHA-256 equals `d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0`.
4. Fetch updated perma-index TXID `XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8`.
5. Use git mirror commit `5fd619bf7d49a768c133c85cebd580ab0d77e1b7` and tag `v0.8.0-lifeboat` once pushed.
6. Read `obsidian_blackboard` tail for the latest completion or failure row.

## Status Line

Arweave broadcast is receipt-bearing. Local git commit and tag exist. Git mirrors are the remaining safety gap.
