from Hesaplar import kullaniciAd,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
sayfa = webdriver.Chrome()
sayfa.get("https://www.instagram.com/?hl=tr")
time.sleep(1.3)
kullaniciAd_giris = sayfa.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
sifre_giris = sayfa.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
kullaniciAd_giris.send_keys(kullaniciAd)
sifre_giris.send_keys(sifre)
giris_Buton = sayfa.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
giris_Buton.click()
time.sleep(3)
sayfa.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
time.sleep(0.3)
sayfa.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]').click()
time.sleep(2)
sayfa.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(2)
dialog = sayfa.find_element_by_css_selector("div[role=dialog] ul")



takipcisayisi = len(dialog.find_elements_by_css_selector('li'))
print(f"first count: {takipcisayisi}")
action = webdriver.ActionChains(sayfa)
while True:
    dialog.click()
    
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    time.sleep(1)    
    newCount = len(dialog.find_elements_by_css_selector('li'))
    print(f"NewCount: {newCount}")
    if newCount==takipcisayisi:
        break
    else:
        takipcisayisi=newCount    




liste = dialog.find_elements_by_css_selector('li')



print(f"Toplam Takip Edilen Sayısı: {len(liste)}\nTakip Ettiklerinin Linkleri:")
for eleman in liste:
    eklenir = eleman.find_element_by_css_selector("a").get_attribute("href")
    print(eklenir)

time.sleep(5)
sayfa.close()
