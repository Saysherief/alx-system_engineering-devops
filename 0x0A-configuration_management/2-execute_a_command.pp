# This puppet kills a process named "killmenow"
# Execute a command 
exec { 'killmenow_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin']
}
