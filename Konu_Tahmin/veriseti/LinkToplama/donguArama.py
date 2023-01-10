from bs4 import BeautifulSoup as bs
def htmlIcerikdondur(html:list,soupic:str,soupclass=''):
    soup = []
    for i in html:
        if soupic!='':
            try:
                i.find(soupic)
                soup.append(i)
            except:
                pass
        else:
            try:
                i.find(soupic,class_=soupclass)
                soup.append(i)
            except:
                pass
    return soup