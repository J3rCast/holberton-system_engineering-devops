# create a custom HTTP header response
exec { 'append to a file':
  command => 'echo "frontend first_frontend
    bind :80
    default_backend web_servers
    
backend web_servers
    balance roundrobin
    server web-01 54.227.49.160
    server web-02 3.88.139.128" >> /etc/haproxy/haproxy.cfg'
}
exec { 'restart nginx':
  command => '/etc/init.d/nginx restart'
}
