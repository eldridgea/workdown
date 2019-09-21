
#Badabing Badabom#

This is a test of my workers script


I've gotten used to having `freeipa-client` available in `dnf` or `apt` repos, so I've rarely setup clients manually. However, I did today in [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) on my Raspberry Pi. I wanted to document it here mainly for my own memory. It was extremely straightforward but there were a couple tweaks needed. (In this doc "example.com" replaces my domain).

On the Pi install sssd, libnss-sss, libpam-sss, openssh-server krb5-user, and krb5-config.

On the FreeIPA server:

```
$ kinit admin

$ ipa host-add --ip-address=192.168.0.3 pi.example.com

$ ipa host-add-managedby --hosts=freeipa.example.com pi.example.com

$ ipa-getkeytab -s freeipa.example.com -p host/pi.example.com -k /tmp/pi.keytab

$ scp /tmp/pi.keytab pi:/etc/krb5.keytab
```

This mostly took care of it but the SSSD conf file needed to be configured. I had an old config from another server that needed to be "upgraded" using [this script](https://github.com/npmccallum/sssd/blob/master/src/config/SSSDConfig/sssd_upgrade_config.py) leaving me with this in /etc/sssd/sssd.conf:

```
[sssd]
config_file_version = 2

[domain/example.com]

cache_credentials = True
krb5_store_password_if_offline = True
ipa_domain = example.com
id_provider = ipa
auth_provider = ipa
access_provider = ipa
ipa_hostname = pi.example.com
chpass_provider = ipa
ipa_server = _srv_, freeipa.example.com
ldap_tls_cacert = /etc/ipa/ca.crt
[sssd]
services = nss, sudo, pam, ssh

domains = example.com
[nss]
homedir_substring = /home

[pam]

[sudo]

[autofs]

[ssh]

[pac]
```

Then, in FreeIPA's web interface, I went to Authentication > Certificates and open up `CN=Certificate Authority,O=EXAMPLE.COM` (serial number 1 in my case), copied the certificate value, and pasted it into /etc/ipa/ca.crt on my Pi.

I then opened /etc/ssh/sshd_config and changed `GSSAPIAuthentication` to "yes". Once I restarted SSSD and SSH, everything worked like a charm
