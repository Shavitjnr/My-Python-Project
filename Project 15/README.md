# PDF Merger/Reader

A command-line utility to merge multiple PDF files into one or extract text from PDF files using PyPDF2 and pdfplumber.

## 📋 Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Merge PDFs](#merge-pdfs)
  - [Extract Text](#extract-text)
- [Contributing](#contributing)
- [License](#license)

## Description
PDF Merger/Reader is a simple Python tool that allows you to:
- Merge multiple PDF files into a single PDF
- Extract text from PDF files (to console or a text file)

It uses the PyPDF2 library for merging and pdfplumber for accurate text extraction.

## Features
- Merge any number of PDF files into one
- Extract all text from a PDF file
- Output extracted text to the console or a file
- Simple command-line interface

## Requirements
- Python 3.6 or higher
- PyPDF2
- pdfplumber

## Installation
1. Clone or download this repository.
2. Navigate to the `Project 15` directory:
   ```bash
   cd "Project 15"
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Merge PDFs
Merge multiple PDF files into a single PDF:
```bash
python main.py merge output.pdf input1.pdf input2.pdf ...
```
- `output.pdf`: The name of the merged PDF file to create.
- `input1.pdf input2.pdf ...`: The PDF files to merge (in order).

### Extract Text
Extract text from a PDF file to the console or a text file:
```bash
python main.py extract input.pdf [output.txt]
```
- `input.pdf`: The PDF file to extract text from.
- `output.txt` (optional): If provided, saves the extracted text to this file. Otherwise, prints to the console.

## Contributing
Contributions are welcome! You can:
- Fix bugs or add features
- Improve documentation
- Submit pull requests for review

## License
MIT License. See LICENSE file for details.
