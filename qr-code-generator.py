import qrcode as qr


link = str(input("link: "))
img = qr.make(link)
type(img) 
img.save("qrcode.png")
