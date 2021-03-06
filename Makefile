.PHONY: help build build-clean serve serve-isso upload
.PHONY: _isso-hugo _isso-devd

DEPLOY_HOST ?= ks
DEPLOY_PATH ?= /srv/http/schnouki.net/htdocs-hugo
UPLOAD_TARGET = $(DEPLOY_HOST):$(DEPLOY_PATH)

SERVE_OPTS = --buildDrafts --buildFuture --i18n-warnings

help:
	@echo "Usage:"
	@echo "  make help             Show this message"
	@echo "  make build            Build the site"
	@echo "  make build-clean      Build the site, cleaning unused cache files"
	@echo "  make serve            Serve the site locally"
	@echo "  make -j serve-isso    Serve the site locally, enabling Isso"
	@echo "  make upload           Upload the updated data to the live site"

build:
	hugo --cleanDestinationDir

build-clean:
	hugo --cleanDestinationDir --gc

serve:
	hugo serve $(SERVE_OPTS)

serve-isso: _isso-hugo _isso-devd
_isso-hugo:
	hugo serve $(SERVE_OPTS) --port 1314
_isso-devd:
	devd --port 1313 /isso/=https://schnouki.net/isso /=http://localhost:1314

upload: | build
	rsync -crvzP -e "ssh -o StrictHostKeyChecking=accept-new" \
		--delete public/ $(UPLOAD_TARGET)
