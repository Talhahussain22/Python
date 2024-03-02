import PyPDF2

# pdf_file=open("English.pdf",'rb')
#
# pdf_reader=PyPDF2.PdfReader(pdf_file)
#
# text=""
#
# for page in range(len(pdf_reader.pages)):
#     pdf_obj=pdf_reader.pages[page]
#     text+=pdf_obj.extract_text()
#
# pdf_file.close()
# print(text)

# def merger_pdf(l):
#     merger=PyPDF2.PdfMerger()
#     for pdf in l:
#         merger.append(PyPDF2.PdfReader(pdf,'rb'))
#     merger.write("Newpdf.pdf")
# l=["1.pdf","2.pdf"]
# merger_pdf(l)


