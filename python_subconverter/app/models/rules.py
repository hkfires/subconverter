from pydantic import BaseModel
from typing import List, Optional

class RuleSet(BaseModel):
    """
    Represents a single ruleset configuration.
    e.g., "🍎 苹果服务,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Apple.list"
    """
    group_name: str
    type: str = "surge"  # Default type
    url: str
    interval: Optional[int] = None

class ProxyGroup(BaseModel):
    """
    Represents a proxy group configuration.
    e.g., "Proxy`select`.*`[]AUTO`[]DIRECT`.*"
    """
    name: str
    type: str  # "select", "url-test", "fallback", etc.
    rules: List[str]
    test_url: Optional[str] = None
    interval: Optional[int] = None
    tolerance: Optional[int] = None