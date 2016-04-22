__author__ = 'muli'

import qrcode
from PIL import  Image

def make_qr(str, savepath):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )

    qr.add_data(str)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(savepath)



if __name__ == '__main__':
    savepath = 'str.png'
    # str = 'http://sandbox.sjws.baidu.com:8080'
    str = 'http://sjws.baidu.com/apk/YhdsClient/apk-rel3/'
    make_qr(str, savepath)


000000