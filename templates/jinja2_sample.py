from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('base.html')

sections = [
    {'title' : 'DE ANZA COVE AMENDMENT',
      'content' : 'Fellow board member Kate Spiro and myself recently met at PBTC with \
                Joshua Coyne and Monica Eslamian who represent Councilmember Jennifer Campbell from\ 
    },
    {'title' : 'number 2',
      'content' : 'num 2 content'
    }
]

output = template.render(sections=sections)
print(output)
