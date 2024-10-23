    # Vamos a crear un programa que dado unos texto en formato txt los vamoos a agrupar en un documento pdf con una página para cada documento de texto.
from fpdf import FPDF
import glob
from pathlib import Path

C = 0  # color.

# Create a list of text filepaths
filepaths = glob.glob(r"files\*.txt")

# Creamos instancia de pdf acudiendo al módulo FPDF. Y le damos formato: orientación Portrait, unidades en mm y formato A4.
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Recorremos cada archivo de texto:
for filepath in filepaths:
    # Añadimos una página PDf por cada archivo de texto.
    pdf.add_page()

    # Extraemos el noche de cada archivo de texto sin la extensión.
    filename = Path(filepath).stem
    document_name = filename.upper()

    # Ponemos ese nombre a cada página del archivo PDf.
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=document_name, align="C", ln = 1)
    pdf.line(86, 21, 124, 21)
    pdf.set_draw_color(C, C, C)

    pdf.cell(w=0, h=12, ln=2)

    # Extraemos el contenido de cada archivo de texto abriéndolos...
    with open(filepath, "r") as file:
        document_content = file.read()  # y guardando en esa variable el contenido de cada texto.
    # Add the text file content to the PDf
    pdf.set_font(family="Times", style= "I", size=12)
    pdf.set_text_color(C, C, C)
    pdf.multi_cell(w=0, h=6, txt=document_content, align="J")

    pdf.ln(176)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(C, C, C)
    pdf.cell(w=0, h=0, txt=str(pdf.page_no()), align="C")
# Produce the PDF
pdf.output("Text_files_to_PDF.pdf")