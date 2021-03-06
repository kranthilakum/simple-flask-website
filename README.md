### Running application

Run app.py in terminal

```bash
python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.0.109:5000/ (Press CTRL+C to quit)
 * Restarting with watchdog (fsevents)
 * Debugger is active!
 * Debugger PIN: 899-605-522
```

Open localhost:5000 or http://192.168.0.109:5000 in web browser.

```bash
192.168.0.109 - - [05/Dec/2021 12:11:58] "GET / HTTP/1.1" 200 -
192.168.0.109 - - [05/Dec/2021 12:11:58] "GET /favicon.ico HTTP/1.1" 404 -
```

Open http://192.168.0.109:5000/cakes in web browser to route site to cakes.

```bash
192.168.0.109 - - [05/Dec/2021 12:17:57] "GET /cakes HTTP/1.1" 200 -
```

### Generate CSS (a lot!)

Generate CSS from Tailwindcss preprocessor directives, in addition to custom application CSS.

```bash
npx tailwindcss -i ./static/style.css -o ./static/main.css
```

### Source

- [Python web server with Flask](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/), Raspberry Pi
