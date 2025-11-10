import PyPDF2

merger = PyPDF2.PdfMerger()

for pdf in ["1.pdf", "2.pdf", ]:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()