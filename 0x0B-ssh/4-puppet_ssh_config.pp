# Client configuration file...
file_line {
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
file_line {
  ensure => 'present'
  path => '/etc/ssh/ssh_config',
  line => ' IdentityFile /home/vagrant/.ssh'
}
