from collections import defaultdict

def solution(flights, origin):
    flight_map = defaultdict(list)
    for src, dst in flights:
        flight_map[src].append(dst)

    def _solution(flights_len, origin, res):
        if len(res) == flights_len + 1:
            return [res[:]]
        if origin not in flight_map:
            return []
        all_res = []
        for i, dst in enumerate(flight_map[origin]):
            res.append(dst)
            flight_map[origin].pop(i)
            all_res.extend(_solution(flights_len, dst, res))
            flight_map[origin].insert(i, dst)
            res.pop()
        return all_res

    res = _solution(len(flights), origin, [origin])
    if res:
        return sorted(res)[0]
