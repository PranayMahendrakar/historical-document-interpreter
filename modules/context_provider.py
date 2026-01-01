from .base import LlamaClient, console
from rich.panel import Panel

class ContextProvider:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a historical context expert providing rich 
        background information for document interpretation."""
    
    def provide_context(self, document_text: str, era: str = None) -> str:
        console.print(Panel("🌍 Providing Historical Context", style="green"))
        era_info = f"Era: {era}" if era else "Era: To be determined from text"
        prompt = f"""Provide comprehensive historical context for this document:

{era_info}

1. Political Context (rulers, governments, conflicts)
2. Social Context (class structure, daily life, customs)
3. Economic Context (trade, currency, economic systems)
4. Cultural Context (religion, arts, education)
5. Related Historical Events
6. Key Figures of the Period

Document:
{document_text}"""
        return self.client.generate(prompt, self.system)
