from template.pdf_report_generator import PDFReportGenerator
from template.word_report_generator import WordReportGenerator

if __name__ == "__main__":
    word_report = WordReportGenerator()
    pdf_report = PDFReportGenerator()

    word_report.generate_report()
    print('\n')
    pdf_report.generate_report()
