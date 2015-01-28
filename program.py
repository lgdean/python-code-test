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

class Program:
    def doit(self): # haha, guess who's secretly a java programmer
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
        output = []
        output.append("Output 1:")
        order1 = sorted(people, key=operator.itemgetter(0))
        order1.sort(key=operator.itemgetter(2))
        output.extend(map(stringifyPerson, order1))
        output.append("")
        output.append("Output 2:")
        order2 = sorted(people, key=operator.itemgetter(3))
        output.extend(map(stringifyPerson, order2))
        output.append("")
        output.append("Output 3:")
        order3 = sorted(people, key=operator.itemgetter(0), reverse=True)
        output.extend(map(stringifyPerson, order3))
        output.append("")
        return output

if __name__ == '__main__':
    for line in Program().doit():
        print line
