class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        times = []
        for pos, spd in pairs:
            time = (target - pos)/spd
            if not times or time > times[-1]:
                times.append(time)

        return len(times)

