# bunker-scraper

### About bunker-scraper

Bunker-Scraper is a quality-of-life script that should make downloading content (that excludes everyting but videos and images) from bunkr sites way easier. This script was coded by me in a late-night-session so it's neither user friendly, nor easy to understand (probably).

**Disclaimer**: bunkr sites is a file sharing platform that is also known to host adult or illegaly acquired content. Do not use that script to do anything stupid!

### How to use

1. download the script to your preferred workspace
2. install the listed requirements
3. execute the command `python ./bunkr.py "<download dir>" <start at> "<album url>"`

| attribute    | function                                                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| download dir | The download directory is simply the path to where you awant to save your downloads (string)                                                                                                 |
| start at     | Specifies at which album entry you want to start downloading. Useful if your download failed and you want to continue at a certin point. Does **not** default to any value and has to be set (int >=0) |
| album url    | The album url is the url that you accessed the bunkr album from in your browser (string)                                                                                                             |

### Requirements

**native**

- Python 3.12.2 (tested) though any version 3.x should work fine
- random
- re (regex)
- requests
- os
- sys

**external - pip installs**

- bs4 (BeatifulSoup)
