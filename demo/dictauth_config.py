from tornado import gen
from traitlets import Dict
from jupyterhub.auth import Authenticator


class DictionaryAuthenticator(Authenticator):
    passwords = Dict(config=True,
                     help="dict of username:password for authentication"
                     )

    @gen.coroutine
    def authenticate(self, handler, data):
        """
        Check username and password against a dictionary.

        Return username if password correct, else return None.
        """
        password = self.passwords.get(data['username'])
        if password == data['password']:
            return data['username']


c.JupyterHub.authenticator_class = DictionaryAuthenticator
c.DictionaryAuthenticator.passwords = {'thead': 'secret'}
