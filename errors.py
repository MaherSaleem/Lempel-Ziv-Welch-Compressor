import sys

def printError(num):
    """
    printError() prints an error and usage message.
    @params: integer to customize the error message (1 if in decompress(),
             2 if in compress(), anything else for other).
    @return: n/a.
    """
    if num == 1:
        print('Error. Invalid compressed list given to decompress().')
    elif num == 2:
        print('Error. Invalid string given to compress().')
    else:
        print('Error.')
    print('Usage:')
    print('Compression: $ main.py <something>.txt <something>.lzw compress')
    print('Decompression: $ main.py <something>.txt <something>.lzw decompress')
    sys.exit()
