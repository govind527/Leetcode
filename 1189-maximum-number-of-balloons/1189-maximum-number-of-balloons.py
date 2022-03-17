class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #Solution explained:

# 1. we could use an integer array to count the frequency of each character in the given text string;
# 2. after building the frequency array, we could just find the minimum one of the five characters and return
        
        counter = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for char in text:
            if char in counter:
                counter[char] += 1
        counter["l"] //= 2
        counter["o"] //= 2
        return min(counter.values())