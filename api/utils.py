from jinja2 import Environment, FileSystemLoader

def write_index(context):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('frontend/template.html')

    output = template.render(**context)

    return output