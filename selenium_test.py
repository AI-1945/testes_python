'''
# importa classe para iniciar o bowser
from selenium import webdriver
#import classe ActionChains responsavel pela manipulação
from selenium.webdriver.common.action_chains import ActionChains
#importa a classe keys que pode ser usada no key_up e key_down
from selenium.webdriver.common.keys import Keys


firefox = webdriver.Firefox()
firefox.get('https://www.jw.org/pt/publicacoes/revistas/?contentLanguageFilter=pt&pubFilter=w&yearFilter=2000')
actions = ActionChains(firefox)

actions.click_and_hold()
actions.release()
actions.perform()

botao = firefox.find_element_by_id('secondaryButton fileDownloadButton')
actions.click_and_hold(on_element=botao)
actions.perform()
'''

import selenium
import unittest, time, re

class NewTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(
                                 "http://www.google.com/"
                                  )
        self.selenium.start()
    def test_new(self):
        sel = self.selenium
        sel.open( " / " )
        sel.type( " q " , " selenium rc " )
        sel.click( " btnG " )
        sel.wait_for_page_to_load( " 30000 " )
        self.failUnless(sel.is_text_present( " Results * for selenium rc " ))
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)