from selenium import webdriver
from mailsifreHesap import sifre
from mailAdSoyad import ad,soyad
from mailHesap import mail
from HotmailSahip import kontrol_email,kontrol_sifre
import time


class mailcreateProton:
    def __init__(self,mail,sifre,kontrol_email,kontrol_sifre):
        self.mail = mail
        self.sifre = sifre
        self.kontrol_sifre = kontrol_sifre
        self.kontrol_email = kontrol_email
    def sayfa1(self):
        sayfa = webdriver.Firefox()
        self.sayfa = sayfa
        sayfa.get("https://mail.protonmail.com/create/new?language=en")
        time.sleep(3)
        iframe = sayfa.find_elements_by_tag_name('iframe')[0]
        frame = sayfa.switch_to_frame(iframe)
        a = sayfa.find_element_by_xpath('//*[@id="username"]')
        a.send_keys(self.mail)
        iframereturn = sayfa.switch_to_default_content()
        sifre1 = sayfa.find_element_by_xpath('//*[@id="password"]')
        sifre2 = sayfa.find_element_by_xpath('//*[@id="passwordc"]')
        sifre1.send_keys(self.sifre)
        sifre2.send_keys(self.sifre)
        iframe = sayfa.find_elements_by_tag_name('iframe')[1]
        frame = sayfa.switch_to_frame(iframe)
        recoverymail = sayfa.find_element_by_xpath('//*[@id="notificationEmail"]')
        recoverymail.send_keys(self.kontrol_email)
        buton = sayfa.find_element_by_xpath('//*[@id="app"]/div/footer/button').click()
        time.sleep(2)
        self.sayfa2()
    def sayfa2(self):
        buton = self.sayfa.find_element_by_xpath('//*[@id="id-signup-radio-email"]').click()
        time.sleep(1.3)
        recoverymail = self.sayfa.find_element_by_xpath('//*[@id="emailVerification"]')
        recoverymail.send_keys(kontrol_email)
        time.sleep(1)
        buton = self.sayfa.find_element_by_xpath('//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button')
        buton.click()
        time.sleep(2)
        emailOnay(self.kontrol_email,self.kontrol_sifre) 
    def bitir(self,onayKodu):
        pass
        # complete_Button = self.sayfa.find_element_by_xpath('//*[@id="verification-panel"]/p[3]/button')
        # complete_Button.click()
        # time.sleep(5)
        
    # def bitir(self,onayKodu):

class emailOnay:
    def __init__(self,kontrol_email,kontrol_sifre):
        self.onay_sifre = kontrol_sifre
        self.onay_email = kontrol_email
        onaysayfa = webdriver.Chrome()
        self.onaysayfa = onaysayfa
        onaysayfa.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1595253122&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dfbd6e77e-8727-15a1-a819-a5acdb8feed5&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
        time.sleep(5)
        self.sayfa1()
    def sayfa1(self):
        tm_mail = self.onaysayfa.find_element_by_xpath('//*[@id="i0116"]')
        tm_mal.send_keys(self.onay_email)
        time.sleep(0.7)
        self.onaysayfa.find_elements_by_xpath('//*[@id="idSIButton9"]').click()




start = mailcreateProton(mail,sifre,kontrol_email,kontrol_sifre)
start.sayfa1()
