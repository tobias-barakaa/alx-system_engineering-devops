# fixes`

file { '/etc/apache2/sites-available/your_site.conf':
  ensure => present,
  source => 'puppet:///modules/your_module/your_site.conf',
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => File['/etc/apache2/sites-available/your_site.conf'],
}
