# IPTOGEO

An API interface forked from [afreeorange/ip-to-location](https://github.com/afreeorange/ip-to-location) to get geo information via given IP or reading from request header.

## How to use
- Hit http://example.com/getgeo to get your geo information
- Hit http://example.com/getgeo/[ONE-OR-MANY-IPV4-ADDRESS] to get the geo information of that IP
- Check health: http://example.com/ping
- Log file: /var/log/iptogeo.log

## Features
- The API service run as an uwsgi backend application
- It support Reverse Proxy situation, which the uwsgi service will use X-FORWARDED-FOR request header after proxy
- It will download latest MaxMind DB when service started/restart
- Response data in json string, example in screenshots

![UI](https://raw.githubusercontent.com/hxyconan/iptogeo/master/screenshots/screenshot_single_ip.png)

![UI](https://raw.githubusercontent.com/hxyconan/iptogeo/master/screenshots/screenshot_multi_ips.png)

## Running emperor.uwsgi.service vassal
- Copy the `iptogeo_emperor_vassal_uwsgi.ini.default` to `/etc/uwsgi-emperor/vassals/iptogeo.ini` then this API will be managed by emperor.uwsgi.service
- Boot the uWSGI API application
```
systemctl start|restart|stop|status emperor.uwsgi.service
```
- The `/etc/uwsgi-emperor/vassals/iptogeo.ini` includes a UWSGI hardcode hook: `exec-pre-app` which will downlad the maxmind db before app load
- uWSGI service runs at special port in backend, Nginx need to be installed for proxy the request to such special backend port
- Copy `iptogeo_nginx.conf.default` to `/etc/ngix/sites-enabled/iptogeo.conf` for setup nginx to listen all requests from port 80


## TODO
- How to move this API to AWS Lambda service for more elastic and cheaper


## About the forked ip-to-location repo
- It generates the geo imformation by lookup your IP in MaxMind geo database
- It uses gunicorn to start the application
- More information check: [https://github.com/afreeorange/ip-to-location](https://github.com/afreeorange/ip-to-location)


## License
Copyright (c) 2010-2016 Bob Huang, https://github.com/hxyconan/iptogeo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
