## Responsible for creating landing page’s HTML file

import webgen

def stage(data):
    html = webgen.renderTemplate(data["templates"]["page"], {
        "title":       webgen.generatePageTitle("", data),
        "description": "Curious Cat lives!",
        "logo":        webgen.renderTemplate(data["templates"]["link"], {
            "href": ".",
            "content": "Home",
        }),
        "navigation":  webgen.generateNavigation(),
        "criticalcss": webgen.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         data["definitions"]["filenames"]["css"],
        "class":        "home content",
        "content":     webgen.renderMarkdown(open("../data/home.md", "r").read()),
    })
    htmlFile = webgen.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()

    ## Add home page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/")
