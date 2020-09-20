from PyPDF2 import PdfFileReader, PdfFileMerger
import os
from tkinter import *
from tkinter.filedialog import *

merger = PdfFileMerger()
root = Tk()
root.withdraw()
file_path = askopenfilenames(parent=root,filetypes=[("PDF Files",".pdf")])
print(root.tk.splitlist(file_path))

for items in file_path:
    if items.endswith('.pdf'):
        merger.append(items)

merger.write("result_pdf.pdf")
merger.close()