# cpe489: image processing and computer vision

## official tutorial in Thai
https://www.youtube.com/playlist?list=PLJHz4JesQovaLLuBQkpx1TaVWXQhDsZiv

## ocr
to do an ocr, you'll need to do some steps first.
1. threshold
2. convolution

### histogram
the count of px on each color shade.
graph: y- px count, x- color value

### threshold
make sense to do on 2 color images. threshold a grayscale image by choose a 0-255 value.

### convolution
MATH: dot product between an image and a small image(filter, template, matrix or mask)

#### blur
mean blur treat every squares equal
1  |  1 |  1 |  1 |  1
1  |  1 | 1  |  1 |  1
1  | 1  | 1  | 1  |  1
1  |  1 | 1  | 1  |  1
1  |  1 |  1 | 1  |  1

gaussian blur treat central pixel more heavy than the conner/boarder pixel.
1  |  1 |  1 |  1 |  1
1  |  2 | 3  |  2 |  1
1  | 3  | 4  | 3  |  1
1  |  2 | 3  | 2  |  1
1  |  1 |  1 | 1  |  1


## Tip
1. It's hard to explain image processing in RGB color. So, I changed it to gray image first.
