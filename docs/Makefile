main: index.md
	bundle exec jekyll serve

index.md: ../README.md
	sed 's|/docs/||g' $^ > $@

install:
	bundle install
