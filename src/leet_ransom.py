import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        else:
            for elm in ransomNote:
                if elm in magazine:
                    magazine = magazine.replace(elm, '', 1)
                else:
                    return False
            return True
        
if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct(ransomNote='aac', magazine='caab'))
    print(collections.Counter('aa'))