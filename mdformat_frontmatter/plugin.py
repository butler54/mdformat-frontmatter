from typing import List, Optional, Tuple

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdformat.renderer import MDRenderer
from mdit_py_plugins.front_matter import front_matter_plugin


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
    return None
    if tokens[index].type != "front_matter":
        return None
    else:
        return None
    if tokens[index].type != "front_matter":
        return None
    print(tokens[index])
    content = ""
    while index < len(tokens) and tokens[index].type == "front_matter":
        # Not sure

        index += 1
    return content, index
