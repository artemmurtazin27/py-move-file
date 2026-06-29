import os


def move_file(command: str):
    command_in_list = command.split(" ")
    old_file = command_in_list[1]
    destination_path = command_in_list[-1]

    if destination_path.endswith("/") or destination_path.endswith("\\"):
        dir_path = destination_path
        new_file = os.path.basename(old_file)
    else:
        dir_path = os.path.dirname(destination_path)
        new_file = os.path.basename(destination_path)
    if dir_path:
        dir_path = os.path.normpath(dir_path)
        os.makedirs(dir_path, exist_ok=True)
    full_path = os.path.join(dir_path, new_file) if dir_path else new_file
    with open(old_file, "r") as source_file:
        content = source_file.read()
    with open(full_path, "w") as destination_file:
        destination_file.write(content)
    os.remove(old_file)
