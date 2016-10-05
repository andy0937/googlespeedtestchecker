import requests
import config
from tqdm import tqdm


def makeURL(link):
    URL = config.host+link
    return URL

def makeRequest(url, strategy, api_key ):
    link = config.pagespeedHost + url+"&strategy="+strategy+"&fields=id%2CruleGroups"+"&key="+api_key
    r = requests.get(link)
    return r.json()


def parseJSON(response):
    id = response['id']
    r = response['ruleGroups']
    r1 = r['SPEED']
    r.clear()
    score = r1['score']
    r1.clear()
    return {
            'id': id,
            'score': str(score)}


if __name__ == '__main__':
    currentURL = open(config.sitemap)
    output = open(config.outputlog, 'w')
    for line in tqdm(currentURL.readlines()):
        k = makeURL(line.strip('\t\n'))
        req = makeRequest(k, config.strategy, config.api_key)
        vals = parseJSON(req)
        writeStr = vals['id'] + '|' + vals['score'] + '\n'
        output.write(writeStr)
currentURL.close()
output.close()