import json




def main():
    rawRequiredStationList = input()
    stationCount = int(input())
    stationNeeded = json.loads(rawRequiredStationList)
    stationNeeded = set(stationNeeded)

    stationAvailable = {}

    for i in range(stationCount):
        stationInfo = json.loads(input())
        stationAvailable[stationInfo['Name']] = set(stationInfo['Cities'])

    final_stations = []

    while stationNeeded:
        best_station = None
        states_covered = set()

        for station, cities in stationAvailable.items():
            covered = stationNeeded & cities 
            
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        if best_station is None:
            break
        stationNeeded -= states_covered
        final_stations.append(best_station)

    print(f"{sorted(final_stations)}")


main()