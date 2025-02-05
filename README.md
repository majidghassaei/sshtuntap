# sshtuntap

Linux TUN/TAP using the `openssh` and `Python3`

This package comes with two command line interfaces:

* ssh-tuntap-server
* ssh-tuntap-client

this tutorial show's how to use this project:

## Tutorial

Currently only `point-to-point (tun)` layer-3 tunneling is supported.


### Install

You have to install this package on both client and server.

```bash
sudo -H pip3 install sshtuntap
```

Or

```bash
sudo -H pip3 install git+https://github.com/pylover/sshtuntap.git
```

#### Bash auto completion

```bash
sudo ssh-tuntap-server completion install
sudo ssh-tuntap-client completion install
```

Open new bash instance to perform changes.


#### Help?


```bash
ssh-tuntap-server --help
ssh-tuntap-client --help
```

### Server setup

The server cli stands for setup network, add, delete and list users. 
this is just a utility to perform user and tuntap interface 
management and ip address assignment.


#### Install ifupdown package

Install ifupdown package in server.

```bash
apt install ifupdown
```

#### OpenSSH Server

Enable ssh tunneling on the server by editing the 
`/etc/ssh/sshd_config` and ensure the line:

```ssh
PermitTunnel yes
```

Or


```ssh
PermitTunnel point-to-point
```

see `man 5 sshd_config` for more info.


Restart the ssh server to perform the changes.


#### Define Network

```bash
ssh-tuntap-server setup
```

Or

```bash
ssh-tuntap-server setup 192.168.100.0/24
```


#### Add `foo` host

You have to create the server user mannualy (depends on your distro).

Here I'm using ubuntu server 18.04. and assume the server's hostname is 
`example.com`.

Run these commands on the server:

```bash
sudo adduser foo
```

Then use this command create `/home/foo/.ssh/tuntap.yml`:

```bash
ssh-tuntap-server add foo
```


### Client

Clinet command line stands for fetch host configuration from the server 
and perform connection using the `ssh -w`.


```bash
ssh-copy-id foo@example.com
ssh-tuntap-client setup foo@example.com
```

Use this to connect:

```bash
sudo ssh-tuntap-clinet connect
```

### Nat

Edit `/etc/sysctl.conf` on the server to enable ip forwarding.

```bash
net.ipv4.ip_forward = 1
```

Run `sysctl -p` to refresh with the new configuration

```bash
sudo sysctl -p
```

Configure NAT

```bash
sudo iptables -tnat -APOSTROUTING -s192.168.100.0/24 -jMASQUERADE
```

