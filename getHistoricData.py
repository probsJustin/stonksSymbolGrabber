import requests
import logging
import multiprocessing
import datetime


stockDataList = list()

with open("stocksymbols", "r") as fpReader:
    stonksSymbols = fpReader.read().split('\n')

logging.basicConfig(filename='./historicStockData',level=logging.DEBUG)


def workerFunction(stockSymbol):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stockSymbol + "&apikey=--"
    response = requests.request("GET", url)
    return response.text


def mp_worker(textWorker):
    print(" Processs Starting: " + textWorker)
    logging.info(workerFunction(textWorker))
    print(" Process Stopping: " + textWorker)

def mp_handler():
    p = multiprocessing.Pool(5)
    p.map(mp_worker, stonksSymbols)


if __name__ == '__main__':
    mp_handler()

