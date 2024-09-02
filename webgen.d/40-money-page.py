## Responsible for creating money page's HTML file

import webgen

def stage(data):
    html = webgen.renderTemplate(data["templates"]["page"], {
        "title":       webgen.generatePageTitle("Money", data),
        "description": "You have it, and I want it, too",
        "logo":        webgen.renderTemplate(data["templates"]["link"], {
            "href": "..",
            "content": "Home",
        }),
        "navigation":  webgen.generateNavigation(),
        "criticalcss": webgen.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         "../" + data["definitions"]["filenames"]["css"],
        "class":        "money content",
        "content":     webgen.renderMarkdown(open("../data/money.md", "r").read()),
    })
    htmlFile = webgen.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["config"]["Site"]["MoneyPath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()

    ## Add money page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/" + data["config"]["Site"]["MoneyPath"] + "/")
