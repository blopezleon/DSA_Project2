#!/usr/bin/env python3
"""One search request, normalize tracks, print sample rows."""

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
from jukeboxers.schema import COLUMN_ORDER
from jukeboxers.spotify_client import search_tracks

# Fixed public search — small limit for a sample only.
SEARCH_Q = "year:2020"
SEARCH_LIMIT = 10


def main() -> None:
    client_id, client_secret = get_client_credentials()
    token = fetch_access_token(client_id, client_secret)
    payload = search_tracks(token, SEARCH_Q, limit=SEARCH_LIMIT)

    tracks_obj = payload.get("tracks") or {}
    items = tracks_obj.get("items") or []
    rows = []
    for item in items:
        if not isinstance(item, dict):
            continue
        rows.append(track_to_row(item))

    print(f"Search: q={SEARCH_Q!r} limit={SEARCH_LIMIT} ({len(rows)} tracks)\n")
    for row in rows:
        ordered = {k: row[k] for k in COLUMN_ORDER}
        print(json.dumps(ordered, ensure_ascii=False))


if __name__ == "__main__":
    main()
