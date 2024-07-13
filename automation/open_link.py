def url(string):
    with open("template.yaml", "a") as file:
        file.write(f'- openLink: \n')
        file.write(f'   link: "{string}"\n')
        file.write(f'   autoVerify: true\n')
