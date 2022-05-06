import pandas as pd
df = pd.read_csv('nba.csv')
# # 1. Soru
# result = df.head(10)
# # 2. Soru
# result = df.index
# # 3. Soru
# result = df['Salary'].mean()
# # 4. Soru
# result = df['Salary'].max()
# # 5. Soru
# result = df[df['Salary']==df['Salary'].max()]
# # 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
# result = df[(df['Age']>=20) & (df['Age']<25)].sort_values('Age',ascending=False)
# # 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
# result = df['Team'][df['Name']=='John Holland']
# # 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
# result = df.groupby('Team').mean()['Salary']
# # 9- Kaç farklı takım mevcut ?
# result = len(df.groupby('Team'))
# result = df['Team'].unique()
# # 10- Her takımda kaç oyuncu oynamaktadır ?
# result = df.groupby('Team')['Name'].count()
# result = df['Team'].value_counts()
# 11- İsmi içinde "and" geçen kayıtları bulunuz.
# df.dropna(inplace=True)
# result = df[df['Name'].str.contains('and')]

# def str_find(name):
#     if "and" in name.lower():
#         return True
#     return False

# result = df[df["Name"].apply(str_find)]




# print(result)