# Kill the "killmenow" process using pkill
exec { 'killmenow':
  command => 'pkill -f "killmenow"',
  onlyif  => 'pgrep -f "killmenow"',
}

