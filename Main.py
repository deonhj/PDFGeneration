from fpdf import FPDF
from fpdf.enums import XPos, YPos
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=0)
    pdf.line(10, 20, 200, 20)


pdf.output("output.pdf")
