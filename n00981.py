from datetime import datetime
import collections


class TimeMap:

    def __init__(self):
        self.vals = {{}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals.keys():

    def get(self, key: str, timestamp: int) -> str:


if __name__ == "__main__":
    start_time = datetime.now()
    sol = Solution()

    print(sol.updateMatrix())
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))