#  a manifest that kills a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/alx-system_engineering-devops/0x0A-configuration_management/2-execute_a_command.pp',
  refreshonly => true,
}

