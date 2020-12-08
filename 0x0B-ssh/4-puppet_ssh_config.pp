# Client configuration file...
file_line {
  ensure => 'present'
  path => '/etc/ssh/ssh_config',
  line => ' IdentityFile /home/vagrant/.ssh',
}
file_line {
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
