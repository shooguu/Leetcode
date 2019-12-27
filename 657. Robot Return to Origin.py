class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for item in moves:
            if item == 'U':
                y += 1
            elif item == 'D':
                y -= 1
            elif item == 'R':
                x += 1
            else:
                x -= 1
        return x == 0 and y == 0
