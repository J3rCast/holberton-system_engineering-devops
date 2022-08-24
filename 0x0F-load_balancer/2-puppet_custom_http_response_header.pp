# create a custom HTTP header response
file { '/etc/nginx/sites-available/default':
  ensure => present,
  source => '/home/ubuntu/new_default_1'
}
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart'
}
