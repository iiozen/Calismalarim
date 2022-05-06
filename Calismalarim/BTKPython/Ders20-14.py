import pandas as pd
df = pd.read_csv('youtube-ing.csv')
# 1- İlk 10 kaydı getiriniz.
# result = df.head(10)
# 2- İkinci 5 kaydı getiriniz.
# result = df[10:15]
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
# result = df.columns
# result2 = len(result)
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# result = df.drop(['thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description'],axis = 1)
# # 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
# result = df['likes'].mean()
# result2 = df['dislikes'].mean()
# # 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
# result = df.head(50)[['dislikes','likes']]
# # 7- En çok görüntülenen video hangisidir ?
# result = df[['title','views']][df['views'].max()==df['views']]
# # 8- En düşük görüntülenen video hangisidir?
# result = df[['title','views']][df['views'].min()==df['views']]
# # 9- En fazla görüntülenen ilk 10 video hangisidir ?
# result = df.sort_values('views',ascending=False).head(10)[['title','views']]
# # 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# result = df.groupby('category_id').mean().sort_values('likes')['likes']
# # 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# result = df.groupby('category_id').sum().sort_values('comment_count',ascending=False)['comment_count']
# # 12- Her kategoride kaç video vardır ?
# result = df.groupby('category_id').count().sort_values('title',ascending=False)['title']
# result = df['category_id'].value_counts()
# # 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
# def uzunluk_al(urun):
#     return len(urun)
# df['title_uzunluğu'] = df['title'].apply(len)
# df['title_uzunluğu'] = df['title'].apply(uzunluk_al)
# result = df[['title','title_uzunluğu']].head(10)
# # 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# # result = df.groupby('title').count().sort_values('tags',ascending=False)['tags'].head(10)

# def tagCount(tag):
#     return len(tag.split('|'))

# df["tag_count"] = df["tags"].apply(tagCount)
# result = df.sort_values('tag_count',ascending=False)[['title','tag_count']]
# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)
def populer(urun):
    urun = pd.concat(urun,axis=1)
    a=0
    if a==0:
        print(urun)
    a+=1
    # return like/dislike

df['popüler'] = df[['likes','dislikes']].apply(populer)
# # result = df.sort_values('popüler')[['title','likes','dislikes','popüler']].head(30)
# result = df['popüler'].head(10)




# print(result)