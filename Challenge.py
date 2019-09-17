import os
import shutil


class Challenge(object):
    def __init__(self, name, category, message, value, downloaded_file_paths, parent_path):
        self.name = name.replace(" ", "_")
        self.category = category
        self.message = message
        self.value = value
        self.parent_path = parent_path
        self.downloaded_file_paths = downloaded_file_paths
        self.setup_challenge_dir()

    def setup_challenge_dir(self):
        dir_path = os.path.join(self.parent_path, self.category, self.name)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, "message"), "w") as f:
            f.write(self.message)

        with open(os.path.join(dir_path, "value"), "w") as f:
            f.write(self.value)

        for f in self.downloaded_file_paths:
            shutil.copy(f, os.path.join(dir_path, os.path.split(f)[1]))

