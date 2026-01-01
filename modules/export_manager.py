from .base import LlamaClient, console
from rich.panel import Panel
import json
from datetime import datetime

class ExportManager:
    def __init__(self):
        self.client = LlamaClient()
    
    def export_analysis(self, analyses: dict, format: str = "markdown") -> str:
        console.print(Panel(f"💾 Exporting Analysis as {format.upper()}", style="cyan"))
        
        if format == "markdown":
            return self._to_markdown(analyses)
        elif format == "json":
            return json.dumps(analyses, indent=2)
        else:
            return str(analyses)
    
    def _to_markdown(self, analyses: dict) -> str:
        md = f"# Historical Document Analysis Report\n\n"
        md += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        for section, content in analyses.items():
            md += f"## {section.replace('_', ' ').title()}\n\n"
            md += f"{content}\n\n"
            md += "---\n\n"
        
        return md
    
    def generate_report(self, document: str) -> str:
        prompt = f"""Generate a comprehensive scholarly report for this historical document:

Document: {document}

Include: Executive Summary, Detailed Analysis, Historical Context, 
Authenticity Assessment, Recommendations for Further Research."""
        return self.client.generate(prompt)
