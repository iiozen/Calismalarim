import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Konular için countvector'de kelime kısıtlaması yokken diğerine koydum.
# cv = CountVectorizer()

cv = CountVectorizer()
cv2 = CountVectorizer(max_features=300)


veri = pd.read_csv('egitimehazir.csv')

X = veri['icerik'].values.astype('U')
y1 = veri['başlık'].values.astype('U')
# vectorlenecek = veri.iloc[:,:2].values.astype('U')

# cv.fit(vectorlenecek.ravel())
cv.fit(X)
cv2.fit(y1)




# joblib.dump(cv2,'vectorizerBaslik300.joblib')
joblib.dump(cv,'vectorizerIcerik.joblib')

# X bizim eğitimde bağımsız değişkenimiz
X = cv.transform(X).toarray()
print(X.shape)

# y1 y bağımlı değişkenimizin bir parçası
y1 = cv2.transform(y1).toarray()
print(y1.shape)

# y yi oluşturacak diğer yapılar ise
# genel_konu üst_konu ve alt_konulardır.
# Labelencoding ile bunlarıda eğitime hazır hale getiriyorum.

legenel_konu = LabelEncoder()
leust_konu = LabelEncoder()
lealt_konu = LabelEncoder()
y2 = veri.iloc[:,2:].values
# le.fit(y2.ravel())


genel_konu = veri['genel_konu'].values
ust_konu = veri['ust_konu'].values
alt_konu = veri['alt_konu'].values



legenel_konu.fit(genel_konu)

joblib.dump(legenel_konu,'labelEncodergenel_konu.joblib')

leust_konu.fit(ust_konu)

joblib.dump(leust_konu,'labelEncoderust_konu.joblib')

lealt_konu.fit(alt_konu)

joblib.dump(lealt_konu,'labelEncoderalt_konu.joblib')

# y = np.column_stack([ygenel_konu,yust_konu,yalt_konu])


ygenel_konu = legenel_konu.transform(genel_konu)
yust_konu = leust_konu.transform(ust_konu)
yalt_konu = lealt_konu.transform(alt_konu)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,ygenel_konu,test_size=0.1,random_state=42)
gnb = GaussianNB()
# clf = MultiOutputClassifier(gnb)
gnb.fit(X_train,y_train)
joblib.dump(gnb,'modelgenel_konu.joblib')

acc2 = gnb.score(X_test,y_test)
print('scoregenel_konu : ',acc2)

X_train, X_test, y_train, y_test = train_test_split(X,yust_konu,test_size=0.1,random_state=42)
gnb = GaussianNB()
# clf = MultiOutputClassifier(gnb)
gnb.fit(X_train,y_train)
joblib.dump(gnb,'modelust_konu.joblib')

acc2 = gnb.score(X_test,y_test)
print('scoreust_konu : ',acc2)

X_train, X_test, y_train, y_test = train_test_split(X,yalt_konu,test_size=0.1,random_state=42)
gnb = GaussianNB()
# clf = MultiOutputClassifier(gnb)
gnb.fit(X_train,y_train)
joblib.dump(gnb,'modelalt_konu.joblib')

acc2 = gnb.score(X_test,y_test)
print('scorealt_konu : ',acc2)

X1_train, X1_test, y1_train, y1_test = train_test_split(X,y1,test_size=0.1,random_state=42)



# Bir girişten birden çok farklı veri elde etmek istediğim için
# MultiOutputClassifier'ı kullanarak Gaussian Naive Bayes kullanacağım.

print('train başlıyor')
# gnb = GaussianNB()
# clf = MultiOutputClassifier(gnb)
# clf2 = MultiOutputClassifier(gnb)
# clf.fit(X_train,y_train)
# clf2.fit(X1_train,y1_train)


# joblib.dump(clf2,'baslikModel300.joblib')

print('train bitti')
# acc2 = clf.score(X_test,y_test)

# acc = clf2.score(X1_test,y1_test)

# print('scoregenel_konu : ',acc2)

# print('scoregnb:' , acc)