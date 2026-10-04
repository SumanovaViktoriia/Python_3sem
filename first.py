class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = {}
        
        for ch in magazine:
            available[ch] = available.get(ch, 0) + 1
        
        for ch in ransomNote:
            if available.get(ch, 0) == 0:
                return False
            available[ch] -= 1
        
        return True