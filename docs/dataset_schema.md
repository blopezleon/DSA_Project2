# Dataset Schema

## Row Definition
Each row in the dataset represents **one Spotify track/song**.

## Primary Sort Field
The primary field used for sorting comparisons is:

- `popularity` — integer from 0 to 100

## Planned Columns

| Column Name | Data Type | Description |
|---|---|---|
| track_id | string | Unique Spotify ID for the track |
| track_name | string | Name of the track |
| artist_name | string | Primary artist name |
| album_name | string | Name of the album |
| popularity | integer | Spotify popularity score from 0 to 100 |
| duration_ms | integer | Length of the track in milliseconds |
| explicit | boolean | Whether the track is marked explicit |

## Notes
- One track counts as one row.
- The dataset must contain at least **100,000 rows**.
- The `popularity` field will be the main field used by the sorting algorithms.
- The dataset will be collected from the otify API and later exported into a processed format usable by the sorting code.
