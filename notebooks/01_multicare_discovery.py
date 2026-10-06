import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

print("DATA DIR:", DATA_DIR)

cases = pd.read_parquet(DATA_DIR / "cases.parquet")
case_images = pd.read_parquet(DATA_DIR / "case_images.parquet")

captions = pd.read_csv(
    DATA_DIR / "captions_and_labels.csv",
    low_memory=False
)

abstracts = pd.read_parquet(DATA_DIR / "abstracts.parquet")
metadata = pd.read_parquet(DATA_DIR / "metadata.parquet")


print("\n========== CASES ==========")
print("Shape:", cases.shape)
print("Columns:", cases.columns.tolist())

print("\n========== CASE IMAGES ==========")
print("Shape:", case_images.shape)
print("Columns:", case_images.columns.tolist())

print("\n========== CAPTIONS ==========")
print("Shape:", captions.shape)
print("Columns:", captions.columns.tolist())

print("\n========== ABSTRACTS ==========")
print("Shape:", abstracts.shape)
print("Columns:", abstracts.columns.tolist())

print("\n========== METADATA ==========")
print("Shape:", metadata.shape)
print("Columns:", metadata.columns.tolist())

print("\n========== SUCCESS ==========")
print("All MultiCaRe metadata files loaded successfully!")


# ============================================================
# STEP 2: BASIC DATA DISCOVERY
# ============================================================

print("\n" + "=" * 70)
print("STEP 2 - MULTICARE DATA DISCOVERY")
print("=" * 70)

# ------------------------------------------------------------
# 1. Basic information
# ------------------------------------------------------------

datasets = {
    "cases": cases,
    "case_images": case_images,
    "captions": captions,
    "abstracts": abstracts,
    "metadata": metadata
}

for name, df in datasets.items():
    print(f"\n{name.upper()}")
    print("-" * 50)
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())


# ------------------------------------------------------------
# 2. Show first 3 rows
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("SAMPLE DATA")
print("=" * 70)

for name, df in datasets.items():
    print(f"\n### {name.upper()} ###")
    print(df.head(3).to_string())


# ------------------------------------------------------------
# 3. Check missing values
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("MISSING VALUES")
print("=" * 70)

for name, df in datasets.items():
    print(f"\n### {name.upper()} ###")

    missing = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    print(missing.head(15))


print("\n" + "=" * 70)
print("STEP 2 COMPLETE")
print("=" * 70)