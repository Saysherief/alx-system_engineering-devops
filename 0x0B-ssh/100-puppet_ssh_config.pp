# This puppet creates a Client configuration file
# The code creates/updates the file '~/.ssh/config' with specific path, permission,
# owner, group & content
file { '/root/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
  content => "
Host *
    PasswordAuthentication no

Host 54.157.137.159
    IdentityFile ~/.ssh/school
  ",
}
