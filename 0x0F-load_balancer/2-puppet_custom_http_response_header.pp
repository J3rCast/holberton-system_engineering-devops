# create a custom HTTP header response
package { 'nginx':
  ensure => installed,
  name   => nginx
}
file { '/etc/nginx/sites-available/default':
  ensure => present,
  source => '/home/jerson/Holberton/holbertonschool-system_engineering-devops/0x0F-load_balancer/new_default_1'
  #source => '/home/ubuntu/new_default_1'
}
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart'
}
