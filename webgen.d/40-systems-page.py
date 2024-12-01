## Responsible for creating systems page’s HTML file

import os

import yaml

import webgen

blankPixel = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="

# CA: 🇨🇦
# DE: 🇩🇪
# IT: 🇮🇹
# NL: 🇳🇱
# UK: 🇬🇧
# US: 🇺🇸

def printSystemHtml(systemDataItem):
    # Print system component's title
    title = (systemDataItem["name"] if "name" in systemDataItem else systemDataItem["what"])
    output = "<div>"
    output += "<h3>" + title + "</h3>"
    output += "<a href=" + (systemDataItem["link"] if "link" in systemDataItem else "javascript:void(0)") + "><img src=" + (systemDataItem["image"] if "image" in systemDataItem else blankPixel) + " alt=" + title + " /></a>"
    output += "<ul>"
    for systemKey, systemValue in systemDataItem.items():
        if systemKey != "_":
            # Print properties of the system
            if systemKey not in ["what", "name", "image", "link"]:
                value = systemValue if (isinstance(systemValue, str)) else ", ".join(systemValue)
                output += "<li>" + systemKey.replace("_", " ").title() + ": " + value + " </li>"
        else:
            # Print sub-systems
            for subSystemDataItem in systemValue:
                output += "<li>" + printSystemHtml(subSystemDataItem) + "</li>"
    output += "</ul>"
    output += "</div>"
    return output

def stage(data):
    #
    # Parse systems YAML and header Markdown files
    #
    systemsSourcePath = os.path.join(
        data["definitions"]["runtime"]["cwd"],
        "data",
        "systems.yaml",
    )
    pageHtml = ""
    systemsSourcePath = os.path.abspath(systemsSourcePath)

    with open(systemsSourcePath, "r") as stream:
        try:
            # print(yaml.safe_load(stream))
            systemsObject = yaml.safe_load(stream)
            for systemKey, systemData in systemsObject.items():
                pageHtml += "<fieldset>"
                pageHtml += "<legend><h2>" + systemKey.title() + "</h2></legend>"
                for systemDataItem in systemData:
                    pageHtml += printSystemHtml(systemDataItem)
                pageHtml += "</fieldset>"
                pageHtml += "<br />"
        except yaml.YAMLError as exception:
            pageHtml = "Error: " + str(exception)

    html = webgen.renderTemplate(data["templates"]["page"], {
        "title":       webgen.generatePageTitle("Systems", data),
        "description": "Detailed description of various systems installed aboard SV Curious Cat",
        "logo":        webgen.renderTemplate(data["templates"]["link"], {
            "href": "..",
            "content": "Home",
        }),
        "navigation":  webgen.generateNavigation(),
        "criticalcss": webgen.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         "../" + data["definitions"]["filenames"]["css"],
        "class":        "systems content",
        "content":     webgen.renderMarkdown(open("../data/systems.md", "r").read()) + pageHtml,
    })
    htmlFile = webgen.mkfile(
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
