# Input: 5

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

def printSquare(N):
        for i in range (1,N+1):
            print('* ' * i)

if __name__ == "__main__":
    printSquare(1)