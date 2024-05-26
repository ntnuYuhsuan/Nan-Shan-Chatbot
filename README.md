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
[link](https://drive.google.com/drive/folders/1O0hD32MNuYnyON4CVo6fdVhNjv-Wb_4G?usp=drive_link)
```
raw = pd.read_csv('../post_PCA.csv')
repur_list = pd.read_csv('../repur_list.csv')
Reference = pd.read_excel("../南山資料/台大財金 金融科技 變數欄位_NTU 20240326.xlsx")
```

```python recommendation.py```


## Output

### gpt-4o

根據提供的資料，包含客戶的詳細資訊、FAISS檢索結果以及客戶軌跡資料，可以推薦如下產品：

1. **AH-重疾商品**：
   - 客戶目前擁有2張AH-重疾商品保單，相較於相似客群的4張，數量偏少。可以考慮增加這類保單來提升保障。

2. **AH-住院商品**：
   - 相似客群傾向購買AH-住院商品保單數為3張，而客戶目前已經擁有3張，與相似客群持平，因此可以繼續推薦此類產品以維持保障。

3. **AH-長照商品**：
   - 客戶目前擁有1張長照商品保單，雖然相似客群中並沒有購買此類產品，但這類產品對於年齡較大的客戶（如61歲）仍然是重要的保障，建議持續推薦。

4. **AH-意外商品**：
   - 相似客群中並未購買AH-意外商品，客戶也沒有此類保單。可以根據客戶具體需求和風險評估，決定是否推薦此類產品。

綜合分析，最適合推薦的產品包括：
- **增加AH-重疾商品保單數**，以提升保障水平。
- **持續推薦AH-住院商品保單**，維持現有保障。
- **保留並可能增加AH-長照商品保單**，以應對未來長期護理需求。

這樣的推薦策略能夠滿足客戶現有情況並提升其未來保障。

### TAIDE-Llama3

根據FAISS檢索資料與客戶足跡，我們為該客戶推薦以下產品:

* AH-住院商品保單數：基於他所購買的產品類別，這是個明顯的推薦項目。
* AH-重疾商品保單數：我們發現他有較高的可能性對這類型產品感興趣，儘管目前購買量不多，我們仍建議持續關注。
* AH-意外商品保單數：根據足跡資料，他購買這類型產品的機率相對較低，但依然是他未來考慮的潛在選項。
* AH-長照商品保單數：他目前擁有1張這類型保單，考量他的年齡與性別，我們預期他未來幾年內可能會增加保障項目。

這些推薦是根據客戶目前所持有的產品，以及其在該領域內的足跡資料。我們建議在做出購買決策前，客戶應諮詢專業顧問，以獲得量身訂製的建議。
