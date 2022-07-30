# Fast way
class Solution:
    def defangIPaddr(self, address: str) -> str:
        if not address:
            return ''
        
        return address.replace('.', '[.]')


# Slower way:
class Solution:
    def defangIPaddr(self, address: str) -> str:
        if not address:
            return ''
        
        arr = address.split('.')
        return '[.]'.join(arr)