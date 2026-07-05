# Knowledge Base Data Model

## BugRecord Schema

| Field | Description |
|-------|-------------|
| id | Unique defect ID |
| title | Bug title |
| description | Bug description |
| logs | Error logs |
| stack_trace | Stack traces |
| severity | Severity level |
| priority | Priority |
| component | System module |
| resolution | Previous fix |
| source_dataset | Mozilla / Apache / Eclipse |
| embedding | Vector representation |

---

## Example Record

```json
{
  "id": "MOZ_1001",
  "title": "NullPointerException during login",
  "description": "Application crashes on login",
  "severity": "Critical",
  "priority": "P1",
  "component": "Authentication",
  "resolution": "Initialize object before access",
  "source_dataset": "Mozilla"
}
```

---

## Dataset Information

### Dataset Source
Eclipse Bugzilla Dataset

### Original Dataset Size
10,000 bug reports

### Selected Dataset Size
5,000 bug reports

### Selection Strategy
Although the Eclipse dataset contained 10,000 bug reports, a representative subset of 5,000 defects was selected for Milestone 1 to satisfy project requirements while maintaining efficient embedding generation and retrieval performance.

---

## Embedding Configuration

### Embedding Model
SentenceTransformer (`all-MiniLM-L6-v2`)

### Embedding Dimension
384

### Chunk Size
500 characters

### Vector Database
ChromaDB

### Similarity Metric
Cosine Similarity

---

## Knowledge Base Purpose

The Historical Defect Knowledge Base supports:

- Duplicate bug detection
- Similarity matching
- Root cause analysis
- Resolution recommendation
- Retrieval-Augmented Generation (RAG)

## Document Chunking

Chunking Strategy:
Fixed-size chunking

Chunk Size:
500 characters

Purpose:

• Improve semantic retrieval
• Enable efficient embedding generation
• Support similarity search
• Reduce context size for RAG

## Vector Store Configuration

Vector Database:
ChromaDB

Collection Name:
bug_reports

Embedding Model:
all-MiniLM-L6-v2

Embedding Dimension:
384

Indexed Documents:
5000

Persistence:
Local Storage (chroma_db/)
## Retrieval Pipeline

1. User submits a defect description

2. Query embedding generated using
all-MiniLM-L6-v2

3. ChromaDB performs similarity search

4. Top-K historical defects retrieved

5. Results returned for analysis

Similarity Metric:
Cosine Similarity

Top-K:
5