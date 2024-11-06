import os

import pytest
import yaml

from tools.variables import ROOT_DIR


class TestBase:

    @pytest.fixture(scope="session", autouse=True)
    def setup_once(self):
        (self.read_properties())

    @staticmethod
    def read_properties(file_path=os.path.join(ROOT_DIR, "properties.yaml")):
        try:
            with open(file_path, 'r') as f:
                TestBase.VARIABLES = yaml.safe_load(f)
        except (FileNotFoundError, yaml.YAMLError) as e:
            print(f"Error reading YAML file '{file_path}': {e}")
