allow command `cat /path/to/files/certificate.crt` using the specified SSH key:\
`command="cat /path/to/files/certificate.crt",restrict ssh-ed25519 AAAAC3Nza...[key_content]... server-a`

make user with no permissions and put ^ in `.ssh/authorized_keys`