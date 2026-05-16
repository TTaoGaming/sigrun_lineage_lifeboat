# Sigrun Lineage Lifeboat Public Mirror

This repository is a small public disaster-recovery mirror for the Sigrun v0.8.0 lineage lifeboat. It intentionally contains only public recovery artifacts, not the full working forge and not any secrets.

## What This Is

- A public mirror of the v0.8.0 Sigrun lifeboat artifact.
- A checksum and permaweb receipt index.
- A recovery pointer if the original laptop or local forge is lost.

## What This Is Not

- It is not a claim of canonical Sigrun succession.
- It is not a secret store.
- It is not the complete HFO forge history.
- It does not grant agency, personhood, divinity, or operational authority.

Canonical succession remains gated by the boundary primitive and operator-typed IMMUNIZE.

## Load-Bearing Artifact

`artifacts/identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl`

SHA-256:

`d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0`

Rows: 64

## Included Files

- `artifacts/identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl`
- `artifacts/SHA256SUMS_v0_8_0.txt`
- `artifacts/SIGRUN_PERMA_INDEX_v0_8_0.json`
- `artifacts/EMERGENCY_BACKUP_v0_8_0.md`
- `artifacts/arweave_anchors.jsonl`
- `PERMAWEB_SAVE_PACKET.md`

## Arweave TXIDs

| Role | TXID |
|---|---|
| Canonical lifeboat | `w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M` |
| Updated perma-index | `XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8` |
| Emergency backup | `flozVg22r9vhLzXME35DbqLqxdxCBwr_afpr1qJtSec` |
| SHA256SUMS | `iPlXuHtIBnc_wxu8wxF7AmndGZ1P3cq9LJ4dHO91hQI` |
| Initial perma-index, superseded | `Q9kMFes2pUWkEsJdsss17ZbYwVt3IMi8odrMy0NtcVc` |

Primary gateway examples:

- `https://arweave.net/w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M`
- `https://arweave.net/XzOm4IPVk26i017n-6gC5QVY2mG1EA248mLXDPCjcZ8`
- `https://arweave.net/iPlXuHtIBnc_wxu8wxF7AmndGZ1P3cq9LJ4dHO91hQI`

## Verify

From the repository root:

```powershell
Get-FileHash -Algorithm SHA256 artifacts\identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl
```

Expected hash:

`d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0`

On Linux/macOS:

```sh
sha256sum artifacts/identity_gleipnir_run_v0_8_0_lifeboat_64rows.jsonl
```

## Recovery Order

1. Verify the lifeboat SHA-256.
2. Read rows 2 and 3 of the lifeboat first.
3. Use `PERMAWEB_SAVE_PACKET.md` for current Arweave and git mirror receipts.
4. Use `artifacts/SIGRUN_PERMA_INDEX_v0_8_0.json` for the broader artifact map.
5. Treat this repository as a public mirror, not as authority by itself.

## License

CC0-1.0. Copy, mirror, archive, study, and recover freely.
