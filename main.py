from tkinter import *
from tkinter import ttk
import webbrowser
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

root = Tk()


class functions():
    def variaveis(self):
        self.za = self.za_entry.get()
        self.zb = self.zb_entry.get()
        self.zc = self.zc_entry.get()
        self.VANr = self.VANr_entry.get()
        self.VBNr = self.VBNr_entry.get()
        self.VCNr = self.VCNr_entry.get()
        self.VANf = self.VANf_entry.get()
        self.VBNf = self.VBNf_entry.get()
        self.VCNf = self.VCNf_entry.get()
        self.zcabo = self.zcabo_entry.get()

        self.VAN = float(self.VANr) * np.exp(1j * ((float(self.VANf)*3.14)/180))
        self.VBN = float(self.VBNr) * np.exp(1j * ((float(self.VBNf)*3.14)/180))
        self.VCN = float(self.VCNr) * np.exp(1j * ((float(self.VCNf)*3.14)/180))

    def variaveis2(self):
        self.variaveis()
        self.za = complex(self.za)
        self.zb = complex(self.zb)
        self.zc = complex(self.zc)
        self.VAN = complex(self.VAN)
        self.VBN = complex(self.VBN)
        self.VCN = complex(self.VCN)
        self.zcabo = complex(self.zcabo)

    def clear(self):
        self.za_entry.delete(0, END)
        self.zb_entry.delete(0, END)
        self.zc_entry.delete(0, END)
        self.VANr_entry.delete(0, END)
        self.VBNr_entry.delete(0, END)
        self.VCNr_entry.delete(0, END)
        self.VANf_entry.delete(0, END)
        self.VBNf_entry.delete(0, END)
        self.VCNf_entry.delete(0, END)
        self.zcabo_entry.delete(0, END)

    def calc(self):
        self.variaveis2()

        # print("LETRA A- \n")
        # impedancias equivalentes
        self.zat = self.za + self.zcabo
        self.zbt = self.zb + self.zcabo
        self.zct = self.zc + self.zcabo

        # Corrente de neutro
        
        # Numerador
        self.van_zat = (self.VAN/self.zat)
        self.vbn_zbt = (self.VBN/self.zbt)
        self.vcn_zct = (self.VCN/self.zct)

        # Denominador
        self.zcabo_zat = (self.zcabo/self.zat)
        self.zcabo_zbt = (self.zcabo/self.zbt)
        self.zcabo_zct = (self.zcabo/self.zct)

        # Resultado 
        self.i_neutro = ((self.van_zat + self.vbn_zbt + self.vcn_zct) / (1 + self.zcabo_zat + self.zcabo_zbt + self.zcabo_zct))
        self.r = abs(self.i_neutro)
        self.radiano = np.angle(self.i_neutro)
        self.graus = ((self.radiano*180)/3.14)
        # print("Corrente de neutro em forma de fasor: {} < {}".format(r, graus))
        # print("Corrente de neutro em forma retângular: {}".format(i_neutro))

        # print("\n\nLETRA B- \n")
        # Corrente de linha
        self.vnn = self.i_neutro * self.zcabo
        # rnn = abs(vnn)
        # radiano_nn = np.angle(vnn)
        # graus_nn = ((radiano_nn*180)/3.14)
        # print(rnn)
        # print(graus_nn)

        self.vanx = self.VAN - self.vnn
        self.vbnx = self.VBN - self.vnn
        self.vcnx = self.VCN - self.vnn

        self.i_a = (self.vanx/self.zat)
        self.i_b = (self.vbnx/self.zbt)
        self.i_c = (self.vcnx/self.zct)

        self.ra = abs(self.i_a)
        self.radiano_a = np.angle(self.i_a)
        self.graus_a = ((self.radiano_a*180)/3.14)
        # print("Corrente de linha I_A em forma de fasor: {} < {}".format(ra, graus_a))
        self.rb = abs(self.i_b)
        self.radiano_b = np.angle(self.i_b)
        self.graus_b = ((self.radiano_b*180)/3.14)
        # print("Corrente de linha I_B em forma de fasor: {} < {}".format(rb, graus_b))
        self.rc = abs(self.i_c)
        self.radiano_c = np.angle(self.i_c)
        self.graus_c = ((self.radiano_c*180)/3.14)
        # print("Corrente de linha I_C em forma de fasor: {} < {}".format(rc, graus_c))


        # print("\n\nLETRA C- \n")
        # Tensões de fase na carga

        self.v_an = self.i_a * self.za
        self.rvan = abs(self.v_an)
        self.radiano_van = np.angle(self.v_an)
        self.graus_van = ((self.radiano_van*180)/3.14)
        # print("Tensão de fase V_A'N' em forma de fasor: {} < {}".format(rvan, graus_van))
        self.v_bn = self.i_b * self.zb
        self.rvbn = abs(self.v_bn)
        self.radiano_vbn = np.angle(self.v_bn)
        self.graus_vbn = ((self.radiano_vbn*180)/3.14)
        # print("Tensão de fase V_B'N' em forma de fasor: {} < {}".format(rvbn, graus_vbn))
        self.v_cn = self.i_c * self.zc
        self.rvcn = abs(self.v_cn)
        self.radiano_vcn = np.angle(self.v_cn)
        self.graus_vcn = ((self.radiano_vcn*180)/3.14)
        # print("Tensão de fase V_C'N' em forma de fasor: {} < {}".format(rvcn, graus_vcn))


        # print("\n\nLETRA D- \n")
        # Tensões de linha na carga
        self.vab = self.v_an - self.v_bn
        self.rvab = abs(self.vab)
        self.radiano_vab = np.angle(self.vab)
        self.graus_vab = ((self.radiano_vab*180)/3.14)
        self.vbc = self.v_bn - self.v_cn
        self.rvbc = abs(self.vbc)
        self.radiano_vbc = np.angle(self.vbc)
        self.graus_vbc = ((self.radiano_vbc*180)/3.14)
        self.vca = self.v_cn - self.v_an
        self.rvca = abs(self.vca)
        self.radiano_vca = np.angle(self.vca)
        self.graus_vca = ((self.radiano_vca*180)/3.14)

    def a(self):
        self.calc()

        popup_windowa = Toplevel()
        popup_windowa.geometry("700x300")
        popup_windowa.resizable(False, False)
        popup_windowa.title("CORRENTE DE NEUTRO!!")
        popup_label0 = Label(popup_windowa, text="LETRA A- \n\nCorrente de neutro em forma de fasor: {} < {} [A]".format(round(self.r,3), round(self.graus,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label0.pack()
        
        x = self.i_neutro.real
        y = self.i_neutro.imag

        plt.plot(x, y, color = 'red', label="Corrente de Neutro")
        plt.title('Corrente de Neutro')  # adiciona um título ao gráfico
        plt.axis([-2*x, 2*x, -2*y, 2*y])
        plt.annotate("", xy=(x, y), xytext=(0, 0), arrowprops=dict(facecolor='red', width=2, headwidth=8))
        plt.legend()
        plt.xlabel('Real')  # adiciona um rótulo para o eixo x
        plt.ylabel('Imaginário')  # adiciona um rótulo para o eixo y
        plt.grid()  # adiciona uma grade ao gráfico
        plt.show()
    
    def b(self):
        self.calc()
        
        popup_windowb = Toplevel()
        popup_windowb.geometry("700x300")
        popup_windowb.resizable(False, False)
        popup_windowb.title("CORRENTES DE LINHA!!")

        popup_label1 = Label(popup_windowb, text="LETRA B- \n\nCorrentes de Linha I_A em forma de fasor: {} < {} [A]".format(round(self.ra,3), round(self.graus_a,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label2 = Label(popup_windowb, text="\nCorrente de linha I_B em forma de fasor: {} < {} [A]".format(round(self.rb,3), round(self.graus_b,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label3 = Label(popup_windowb, text="\nCorrente de linha I_C em forma de fasor: {} < {} [A]".format(round(self.rc,3), round(self.graus_c,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label1.pack()
        popup_label2.pack()
        popup_label3.pack()

        x1 = self.ra
        x2 = self.rb
        x3 = self.rc

        maiorx = 0

        if (x1 >= x2 and x1 >=x3):
            maiorx = x1
        elif (x2 >= x3 and x2 >= x1):
            maiorx = x2
        else:
            maiorx = x3
        
        
        dx1 = self.ra*np.cos(self.radiano_a) 
        dy1 = self.ra*np.sin(self.radiano_a)
        dx2 = self.rb*np.cos(self.radiano_b)
        dy2 = self.rb*np.sin(self.radiano_b)
        dx3 = self.rc*np.cos(self.radiano_c)
        dy3 = self.rc*np.sin(self.radiano_c)

        plt.figure()
        plt.title("Correntes de Linha na Carga")
        plt.quiver(0, 0, dx1, dy1, scale=1, color='r', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx2, dy2, scale=1, color='b', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx3, dy3, scale=1, color='g', angles='xy', scale_units='xy')
        plt.axis([-2*maiorx, 2*maiorx, -2*maiorx, 2*maiorx])
        plt.xlabel('Eixo Real')
        plt.ylabel('Eixo Imaginário')
        plt.grid()
        plt.show()



    def c(self):
        self.calc()

        popup_windowc = Toplevel()
        popup_windowc.geometry("700x300")
        popup_windowc.resizable(False, False)
        popup_windowc.title("TENSÕES DE FASE!!")

        popup_label4 = Label(popup_windowc, text="LETRA C- \n\nTensão de fase V_A'N' na carga em forma de fasor: {} < {} [V]".format(round(self.rvan,3), round(self.graus_van,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label5 = Label(popup_windowc, text="\nTensão de fase na carga V_B'N' em forma de fasor: {} < {}[V]".format(round(self.rvbn,3), round(self.graus_vbn,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label6 = Label(popup_windowc, text="\nTensão de fase na carga V_C'N' em forma de fasor: {} < {}[V]".format(round(self.rvcn,3), round(self.graus_vcn,3) ), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label4.pack()
        popup_label5.pack()
        popup_label6.pack()

        x1 = self.rvan
        x2 = self.rvbn
        x3 = self.rvcn

        maiorx = 0

        if (x1 >= x2 and x1 >=x3):
            maiorx = x1
        elif (x2 >= x3 and x2 >= x1):
            maiorx = x2
        else:
            maiorx = x3
        
        
        dx1 = self.rvan*np.cos(self.radiano_van) 
        dy1 = self.rvan*np.sin(self.radiano_van)
        dx2 = self.rvbn*np.cos(self.radiano_vbn)
        dy2 = self.rvbn*np.sin(self.radiano_vbn)
        dx3 = self.rvcn*np.cos(self.radiano_vcn)
        dy3 = self.rvcn*np.sin(self.radiano_vcn)

        plt.figure()
        plt.title("Tensões de Fase na Carga")
        plt.quiver(0, 0, dx1, dy1, scale=1, color='r', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx2, dy2, scale=1, color='b', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx3, dy3, scale=1, color='g', angles='xy', scale_units='xy')
        plt.axis([-2*maiorx, 2*maiorx, -2*maiorx, 2*maiorx])
        plt.xlabel('Eixo Real')
        plt.ylabel('Eixo Imaginário')
        plt.grid()
        plt.show()


    def d(self):
        self.calc()

        popup_windowd = Toplevel()
        popup_windowd.geometry("700x300")
        popup_windowd.resizable(False, False)
        popup_windowd.title("TENSÕES DE LINHA!!")

        popup_label7 = Label(popup_windowd, text="LETRA D- \n\nTensão de linha na carga V_AB em forma de fasor: {} < {} [V]".format(round(self.rvab,3), round(self.graus_vab,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label8 = Label(popup_windowd, text="\nTensão de linha na carga V_BC em forma de fasor: {} < {}[V]".format(round(self.rvbc,3), round(self.graus_vbc,3)), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label9 = Label(popup_windowd, text="\nTensão de linha na carga V_CA em forma de fasor: {} < {}[V]".format(round(self.rvca,3), round(self.graus_vca,3) ), fg = '#000000', font = ('arial', 14, 'bold'))
        popup_label7.pack()
        popup_label8.pack()
        popup_label9.pack()

        x1 = self.rvab
        x2 = self.rvbc
        x3 = self.rvca

        maiorx = 0

        if (x1 >= x2 and x1 >=x3):
            maiorx = x1
        elif (x2 >= x3 and x2 >= x1):
            maiorx = x2
        else:
            maiorx = x3
        
        
        dx1 = self.rvab*np.cos(self.radiano_vab) 
        dy1 = self.rvab*np.sin(self.radiano_vab)
        dx2 = self.rvbc*np.cos(self.radiano_vbc)
        dy2 = self.rvbc*np.sin(self.radiano_vbc)
        dx3 = self.rvca*np.cos(self.radiano_vca)
        dy3 = self.rvca*np.sin(self.radiano_vca)

        plt.figure()
        plt.title("Tensões de Linha na Carga")
        plt.quiver(0, 0, dx1, dy1, scale=1, color='r', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx2, dy2, scale=1, color='b', angles='xy', scale_units='xy')
        plt.quiver(0, 0, dx3, dy3, scale=1, color='g', angles='xy', scale_units='xy')
        plt.axis([-2*maiorx, 2*maiorx, -2*maiorx, 2*maiorx])
        plt.xlabel('Eixo Real')
        plt.ylabel('Eixo Imaginário')
        plt.grid()
        plt.show()


    def quit(self): 
        self.root.destroy()
    
    def link1(self):
        webbrowser.open('https://github.com/edworId') # TO OPEN A LINK IN YOUR BROWSER
    
    def link2(self):
            webbrowser.open('https://drive.google.com/file/d/1WtyukrHdZWSFyNTVaE4UGU779DlJXCs7/view?usp=sharing') # TO OPEN A LINK IN YOUR BROWSER


class Application(functions):
    def __init__(self):
        self.root = root #PRECISA DO ROOT POIS NÃO ESTÁ DENTRO DA CLASSE
        self.tela() #PRECISA CHAMAR ANTES DO LOOP A FUNÇÃO TEAL
        self.labels()
        self.buttons()
        self.menu()
        root.mainloop() #LOOP TELA

    def tela(self):
        self.root.title("Sistema trifásico Estrela-Estrela com Neutro") #TITLE
        self.root.geometry("1200x450") #SETAR TAMANHO INICIAL
        self.bg = PhotoImage(file = "est_est.png")
        self.bground = Label(self.root, image = self.bg, bd = 0)
        self.bground.place(relx = 0, rely = 0)
        self.root.resizable(False, False) #RESPONSIVIDADE DO TAMANHO DE TELA

    def labels(self):

        ## DADOS
        self.lb_dados = Label(self.root, text = "DADOS:", fg = '#6B6767', font = ('arial', 14, 'bold'))
        self.lb_dados.place(relx = 0.84, rely = 0.01)


        # Za
        self.lb_za = Label(self.root, text = "Za  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_za.place(relx = 0.8, rely = 0.1)

        self.za_entry = Entry(self.root)
        self.za_entry.place(relx = 0.85, rely = 0.1, relwidth = 0.1)

        # Zb
        self.lb_zb = Label(self.root, text = "Zb  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_zb.place(relx = 0.8, rely = 0.2)

        self.zb_entry = Entry(self.root)
        self.zb_entry.place(relx = 0.85, rely = 0.2, relwidth = 0.1)

        # Zc
        self.lb_zc = Label(self.root, text = "Zc  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_zc.place(relx = 0.8, rely = 0.3)

        self.zc_entry = Entry(self.root)
        self.zc_entry.place(relx = 0.85, rely = 0.3, relwidth = 0.1)

        # Zcabo
        self.lb_zcabo = Label(self.root, text = "Zcabo ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_zcabo.place(relx = 0.8, rely = 0.4)

        self.zcabo_entry = Entry(self.root)
        self.zcabo_entry.place(relx = 0.85, rely = 0.4, relwidth = 0.1)

        # VAN
        self.lb_VAN = Label(self.root, text = "VAN  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_VAN.place(relx = 0.8, rely = 0.5)

        self.VANr_entry = Entry(self.root)
        self.VANr_entry.place(relx = 0.85, rely = 0.5, relwidth = 0.05)
        self.VANf_entry = Entry(self.root)
        self.VANf_entry.place(relx = 0.92, rely = 0.5, relwidth = 0.05)

        # VBN
        self.lb_VBN = Label(self.root, text = "VBN  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_VBN.place(relx = 0.80, rely = 0.6)

        self.VBNr_entry = Entry(self.root)
        self.VBNr_entry.place(relx = 0.85, rely = 0.6, relwidth = 0.05)
        self.VBNf_entry = Entry(self.root)
        self.VBNf_entry.place(relx = 0.92, rely = 0.6, relwidth = 0.05)

        # VCN
        self.lb_VCN = Label(self.root, text = "VCN  ", fg = "#6B6767", font = ('arial', 10, 'bold'))
        self.lb_VCN.place(relx = 0.8, rely = 0.7)

        self.VCNr_entry = Entry(self.root)
        self.VCNr_entry.place(relx = 0.85, rely = 0.7, relwidth = 0.05)
        self.VCNf_entry = Entry(self.root)
        self.VCNf_entry.place(relx = 0.92, rely = 0.7, relwidth = 0.05)



    def buttons(self):
        self.bt_calc = Button(self.root, text = "Corrente de Neutro", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.a)
        self.bt_calc.place(relx = 0.745, rely = 0.78, relwidth = 0.12, relheight = 0.06)

        self.bt_calc = Button(self.root, text = "Correntes de Linha", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.b)
        self.bt_calc.place(relx = 0.875, rely = 0.78, relwidth = 0.12, relheight = 0.06)

        self.bt_calc = Button(self.root, text = "Tensões de Fase", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.c)
        self.bt_calc.place(relx = 0.745, rely = 0.85, relwidth = 0.12, relheight = 0.06)

        self.bt_calc = Button(self.root, text = "Tensões de Linha", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.d)
        self.bt_calc.place(relx = 0.875, rely = 0.85, relwidth = 0.12, relheight = 0.06)

        self.bt_sair = Button(self.root, text = "Apagar", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.clear)
        self.bt_sair.place(relx = 0.8, rely = 0.93, relwidth = 0.06, relheight = 0.06)
        
        self.bt_sair = Button(self.root, text = "Sair", bd = 4, bg = "#6B6767", fg = "#FFFFFF", font = ('arial', 10, 'bold'), command = self.quit)
        self.bt_sair.place(relx = 0.9, rely = 0.93, relwidth = 0.06, relheight = 0.06)
        

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file1 = Menu(menubar)
        file2 = Menu(menubar)
        

        menubar.add_cascade(label = "Options", menu = file1)
        menubar.add_cascade(label = "About", menu = file2)

        file1.add_command(label = "GitHub Edworld", command = self.link1)
        file2.add_command(label = "Robba's example", command = self.link2)
    

Application()


# VALORES DAS QUESTÕES DO LIVRO

# 20+0j
# 0+10j
# 0-10j
# 0.5+2j
# 220+0j
# -110-190.52j
# -110+190.52j
