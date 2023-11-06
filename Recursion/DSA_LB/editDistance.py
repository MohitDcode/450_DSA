'''
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''

def editDistance(word1, word2, i, j):
    # base case
    if i >=len(word1):
        # means word1 has iterated
        # and len(word1) < len(word2)
        return len(word2) - j
    
    if j >=len(word2):
        # means word2 has iterated
        # and len(word2) < len(word1)
        return len(word1) - i
    
    # processing
    ans = 0

    # case 1: Characters match
    if word1[i] == word2[j]:
        ans = 0 + editDistance(word1, word2, i+1, j+1)

    # case 2: Characters don't match
    else:
        ans = min (
        # perform the actions
        # 1) Insert
        1 + editDistance(word1, word2, i, j+1),
        # 2) Remove
        1 + editDistance(word1, word2, i+1, j),
        # 3) Replace
        1 + editDistance(word1, word2, i+1, j+1)
        )
    return ans

if __name__ == "__main__":
    word1 = 'horse'
    word2 = 'ros'
    print(editDistance(word1, word2, 0, 0))