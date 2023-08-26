# 2-execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -9 -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}
