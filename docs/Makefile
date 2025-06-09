-include ../Makefile

view: *.md ## show site locally
	bundle exec jekyll serve

docs:  ## force update on all md files
	$(MAKE) -B header.txt *.md

installMac:  ## install tools (for os/x)
	brew install gawk
	sudo bundle install

header.txt:  ## create header.txt and index.md from ../README
	echo "$@ ... "
	cat ../README.md | gawk '/^$$/ {exit} 1' > $@
	echo "index.md ... "
	cp ../README.md index.md

%.md: ## add standard header to *md files
	echo "$@ ... "
	cat header.txt > .tmp
	gawk '/^$$/ {body=1} body' $@ >> .tmp
	sed 's|/docs/||g' .tmp | sed 's|\.md)|)|g' > $@
	rm .tmp
