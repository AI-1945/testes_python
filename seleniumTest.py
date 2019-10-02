from selenium import webdriver

firefox = webdriver.Firefox()
firefox.get('http://localhost:63342/testes_python/index_test.html?_ijt=mltudk9ifg58pir45jlv1es51u')
continue_link = firefox.find_element_by_link_text('Continue')

print(continue_link)

# Link para eestudo do selenium
# https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text

# para poder pegar todos os elementos em uma pagina onde
# preciso baixar arquivos pdf, preciso colocar as tags dentro
# de um  loop para que possa pegar todos os links de download