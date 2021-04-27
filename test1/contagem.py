from usuario import Usuario, UsuarioExistente


class Contagem:

    def __init__(self, dict_user):
        self.__ident = dict_user[list(dict_user.keys())[0]]
        self.__nome = dict_user[list(dict_user.keys())[1]]
        self.__quant_agua = dict_user[list(dict_user.keys())[2]]
        self.__quant_vezes = dict_user[list(dict_user.keys())[3]]

    @property
    def ident(self):
        return self.__ident

    @property
    def nome(self):
        return self.__nome

    @property
    def quant_agua(self):
        return self.__quant_agua

    @quant_agua.setter
    def quant_agua(self, ml):
        self.__quant_agua += ml
        self.__quant_vezes += 1

    @property
    def quant_vezes(self):
        return self.__quant_vezes