# Input: 5

# Output:
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def printSquare(N):
        for i in range (1,N+1):
            for j in range(1, i+1):
                print(j, end='')
            print()

if __name__ == "__main__":
    printSquare(5)