.PHONY: help build serve serve-isso upload
.PHONY: _isso-hugo _isso-devd

UPLOAD_TARGET = ks:/srv/http/schnouki.net/htdocs-hugo

help:
	@echo "Usage:"
	@echo "  make help             Show this message"
	@echo "  make build            Build the site"
	@echo "  make serve            Serve the site locally"
	@echo "  make -j serve-isso    Serve the site locally, enabling Isso"
	@echo "  make upload           Upload the updated data to the live site"

build:
	hugo --cleanDestinationDir

serve:
	hugo serve

serve-isso: _isso-hugo _isso-devd
_isso-hugo:
	hugo serve --port 1314
_isso-devd:
	devd --port 1313 /isso/=https://schnouki.net/isso /=http://localhost:1314

upload: | build
	rsync -P -rvzc --delete public/ $(UPLOAD_TARGET)
