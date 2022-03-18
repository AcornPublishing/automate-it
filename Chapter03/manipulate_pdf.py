__author__ = 'Chetan'
from PyPDF2 import PdfFileWriter, PdfFileReader

## Delete blank pages
# infile = PdfFileReader('myPdf.pdf', 'rb')
# output = PdfFileWriter()
#
# for i in xrange(infile.getNumPages()):
#     p = infile.getPage(i)
#     if p.getContents():
#         output.addPage(p)
#
# with open('myPdf_wo_blank.pdf', 'wb') as f:
#    output.write(f)


## Add metadata to your file
from PyPDF2 import PdfFileMerger, PdfFileReader

mergerObj = PdfFileMerger()
fp = open('myPdf.pdf', 'wb')
metadata = {u'/edited':u'ByPdfFileMerger',}
mergerObj.addMetadata(metadata)
mergerObj.write(fp)
fp.close()

pdf = open("myPdf.pdf", 'rb')
readerObj = PdfFileReader(pdf)
print "Document Info:", readerObj.getDocumentInfo()
pdf.close()

## Encrypt files
#
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
fp = open('Exercise.pdf', 'rb')
readerObj = PdfFileReader(fp)

writer = PdfFileWriter()
for page in range(readerObj.numPages):
    writer.addPage(readerObj.getPage(page))

writer.encrypt('P@$$w0rd')

newfp = open('EncryptExercise.pdf', 'wb')
writer.write(newfp)

newfp.close()
fp.close()

from PyPDF2 import PdfFileReader
fp = open('Exercise.pdf', 'rb')
readerObj = PdfFileReader(fp)
page = readerObj.getPage(0)
page.rotateCounterClockwise(90)
writer = PdfFileWriter()
writer.addPage(page)
fw = open('RotatedExercise.pdf', 'wb')
writer.write(fw)
fw.close()
fp.close()