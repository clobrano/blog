TITLE="new-post"

post:
	hugo new content/posts/`date +%Y-%m-%d`-${TITLE}.md

serve:
	hugo server --buildDrafts --buildFuture
