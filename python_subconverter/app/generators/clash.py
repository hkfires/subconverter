import yaml
from typing import List
from .base import BaseGenerator
from ..models.node import ProxyNode

class ClashGenerator(BaseGenerator):
    """
    Clash configuration generator.
    """
    def generate(self, nodes: List[ProxyNode]) -> str:
        """
        Generates a Clash configuration file.
        """
        # Load the base Clash config
        base_config_str = self.render_template(self.settings.clash_rule_base, nodes)
        config = yaml.safe_load(base_config_str)

        # Add proxies to the config
        config['proxies'] = [self.format_node(node) for node in nodes]

        # Add proxy groups (basic implementation for now)
        if 'proxy-groups' not in config:
            config['proxy-groups'] = []
        
        all_node_names = [node.name for node in nodes]
        
        # Create a basic "Proxy" group
        config['proxy-groups'].insert(0, {
            'name': 'PROXY',
            'type': 'select',
            'proxies': ['AUTO', 'DIRECT'] + all_node_names
        })

        # Create a basic "AUTO" group
        config['proxy-groups'].insert(1, {
            'name': 'AUTO',
            'type': 'url-test',
            'proxies': all_node_names,
            'url': 'http://www.gstatic.com/generate_204',
            'interval': 300
        })

        return yaml.dump(config, allow_unicode=True, sort_keys=False)

    def format_node(self, node: ProxyNode) -> dict:
        """
        Formats a ProxyNode object into a Clash-compatible dictionary.
        """
        # This is a simplified formatter. We will expand it later.
        return {
            'name': node.name,
            'type': node.type,
            'server': node.server,
            'port': node.port,
            'cipher': node.cipher,
            'password': node.password,
        }