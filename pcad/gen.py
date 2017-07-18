from genshi.template import TemplateLoader
import os
import sys

if len(sys.argv) < 2:
    print("I need the name of a file as the first argument!")
    exit(1)

loader = TemplateLoader(os.path.dirname(__file__))
tmpl = loader.load(sys.argv[1])
print(tmpl.generate(r_outer=100,
                    r_inner=25,
                    spacing=3,
                    num_clicks=16,
                    flip=True,
                    debug=False))
