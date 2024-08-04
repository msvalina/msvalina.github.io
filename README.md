# msvalina.org

[msvalina.org](https://msvalina.org)

## Build pelican deps

* Use python3
* create venv `python -m venv  ./venv` 
* `source venv/bin/activate`
* `pip3 install "pelican[markdown]"`
* `pip3 install pelican-webassets`
* `echo "\n127.0.0.1 msvalina.loc" | sudo tee -a /etc/hosts `
* `mkdir -p pelican-themes/attila-2.0 ` 
* `curl -L https://github.com/arulrajnet/attila/archive/refs/tags/v2.0.tar.gz | tar -xz -C pelican-themes/attila-2.0 --strip-components=1 ` 

## How to write new article

* On dev branch create content/new-post-foo.rst
* `pelican content -o output -s pelicanconf.py` or
* `make html`

After that

* `ghp-import output -b gh-pages`
* `git push origin gh-pages:master` Probably needs `--force`
