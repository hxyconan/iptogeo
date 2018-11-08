# Changelog
All notable changes to this project will be documented in this file.

## [0.2] - 2018-11-08
### Added
- Add `iptogeo_nginx.conf.default` as sample of nginx sites config
- add `iptogeo_emperor_vassal_uwsgi.ini.default` as sample of emperor.uwsgi.service vassal config file

### Changed
- Recommand to use Nginx instead of Apache for proxy request from port 80 to API backend port
- Tested on Ubuntu 16.04, use emperor.uwsgi.service Systemd instead of native Upstart in version v0.1

