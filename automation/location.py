def set_coordinates(latitude, longitude):
    with open("template.yaml", "a") as file:
        file.write(f'- setLocation: \n')
        file.write(f'   latitude: {latitude}\n')
        file.write(f'   longitude: {longitude}\n')
