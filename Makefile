.PHONY: build
build:
	docker build -t height-app-python -f Dockerfile .

.PHONY: gen
gen:
	docker run --rm -v ${PWD}:/local --platform linux/amd64 swaggerapi/swagger-codegen-cli-v3:3.0.46 generate \
		--input-spec /local/swagger.yaml \
		--lang python \
		--output /local/ \
		--git-user-id emoreth \
		--git-repo-id height-app-python
