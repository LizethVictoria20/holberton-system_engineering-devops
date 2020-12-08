# Client configuration file...
file_line { 'Refuse to authenticate using a password':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
file_line { 'configuration to use the private key':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => ' IdentityFile ~/.ssh/holberton'
}
