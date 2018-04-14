from errors import printError

def compress(text):
    """
    compress() takes a string and compresses it using the LZW algorithm.
    Returns the compressed string in the form of a list of integers.
    @params: string to be compressed.
    @return: compressed string (list of ints).
    """
    text = text.decode("utf-8")
    if text == '':
        return []
    elif type(text) != str:
        printError(2)

    # Creates a list that will hold the integers after compression of the
    # string.
    compressed_lst = []

    # Makes the dictionary to hold our values we map to.
    table = {}
    for i in range(256):
        table[chr(i)] = i


    value = ''
    index = 0
    # Loop over each individual character in the text and keep track of where
    # in the string you are (using the value index). Value keeps track of the
    # longest substring you have seen that is in your table.
    for char in text:

        # Add the latest character to our substring.
        total = value + char
        index += 1
        # If we have seen total before we want to make it our value (aka we
        # want to remember it) and move on to the next character. However,
        # we also need to check if we have reached the end of the string. If
        # we have reached the end, we add the total to our compressed list.
        if total in table:
            value = total

        # However, if we have not seen total before, we add value (the
        # substring we had remembered) to the ditionary and we add total
        # to the dictionary (because we have not seen it before). We then
        # move on to remembering the most recent character.
        else:
            compressed_lst.append(table[value])
            table[total] = len(table)
            value = char

        if index == len(text):
            compressed_lst.append(table[value])
            # print(total) # For testing purposes.

    compressed_str = ''
    for num in compressed_lst:
        # print num
        # print str(num)
        compressed_str += ' ' + str(num)
    # print compressed_str

    return compressed_str.strip() ,len(table)
