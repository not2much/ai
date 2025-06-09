-include ../Makefile

ONE=cat $< | gawk 'BEGIN {FS="\n";RS=""} {print $$0 ; exit}' 
TWOPLUS=cat $@ | gawk 'BEGIN {FS="\n";RS=""} NR==1 { print("\n\n"); next} {print $$0 "\n\n"}'

main: index.md
	bundle exec jekyll serve

docs: index.md *.md

index.md: ../README.md
	sed 's|/docs/||g' $^ > $@

installMac:
	brew install gawk
	bundle install

%.md: ./README.md Makefile ## add standard header to *md files
	echo "$@ ... "
	@($(ONE);  $(TWOPLUS)) > .tmp; mv .tmp $@
