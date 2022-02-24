class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Let the numbers be x,y,z,.....
		# require sum should be 3x+3y+3z
		# original sum = 3x+3y+z
		# Subtract require sum from original sum
		# (3x+3y+3z) - (3x+3y+z) = 2z
		# div the ans by 2 = 2z/2 = z--> our ans

		# return (3 * sum(set(nums)) - sum(nums)) // 24
        
        
        # for i in nums:
        #     if nums.count(i)==1:
        #         return i
        one, two, three = 0, 0, 0
        for num in nums:
		
            two |= (one & num) # this bit show up once previosuly, and recorded in one time, and second time in  num
            one ^= num
            
            three = two & one # show up both in one time & two time
            
            # reset twos if this bit show up three times total
            two = two & (~three)
            one = one & (~three)
        
        return one
        
        