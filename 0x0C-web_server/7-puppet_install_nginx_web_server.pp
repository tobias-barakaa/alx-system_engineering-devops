# Define the Nginx class
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  # Create a default configuration file for Nginx
  file { '/etc/nginx/sites-available/default':
    ensure => file,
    content => template('nginx/default.conf.erb'),
  }

  # Create a symbolic link for the default configuration file
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
  }
}

# Define the redirection rule
class redirection {
  httpd::location { '/redirect_me':
    ensure => present,
    redirect => '301 https://www.github.com/besthor permanent;',
  }
}

# Require the Nginx and redirection classes
class main {
  require => Class['nginx'],
  require => Class['redirection'],
}
