# NLP & Knowledge Extraction Project — Roadmap

This repository contains the roadmap and resources for a project focused on **processing scientific articles, extracting knowledge, and building a minimal RAG/LLM system**.

---

## Project Overview

**Goal:** Develop a system capable of:

- Crawling and classifying scientific articles
- Extracting entities and relationships (knowledge extraction)
- Building a mini-RAG (Retrieval-Augmented Generation) system
- Laying the groundwork for ontology construction
- Experimenting with multi-agent pipelines for automation

---

## Roadmap Phases

### Phase 1 — NLP Basics (1–2 weeks)

**Objective:** Learn and apply basic NLP tools for text preprocessing, vectorization, and classification.

**Key Skills & Tools:**

- Text preprocessing: tokenization, lemmatization, stopwords (spaCy, NLTK, regex) [x] ✅
- Vectorization: TF-IDF, embeddings (Sentence Transformers, HuggingFace) [x] ✅
- Text classification: pretrained models, zero-shot classification [x] ✅

**Expected Outcome:**

- Preprocessed and vectorized abstracts 
- Simple classifier for topic filtering

---

### Phase 2 — Named Entity Recognition & Knowledge Extraction (2 weeks)

**Objective:** Extract entities and structured knowledge from scientific texts.

**Key Skills & Tools:**

- Named Entity Recognition (NER) using SciSpaCy (`en_core_sci_lg`)
- Custom patterns and regex for domain-specific terms
- LLM-assisted extraction of subject–relation–object triplets

**Expected Outcome:**

- JSON files with entities
- CSV files with extracted triplets
- Mini knowledge extraction scripts

---

### Phase 3 — LLM Orchestration and RAG Systems (2–3 weeks)

**Objective:** Integrate LLMs with vector databases to answer questions over documents.

**Key Skills & Tools:**

- LangChain: chains, tools, memory, agents
- LlamaIndex: DocumentStore, VectorStoreIndex, QueryEngine
- RAG pipeline: embeddings + vector DB + retriever + LLM synthesis
- Vector DBs: Qdrant integration

**Expected Outcome:**

- RAG prototype answering queries on scientific abstracts
- Simple Q&A interface

---

### Phase 4 — Multi-Agent Systems and Interface Prototype (2 weeks)

**Objective:** Combine multiple automated agents for tasks like classification, extraction, and ontology building.

**Key Skills & Tools:**

- CrewAI / LangGraph: agents, roles, tools, tasks
- LangFlow: visual pipeline assembly and testing
- Open WebUI: local LLM integration with RAG prototype

**Expected Outcome:**

- Minimal multi-agent pipeline
- Prototype interface for demo purposes

---

## Practical Deliverables

- Working crawler + article classifier
- Entity extraction scripts
- Mini-RAG system with query interface
- Initial understanding of ontology construction
- Multi-agent prototype pipeline

---

## Tools and Technologies

- **Python 3.10+**: main programming language
- **NLP & ML**: spaCy, SciSpaCy, NLTK, SentenceTransformers, HuggingFace
- **Data Handling & Visualization**: pandas, matplotlib
- **LLM & RAG**: LangChain, LlamaIndex, Qdrant
- **Development Environment**: Jupyter / Colab, GitHub

---

This roadmap provides a structured learning and implementation plan, moving from basic NLP preprocessing to building multi-agent RAG systems capable of extracting and reasoning over scientific knowledge.

