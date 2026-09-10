class UndergroundSystem:
    def __init__(self):
        self.checkin = {} # id -> (source, st_time)
        self.between = {} # st -> {end -> (total_time, count)}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkin:
            return

        src_st, st_time = self.checkin[id]
        del self.checkin[id]
        travel_time = t - st_time

        last_time, last_count = 0, 0
        station_map = self.between.get(src_st, {})

        if stationName in station_map:
            last_time, last_count = station_map[stationName]

        station_map[stationName] = [last_time + travel_time, last_count + 1]
        self.between[src_st] = station_map


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_time, travel_count = self.between[startStation][endStation]

        return travel_time / travel_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)