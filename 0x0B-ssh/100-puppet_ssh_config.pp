# This puppet modifies a Client configuration file
# The code modifies the file '/etc/ssh/ssh_config'
file_line { 'Configure SSH authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => [
    '	PasswordAuthentication no',
    '	IdentityFile ~/.ssh/school',
  ],
}
