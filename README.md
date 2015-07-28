# [grantmcgovern.com](http://grantmcgovern.com) (V2)

![preview](http://i1158.photobucket.com/albums/p618/g12mcgov/personal_site_demo.gif)

Overview
=======

Currently, this is my personal website. It's a big improvement from the [old one](https://github.com/g12mcgov/grantmcgovern.com) because it's now dynamic and has a lot of updated features. 

It's currently a Django 1.5.x app that sits on Heroku, using MongoDB as the database layer, New Relic for monitoring, Google Analytics, and with Cloudflare support (SSL/HTTPS). I was inspired to embed a command prompt/terminal on the site, so I used a Javascript plugin I wrote, [Terminal.js](https://github.com/g12mcgov/Terminal.js).

Most of the content on the site is *real time*. For example, the "Code Count" graph found on the front page is a live count of what programming languages I write based on aggregate counts of file extensions in my Dropbox (I store everything in a `/Developer` directory).

Additionally, the "Work Experience" section is dynamically rendered content by using the LinkedIn API. That way, new positions are added in sync with my LinkedIn profile. I originally wanted to do something a little crazy and build the site using either Erlang or [Crow](https://github.com/ipkn/crow) (C++) but found in the spirit of time, templating engines, MongoDB persistence engines, Python/Django was a safe bet.

Installing
=======

If you're interested in using my site as a clone, here's how you'll need to get it up and running:

1) `$ git clone https://github.com/g12mcgov/grantmcgovern.com-V2`

I suggest you first make a virtual environment. (Install [virtualenv](https://virtualenv.pypa.io/en/latest/index.html))

2) `$ virtualenv grantmcgovern`

Then you'll need to run the setup script. 

2) `sudo python setup.py install`

This will create the build package. Then you'll need to create a MongoDB instance. Currently this site runs a lightweight Mongo instance on Heroku via MongoLabs. 

Then, to start the website launch the webserver:

4) `$ python manage.py runserver`

5) Finally, navigate to your `localhost`:

[http://localhost:8000/](http://localhost:8000/) or [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Misc.
=======

I know the [bower_components](https://github.com/g12mcgov/grantmcgovern.com-V2/tree/master/components/bower_components) directory is stored here and it shouldn't be with the `.gitignore` file, however, because I'm managing two remote origins (Heroku + GitHub), and Heroku (production) needs the modules, I'm leaving them here. Sorry.

License:
=======

The MIT License (MIT)

Copyright (c) 2015 Grant McGovern

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


(However, please consult invidual modules/packages for respective licenses).






