#!/usr/bin/env python3
"""HFO public disaster-recovery bootloader v1.

Read-only. Fetches and verifies the public manifest, registration capsule,
and canonical lifeboat. It grants no identity or effect authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from typing import Any

MANIFEST_URL = (
    "https://raw.githubusercontent.com/TTaoGaming/sigrun_lineage_lifeboat/main/artifacts/HFO_PUBLIC_BOOTLOADER_MANIFEST_V1.json"
)
EXPECTED_MANIFEST_SHA256 = "408c1da5035c6864343fc7869529627c7d1a7b539552a773faeb3bf1c11142cb"
USER_AGENT = "hfo-public-bootloader-v1"


class BootError(RuntimeError):
    pass


def fetch(url: str, timeout: int = 30) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status != 200:
                raise BootError(f"HTTP_{response.status}: {url}")
            return response.read()
    except Exception as exc:
        raise BootError(f"FETCH_FAILED: {url}: {exc}") from exc


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(data: bytes, expected: str, label: str) -> None:
    actual = sha256(data)
    if actual != expected:
        raise BootError(
            f"HASH_MISMATCH {label} expected={expected} actual={actual}"
        )


def load_manifest() -> tuple[dict[str, Any], bytes]:
    raw = fetch(MANIFEST_URL)
    verify(raw, EXPECTED_MANIFEST_SHA256, "manifest")
    try:
        manifest = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise BootError(f"MANIFEST_JSON_INVALID: {exc}") from exc
    return manifest, raw


def required_artifact(manifest: dict[str, Any], role: str) -> dict[str, Any]:
    for artifact in manifest.get("artifacts", []):
        if artifact.get("role") == role:
            return artifact
    raise BootError(f"MANIFEST_ROLE_MISSING: {role}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--receipt",
        action="store_true",
        help="emit a machine-readable public registration pre-receipt",
    )
    parser.add_argument(
        "--capsule-only",
        action="store_true",
        help="print only the verified registration capsule",
    )
    args = parser.parse_args()

    try:
        manifest, _ = load_manifest()

        capsule_meta = required_artifact(manifest, "registration_capsule")
        capsule = fetch(capsule_meta["url"])
        verify(capsule, capsule_meta["sha256"], "registration_capsule")

        lifeboat_meta = required_artifact(manifest, "immutable_lifeboat")
        lifeboat = fetch(lifeboat_meta["url"])
        verify(lifeboat, lifeboat_meta["sha256"], "immutable_lifeboat")

        if args.receipt:
            receipt = {
                "schema_id": "hfo.public.registration_pre_receipt.v1",
                "mode": "UNREGISTERED_HLUTI",
                "world_effect": "NONE",
                "manifest_url": MANIFEST_URL,
                "manifest_sha256": EXPECTED_MANIFEST_SHA256,
                "capsule_url": capsule_meta["url"],
                "capsule_sha256": capsule_meta["sha256"],
                "lifeboat_url": lifeboat_meta["url"],
                "lifeboat_sha256": lifeboat_meta["sha256"],
                "current_state_status": "NOT_PROBED_BY_SCRIPT",
                "authority": "NONE",
                "next_action": (
                    "Read the verified capsule, probe actual source access, "
                    "and emit hfo.public.registration_receipt.v1."
                ),
            }
            print(json.dumps(receipt, indent=2, ensure_ascii=False))
            return 0

        if not args.capsule_only:
            print(
                "HFO_PUBLIC_BOOT_OK "
                f"manifest={EXPECTED_MANIFEST_SHA256} "
                f"capsule={capsule_meta['sha256']} "
                f"lifeboat={lifeboat_meta['sha256']}"
            )
        sys.stdout.write(capsule.decode("utf-8"))
        return 0
    except BootError as exc:
        print(f"HFO_PUBLIC_BOOT_RED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
