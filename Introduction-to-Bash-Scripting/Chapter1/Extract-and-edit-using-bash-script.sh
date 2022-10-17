#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
repl:~/workspace$ cd /home/repl/workspace
repl:~/workspace$ bash script.sh