class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for strings in logs:
            if strings=="./":
                print("came inside the ./ and level is at ",level)
                pass
            elif strings=="../":
                if level > 0:
                    level = level-1
                print("came inside the ../ and level is at ",level)
            else:
                level = level + 1
                print("came inside the some thing and level is at ",level)
            print("---------------------------------------------------")

        print(level)
        return level