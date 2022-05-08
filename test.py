from inspect import getouterframes
import selenium.webdriver as webdriver
import time




web = webdriver.Firefox()



web.get('https://candidatures.univ-amu.fr/candidatures/#!accueilView')  # change your url here


time.sleep(2)

nom = "Gurram"
prenom = "Raviteja"
mail = "ravi.gurram6c@gmail.com"

creercompte = web.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[3]/div/div/div/div[3]/div/div[2]/div/div[13]/div')
creercompte.click()
time.sleep(2)

nom_box = web.find_element_by_xpath('//*[@id="gwt-uid-10"]')
nom_box.send_keys(nom)

prenom_box = web.find_element_by_xpath('//*[@id="gwt-uid-12"]')
prenom_box.send_keys(prenom)

addresse_mail_box = web.find_element_by_xpath('//*[@id="gwt-uid-14"]')
addresse_mail_box.send_keys(mail)

conf_mail_box = web.find_element_by_xpath('//*[@id="gwt-uid-16"]')
conf_mail_box.send_keys(mail)
time.sleep(2)
enregistrer = web.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[3]/div/div/div[5]/div/div/div[3]/div')
enregistrer.click()

