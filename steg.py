import sys
import os.path
from PIL import Image

def usage():
    print("Execução: python [-e/-d] img1")

def decode(imgName):
    img = Image.open(imgName, 'r')
    print("decode")

def encode(imgName):
    msg = input('Mensagem secreta: ')

    if len(msg) == 0:
        raise ValueError('Mensagem vazia')

    binario = ''.join(format(ord(x), 'b') for x in msg)

    print(msg, binario)
    img = Image.open(imgName, 'r')

    data = ''
    imgdata = iter(img.getdata())

    print(list(img.getdata()))

def main(imgName, operation):
    try:
        if operation[1] == 'e':
            encode(imgName)
        elif operation[1] == 'd':
            decode(imgName)
    except IOError:
        print ('%s could not be opened' % imgName)

    print()

if __name__ == "__main__":
    try:
        operation = sys.argv[1]
        imgName = sys.argv[2]
        if (operation != "-e" and operation != "-d"):
            usage()
            print("Use -e para encode e -d para decode")
            sys.exit()
        if (os.path.splitext(imgName)[1].lower() != ".png"):
            usage()
            print("Imagem deve ser PNG")
            sys.exit()
    except IndexError:
        usage()

    print("===================================================================")
    print("Maria Teresa Kravetz Andrioli - GRR20171602")
    print("Esteganografia usando técnica LSB")
    usage()
    print("===================================================================\n")
    main(imgName, operation)