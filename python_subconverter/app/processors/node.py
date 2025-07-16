import re
from typing import List
from ..models.node import ProxyNode
from ..core.config import Settings

class NodeProcessor:
    """
    Processes a list of ProxyNode objects based on the given settings.
    This includes filtering, renaming, and other manipulations.
    """
    def __init__(self, settings: Settings):
        self.settings = settings

    def process(self, nodes: List[ProxyNode]) -> List[ProxyNode]:
        processed_nodes = nodes

        # Include remarks filter
        if self.settings.include_remarks:
            try:
                include_regex = re.compile(self.settings.include_remarks)
                processed_nodes = [node for node in processed_nodes if include_regex.search(node.name)]
            except re.error:
                # Ignore invalid regex
                pass

        # Exclude remarks filter
        if self.settings.exclude_remarks:
            try:
                exclude_regex = re.compile(self.settings.exclude_remarks)
                processed_nodes = [node for node in processed_nodes if not exclude_regex.search(node.name)]
            except re.error:
                # Ignore invalid regex
                pass
        
        return processed_nodes
