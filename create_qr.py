import qrcode


class CreateQr:
    def __init__(self):
        pass

    def create_qr(self):
        data = 'https://williamawng.github.io/'
 
        img = qrcode.make(data)
        
        img.save('MyQRCode1.png')

