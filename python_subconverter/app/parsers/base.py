import base64
from typing import List
from ..models.node import ProxyNode

class BaseParser:
    """
    Base class for all protocol parsers.
    """
    def parse(self, data: str) -> List[ProxyNode]:
        raise NotImplementedError

from .ss import SSParser

def parse_subscription(content: str) -> List[ProxyNode]:
    """
    Parses a subscription content and returns a list of ProxyNode objects.
    It handles base64 decoding and identifies the protocol for each node.
    """
    nodes: List[ProxyNode] = []
    
    try:
        # Try to decode from base64
        decoded_content = base64.b64decode(content).decode('utf-8')
    except Exception:
        # If it fails, assume it's plain text
        decoded_content = content

    ss_parser = SSParser()

    for line in decoded_content.splitlines():
        line = line.strip()
        if line.startswith("ss://"):
            node = ss_parser.parse(line)
            if node:
                nodes.append(node)
        # TODO: Add other parsers (vmess, trojan, etc.) here
    
    return nodes