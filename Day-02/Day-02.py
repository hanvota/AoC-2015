# Advent of Code 2015, Day-02
# https://adventofcode.com/2015

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Read in dimensions of each box with Box dimensions (length l, width w, and height h)
# Calculate Surface area of box 2*l*w + 2*w*h + 2*h*l
# add in extra with the area of the smallest side.

if __name__ == '__main__':

    totalArea = 0
    totalRibbon = 0
    dataFile = open('Day-02-data.txt', 'r')
    boxesDimension = dataFile.readlines()
    # print(f'Box is {boxesDimension}')
    # print(f'Length is {len(boxesDimension)}')

    for box in boxesDimension:  # box in format 'hxwxh\n'
        l, w, h = box.strip().split("x")  # strip off the trailing \n and spit into l,w,h at the 'x'
        boxLength = int(l)
        boxWidth = int(w)
        boxHeight = int(h)

        dimension1 = boxLength * boxWidth
        dimension2 = boxWidth * boxHeight
        dimension3 = boxHeight * boxLength
        smallestDimension = min(dimension1, dimension2, dimension3)
        surfaceArea = (2 * dimension1) + (2 * dimension2) + (2 * dimension3) + smallestDimension
        totalArea += surfaceArea

        perim1 = 2 * (boxLength + boxWidth)
        perim2 = 2 * (boxWidth + boxHeight)
        perim3 = 2 * (boxHeight + boxLength)
        smallestPerim = min(perim1, perim2, perim3)
        volume = boxLength * boxWidth * boxHeight  # for length of ribbon of the bow
        bowLength = smallestPerim + volume

        totalRibbon += bowLength

        # print(f'Box size is l:{boxLength} by w:{boxWidth} by h:{boxHeight}, '
        #       f'dim1 is {dimension1}, dim2 is {dimension2}, dim3 is {dimension3}. '
        #       f'smallest dim is {smallestDimension} and SA is {surfaceArea}')

    print(f'Part 1--Total Surface area is {totalArea}')
    print(f'Part 2--Total Ribbon Length is {totalRibbon}')

    dataFile.close()
