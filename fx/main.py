from PIL import Image,ImageEnhance,ImageTk

def contrast(img,value):
    enhancer= ImageEnhance.Contrast(img)
    im_out = enhancer.enhance(value)
    im_out.save('result.png')
    im_out.show()


def bright(img, value):
    enhancer = ImageEnhance.Brightness(img)
    im_out = enhancer.enhance(value)
    im_out.save('result.png')
    im_out.show()


def sharp(img, value):
    enhancer = ImageEnhance.Sharpness(img)
    im_out = enhancer.enhance(value)
    im_out.save('result.png')
    im_out.show()

def gray(img):
    im_out = img.convert('LA')
    im_out.save('result.png')
    im_out.show()

def main():
    img = Image.open('cat.jpg')
    contrast(img,10)
    bright(img,10)
    sharp(img,10)
    gray(img)

if __name__=='__main__':
    main()
