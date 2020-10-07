from PyPDF2 import PdfFileMerger, PdfFileReader
import os

cwd = os.getcwd()
files = os.listdir(os.path.join(cwd, 'obalky'))

for _file in files:
    mergedObject = PdfFileMerger()
    a = os.path.join(cwd, 'obalky', _file)
    b = os.path.join(cwd, 'obsah', _file)
    c = os.path.join(cwd, 'res', _file)
    mergedObject.append(PdfFileReader(a, 'rb'))
    mergedObject.append(PdfFileReader(b, 'rb'))
    mergedObject.write(c)
