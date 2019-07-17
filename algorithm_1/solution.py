import copy, re

def integerEncode(num):
    '''switch integer to encode list'''

    numBinary = bin(num)[2:]                            # first we convert integer to binary
    resultEncode = []                                   # store result
    singleEncodeNum = ''                                # string type for single input number
    print(f'  In base 2, {num} reads as {numBinary}')
    tempNumBinary = copy.deepcopy(numBinary)
    while len(tempNumBinary) > 1:
        if tempNumBinary[0] == tempNumBinary[1]:        # now we get 2 consecutive same bits
            singleEncodeNum += tempNumBinary[0]         # put one bit into singleEncodeNum
            tempNumBinary = tempNumBinary[2:]
        else:
            singNum = int(singleEncodeNum, 2)           # now we get 2 different bits
            resultEncode.append(singNum)                # append previous number to result
            tempNumBinary = tempNumBinary[1:]           # we discard current bit
    if tempNumBinary or singleEncodeNum:                # if there is still some bits left
        if tempNumBinary:
            singleEncodeNum += tempNumBinary[0]         # we update
        singNum = int(singleEncodeNum, 2)
        resultEncode.append(singNum)
    print(f'  It encodes: {resultEncode}')

def encodeListToInt(encodeList):
    '''switch encode list to orginal number'''

    encodeListBinary = []
    originalInteger = ''                               # we first get original iteger binary
    for element in encodeList:                         # change encoded number into binary style
        encodeListBinary.append(int(bin(int(element))[2:]))
    print(f'  In base 2, {encodeList} reads as {encodeListBinary}')
    for item in encodeListBinary:
        item = str(item)
        if originalInteger:                            # handle the bit the we discard before
            if item[0] == '0':
                originalInteger += '1'
            else:
                originalInteger += '0'
        while item:                                    # for every bit we plus twice
            originalInteger += item[0]
            originalInteger += item[0]
            item = item[1:]
    resultInteger = int(originalInteger, 2)
    print(f'  It is encoded by {resultInteger}')

def main():
    inputContent = input('Input either a strictly positive integer\nor a nonempty \
list of strictly positive integers: ')
    if inputContent[0] == '[':
        inputContent = inputContent[1:]               # discard '['
        inputContent = inputContent[0:-1]             # discard ']'
        encodeList = re.split('[,]', inputContent)    # get elements
        print(encodeList)
        encodeListToInt(encodeList)
    else:
        integerEncode(int(inputContent))

if __name__ == '__main__':
    main()