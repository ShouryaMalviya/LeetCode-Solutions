class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = []
        
        # Simulate 32-bit two's complement for negative numbers
        num &= 0xFFFFFFFF
        
        while num > 0:
            # Extract the last 4 bits and map to hex character
            result.append(hex_chars[num & 15])
            # Shift right by 4 bits
            num >>= 4
            
        return "".join(result[::-1])