# Client configuration file...
file_line {
  ensure => 'present'
  path => '/etc/ssh/ssh_config',
  line => ' IdentityFile ~/.ssh/holberton',
}
file_line {
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
