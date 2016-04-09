# ghc-survey
This django project is for surveying neighborhoods. It should provide an easy 
interface for church volunteers.

To launch,  

```
pip install -r requirements.txt
python manage.py syncdb
python manage.py sql questions
python manage.py syncdb
python manage.py runserver
```

Then visit `localhost:8000/survey/` (mind the trailing slash)

