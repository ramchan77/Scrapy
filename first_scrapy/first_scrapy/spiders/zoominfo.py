# -*- coding: utf-8 -*-
import scrapy
import cfscrape

class ZoominfoSpider(scrapy.Spider):
    name = 'zoominfo'
    allowed_domains = ['zoominfo.com']
    def start_requests(self):
        start_urls = ['https://www.zoominfo.com/p/Adam-Ciaccio/-1966996185',
                'https://www.zoominfo.com/p/Vingi-Chan/-928135210',
                'https://www.zoominfo.com/p/Vinicio-Cesar/-1496489623',
                'https://www.zoominfo.com/p/Vinicius-Cenci/-1623272474',
                'https://www.zoominfo.com/p/Vinicius-Cenci/-1623272474',
                'https://www.zoominfo.com/p/Vinicius-Cenci/-1914603951',
                'https://www.zoominfo.com/p/Vinicius-Cerbaro/-1159147027',
                'https://www.zoominfo.com/p/Vinicius-Cerci/-1538897694',
                'https://www.zoominfo.com/p/Vinicius-Cerezer/1864933383',
                'https://www.zoominfo.com/p/Vinicius-Cesar-pena/-1505233969',
                'https://www.zoominfo.com/p/Vinicius-Cesar/-1425848065',
                'https://www.zoominfo.com/p/Vinicius-Cesar/-1505920682',
                'https://www.zoominfo.com/p/Vinicius-Cesar/-1505957037',
                'https://www.zoominfo.com/p/Vinicius-Cesar/-1521562764',
                'https://www.zoominfo.com/p/Adrian-Ciupic%C4%83/1641183025',
                'https://www.zoominfo.com/p/Adrian-Ciuraru/-1845902357',
                'https://www.zoominfo.com/p/Adrian-Ciurea/-1449597674',
                'https://www.zoominfo.com/p/Adrian-Civici/1320553454',
                'https://www.zoominfo.com/p/Adrian-Claas/-1444411912',
                'https://www.zoominfo.com/p/Adrian-Claassen/-1409279109',
                'https://www.zoominfo.com/p/Adrian-Claassen/-979427438',
                'https://www.zoominfo.com/p/Adrian-Claassen/2054371055',
                'https://www.zoominfo.com/p/Adrian-Clabaugh/-1966871199',
                'https://www.zoominfo.com/p/Adrian-Clamp/-1974978315',
                'https://www.zoominfo.com/p/Adrian-eu-veng-Chin/-1450479763',
                'https://www.zoominfo.com/p/Adrian-Hernandez-cisneros/-948305877',
                'https://www.zoominfo.com/p/Adrian-Jefferson-chofor/-1291366149',
                'https://www.zoominfo.com/p/Adriana--alina-Ciumau/2153520684',
                'https://www.zoominfo.com/p/Adriana--stefania-Ciupeanu/-833323526',
                'https://www.zoominfo.com/p/Adriana-Altamirano-cid/2155095817',
                'https://www.zoominfo.com/p/Adriana-Becerra-cid/2204447162',
                'https://www.zoominfo.com/p/Adriana-Cedr%C3%BAn/-824280330',
                'https://www.zoominfo.com/p/Adriana-Cerdeira/-1480213569',
                'https://www.zoominfo.com/p/Adriana-Chil/-1239144541',
                'https://www.zoominfo.com/p/Adriana-Chil/-1508711802',
                'https://www.zoominfo.com/p/Adriana-Chilcott/-1231362363',
                'https://www.zoominfo.com/p/Adriana-Chilelli/-1313642446',
                'https://www.zoominfo.com/p/Adriana-Chilintana/-1874911620',
                'https://www.zoominfo.com/p/Adriana-Chiluisa/-1495918626',
                'https://www.zoominfo.com/p/Adriana-Chimello/-1506736945',
                'https://www.zoominfo.com/p/Adriana-Chimirel/-1514838920',
                'https://www.zoominfo.com/p/Adriana-Chin/-1046060310',
                'https://www.zoominfo.com/p/Adriana-Chinchilla-l%C3%B3pez/-932823851',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/-1018884411',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/-1139647398',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/-1182423520',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/-1527541492',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/-917462414',
                'https://www.zoominfo.com/p/Adriana-Chinchilla/47975069',
                'https://www.zoominfo.com/p/Adriana-Chinelato/-1313216703',
                'https://www.zoominfo.com/p/Adriana-Chinelatto/-1631309360',
                'https://www.zoominfo.com/p/Adriana-Chinelli/-1023612863',
                'https://www.zoominfo.com/p/Adriana-Chinelli/1213258356',
                'https://www.zoominfo.com/p/Adriana-Chinelli/1761427692',
                'https://www.zoominfo.com/p/Adriana-Ching/2165242516',
                'https://www.zoominfo.com/p/Adriana-Chingue/-1629886286',
                'https://www.zoominfo.com/p/Adriana-Chini/-835314191',
                'https://www.zoominfo.com/p/Adriana-Chinsky/-2059162715',
                'https://www.zoominfo.com/p/Adriana-Chinsky/1940430129',
                'https://www.zoominfo.com/p/Adriana-Chiocchi/9881269',
                'https://www.zoominfo.com/p/Adriana-Chiong/-1528722150',
                'https://www.zoominfo.com/p/Adriana-Chippari--gomes/-798941884',
                'https://www.zoominfo.com/p/Adriana-Chiquito/-2042693413']
        cf_requests = []
        for url in start_urls:
            token, agent = cfscrape.get_tokens(url)
            cf_requests.append(scrapy.Request(url=url,
                                       cookies=token,
                                       headers={'User-Agent': agent}))
        return cf_requests
    def parse(self, response):
    	yield {'people_link':response.url,'source':response.css('section.person_profile_box.vcard').extract_first()}
        
