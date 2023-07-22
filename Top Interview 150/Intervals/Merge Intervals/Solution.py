class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i:i[0])
        merged_intervals = [intervals[0]]
        size = len(intervals)

        for i in range(1, size):
            e = merged_intervals[-1][1]
            s = intervals[i][0]

            if s <= e:
                e2 = intervals[i][1]
                merged_intervals[-1][1] = max(e, e2)
            else:
                merged_intervals.append(intervals[i])

        return merged_intervals
