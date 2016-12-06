import config
import requests
from tqdm import tqdm

def makeRequest(url):
    r = requests.get(url)
    return r.status_code

if __name__ == '__main__':
    outputlog = 'response_codes.csv'
    currentURL = open(config.sitemap)
    output = open(outputlog, 'w')
    for line in tqdm(currentURL.readlines()):
        url = line.strip('\t\n')
        req = makeRequest(url)
        if req == 200:
            None
        else:
            writeStr = req + '|' + url
            output.write(writeStr)
    currentURL.close()
    output.close()