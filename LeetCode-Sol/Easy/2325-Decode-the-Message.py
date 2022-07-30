class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        # save to dict
        seen = set()
        seen.add(' ')
        idx=0
        for i in range(len(key)):
            ch = key[i]
            if ch not in seen:
                d[ch] = chr(idx+97)
                idx+=1
                seen.add(ch)

        ret = []
        for ch in message:
            if ch==' ':
              ret.append(' ')
            else:
              val = d[ch]
              ret.append(val)
    
        return ''.join(ret)

# weekly contest 300