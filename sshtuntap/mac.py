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


def replaceroute(gateway, hostaddr='default', check=True):
#Equivalent in mac ==  return shell(f'ip route replace {hostaddr} via {gateway}', check=check)
    pass


def deleteroute(hostaddr, gateway):
#Equivalent in mac ==  return shell(f'ip route del {hostaddr} via {gateway}', check=False)
    pass


def addtuntap(ifname, localuser):
#Equivalent in mac ==  return shell(f'ip tuntap add mode tun dev {ifname} user ' \
#          f'{localuser} group {localuser}')
    pass


def addip(ifname, clientaddr, netmask, serveraddr):
#Equivalent in mac ==  return shell(
#               f'ip address add dev {ifname} {clientaddr}/{netmask} ' \
#               f'peer {serveraddr}/{netmask}'
#           )
    pass


def setlink(ifname):
#Equivalent in mac ==    return shell(f'ip link set up dev {ifname}')
    pass


def deletetuntap(ifname):
#Equivalent in mac ==  return shell(f'ip tuntap delete mode tun dev {ifname}', check=False)
    pass

