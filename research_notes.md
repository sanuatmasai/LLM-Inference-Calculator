# 📚 Research Notes: LLM Inference Calculator

## 🧠 What is LLM Inference?

LLM inference is the process of running a trained large language model to generate responses or predictions based on a given input. It is the stage where the model “infers” or “predicts” from your data without learning anything new.

For example, when you type a message into ChatGPT and get a reply — that’s inference happening behind the scenes.

---

## 📏 Key Metrics Explained

* **Latency**: Time taken to generate a response (in seconds). Lower latency is better.
* **Memory Usage**: Total GPU memory required to load and run the model.
* **Cost per Request**: Estimated cost in USD for running one query, considering compute and token usage.
* **Hardware Compatibility**: Whether the selected model can fit within the available GPU memory.

---

## 📊 Model Comparison (7B vs 13B vs GPT-4)

| Model | Params | Memory (GB) | Avg Latency (1K tokens) | Cost/Million Tokens |
| ----- | ------ | ----------- | ----------------------- | ------------------- |
| 7B    | 7B     | \~16 GB     | \~1s                    | \$0.002             |
| 13B   | 13B    | \~28 GB     | \~2s                    | \$0.004             |
| GPT-4 | \~180B | \~45 GB+    | \~3.5s                  | \$0.06              |

* GPT-4 is more accurate but expensive and slower.
* 7B/13B are open-source (e.g., LLaMA, Mistral) and cheaper to host.

---

## ⚙️ Hardware Reference Table

| Hardware   | Memory (GB) | Cost/Hour (Cloud) | Suitable Models          |
| ---------- | ----------- | ----------------- | ------------------------ |
| A100       | 40          | \$2.5             | All models (up to GPT-4) |
| T4         | 16          | \$0.35            | 7B only                  |
| RTX 4090   | 24          | \$0.0 (local)     | 7B, some 13B (quantized) |
| CPU (8 GB) | 8           | \$0.0 (local)     | Only small/quantized     |

---

## 🧮 Inference Cost Breakdown

1. **Model Token Cost**:

   * 500 tokens with GPT-4 = 0.00003 × 500 = \$0.03
2. **Cloud Infra Cost**:

   * If 1 request takes 3.5s on A100 = (3.5/3600) × \$2.5 = \~\$0.0024
3. **Total Cost**:

   * \$0.03 + \$0.0024 = \~\$0.0324/request

---

## 📚 References

* HuggingFace LLM Benchmarks
* Open LLM Leaderboard ([https://huggingface.co/spaces/HuggingFaceH4/open\_llm\_leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard))
* NVIDIA official GPU specs
* OpenAI pricing page
