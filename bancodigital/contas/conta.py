from ..transacoes.transacao import Transacao
from .historico import Historico

class Conta:
    def __init__(self, cliente, numero, agencia):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite=500, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):
        excedeu_limite = valor > self._limite
        excedeu_saques = self._saques_realizados >= self._limite_saques

        if excedeu_limite:
            print("\nErro: Valor excede o limite por saque!")
        elif excedeu_saques:
            print("\nErro: Limite diário de saques atingido!")
        else:
            if super().sacar(valor):
                self._saques_realizados += 1
                return True
        return False