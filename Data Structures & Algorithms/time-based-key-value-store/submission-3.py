class TimeMap:

    def __init__(self):
        self.c_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.c_map:
            self.c_map[key] = []
        self.c_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.c_map:
            tmp_map = self.c_map[key]
            if timestamp >= tmp_map[-1][1]:
                return tmp_map[-1][0]
            else:
                l = 0
                r = len(tmp_map) - 1
                next_least = ""

                while l <= r:
                    m = (l+r)//2

                    if tmp_map[m][1]<timestamp:
                        l = m + 1
                        next_least = tmp_map[m][0]
                    elif tmp_map[m][1]>timestamp:
                        r = m - 1
                    else:
                        return tmp_map[m][0]
                return next_least
        else:
            return ""