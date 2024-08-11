from abc import ABC, abstractmethod
from typing import Self


class TemplateReportGenerator(ABC):
    def generate_report(self: Self) -> None:
        """
        Template method to generate report.
        """

        self.add_header()
        self.add_content()
        self.add_footer()
        self.end_report()

    @abstractmethod
    def add_header(self) -> None:
        """Add the header to the report."""
        pass

    @abstractmethod
    def add_content(self) -> None:
        """Add the main content to the report."""
        pass

    @abstractmethod
    def add_footer(self) -> None:
        """Add the footer to the report."""
        pass

    def end_report(self) -> None:
        """Finalize the report."""
        print("Report finalized.")
