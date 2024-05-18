# creates a new user holberton

user {'create_user':
    name  => 'holberton',
    shell => '/bin/bash',
    home  => '/home/holberton'
}

file {'/home/holberton':
    ensure => present,
    owner  => 'holberton',
    mode   => '0755'
}
