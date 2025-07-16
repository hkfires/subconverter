from fastapi import FastAPI, Request
import requests
from typing import Optional

from .core.config import Settings
from fastapi.responses import PlainTextResponse
from .core.loader import load_settings
from .parsers.base import parse_subscription
from .processors.node import NodeProcessor
from .processors.rules import RuleProcessor
from .generators.clash import ClashGenerator

app = FastAPI(
    title="Python SubConverter",
    description="A Python-based utility to convert between various subscription formats.",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Python SubConverter"}

@app.get("/sub", response_class=PlainTextResponse)
async def subconverter(
    request: Request,
    target: str,
    url: str,
    config: Optional[str] = None,
    include: Optional[str] = None,
    exclude: Optional[str] = None,
):
    """
    The main endpoint for subscription conversion.
    """
    # 1. Load settings
    settings = load_settings()

    # 2. Override settings with URL parameters
    if include:
        settings.include_remarks = include
    if exclude:
        settings.exclude_remarks = exclude

    # 3. Fetch subscription content
    try:
        sub_content = requests.get(url, timeout=5).text
    except requests.RequestException as e:
        return f"Error: Failed to fetch subscription: {e}"

    # 4. Parse subscription
    nodes = parse_subscription(sub_content)

    # 5. Process nodes
    node_processor = NodeProcessor(settings)
    processed_nodes = node_processor.process(nodes)

    # 6. Select generator based on target
    if target.lower() == "clash":
        generator = ClashGenerator(settings)
    else:
        return f"Error: Target '{target}' is not supported yet."

    # 7. Generate final config
    final_config = generator.generate(processed_nodes)
    
    return final_config