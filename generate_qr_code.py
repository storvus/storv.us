import os

import qrcode

# qr = qrcode.QRCode

# qrcode.make("http://localhost:63342/storv.us/quest107c2c93-3680-430d-be12-786dce7769d1.html?_ijt=291lt058hen75437pdogu0j7ni").save("qrcode.png")

url = "https://storvus.github.io/storv.us/quest107c2c93-3680-430d-be12-786dce7769d1.html"
qr = qrcode.QRCode(
    version=1,  # размер (1–40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # высокий уровень коррекции (чтобы не повредился при вставке лого)
    box_size=10,  # размер "квадратиков"
    border=4,     # рамка
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white").convert("RGB")
print("Файл сохранён в:", os.getcwd())

img.save("images/quest0/qrcode.png")
