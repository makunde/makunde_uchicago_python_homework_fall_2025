# Assignment 5 — PDF indexer (usage)

This folder contains script in `problem_8.py` that extracts keywords from PDF lecture slides and writes a simple index file listing keywords by frequency.

### Dependencies
- Python 3.8+ (macOS default Python3 is fine)
- `pypdf` package (install with pip):

```bash
python3 -m pip install --user pypdf
```

### Where to run
- Run the command from the `assignment_5` directory (the examples below assume your current working directory is `assignment_5`).

### Required flag
- The `--common_words_filter` flag is required. It tells the script which stopwords file to use to filter out very common words like "the" and "and".

### Command
```bash
python problem_8.py --common_words_filter=[common word .txt file] [lecture pdf1] [lecture pdf2]...
```
### Exact copy-paste command for all lecture slides
Paste the following single command in the `root` directory to process the three provided lecture PDFs (these PDFs live in `lecture_pdfs/`):

```bash
python problem_8.py --common_words_filter=common_words.txt lecture_pdfs/*.pdf
```

### Output location
- All generated index files are written into the `lecture_pdfs/` folder next to the processed PDFs. For example, running the command above will produce files like `lecture_pdfs/mpcs50101-2025-autumn-module-1-synchronous_index.txt`.

### Notes
- If you get an import error for `pypdf`, make sure you installed the package into the same Python interpreter you run with `python` (or use `python3` explicitly).
- If you'd prefer to run a single PDF, just pass a single PDF path instead of the three shown above.

If you'd like, I can also add a small wrapper script to decode any included base64 sample PDF and run this command automatically.

