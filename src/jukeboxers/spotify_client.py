"""Minimal Spotify Web API HTTP client (Client Credentials)."""

from __future__ import annotations

import time
from typing import Any

import requests

from jukeboxers.config import SPOTIFY_API_BASE


def _request_json(
    method: str,
    path: str,
    access_token: str,
    *,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    url = f"{SPOTIFY_API_BASE}{path}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=30,
    )
    if response.status_code == 429:
        retry_after = float(response.headers.get("Retry-After", "1"))
        time.sleep(retry_after)
        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            timeout=30,
        )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise ValueError("Expected JSON object from API")
    return data


def search_tracks(
    access_token: str,
    q: str,
    *,
    limit: int = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {"q": q, "type": "track", "limit": limit}
    return _request_json("GET", "/search", access_token, params=params)
