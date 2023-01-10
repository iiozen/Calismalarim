import re
import trkarakter
from etkisizKelimeler import etkisizler
from zemberek import TurkishMorphology


morphology = TurkishMorphology.create_with_defaults()
# nltk.download('stopwords',quiet=True)
# from nltk.corpus import stopwords
# durmaKelimeleri = set(stopwords.words('turkish'))
durmaKelimeleri = etkisizler()
        
    
def Onisleme(veri):
    veridegismis = []
    for cumle in veri:       
        ## Tırnak işareti dışı noktalama işaretleri ve sayıları temizliyorum.
        cumle.replace('','ö')
        cumleyeni = re.sub(trkarakter.turkceKarakterler,' ',cumle)
        # Tüm harfleri küçük harfe dönüştürüyorum.
        cumleyeni = cumleyeni.translate(trkarakter.lower_map)
        cumleyeni= cumleyeni.lower()
        
        # Kelimeleri ayırıyorum.
        cumleyeni = cumleyeni.split()
        for kelimeindex,kelime in enumerate(cumleyeni):
            # Kelimenin başı ve sonundaki boşlukları temizliyorum.
            kelime = kelime.strip()
            # Tırnak işaretini gelen ekiyle siliyorum.
            if kelime.find("'")!=-1:
                kelime=kelime[0:kelime.find("'")]
                cumleyeni[kelimeindex]=kelime



        # Etkisiz kelimeleri buluyorum.
        dusur=[]
        for say,kelimeic in enumerate(cumleyeni):
            if kelimeic in durmaKelimeleri:
                dusur.append(say)
        for sayi in range(len(dusur)-1,-1,-1):
            cumleyeni.pop(dusur[sayi])
        dusur=[]
            # Kalan kelimelerin köklerini buluyorum.
        for index in range(len(cumleyeni)-1,-1,-1):
            if cumleyeni[index]=='':
                cumleyeni.pop(index)
                
        for say,kelimeic in enumerate(cumleyeni):
            kelimeic = morphology.analyze(kelimeic).analysis_results
            try:
                kelimeic = str(kelimeic[0])
                ilk = kelimeic.find('[')
                iki = kelimeic.find(':',ilk)
                kelimeic = kelimeic[ilk+1:iki].strip()
                kelimeic = kelimeic.translate(trkarakter.lower_map)
                kelimeic = kelimeic.lower()
                cumleyeni[say]=kelimeic
            except:
                dusur.append(say)
        # Köklerini bulamadıklarımın ve etkisiz kelimelerin
        # indexini matrise kaydettim ve şimdi onları siliyorum.
        for sayi in range(len(dusur)-1,-1,-1):
            cumleyeni.pop(dusur[sayi])

        # Son olarak tek harf kalanları siliyorum.
        for i in range(len(cumleyeni)-1,-1,-1):
            if len(cumleyeni[i])<2:
                cumleyeni.pop(i)
        # Kelimeleri boşluklarla birleştirerek tekrar cümle haline getiriyorum.
        cumleyeni = ' '.join(cumleyeni)
        veridegismis.append(cumleyeni)
        
    # veriyeni = Onisleme(veri)
    # t = open('dnmcvp.txt','w',encoding='utf-8')
    # for s,cmle in enumerate(veriyeni):
    #     if s>0:
    #         veriyeni[s] = '\n'+cmle
    
    return veridegismis