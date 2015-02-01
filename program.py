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
    month, day, year = map(int, strs)
    return datetime.date(year, month, day)

def parse_gender(s):
    s = s.capitalize()
    if s == "F": return "Female"
    if s == "M": return "Male"
    return s

# everything is a nail!
CSVRecord = namedtuple('CSVRecord',
                       ['last', 'first', 'gender', 'fav_color', 'dob'])
PipeRecord = namedtuple('PipeRecord',
                        ['last', 'first', 'm', 'gender', 'fav_color', 'dob'])
SpaceRecord = namedtuple('SpaceRecord',
                         ['last', 'first', 'm', 'gender', 'dob', 'fav_color'])

def do_it():
    people = []
    with open("input_files/comma.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(',')] # hm, prefer map?
            record = CSVRecord(*parts)
            people.append(Person(record.last, record.first,
                                 parse_gender(record.gender),
                                 date_from_mdy(record.dob.split('/')),
                                 record.fav_color))
    with open("input_files/pipe.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split('|')] # hm, prefer map?
            record = PipeRecord(*parts)
            people.append(Person(record.last, record.first,
                                 parse_gender(record.gender),
                                 date_from_mdy(record.dob.split('-')),
                                 record.fav_color))
    with open("input_files/space.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(' ')] # hm, prefer map?
            record = SpaceRecord(*parts)
            people.append(Person(record.last, record.first,
                                 parse_gender(record.gender),
                                 date_from_mdy(record.dob.split('-')),
                                 record.fav_color))
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
