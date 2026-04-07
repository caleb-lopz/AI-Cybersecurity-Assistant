

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from pathlib import Path
import requests
from sentence_transformers import SentenceTransformer
from docling.chunking import HybridChunker
import chromadb 



pdf_path = Path(r"C:\Users\López\Desktop\API_PRUEBA\NIST.CSWP.29.pdf")


conv = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(backend=PyPdfiumDocumentBackend)
    }
)

doc = conv.convert(pdf_path).document

chunker = HybridChunker(max_tokens = 256)
chunks = list(chunker.chunk(dl_doc = doc))

embedder = SentenceTransformer("all-MiniLM-L6-v2")
texts = [chunk.text for chunk in chunks]
client = chromadb.PersistentClient(path="./chroma_db")
embeddings = embedder.encode(texts, 
    show_progress_bar=True,
    batch_size=8,          
)

cybersec_pdf = pdf_path.stem.replace(" ", "_")
collection = client.get_or_create_collection(name = "cybersec")

collection.add(ids = [f"chunk{i}" for i in range(len(chunks))],
               embeddings = embeddings.tolist(),
               documents = texts,
               metadatas = [{"chunk_index": i, "source": str(cybersec_pdf)} for i in range(len(chunks))])



