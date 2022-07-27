from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.pyplot import text
from numpy import pad
from PIL import Image,ImageTk
import string 
import random



cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul


janela=Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor2)

frame_cima=Frame(janela,width=295,height=50,bg=cor2,pady=0,padx=0,relief='flat')
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo=Frame(janela,width=280,height=310,bg=cor2,pady=0,padx=0,relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW)

estilo=ttk.Style(janela)
estilo.theme_use('clam')

#frame-cima

imagem=Image.open('senha.png')
imagem=imagem.resize((30,30),Image.ANTIALIAS)
imagem=ImageTk.PhotoImage(imagem)

app_logo=Label(frame_cima,height=60,image=imagem,compound=LEFT, padx=10,bg=cor2,relief='flat',anchor='nw')
app_logo.place(x=2,y=0)

app_nome=Label(frame_cima,text='GERADOR DE SENHAS',height=1,width=20,font=('Ivy 16 bold'),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_nome.place(x=35,y=2)

app_linha=Label(frame_cima,height=1,width=295,font=('Ivy 1'),padx=0,bg=cor4,fg=cor1,relief='flat',anchor='nw')
app_linha.place(x=0,y=35)


#funcao gerar senha
def criar_senha():
    alfabeto_maior=string.ascii_uppercase
    alfabeto_menor=string.ascii_lowercase
    numeros='123456789'
    simbolos='[]@{}$*&!,_-+;'
    
    global combinar
    
    
    #condicao maiuscula
    
    if estado_1.get()== alfabeto_maior:
        combinar=alfabeto_maior
    else:
        pass
    
     #condicao minuscula
        
    if estado_2.get()== alfabeto_menor:
        combinar=combinar + alfabeto_menor
    else:
        pass 
    
     #numeros
        
    if estado_3.get()== numeros:
        combinar=combinar + numeros
    else:
        pass 
        
     #condicao minuscula
        
    if estado_4.get()== simbolos:
        combinar=combinar + simbolos
    else:
        pass 
        
        
    comprimento=int(spin.get())
    senha="".join(random.sample(combinar, comprimento))
    
    app_senha['text']=senha
    
    def copiar_senha():
        info=senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)
        
        messagebox.showinfo("Sucesso","A Senha foi copiada com sucesso!") 
    buton_copiar=Button(frame_baixo,command=copiar_senha,text='Copiar',width=7 ,height=2,font=('Ivy 10 bold'),bg=cor2,fg=cor1,relief='raised',overrelief='solid',anchor='center')
    buton_copiar.grid(row=0,column=1,sticky=NW,padx=5,pady=7,columnspan=1)


#frame-baixo

app_senha=Label(frame_baixo,text='- - -',height=2,width=25,font=('Ivy 10 bold'),padx=0,bg=cor2,fg=cor1,relief='solid',anchor='center')
app_senha.grid(row=0,column=0,columnspan=1,sticky=NSEW,padx=3,pady=10)

app_info=Label(frame_baixo,text='Número total de caracteres na senha',height=1,font=('Ivy 10 bold'),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_info.grid(row=1,column=0,columnspan=2,sticky=NSEW,padx=5,pady=1)


var=IntVar()
var.set(8)
spin=Spinbox(frame_baixo,from_=0,to=20,width=5,textvariable=var)
spin.grid(row=2,column=0,columnspan=2,sticky=NW,padx=5,pady=8)

alfabeto_maior=string.ascii_uppercase
alfabeto_menor=string.ascii_lowercase
numeros='123456789'
simbolos='[]@{}$*&!,_-+;'


frame_carecteres=Frame(frame_baixo,width=295,height=210,bg=cor2,pady=0,padx=0,relief='flat')
frame_carecteres.grid(row=3,column=0,sticky=NSEW,columnspan=3)


#Letras Maiusculas
estado_1=StringVar()
estado_1.set(False)
check_1=Checkbutton(frame_carecteres,width=1,var=estado_1,onvalue=alfabeto_maior,offvalue='off',relief='flat',bg=cor2)
check_1.grid(row=0,column=0,sticky=NW,padx=2,pady=5)
app_maiusculas=Label(frame_carecteres,text='ABC Letras maiúsculas',height=1,font=('Ivy 10 '),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_maiusculas.grid(row=0,column=1,sticky=NW,padx=2,pady=5)


#Letras minusculas
estado_2=StringVar()
estado_2.set(False)
check_2=Checkbutton(frame_carecteres,width=1,var=estado_2,onvalue=alfabeto_menor,offvalue='off',relief='flat',bg=cor2)
check_2.grid(row=1,column=0,sticky=NW,padx=2,pady=5)
app_minusculas=Label(frame_carecteres,text='abc Letras minusculas',height=1,font=('Ivy 10 '),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_minusculas.grid(row=1,column=1,sticky=NW,padx=2,pady=5)


#numeros
estado_3=StringVar()
estado_3.set(False)
check_3=Checkbutton(frame_carecteres,width=1,var=estado_3,onvalue=numeros,offvalue='off',relief='flat',bg=cor2)
check_3.grid(row=2,column=0,sticky=NW,padx=2,pady=5)
app_numeros=Label(frame_carecteres,text='123 Números' ,height=1,font=('Ivy 10 '),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_numeros.grid(row=2,column=1,sticky=NW,padx=2,pady=5)


#simbolos
estado_4=StringVar()
estado_4.set(False)
check_4=Checkbutton(frame_carecteres,width=1,var=estado_4,onvalue=simbolos,offvalue='off',relief='flat',bg=cor2)
check_4.grid(row=3,column=0,sticky=NW,padx=2,pady=5)
app_simbolos=Label(frame_carecteres,text='!@# Símbolos' ,height=1,font=('Ivy 10 '),padx=0,bg=cor2,fg=cor1,relief='flat',anchor='nw')
app_simbolos.grid(row=3,column=1,sticky=NW,padx=2,pady=5)



#botao

buton_gerar_senha=Button(frame_carecteres,command=criar_senha,text='Gerar Senha',width=34 ,height=1,font=('Ivy 10 bold'),bg=cor4,fg=cor2,relief='flat',overrelief='solid',anchor='center')
buton_gerar_senha.grid(row=5,column=0,sticky=NSEW,padx=5,pady=11,columnspan=5)





janela.mainloop()