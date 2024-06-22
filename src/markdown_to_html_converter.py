import os
from typing import List
import markdown
from markdown.extensions.extra import ExtraExtension

class MarkdownToHtmlConverter:
    _CURRENT_DIRECTORY = "."
    _MARKDOWN_EXTENSION = ".md"
    _HTML_EXTENSION = ".html"
    _READ_MODE = "r"
    _WRITE_MODE = "w"
    _ENCODING = "utf-8"

    def _get_md_files(self) -> List[str]:
        return [
            md_file
            for md_file in os.listdir(self._CURRENT_DIRECTORY)
            if md_file.endswith(self._MARKDOWN_EXTENSION)
        ]

    def _read_md_file(self, file_path: str) -> str:
        with open(
            os.path.join(self._CURRENT_DIRECTORY, file_path),
            mode=self._READ_MODE,
            encoding=self._ENCODING,
        ) as md_file:
            return md_file.read()

    def _write_html_file(self, html_file_path: str, html_content: str) -> None:
        with open(
            os.path.join(self._CURRENT_DIRECTORY, html_file_path),
            mode=self._WRITE_MODE,
            encoding=self._ENCODING,
        ) as html_file:
            html_file.write(html_content)

    def _convert_md_content_to_html_content(self, md_content: str) -> str:
        return markdown.markdown(md_content, extensions=[ExtraExtension()])

    def main(self) -> None:
        md_files = self._get_md_files()
        for md_file in md_files:
            md_content = self._read_md_file(md_file)
            html_content = self._convert_md_content_to_html_content(md_content)
            html_file = md_file.replace(self._MARKDOWN_EXTENSION, self._HTML_EXTENSION)
            self._write_html_file(html_file, html_content)
        print("処理終了ですぜ。")

if __name__ == "__main__":  # pragma: no cover
    converter = MarkdownToHtmlConverter()
    converter.main()
