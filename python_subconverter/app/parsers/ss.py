import base64
import re
from typing import List, Optional
from urllib.parse import unquote, urlparse
from ..models.node import ProxyNode
from .base import BaseParser

class SSParser(BaseParser):
    """
    Parses Shadowsocks (ss://) links.
    """
    def parse(self, link: str) -> Optional[ProxyNode]:
        match = re.match(r"ss://(?P<encoded_part>.+)", link)
        if not match:
            return None

        encoded_part = match.group("encoded_part")
        
        try:
            # Decode the main part
            decoded_part = base64.urlsafe_b64decode(encoded_part.split('#')[0] + '==').decode('utf-8')
            
            # Extract name from after the hash
            name = unquote(encoded_part.split('#')[1]) if '#' in encoded_part else "SS Node"
            
            # Parse the decoded part
            parts = decoded_part.split(':')
            cipher = parts[0]
            password_server = parts[1]
            
            password, server = password_server.split('@')
            server_address, port = server.split(':')

            return ProxyNode(
                name=name,
                type="ss",
                server=server_address,
                port=int(port),
                cipher=cipher,
                password=password,
            )
        except Exception:
            return None