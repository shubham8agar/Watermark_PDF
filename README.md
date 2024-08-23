# Watermark_PDF
PDF Watermarking Script

# PDF Watermarking Script

This Python script allows you to apply a watermark to all PDF files in the same directory where the script is located. The watermarked PDFs are saved with filenames prefixed by `wm-`.

## Features

- **Automatic Watermarking**: Applies a watermark to all PDFs in the current directory.
- **Customizable Watermark Text**: Easily change the watermark text by modifying a variable.
- **Avoids Reprocessing**: Skips files that have already been watermarked (those starting with `wm-`).

## Prerequisites

Make sure you have Python installed on your system. You will also need to install the following Python libraries:

- `PyPDF2`: To read, manipulate, and write PDF files.
- `reportlab`: To create the watermark PDF.

You can install these libraries using pip:

```bash
pip install PyPDF2 reportlab
python watermark.py
