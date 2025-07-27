import sys
import os
import PyPDF2
import pdfplumber

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDFs saved to {output_path}")

def extract_text(pdf_path, output_txt_path=None):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    if output_txt_path:
        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted text saved to {output_txt_path}")
    else:
        print(text)

def print_usage():
    print("Usage:")
    print("  Merge PDFs: python main.py merge output.pdf input1.pdf input2.pdf ...")
    print("  Extract text: python main.py extract input.pdf [output.txt]")

def main():
    if len(sys.argv) < 3:
        print_usage()
        return
    command = sys.argv[1].lower()
    if command == 'merge':
        if len(sys.argv) < 5:
            print("Error: Need at least two input PDFs to merge.")
            print_usage()
            return
        output_pdf = sys.argv[2]
        input_pdfs = sys.argv[3:]
        for pdf in input_pdfs:
            if not os.path.exists(pdf):
                print(f"Error: File not found: {pdf}")
                return
        merge_pdfs(input_pdfs, output_pdf)
    elif command == 'extract':
        input_pdf = sys.argv[2]
        if not os.path.exists(input_pdf):
            print(f"Error: File not found: {input_pdf}")
            return
        output_txt = sys.argv[3] if len(sys.argv) > 3 else None
        extract_text(input_pdf, output_txt)
    else:
        print_usage()

if __name__ == "__main__":
    main()
