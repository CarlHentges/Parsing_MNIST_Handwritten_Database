# this program parses the MNIST training labels dataset and outputs the result
# to the console, if a command line argument is specified then the program will
# parses that many labels, else it will only output the first one
# Carl Hentges 2018

import sys
ImageFile = open("train-images.idx3-ubyte", "rb")   # open label file
labelFile = open("train-labels.idx1-ubyte", "rb")   # open label file

if (len(sys.argv)==1):                          # if no command line argument
    toRead = 1;                                 # is given use 1
else:
    toRead = int(sys.argv[1])                   # read command line argument

try:

    for x in range(0,16):                     # the first 16 bytes specify image
        raw = ImageFile.read(1)               # file information printed here
        print(int.from_bytes(raw,byteorder='big'),end="")
    print("")

    for x in range(0,8):                      # the first 8 bytes specify label
        raw = labelFile.read(1)               # file information printed here
        print(int.from_bytes(raw,byteorder='big'),end="")
    print("")

    for x in range(0,toRead):                 # number of characters to read

        raw = labelFile.read(1)               # read and print byte form file
        print("-"*13,int.from_bytes(raw,byteorder='big'),"-"*13)

        for y in range(0,28):                 # columns per image
            for x in range(0,28):             # rows per image

                raw = ImageFile.read(1)       # read one byte form file
                if(int.from_bytes(raw,byteorder='big') == 0):
                    print(" ", end = "")      # if pixel value is 0 print ' '
                else:                         # if the pixel is not 0 (white)
                    print("X",end="")         # print 'X'
            print("")                         # print newline after each row
finally:
    ImageFile.close()                         # close Image file
    labelFile.close()                         # close Lable file
