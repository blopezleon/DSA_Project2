"""Spotify Client Credentials access token."""

from __future__ import annotations

import requests

from jukeboxers.config import SPOTIFY_ACCOUNTS_TOKEN_URL


def fetch_access_token(client_id: str, client_secret: str) -> str:
    response = requests.post(
        SPOTIFY_ACCOUNTS_TOKEN_URL,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    token = data.get("access_token")
    if not token or not isinstance(token, str):
        raise ValueError("Token response missing access_token")
    return token
