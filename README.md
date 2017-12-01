# Britecore - Insurance

To run on a local server:
```sh
$ virtualenv venv -p python3
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python insurance/manage.py migrate
$ python insurance/manage.py runserver
```

#### NOTE:-
-- Use Python2.7 or Python3.6 else 'Zappa' won't work.<br>
-- In the **index.html** file, do not forget to change the value of 'apiBaseUrl' path if you host it somewhere else or your endpoint/path changes.