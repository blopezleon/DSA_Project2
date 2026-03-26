# Dataset Spec

- one row = one unique track record
- target = 100000+ rows
- source = Spotify Web API
- chosen numeric sort field = popularity
- outputs:
  - data/raw/
  - data/processed/final_dataset.csv
  - docs/schema.md
- success criteria:
  - deduplicated by track_id
  - popularity is present and numeric
  - processed CSV loads cleanly in Python
  - README includes regeneration steps
