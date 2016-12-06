import sys
import requests
import config
from tqdm import tqdm

def clear():
    sys.stdout.write('\033[1J')
    sys.stdout.write('\033[;H')

def strategyPicker():
    strategy_counter = int()
    while strategy_counter!=1 or strategy_counter!=2:
        print("\rStrategy:\n"
           "1. desktop\n"
           "2. mobile")
        strategy_counter = int(input())
        if strategy_counter == 1:
            strategy = "desktop"
            break
        elif strategy_counter == 2:
            strategy = "mobile"
            break
        else:
             clear()
    return strategy

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
    strategy = strategyPicker()
    outputlog = 'result_'+strategy+'.csv'
    currentURL = open(config.sitemap)
    output = open(outputlog, 'w')
    for line in tqdm(currentURL.readlines()):
        url = line.strip('\t\n')
        req = makeRequest(url, strategy, config.api_key)
        vals = parseJSON(req)
        writeStr = vals['score'] + ' | ' + vals['id'] + '\n'
        output.write(writeStr)
    currentURL.close()
    output.close()