#!/usr/bin/env python3
"""
Historical Document Interpreter
A Llama-based system for analyzing and interpreting historical texts.
Author: Pranay M
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from modules import (
    DocumentParser, EraIdentifier, LanguageAnalyzer,
    ContextProvider, AuthenticityChecker, TranslationAssistant,
    AnnotationEngine, ComparisonTool, TimelineBuilder, ExportManager
)

console = Console()

SAMPLE_DOCUMENT = """
Wee the People of the United States, in Order to form a more perfect Union, 
establish Justice, insure domestick Tranquility, provide for the common defence, 
promote the general Welfare, and secure the Blessings of Liberty to ourselves 
and our Posterity, do ordain and establish this Constitution for the United 
States of America.
"""

def show_menu():
    table = Table(title="📜 Historical Document Interpreter", show_header=True)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Tool", style="green")
    table.add_column("Description", style="white")
    
    tools = [
        ("1", "Document Parser", "Parse structure and extract metadata"),
        ("2", "Era Identifier", "Identify historical period and date"),
        ("3", "Language Analyzer", "Analyze archaic language and terms"),
        ("4", "Context Provider", "Get historical background context"),
        ("5", "Authenticity Checker", "Check for anachronisms and forgery"),
        ("6", "Translation Assistant", "Translate to modern language"),
        ("7", "Annotation Engine", "Create scholarly annotations"),
        ("8", "Comparison Tool", "Compare two documents"),
        ("9", "Timeline Builder", "Build timeline from document"),
        ("10", "Export Manager", "Export analysis report"),
        ("11", "Full Analysis", "Run complete analysis pipeline"),
        ("0", "Exit", "Exit the program")
    ]
    
    for opt, tool, desc in tools:
        table.add_row(opt, tool, desc)
    
    console.print(table)

def get_document_input() -> str:
    console.print("\n[yellow]Enter your historical document text.[/yellow]")
    console.print("[dim]Type 'SAMPLE' to use sample document, or 'END' on a new line when done:[/dim]\n")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip().upper() == "SAMPLE":
            console.print("[green]Using sample document (US Constitution Preamble)[/green]")
            return SAMPLE_DOCUMENT
        lines.append(line)
    
    return "\n".join(lines) if lines else SAMPLE_DOCUMENT

def main():
    console.print(Panel.fit(
        "[bold blue]📜 Historical Document Interpreter[/bold blue]\n"
        "[dim]Powered by Llama - Analyze and interpret historical texts[/dim]",
        border_style="blue"
    ))
    
    # Initialize tools
    parser = DocumentParser()
    era_id = EraIdentifier()
    lang_analyzer = LanguageAnalyzer()
    context = ContextProvider()
    auth_checker = AuthenticityChecker()
    translator = TranslationAssistant()
    annotator = AnnotationEngine()
    comparator = ComparisonTool()
    timeline = TimelineBuilder()
    exporter = ExportManager()
    
    current_document = None
    analyses = {}
    
    while True:
        show_menu()
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", default="1")
        
        if choice == "0":
            console.print("[yellow]Goodbye! Happy researching![/yellow]")
            break
        
        if choice in ["1", "2", "3", "4", "5", "6", "7", "9", "11"]:
            if not current_document or Confirm.ask("Enter new document?", default=False):
                current_document = get_document_input()
        
        try:
            if choice == "1":
                result = parser.parse(current_document)
                analyses["document_structure"] = result
                
            elif choice == "2":
                result = era_id.identify_era(current_document)
                analyses["era_identification"] = result
                
            elif choice == "3":
                result = lang_analyzer.analyze(current_document)
                analyses["language_analysis"] = result
                
            elif choice == "4":
                era = Prompt.ask("Known era (or press Enter to detect)", default="")
                result = context.provide_context(current_document, era if era else None)
                analyses["historical_context"] = result
                
            elif choice == "5":
                claimed_era = Prompt.ask("Claimed era of the document")
                result = auth_checker.check_authenticity(current_document, claimed_era)
                analyses["authenticity_check"] = result
                
            elif choice == "6":
                target = Prompt.ask("Target language", default="modern English")
                result = translator.translate(current_document, target)
                analyses["translation"] = result
                
            elif choice == "7":
                result = annotator.annotate(current_document)
                analyses["annotations"] = result
                
            elif choice == "8":
                console.print("[yellow]Enter first document:[/yellow]")
                doc1 = get_document_input()
                console.print("[yellow]Enter second document:[/yellow]")
                doc2 = get_document_input()
                result = comparator.compare_documents(doc1, doc2)
                analyses["document_comparison"] = result
                
            elif choice == "9":
                result = timeline.build_timeline(current_document)
                analyses["timeline"] = result
                
            elif choice == "10":
                if not analyses:
                    console.print("[red]No analyses to export. Run some tools first.[/red]")
                    continue
                fmt = Prompt.ask("Export format", choices=["markdown", "json"], default="markdown")
                result = exporter.export_analysis(analyses, fmt)
                
                filename = f"analysis_report.{'md' if fmt == 'markdown' else 'json'}"
                with open(filename, "w") as f:
                    f.write(result)
                console.print(f"[green]Report saved to {filename}[/green]")
                
            elif choice == "11":
                console.print(Panel("Running Full Analysis Pipeline", style="bold green"))
                analyses["document_structure"] = parser.parse(current_document)
                analyses["era_identification"] = era_id.identify_era(current_document)
                analyses["language_analysis"] = lang_analyzer.analyze(current_document)
                analyses["historical_context"] = context.provide_context(current_document)
                analyses["timeline"] = timeline.build_timeline(current_document)
                console.print(Panel("[green]Full analysis complete![/green]", style="green"))
                
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            console.print("[yellow]Make sure Ollama is running: ollama serve[/yellow]")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
