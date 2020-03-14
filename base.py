from ftplib import FTP

# some cool parameters and what not
nasdaqUrl = 'ftp.nasdaqtrader.com'
symbols = list()


ftp = FTP(nasdaqUrl)
ftp.login()
ftp.retrlines('LIST')
print("========================================")
ftp.cwd('SymbolDirectory')
ftp.retrlines('LIST')

#bad way to do this but to lazy to care since this is some junk data for ML testing
with open('stockData', 'wb') as fp:
    ftp.retrbinary('RETR otherlisted.txt', fp.write)
    ftp.retrbinary('RETR nasdaqlisted.txt', fp.write)

with open("stockData", "r") as fpReader:
    stonksSymbols = fpReader.read()
    for x in stonksSymbols.split('\n')[0:-2]:
        symbol = x.split('|')
        symbols.append(symbol[0])

with open('stocksymbols', 'w') as fp:
    for x in symbols:
        fp.write(x + '\n')