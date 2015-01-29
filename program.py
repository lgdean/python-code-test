import datetime

def stringify_person(p_tuple):
    hack_tuple = (p_tuple[0], p_tuple[1], p_tuple[2],
                 "{dt.month}/{dt.day}/{dt.year}".format(dt=p_tuple[3]),
                 p_tuple[4])
    return " ".join(map(str, hack_tuple)) # last first gender dob color

def date_from_mdy(strs):
    ints = map(int, strs)
    return datetime.date(ints[2], ints[0], ints[1])

def do_it():
    people = []
    with open("input_files/comma.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(',')] # hm, prefer map?
            people.append((parts[0], parts[1], parts[2],
                           date_from_mdy(parts[4].split('/')), parts[3]))
    with open("input_files/pipe.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split('|')] # hm, prefer map?
            people.append((parts[0], parts[1],
                           "Female" if parts[3][0] == "F" else "Male",
                           date_from_mdy(parts[5].split('-')), parts[4]))
    with open("input_files/space.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(' ')] # hm, prefer map?
            people.append((parts[0], parts[1],
                           "Female" if parts[3][0] == "F" else "Male",
                           date_from_mdy(parts[4].split('-')), parts[5]))
    sorts = [
        {'key': lambda p: (p[2],p[0])},
        {'key': lambda p: p[3]},
        {'key': lambda p: p[0], 'reverse': True}
    ]
    output = []
    for idx,sorter in enumerate(sorts):
        output.append("Output %d:"%(idx+1))
        sorted_people = sorted(people, **sorter)
        output.extend(map(stringify_person, sorted_people))
        output.append("")
    return output

if __name__ == '__main__':
    for line in do_it():
        print line
