
from customtkinter import *
import time

indice_atual = 0
def flashcard1():
    global indice_atual
    palavra = lista_palavra[indice_atual]
    preencher = palavra[0] + "_ " * (len(palavra) - 1)
    enunciado.configure(text=f"Complete a palavra: {preencher}") 
    return preencher

def validar_tentativa():
    tentativa = textbox.get("0.0", "end").strip()
    palavra = lista_palavra[indice_atual]
    if tentativa.lower() == palavra.lower():
        feedback_label.configure(text="Parabéns! Você acertou!", text_color="green")
        janela.after(1000, proximo_flashcard)
    else:
        feedback_label.configure(text="errou, seu animal! tenta de novo seu bosta", text_color="red")
        enunciado.configure(text= f"Complete a palavra: {palavra[0] + "_ " * (len(palavra) - 1)}")
        

def proximo_flashcard():
    global indice_atual
    if indice_atual < len(lista_palavra):
        indice_atual += 1
        flashcard1()  # Atualiza o flashcard com a próxima palavra
        feedback_label.configure(text="")  # Limpa o feedback
        textbox.delete("0.0", "end")
    else:
        feedback_label.update(text="PARABÉNS SEU ANIMALZINHO! CONSEGUIU COMPLETAR O FLASHCARDS DA RESENHA", text_color = "yellow")
        textbox.configure(state="disabled")
        enunciado.configure(text="SAI DAQUI! VAI SEU COCÔZINHO")

janela = CTk()
janela.geometry("800x600")

label = CTkLabel(master=janela, text="Bem vindo ao Flashcard da resenha", font=("Calibri", 30), text_color="#FFFAFA")
label.place(relx=0.5, rely=0.08, anchor="center") 


enunciado = CTkLabel(master=janela, text="",font=("Calibri", 20), text_color="#FFFAFA")
enunciado.place(relx=0.5, rely=0.4, anchor="center") 


textbox = CTkTextbox(master=janela, corner_radius= 10, border_color="#FFFAFA", border_width=1, border_spacing =3, width=200, height=50, activate_scrollbars = False)
textbox.place(relx=0.5, rely=0.5, anchor="center") 

lista_palavra = ["Ovo", "Bash"]
flashcard1()

feedback_label = CTkLabel(master=janela,text="",font=("Calibri", 18),text_color="#FFFAFA")
feedback_label.place(relx=0.5, rely=0.7, anchor="center")


tn = CTkButton(master=janela, text="Enviar resposta", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", border_color="#FFCC70", border_width=2, command = validar_tentativa)
tn.place(relx=0.5, rely=0.8, anchor="center") 

janela.mainloop()





