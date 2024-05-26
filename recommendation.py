# %load_ext cudf.pandas
import pandas as pd
import joblib
import faiss
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

target_customer = 64
raw = pd.read_csv('../post_PCA.csv')
repur_list = pd.read_csv('../repur_list.csv')
Reference = pd.read_excel("../南山資料/台大財金 金融科技 變數欄位_NTU 20240326.xlsx")
index = faiss.read_index('Models/faiss_vb_repur.index')
reference_dict = dict(zip(Reference.iloc[1:, 3], Reference.iloc[1:, 4]))
new_customer_vector = raw.iloc[target_customer, :-2].values.astype('float32').reshape(1, -1)
distances, indices = index.search(new_customer_vector, 5)

model = 'XGBoost_0.92' 
# 'Logistic_Regression_0.97', 'Decision_Tree_0.86', 'XGBoost_0.92', 'SVM_0.97', "SVD+Logistic_Regression_0.98"
# scaler = joblib.load('Models/scaler.joblib')

# logi = joblib.load(f'Models/{model}.joblib')
# new_customer_vector_scaled = scaler.transform(new_customer_vector)
# pred_probabilities = logi.predict_proba(new_customer_vector_scaled)
# print(pred_probabilities)

llm = ChatOllama(model="taide-llama3")
# llm = ChatOllama(model="taide-llama3", device="cuda")
# llm = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="""
                  |:------------------|----:|
                  | AH-住院商品保單數 |   3 |
                  | AH-重疾商品保單數 |   4 |
                  | AH-意外商品保單數 |   0 |
                  | AH-長照商品保單數 |   0 |
                  根據客戶的相似客群分析，傾向購買AH-住院商品以及AH-重疾商品類型的保單。"""),
    SystemMessage(content="""|:----------------------|:--------|
                | 客戶年齡(歲)          | 61.0    |
                | 性別                  | 0       |
                | 城市                  | 臺中市  |
                | 年收入(元)            | 2012284 |
                | 財富等級              | R1C     |
                | AH-住院商品保單數     | 3       |
                | AH-重疾商品保單數     | 2       |
                | AH-意外商品保單數     | 0       |
                | AH-長照商品保單數     | 1       |
                根據客戶詳細資料分析，AH-住院商品保單數，與客群結果相當，AH-重疾商品保單數相較於相似客群較為稀少。"""),
    # HumanMessage(content="欄位對照參考資料:"),
    # HumanMessage(content="{reference}"),
    HumanMessage(content="客戶詳細資訊:"),
    HumanMessage(content="{target_info}"),
    HumanMessage(content="關於這個客戶利用FAISS檢索其他相似客戶的結果如下:"),
    HumanMessage(content="{result_summalize}"),
    # HumanMessage(content="{result}"),
    HumanMessage(content="基於FAISS相似度檢索，與此客戶類似的客群購買了這些種類的產品:"),
    HumanMessage(content="{result_summalize}"),
    HumanMessage(
        content="按照FAISS檢索資料以及客戶軌跡資料，適合推薦他什麼產品？"
    ),
]
prompt = ChatPromptTemplate.from_messages(messages)

POL_CNT = ["AHa_POL_CNT",'AHb_POL_CNT','AHc_POL_CNT','AHd_POL_CNT']
features = [
    "AGE", "GENDER", "City", "CLIENT_INCOME", "WEALTH_LEVEL_REV", 
    "loytal_level", "cust_group", "CUSTOMER_LEVEL", 
    "SIN", "REG", "ILP", "AH", 
    "tot_pol_cnt", "tot_txn_cnt", "ACT_NUM", "ACT_DAYS"
]
repur_list = repur_list.loc[:, features+POL_CNT]
info = repur_list.iloc[target_customer].to_frame().T
dumps = repur_list.loc[indices[0]].reset_index(drop=True)
dumps_sum = dumps[POL_CNT].sum()
chain = prompt | llm | StrOutputParser()
info.columns = info.columns.map(reference_dict)
dumps.columns = dumps.columns.map(reference_dict)
dumps_sum.index = dumps_sum.index.map(reference_dict)
print(chain.invoke({"target_info": info.to_markdown(),
                    "result_summalize":dumps_sum.to_markdown(),
                    # "result": dumps.to_markdown(),
                    "reference": Reference}))
# print(chain.)