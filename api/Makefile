ifdef PROD_BUILD
	include .make.env
else
	include .make.env.dev
endif

IMAGE_NAME ?= api
CONTAINER_NAME ?= api
CONTAINER_INSTANCE ?= default

.PHONY: build build-force push shell run start stop rm release

build: Dockerfile check-env
	docker build --build-arg NS=$(NS) --build-arg VERSION=$(VERSION) -t $(NS)/$(IMAGE_NAME):$(VERSION) -f Dockerfile .

push:
	docker push $(NS)/$(IMAGE_NAME):$(VERSION)

shell:
	docker run --rm --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) -i -t --entrypoint /bin/bash $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION)

run:
	docker run --rm --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION)

start:
	docker run -d --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION)

stop:
	docker stop $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)

rm:
	docker rm $(CONTAINER_NAME)-$(CONTAINER_INSTANCE)

release: build
	make push -e VERSION=$(VERSION)

clean:
	docker image rm $(NS)/$(IMAGE_NAME):$(VERSION)

default: build

check-env:
ifndef VERSION
	$(error VERSION is undefined - specify with -e VERSION or inside .make_env)
endif
