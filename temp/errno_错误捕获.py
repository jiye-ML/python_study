import errno
try:
    fp = open("no.such.file")
except IOError as error:
    print(error.strerror)
    if error == errno.ENOENT:
        print("no such file")
    elif error == errno.EPERM:
        print("permission denied")
    else:
        print(error.strerror)