# Define a Puppet class to manage user limits
class user_limit {
  # Ensure that the 'holberton' user exists
  user { 'holberton':
    ensure => present,
  }

  # Execute a command to set the open file limit for 'holberton' user
  exec { 'set_user_ulimit':
    # Command to set the open file limit
    command => 'ulimit -n <desired_limit>',
    # Specify the user for whom to set the limit
    user    => 'holberton',
    # Define the search path for the command
    path    => '/bin:/usr/bin:/usr/local/bin',
    # Only run the command if the current limit is not already the desired limit
    unless  => 'test $(ulimit -n) -eq <desired_limit>',
    # Ensure the 'holberton' user exists before running the command
    require => User['holberton'],
  }
}

# Include the 'user_limit' class to apply the changes
include user_limit
