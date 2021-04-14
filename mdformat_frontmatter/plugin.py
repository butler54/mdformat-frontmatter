import io
from typing import Mapping

from markdown_it import MarkdownIt
import mdformat.renderer
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer.typing import Postprocess, Render
from mdit_py_plugins.front_matter import front_matter_plugin
import ruamel.yaml


def update_mdit(mdit: MarkdownIt) -> None:
    """Update the parser, e.g. by adding a plugin: `mdit.use(myplugin)`"""
    mdit.use(front_matter_plugin)


def _render_frontmatter(node: RenderTreeNode, context: RenderContext) -> str:
    # Safety check - parse and dump yaml to ensure it is correctly formatted
    try:
        yaml = ruamel.yaml.YAML()
        # Make sure to always have `sequence >= offset + 2`
        yaml.indent(mapping=2, sequence=4, offset=2)
        parsed = yaml.load(node.content)
        dump_stream = io.StringIO()
        yaml.dump(parsed, stream=dump_stream)
        formatted_yaml = dump_stream.getvalue()
    except Exception as e:
        mdformat.renderer.LOGGER.warning(f"Invalid YAML in a front matter block: {e}.")
        formatted_yaml = node.content

    return node.markup + "\n" + formatted_yaml + node.markup


RENDERERS: Mapping[str, Render] = {"front_matter": _render_frontmatter}

POSTPROCESSORS: Mapping[str, Postprocess] = {}
