import datetime
from collections import namedtuple

# Cool feature, but I might not want to expose the tuple-ness (and the
# order of fields) in the real world. But I do like the immutability!
Person = namedtuple('Person', ['last', 'first', 'gender', 'dob', 'fav_color'])

def stringify_person(p):
    hack_tuple = (p.last, p.first, p.gender,
                  "{dt.month}/{dt.day}/{dt.year}".format(dt=p.dob),
                  p.fav_color)
    return " ".join(map(str, hack_tuple)) # last first gender dob color

def date_from_mdy(strs):
    ints = map(int, strs)
    return datetime.date(ints[2], ints[0], ints[1])

def parse_gender(s):
    return "Female" if s == "F" else "Male"

def do_it():
    people = []
    with open("input_files/comma.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(',')] # hm, prefer map?
            people.append(Person(parts[0], parts[1], parts[2],
                                 date_from_mdy(parts[4].split('/')), parts[3]))
    with open("input_files/pipe.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split('|')] # hm, prefer map?
            people.append(Person(parts[0], parts[1],
                                 parse_gender(parts[3][0]),
                                 date_from_mdy(parts[5].split('-')), parts[4]))
    with open("input_files/space.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(' ')] # hm, prefer map?
            people.append(Person(parts[0], parts[1],
                                 parse_gender(parts[3][0]),
                                 date_from_mdy(parts[4].split('-')), parts[5]))
    sorts = [
        {'key': lambda p: (p.gender,p.last)},
        {'key': lambda p: p.dob},
        {'key': lambda p: p.last, 'reverse': True}
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
