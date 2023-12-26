#!/usr/bin/env puppet

# creates a configuration file


file {
'config_file':
ensure  => 'present',
path    => '/home/okibe/.ssh/config',
content => "Host ubuntu\n\tHostName 52.91.126.51\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school"
}
