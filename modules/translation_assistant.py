from .base import LlamaClient, console
from rich.panel import Panel

class TranslationAssistant:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a historical document translator preserving 
        nuance, context, and period-appropriate meaning."""
    
    def translate(self, document_text: str, target_lang: str = "modern English") -> str:
        console.print(Panel(f"🌐 Translating to {target_lang}", style="magenta"))
        prompt = f"""Translate this historical document to {target_lang}:

Provide:
1. Direct Translation (preserving structure)
2. Modernized Translation (natural contemporary phrasing)
3. Translation Notes (difficult passages, ambiguities)
4. Cultural Concepts Requiring Explanation

Original:
{document_text}"""
        return self.client.generate(prompt, self.system)
