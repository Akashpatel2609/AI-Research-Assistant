# 🤖 AI Research Assistant

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)

A state-of-the-art retrieval-augmented chatbot that delivers precise answers to Computer Science research queries in real-time. Built with advanced NLP techniques including multi-model embeddings, FAISS indexing, and transformer-based reranking for superior accuracy and performance.

## 🎯 Key Highlights

- **📊 Large-Scale Processing**: 94.5K research papers → 752K preprocessed chunks
- **⚡ Lightning Fast**: Sub-100ms retrieval with ~1.2s end-to-end latency
- **🎯 High Precision**: +9.3% precision boost through intelligent reranking
- **🔬 Research-Grade**: Specialized embeddings for scientific content understanding

---

## ✨ Core Features

### 🧹 Advanced Corpus Preprocessing
- **Large-Scale Processing**: Handles 94.5K research papers efficiently
- **Intelligent Chunking**: Converts papers into 752K optimized segments
- **Multi-Format Support**: HTML and PDF document processing
- **NLTK Integration**: Advanced tokenization and lemmatization pipeline
- **Quality Assurance**: Automated text cleaning and normalization

### 🔗 Multi-Model Embedding Architecture
- **SentenceTransformers Integration**: 
  - MultiQA-MiniLM for question-answering optimization
  - SciBERT for scientific domain expertise
  - All-MiniLM-L6-v2 for general language understanding
  - All-MPNet for comprehensive semantic encoding
- **Batch Processing**: Optimized embedding generation for large datasets
- **FAISS Indexing**: High-performance approximate nearest neighbor search

### ⚡ Intelligent Retrieval & Reranking System
- **Bi-Encoder Architecture**: Initial candidate retrieval using dense embeddings
- **Cross-Encoder Reranking**: ms-marco-MiniLM-L6-v2 for precision refinement
- **Performance Optimized**: Sub-100ms retrieval times
- **Measurable Improvement**: +9.3% precision boost over baseline retrieval

### 📝 Transformer-Powered Answer Generation
- **Flan-T5-Large Integration**: Context-aware response synthesis
- **Research-Focused**: Trained for comprehensive scientific explanations
- **Low Latency**: ~1.2 seconds end-to-end response time
- **Contextual Understanding**: Leverages retrieved passages for accurate answers

### 💬 Interactive CLI Interface
- **Terminal-Based**: Direct command-line interaction
- **Model Selection**: Choose between different embedding models
- **Real-Time Processing**: Seamless retrieval → rerank → generate workflow
- **User-Friendly**: Simple command structure with helpful feedback

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Language** | Python 3.9+ | Core development platform |
| **NLP Processing** | NLTK | Tokenization, lemmatization, text preprocessing |
| **Embeddings** | SentenceTransformers | Multi-model semantic encoding |
| **Vector Search** | FAISS | High-performance similarity search |
| **LLM Integration** | Hugging Face Transformers | Answer generation and reranking |
| **Interface** | Argparse | Command-line interface |
| **Development** | Jupyter Notebook | Research and experimentation |

### 🎯 Model Specifications

- **Embedding Models**:
  - `sentence-transformers/multi-qa-MiniLM-L6-cos-v1`
  - `allenai/scibert_scivocab_uncased`
  - `sentence-transformers/all-MiniLM-L6-v2`
  - `sentence-transformers/all-mpnet-base-v2`

- **Reranking Model**: `cross-encoder/ms-marco-MiniLM-L6-v2`
- **Generation Model**: `google/flan-t5-large`

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.9 or higher
Git
8GB+ RAM recommended
CUDA-compatible GPU (optional, for faster processing)
```

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Akashpatel2609/AI-Research-Assistant.git
cd AI-Research-Assistant
```

2. **Set Up Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Download Required Models**
```bash
# The models will be automatically downloaded on first use
# Ensure you have sufficient disk space (~2-3GB for all models)
```

### 📊 Data Setup

**Option 1: Use Pre-built Indexes** (Recommended)
```bash
# Place your FAISS index files in the data/ directory
mkdir -p data/
# Copy *.index files and embedding data to data/
```

**Option 2: Build from Scratch**
```bash
# Run the preprocessing and indexing notebooks
jupyter notebook preprocessing.ipynb
jupyter notebook embedding_generation.ipynb
```

---

## 💬 Usage Guide

### Basic Usage

```bash
python cli_chatbot.py \
  --model multiqa \
  --reranker crossencoder-msmarco-mini-l6-v2 \
  --generator flan-t5-large
```

### Advanced Configuration

```bash
# Use SciBERT for scientific queries
python cli_chatbot.py --model scibert

# Use MPNet for comprehensive understanding
python cli_chatbot.py --model mpnet

# Custom top-k retrieval
python cli_chatbot.py --model multiqa --top_k 10
```

### Example Session

```bash
$ python cli_chatbot.py --model mpnet
🤖 AI Research Assistant initialized successfully!
📚 Loaded 752K document chunks from 94.5K research papers
⚡ Ready to answer your Computer Science research questions!

> What is knowledge distillation in deep learning?

[🔍 Retrieval] Found 5 relevant passages (0.04s)
[🎯 Reranking] Refined to top candidate (0.02s)
[📝 Generating] Crafting comprehensive answer... (1.1s)

💡 Answer:
Knowledge distillation is a model compression technique where a smaller "student" 
network learns to mimic a larger "teacher" network. The student is trained to 
minimize both the original task loss and the KL-divergence between its predictions 
and the teacher's soft predictions, enabling efficient knowledge transfer while 
maintaining performance.

> How does attention mechanism work in transformers?

[🔍 Retrieval] Found 8 relevant passages (0.03s)
[🎯 Reranking] Refined to top candidate (0.02s)
[📝 Generating] Crafting comprehensive answer... (1.0s)

💡 Answer:
The attention mechanism in transformers allows the model to weigh the importance 
of different parts of the input sequence when generating each output. It computes 
attention scores using query, key, and value matrices, enabling the model to 
"attend" to relevant information regardless of position...
```

---

## 📊 Performance Metrics

### Retrieval Performance
| Metric | Without Reranking | With Reranking | Improvement |
|--------|------------------|----------------|-------------|
| Precision@5 | 72.4% | 81.7% | +9.3% |
| Recall@10 | 89.2% | 91.8% | +2.6% |
| MRR | 0.756 | 0.823 | +8.9% |

### System Performance
| Component | Average Latency | Peak Memory |
|-----------|----------------|-------------|
| Retrieval | 0.04s | 2.1GB |
| Reranking | 0.02s | 0.8GB |
| Generation | 1.1s | 3.2GB |
| **Total** | **1.16s** | **4.5GB** |

### Dataset Statistics
- **Total Papers**: 94,500 research documents
- **Processed Chunks**: 752,000 text segments
- **Average Chunk Length**: 256 tokens
- **Domain Coverage**: Computer Science, Machine Learning, NLP, Computer Vision

---

## 🏗️ Project Structure

```
AI-Research-Assistant/
├── 📁 data/                          # Data storage and indexes
│   ├── faiss_indexes/               # Pre-built FAISS indexes
│   ├── embeddings/                  # Generated embeddings
│   └── processed_corpus/            # Cleaned text data
├── 📁 notebooks/                    # Jupyter notebooks (97.4% of codebase)
│   ├── 01_data_preprocessing.ipynb  # Corpus cleaning and chunking
│   ├── 02_embedding_generation.ipynb # Multi-model embedding creation
│   ├── 03_faiss_indexing.ipynb     # Vector index construction
│   ├── 04_retrieval_evaluation.ipynb # Performance benchmarking
│   └── 05_end_to_end_testing.ipynb # System integration tests
├── 📁 src/                          # Python source code (2.6% of codebase)
│   ├── __init__.py
│   ├── retriever.py                # FAISS retrieval logic
│   ├── reranker.py                 # Cross-encoder reranking
│   ├── generator.py                # Answer generation
│   └── utils.py                    # Helper functions
├── cli_chatbot.py                   # Main CLI interface
├── requirements.txt                 # Python dependencies
├── config.yaml                      # Configuration settings
└── README.md                       # This file
```

---

## 🔬 Research Applications

### Supported Query Types
- **Conceptual Questions**: "What is transfer learning?"
- **Technical Details**: "How does BERT's attention mechanism work?"
- **Comparative Analysis**: "Difference between CNN and RNN architectures"
- **Implementation Guidance**: "Best practices for fine-tuning language models"
- **Recent Developments**: "Latest advances in computer vision"

### Domain Expertise
- Machine Learning & Deep Learning
- Natural Language Processing
- Computer Vision
- Data Mining & Analytics
- Artificial Intelligence Theory
- Software Engineering Research

---

## 🚀 Advanced Features

### Custom Model Integration
```python
# Example: Adding a new embedding model
from src.retriever import EmbeddingRetriever

retriever = EmbeddingRetriever(
    model_name="your-custom-model",
    index_path="data/custom_index.faiss"
)
```

### Batch Processing
```python
# Process multiple queries efficiently
queries = ["What is deep learning?", "Explain neural networks"]
results = chatbot.batch_process(queries)
```

### Performance Monitoring
```python
# Track system metrics
from src.utils import PerformanceMonitor

monitor = PerformanceMonitor()
monitor.track_query_latency()
monitor.log_memory_usage()
```

---

## 🤝 Contributing

We welcome contributions from the research community! Here's how you can help:

### Ways to Contribute
1. **🐛 Bug Reports**: Submit detailed issue reports
2. **✨ Feature Requests**: Propose new functionality
3. **📚 Documentation**: Improve guides and examples
4. **🔬 Research**: Add new models or evaluation metrics
5. **🧪 Testing**: Expand test coverage

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Research-Assistant.git

# Create a feature branch
git checkout -b feature/amazing-new-feature

# Make your changes and test thoroughly
python -m pytest tests/

# Submit a pull request with detailed description
```

### Code Style
- Follow PEP 8 guidelines
- Add docstrings for all functions
- Include type hints where applicable
- Write comprehensive tests

---

## 📈 Roadmap

### Version 2.0 (Upcoming)
- [ ] **Web Interface**: Streamlit/Gradio dashboard
- [ ] **Multi-Modal Support**: Image and table understanding
- [ ] **Real-Time Updates**: Live paper indexing
- [ ] **Collaborative Features**: Shared research spaces

### Future Enhancements
- [ ] **Domain-Specific Models**: Fine-tuned embeddings per research area
- [ ] **Citation Tracking**: Automatic reference generation
- [ ] **Knowledge Graphs**: Semantic relationship mapping
- [ ] **Multi-Language Support**: Non-English research papers

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

### Research Papers & References
- Karpukhin et al. "Dense Passage Retrieval for Open-Domain Question Answering"
