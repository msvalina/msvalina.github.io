# msvalina.org

[msvalina.org](https://msvalina.org)

## How to write new article

* On dev branch create content/new-post-foo.rst
* `pelican content -o output -s pelicanconf.py` or
* `make html`

After that

* `ghp-import output -b gh-pages`
* `git push origin gh-pages:master` Probably needs `--force`
