# NLP Project Roadmap — First 2 Weeks

This repository contains materials and scripts for the first 2 weeks of the NLP project focused on **processing and classifying scientific articles**, extracting key entities, and preparing a small knowledge extraction pipeline.

---

## Goal for First 2 Weeks

- Learn basic NLP preprocessing steps (tokenization, lemmatization, stopwords).
- Apply vectorization and embeddings for semantic similarity.
- Implement simple text classification.
- Extract named entities (NER) and test simple knowledge extraction (triplets).
- Build a minimal prototype pipeline.

---

## Week 1 — Introduction to NLP & Text Preprocessing

| Day | Topic                       | Tasks                                                                                           | Deliverable                          |
| --- | --------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------- |
| 1 [x] ✅ | Introduction to NLP          | Install libraries (spaCy, NLTK, pandas, regex). Tokenization, lemmatization, stopwords.       | Notebook `Text_Preprocessing.ipynb` |
| 2   | Text Vectorization           | Learn TF-IDF and embeddings. Compare 5 abstracts by cosine similarity.                          | `semantic_similarity_demo.py`       |
| 3   | Zero-shot Classification     | Use Hugging Face pipelines (facebook/bart-large-mnli) for classifying abstracts.               | Classification notebook              |
| 4   | Integration with Crawler     | Process 10–20 abstracts: clean → tokenize → classify.                                           | Minimal classification pipeline      |
| 5   | Visualization & Summary      | Heatmap / similarity graph. Write short report on patterns.                                     | Graph + 0.5 page summary            |

---

## Week 2 — Named Entity Recognition & Knowledge Extraction

| Day | Topic                            | Tasks                                                                                       | Deliverable                        |
| --- | -------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------- |
| 6   | NER (Named Entity Recognition)    | Install SciSpaCy. Extract entities (particles, energy, detectors) from 2–3 articles.       | JSON with extracted entities       |
| 7   | Manual Entity Filtering           | Clean NER results. Apply regex for structured entities (energy ranges, mass values).      | `extract_entities.py` script       |
| 8   | Simple Knowledge Extraction       | Use LLM (API or local Ollama) to extract subject–relation–object triplets.                 | CSV with triplets                  |
| 9   | Mini Pipeline                     | Combine crawler → classification → NER → knowledge extraction into one workflow.           | Prototype v1.0                     |
| 10  | Reflection & Visualization        | Visualize entities (graph or word cloud). Write short summary of progress & challenges.    | Mini-report + demo                 |

---

## Work Format

- **Time per day:** 2–3 hours (1 h theory + 1–2 h practice)
- **Workspace:** Jupyter / Colab + GitHub repository
- **Tools:** Python 3.10+, spaCy, SciSpaCy, HuggingFace, SentenceTransformers, pandas, matplotlib
- **Weekly reflection:** Every Friday write a 5-minute summary of progress and issues

---

## Expected Outcomes by End of Week 2

- Tokenized, lemmatized, and preprocessed abstracts. [x] ✅
- Vector representations for semantic similarity comparisons.
- Basic zero-shot classification of abstracts.
- Named entity extraction pipeline for scientific terms.
- Mini knowledge extraction pipeline producing triplets.

