import string
import sys
import hashlib

allStrings = []

def stringGenerator(currentString):
    if len(currentString) == 6:
        allStrings.append(currentString)
        return

    for c in string.ascii_lowercase:
        stringGenerator(currentString + c)

def generateSha(plainText):
    return hashlib.sha256(plainText.encode("ascii")).hexdigest()

def main():
    shaString = sys.argv[2]
    stringGenerator(sys.argv[1])
    # print("first string: " + )
    for plainText in allStrings:
        hexShaString = generateSha(plainText)
        # print("given: ", shaString, "\ngenerated: ", hexShaString)
        if hexShaString == shaString:
            return plainText
            
    return "No match!"

if __name__ == "__main__":
    print(main())
