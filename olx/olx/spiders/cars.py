# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['pe.olx.com.br']
    start_urls = ['http://pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios?q=veiculos/']

    # em caso de bloqueio do crawler com erro 544, devemos desbloquear a variavel constante USER_AGENT
    # descomentando a variavel pra não ser bloqueado.
    def parse(self, response):
        items = response.xpath('//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]')#pegando a ul e o id da ul e depois pegando li
        self.log(len(items))
        for item in items:
            #self.log(item.xpath('./a/href').extract_first())# Aqui a gente pega a url com os dados especifico
            url = item.xpath('./a/href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        #self.log(response.url)
        title = response.xpath('//title/text()').extract_first()
        year = response.xpath(
                    '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
        ).extract_first()
        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
        ).extract_first()

        yield {
            'title': title,
            'year': year,
            'ports': ports,
        }
