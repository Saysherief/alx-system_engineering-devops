# This puppet creates a file in /tmp
# The code creates the file 'school' with specific path, permission,
# owner, group & content
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
