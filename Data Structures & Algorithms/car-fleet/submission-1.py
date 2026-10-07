class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # times = []
        # for i, car in enumerate(position):
        #     times.append((target-car)/speed[i])
        # return len(set(times))

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            stack.append((target-p)/s)

            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)