def bucket_sort(songs: list[dict], key: str, min_val: float = 0.0, max_val: float = 100.0, num_buckets: int = 10) -> list[dict]:
    if not songs:
        return []

    buckets: list[list[dict]] = [[] for _ in range(num_buckets)]

    value_range = max_val - min_val
    if value_range == 0:
        return list(songs)

    for song in songs:
        value = song[key]
       
        normalised = (value - min_val) / value_range
        
        bucket_index = min(int(normalised * num_buckets), num_buckets - 1)
        buckets[bucket_index].append(song)

    for bucket in buckets:
        bucket.sort(key=lambda s: s[key])

    sorted_songs: list[dict] = []
    for bucket in buckets:
        sorted_songs.extend(bucket)

    return sorted_songs