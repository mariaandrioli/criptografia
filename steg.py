import sys
import os.path
import math
from PIL import Image

MAX_SIZE_MSG = 255

def needed_bytes(size):
    return math.ceil(math.log(size[0]*size[1]))

def make_image(lista, size, name):
    image = Image.new('RGB', size)
    image.putdata(lista)
    image.save(name)

def usage():
    print("Execução: python [-e/-d] img1")

def decode(imgName):
    img = Image.open(imgName, 'r')

    result = [] 
    
    for t in img.getdata(): 
        for x in t: 
            result.append(x) 

    # print(result)

    tam = ''
    for i in range(8):
        if result[i] % 2 == 0:
            tam = tam + '0'
        else:
            tam = tam + '1'

    tam = int(tam, 2)
    msg = ''

    for i in range(8,tam*8+8):
        if result[i] % 2 == 0:
            msg = msg + '0'
        else:
            msg = msg + '1'

    n = ''.join([chr(int(msg[i:i+8],2)) for i in range(0,len(msg),8)])
    print("Mensagem secreta:", n)

    # imgdata = iter(result)
    # tupled = [*zip(imgdata, imgdata, imgdata)]
    # make_image(tupled, img.size, "encoded.png")

def encode(imgName):
    msg = input('Mensagem secreta: ')
    img = Image.open(imgName, 'r')

    # for i in img.getdata():
    #     print(i)

    if len(msg) == 0:
        raise ValueError('Mensagem vazia')
    if len(msg) > img.size[0]*img.size[1] or len(msg) > MAX_SIZE_MSG:
        raise ValueError('Mensagem muito grande')

    binario = ''.join(bin(x)[2:].zfill(8) for x in msg.encode('UTF-8'))

    result = [] 

    tam_bin = bin(len(msg))[2:]
    tam = '00000000' + tam_bin
    tam = tam[len(tam_bin):]

    for t in img.getdata(): 
        for x in t: 
            result.append(x) 

    for i in range(len(tam)):
        if tam[i] == '0':
            if result[i] % 2 != 0:
                result[i] = result[i] - 1
        if tam[i] == '1':
            if result[i] % 2 == 0:
                result[i] = result[i] - 1

    for i in range(len(binario)):
        if binario[i] == '0':
            if result[i+8] % 2 != 0:
                result[i+8] = result[i+8] - 1
        if binario[i] == '1':
            if result[i+8] % 2 == 0:
                result[i+8] = result[i+8] - 1


    imgdata = iter(result)
    tupled = [*zip(imgdata, imgdata, imgdata)]
    make_image(tupled, img.size, "encoded.png")

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