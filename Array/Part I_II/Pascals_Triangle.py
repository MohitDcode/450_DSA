def usingRecursion(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]

    prevRows = usingRecursion(numRows - 1)
    newRow = [1] * numRows

    for i in range(1, numRows-1):
        newRow[i] = prevRows[-1][i-1] + prevRows[-1][i]
    
    prevRows.append(newRow)
    return prevRows

def usingCombinatorialFormula(numRows):
        result = []
        if numRows == 0:
            return result
        first_row = [1]
        result.append(first_row)

        for i in range(1, numRows):
            prev_row = result[i - 1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            result.append(current_row)

        return result

def usingDynamicProgramming(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    
    prevRows = usingDynamicProgramming(numRows-1)
    prevRow = prevRows[-1]
    currentRow = [1]

    for i in range(1, numRows-1):
        currentRow.append(prevRow[i-1] + prevRow[i])
    currentRow.append(1)
    prevRows.append(currentRow)

    return(prevRows)

if __name__ == "__main__":
    match input("Select 1 for Recursion, 2 for Combinatorial Formula, 3 for Dynamic Programming : "):
        case '1':
            print(usingRecursion(5))
        case '2':
            print(usingCombinatorialFormula(5))
        case '3':
            print(usingDynamicProgramming(5))