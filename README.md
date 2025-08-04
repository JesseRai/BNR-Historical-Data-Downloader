# BNR Historical Data Downloader

This Python script downloads historical financial or economic data from the **Romanian National Bank (BNR)**'s website in `.csv` format using an internal dataset ID (`cid`).

## Features

- Downloads data by `cid` directly from BNR (`https://www.bnr.ro/idbsfiles`)
- Saves the file as a `.csv`
- Requires no browser automation (uses only `requests`)

## How to Use

### Run from Command Line:

```bash
python script_name.py <cid> <filename>
