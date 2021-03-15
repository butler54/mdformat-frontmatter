from typing import List, Optional, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
import mdformat.renderer
from mdformat.renderer import MDRenderer
from mdit_py_plugins.front_matter import front_matter_plugin
from yaml import YAMLError, dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    mdit.use(front_matter_plugin)


def render_token(
    renderer: MDRenderer,
    tokens: List[Token],
    index: int,
    options: dict,
    env: dict,
) -> Optional[Tuple[str, int]]:
    """Convert token(s) to a string, or return None if no render method available.

    :returns: (text, index) where index is of the final "consumed" token
    """
    token = tokens[index]
    if token.type != "front_matter":
        return None
    # Safety check - parse and dump yaml to ensure it is correctly formatted
    try:
        yamled = load(token.content, Loader=Loader)
        serialized = dump(yamled, Dumper=Dumper)
        content = token.markup + "\n" + serialized + token.markup + "\n"
    except YAMLError:
        mdformat.renderer.LOGGER.warning("Invalid YAML in a front matter block")

        content = token.markup + "\n" + token.content + token.markup + "\n"

    return content, index
