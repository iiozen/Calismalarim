def etkisizler():
    with open('etkisiz.txt','r',encoding='utf-8') as f:
        etkisiz = f.read()
        etkisiz =  etkisiz.replace(' ','')
        etkisiz = etkisiz.split(',')
        etkisiz = set(etkisiz)
    return etkisiz