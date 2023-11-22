import create_qr


cq = create_qr.CreateQr(data="https://williamawng.github.io/", file_name="william_website_qr.png")
cq.create_qr()

cq2 = create_qr.CreateQr(data="https://scratch.mit.edu/projects/194895616", file_name="geometry_dash_qr.png")
cq2.create_qr()