from typing import Mapping, MutableMapping

from markdown_it import MarkdownIt
import mdformat.renderer
from mdformat.renderer import RenderTreeNode
from mdformat.renderer.typing import RendererFunc
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


def _render_frontmatter(
    node: RenderTreeNode,
    renderer_funcs: Mapping[str, RendererFunc],
    options: Mapping,
    env: MutableMapping,
) -> str:
    # Safety check - parse and dump yaml to ensure it is correctly formatted
    try:
        yamled = load(node.content, Loader=Loader)
        formatted_yaml = dump(yamled, Dumper=Dumper)
    except YAMLError:
        mdformat.renderer.LOGGER.warning("Invalid YAML in a front matter block")
        formatted_yaml = node.content

    return node.markup + "\n" + formatted_yaml + node.markup


RENDERER_FUNCS: Mapping[str, RendererFunc] = {"front_matter": _render_frontmatter}
