"""Wrapper for sending emails using the Mailgun API
"""
import requests
import yaml

class MailgunEmailer:
    """The Mailgun Emailer object
    """

    def __init__(self, api_url=False, api_key=False):
        """Creates an emailer for a Mailgun account.

        args:
            api_url (str): the Mailgun API endpoint
            api_key (str): the Mailgun account API key
        """
        if not api_key or not api_url:
            self.yaml = self.load_yaml("data")
        else:
            self.yaml = None
        try:
            if not api_key:
                api_key = self.yaml["api_key"]
            if not api_url:
                api_url = self.yaml["api_url"]
        except KeyError as error:
            raise f"Yaml value not found: {error}"
        self.api_url = api_url
        self.api_key = api_key

    @staticmethod
    def load_yaml(file_name):
        """Loads the contents of a yaml file.

        args:
            file_name (str): the yaml filename (without extension)
        """
        try:
            with open(f"{file_name}.yaml", "r") as yaml_file:
                return yaml.load(yaml_file)
        except FileNotFoundError:
            raise f"No `{file_name}.yaml` file found"

    def send_from_args(self, **kwargs):
        """Sends an email using the Mailgun email parameters.

        args:
            kwargs (dict): the email parameters (`from`, `to`, `subject`, `text`)
        """
        try:
            data = {
                "from": kwargs["from_addr"],
                "to": kwargs["to_addr"],
                "subject": kwargs["subject"],
                "text": kwargs["message"]
            }
        except KeyError as error:
            raise f"Yaml value not found: {error}"
        return requests.post(self.api_url, auth=("api", self.api_key), data=data)

    def send_from_yaml(self, file_name):
        """Sends an email using parameters in a yaml file.

        args:
            file_name (str): the yaml filename (without extension)
        """
        return self.send_from_args(**self.load_yaml(file_name))
