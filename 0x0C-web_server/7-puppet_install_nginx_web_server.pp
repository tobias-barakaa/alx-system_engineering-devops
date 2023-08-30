# Puppet Manifest for Automating Project Requirements

# Install the Nginx package
package { 'nginx':
  ensure => installed,  # Ensure that the 'nginx' package is installed
}

# Configure redirection in the default Nginx server block
file_line { 'configure_redirection':
  ensure => 'present',                            # Ensure the specified line is present in the file
  path   => '/etc/nginx/sites-enabled/default',   # Path to the Nginx server block configuration
  after  => 'listen 80 default_server;',         # Insert the line after the 'listen 80 default_server;' line
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',  # Define the redirection rule
}

# Create the 'Hello World!' index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',  # Set the content of the index.html file to 'Hello World!'
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure  => running,          # Ensure the 'nginx' service is running
  require => Package['nginx'], # Require the 'nginx' package to be installed before starting the service
}
