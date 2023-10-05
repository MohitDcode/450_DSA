# Input: nums = [3,1,3,4,2]
# Output: 3
def usingSortingMethod(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
    return -1

def usingMapMethod(nums):
    numCount = {}

    for num in nums:
        if num in numCount:
            return num
        numCount[num] = 1
    return -1
def usingLinkedListCycleMethod(nums): # Also known as Floyds Cycle Detection
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: Find enterance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow # or fast, as they both point to the entrance of the cycle

def FloydsCycleDetection(nums):
    return(usingLinkedListCycleMethod(nums))

if __name__ == "__main__":
    nums = [3,1,3,4,2]
    match input("Select 1 for Sorting Method, 2 for Map Method, 3 for Linked-List Cycle Method, 4 for Floyds Cycle Detection : "):
        case '1':
            print(usingSortingMethod(nums))
        case '2':
            print(usingMapMethod(nums))
        case '3':
            print(usingLinkedListCycleMethod(nums))
        case '4':
            print(FloydsCycleDetection(nums))