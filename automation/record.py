import datetime


def start_recording(name=None):
    date_name = datetime.datetime.now()
    date_name = date_name.strftime("%Y-%m-%d_%H-%M-%S")
    date_name = date_name.replace("-", "_")
    if not name:
        name = 'video'
    with open("template.yaml", "a") as file:
        file.write(f"- startRecording: {name}_{date_name}\n")


def stop_recording():
    with open("template.yaml", "a") as file:
        file.write(f"- stopRecording: \n")
