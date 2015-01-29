import sys
import datetime
import operator

def stringifyPerson(pTuple):
    hackTuple = (pTuple[0], pTuple[1], pTuple[2],
                 "{dt.month}/{dt.day}/{dt.year}".format(dt=pTuple[3]),
                 pTuple[4])
    return " ".join(map(str, hackTuple)) # last first gender dob color

def dateFromMDY(strs):
    ints = map(int, strs)
    return datetime.date(ints[2], ints[0], ints[1])

def do_it():
    people = []
    with open("input_files/comma.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(',')] # hm, prefer map?
            people.append((parts[0], parts[1], parts[2],
                           dateFromMDY(parts[4].split('/')), parts[3]))
    with open("input_files/pipe.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split('|')] # hm, prefer map?
            people.append((parts[0], parts[1],
                           "Female" if parts[3][0] == "F" else "Male",
                           dateFromMDY(parts[5].split('-')), parts[4]))
    with open("input_files/space.txt","r") as f:
        for line in f:
            parts = [l.strip() for l in line.split(' ')] # hm, prefer map?
            people.append((parts[0], parts[1],
                           "Female" if parts[3][0] == "F" else "Male",
                           dateFromMDY(parts[4].split('-')), parts[5]))
    sorts = [
        {'key': lambda p: (p[2],p[0])},
        {'key': lambda p: p[3]},
        {'key': lambda p: p[0], 'reverse': True}
    ]
    output = []
    for idx,sorter in enumerate(sorts):
        output.append("Output %d:"%(idx+1))
        sorted_people = sorted(people, **sorter)
        output.extend(map(stringifyPerson, sorted_people))
        output.append("")
    return output

if __name__ == '__main__':
    for line in do_it():
        print line
