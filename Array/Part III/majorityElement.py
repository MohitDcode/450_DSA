# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(nums):
        # Create a Counter to store the count of each element
        element_count = {}
        for i in range(len(nums)):
            if (nums[i] in element_count):
                element_count[nums[i]] += 1
            else:
                element_count[nums[i]] = 1

        majority_elements = []
        threshold = len(nums) // 3

        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements[0]


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))