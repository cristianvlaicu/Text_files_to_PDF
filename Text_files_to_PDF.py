# We are going to create a program that, given some text in txt format, will group them into a pdf document with one page for each text document.

from fpdf import FPDF
import glob
from pathlib import Path

C = 0  # color.

# Create a list of text filepaths
filepaths = glob.glob(r"files\*.txt")

# Create a pdf instance using the FPDF module. And we format it: Portrait orientation, units in mm and A4 format.
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Iterate over each text file:
for filepath in filepaths:
    # Add a PDF page for each text file.
    pdf.add_page()

    # Extract the name of each text file without the extension.
    filename = Path(filepath).stem
    document_name = filename.upper()

    # Put that name on each page of the PDF file.
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=document_name, align="C", ln=1)
    pdf.line(86, 21, 124, 21)
    pdf.set_draw_color(C, C, C)

    pdf.cell(w=0, h=12, ln=2)

    # Extract the content of each text file by opening them...
    with open(filepath, "r") as file:
        document_content = (
            file.read()
        )  # and saving the content of each text in that variable.
    # Add the text file content to the PDF
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(C, C, C)
    pdf.multi_cell(w=0, h=6, txt=document_content, align="J")

    pdf.ln(176)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(C, C, C)
    pdf.cell(w=0, h=0, txt=str(pdf.page_no()), align="C")

# Produce the PDF
pdf.output("Text_files_to_PDF.pdf")