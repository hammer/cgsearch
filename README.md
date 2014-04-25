Solr search index for the [CGHub](https://cghub.ucsc.edu/) metadata.

Download metadata from the [CGHub Data Browser](https://browser.cghub.ucsc.edu/), then:
```
$ solr /path/to/cgsearch-solr-home
$ scripts/index_cghub_medata.py -m metadata.xml
```
