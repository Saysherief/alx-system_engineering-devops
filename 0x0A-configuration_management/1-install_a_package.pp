# This puppet installs Flask from pip3

# The code below ensures pip is installed first
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
