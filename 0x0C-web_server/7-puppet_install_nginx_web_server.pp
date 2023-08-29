# Define the Nginx class
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure => file,
    source => 'puppet:///modules/nginx/default.conf',
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
  }

  ->

  # Redirect all requests to /redirect_me to /
  # with a 301 redirect.
  httpd::location { '/redirect_me':
    ensure => present,
    redirect => '301 https://example.com/',
  }
}

