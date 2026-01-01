# 📜 Historical Document Interpreter

A Llama-based AI system that helps historians analyze and interpret historical texts.

**Author:** Pranay M

## 🌟 Features

| Module | Description |
|--------|-------------|
| **Document Parser** | Parse structure and extract metadata |
| **Era Identifier** | Identify historical period and date documents |
| **Language Analyzer** | Analyze archaic language, terms, and grammar |
| **Context Provider** | Get rich historical background context |
| **Authenticity Checker** | Check for anachronisms and forgery signs |
| **Translation Assistant** | Translate to modern language |
| **Annotation Engine** | Create scholarly footnotes and annotations |
| **Comparison Tool** | Compare two historical documents |
| **Timeline Builder** | Build timeline from document references |
| **Export Manager** | Export analysis as Markdown or JSON |

## 🚀 Quick Start

```bash
# Start Ollama
ollama pull llama3.2
ollama serve

# Install dependencies
pip install -r requirements.txt

# Run the interpreter
python main.py
```

## 📁 Project Structure

```
51-historical-document-interpreter/
├── main.py                    # Main application
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── modules/
│   ├── __init__.py
│   ├── base.py               # Llama client
│   ├── document_parser.py    # Document parsing
│   ├── era_identifier.py     # Era identification
│   ├── language_analyzer.py  # Language analysis
│   ├── context_provider.py   # Historical context
│   ├── authenticity_checker.py # Authenticity checks
│   ├── translation_assistant.py # Translation
│   ├── annotation_engine.py  # Annotations
│   ├── comparison_tool.py    # Document comparison
│   ├── timeline_builder.py   # Timeline creation
│   └── export_manager.py     # Export functionality
├── data/                     # Sample documents
└── templates/                # Report templates
```

## 💡 Use Cases

- Analyze medieval manuscripts
- Date unknown historical documents
- Translate archaic texts
- Check document authenticity
- Create scholarly annotations
- Compare related documents

## 📄 License

MIT License - Pranay M
