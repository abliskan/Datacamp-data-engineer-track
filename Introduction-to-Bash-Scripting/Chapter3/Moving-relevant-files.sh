$ cat script.sh
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on sfile's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi

$ bash script.sh logfiles8.txt
$ bash script.sh log1.txt
$ bash script.sh logdays.txt