class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow_dict = collections.defaultdict(int)
  
        for i in allowed:
            allow_dict[i]+=1

        count = 0
        for word in words:
            d = collections.defaultdict(int)
            for i in word:
                d[i]+=1
            
            # check if valid
            if set(allow_dict.keys()).issuperset(d.keys()):
                count+=1
          

        return count
