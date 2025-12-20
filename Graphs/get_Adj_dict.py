from collections import defaultdict

def get_adj_dict(flights):
    """
    create a dict. At each pair add the destination to the source dict
    and source to the dest, using defaultdict for cleaner code
    """
    adj_dict = defaultdict(list)
    for source, dest in flights:   # tuple unpacking
        adj_dict[source].append(dest)
        adj_dict[dest].append(source)
    return dict(adj_dict)  # convert back to normal dict if you like

flights = [
    ['Cape Town', 'Addis Ababa'],
    ['Cairo', 'Lagos'],
    ['Lagos', 'Addis Ababa'],
    ['Nairobi', 'Cairo'],
    ['Cairo', 'Cape Town']
]

print(get_adj_dict(flights))
