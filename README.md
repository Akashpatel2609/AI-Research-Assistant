# 🤖 AI Research Chatbot

A lightweight, retrieval-augmented chatbot that answers Computer Science research queries in real time. It uses multi-model embeddings, FAISS indexing, and Transformer-based reranking to deliver precise, low-latency responses via a simple CLI.

---

## ✨ Features

- **🧹 Corpus Preprocessing**  
  - Cleans & tokenizes 94.5K research papers into 752K lemmatized chunks (HTML/PDF scrubbing + NLTK).  

- **🔗 Multi-Model Embeddings**  
  - Encodes passages with SentenceTransformers (MultiQA, SciBERT, All-MiniLM, MPNet).  
  - Batch processing for fast FAISS indexing.  

- **⚡ FAISS Retrieval & Reranking**  
  - Bi-encoder top-k search + CrossEncoder (ms-marco-MiniLM-L6-v2) reranking.  
  - +9.3 % precision boost, sub-100 ms retrieval.  

- **📝 Transformer-Powered Answers**  
  - Flan-T5-Large synthesizes context-aware replies.  
  - ~1.2 s end-to-end latency.  

- **💬 CLI Chatbot Interface**  
  - Ask questions directly in the terminal.  
  - Seamless retrieval → rerank → generate workflow.

---

## 🛠️ Tech Stack

- **Python 3.9+**  
- **NLTK** (tokenization, lemmatization)  
- **SentenceTransformers** (multiqa-MiniLM, scibert, all-MiniLM, all-mpnet)  
- **FAISS** (approximate nearest neighbors)  
- **Hugging Face Transformers** (Flan-T5-Large, Cross-Encoder ms-marco-MiniLM-L6-v2)  
- **Argparse** (CLI parsing)

---

## 🚀 Installation

1. **Clone**  
   ```bash
   git clone https://github.com/<your-username>/ai-research-chatbot.git
   cd ai-research-chatbot


2. **Setup venv**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install deps**

   ```bash
   pip install -r requirements.txt
   ```

4. **Data & Indexes**

   * Place FAISS index files (`*.index`) and embeddings under `data/` or regenerate using scripts below.

---



## 💬 Usage

1. **Run Chatbot CLI**

   ```bash
   python cli_chatbot.py \
     --model multiqa \
     --reranker crossencoder-msmarco-mini-l6-v2 \
     --generator flan-t5-large
   ```
2. **Example Session**

   ```bash
   $ python cli_chatbot.py --model mpnet
   [Chatbot] Welcome! Ask a CS research question.
   > What is knowledge distillation?

   [Retrieval] 5 candidates (0.04 s)  
   [Reranking] Top passage (0.02 s)  
   [Answer] Distillation is a model compression technique where a smaller “student” network learns from a larger “teacher” network by minimizing cross-entropy and KL-divergence. (1.1 s)
   ```


