from barcode import EAN13, Code39, Code128, ISBN13

from barcode.writer import ImageWriter


class CreateBarcode:
    def __init__(self):
        pass

    def generate_bar_code(self, data, file_name):

        code = Code128(data, writer = ImageWriter())
        #code = EAN13(number) 
        #code = Code39(number)
        options = {
                    "font_size": 7
                }
        code.save(file_name, options)

    def generate_isbn13(self, data, file_name):

        code = ISBN13(data, writer=ImageWriter())
        options = {
                    "font_size": 7
                }
        code.save(file_name, options)

