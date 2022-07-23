import PyPDF2
import os


def pdf_watermarker():
    watermark_pdf = PyPDF2.PdfFileReader(
        "C:\\Users\\Fudzi\\workspace\\watermarker\\pdf\\213_wtr.pdf")
    output = PyPDF2.PdfFileWriter()
    for filename in os.listdir('C:\\Users\\Fudzi\\workspace\\watermarker\\pdf'):
        template = PyPDF2.PdfFileReader(open(f'C:\\Users\\Fudzi\\workspace\\watermarker\\pdf\\{filename}', 'rb'))
        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark_pdf.getPage(0))
            output.addPage(page)
            clean_name = os.path.splitext(filename)[0]
            isdir = os.path.isdir(
                'C:\\Users\\Fudzi\\workspace\\watermarker\\watermarked_pdfs')
            if not isdir:
                os.makedirs('.\\watermarked_pdfs')
            with open(f'C:\\Users\\Fudzi\\workspace\\watermarker\\watermarked_pdfs\\{clean_name}_watermarked.pdf', 'wb') as file:
                output.write(file)


pdf_watermarker()
