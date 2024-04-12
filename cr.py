import crypt as c
import datetime

class User:
    def __init__(self, id, name, password): # méthode spéciale qui est appelée lors de la création d'un objet
        self.id = id
        self.name = name
        self._salt = c.mksalt() # crée un salt aléatoire, c'est a dire
        # une chaine de caractère aléatoire qui sera utilisée pour crypter le mot de passe
        self.password = self._crypt_pwd(password) # on chiffre le mdp

    def _crypt_pwd(self, password):
        return c.crypt(password, self._salt)
    # on chiffre le mdp avec le salt

    def user_check_pwd(self, password):
        return self.password == self._crypt_pwd(password)


###
# john = User()
# john.id = 1
# john.name = 'john'
# john.password = '12345'

# print('Bonjour, je suis {}.'.format(john.name))
#ici john.check_pwd('123') ~~ User.check_pw('john','123')