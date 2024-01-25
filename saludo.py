import os

def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()

def run():
    # nombre = os.getenv('INPUT_NOMBRE', default="John Doe")
    nombre = 'Paco'
    set_github_action_output('saludo', f'Hola, {nombre}!')

if __name__ == '__main__':
    run()