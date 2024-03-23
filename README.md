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

> Local product-page is OK
<br/>
![local-pp.png](utils%2Ferror_images%2Flocal-pp.png)

> Live product-page throws ERRORS
<br/>
![live-pp.png](utils%2Ferror_images%2Flive-pp.png)

>> Local POST API Responses are OK
<br/>
![local-POST-req-1.png](utils%2Ferror_images%2Flocal-POST-req-1.png)
![local-POST-req-2.png](utils%2Ferror_images%2Flocal-POST-req-2.png)
![local-POST-req-3.png](utils%2Ferror_images%2Flocal-POST-req-3.png)
![local-POST-req-4.png](utils%2Ferror_images%2Flocal-POST-req-4.png)

>> Live POST API Responses throwing ERRORS
<br/>
![live-POST-reqs.png](utils%2Ferror_images%2Flive-POST-reqs.png)

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