class TimeMap:

    def __init__(self):
        self.hmtime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmtime:
            self.hmtime[key] = [(timestamp, value)]
        else:
            self.hmtime[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        if key not in self.hmtime:
            return ""
        r = len(self.hmtime[key]) - 1
        res = ""
        while l <= r:
            mid = l + (r-l)//2
            t = self.hmtime[key][mid][0]
            if t < timestamp:
                res = self.hmtime[key][mid][1]
                l = mid + 1
            elif t == timestamp:
                return self.hmtime[key][mid][1]
            else:
                r = mid - 1
        return res
        
