```
python setup.py install
gunicorn -w 4 -b 0.0.0.0:8000 juststream.wsgi:app
```
