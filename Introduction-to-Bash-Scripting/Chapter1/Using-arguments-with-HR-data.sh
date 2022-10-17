# Echo the first ARGV argument
echo $! 

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "$1".csv

# Now save and run!
repl:~/workspace$ cd /home/repl/workspace
repl:~/workspace$ bash script.sh Seoul
repl:~/workspace$ bash script.sh Tallinn