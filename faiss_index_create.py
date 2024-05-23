import pandas as pd
import faiss
import joblib

raw = pd.read_csv('../post_PCA.csv')
scaler = joblib.load('../Models/scaler.joblib')
X = raw.iloc[:, :-2].values.astype('float32')
# X = scaler.transform(raw.iloc[:, :-2].values)
# X = scaler.transform(raw.drop(['Y1_repurchase', 'REPUR_FLG'], axis=1))

d = X.shape[1]# 設定向量的維度
index = faiss.IndexFlatL2(d)
index.add(X)# 將資料加入索引
faiss.write_index(index, '../Models/faiss_vb_origin.index') # 保存索引