from .base import LlamaClient, console
from rich.panel import Panel

class TimelineBuilder:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a historical timeline expert extracting 
        and organizing temporal information from documents."""
    
    def build_timeline(self, document_text: str) -> str:
        console.print(Panel("📅 Building Historical Timeline", style="green"))
        prompt = f"""Extract all temporal references and build a timeline:

Document:
{document_text}

Create:
1. Explicit Dates Mentioned
2. Implied Time References
3. Relative Time Markers
4. Duration References
5. Chronological Sequence of Events
6. Timeline Visualization (ASCII)

Format: DATE/PERIOD | EVENT | SIGNIFICANCE | SOURCE QUOTE"""
        return self.client.generate(prompt, self.system)
