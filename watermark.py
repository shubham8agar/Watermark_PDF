import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to create the watermark PDF
def create_watermark(watermark_text, watermark_pdf):
    c = canvas.Canvas(watermark_pdf, pagesize=A4)
    width, height = A4
    c.saveState()
    c.translate(width / 2, height / 2)
    c.setFont("Helvetica", 40)
    c.setFillGray(0.5, 0.5)
    c.rotate(45)
    c.drawCentredString(0, 0, watermark_text)
    c.restoreState()
    c.save()

# Function to apply watermark to all PDFs in the current folder
def add_watermark_to_all_pdfs_in_folder(watermark_pdf, watermark_text):
    folder_path = os.getcwd()  # Get the current working directory
    create_watermark(watermark_text, watermark_pdf)

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf") and not filename.startswith("wm-"):
            input_pdf = os.path.join(folder_path, filename)
            output_pdf = os.path.join(folder_path, f"wm-{filename}")

            pdf_reader = PdfReader(input_pdf)
            pdf_writer = PdfWriter()
            watermark_reader = PdfReader(watermark_pdf)
            watermark_page = watermark_reader.pages[0]

            for page in pdf_reader.pages:
                page.merge_page(watermark_page)
                pdf_writer.add_page(page)

            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

    print(f"Watermarked PDFs created in {folder_path}")

# Usage
watermark_pdf = "watermark.pdf"
watermark_text = "Type your text here"

add_watermark_to_all_pdfs_in_folder(watermark_pdf, watermark_text)
