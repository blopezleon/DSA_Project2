"""Processed track row — matches docs/dataset_schema.md column order."""

from __future__ import annotations

from typing import TypedDict


class ProcessedTrack(TypedDict):
    track_id: str
    track_name: str
    artist_name: str
    album_name: str
    popularity: int
    duration_ms: int
    explicit: bool


COLUMN_ORDER: tuple[str, ...] = (
    "track_id",
    "track_name",
    "artist_name",
    "album_name",
    "popularity",
    "duration_ms",
    "explicit",
)
