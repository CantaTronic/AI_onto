
from json import dump
from time import sleep
import datetime as dt
from uuid import uuid5, UUID, NAMESPACE_URL
import json
import requests
import logging
from bs4 import BeautifulSoup
from lxml.etree import fromstring, QName
import xmljson
#from db import DB

logging.basicConfig(filename='arxiv.log', level=logging.INFO)

#db = DB('postgresql://tech_forecast:5odnVv9tjYoMoeQy@localhost:1004/arxiv')
g_article_ids = set()

def xml2json(xml):
    xml = fromstring(xml)
    for it in xml.iter():
        it.tag = QName(it).localname
        if it.text is not None:
            it.text = it.text.strip()
    for it in xml.iter('link'):
        it.text = it.attrib['href']
        it.tag = f'link_{it.attrib["rel"]}'
    for it in xml.iter('primary_category'):
        it.text = it.attrib['term']
    for it in xml.iter('category'):
        it.text = it.attrib['term']
    xml = xmljson.parker.data(xml)
    if not isinstance(xml['category'], list):
        xml['category'] = [xml['category']]
    return xml

URL = 'http://export.arxiv.org/api/query'
#N_REC = 1000
N_REC = 10

CATS = {}
#query = db.select(
    #db.public.categories.c.id,
    #db.public.categories.c.name,
#)
#for row in db.execute(query):
    #if row.name is None: continue
    #CATS[row.name] = row.id

#def init():
    #for i, row in enumerate(db.exec_stream(db.select(db.public.articles.c.id))):
        #if i % 1000 == 0: print(i, end='\r')
        #g_article_ids.add(UUID(row[0]).bytes)


def get_data(cat, start_rec):
    for i in range(8):
        params = {
            'search_query': f'cat:{cat}',
            'start': start_rec,
            'max_results': N_REC,
            'sortBy': 'submittedDate',
            'sortOrder': 'ascending',
        }
        try:
            response = requests.get(url=URL, params=params, timeout=60)
        except Exception as e:
            logging.warning(
                f'{dt.datetime.now().isoformat()}:'
                f' exception {type(e).__name__}:'
                f' ({str(e)})'
            )
            sleep(60*2**i)
            continue
        if response.status_code == 200:
            sleep(3)
            return response.text
        logging.warning(
            f'{dt.datetime.now().isoformat()}:'
            f' status_code = {response.status_code}'
            f' ({response.text})'
        )
        continue
    logging.error(
        f'{dt.datetime.now().isoformat()}:'
        f' failed get_data(date={date.isoformat()}, start_rec={start_rec})'
    )
    raise RuntimeError(
        f'Failed get_data(date={date.isoformat()}, start_rec={start_rec})'
    )

def parse_records(data):
    articles = []
    parsed = BeautifulSoup(data, 'lxml-xml')
    totalresults = int(parsed.find('opensearch:totalResults').get_text())
    for entry in parsed.find_all('entry'):
        url = entry.find('id').get_text()
        uuid = uuid5(NAMESPACE_URL, url)
        if uuid.bytes in g_article_ids: continue
        g_article_ids.add(uuid.bytes)
        uuid = str(uuid)
        xml = entry.prettify()
        json = xml2json(xml)
        #articles.append({
            #'id': uuid,
            #'url': url,
            #'published': entry.find('published').get_text(),
            ##'xml': xml,
            ##'primary_category_id': CATS.get(json['primary_category']),
            #'json': json,
        #})
        articles.append(json)
    return articles, totalresults

def get_all_data(cat):
    logging.info(
        f'{dt.datetime.now().isoformat()}:'
        f' getting data for {cat}...'
    )
    start_rec = 0
    while True:
        t = get_data(cat, start_rec)
        articles, totalresults = parse_records(t)
        #print (articles)
        with open("outfile.json", "w") as f:
            dump(articles, f, indent=4, ensure_ascii=False)
        break
        #if len(articles):
            #db.execute(db.public.articles.insert(), articles)
        #else:
            #break
        logging.info(
            f'{dt.datetime.now().isoformat()}:'
            f' startindex={start_rec},'
            f' totalresults={totalresults},'
            f' articles={len(articles)}'
        )
        start_rec += N_REC
        if totalresults <= start_rec:
            break
        #break

#>>> result = requests.get('http://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=10&sortBy=submittedDate&sortOrder=ascending')
#>>> parsed = BeautifulSoup(result.text, 'html.parser')
#>>> t = parsed.find('opensearch:totalresults').get_text()
#>>> parsed.find_all('entry')

#astro-ph.IM

if __name__ == '__main__':
    #init()
    #cats = db.execute(
        #db.select(
            #db.public.categories.c.id,
            #db.public.categories.c.name,
        #).order_by(
            #db.public.categories.c.id
        #).where(
            #db.public.categories.c.parent_id != None
        #)
    #).fetchall()
    cats = [
        #"astro-ph.CO",
        #"astro-ph.EP",
        #"astro-ph.GA",
        #"astro-ph.HE",
        "astro-ph.IM",
        #"astro-ph.SR",
        ##hep-ex,
        ##hep-ph,
        ##hep-th,
        ##nucl-ex,
        ##nucl-th
    ]   #categories, within which we donwload the metadata
    for cat in cats:
        get_all_data(cat)
