TITLE ?= "new-post"

slugify = $(shell echo $(TITLE) | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')

post:
	hugo new content/posts/`date +%Y-%m-%d`-$(call slugify).md

serve:
	hugo server --buildDrafts --buildFuture
