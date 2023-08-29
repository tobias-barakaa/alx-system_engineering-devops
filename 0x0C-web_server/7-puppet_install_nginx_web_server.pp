# Define the Nginx class
class nginx {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
        ensure => running,
        enable => true,
        require => Package['nginx'],
    }

    file { '/var/www/html/index.html':
        ensure => file,
        content => 'Hello World!',
        require => Package['nginx'],
    }
}

# Apply the Nginx class
include nginx

# Define the Redirect class
class redirect {
    file { '/etc/nginx/sites-available/redirect_me':
        ensure => file,
        content => "
        server {
            listen 80;
            server_name _;
            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }
        }
        ",
        require => Class['nginx'],
    }

    file { '/etc/nginx/sites-enabled/redirect_me':
        ensure => link,
        target => '/etc/nginx/sites-available/redirect_me',
        require => File['/etc/nginx/sites-available/redirect_me'],
    }
}

# Apply the Redirect class
include redirect
