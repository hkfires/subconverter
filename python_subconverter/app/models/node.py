from pydantic import BaseModel
from typing import Optional

class ProxyNode(BaseModel):
    """
    A standard data model for a proxy node.
    This class will be used to represent all types of nodes internally.
    """
    # Basic info
    name: str
    type: str  # e.g., "ss", "vmess", "trojan"
    server: str
    port: int

    # Encryption and authentication
    cipher: Optional[str] = None
    password: Optional[str] = None
    
    # Vmess specific
    uuid: Optional[str] = None
    alter_id: Optional[int] = None
    
    # Transport settings
    network: Optional[str] = "tcp"  # "tcp", "ws", etc.
    ws_path: Optional[str] = None
    ws_headers: Optional[dict] = None
    
    # TLS settings
    tls: Optional[bool] = False
    sni: Optional[str] = None
    skip_cert_verify: Optional[bool] = False

    # Other attributes
    group: Optional[str] = None