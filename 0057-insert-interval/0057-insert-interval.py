class Solution(object):
    def insert(self, intervals, newInterval):
        # store merged intervals
        merged = []
        # start and end of new interval
        start, end = newInterval
        
        for interval in intervals:
            # if end of current interval is less than start of new interval & no overlaps, add current interval to merged list
            if interval[1] < start:
                merged.append(interval)
            # if start of new interval is greater than end of current interval & no overlaps, add new interval to merged list
            elif interval[0] > end:
                merged.append([start, end])
                start, end = interval
            else: # if there's overlaps, update start and end of new intervals
                start = min(start, interval[0])
                end = max(end, interval[1])
        
        merged.append([start, end])
        
        return merged