def getMinMax(a):
    max, min = a[0], a[0]

    for i in range(len(a)):
        if a[i]>max:
            max = a[i]
        if a[i]<min:
            min = a[i]
    return min, max

if __name__ == "__main__":
    a = [3, 2, 1, 56, 10000, 167]
    print(getMinMax(a))