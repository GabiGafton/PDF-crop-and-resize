from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

pdf_file = PdfFileReader(open("temp.pdf","rb"))
page = pdf_file.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())