'''xargs act like as touple'''
def self(*details):
    print(details[0])
def self2(*details):
    print(details)


self("Anik Sen", "CSE", 22)
self2("Anik Sen", "CSE", 22)  #return as like touple


def add(*num):
    sum = 0
    for i in num:
        sum= sum + i
    print(sum)

add(12,34,12,53)

'''xxargs act like as dictionary'''
def student(**details):
    print(details)
    print(details["name"])

student(name="Anik Sen",age=22)  #return as like dictionary
