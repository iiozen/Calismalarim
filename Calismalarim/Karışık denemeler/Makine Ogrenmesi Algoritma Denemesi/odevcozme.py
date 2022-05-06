
from sklearn.metrics import r2_score as r2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

veri = pd.read_csv("maaslar_yeni.csv")

veri_ohelenecek = veri['unvan']
veri_ohelenecek = pd.DataFrame(veri_ohelenecek,columns=['unvan'])
veri = veri.drop(['Calisan ID','unvan'],axis=1)


from sklearn.preprocessing import OneHotEncoder as ohe

enc = ohe()
veri_ohelenen = pd.DataFrame(enc.fit_transform(veri_ohelenecek[['unvan']]).toarray())
veri_ohelenen.columns = [i for j in enc.categories_ for i in j]

islenen_veri = pd.concat([veri_ohelenen,veri],axis=1)


y = islenen_veri['maas']
x = islenen_veri.drop('maas',axis=1)
X = x.values
Y = y.values

from sklearn.linear_model import LinearRegression

MLR_reg = LinearRegression()
MLR_reg.fit(X,Y)
MLR_predict = MLR_reg.predict(X)
Uzunluk = [a for a in range(1,Y.size+1)]
plt.scatter(Uzunluk,Y,color='red')
plt.plot(Uzunluk,MLR_predict,color='blue')
plt.show()




from sklearn.preprocessing import PolynomialFeatures as polyn
derece = len(veri.columns)+1

poly_reg = polyn(degree=12)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,Y)
Poly_predict = lin_reg2.predict(X)
plt.scatter(Uzunluk,Y,color='red')
plt.plot(Uzunluk,Poly_predict,color='blue')
plt.show()



from sklearn.metrics import r2_score as r2

MLR_R2 = r2(Y,MLR_predict)
print("MLR_R2 : ", MLR_R2)


Poly_R2 = r2(Y,Poly_predict)
print("Poly_R2 : ",Poly_R2)