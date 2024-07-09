class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = []
        totaltime=0
        for arrival,time in customers:
            if totaltime < arrival:
                totaltime = time + arrival
            else:
                totaltime = totaltime+time
            waiting.append(totaltime-arrival)
        result = sum(waiting) / len(waiting)
        result = round(result, 5)
        print(result)

        return result