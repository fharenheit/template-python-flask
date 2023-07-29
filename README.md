# Python Flask Project Template

Flask 기반 REST API 프로젝트 템플릿

## Requirement

* Python 3.6 이상

## Package

```
# pip3 install -r requirements
```

## Run

```
# export FLASK_APP = app.py
# export FLASK_ENV = development
# export FLASK_DEBUG = 0
# python3 -m flask run 
```

## Trouble Shootings

* `Fatal Python error: init_stdio_encoding: failed to get the Python codec name of the stdio encoding`
  * 윈도 환경에서 IntelliJ에서 에러가 발생하는 경우 Settings에서 Encoding으로 검색하여 UTF-8로 변경 
