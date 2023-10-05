# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge(intervals):
    START, END = 0, 1
    result = []
    
    # make all intervals sorted on (left endpoint, right endpoint) pair in ascending order
    intervals.sort( key = lambda x: (x[START], x[END] ) ) 
    for interval in intervals:
        if not result or ( result[-1][END] < interval[START] ):
            # no overlapping
            result.append( interval )
        else:
            # has overlapping
            # merge with previous interval
            result[-1][END] = max(result[-1][END], interval[END])
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))