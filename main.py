import sys
import os.path
from errors import printError
from decompression import decompress
from compression import compress
import time
import math

from openpyxl import Workbook

# -------------------------------------
files = [
    {'name': 'rands/rand_10.txt', 'description': 'File The has 10 Random Chars'},
    {'name': 'rands/rand_100.txt', 'description': 'File The has 100 Random chars'},
    {'name': 'rands/rand_1K.txt', 'description': 'File The has 1 Thousand Random chars'},
    {'name': 'rands/rand_10K.txt', 'description': 'File The has 10 Thousand Random chars'},
    {'name': 'rands/rand_100K.txt', 'description': 'File The has 100 Thousand Random chars'},
    {'name': 'rands/rand_1M.txt', 'description': 'File The has 1 Million Random chars'},
    {'name': 'rands/rand_10M.txt', 'description': 'File The has 10 Million Random chars'},
    # {'name': 'rands/rand_100M.txt', 'description': 'File The has 100 Million Random chars'},


    {'name': 'repeated_char/rc_10.txt', 'description': 'File The has 10 Repeated "m"'},
    {'name': 'repeated_char/rc_100.txt', 'description': 'File The has 100 Repeated "m"'},
    {'name': 'repeated_char/rc_1K.txt', 'description': 'File The has 1K Repeated "m"'},
    {'name': 'repeated_char/rc_10K.txt', 'description': 'File The has 10K Repeated "m"'},
    {'name': 'repeated_char/rc_100K.txt', 'description': 'File The has 100K Repeated "m"'},
    {'name': 'repeated_char/rc_1M.txt', 'description': 'File The has 1M Repeated "m"'},
    {'name': 'repeated_char/rc_10M.txt', 'description': 'File The has 10M Repeated "m"'},
    # {'name': 'repeated_char/rc_100M.txt', 'description': 'File The has 100M Repeated "m"'},

    {'name': 'repeated_sentence/rs_10.txt', 'description': 'File The has 1  "Iam Maher "'},
    {'name': 'repeated_sentence/rs_100.txt', 'description': 'File The has 10 Repeated "Iam Maher "'},
    {'name': 'repeated_sentence/rs_1K.txt', 'description': 'File The has 100 Repeated "Iam Maher "'},
    {'name': 'repeated_sentence/rs_10K.txt', 'description': 'File The has 1K Repeated "Iam Maher "'},
    {'name': 'repeated_sentence/rs_100K.txt', 'description': 'File The has 10K Repeated "Iam Maher "'},
    {'name': 'repeated_sentence/rs_1M.txt', 'description': 'File The has 100K Repeated "Iam Maher "'},
    {'name': 'repeated_sentence/rs_10M.txt', 'description': 'File The has 1M Repeated "Iam Maher "'},
    # {'name': 'repeated_sentence/rs_100M.txt', 'description': 'File The has 10M Repeated "Iam Maher "'},

]

inputFilesPrefix = 'input_files/'
outputFilePrefix = 'output_files/'
opComporess = 1  # 1 is compression, 0 is decompression

wb = Workbook()
ws = wb.active


# -------------------------------------



def main():
    # grab the active worksheet
    ws.append(['File Name', 'input File Size', 'Output File Size', 'CR', 'Bits for table', 'Execution', 'Description'])

    for fileObject in files:
        start_time = time.time()

        if opComporess == 0:
            operation = 'decompress'
            # TODO check ele eshe
        elif opComporess == 1:
            operation = 'compress'
            inputFileName = inputFilesPrefix + fileObject['name']
            outputFileName = outputFilePrefix + fileObject['name']
        else:
            sys.exit('INVALID OPERATION')
        if operation == 'compress':
            # Call compress() on the given file.
            try:
                f = open(inputFileName, 'rb')

                comp, tableLength = compress(f.read())
                comp = ''.join(comp)
                f.close()

                f_comp = open(outputFileName, 'w')
                f_comp.write(comp)
                f_comp.close()

            except Exception:
                # print e
                printError(0)
        elif operation == 'decompress':
            # Call decompress() on the given file.

            try:
                # comp = pickle.load(open(sys.argv[1], 'rb'))
                comp_str_list = open(inputFileName, 'rb').read().split()

                comp_int_lst = []
                for num in comp_str_list:
                    comp_int_lst.append(int(num))

                decomp = decompress(comp_int_lst)

                f = open(outputFileName, 'w')
                f.write(decomp)
                f.close()

            except Exception:
                # print e
                printError(1)
        else:
            printError(0)

        end_time = time.time()
        fileExecutionTime = end_time - start_time
        printSummary(inputFileName, outputFileName, fileExecutionTime, fileObject, tableLength)

    wb.save("report.xlsx")


def printSummary(file1, file2, fileExecutionTime, fileObject, tableLength):
    """
    printSummary() prints out the number of bytes in the original file and in
    the result file.
    @params: two input_files that are to be checked.
    @return: n/a.
    """
    # Checks if the input_files exist in the current directory.


    if (not os.path.isfile(file1)) or (not os.path.isfile(file2)):
        printError(0)

    bitOfCharInTable = math.ceil(math.log(tableLength, 2))
    # Finds out how many bytes in each file.
    file2 = open(file2, "r", encoding="utf-8-sig")
    f1_bytes = os.path.getsize(file1)
    f2_bytes = (len(file2.read().split()) * bitOfCharInTable) / 8
    CR = f1_bytes / f2_bytes
    file2.close()

    print('File Name: ' + fileObject['name'])
    print('Description: ' + fileObject['description'])
    print('input File Size' ': ' + str(f1_bytes) + ' bytes')
    print('output File Size' + ': ' + str(f2_bytes) + ' bytes')
    print('--- Compression Ratio: ', CR, ' ---')
    print('--- Number Of bits for Char', bitOfCharInTable, '---')
    print("--- Execution Time (seconds):  %s ---" % fileExecutionTime)
    print('================================================================================')

    # ws.append(['File Name', 'input File Size', 'Output File Size', 'CR', 'Bits for table', 'Execution', 'Description'])
    ws.append([fileObject['name'], str(f1_bytes), str(f2_bytes), CR, bitOfCharInTable, fileExecutionTime,
               fileObject['description']])


if __name__ == '__main__':
    main()
