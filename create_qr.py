import qrcode


class CreateQr:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def create_qr(self):
        img = qrcode.make(self.data)
        img.save(self.file_name)

