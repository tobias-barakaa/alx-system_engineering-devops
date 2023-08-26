# 2-execute_a_command.pp

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
