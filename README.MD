<h1>URL SHORTENER</h1>
<p>Create a short url for any original url you want</p>
<p>Display matrices such as: link count, number of different users per link</p>
<h3>Run Locally</h3>
<p>Enter urlShortener folder, and:</p>
<p>run by entering: python manage.py runserver <br>in url_shortener\urlShortener folder</p>
<p>an original link should be of the form 'http://www....'</p>
<p>Run locally with python manage.py runserver and test the api using  http://127.0.0.1:8000/admin</p>
<h3>Run with Docker</h3>
docker build -t url-shortener-app .
<br>
docker run -it -p 8000:8000 url-shortener-app</l1>