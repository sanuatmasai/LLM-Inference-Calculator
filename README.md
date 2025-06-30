# 🧮 LLM Inference Calculator

A simple, beginner-friendly calculator to estimate latency, memory usage, and cost for running Large Language Models (LLMs) in different deployment scenarios.

---

## 📦 Features

* Supports models: 7B, 13B, GPT-4
* Select hardware: A100, T4, RTX 4090, CPU
* Deployment modes: local / cloud
* Calculates:

  * Inference latency
  * Memory usage (GB)
  * Cost per request (\$)
  * Hardware compatibility

---

## 🚀 How to Use

### 🖥️ Requirements

* Python 3.8+

### 📥 Setup

```bash
$ git clone <your_repo_url>
$ cd llm-inference-calculator
$ python inference_calculator.py
```

### 🧪 Example

```bash
Enter model size (7B / 13B / GPT-4): 13B
Enter number of tokens (e.g. 500): 1000
Enter batch size (e.g. 8): 4
Enter hardware type (A100 / T4 / RTX 4090 / CPU): A100
Deployment mode (local / cloud): cloud
```

#### Output

```
--- Inference Estimation ---
Latency (s): 1.0
Memory Usage (GB): 28.8
Cost per Request ($): 0.0061
Hardware Compatible: True
```

---

## 📁 Project Structure

```
├── inference_calculator.py    # Main calculator script
├── research_notes.md          # LLM + hardware research
├── scenario_analysis.md       # Use case testing and results
└── README.md                  # This file
```

---

## 💡 Why Use This?

Without this calculator, you risk:

* Choosing incompatible hardware
* Deploying slow or expensive models
* Overpaying for underutilized cloud resources

---

## 🤝 Contributing

Pull requests welcome! Suggest benchmarks, add hardware configs, or improve formulas.

---

## 📚 Resources

* HuggingFace Open LLM Leaderboard
* OpenAI Pricing Page
* NVIDIA GPU Documentation
