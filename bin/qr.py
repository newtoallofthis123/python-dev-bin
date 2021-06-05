import pyqrcode as qrc

print("Qr-Code Generator using python")

def qr(name, data):
    qr_code = qrc.create(data)
    qr_code.png(name, scale=10)

da = str(input("Data of Qr-code: "))
na = str(input("Name of qr-code: ")) + ".png"

qr(na, da)