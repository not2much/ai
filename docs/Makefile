-include ../Makefile

ONE=cat $< | gawk 'BEGIN {FS="\n";RS=""} {print $$0 ; exit}' 
TWOPLUS=cat $@ | gawk 'BEGIN {FS="\n";RS=""} NR==1 { print("\n\n"); next} {print $$0 "\n\n"}'

main: *.md
	bundle exec jekyll serve

docs: *.md

installMac:
	brew install gawk
	bundle install

%.md: ../README.md Makefile ## add standard header to *md files
	echo "$@ ... "
	echo @($(ONE);  $(TWOPLUS)) > .tmp; mv .tmp $@
	#@($(ONE);  $(TWOPLUS)) > .tmp; mv .tmp $@
	#sed -i 's|/docs/||g' $@
