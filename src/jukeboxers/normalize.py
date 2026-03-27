"""Map Spotify Track JSON to ProcessedTrack."""

from __future__ import annotations

from typing import Any, Mapping

from jukeboxers.schema import ProcessedTrack


def track_to_row(track: Mapping[str, Any]) -> ProcessedTrack:
    """Primary artist = first entry in artists[]."""
    artists = track.get("artists") or []
    if artists:
        first_artist = artists[0] or {}
        artist_name = str(first_artist.get("name") or "")
    else:
        artist_name = ""

    album = track.get("album") or {}
    album_name = str(album.get("name") or "")

    explicit = track.get("explicit")
    if explicit is None:
        explicit_bool = False
    else:
        explicit_bool = bool(explicit)

    popularity = track.get("popularity")
    if popularity is None:
        popularity_int = 0
    else:
        popularity_int = int(popularity)

    duration = track.get("duration_ms")
    if duration is None:
        duration_ms = 0
    else:
        duration_ms = int(duration)

    track_id = str(track.get("id") or "")
    track_name = str(track.get("name") or "")

    return ProcessedTrack(
        track_id=track_id,
        track_name=track_name,
        artist_name=artist_name,
        album_name=album_name,
        popularity=popularity_int,
        duration_ms=duration_ms,
        explicit=explicit_bool,
    )
