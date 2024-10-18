import re
from pathlib import Path
from pylode.profiles.ontpub import OntPub
from textwrap import indent
from markdown import markdown

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

# add examples images
html = re.sub('<h2>Classes</h2>', '''<h2>Classes</h2>
                <img src="img/geoname.svg" width="50%"/>
                <br />
                <img src="img/mining-permit.svg" width="50%"/>
                <br />''', html)

# add Introduction
html = re.sub(
    '<div class="section" id="classes">',
    '<div class="section" id="intro">' +
    indent(markdown(open("intro.md").read()), "       ") +
    '</div>' +
    '<div class="section" id="classes">' ,
    html
)

html = re.sub(
    r'''<li>(\s*)<h4>(\s*)<a href="#metadata">Metadata</a>(\s*)</h4>(\s*)</li>''',
'''<li>
                  <h4>
                    <a href="#metadata">Metadata</a>
                  </h4>
                </li>
                <li>
                  <h4>
                    <a href="#intro">Introduction</a>
                  </h4>
                  <ul class="second">
                    <li>
                      <a href="#purpose">Purpose</a>
                    </li>
                    <li>
                      <a href="#basic">Basic Concepts</a>
                    </li>
                  </ul>                  
                </li>''',
    html
)

# write HTML to file
open(REPO_DIR / "model.html", "w").write(html)
