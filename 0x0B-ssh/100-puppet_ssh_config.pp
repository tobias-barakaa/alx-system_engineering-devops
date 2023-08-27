file { '/etc/ssh/sshd_config':
  content => "
# ... other lines ...
PasswordAuthentication no
# ... other lines ...
",
}

file { '/etc/ssh/ssh_config':
  content => "
# ... other lines ...
IdentityFile ~/.ssh/school
# ... other lines ...
",
}
