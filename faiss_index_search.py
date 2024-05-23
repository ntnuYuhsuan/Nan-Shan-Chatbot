import faiss
import numpy as np
import pandas as pd
raw = pd.read_csv('../post_PCA.csv')

new_customer_vector = raw.iloc[0, :-2].values.astype('float32').reshape(1, -1)
index = faiss.read_index('../Models/faiss_vb.index')# 讀取索引

# 搜索最相似的10個客戶
k = 10
distances, indices = index.search(new_customer_vector, k)

similar_customers = raw.iloc[indices[0]].reset_index(drop=True)
print("相似客戶的資料：")
print(similar_customers)

# 輸出結果
# print("相似客戶的索引：", indices)
# print("相似客戶的距離：", distances)