import PyPDF2
import os

def combine_pdfs(pdf_list, output_filename):
    """
    Combines multiple PDF files into one.
    
    Parameters:
        pdf_list (list of str): List of paths to the PDF files to combine.
        output_filename (str): Path to the resulting combined PDF file.
    """
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        try:
            with open(pdf, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
        except Exception as e:
            print(f"Error processing {pdf}: {e}")

    # Write the combined PDF to a file
    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)
    print(f"Combined PDF saved as {output_filename}")

if __name__ == "__main__":
    # List of PDF files to combine (update this list with your PDF file paths)
    def get_files(directory):
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')]
    pdf_files = get_files("C:\\Users\\dhruv\\Desktop\\tkinter\\BOOK")

    # Output file name
    output_pdf = 'C:\\Users\\dhruv\\Desktop\\tkinter\\BOOK\\tkinter book.pdf'

    # Combine the PDFs
    combine_pdfs(pdf_files, output_pdf)
