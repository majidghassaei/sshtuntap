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
    shell(f'ip route replace {hostaddr} via {gateway}')
    shell(f'ip route replace default via {serveraddr}')
    shell(
        f'sudo -u {localuser} ssh {remoteuser}@{hostname} ' \
        f'-Nw {index}:{index} {" ".join(sshargs)}'
    )

