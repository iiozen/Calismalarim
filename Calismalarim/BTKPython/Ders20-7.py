import pandas as pd

df = pd.read_csv('imdb.csv')

# # 1. Soru
# result = df.info()
# # 2. Soru
# result = df.head()
# # 3. Soru
# result = df.head(10)
# # 4. Soru
# result = df.tail()
# # 5. Soru
# result = df.tail(10)
# # 6. Soru
# result = df['Movie_Title']
# # 7. Soru
# result = df['Movie_Title'][:5]
# # 8. Soru
# result = df[['Movie_Title','Rating']][:5]
# # 9. Soru
# result = df[['Movie_Title','Rating']][-7:]
# # 10. Soru
# result = df [['Movie_Title','Rating']][5:10]
# # 11. Soru
# result = df[['Movie_Title','Rating']][df['Rating']>=8.0][:50]
# # 12. Soru
# # result = df[['Movie_Title','YR_Released']][2014<=df['YR_Released']][df['YR_Released']<=2015]
# # 13. Soru
# result = df[['Movie_Title','Num_Reviews','Rating']][(df['Num_Reviews']>100000) | ((8.0<df['Rating']) & (df['Rating']<9.0))]
# # result = df[(df['Num_Reviews']>100000) | ((8.0<df['Rating']) & (df['Rating']<9.0))][['Movie_Title','Num_Reviews','Rating']]
# print(result)
