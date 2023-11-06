def swap(string):
      return string[-1:] + string[1:-1] + string[:1]
def printPermutation(string, index):
    # base case
    if index >= len(string):
        print("".join(string))
    
    # processing
    for j in range(index, len(string)):
        words = [c for c in string]
        words[j], words[index] = words[index], words[j]

    # recursive call
        printPermutation(words, index + 1)

if __name__ == '__main__':
    string = 'abc'
    printPermutation(string, 0)