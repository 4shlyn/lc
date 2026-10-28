
class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.cache:
            self.cache[key][0].append(timestamp)
            self.cache[key][1].append(value)
        else:
            self.cache[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""

        i = 0
        j = len(self.cache[key][0]) - 1
        result = ""

        while i <= j:
            m = (i + j) // 2
            c = self.cache[key][0][m]

            if c == timestamp:
                return self.cache[key][1][m]
            elif c < timestamp:
                result = self.cache[key][1][m]
                i = m + 1
            else:
                j = m - 1

        return result
