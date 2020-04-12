class Solution:
    def longestPalindrome(self, s: str) -> int:
        # First-pass attempt:

        # Observation:
        # The length of a palindrome = 2d + 1r, where d is the number of duplicates, and
        # r is 1 or 0, indicates if there are characters other than duplicates.

        # Approach:
        # For each set of characters, count the number of duplicates.
        # If there are any remaining singlular characters, then the number of pairs + 1 is the longest palindrome
        # If there are not any remaining singlular characters, then the number of pairs is the longest palindrome
        charset = {}
        longest = 0
        # O(n)
        for i in s:
            if i not in charset:
                charset[i] = 1
            else:
                charset[i] += 1

        # Less than O(n)
        for k in charset.keys():
            while charset[k] > 1:
                longest += 2
                charset[k] -= 2

        # O(1) best, O(n) worst
        for v in charset.values():
            if v > 0:
                longest += 1
                break

        return longest
