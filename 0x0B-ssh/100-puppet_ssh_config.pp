# Define a class for SSH client configuration
class ssh_client_config {

  # Ensure the SSH client uses the private key ~/.ssh/school
  file_line { 'Set SSH IdentityFile':
    path   => '/etc/ssh/ssh_config', # Path to the SSH client configuration file
    line   => '    IdentityFile ~/.ssh/school', # Line to add or modify
    match  => '^ *IdentityFile', # A pattern to match existing lines
  }

  # Ensure the SSH client refuses to authenticate using a password
  file_line { 'Disable Password Authentication':
    path   => '/etc/ssh/ssh_config', # Path to the SSH client configuration file
    line   => '    PasswordAuthentication no', # Line to add or modify
    match  => '^ *PasswordAuthentication', # A pattern to match existing lines
  }

}

# Apply the SSH client configuration class
include ssh_client_config
