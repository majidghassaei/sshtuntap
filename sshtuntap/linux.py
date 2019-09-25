import pwd
import subprocess as sp


def userexists(name):
    try:
        return pwd.getpwnam(name)
    except KeyError:
        return False


def shell(cmd, check=True):
    print(f'Shell: {cmd}')
    return sp.run(cmd, shell=True, check=check)  #, stdout=sp.PIPE, stderr=sp.PIPE)


def addroute(*args, **kwargs):
    #To be implemented
    pass


def replaceroute(*args, **kwargs):
    #To be implemented
    pass


def ssh(*args, **kwargs):
    #To be implemented
    pass


def deleteroute(*args, **kwargs):
    #To be implemented
    pass


def addtuntap(*args, **kwargs):
    #To be implemented
    pass


def addip(*args, **kwargs):
    #To be implemented
    pass


def setlink(*args, **kwargs):
    #To be implemented
    pass


def deletetuntap(*args, **kwargs):
    #To be implemented
    pass



