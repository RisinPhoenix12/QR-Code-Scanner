import pyqrcode
qr=pyqrcode.create('hello')
qr.svg('hello.svg',scale=7)