#! /usr/bin/python
#
#
opened = False
while not opened :
    filename = raw_input("Enter the filename ")
    try :
        f=file(filename,"r")
    except IOError:
        print "Unable to open "+filename
        opened = False
    else :
        opened = True
print "opened file "+filename+"for reading"

for line in f :
    try :
        a_float_num = float(line)
        print "Read %g" % a_float_num
    except ValueError, e:
        print "Read something that wasn't a floating point number\n%s" % e
    except IOError:
        print "An I/O error occurred - continuing"

f.close()

