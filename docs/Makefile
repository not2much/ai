-include ../Makefile

view: *.md
	bundle exec jekyll serve

docs: header.txt *.md

installMac:
	brew install gawk
	sudo bundle install

header.txt:
	cat ../README.md | gawk '/^$$/ {exit} 1' > $@

%.md: ## add standard header to *md files
	echo "$@ ... "
	cat header.txt > .tmp
	gawk '/^$$/ {body=1} body' $@ >> .tmp
	sed 's|/docs/||g' .tmp | sed 's|\.md)|)|g' > $@
	rm .tmp
