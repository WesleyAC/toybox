from genshi.template import TemplateLoader
import os

loader = TemplateLoader(os.path.dirname(__file__))
tmpl = loader.load('encoder.svg')
print(tmpl.generate(r_outer=100,
                    r_inner=50,
                    spacing=3,
                    num_clicks=16,
                    debug=False))
