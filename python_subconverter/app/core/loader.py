import configparser
import yaml
import tomli
from pathlib import Path
from .config import Settings

def load_settings() -> Settings:
    """
    Loads settings from pref.toml, pref.yml, or pref.ini in order of priority.
    """
    base_path = Path("./python_subconverter")
    config_data = {}

    # For now, we only implement INI loading. TOML and YAML will be added later.
    ini_path = base_path / "pref.ini"
    if ini_path.exists():
        parser = configparser.ConfigParser()
        parser.read(ini_path)
        for section in parser.sections():
            for key, value in parser.items(section):
                config_data[key] = value
    
    return Settings(**config_data)
