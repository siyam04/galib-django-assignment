## E-commerce Assignment

* Python Version 3.12.2
* Django Version 5.0.3
* Database: SQLite3 (default)

<hr/>

### Links

* API Doc: http://localhost:8000/
* Django Admin: http://127.0.0.1:8000/admin/
* Product Page: http://localhost:8000/product-page/
* GitHub: https://github.com/siyam04/galib-django-assignment
* Live: https://galib04.pythonanywhere.com/ (throws some error, but works fine in Local)

>> Local product-page is OK
![img_1.png](..%2Fimg_1.png)

>> Live product-page throws ERRORS
![img.png](..%2Fimg.png)

>> Local POST API Responses are OK
![img_4.png](..%2Fimg_4.png)
![img_5.png](..%2Fimg_5.png)
![img_6.png](..%2Fimg_6.png)
![img_7.png](..%2Fimg_7.png)

>> Live POST API Responses throwing ERRORS
![img_2.png](..%2Fimg_2.png)

<hr/>

### Populate Fake Data for User

```
python generate_fake_data.py
```

### Pythonanywhere Deployment

* Doc Followed: https://tutorial.djangogirls.org/en/deploy/

```
pa_autoconfigure_django.py --python=3.10 https://github.com/siyam04/galib-django-assignment.git --nuke
```
