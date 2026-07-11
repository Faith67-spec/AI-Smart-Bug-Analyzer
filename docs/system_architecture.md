# System Architecture

## Overview

The AI Smart Bug Analyzer & Fix Advisor is designed as a modular system composed of six major modules.

## Modules

### 1. Bug Submission Module
Accepts bug reports through text input or file upload.

Supported inputs:
- Bug reports
- Error logs
- Stack traces
- TXT files
- LOG files

### 2. Historical Defect Knowledge Base
Stores historical defects collected from:

- Eclipse dataset

Stores:
- Bug reports
- Metadata
- Embeddings

### 3. RAG Pipeline

Functions:
- Chunking
- Embedding generation
- Vector indexing
- Similarity retrieval

### 4. Multi-Agent System

Agents:

- Triage Agent
- Log Analysis Agent
- Duplicate Agent
- Root Cause Agent
- Remediation Agent

### 5. Findings Generator

Produces:

- Similar defects
- Root cause
- Fix suggestions

### 6. Analytics Module

Identifies:

- recurring issues
- trends
- systemic failures

## Architecture Diagram

![System Architecture](diagrams/system_architecture.png)
