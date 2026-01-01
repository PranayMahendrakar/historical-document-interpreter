from .base import LlamaClient, console
from rich.panel import Panel

class AnnotationEngine:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a scholarly annotation expert creating 
        comprehensive footnotes and marginalia for historical documents."""
    
    def annotate(self, document_text: str) -> str:
        console.print(Panel("📝 Creating Scholarly Annotations", style="blue"))
        prompt = f"""Create scholarly annotations for this historical document:

For each significant element, provide:
- [1] Person annotations (biographical info)
- [2] Place annotations (historical geography)
- [3] Event annotations (historical context)
- [4] Term annotations (definitions, etymology)
- [5] Cross-references to other historical sources

Document:
{document_text}"""
        return self.client.generate(prompt, self.system)
