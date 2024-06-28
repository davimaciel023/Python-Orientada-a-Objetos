# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    

    def log_error(self, msg):
        return self.log_error(f"Erro: {msg}")

    def log_success(self, msg):
        return self.log_error(f"Success: {msg}")

    
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('qualquer coisa')
    l.log_success('Sucesso')