def text(string):
    with open("template.yaml", "a") as file:
        file.write(f'- eraseText \n')
        file.write(f'- inputText: "{string}"\n')
        file.write(f'- hideKeyboard \n')
        file.write(f'- runFlow:\n')
        file.write(f'   when:\n')
        file.write(f'     platform: iOS\n')
        file.write(f'   commands:\n')
        file.write(f'       - tapOn: "Done"\n')