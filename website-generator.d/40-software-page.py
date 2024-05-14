## Responsible for creating software page's HTML file

import utils

def stage(data):
    html = utils.renderTemplate(data["templates"]["page"], {
        "title":       utils.generatePageTitle("Software", data),
        "description": "All the amazing digital tools",
        "logo":        utils.renderTemplate(data["templates"]["link"], {
            "href": "..",
            "content": "Home",
        }),
        "navigation":  utils.generateNavigation(),
        "criticalcss": utils.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         "../" + data["definitions"]["filenames"]["css"],
        "class":        "software content",
        "content":     utils.renderMarkdown(open("../data/software.md", "r").read()),
    })
    htmlFile = utils.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["config"]["Site"]["SoftwarePath"],
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()
    ## Copy asset files
    utils.cpr(
        utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], "data", "software"),
        utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", data["config"]["Site"]["SoftwarePath"])
    )

    ## Add software page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/" + data["config"]["Site"]["SoftwarePath"] + "/")
