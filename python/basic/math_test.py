import math

print (math.pi)

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

# print_lyrics()

def do_twice(f):
    f()
    f()

do_twice(print_lyrics)