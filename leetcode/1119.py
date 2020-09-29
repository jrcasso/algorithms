class Solution:
    def removeVowels(self, S: str) -> str:
        for i in ['a', 'e', 'i', 'o', 'u']:        
            S = S.replace(i, '')
        return S
