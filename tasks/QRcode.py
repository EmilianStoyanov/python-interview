# pip install pyqrcode
# pip install pypng

from pyqrcode import QRCode

dest = "https://www.coingecko.com/"

myQR = QRCode(dest)
myQR.show()
