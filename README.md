```
python setup.py install
twistd -n web --port tcp:80 --wsgi juststream.wsgi.app
```
