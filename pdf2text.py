import PyPDF2

def extract_text_from_pdf(pdf_file_path, output_file_path):
  """Extracts text from a PDF file and saves it to an output file.

  Args:
    pdf_file_path: The path to the PDF file to extract text from.
    output_file_path: The path to the output file to save the text data to.
  """

  pdf_reader = PyPDF2.PdfReader(pdf_file_path)
  output_file = open(output_file_path, "w")

  for page in pdf_reader.pages:
    text = page.extract_text()
    output_file.write(text)

  output_file.close()


if __name__ == "__main__":
  pdf_file_path = "pdftext.pdf"
  output_file_path = "pdftext.txt"

  extract_text_from_pdf(pdf_file_path, output_file_path)