#!/usr/bin/env puppet

# creates a configuration file


file {
'config_file':
ensure  => present,
path    => '/etc/ssh/ssh_config',
content => "IdentityFile ~/.ssh/school\n\tPasswordAuthentication no"
}
