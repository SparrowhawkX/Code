# Texas PUC Filing Download Script

This script automatically downloads all 203 filings from Texas PUC case **58481** (Rulemaking to Implement Large Load Interconnection Standards under PURA 37.0561).

## How to Use

### Option 1: Run the Python Script (Recommended)

**Requirements:**
- Python 3.6 or newer
- Install dependencies: `pip install requests beautifulsoup4`

**Steps:**

```bash
pip install requests beautifulsoup4
python download_puc_filings.py
```

The script will create a folder called `puc_filings_58481/` with all downloaded files.

**What the script does:**
- Downloads all 203 items from case 58481
- Creates a subfolder for each item (`item_001`, `item_002`, etc.)
- Skips already-downloaded files so reruns are safe
- Saves all documents within their respective item folders
- Creates a `manifest.json` file with download metadata
- Creates a `failed_items.json` if any downloads fail
- Respects the server with delays between requests

**Download time:** Approximately 10–30 minutes depending on internet speed and file sizes

### Option 2: Manual Browser Download

1. Visit: https://interchange.puc.texas.gov/Search/Filings?ControlNumber=58481
2. Click on each item number (1–203)
3. Download the documents from each item page

## Output Structure

```
puc_filings_58481/
├── item_001/
│   ├── document1.pdf
│   └── document2.zip
├── item_002/
│   └── filing_document.pdf
...
├── manifest.json        # metadata for all downloads
└── failed_items.json    # only present if any downloads failed
```

## Troubleshooting

**"Module not found: requests"**
```
pip install requests beautifulsoup4
```

**"Connection error" or "Timeout"**
- The server may be temporarily unavailable; try running again (already-downloaded files are skipped)
- Check your internet connection

**Some files didn't download**
- Check `failed_items.json` for which items had issues
- Try downloading those specific items manually from the website

**Script is running slowly**
- This is intentional — the script waits between requests to avoid overwhelming the server
- Expected time: 10–30 minutes for all 203 items

## Case Information

| Field | Value |
|---|---|
| Control Number | 58481 |
| Case Style | RULEMAKING TO IMPLEMENT LARGE LOAD INTERCONNECTION STANDARDS UNDER PURA 37.0561 |
| Total Items | 203 |
| Source | Texas Public Utility Commission (PUC) Interchange Filing System |
