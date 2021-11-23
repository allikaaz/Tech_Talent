import pandas as pd
rw_col = pd.read_csv("AlliK.csv")
print(rw_col.shape)
#print(rw_col[3:8])
#print(rw_col.iloc[2:8])
#print(rw_col.loc[2:7])
data_1 = rw_col["All-inclusive"].mean()
print(data_1)
data_mn = rw_col.mean()
print(data_mn)
score_min = rw_col["Score"].min()
print(score_min)
score_max = rw_col["Score"].max()
print(score_max)
data_more = rw_col['Score'] > 8
print(data_more)
data_more2 = rw_col['All-inclusive'] > 9
print(data_more2)
