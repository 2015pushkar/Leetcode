def get_direct_flights(flights, source):
    res = []
    for i in range(len(flights[source])):
        if flights[source][i] == 1:
            res.append(i)
    return res


flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))