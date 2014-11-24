If you are going to use the ssh tunnel with the option "-D 8080" then you need to setup the browser to use a SOCKS5 proxy. Setup the proxy config page with the following entries and leave the rest of the entries blank.

> Manual proxy configuration:
  SOCKS Proxy  127.0.0.1  Port 8080
  check the box for "SOCKS v5"
  
ssh and direct connect (SOCKS5) : The following line will start the ssh client and connect to username@remote_machine.com. Port 8080 on localhost (127.0.0.1) will listen for requests and send them to the remote machine. The remote machine will then send the packets out as if they originated from itself. The ssh options are in the man page of ssh, but to summarize them in order: Compression, SSH2 only, Quite, Force pseudo-tty allocation, Redirect stdin from /dev/null, and Place the ssh client into "master" mode for connection sharing.

> ssh -C2qTnN -D 8080 username@remote_machine.com

> ssh -C2qTnN -D 8080 -vp 2722 username@remote_machine.com
