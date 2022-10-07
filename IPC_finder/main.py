import PyPDF2
import glob
import os

# output = "out.pdf"
# start_page = 0
# end_page = -1
# inputfile = (IPC_data, 'rb')
# merger = PdfFileMerger()
# page_range = str(start_page) + ':' + str(end_page)
# print(page_range)
# merger_pages = merger.append(File_object, pages = PageRange(page_range))
# print("Done")
# print(.extractText())
# merger.write(output)
# print("done")

# IPC_data = "IPC.pdf"
# File_object = open(IPC_data, 'rb')
# print("Loaded")
#
# reader = pdfReader = PyPDF2.PdfFileReader(File_object)
# count = pdfReader.numPages
# for i in range(count):
#     page = pdfReader.getPage(i)
#     output = []
#     output.append(page.extractText())
#
# print()
# Page_object = pdfReader.getPage(0)
#
# print(Page_object.extractText())

file_path = './'
read_files = glob.glob(os.path.join(file_path,'*.pdf'))

for files in read_files:
    pdfReader = PyPDF2.PdfFileReader(files)
    count = pdfReader.numPages
    output = []
    for i in range(count):
        page = pdfReader.getPage(i)
        output.append(page.extractText())
    print(output)
