class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        count_diff = 0
        seen = []
        
        for word in words:
            morse = ''
            for c in word:
                idx = ord(c)-ord('a')
                morse = morse + morse_code[idx]
            seen.append(morse)
        return len(set(seen))