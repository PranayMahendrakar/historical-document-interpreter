from .base import LlamaClient, console
from rich.panel import Panel

class AuthenticityChecker:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a document authenticity expert analyzing 
        historical documents for anachronisms and signs of forgery."""
    
    def check_authenticity(self, document_text: str, claimed_era: str) -> str:
        console.print(Panel("🔍 Checking Document Authenticity", style="red"))
        prompt = f"""Analyze this document for authenticity indicators:

Claimed Era: {claimed_era}

Check for:
1. Anachronistic Language (words/phrases from wrong period)
2. Anachronistic References (events, technology, concepts)
3. Stylistic Consistency with Period
4. Logical Consistency
5. Common Forgery Indicators
6. Authenticity Confidence Score (1-10)
7. Recommendations for Further Verification

Document:
{document_text}"""
        return self.client.generate(prompt, self.system)
