from ftplib import FTP

# some cool parameters and what not
nasdaqUrl = 'ftp.nasdaqtrader.com'

ftp = FTP(nasdaqUrl)
ftp.login()
ftp.retrlines('LIST')
print("========================================")
ftp.cwd('SymbolDirectory')
ftp.retrlines('LIST')

#bad way to do this but to lazy to care since this is some junk data for ML testing
with open('stockData', 'wb') as fp:
    ftp.retrbinary('RETR otherlisted.txt', fp.write)

with open('stockData', 'a') as fpp:
    ftp.retrlines('RETR nasdaqlisted.txt', fpp.write)