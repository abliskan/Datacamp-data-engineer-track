#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

# Now save and run!
repl:~/workspace$ cd /home/repl/workspace
repl:~/workspace$ bash script.sh