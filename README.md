```
python setup.py install
waitress-serve --port 80 --call 'juststream.wsgi:create_app'
```
