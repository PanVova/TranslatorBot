import random

from selenium import webdriver
from time import sleep


class TranslatorBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.jp_word=''
        self.eng_word=''
        self.list = []

    def read_from_file(self):
        with open('jpn_words.txt', 'r+', encoding='utf8') as f:
            for i in f.readlines():
                self.list.append(i)

    def translate_Word(self, word):
        self.driver.get('https://translate.google.ru/#view=home&op=translate&sl=ja&tl=ru')
        sleep(2)

        search_word= self.driver.find_element_by_xpath('//*[@id="source"]')
        search_word.send_keys(word)
        sleep(1)
        try:
            get_word= self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div').text
        except(Exception):
            get_word="No Translation Found"

        self.jp_word=word.rstrip("\n")
        self.eng_word=get_word
        #print(self.jp_word+'-'+self.eng_word)

    def write_to_File(self):
        with open('result.txt', 'a+', encoding='utf8') as f:
            f.write(self.jp_word + '-' + self.eng_word + '\n')


bot = TranslatorBot()
bot.read_from_file()
for i in bot.list:
    bot.translate_Word(i)
    bot.write_to_File()





