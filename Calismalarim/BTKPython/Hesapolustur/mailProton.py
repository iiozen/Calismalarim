from selenium import webdriver
from mailsifreHesap import sifre
from mailAdSoyad import ad,soyad
from mailHesap import mail
from HotmailSahip import kontrol_email,kontrol_sifre
import time

sayfa = webdriver.Chrome()
sayfa.get("https://mail.protonmail.com/create/new?language=en")
time.sleep(3)


iframe = sayfa.find_elements_by_tag_name('iframe')[0]
frame = sayfa.switch_to_frame(iframe)

a = sayfa.find_element_by_xpath('//*[@id="username"]')
a.send_keys(mail)






iframereturn = sayfa.switch_to_default_content()
sifre1 = sayfa.find_element_by_xpath('//*[@id="password"]')
sifre2 = sayfa.find_element_by_xpath('//*[@id="passwordc"]')
sifre1.send_keys(sifre)
sifre2.send_keys(sifre)



iframe = sayfa.find_elements_by_tag_name('iframe')[1]
frame = sayfa.switch_to_frame(iframe)
recoverymail = sayfa.find_element_by_xpath('//*[@id="notificationEmail"]')
recoverymail.send_keys(kontrol_email)

buton = sayfa.find_element_by_xpath('//*[@id="app"]/div/footer/button').click()
time.sleep(2)



buton = sayfa.find_element_by_xpath('//*[@id="id-signup-radio-email"]').click()
time.sleep(1.3)
recoverymail = sayfa.find_element_by_xpath('//*[@id="emailVerification"]')
recoverymail.send_keys(kontrol_email)
time.sleep(1)
buton = sayfa.find_element_by_xpath('//*[@id="verification-panel"]/form[1]/div[1]/div[2]/button')
buton.click()
time.sleep(2)



complete_Button = sayfa.find_element_by_xpath('//*[@id="verification-panel"]/p[3]/button')
complete_Button.click()


