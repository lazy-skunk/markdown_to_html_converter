from src.logger import Logger
from src.markdown_to_html_converter import MarkdownToHtmlConverter

if __name__ == "__main__":
    logger_instance = Logger().get_logger()
    converter = MarkdownToHtmlConverter(logger_instance)
    converter.main()
