"""This script will download trips data from Google drive."""
from pathlib import Path
import gdown

ROOT_DIR = Path(__file__).parent.parent


def download_trips_data():
    """Download trips data."""
    url = "https://drive.google.com/u/0/uc?id=1QLBGFOoKw_3-iM58q4unWfwHmPqfnrYr&export=download"
    output = ROOT_DIR / Path("data/chicago_taxi_trips_2020.parquet")
    if not output.exists():
        gdown.download(url, str(output), fuzzy=True)


if __name__ == "__main__":
    download_trips_data()
