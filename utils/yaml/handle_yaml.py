import yaml

class YamlHandler:
    def loader(self, filepath):
        """loading a yaml file
        filepath: str, absolute path to .yml file"""
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
