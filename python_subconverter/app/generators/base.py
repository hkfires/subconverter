from jinja2 import Environment, FileSystemLoader
from typing import List
from ..models.node import ProxyNode
from ..core.config import Settings

class BaseGenerator:
    """
    Base class for all configuration generators.
    """
    def __init__(self, settings: Settings):
        self.settings = settings
        self.env = Environment(loader=FileSystemLoader("./python_subconverter/base/"))

    def render_template(self, template_name: str, nodes: List[ProxyNode], **kwargs) -> str:
        """
        Renders a Jinja2 template with the given context.
        """
        template = self.env.get_template(template_name)
        return template.render(nodes=nodes, **kwargs)

    def generate(self, nodes: List[ProxyNode]) -> str:
        """
        Generates the final configuration file.
        """
        raise NotImplementedError