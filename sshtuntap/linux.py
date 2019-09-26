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
    shell(f'ip route replace {hostaddr} via {gateway}', check=check)
    pass


def deleteroute(hostaddr, gateway):
    shell(f'ip route del {hostaddr} via {gateway}', check=False)
    pass


def addtuntap(ifname, localuser):
    shell(f'ip tuntap add mode tun dev {ifname} user ' \
          f'{localuser} group {localuser}')
    pass


def addip(ifname, clientaddr, netmask, serveraddr):
    shell(
        f'ip address add dev {ifname} {clientaddr}/{netmask} ' \
        f'peer {serveraddr}/{netmask}'
    )
    pass


def setlink(ifname):
    shell(f'ip link set up dev {ifname}')
    pass


def deletetuntap(ifname):
    shell(f'ip tuntap delete mode tun dev {ifname}', check=False)
    pass

