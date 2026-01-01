from .base import LlamaClient, console
from rich.panel import Panel

class ComparisonTool:
    def __init__(self):
        self.client = LlamaClient()
        self.system = """You are a comparative historical analysis expert 
        examining relationships between historical documents."""
    
    def compare_documents(self, doc1: str, doc2: str) -> str:
        console.print(Panel("⚖️ Comparing Historical Documents", style="yellow"))
        prompt = f"""Compare these two historical documents:

Document 1:
{doc1[:1500]}

Document 2:
{doc2[:1500]}

Analyze:
1. Temporal Relationship (which is earlier/later)
2. Authorship Similarities/Differences
3. Thematic Connections
4. Linguistic Evolution (if from different periods)
5. Historical Relationship (response, copy, related event)
6. Contradictions or Confirmations"""
        return self.client.generate(prompt, self.system)
