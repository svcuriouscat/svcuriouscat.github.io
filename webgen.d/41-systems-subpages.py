## Responsible for creating systems subpages’ HTML files

import os

import webgen

def stage(data):
    #
    # Loop through systems documents
    #
    systemsSourcePath = os.path.join(
        data["definitions"]["runtime"]["cwd"],
        "data",
        "systems",
    )
    systemsLinks = []
    systemsSourcePath = os.path.abspath(systemsSourcePath)
    systemsDocumentNames = sorted(next(os.walk(systemsSourcePath), (None, None, []))[2])
    for systemDocumentName in systemsDocumentNames:
        systemsLinks.append(webgen.renderTemplate(data["templates"]["link"], {
            "href": os.path.splitext(systemDocumentName)[0] + "/",
            "content": os.path.splitext(systemDocumentName)[0].replace('-', ' ', 1).title(),
        }))

        html = webgen.renderTemplate(data["templates"]["page"], {
            "title":       webgen.generatePageTitle(os.path.splitext(systemDocumentName)[0].replace('-', ' ', 1).title(), data),
            "description": os.path.splitext(systemDocumentName)[0].replace('-', ' ', 1).title(),
            "logo":        webgen.renderTemplate(data["templates"]["link"], {
                "href": "../..",
                "content": "Home",
            }),
            "navigation":  webgen.generateNavigation(),
            "criticalcss": webgen.compileSass(open("../src/styles/critical.scss", "r").read()),
            "css":         "../../" + data["definitions"]["filenames"]["css"],
            "class":        "systems-" + os.path.splitext(systemDocumentName)[0] + " content",
            "content":     webgen.renderMarkdown(open("../data/systems/" + systemDocumentName, "r").read()),
        })
        htmlFile = webgen.mkfile(
            data["definitions"]["runtime"]["cwd"],
            data["config"]["Filesystem"]["DestinationDirPath"],
            data["config"]["Site"]["SystemsPath"],
            os.path.splitext(systemDocumentName)[0],
            data["definitions"]["filenames"]["index"]
        )
        htmlFile.write(html)
        htmlFile.close()

        ## Add systems subpage link to sitemap
        if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
            data["sitemap"].append("/systems/" + os.path.splitext(systemDocumentName)[0] + "/")
