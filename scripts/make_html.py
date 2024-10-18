import re
from pathlib import Path
from pylode.profiles.ontpub import OntPub
from textwrap import indent

REPO_DIR = Path(__file__).parent.parent.resolve()

# initialise
od = OntPub(ontology=REPO_DIR / "model.ttl")

# make HTML
html = od.make_html()

# add overview image
name = re.findall(r"<h1>(.*)</h1>", html)[0]
name_plus_img = f'''<h1>{name}</h1>
        <img src="img/overview.svg" width="75%"/>'''
html = indent(re.sub(r"<h1>(.*)</h1>", name_plus_img, html), "        ")

html = re.sub('<h2>Classes</h2>', '''<h2>Classes</h2>
                <img src="img/geoname.svg" width="50%"/>
                <br />
                <img src="img/mining-permit.svg" width="50%"/>
                <br />''', html)

# write HTML to file
open(REPO_DIR / "model.html", "w").write(html)
