import faiss
import numpy as np
import pandas as pd
raw = pd.read_csv('../post_PCA.csv')
raw = raw[raw['REPUR_FLG'] == True]

new_customer_vector = raw.iloc[0, :-2].values.astype('float32').reshape(1, -1)
index = faiss.read_index('../Models/faiss_vb_repur.index')# 讀取索引

# 搜索最相似的10個客戶
k = 5
distances, indices = index.search(new_customer_vector, k)

repur_list = pd.read_csv('../repur_list.csv', index_col=0)
similar_customers = repur_list.iloc[indices[0]].reset_index(drop=True)

print("相似客戶的資料：")
print(type(similar_customers.to_markdown()))

# 輸出結果
# print("相似客戶的索引：", indices)
# print("相似客戶的距離：", distances)