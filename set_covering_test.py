states_needed = set(["id", "nv", "ut", "wa", "id", "mt", "or", "nv", "ca", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = []

while states_needed:

    best_coverage = set()
    best_station = None
    for station, states in stations.items():
        covered = states & states_needed
        if len(covered) > len(best_coverage):
            best_station = station
            best_coverage = covered
    final_stations.append(best_station)
    states_needed -= best_coverage