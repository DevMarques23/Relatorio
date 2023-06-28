from pymssql import _mssql
import pymssql
import cx_Oracle
import os
from style import *
#

caminho = os.path.abspath(os.path.dirname('.'))  # Pega diretorio atual
cx_Oracle.init_oracle_client(lib_dir=caminho + "\client64")

class DataBase():
    def conexao(self):
        # =================
        # CONEXÃO ORACLE
        # =================
        self.connection = cx_Oracle.connect(self.campo_user.get() + '/' + self.campo_senha.get()  + '@' + self.campo_inst.get() )
        self.cursor = self.connection.cursor()
        self.teste = bool(self.connection)

        if self.teste == True:
            showinfo(title='Atenção', message=f'Conectado!')
        else:
            showinfo(title='Atenção', message=f'Não Conectado!')

        return (self.teste)
    '''
    # =================
    # CONFIGURACAO ORACLE
    # =================
    def config_oracle(self):
        self.lista = []
        self.cont = -1
        try:
            self.oracle_select = ('SELECT empresa, revenda, conta, conta editada, des_conta, natureza '
                             'from ctb_conta where empresa = 1 and revenda = 1')
            self.cursor.execute(self.oracle_select)
            self.row = self.cursor.fetchall()
            for rows in self.row:
                self.cont = self.cont + 1
                self.lista.append(rows)
        except cx_Oracle.DatabaseError as err:
            print('')
            print('Empresa/Revenda não localizada!!!')
            print('')
        # Esse result deve estar aqui pois se o banco não localizar nenhum dado, ele vai dar erro
        #print(lista[cont][3])
        return self.lista
        '''


