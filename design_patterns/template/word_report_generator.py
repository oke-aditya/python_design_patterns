from template.template_report_generator import TemplateReportGenerator


class WordReportGenerator(TemplateReportGenerator):

    def add_header(self) -> None:
        print("Adding word header")

    def add_content(self) -> None:
        print("Adding word header")

    def add_footer(self) -> None:
        print("Adding footer")
