import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from conecta_banco import *
#
class Frame():

    def limpa_campos(self):
        self.treev["columns"] = ("0", "1", "2", "3", "4", "5")
        self.treev.heading('0', text='')
        self.treev.heading('1', text='')
        self.treev.heading('2', text='')
        self.treev.heading('3', text='')
        self. treev.heading('4', text='')
        self.treev.heading('5', text='')
        self.cont = -1
        for a in self.result_o:
            self.cont = self.cont + 1
            self.treev.delete(*self.treev.get_children())
        self.combobox.set('')

    def informa(self):

        #showinfo(title='Atenção',message=f'Você selecionou {var.get()}!')
        if self.var.get() == 'Plano de Contas':
            # Defining number of columns
            self.treev["columns"] = ("0", "1", "2", "3", "4", "5")
            self.treev.heading('0', text='empresa')
            self.treev.heading('1', text='revenda')
            self.treev.heading('2', text='conta')
            self.treev.heading('3', text='conta editada')
            self.treev.heading('4', text='des_conta')
            self.treev.heading('5', text='natureza')
            self.cont = -1
            for a in self.result_o:
                self.cont = self.cont + 1
                self.treev.insert("", "end", values=(f"{a[0]}", f"{a[1]}", f"{a[2]}", f"{a[3]}", f"{a[4]}", f"{a[5]}"))
            self.showinfo(title='Atenção', message=f'Foram encontrados: {self.cont} registros!')
        elif self.var.get() == 'Titulos em Aberto':
            self.treev["columns"] = ("0", "1", "2", "3", "4", "5")
            self.treev.heading('0', text='empresa')
            self.treev.heading('1', text='revenda')
            self.treev.heading('2', text='conta')
            self.treev.heading('3', text='conta editada')
            self.treev.heading('4', text='des_conta')
            self.treev.heading('5', text='natureza')

    def tipo_banco(self,val):
        showinfo(title='Atenção', message=f'Você selecionou {self.var2.get()}!')
        self.tipo = self.var2.get()
        if self.tipo == 'ORACLE':
            self.tipo = 1
        if self.var2.get() == 'ORACLE':
            self.label2 = tkinter.Label(master=self.window2, text="IP/Instancia:", width=30, height=1)
            self.label2.place(relx=0.2, rely=0.23)
            self.campo_inst = Entry(self.window2, bd=5, width=34)
            self.campo_inst.place(relx=0.2, rely=0.31)

            self.label3 = tkinter.Label(master=self.window2, text="Usuário:", width=30, height=1)
            self.label3.place(relx=0.2, rely=0.43)
            self.campo_user = Entry(self.window2, bd=5, width=34)
            self.campo_user.place(relx=0.2, rely=0.51)

            self.label4 = tkinter.Label(master=self.window2, text="Senha:", width=30, height=1)
            self.label4.place(relx=0.2, rely=0.63)
            self.campo_senha = Entry(self.window2, bd=5, width=34)
            self.campo_senha.place(relx=0.2, rely=0.71)
        return

    def tela_conect(self):
        self.window2 = Tk()
        self.window2.title("Conexão")
        self.window2.configure(width=350, height=350)
        self.window2.configure(bg='purple')
        self.window2.resizable(False,False)
        # lable
        self.label1 = tkinter.Label(master=self.window2, text="Banco de dados:", width=30, height=1)
        self.label1.place(relx=0.2, rely=0.05)
        self.var2 = tkinter.StringVar()
        self.combobox2 = ttk.Combobox(self.window2, textvariable=self.var2,width=32)
        self.combobox2.place(relx=0.2, rely=0.13)
        self.combobox2['state'] = 'readonly'
        self.combobox2['values'] = ('ORACLE', 'SQLSERVER')
        self.combobox2.bind('<<ComboboxSelected>>', self.tipo_banco)



        '''
        label2 = tkinter.Label(master=window2, text="Instancia:", width=30, height=1)
        label2.place(relx=0.2, rely=0.23)
        campo_inst = Entry(window2, bd=5,width=34)
        campo_inst.place(relx=0.2, rely=0.31)
    
        label3 = tkinter.Label(master=window2, text="Usuário:", width=30, height=1)
        label3.place(relx=0.2, rely=0.43)
        campo_user = Entry(window2, bd=5,width=34)
        campo_user.place(relx=0.2, rely=0.51)
    
        label4 = tkinter.Label(master=window2, text="Senha:", width=30, height=1)
        label4.place(relx=0.2, rely=0.63)
        campo_seha = Entry(window2, bd=5,width=34)
        campo_seha.place(relx=0.2, rely=0.71)
        '''
        #Button
        self.button = ttk.Button(master=self.window2, text="Conectar", command=self.conexao, width=21)
        self.button.place(relx=0.6, rely=0.92)

        self.window2.mainloop()

    # declara a janela
    def tela_main(self):
        '''
        global var
        global treev
        global window
        global combobox
        '''
        self.window = Tk()
        self.window.title("Gera_Relatório")
        self.window.configure(width=900, height=700)
        self.window.configure(bg='purple')
        self.window.resizable(True, True)

        #lable
        self.label = tkinter.Label(master=self.window,text="Relatório:",width=10,height=3)
        self.label.place(relx=0.01, rely=0.01)

        #Criando Combobox
        self.var = tkinter.StringVar()#avalia se um valor foi alterado ou atribuido
        self.combobox = ttk.Combobox(self.window, textvariable=self.var)
        self.combobox['values'] = ('Plano de Contas', 'Titulos em Aberto')
        self.combobox.place(relx=0.01,rely=0.1)
        self.combobox['state'] = 'readonly'


        # Responsável por trazer as informações do combobox
        self.combobox.bind('<<ComboboxSelected>>', self.informa)
        #Criando Frame
        self.frame_result = ttk.Frame(master=self.window,width=900,height=800)
        self.frame_result.place(relx=0.01, rely=0.22)

        # Using treeview widget
        self.treev = ttk.Treeview(self.frame_result, selectmode='browse',show='headings') # O show='headings' faz com que a primeira coluna seja ocultada
        self.treev.pack(side='left')
        self.verscrlbar = ttk.Scrollbar(self.frame_result,orient="vertical",command=self.treev.yview)
        self.verscrlbar.pack(side='right', fill='y')
        self.treev.configure(yscrollcommand=self.verscrlbar.set)
        #horscrlbar = ttk.Scrollbar(frame_result,orient="horizontal",command=treev.xview)
        #horscrlbar.pack(side='bottom', fill='x')
        #treev.configure(xscrollcommand=horscrlbar.set)

        #colunas vazias apenas para dimencionar a tela
        self.treev["columns"] = ("0", "1", "2", "3", "4", "5")

        self.button = ttk.Button(master=self.window,text="Limpar",command=self.limpa_campos,width=50)
        self.button.place(relx=0.01, rely=0.6)

        self.window.mainloop()



