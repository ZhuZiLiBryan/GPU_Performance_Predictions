from pathlib import Path

# Create data directory
# unzip data here
data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)