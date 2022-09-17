## Responsible for creating HTML files related to gallery and copying over picture files

import os

import utils

def stage(data):
    #
    # Loop through gallery albums
    #
    galleryDataPath = os.path.join(
        data["definitions"]["runtime"]["cwd"],
        "data",
        "gallery",
    )
    galleryTemplateDataAlbums = []
    galleryDataPath = os.path.abspath(galleryDataPath)
    albumNames = sorted(next(os.walk(galleryDataPath))[1], reverse=True)
    for albumName in albumNames:
        galleryTemplateDataAlbums.append({"name": albumName, "pictures": []})
        galleryDataAlbumPath = os.path.join(
            galleryDataPath,
            albumName,
        )
        ## Loop through gallery album → pictures
        pictures = sorted(next(os.walk(galleryDataAlbumPath))[2])
        if len(pictures) > 1:
            for pictureFileName in pictures:
                if pictureFileName.startswith("."):
                    continue
                galleryTemplateDataAlbums[-1]["pictures"].append("../assets/gallery/" + albumName + "/" + pictureFileName)
        else:
            galleryTemplateDataAlbums.pop()
    pageHTML = utils.renderTemplate(data["templates"]["gallery"], {
        "albums": galleryTemplateDataAlbums
    })
    ## Scan
    html = utils.renderTemplate(data["templates"]["page"], {
        "title":       utils.generatePageTitle("Gallery", data),
        "description": "Pictures of Curious Cat, old and new",
        "logo":        utils.renderTemplate(data["templates"]["link"], {
            "href": ".",
            "content": "Home",
        }),
        "navigation":  utils.generateNavigation(),
        "criticalcss": utils.compileSass(open("../src/styles/critical.scss", "r").read()),
        "css":         "../" + data["definitions"]["filenames"]["css"],
        "class":        "gallery content",
        "content":     pageHTML,
    })
    htmlFile = utils.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        "gallery",
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()
    ## Copy asset files
    utils.cpr(
        utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], "data", "gallery"),
        utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", "gallery")
    )
    ## Add home page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/gallery/")
