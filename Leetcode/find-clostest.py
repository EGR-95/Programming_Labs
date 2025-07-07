class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = nums[0]

        for x in nums:
            if abs(x) < abs(closest) or (abs(x) == abs(closest) and x > closest): 
                closest = x

        return closest

# Get input from user
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, user_input.strip().split()))
    
    sol = Solution()
    result = Solution().findClosestNumber(nums)
    print("Closest number to 0 is:", result)

