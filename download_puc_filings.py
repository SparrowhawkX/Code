#!/usr/bin/env python3
"""
Download all filings from Texas PUC case 58481
This script iterates through all 203 items and downloads all associated documents
"""

import requests
from bs4 import BeautifulSoup
import os
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
import json
import urllib3

# Suppress SSL warnings — the PUC site uses a government intermediate CA
# not included in Python's default cert bundle; the site itself is legitimate.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Settings
BASE_URL = "https://interchange.puc.texas.gov"
CONTROL_NUMBER = "58481"
OUTPUT_DIR = Path("puc_filings_58481")
OUTPUT_DIR.mkdir(exist_ok=True)

# Create session with headers to avoid being blocked
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})
session.verify = False  # bypass SSL cert chain issue with government CA

print(f"Starting download of all filings for control number {CONTROL_NUMBER}")
print(f"Output directory: {OUTPUT_DIR}")
print(f"Processing 203 items...\n")

# Quick connectivity check on item 1 before full run
print("Testing connection to item 1...")
test_url = f"{BASE_URL}/search/documents/?controlNumber={CONTROL_NUMBER}&itemNumber=1"
try:
    test_resp = session.get(test_url, timeout=15)
    print(f"  Status: {test_resp.status_code}")
    print(f"  Page title snippet: {test_resp.text[:300]}\n")
except Exception as e:
    print(f"  Connection failed: {e}")
    print("  Cannot reach the site. Exiting.")
    exit(1)

downloaded_count = 0
failed_items = []
manifest = []

# Loop through all 203 items
for item_number in range(1, 204):
    try:
        # Construct URL for this item
        item_url = f"{BASE_URL}/search/documents/?controlNumber={CONTROL_NUMBER}&itemNumber={item_number}"

        # Show progress
        if item_number % 10 == 0 or item_number == 1:
            print(f"Processing items {item_number-9} to {min(item_number+9, 203)}...")

        # Fetch the item page
        response = session.get(item_url, timeout=15)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all file download links
        # Files are usually in <a> tags with specific href patterns
        file_links = []

        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text(strip=True)

            # Look for file download links
            if href and any(ext in href.lower() for ext in ['.pdf', '.zip', '.docx', '.xlsx', '.doc', '.txt', '.xml', '.xls']):
                file_links.append({
                    'name': text or href,
                    'href': href
                })

        # If we found documents, prepare for download
        if file_links:
            # Create subdirectory for this item
            item_dir = OUTPUT_DIR / f"item_{item_number:03d}"
            item_dir.mkdir(exist_ok=True)

            for file_info in file_links:
                file_href = file_info['href']
                filename = 'unknown'
                try:
                    # Construct full URL if relative
                    if file_href.startswith('/'):
                        file_url = BASE_URL + file_href
                    elif file_href.startswith('http'):
                        file_url = file_href
                    else:
                        file_url = urljoin(item_url, file_href)

                    # Extract filename from URL
                    parsed_url = urlparse(file_url)
                    filename = os.path.basename(parsed_url.path)

                    if not filename or '.' not in filename:
                        # Try to get from text or construct default
                        filename = file_info['name'][:50].replace('/', '_').replace('\\', '_')
                        if '.' not in filename:
                            filename = f"document_{item_number}.pdf"

                    # Skip already-downloaded files
                    file_path = item_dir / filename
                    if file_path.exists():
                        print(f"  Skipping (already exists): {filename}")
                        downloaded_count += 1
                        continue

                    # Download file
                    file_response = session.get(file_url, timeout=30, allow_redirects=True)
                    file_response.raise_for_status()

                    with open(file_path, 'wb') as f:
                        f.write(file_response.content)

                    manifest.append({
                        'item': item_number,
                        'file': filename,
                        'size': len(file_response.content),
                        'url': file_url
                    })

                    downloaded_count += 1

                except Exception as e:
                    failed_items.append({
                        'item': item_number,
                        'file': filename,
                        'error': str(e)
                    })

        # Be respectful to the server - add delay
        time.sleep(0.3)

    except Exception as e:
        failed_items.append({
            'item': item_number,
            'file': 'N/A',
            'error': str(e)
        })

# Save manifest
manifest_path = OUTPUT_DIR / "manifest.json"
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f"\n{'='*60}")
print(f"Download complete!")
print(f"Total files downloaded: {downloaded_count}")
print(f"Output directory: {OUTPUT_DIR}")
print(f"Manifest saved to: {manifest_path}")

if failed_items:
    print(f"\nFailed downloads ({len(failed_items)}):")
    for item in failed_items[:20]:
        print(f"  Item {item['item']}: {item['error']}")

    failed_path = OUTPUT_DIR / "failed_items.json"
    with open(failed_path, 'w') as f:
        json.dump(failed_items, f, indent=2)
    print(f"\nFull list of failed items saved to: {failed_path}")

print(f"\nOrganization:")
print(f"  - Each item has its own folder (item_001, item_002, etc.)")
print(f"  - All files are in their respective item folders")
print(f"  - manifest.json contains download metadata")
