import requests
from pathlib import Path
from tqdm import tqdm

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

files = {
    "cases.parquet":
        "https://zenodo.org/records/20415668/files/cases.parquet?download=1",

    "case_images.parquet":
        "https://zenodo.org/records/20415668/files/case_images.parquet?download=1",

    "captions_and_labels.csv":
        "https://zenodo.org/records/20415668/files/captions_and_labels.csv?download=1",

    "abstracts.parquet":
        "https://zenodo.org/records/20415668/files/abstracts.parquet?download=1",

    "metadata.parquet":
        "https://zenodo.org/records/20415668/files/metadata.parquet?download=1",
}


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total = int(response.headers.get("content-length", 0))

    with open(output_path, "wb") as f:
        with tqdm(
            total=total,
            unit="B",
            unit_scale=True,
            desc=output_path.name
        ) as pbar:

            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))


for filename, url in files.items():

    output_path = DATA_DIR / filename

    if output_path.exists():
        print(f"[SKIP] {filename}")
        continue

    print(f"\nDownloading {filename}...")
    download_file(url, output_path)

print("\nDone.")