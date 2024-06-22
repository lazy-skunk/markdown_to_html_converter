import os
import pytest
from markdown_to_html_converter import MarkdownToHtmlConverter

@pytest.fixture(scope="module")
def setup_test_environment():
    _test_dir = 'test_dir'
    _md_filename = 'test.md'
    _html_filename = 'test.html'

    os.makedirs(_test_dir, exist_ok=True)

    with open(os.path.join(_test_dir, _md_filename), 'w', encoding='utf-8') as f:
        f.write('# Test Markdown\n\nTest!')

    yield _test_dir, _md_filename, _html_filename

    os.remove(os.path.join(_test_dir, _md_filename))
    if os.path.exists(os.path.join(_test_dir, _html_filename)):
        os.remove(os.path.join(_test_dir, _html_filename))
    os.rmdir(_test_dir)

def test_get_md_files(setup_test_environment):
    test_dir, md_filename, _ = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._CURRENT_DIRECTORY = test_dir
    md_files = converter._get_md_files()
    assert md_filename in md_files

def test_read_md_file(setup_test_environment):
    test_dir, md_filename, _ = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._CURRENT_DIRECTORY = test_dir
    content = converter._read_md_file(md_filename)
    assert content == '# Test Markdown\n\nTest!'

def test_convert_md_to_html():
    converter = MarkdownToHtmlConverter()
    md_content = '# Test Markdown\n\nTest!'
    html_content = converter._convert_md_content_to_html_content(md_content)
    assert '<h1>Test Markdown</h1>' in html_content

def test_write_html_file(setup_test_environment):
    test_dir, _, html_filename = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._CURRENT_DIRECTORY = test_dir
    html_content = '<h1>Test Markdown</h1>\n\n<p>Test!</p>'
    converter._write_html_file(html_filename, html_content)
    
    with open(os.path.join(test_dir, html_filename), 'r', encoding='utf-8') as f:
        written_content = f.read()
    
    assert written_content == html_content

def test_main(setup_test_environment):
    test_dir, _, html_filename = setup_test_environment
    converter = MarkdownToHtmlConverter()
    converter._CURRENT_DIRECTORY = test_dir
    converter.main()
    
    assert os.path.exists(os.path.join(test_dir, html_filename))