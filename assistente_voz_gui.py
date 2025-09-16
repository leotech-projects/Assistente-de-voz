import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import speech_recognition as sr
import pyttsx3
import subprocess
import psutil
import webbrowser
import os
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# --- Inicialização do motor de voz ---
engine = pyttsx3.init()
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# --- Controle de volume ---
def alterar_volume(valor):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if valor == "aumentar":
        volume.SetMasterVolumeLevelScalar(min(volume.GetMasterVolumeLevelScalar() + 0.1, 1.0), None)
    elif valor == "diminuir":
        volume.SetMasterVolumeLevelScalar(max(volume.GetMasterVolumeLevelScalar() - 0.1, 0.0), None)
    falar(f"Volume {valor}")
    log_area.insert(tk.END, f"Volume {valor}\n")
    log_area.see(tk.END)

# --- Comandos Windows ---
def desligar_pc():
    falar("Desligando o computador...")
    log_area.insert(tk.END, "Desligando computador...\n")
    log_area.see(tk.END)
    os.system("shutdown /s /t 5")

def reiniciar_pc():
    falar("Reiniciando o computador...")
    log_area.insert(tk.END, "Reiniciando computador...\n")
    log_area.see(tk.END)
    os.system("shutdown /r /t 5")

def abrir_configuracoes():
    falar("Abrindo configurações do Windows")
    log_area.insert(tk.END, "Abrindo Configurações...\n")
    log_area.see(tk.END)
    subprocess.Popen(["start", "ms-settings:"], shell=True)

def abrir_explorer():
    falar("Abrindo Explorer")
    log_area.insert(tk.END, "Abrindo Explorer...\n")
    log_area.see(tk.END)
    subprocess.Popen(["explorer"])

def print_screen():
    falar("Capturando tela")
    log_area.insert(tk.END, "Capturando tela...\n")
    log_area.see(tk.END)
    subprocess.Popen(["snippingtool"])

# --- Programas instalados ---
programas = {
    "Bloco de Notas": r"C:\Windows\System32\notepad.exe",
    "Calculadora": r"C:\Windows\System32\calc.exe",
    "Chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "Edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "Firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "VLC": r"C:\Program Files\VideoLAN\VLC\vlc.exe"
}

# --- Sites ---
sites = {
    "YouTube": "https://www.youtube.com",
    "Google": "https://www.google.com",
    "Gmail": "https://mail.google.com",
    "GitHub": "https://github.com",
    "Netflix": "https://www.netflix.com",
    "Globo": "https://www.globo.com"
}

# --- Funções para abrir/fechar programas ---
def abrir_programa(nome):
    caminho = programas.get(nome)
    if caminho:
        subprocess.Popen([caminho])
        falar(f"Abrindo {nome}")
        log_area.insert(tk.END, f"Abrindo {nome}\n")
        log_area.see(tk.END)
    else:
        log_area.insert(tk.END, f"Programa {nome} não encontrado.\n")
        log_area.see(tk.END)

def fechar_programa(nome):
    for proc in psutil.process_iter(['pid','name']):
        if nome.lower() in proc.info['name'].lower():
            psutil.Process(proc.info['pid']).terminate()
            falar(f"Fechando {nome}")
            log_area.insert(tk.END, f"Fechando {nome}\n")
            log_area.see(tk.END)
            return
    log_area.insert(tk.END, f"Programa {nome} não está em execução\n")
    log_area.see(tk.END)

# --- Função para ouvir comandos ---
def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        log_area.insert(tk.END, "🎤 Ouvindo...\n")
        log_area.see(tk.END)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR").lower()
        log_area.insert(tk.END, f"Você disse: {comando}\n")
        log_area.see(tk.END)
        processar_comando(comando)
    except sr.UnknownValueError:
        falar("Não entendi o que você disse")
        log_area.insert(tk.END, "Não entendi o comando\n")
        log_area.see(tk.END)
    except sr.RequestError:
        falar("Erro ao acessar serviço de reconhecimento")
        log_area.insert(tk.END, "Erro no serviço de reconhecimento\n")
        log_area.see(tk.END)

# --- Processamento de comandos ---
def processar_comando(comando):
    # Abrir programas
    for nome in programas.keys():
        if f"abrir {nome.lower()}" in comando:
            abrir_programa(nome)
            return
        if f"fechar {nome.lower()}" in comando:
            fechar_programa(nome)
            return
    # Abrir sites
    if "abrir" in comando:
        for nome, url in sites.items():
            if nome.lower() in comando:
                webbrowser.open(url)
                falar(f"Abrindo {nome}")
                log_area.insert(tk.END, f"Abrindo {nome}\n")
                log_area.see(tk.END)
                return
    # Comandos Windows
    if "desligar" in comando:
        desligar_pc()
    elif "reiniciar" in comando:
        reiniciar_pc()
    elif "abrir configurações" in comando:
        abrir_configuracoes()
    elif "abrir explorer" in comando:
        abrir_explorer()
    elif "print screen" in comando or "capturar tela" in comando:
        print_screen()
    # Volume
    elif "aumentar volume" in comando:
        alterar_volume("aumentar")
    elif "diminuir volume" in comando:
        alterar_volume("diminuir")
    # Encerrar assistente
    elif "sair" in comando or "encerrar" in comando:
        falar("Encerrando assistente")
        root.destroy()
    else:
        falar("Comando não reconhecido")
        log_area.insert(tk.END, "Comando não reconhecido\n")
        log_area.see(tk.END)

def iniciar_assistente():
    threading.Thread(target=ouvir_comando).start()

# --- Criando GUI avançada ---
root = tk.Tk()
root.title("Assistente de Voz – Painel de Controle")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

# Título
titulo = tk.Label(root, text="🎙 Assistente de Voz", font=("Arial", 20, "bold"), bg="#1e1e1e", fg="white")
titulo.pack(pady=10)

# Botões de controle rápido
frame_botoes = tk.Frame(root, bg="#1e1e1e")
frame_botoes.pack(pady=5)

btn_falar = tk.Button(frame_botoes, text="🎤 Falar", command=iniciar_assistente, font=("Arial",14), bg="#4CAF50", fg="white", width=12)
btn_falar.grid(row=0, column=0, padx=5, pady=5)

btn_volume_up = tk.Button(frame_botoes, text="🔊 Aumentar Volume", command=lambda: alterar_volume("aumentar"), font=("Arial",12), bg="#2196F3", fg="white")
btn_volume_up.grid(row=0, column=1, padx=5, pady=5)

btn_volume_down = tk.Button(frame_botoes, text="🔉 Diminuir Volume", command=lambda: alterar_volume("diminuir"), font=("Arial",12), bg="#2196F3", fg="white")
btn_volume_down.grid(row=0, column=2, padx=5, pady=5)

btn_desligar = tk.Button(frame_botoes, text="⏻ Desligar", command=desligar_pc, font=("Arial",12), bg="#f44336", fg="white")
btn_desligar.grid(row=1, column=0, padx=5, pady=5)

btn_reiniciar = tk.Button(frame_botoes, text="🔄 Reiniciar", command=reiniciar_pc, font=("Arial",12), bg="#f44336", fg="white")
btn_reiniciar.grid(row=1, column=1, padx=5, pady=5)

btn_config = tk.Button(frame_botoes, text="⚙ Abrir Configurações", command=abrir_configuracoes, font=("Arial",12), bg="#ff9800", fg="white")
btn_config.grid(row=1, column=2, padx=5, pady=5)

btn_explorer = tk.Button(frame_botoes, text="📁 Abrir Explorer", command=abrir_explorer, font=("Arial",12), bg="#9C27B0", fg="white")
btn_explorer.grid(row=2, column=0, padx=5, pady=5)

btn_print = tk.Button(frame_botoes, text="📸 Captura de Tela", command=print_screen, font=("Arial",12), bg="#795548", fg="white")
btn_print.grid(row=2, column=1, padx=5, pady=5)

btn_sair = tk.Button(frame_botoes, text="❌ Sair", command=root.destroy, font=("Arial",12), bg="#607D8B", fg="white")
btn_sair.grid(row=2, column=2, padx=5, pady=5)

# Área de log
log_area = scrolledtext.ScrolledText(root, width=80, height=20, bg="#333333", fg="white", font=("Consolas",12))
log_area.pack(padx=10, pady=10)

root.mainloop()
