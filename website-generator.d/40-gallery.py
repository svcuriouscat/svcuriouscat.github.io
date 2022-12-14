## Responsible for creating HTML files related to gallery and copying over picture files

import os
from PIL import Image

import utils

def stage(data):
    #
    # Loop through gallery albums
    #
    gallerySourcePath = os.path.join(
        data["definitions"]["runtime"]["cwd"],
        "data",
        "gallery",
    )
    galleryTemplateAlbums = []
    gallerySourcePath = os.path.abspath(gallerySourcePath)
    albumNames = sorted(next(os.walk(gallerySourcePath))[1], reverse=True)
    for albumName in albumNames:
        galleryTemplateAlbums.append({"name": albumName, "pictures": []})
        galleryDataAlbumPath = os.path.join(
            gallerySourcePath,
            albumName,
        )
        ## Loop through gallery album → pictures
        pictures = sorted(next(os.walk(galleryDataAlbumPath))[2])
        if len(pictures) > 1:
            for fileName in pictures:
                if fileName.startswith("."):
                    continue
                albumAndFilePath = albumName + "/" + fileName
                albumAndThumbFilePath = albumName + "/thumb_" + fileName
                ## Create thumbnail
                image = Image.open("../data/gallery/" + albumName + "/" + fileName)
                image.thumbnail((640, 640))
                utils.mkdir(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", "gallery", albumName)
                image.save(utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", "gallery", albumAndThumbFilePath))
                ## Append to array of albums
                galleryTemplateAlbums[-1]["pictures"].append({ "orig": "../assets/gallery/" + albumAndFilePath, "thumb": "../assets/gallery/" + albumAndThumbFilePath })
                ## Copy original asset file
                utils.cp(
                    utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], "data", "gallery", albumAndFilePath),
                    utils.resolveFsPath(data["definitions"]["runtime"]["cwd"], data["config"]["Filesystem"]["DestinationDirPath"], "assets", "gallery", albumAndFilePath)
                )
        else:
            ## Omit empty albums
            galleryTemplateAlbums.pop()
    pageHTML = utils.renderTemplate(data["templates"]["gallery"], {
        "albums": galleryTemplateAlbums
    })
    ## Generate HTML contents out of template
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
    ## Create new HTML file
    htmlFile = utils.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        "gallery",
        data["definitions"]["filenames"]["index"]
    )
    htmlFile.write(html)
    htmlFile.close()
    ## Add home page link to sitemap
    if data["config"].getboolean("Site", "CreateSitemap", fallback=False):
        data["sitemap"].append("/gallery/")
