# Nan-Shan-Chatbot

以Langchain, Faiss, Ollama 建立基於向量搜索的商品推薦聊天機器人


https://www.anaconda.com/download/

```conda env create -f environment.yml```

download taide-8b-a.3-q4_k_m.gguf

https://huggingface.co/nctu6/Llama3-TAIDE-LX-8B-Chat-Alpha1-GGUF

running ollama server

https://github.com/ollama/ollama?tab=readme-ov-file


Modelfile跟TAIDE量化模型taide-8b-a.3-q4_k_m.gguf放在同一個路徑底下

```ollama create taide-llama3 -f Modelfile```

## Start

放置檔案路徑
```
raw = pd.read_csv('../post_PCA.csv')
repur_list = pd.read_csv('../repur_list.csv')
Reference = pd.read_excel("../南山資料/台大財金 金融科技 變數欄位_NTU 20240326.xlsx")
```

```python recommendation.py```