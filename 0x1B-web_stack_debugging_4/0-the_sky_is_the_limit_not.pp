# increase the ULIMIT directive to 2048


exec {'raise_ulimit':
    command =>  'sed -i "s/^ULIMIT.*/ULIMIT=\" -n 2048\"/" /etc/default/nginx',
    path    =>   ['/usr/bin/', '/bin/']
}


exec {'restart':
    command =>   'sudo service nginx restart',
    path    =>    ['/usr/bin/', '/bin/']
}
