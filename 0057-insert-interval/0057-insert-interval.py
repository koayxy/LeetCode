class Solution(object):
    def insert(self, intervals, newInterval):
        merged = []
        start, end = newInterval
        
        for interval in intervals:
            if interval[1] < start:
                merged.append(interval)
            elif interval[0] > end:
                merged.append([start, end])
                start, end = interval
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        
        merged.append([start, end])
        
        return merged