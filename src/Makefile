-include ../Makefile

compare: ../../../moot/optimize/[bchmp]*/*.csv
		mkdir -p ~/tmp
		{ $(foreach d, $^, (python3 -B n2m.py -f $d --compare &);) } | tee ~/tmp/$@.out

compared:
	cat ~/tmp/compare.out | sort -n -t,  \
	| gawk -F, -f ../etc/compare.awk  \
	| column -s, -t \
	| grep --color "A"
	

