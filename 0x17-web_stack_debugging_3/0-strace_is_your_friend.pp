# Fixing file permission issue
file { '/path/to/file':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  require => Package['apache2'],  # Ensure Apache is installed before applying this fix
}

