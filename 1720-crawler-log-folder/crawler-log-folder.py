class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for strings in logs:
            if strings=="./":
                pass
            elif strings=="../":
                if level > 0:
                    level = level-1
            else:
                level = level + 1
        return level