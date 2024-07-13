import os
import subprocess

TEMPLATE_FILE = "template.yaml"
MAESTRO = f"maestro test {TEMPLATE_FILE} --format junit"


def before_scenario(context, scenario):
    if os.path.exists(TEMPLATE_FILE):
        os.remove(TEMPLATE_FILE)
    tag_names = scenario.effective_tags
    app_package = 'ai.powerup.stori.debug'
    if tag_names:
        for tag_name in tag_names:
            if tag_name.lower() == "qa":
                app_package = 'ai.powerup.stori.qa'
            elif tag_name.lower() == "ios" or tag_name.lower() == "prod":
                app_package = 'ai.powerup.stori'
    with open("template.yaml", "a") as file:
        file.write(f'appId: {app_package}\n')
        file.write('---\n')


def after_scenario(context, scenario):
    print(scenario.name)
    print(subprocess.run(MAESTRO, shell=True))



