class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            # Create a row of length i + 1 filled with 1s
            row = [1] * (i + 1)
            # Calculate intermediate values using the previous row
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res