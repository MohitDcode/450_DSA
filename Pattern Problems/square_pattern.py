# Geek is very fond of patterns. Once, his teacher gave him a square pattern to solve. He gave Geek an integer n and asked him to build a pattern.
# Help Geek to build a star pattern.

# Input: 5

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def printSquare(N):
        for i in range (0,N):
            print('* ' * N)

if __name__ == "__main__":
    print(printSquare(5))