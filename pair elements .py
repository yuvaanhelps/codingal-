# create a class
class Pair_elements:
    def  twosum(self,nums, target):
        # create an empty dictionary
        lookup ={}
        # iterate the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
# take input of sum from user
value = int(input("enter the sum for which you want to make this search: "))
print("index 1=%d, index 2=%d" % Pair_elements().twosum((10, 20, 30, 40, 50, 60, 70), value))