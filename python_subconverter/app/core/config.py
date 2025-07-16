from pydantic import BaseModel
from typing import Optional, List
from ..models.rules import RuleSet, ProxyGroup

class Settings(BaseModel):
    """
    This class holds all the configuration settings for the application.
    It mirrors the structure of pref.ini and URL parameters.
    We will expand this model as we implement more features.
    """
    # [common]
    clash_rule_base: str = "base/base/GeneralClashConfig.yml"
    surge_rule_base: str = "base/base/surge.conf"
    
    # [node_pref]
    udp_flag: bool = False
    include_remarks: Optional[str] = None
    exclude_remarks: Optional[str] = None

    # [ruleset] & [proxy_group]
    rulesets: List[RuleSet] = []
    proxy_groups: List[ProxyGroup] = []
    
    # ... more settings to come