import sys
import os.path
import math
import random
from PIL import Image

MAX_SIZE_MSG = 255
BITS_IN_BYTE = 8

def needed_bytes(size):
    return math.ceil(math.log(size[0]*size[1], 2)/8)

def max_start(size, tam, result):
    qtd = needed_bytes(size)*BITS_IN_BYTE
    total = result - qtd - (tam*BITS_IN_BYTE)
    return total

def get_start(size, tam, result):
    total = max_start(size,tam, result)
    rand = random.randint(8, total)
    return rand

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

    tam = ''
    for i in range(8):
        if result[i] % 2 == 0:
            tam = tam + '0'
        else:
            tam = tam + '1'
    tam = int(tam, 2)

    start = ''
    max = len(result) - needed_bytes(img.size)*BITS_IN_BYTE

    # for i in range(len(result)):
    #     print(i, result[i])

    for i in range(max, len(result)):
        if result[i] % 2 == 0:
            start = start + '0'
        else:
            start = start + '1'
    start = int(start, 2)

    msg = ''

    for i in range(start,tam*BITS_IN_BYTE+start):
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

    start = get_start(img.size, len(msg), len(result))
    start_binario = bin(start)[2:]
    start_b_string = '0'*needed_bytes(img.size)*BITS_IN_BYTE + start_binario
    start_b_string = start_b_string[len(start_binario):]
    print(start)

    max = max_start(img.size, len(msg), len(result)) + (len(msg)*BITS_IN_BYTE)
    for i in range(len(start_b_string)):
        if start_b_string[i] == '0':
            if result[max+i] % 2 != 0:
                result[max+i] = result[max+i] - 1
        if start_b_string[i] == '1':
            if result[max+i] % 2 == 0:
                result[max+i] = result[max+i] - 1

    for i in range(len(binario)):
        if binario[i] == '0':
            if result[start+i] % 2 != 0:
                result[start+i] = result[start+i] - 1
        if binario[i] == '1':
            if result[start+i] % 2 == 0:
                result[start+i] = result[start+i] - 1

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