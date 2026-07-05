# AI Smart Bug Analyzer & Fix Advisor
This document presents the research conducted for Milestone 1 of the AI Smart Bug Analyzer & Fix Advisor project, focusing on defect analysis workflows, RAG systems, semantic similarity techniques, and bug report structures.

## Milestone 1 – Research Notes

### 1. Defect Analysis Workflow

Defect analysis is the process of identifying, categorizing, investigating, and resolving software defects efficiently.

A typical defect analysis workflow consists of the following stages:

**Bug Submission**

* Users submit bug reports, stack traces, crash reports, or error logs.
* The information can be entered manually or uploaded as files.

**Bug Triage**

* Determines the severity and priority of the defect.
* Assigns the defect to the appropriate component or development team.

**Duplicate Detection**

* Checks whether a similar defect has already been reported.
* Reduces duplicate effort and accelerates resolution.

**Log Analysis**

* Examines logs, exceptions, and stack traces.
* Identifies recurring patterns and error signatures.

**Root Cause Analysis**

* Determines the underlying cause of the defect.
* Examples include null pointer exceptions, configuration issues, dependency conflicts, and database failures.

**Fix Recommendation**

* Suggests possible solutions based on historical defects and previous resolutions.

**Knowledge Base Update**

* Newly resolved defects are added to the knowledge repository for future retrieval.

---

### 2. Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) combines information retrieval techniques with language models to provide context-aware responses.

Instead of relying solely on pre-trained knowledge, RAG retrieves relevant documents from a knowledge base before generating answers.

The RAG pipeline consists of the following stages:

Document Collection

↓

Preprocessing

↓

Chunking

↓

Embedding Generation

↓

Vector Database Storage

↓

Similarity Search

↓

Relevant Document Retrieval

↓

Language Model Processing

↓

Response Generation

#### Components of RAG

**Document Collection**

* Historical bug reports
* Mozilla datasets
* Apache datasets
* Eclipse datasets

**Chunking**
Large documents are divided into smaller segments to improve retrieval efficiency.

Benefits:

* Improved search quality
* Faster retrieval
* Better embedding generation

**Embeddings**
Embeddings convert text into numerical vectors while preserving semantic meaning.

Similar bug reports are positioned close together in vector space.

**Vector Database**
Stores embeddings for efficient retrieval.

Examples:

* ChromaDB
* FAISS
* Pinecone

**Similarity Search**
Retrieves the most relevant defects from historical datasets.

**Language Model**
Uses retrieved information to suggest:

* Root causes
* Duplicate reports
* Resolution recommendations

---

### 3. Semantic Similarity Techniques

Semantic similarity measures the degree to which two pieces of text convey the same meaning.

Example:

Bug Report A:
"NullPointerException in UserController"

Bug Report B:
"Application crashes because controller object is null."

Although the wording differs, both defects describe the same problem.

#### Cosine Similarity

Cosine similarity measures the angle between two embedding vectors.

Values range between:

* 0 → unrelated
* 1 → identical meaning

Cosine similarity is widely used in duplicate bug detection systems.

#### Sentence Transformers

Sentence Transformers generate dense vector representations of text.

Model considered for this project:

* all-MiniLM-L6-v2

Advantages:

* Lightweight
* Fast inference
* High semantic accuracy
* Suitable for RAG applications

#### SBERT

Sentence-BERT improves semantic similarity computation at the sentence level.

Applications:

* Duplicate defect detection
* Similarity matching
* Historical defect retrieval

---

### 4. Bug Report Structure

A structured bug report enables developers to reproduce issues quickly and identify defects efficiently.

Typical fields include:

* Title
* Description
* Environment
* Steps to Reproduce
* Expected Result
* Actual Result
* Error Logs
* Stack Trace
* Severity
* Priority
* Resolution

Example:

Title:
Login API throws NullPointerException

Environment:
Java 17
Spring Boot 3
Windows 11

Steps to Reproduce:

1. Open Login Page
2. Enter Credentials
3. Click Login

Expected Result:
User authentication succeeds.

Actual Result:
Application crashes.

Exception:
NullPointerException at UserController.java:42

Severity:
Critical

Priority:
High

---

### 5. Design Decisions

The following technologies have been selected for Milestone 1 implementation.
| Component            | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Backend Framework    | FastAPI                  |
| Frontend Prototype   | Streamlit                |
| Embedding Model          | Sentence Transformer(all-MiniLM-L6-v2)  |
| Vector Database      | ChromaDB                 |
| RAG Framework        | LangChain                |
| Similarity Technique | Cosine Similarity        |
| Dataset Sources      | Mozilla, Apache, Eclipse |
| Storage              | SQLite                   |
| Version Control      | GitHub                   |


#### Justification
Python was selected as the primary programming language due to its extensive ecosystem for Artificial Intelligence, Natural Language Processing, and Retrieval-Augmented Generation applications.

FastAPI was chosen as the backend framework because it provides high performance, asynchronous request handling, automatic API documentation, and seamless integration with machine learning libraries.

Streamlit was selected to rapidly prototype the Bug Submission Module with minimal frontend development effort.

Sentence Transformers, specifically the all-MiniLM-L6-v2 model, provide efficient semantic embeddings suitable for duplicate defect detection and similarity matching.

ChromaDB offers lightweight local vector storage, making it an ideal choice for developing an initial RAG pipeline without requiring cloud infrastructure.

LangChain simplifies document loading, chunking, embedding generation, retrieval, and orchestration of Retrieval-Augmented Generation workflows.

---

### Dataset Selection

Although the Eclipse dataset contains approximately 10,000 bug reports, a representative subset of 5,000 defects was selected for Milestone 1 to satisfy project requirements while maintaining efficient preprocessing, embedding generation, and retrieval performance.

### Conclusion

This research establishes the foundational concepts required for developing the AI Smart Bug Analyzer & Fix Advisor system. The study of defect analysis workflows, Retrieval-Augmented Generation (RAG), semantic similarity techniques, and bug report structures guided the selection of the proposed architecture and technology stack for Milestone 1.

### References

- Mozilla Bug Repository
- Apache JIRA Dataset
- Eclipse Bugzilla Dataset
- Sentence Transformers Documentation
- LangChain Documentation
- ChromaDB Documentation
- FastAPI Documentation
- Streamlit Documentation