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

def person_from_record(record, date_sep):
    return Person(record.last, record.first,
                  parse_gender(record.gender),
                  date_from_mdy(record.dob.split(date_sep)),
                  record.fav_color)

def people_from_file(file_name, sep, record_type, date_sep):
    people = []
    with open(file_name, "r") as f:
        for line in f:
            parts = [s.strip() for s in line.split(sep)]
            record = record_type(*parts)
            people.append(person_from_record(record, date_sep))
    return people

def load_all_files():
    people = []
    people.extend(people_from_file("input_files/comma.txt",
                                   ',', CSVRecord, '/'))
    people.extend(people_from_file("input_files/pipe.txt",
                                   '|', PipeRecord, '-'))
    people.extend(people_from_file("input_files/space.txt",
                                   ' ', SpaceRecord, '-'))
    return people

def make_sorted_output(people):
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

def do_it():
    people = load_all_files()
    return make_sorted_output(people)

if __name__ == '__main__':
    for line in do_it():
        print line
