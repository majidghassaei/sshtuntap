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
    return shell(f'ip route replace {hostaddr} via {gateway}', check=check)


def deleteroute(hostaddr, gateway):
    return shell(f'ip route del {hostaddr} via {gateway}', check=False)


def addtuntap(ifname, localuser):
    return shell(f'ip tuntap add mode tun dev {ifname} user ' \
          f'{localuser} group {localuser}')


def addip(ifname, clientaddr, netmask, serveraddr):
    return shell(
               f'ip address add dev {ifname} {clientaddr}/{netmask} ' \
               f'peer {serveraddr}/{netmask}'
           )


def setlink(ifname):
    return shell(f'ip link set up dev {ifname}')


def deletetuntap(ifname):
    return shell(f'ip tuntap delete mode tun dev {ifname}', check=False)

