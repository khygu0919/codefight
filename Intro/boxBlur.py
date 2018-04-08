'''
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.
'''
def boxBlur(image):
    a=len(image)
    b=len(image[0])
    c=[]
    for i in range(0,a-2):
        d=[]
        for j in range(0,b-2):
            d.append((sum(image[i][j:j+3])+sum(image[i+1][j:j+3])+sum(image[i+2][j:j+3]))//9)
        c.append(d)
    return c