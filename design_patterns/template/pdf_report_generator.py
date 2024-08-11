from template.template_report_generator import TemplateReportGenerator


class PDFReportGenerator(TemplateReportGenerator):

    def add_header(self) -> None:
        print("Adding PDF Header")

    def add_content(self) -> None:
        print("Adding PDF content")

    def add_footer(self) -> None:
        print("Adding PDF Footer")
