import logging
import os
from typing import List, Optional

import markdown
from markdown.extensions.extra import ExtraExtension

from src.logger import Logger


class MarkdownToHtmlConverter:
    _IO_DIRECTORY = "io_content"
    _MARKDOWN_EXTENSION = ".md"
    _HTML_EXTENSION = ".html"
    _READ_MODE = "r"
    _WRITE_MODE = "w"
    _ENCODING = "utf-8"

    def __init__(self, logger: Optional[logging.Logger] = None) -> None:
        if logger is None:
            logger_instance = Logger()
            self.logger = logger_instance.get_logger()
        else:
            self.logger = logger

    def _get_md_files(self) -> List[str]:
        try:
            return [
                md_file
                for md_file in os.listdir(self._IO_DIRECTORY)
                if md_file.endswith(self._MARKDOWN_EXTENSION)
            ]
        except OSError as e:
            self.logger.error(
                f"Error accessing directory {self._IO_DIRECTORY}: {e}"
            )
            return []

    def _read_md_file(self, file_path: str) -> str:
        try:
            with open(
                os.path.join(self._IO_DIRECTORY, file_path),
                mode=self._READ_MODE,
                encoding=self._ENCODING,
            ) as md_file:
                return md_file.read()
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
        except IOError as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
        return ""

    def _convert_md_content_to_html_content(self, md_content: str) -> str:
        try:
            return markdown.markdown(md_content, extensions=[ExtraExtension()])
        except Exception as e:
            self.logger.error(f"Error converting Markdown to HTML: {e}")
            return ""

    def _write_html_file(self, html_file_path: str, html_content: str) -> None:
        try:
            with open(
                os.path.join(self._IO_DIRECTORY, html_file_path),
                mode=self._WRITE_MODE,
                encoding=self._ENCODING,
            ) as html_file:
                html_file.write(html_content)
        except IOError as e:
            self.logger.error(f"Error writing file {html_file_path}: {e}")

    def main(self) -> None:
        self.logger.info("Starting Markdown to HTML conversion.")
        md_files = self._get_md_files()
        if not md_files:
            self.logger.info("No Markdown files found.")
            return

        for md_file in md_files:
            md_content = self._read_md_file(md_file)
            if not md_content:
                continue

            html_content = self._convert_md_content_to_html_content(md_content)
            if not html_content:
                continue

            html_file = md_file.replace(
                self._MARKDOWN_EXTENSION, self._HTML_EXTENSION
            )
            self._write_html_file(html_file, html_content)

        self.logger.info(
            "Congratulations! Markdown to HTML conversion completed!!!"
            " Your files are now shiny HTML!"
        )
