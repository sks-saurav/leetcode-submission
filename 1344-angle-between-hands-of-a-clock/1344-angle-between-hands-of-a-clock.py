class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0

        curr_hour =  60 * hour + minutes
        h_angle = (curr_hour / 720) * 360

        curr_min = minutes
        m_angle = (curr_min / 60) * 360

        angle_between = abs(h_angle - m_angle)

        return min(angle_between, 360 - angle_between)


