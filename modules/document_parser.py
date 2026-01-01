from .base import LlamaClient, console
from rich.panel import Panel

class DocumentParser:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are an expert historical document parser. 
        Analyze document structure, identify key sections, extract metadata, 
        and recognize document types (letters, decrees, treaties, etc.)."""
    
    def parse(self, document_text: str) -> str:
        console.print(Panel("📜 Parsing Historical Document", style="blue"))
        prompt = f"""Analyze this historical document and provide:
1. Document Type (letter, decree, treaty, record, etc.)
2. Structural Elements (greeting, body, signature, seals)
3. Key Entities Mentioned (people, places, organizations)
4. Estimated Time Period
5. Language/Script Used
6. Preservation State Indicators

Document:
{document_text}"""
        return self.client.generate(prompt, self.system)
    
    def extract_metadata(self, document_text: str) -> dict:
        prompt = f"""Extract metadata from this historical document as JSON:
- author, recipient, date, location, document_type, language, key_topics

Document: {document_text}"""
        response = self.client.generate(prompt, self.system, stream=False)
        return {"raw_analysis": response}
