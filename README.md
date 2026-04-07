# AI Cybersecurity Assistant — RAG with Docling + Gemini

A conversational AI assistant that answers cybersecurity questions by retrieving
relevant information from a PDF document using a RAG (Retrieval-Augmented
Generation) pipeline. Built as a practical, beginner-friendly project to learn
the fundamentals of document indexing, vector search, and LLM integration.

> If you are just starting to learn how to build AI-powered document readers,
> this is a great place to start. Every component here is a fundamental building
> block used in more advanced RAG systems.

---

## How it works

**Indexing (`indexing_docline_basics.py`)**
1. A PDF is loaded and converted into structured text using **Docling**
2. The text is split into chunks using **HybridChunker** (max 256 tokens)
3. Each chunk is embedded using **SentenceTransformer (all-MiniLM-L6-v2)**
4. Embeddings and text are stored in a local **ChromaDB** collection

**Querying (`query_docline_basics.py`)**
1. The user types a question in the terminal
2. The question is embedded using the same model
3. The top 5 most relevant chunks are retrieved from ChromaDB
4. A prompt is built with the retrieved context and sent to **Gemini 2.5 Flash**
5. The assistant responds in plain, easy-to-understand language
6. Chat history is maintained for follow-up questions

> Note: Responses may be slightly verbose since this pipeline uses basic
> similarity search without reranking. More advanced RAG strategies will
> be covered in future repositories.

---

## Project structure

```bash
AI-Cybersecurity-Assistant/
├── indexing_docline_basics.py   # PDF ingestion, chunking, and indexing
├── query_docline_basics.py      # Retrieval, prompting, and chat loop
├── chroma_db/                   # Local vector database (auto-generated)
├── .env                         # API key storage (not committed)
├── requirements.txt             # Python dependencies
└── README.md
```
---

## Important

- The indexing script only needs to be run **once** per document.
- To add more documents, loop through a list of PDF paths in
  `indexing_docline_basics.py`.
- Never commit your `.env` file — add it to `.gitignore`.

---

## Requirements

- Python 3.11 (virtual environment recommended)
- A [Gemini API key](https://aistudio.google.com/app/apikey)

Create a `.env` file in the root folder:

---

## Installation
```bash
git clone https://github.com/calab-lopz/cybersec-rag.git
cd cybersec-rag
python -m venv venv # 3.11 version recomended
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage

**Step 1 — Index your document**
```bash
python indexing_docline_basics.py
```

**Step 2 — Start the assistant**
```bash
python query_docline_basics.py
```
---
## demo
<img width="1430" height="466" alt="Captura de pantalla 2026-04-06 231207" src="https://github.com/user-attachments/assets/e28233dd-4e37-400b-be95-a43a4929f6fb" />

---

## Tech stack

| Tool | Purpose |
|------|---------|
| [Docling](https://github.com/DS4SD/docling) | PDF parsing and hybrid chunking |
| [SentenceTransformers](https://www.sbert.net) — all-MiniLM-L6-v2 | Text embeddings |
| [ChromaDB](https://www.trychroma.com) | Local vector database |
| [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini) | LLM response generation |
| [python-dotenv](https://pypi.org/project/python-dotenv) | API key management |

---

## What's next


This project covers the fundamentals. Future repositories in this series will
cover more advanced RAG strategies with increasing difficulty, including:

- Hybrid search (dense + keyword)
- Reranking with Cross-Encoders
- Multi-document retrieval
- Agentic RAG pipelines
