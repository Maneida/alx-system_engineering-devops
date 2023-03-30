# Using Puppet, create a manifest that kills a process named 'killmenow'
# Must use 'exec' and 'pkill'

exec { 'killmenow':
  command   => '/usr/bin/pkill -f killmenow',
  onlyif    => '/usr/bin/pgrep -f killmenow',
  path      => '/usr/bin',
  logoutput => true,
}
