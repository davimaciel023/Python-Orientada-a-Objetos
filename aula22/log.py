# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
class LogFileMixin(Log):
    ...

if __name__ == '__main__':
    l = Log()
    l.log('qualquer coisa')