def bidirectional_flights(flights):
    seen = set()
    for src in range(len(flights)):
        for dest in flights[src]:
            if src not in flights[dest]:
                return False
    return True
            


    

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))