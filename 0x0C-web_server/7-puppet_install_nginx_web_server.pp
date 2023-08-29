# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure redirection and server block
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => 'file',
  content => "
    server {
      listen 80 default_server;
      server_name _;

      location /redirect_me {
        return 301 https://www.github.com/besthor permanent;
      }

      location / {
        root   /var/www/html;
        index  index.html;
      }
    }
  ",
}

# Enable the redirection site
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
