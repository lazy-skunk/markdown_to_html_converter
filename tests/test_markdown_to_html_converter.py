import os
from typing import Any, Generator, Tuple
from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.markdown_to_html_converter import MarkdownToHtmlConverter


def _create_test_file(directory: str, filename: str, content: str) -> None:
    with open(os.path.join(directory, filename), "w", encoding="utf-8") as f:
        f.write(content)


def _cleanup_test_directory(directory: str) -> None:
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            _cleanup_test_directory(file_path)
            os.rmdir(file_path)
    os.rmdir(directory)


@pytest.fixture(scope="module")
def setup_test_environment() -> (
    Generator[Tuple[str, str, str, str], None, None]
):
    _test_dir = "test_dir"
    _md_filename = "test.md"
    _empty_md_filename = "empty.md"
    _html_filename = "test.html"

    os.makedirs(_test_dir, exist_ok=True)

    _create_test_file(_test_dir, _md_filename, "# Test Markdown\n\nTest!")
    _create_test_file(_test_dir, _empty_md_filename, "")

    yield _test_dir, _md_filename, _empty_md_filename, _html_filename

    _cleanup_test_directory(_test_dir)


@pytest.fixture(scope="module")
def setup_empty_directory() -> Generator[str, Any, Any]:
    _test_dir = "empty_dir"
    os.makedirs(_test_dir, exist_ok=True)

    yield _test_dir

    _cleanup_test_directory(_test_dir)


@pytest.fixture
def mock_logger() -> MagicMock:
    return MagicMock()


def test_get_md_files(
    setup_test_environment: Tuple[str, str, str, str], mock_logger: MagicMock
) -> None:
    test_dir, md_filename, empty_md_filename, _ = setup_test_environment
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = test_dir
    md_files = converter._get_md_files()

    expected_files = [md_filename, empty_md_filename]

    for filename in expected_files:
        assert filename in md_files, f"{filename} should be in {md_files}"


def test_get_md_files_oserror(mock_logger: MagicMock) -> None:
    converter = MarkdownToHtmlConverter(mock_logger)
    with patch("os.listdir", side_effect=OSError("Error accessing directory")):
        md_files = converter._get_md_files()
        assert md_files == [], "md_files should be an empty list on OSError"
        mock_logger.error.assert_called_with(
            "Error accessing directory io_content: Error accessing directory"
        )


def test_read_md_file(
    setup_test_environment: Tuple[str, str, str, str]
) -> None:
    test_dir, md_filename, _, _ = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._IO_DIRECTORY = test_dir
    content = converter._read_md_file(md_filename)
    assert (
        content == "# Test Markdown\n\nTest!"
    ), f"Content of {md_filename} should be '# Test Markdown\n\nTest!'"


def test_read_md_file_error(mock_logger: MagicMock) -> None:
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = "non_existing_dir"
    content = converter._read_md_file("non_existing_file.md")
    assert (
        content == ""
    ), "Content should be an empty string for non-existing file"
    mock_logger.error.assert_called_with(
        "File not found: non_existing_file.md"
    )


def test_read_md_file_ioerror(mock_logger: MagicMock) -> None:
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = "test_dir"
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = IOError("Cannot read file")
        content = converter._read_md_file("test.md")
        assert content == "", "Content should be an empty string on IOError"
        mock_logger.error.assert_called_with(
            "Error reading file test.md: Cannot read file"
        )


def test_convert_md_to_html() -> None:
    converter = MarkdownToHtmlConverter()
    md_content = "# Test Markdown\n\nTest!"
    html_content = converter._convert_md_content_to_html_content(md_content)
    assert (
        "<h1>Test Markdown</h1>" in html_content
    ), "HTML content should contain '<h1>Test Markdown\n\nTest!'"


def test_convert_md_to_html_error(mock_logger: MagicMock) -> None:
    converter = MarkdownToHtmlConverter(mock_logger)
    with patch("markdown.markdown", side_effect=Exception("Conversion error")):
        html_content = converter._convert_md_content_to_html_content(
            "invalid markdown"
        )
        assert html_content == ""
        mock_logger.error.assert_called_with(
            "Error converting Markdown to HTML: Conversion error"
        )


def test_write_html_file(
    setup_test_environment: Tuple[str, str, str, str]
) -> None:
    test_dir, _, _, html_filename = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._IO_DIRECTORY = test_dir
    html_content = "<h1>Test Markdown</h1>\n\n<p>Test!</p>"
    converter._write_html_file(html_filename, html_content)

    with open(
        os.path.join(test_dir, html_filename), "r", encoding="utf-8"
    ) as f:
        written_content = f.read()

    assert (
        written_content == html_content
    ), f"Expected: {html_content}, but got: {written_content}"


def test_write_html_file_error(mock_logger: MagicMock) -> None:
    converter = MarkdownToHtmlConverter(mock_logger)
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = IOError("Cannot write file")
        converter._IO_DIRECTORY = "non_existing_dir"
        converter._write_html_file("non_existing_file.html", "content")
        mock_logger.error.assert_called_with(
            "Error writing file non_existing_file.html: Cannot write file"
        )


def test_main(
    setup_test_environment: Tuple[str, str, str, str], mock_logger: MagicMock
) -> None:
    test_dir, _, _, html_filename = setup_test_environment
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = test_dir
    converter.main()

    assert os.path.exists(
        os.path.join(test_dir, html_filename)
    ), f"{html_filename} should exist in {test_dir}"
    mock_logger.info.assert_called_with(
        "Congratulations! Markdown to HTML conversion completed!!!"
        " Your files are now shiny HTML!"
    )


def test_main_no_md_files(
    setup_empty_directory: str, mock_logger: MagicMock
) -> None:
    test_dir = setup_empty_directory
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = test_dir
    converter.main()
    mock_logger.info.assert_called_with("No Markdown files found.")


def test_main_convert_md_content_to_html_content_empty(
    setup_test_environment: Tuple[str, str, str, str], mock_logger: MagicMock
) -> None:
    test_dir, md_filename, _, _ = setup_test_environment
    converter = MarkdownToHtmlConverter(mock_logger)
    converter._IO_DIRECTORY = test_dir

    with patch.object(converter, "_get_md_files", return_value=[md_filename]):
        with patch.object(
            converter, "_convert_md_content_to_html_content", return_value=""
        ):
            converter.main()
            mock_logger.info.assert_any_call(
                "Starting Markdown to HTML conversion."
            )
            mock_logger.error.assert_not_called()
