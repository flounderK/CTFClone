import os
import shutil


class Challenge(object):
    def __init__(self, name, category, message, value, downloaded_file_paths, parent_path):
        self.name = name
        self.category = category
        self.message = message
        self.value = value
        self.parent_path = parent_path
        self.downloaded_file_paths = downloaded_file_paths

    def setup_challenge_dir(self):
        """

        :return:
        """
        pass

