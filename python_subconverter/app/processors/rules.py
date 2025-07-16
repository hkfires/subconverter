import requests
from typing import List
from ..models.rules import RuleSet

class RuleProcessor:
    """
    Fetches and processes ruleset content from local files or URLs.
    """
    def __init__(self, rulesets: List[RuleSet]):
        self.rulesets = rulesets

    def get_ruleset_content(self, ruleset: RuleSet) -> str:
        """
        Fetches the content of a single ruleset.
        """
        if ruleset.url.startswith("http"):
            try:
                return requests.get(ruleset.url, timeout=5).text
            except requests.RequestException:
                return ""
        else:
            # Assume it's a local file path relative to the base dir
            try:
                with open(f"./python_subconverter/{ruleset.url}", "r", encoding="utf-8") as f:
                    return f.read()
            except FileNotFoundError:
                return ""

    def process(self) -> List[str]:
        """
        Processes all rulesets and returns a list of their content.
        """
        all_rules_content: List[str] = []
        for ruleset in self.rulesets:
            content = self.get_ruleset_content(ruleset)
            if content:
                # TODO: Add logic to convert between different rule formats
                all_rules_content.append(content)
        
        return all_rules_content