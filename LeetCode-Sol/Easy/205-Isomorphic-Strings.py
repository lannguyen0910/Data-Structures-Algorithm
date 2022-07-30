class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for s_, t_ in zip(s, t):
            if (s_ not in list(d.keys())) and (t_ not in list(d.values())):
                d[s_] = t_
            else:
                val = d.get(s_)
                if val != t_:
                    return False
        return True
