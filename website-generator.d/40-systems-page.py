## Responsible for creating systems page’s HTML file

import utils

def stage(data):
    html = utils.renderTemplate(data["templates"]["page"], {
        "title":       utils.generatePageTitle("", data),
        "description": "Detailed description of various systems installed aboard SV Curious Cat",
        "logo":        utils.renderTemplate(data["templates"]["link"], {
            "href": "..",
            "content": "Home",
        }),
        "navigation":  utils.generateNavigation(),
        "criticalcss": utils.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         "../" + data["definitions"]["filenames"]["css"],
        "class":        "systems content",
        "content":     utils.renderMarkdown(open("../data/systems.md", "r").read()),
    })
    htmlFile = utils.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["config"]["Site"]["SystemsPath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()

    ## Add systems page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/systems/")
