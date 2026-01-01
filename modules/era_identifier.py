from .base import LlamaClient, console
from rich.panel import Panel

class EraIdentifier:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a historical era identification expert.
        Analyze linguistic patterns, references, and context to date documents."""
    
    def identify_era(self, document_text: str) -> str:
        console.print(Panel("⏳ Identifying Historical Era", style="yellow"))
        prompt = f"""Analyze this document to identify its historical era:

1. Linguistic Dating Clues (vocabulary, spelling, grammar)
2. Historical References (events, figures, institutions)
3. Cultural Context Markers
4. Material Culture References
5. Estimated Date Range with Confidence Level
6. Supporting Evidence

Document:
{document_text}"""
        return self.client.generate(prompt, self.system)
