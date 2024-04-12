# FIX MISSPELT EXT
exec {'fix_error':
command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/ /var/www/html/wp-settings.php',
path    => '/bin/',
}
exec {'apache2':
command => 'sudo service apache2 restart',
path    => ['/bin/', '/usr/bin/']
}
