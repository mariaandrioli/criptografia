import sys
from PIL import Image

def main(imgName):
    try:
        img = Image.open(imgName, 'r')
        height, width = img.size
    except IOError:
        print ('%s could not be opened' % imgName)

    print()

if __name__ == "__main__":
    imgName = sys.argv[1]
    main(imgName)