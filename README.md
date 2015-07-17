# grantmcgovern.com (V2)

![preview](http://i1158.photobucket.com/albums/p618/g12mcgov/personal_site_demo.gif)

Overview
=======

Currently, this is my personal website. It's a big improvement from the [old one](https://github.com/g12mcgov/grantmcgovern.com) because it's now dynamic and has a lot of updated features. 

It's currently a Django 1.5.x app that sits on Heroku, using MongoDB as the database layer, New Relic for monitoring, Google Analytics, and with Cloudflare support (SSL/HTTPS). I was inspired to embed a command prompt/terminal on the site, so I used a Javascript plugin I wrote, [Terminal.js](https://github.com/g12mcgov/Terminal.js).

Most of the content on the site is *real time*. For example, the "Code Count" graph found on the front page is a live count of what programming languages I write based on aggregate counts of file extensions in my Dropbox (I store everything in a `/Developer` directory).

Additionally, the "Work Experience" section is dynamically rendered content by using the LinkedIn API. That way, new positions are added in sync with my LinkedIn profile. I originally wanted to do something a little crazy and build the site using either Erlang or [Crow](https://github.com/ipkn/crow) (C++) but found in the spirit of time, templating engines, MongoDB persistence engines, Python/Django was a safe bet.



