import sys


def caesar(shiftVal, inputFileName, outputFileName):
    fin = open(inputFileName)
    text = fin.read()
    fin.close()

    output = ""
    for char in text:
        if char.isalpha():
            if (char.isupper()):
                output += chr((ord(char) + shiftVal - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                output += chr((ord(char) + shiftVal - 97) % 26 + 97)
        else:
            output += char

    fout = open(outputFileName, "w+")
    fout.write(output)
    fout.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Wrong number of arguments!')
    else:
        shiftVal = int(sys.argv[1])
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        caesar(shiftVal, inputFileName, outputFileName)
