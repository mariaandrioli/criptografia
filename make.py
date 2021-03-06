# creates small image for testing
from PIL import Image

tupledlist=[(27, 64, 164), (248, 244, 194), (174, 246, 250), (149, 95, 232),
(188, 156, 169), (71, 167, 127), (132, 173, 97), (113, 69, 206),
(255, 29, 213), (53, 153, 220), (246, 225, 229), (142, 82, 175),
(188, 156, 169), (71, 167, 127), (132, 173, 97), (113, 69, 206),
(27, 64, 164), (248, 244, 194), (174, 246, 250), (149, 95, 232),
(246, 225, 229), (142, 82, 175), (188, 156, 169), (71, 167, 127)]

OUTPUT_IMAGE_SIZE = (4, 6)
image = Image.new('RGB', OUTPUT_IMAGE_SIZE)
image.putdata(tupledlist)
image.save("test.png")