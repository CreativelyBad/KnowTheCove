from jinja2 import Environment, FileSystemLoader

def write_index(context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    output = template.render(**context)

    with open('index.html', 'w') as f:
        f.write(output)