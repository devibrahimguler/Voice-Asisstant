from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import passwords
import arinListen as AL
import time


def askOnAsk(askInAsk, browser, name):
    if name == 'instagram':
        if 'profil' in askInAsk:
            browser.get('https://www.instagram.com/muntazif/')
        if 'ana sayfa' in askInAsk:
            browser.get('https://www.instagram.com')
        if "keşfet" in askInAsk:
            browser.get('https://www.instagram.com/explore/')
        if 'mesajlar' in askInAsk:
            browser.get('https://www.instagram.com/direct/inbox/')
        if 'aşağı in' in askInAsk:
            loop = 0
            while loop <= 10:
                stop = AL.arinListen()
                if 'dur' in stop:
                    break
                browser.find_element_by_xpath('/html/body').send_keys(Keys.SPACE)
                time.sleep(2)
                loop += 1

    if name == 'facebook':
        if 'profil' in askInAsk:
            browser.get('https://www.facebook.com/ibrahim.guler.35977897')
        if 'ana sayfa' in askInAsk:
            browser.get('https://www.facebook.com')
        if "keşfet" in askInAsk:
            browser.get('https://www.facebook.com/watch')
        if 'mesajlar' in askInAsk:
            browser.get('https://www.facebook.com/messages/t')
        if 'aşağı in' in askInAsk:
            browser.find_element_by_xpath(
                '//*[@id="facebook"]/body').send_keys(Keys.SPACE)
    if name == 'search':
        if 'ilk sayfa' in askInAsk:
            browser.find_element_by_xpath(
                '//*[@id="rso"]/div/div[1]/div/div/div[1]/a/h3')
        if 'aşağı in' in askInAsk:
            loop = 0
            while loop <= 10:
                stop = AL.arinListen()
                if 'dur' in stop:
                    break
                browser.find_element_by_xpath('//*[@id="gsr"]').send_keys(Keys.SPACE)
                time.sleep(2)
                loop += 1


def asks(asking):
    if 'instagram' in asking:
        name = 'instagram'
        browser = webdriver.Safari()
        time.sleep(2)
        browser.get('https://www.instagram.com')
        time.sleep(2)
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(passwords.instagramUser)
        time.sleep(2)
        browser.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passwords.instagramPassword, Keys.ENTER)
        AL.arinListen('ihtiyacın olursa seslen.'.lower())
        while True:
            shutdown = 0
            wait = AL.arinListen().lower()
            wait = wait
            print(wait)
            if 'mira' in wait:
                AL.arinListen('ne istersin'.lower())
                while True:
                    askInAsk = AL.arinListen().lower()
                    print(askInAsk)
                    if 'bekle' in askInAsk:
                        shutdown = 0
                        break
                    if 'çık' in askInAsk:
                        shutdown = 1
                        break
                    if 'kapat' in askInAsk:
                        shutdown = 1
                        break
                    askOnAsk(askInAsk, browser, name)
            if shutdown == 1:
                browser.close()
                break
    elif 'facebook' in asking:
        name = 'facebook'
        browser = webdriver.Safari()
        browser.get('https://www.facebook.com')
        time.sleep(2)
        browser.find_element_by_xpath(
            '//*[@id="email"]').send_keys(passwords.fecebookUser)
        time.sleep(2)
        browser.find_element_by_xpath(
            '//*[@id="pass"]').send_keys(passwords.fecebookPassword, Keys.ENTER)
        AL.arinListen('ihtiyacın olursa seslen.'.lower())
        while True:
            shutdown = 0
            wait = AL.arinListen().lower()
            print(wait)
            if 'mira' in wait:
                AL.arinListen('ne istersin'.lower())
                while True:
                    askInAsk = AL.arinListen().lower()
                    print(askInAsk)
                    if 'bekle' in askInAsk:
                        shutdown = 0
                        break
                    if 'çık' in askInAsk:
                        shutdown = 1
                        break
                    if 'kapat' in askInAsk:
                        shutdown = 1
                        break
                    askOnAsk(askInAsk, browser, name)
            if shutdown == 1:
                browser.close()
                break
    else:
        if asking != '':
            name = 'search'
            browser = webdriver.Safari()
            browser.get(f'https://www.google.com/search?q={asking}')
            AL.arinListen('ihtiyacın olursa seslen.'.lower())
            while True:
                shutdown = 0
                wait = AL.arinListen().lower()
                print(wait)
                if 'mira' in wait:
                    AL.arinListen('ne istersin'.lower())
                    while True:
                        askInAsk = AL.arinListen().lower()
                        print(askInAsk)
                        if 'bekle' in askInAsk:
                            shutdown = 0
                            break
                        if 'çık' in askInAsk:
                            shutdown = 1
                            break
                        if 'kapat' in askInAsk:
                            shutdown = 1
                            break
                        askOnAsk(askInAsk, browser, name)
                if shutdown == 1:
                    browser.close()
                    break
