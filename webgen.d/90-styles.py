## Compile Sass into CSS

import webgen

def stage(data):
    ## Write style file
    styleFile = webgen.mkfile(
        data["definitions"]["runtime"]["cwd"],
        data["config"]["Filesystem"]["DestinationDirPath"],
        data["config"]["Filesystem"]["StyleFile"],
    )
    css = webgen.compileSass(open("../src/styles/main.scss", "r").read())
    styleFile.write(css)
    styleFile.close()
