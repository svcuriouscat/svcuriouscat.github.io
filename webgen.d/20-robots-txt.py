## Creates robots.txt

from urllib.parse import urlparse

import webgen

def stage(data):
    url = urlparse(data["config"]["Site"]["Url"])
    contents = "Host: " + url.netloc + "\n"
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        contents += "Sitemap: " + webgen.resolveURL(url.geturl(), data["definitions"]["filenames"]["sitemap"]) + "\n"
    fileHandle = webgen.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        "robots.txt",
    )
    fileHandle.write(contents)
    fileHandle.close()
