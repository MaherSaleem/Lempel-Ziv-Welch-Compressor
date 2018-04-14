from errors import printError


def decompress(compressed_lst):
    """
    decompress() takes a list of integers and decompresses it using the LZW
    algorithm. Returns the decompressed string.
    @params: compressed string (list of ints).
    @return: decompressed string.
    """
    if compressed_lst == []:
        return ''
    elif type(compressed_lst) != list:
        printError(1)
    # We start by reconstructing the dictionary we used to compress the
    # string. However, now the keys are the integers and the values are the
    # strings.
    table = {}
    for i in range(256):
        table[i] = chr(i)

    prev = str(chr(compressed_lst[0]))
    compressed_lst = compressed_lst[1:]
    decompressed_str = prev
    # Loops over element in the compressed list so that we can decompress it.
    # If an element does not exist in our table it must be premature and
    # hence, the list we were given is invalid --> error.
    # If an element is in the list we retrieve it and add it to our solution.
    # And then make sure to add a new value to our table, which is the
    # previous element plus the first letter of the current string.
    for element in compressed_lst:
        if element == len(table):
            # print prev # For testing purposes.
            string = prev + prev
        elif element not in table:
            printError(1)
        else:
            string = table[element]

        decompressed_str += string

        # Constructs new values to add to our table by taking the previous
        # string and adding the first letter of the current string to it.
        table[len(table)] = prev + string[0]

        prev = string

    return decompressed_str
