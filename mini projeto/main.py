"""
Criar uma classe com sistema de login automatizado, que peça algumas informações ao usuário sobre o currículo
Pedir: Nome, idade, objetivo, experiencia
"""
class Curriculo:
    def __init__(self, nome, idade, objetivo, experiencia):
        self._nome = nome
        self._idade = idade
        self._objetivo = objetivo
        self._experiencia = experiencia

    