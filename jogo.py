import tkinter as tk
import random

enigmas = [
    {"pergunta": "Quanto mais você tira, maior fica?", "resposta": "buraco"},
    {"pergunta": "Tem dentes, mas não morde?", "resposta": "pente"},
    {"pergunta": "Sobe e desce, mas não sai do lugar?", "resposta": "escada"},
    {"pergunta": "Anda sem pernas e chora sem olhos?", "resposta": "nuvem"}
]

random.shuffle(enigmas)

class Jogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Enigmas 🧠")
        self.root.geometry("600x450")
        self.root.configure(bg="#121212")

        self.indice = 0
        self.pontos = 0

        self.frame = tk.Frame(root, bg="#121212")
        self.frame.pack(expand=True)

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        titulo = tk.Label(self.frame, text="🧩 JOGO DE ENIGMAS",
                          font=("Arial", 26, "bold"),
                          fg="#00ffcc", bg="#121212")
        titulo.pack(pady=30)

        botao = tk.Button(self.frame, text="INICIAR",
                          font=("Arial", 18, "bold"),
                          bg="#00ffcc", fg="black")
        botao.config(command=self.tela_jogo)
        botao.pack(pady=30)

    def tela_jogo(self):
        self.limpar_tela()

        self.pergunta_label = tk.Label(
            self.frame,
            text=enigmas[self.indice]["pergunta"],
            font=("Arial", 18),
            wraplength=500,
            fg="white",
            bg="#121212"
        )
        self.pergunta_label.pack(pady=25)

        self.entry = tk.Entry(self.frame, font=("Arial", 16))
        self.entry.pack(pady=15)

        self.feedback = tk.Label(self.frame, text="",
                                 font=("Arial", 16, "bold"),
                                 bg="#121212")
        self.feedback.pack(pady=10)

        botao = tk.Button(self.frame, text="RESPONDER",
                          font=("Arial", 16, "bold"),
                          command=self.verificar,
                          bg="#00ffcc", fg="black")
        botao.pack(pady=15)

        self.pontos_label = tk.Label(
            self.frame,
            text=f"Pontos: {self.pontos}",
            font=("Arial", 14),
            fg="lightgray",
            bg="#121212"
        )
        self.pontos_label.pack()

    def verificar(self):
        resposta = self.entry.get().lower().strip()
        correta = enigmas[self.indice]["resposta"]

        if resposta == correta:
            self.pontos += 1
            self.feedback.config(text="✔️ ACERTOU!", fg="green")
        else:
            self.feedback.config(text=f"❌ ERA: {correta}", fg="red")

        self.pontos_label.config(text=f"Pontos: {self.pontos}")

        self.indice += 1
        self.root.after(1500, self.proximo)

    def proximo(self):
        if self.indice < len(enigmas):
            self.tela_jogo()
        else:
            self.fim()

    def fim(self):
        self.limpar_tela()

        msg = tk.Label(self.frame,
                       text=f"FIM DE JOGO!\nPontuação: {self.pontos}",
                       font=("Arial", 20, "bold"),
                       fg="#00ffcc",
                       bg="#121212")
        msg.pack(pady=30)

        botao = tk.Button(self.frame, text="JOGAR NOVAMENTE",
                          font=("Arial", 16, "bold"),
                          command=self.reiniciar,
                          bg="#00ffcc", fg="black")
        botao.pack(pady=20)

    def reiniciar(self):
        self.indice = 0
        self.pontos = 0
        random.shuffle(enigmas)
        self.tela_inicial()


root = tk.Tk()
app = Jogo(root)
root.mainloop()