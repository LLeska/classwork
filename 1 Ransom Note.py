class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in ransomNote:
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True
