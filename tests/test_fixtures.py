from pathlib import Path

from markdown_it.utils import read_fixture_file
from mdformat import text as render_text
import pytest

FIXTURE_PATH = Path(__file__).parent / "fixtures.md"
SIMPLE_MD_TEST_PATH = Path(__file__).parent / "simple-md-test.md"
fixtures = read_fixture_file(FIXTURE_PATH)


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures, ids=[f[1] for f in fixtures]
)
def test_fixtures(line, title, text, expected):
    output = render_text(text, extensions={"frontmatter"})
    print(output)
    assert output.rstrip() == expected.rstrip(), output


def test_simple_md() -> None:
    """Simple test of """
    md_content = SIMPLE_MD_TEST_PATH.read_text()
    output = render_text(md_content, extensions={"frontmatter"})
    print(output)
    assert output.rstrip() == md_content.rstrip()
