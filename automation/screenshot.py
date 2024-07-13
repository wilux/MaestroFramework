import datetime


def take(name=None):
    date_name = datetime.datetime.now()
    date_name = date_name.strftime("%Y-%m-%d_%H-%M-%S")
    date_name = date_name.replace("-", "_")
    if not name:
        name = 'screenshot'
    with open("template.yaml", "a") as file:
        file.write(f"- takeScreenshot: {name}_{date_name}\n")
