import PyPDF2

pdf_file=open("C:\\Users\\Priyanka B\\Downloads\\Assignment Submission_ Data Analyst Work from Home.pdf","rb")
pdf_reader=PyPDF2.PdfReader(pdf_file)
print(len(pdf_reader.pages))
pageObj=pdf_reader.pages[0]
print(pageObj.extract_text())
pdf_file.close()




