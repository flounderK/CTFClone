# CTFClone
A python script to download everything from a CTFd instance with selenium

Currently only linux is supported

Web-based challenge downloads are only minimally supported, the main purpose of the script is to download RE, PWN, DFIR, and crypto challenges.

== Usage ==
run chrome_driver_download.py to download the chromedriver


usage: CTFClone.py [-h] [--ctf-name CTF_NAME] url

positional arguments:
  url                   url for the page to ctf

optional arguments:
  -h, --help            show this help message and exit
  --ctf-name CTF_NAME, -n CTF_NAME
                        Name of the ctf (to be used as a directory name



