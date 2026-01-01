from .base import LlamaClient, console
from rich.panel import Panel

class LanguageAnalyzer:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a historical linguistics expert specializing in 
        archaic languages, dialectal variations, and linguistic evolution."""
    
    def analyze(self, document_text: str) -> str:
        console.print(Panel("🔤 Analyzing Historical Language", style="cyan"))
        prompt = f"""Perform linguistic analysis on this historical text:

1. Language Identification (including dialects/variants)
2. Archaic Terms and Their Modern Equivalents
3. Grammatical Structures (compare to modern usage)
4. Spelling Conventions and Variations
5. Script/Writing System Analysis
6. Sociolinguistic Markers (formal/informal, class indicators)

Text:
{document_text}"""
        return self.client.generate(prompt, self.system)
