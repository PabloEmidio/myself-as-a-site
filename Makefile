.PHONY: site
site:
	cd hugo-resources && hugo
	python bin/hugomake.py
	uvicorn myself_as_a_site.app:app --reload

.PHONY: clean
clean:
	cd hugo-resources && rm -rf assets/ public/ resources/
