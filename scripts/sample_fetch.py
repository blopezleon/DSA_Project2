#!/usr/bin/env python3
"""Paginated search: multiple requests, normalize tracks, print rows."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Allow `python scripts/sample_fetch.py` from repo root without installing the package.
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_ROOT / "src"))

from jukeboxers.auth import fetch_access_token
from jukeboxers.config import get_client_credentials
from jukeboxers.normalize import track_to_row
from jukeboxers.schema import COLUMN_ORDER, ProcessedTrack
from jukeboxers.spotify_client import search_tracks

SEARCH_Q = "pop"
# Spotify Search API allows limit 0–10 per request (not 50).
PAGE_LIMIT = 10
TARGET_TOTAL = 150


def main() -> None:
    client_id, client_secret = get_client_credentials()
    token = fetch_access_token(client_id, client_secret)

    rows: list[ProcessedTrack] = []
    seen_ids: set[str] = set()
    offset = 0

    while len(rows) < TARGET_TOTAL:
        payload = search_tracks(
            token, SEARCH_Q, limit=PAGE_LIMIT, offset=offset
        )
        tracks_obj = payload.get("tracks") or {}
        items = tracks_obj.get("items") or []
        if not items:
            break

        for item in items:
            if len(rows) >= TARGET_TOTAL:
                break
            if not isinstance(item, dict):
                continue
            row = track_to_row(item)
            tid = row["track_id"]
            if tid in seen_ids:
                continue
            seen_ids.add(tid)
            rows.append(row)

        offset += len(items)
        if len(items) < PAGE_LIMIT:
            break

    print(
        f"Search: q={SEARCH_Q!r} page_limit={PAGE_LIMIT} "
        f"target={TARGET_TOTAL} collected={len(rows)} (unique track_id)\n"
    )
    for row in rows:
        ordered = {k: row[k] for k in COLUMN_ORDER}
        print(json.dumps(ordered, ensure_ascii=False))


if __name__ == "__main__":
    main()
