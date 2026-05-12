class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # add everything to a set
        available_numbers = set()
        for num in nums:
            available_numbers.add(num)
        
        # go through set to find longest sequence
        # {3 5 7 2 1 12}
        longest_stretch = 0
        for entry in available_numbers:
            seq_iterator = entry
            length_stretch = 1
            while seq_iterator - 1 in available_numbers:
                length_stretch += 1
                seq_iterator -= 1
            longest_stretch = max(longest_stretch, length_stretch)
        return longest_stretch
            

        
        