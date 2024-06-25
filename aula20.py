# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         return super().upper()


# string = MinhaString("Davi")
# print(string.upper())

class A:
    atributo_a = 'valor'
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor'
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor'
    def metodo(self):
        super().metodo()
        print('C')

c = C()
c.metodo()