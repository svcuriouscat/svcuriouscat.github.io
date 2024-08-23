## Creates sitemap.xml

import webgen

def stage(data):
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        ## Write sitemap file
        sitemapFile = webgen.mkfile(
            data["definitions"]["runtime"]["cwd"],
            data["config"]["Filesystem"]["DestinationDirPath"],
            data["definitions"]["filenames"]["sitemap"],
        )
        xml = webgen.renderTemplate(data["templates"]["sitemap"], {
            "links": map(lambda path: webgen.resolveURL(data["config"]["Site"]["URL"], path), data["sitemap"]),
        })
        sitemapFile.write(xml)
        sitemapFile.close()
