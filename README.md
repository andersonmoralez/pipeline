# pipeline

### Create files Pylint and Pre-commit config (utf-8 encoding):

Command Config File Pre-commit:
```
pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8
```

Command Config File Pylint:
```
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
```
