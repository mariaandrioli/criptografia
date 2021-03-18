import sys
import os.path
from PIL import Image

def make_image(lista, size, name):
    image = Image.new('RGB', size)
    image.putdata(lista)
    image.save(name)

def usage():
    print("Execução: python [-e/-d] img1")

def decode(imgName):
    img = Image.open(imgName, 'r')
    print("decode")

def encode(imgName):
    msg = input('Mensagem secreta: ')
    img = Image.open(imgName, 'r')

    if len(msg) == 0:
        raise ValueError('Mensagem vazia')
    if len(msg) > img.size[0]*img.size[1]:
        raise ValueError('Mensagem muito grande')

    binario = ''.join(bin(x)[2:].zfill(8) for x in msg.encode('UTF-8'))

    result = [] 
    
    for t in img.getdata(): 
        for x in t: 
            result.append(x) 

    for i in range(len(binario)):
        if binario[i] == '0':
            if result[i] % 2 != 0:
                result[i] = result[i] - 1
        if binario[i] == '1':
            if result[i] % 2 == 0:
                result[i] = result[i] - 1


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