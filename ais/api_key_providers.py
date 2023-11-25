import keyring


class KeyRingProvider:
    """
    A class to manage the OpenAI API key using keyring.
    """

    def __init__(self):
        self.service_name = "dev.trungnguyenv.ais"

    def set_api_key(self, api_key: str):
        """
        Set the API key in the keyring.
        """
        keyring.set_password(self.service_name, "api_key", api_key)

    def get_api_key(self) -> str:
        """
        Retrieve the API key from the keyring.
        """
        return keyring.get_password(self.service_name, "api_key")

    def delete_api_key(self):
        """
        Delete the API key from the keyring.
        """
        keyring.delete_password(self.service_name, "api_key")
