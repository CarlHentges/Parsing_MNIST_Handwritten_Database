# this program parses the MNIST training labels dataset and outputs the result
# to the console, if a command line argument is specified then the program will
# parses that many labels, else it will only output the first one
# Carl Hentges 2018

import sys
file = open("train-labels.idx1-ubyte", "rb")    # open label file

if (len(sys.argv)==1):                          # if no command line argument
    toRead = 1;                                 # is given use 1
else:
    toRead = int(sys.argv[1])                   # read command line argument

try:

    for x in range(0,8):                        # the first 8 bytes specify
        raw = file.read(1)                      # file information printed here
        print(int.from_bytes(raw,byteorder='big'),end="")
    print("")

    for x in range(0,toRead):                   # number of characters to read

        raw = file.read(1)                      # read and print byte form file
        print(int.from_bytes(raw,byteorder='big'))
finally:
    file.close()                                # close file
