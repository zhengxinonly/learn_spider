import requests
import re

import execjs

text = """
window = this;

document = {
};
location = {
    href: "chrome-search://local-ntp/local-ntp.html",
    replace: function (str) {

    }
};
window.location = location;
window.location.protocol = "chrome-search:";
"""

response = requests.get('https://www.guazi.com/')
script = re.search('<script type="text/javascript">(.*?)</script>', response.text, re.S)
js = script.group(1).strip()
js = text + js
ctx = execjs.compile(js)
print(ctx.eval('document.cookie'))
