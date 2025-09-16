Perfeito! 😎
Vou te passar uma **versão final do assistente de voz totalmente em Python**, que não depende de softwares externos para controlar **volume, abrir/fechar programas e sites, além de comandos do Windows**.

Ela usa a biblioteca **`pycaw`** para controlar o volume do sistema diretamente via Python, sem precisar do `nircmd`.

---

### **Passo 1 – Instalar bibliotecas necessárias**

No terminal do VSCode (ou prompt de comando):

```bash
pip install SpeechRecognition pyttsx3 psutil pycaw comtypes
pip install pyaudio
```

> ⚠️ Se `pyaudio` der erro no Windows, baixe o `.whl` compatível:
> [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
> Depois instale:

```bash
pip install PyAudio‑<versão>‑cp<versão_python>-cp<versão_python>-win_amd64.whl
```

---

### **Código Python – Assistente de Voz Final**

```python
import speech_recognition as sr
import pyttsx3
import subprocess
import psutil
import webbrowser
import os
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Inicializa voz
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo... fale o comando:")
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        falar("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        falar("Erro ao acessar o serviço de reconhecimento.")
        return ""

# --- Funções ---
def abrir_programa(nome_programa, caminho):
    try:
        subprocess.Popen([caminho])
        falar(f"Abrindo {nome_programa}")
    except Exception as e:
        falar("Não consegui abrir o programa.")
        print(e)

def fechar_programa(nome_processo):
    for proc in psutil.process_iter(['pid', 'name']):
        if nome_processo.lower() in proc.info['name'].lower():
            psutil.Process(proc.info['pid']).terminate()
            falar(f"Fechando {nome_processo}")
            return
    falar(f"Programa {nome_processo} não está em execução.")

# Controle de volume com Pycaw
def alterar_volume(valor):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # valor em -65.25 (mudo) até 0.0 (100%)
    if valor == "aumentar":
        volume.SetMasterVolumeLevelScalar(min(volume.GetMasterVolumeLevelScalar() + 0.1, 1.0), None)
    elif valor == "diminuir":
        volume.SetMasterVolumeLevelScalar(max(volume.GetMasterVolumeLevelScalar() - 0.1, 0.0), None)
    falar(f"Volume {valor}")

# Comandos Windows
def desligar_pc():
    falar("Desligando o computador...")
    os.system("shutdown /s /t 5")

def reiniciar_pc():
    falar("Reiniciando o computador...")
    os.system("shutdown /r /t 5")

def abrir_configuracoes():
    falar("Abrindo configurações do Windows")
    subprocess.Popen(["start", "ms-settings:"], shell=True)

# --- Programas ---
programas = {
    "bloco de notas": r"C:\Windows\System32\notepad.exe",
    "calculadora": r"C:\Windows\System32\calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe"
}

# --- Sites ---
sites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "netflix": "https://www.netflix.com",
    "globo": "https://www.globo.com"
}

# --- Loop principal ---
while True:
    comando = ouvir_comando()

    # Abrir sites/programas
    if "abrir" in comando:
        aberto = False

        # Abrir site com navegador específico
        if "site" in comando:
            for nome, url in sites.items():
                if nome in comando:
                    if "chrome" in comando:
                        webbrowser.get(programas["chrome"]).open(url)
                        falar(f"Abrindo {nome} no Chrome")
                    elif "edge" in comando:
                        webbrowser.get(programas["edge"]).open(url)
                        falar(f"Abrindo {nome} no Edge")
                    elif "firefox" in comando:
                        webbrowser.get(programas["firefox"]).open(url)
                        falar(f"Abrindo {nome} no Firefox")
                    else:
                        webbrowser.open(url)
                        falar(f"Abrindo {nome} no navegador padrão")
                    aberto = True
                    break

        # Abrir programa
        if not aberto:
            for nome, caminho in programas.items():
                if nome in comando:
                    abrir_programa(nome, caminho)
                    aberto = True
                    break

        # Abrir site sem navegador específico
        if not aberto:
            for nome, url in sites.items():
                if nome in comando:
                    webbrowser.open(url)
                    falar(f"Abrindo {nome}")
                    aberto = True
                    break

        if not aberto:
            falar("Não reconheci o programa ou site que você pediu.")

    # Fechar programas
    elif "fechar" in comando:
        fechado = False
        for nome in programas.keys():
            if nome in comando:
                fechar_programa(nome)
                fechado = True
                break
        if not fechado:
            falar("Não reconheci o programa para fechar.")

    # Comandos de volume
    elif "aumentar volume" in comando:
        alterar_volume("aumentar")
    elif "diminuir volume" in comando:
        alterar_volume("diminuir")

    # Comandos Windows
    elif "desligar" in comando:
        desligar_pc()
    elif "reiniciar" in comando:
        reiniciar_pc()
    elif "abrir configurações" in comando:
        abrir_configuracoes()

    # Encerrar assistente
    elif "sair" in comando or "encerrar" in comando:
        falar("Encerrando o assistente. Até mais!")
        break
```

---

### ✅ Funcionalidades do assistente final:

1. **Abrir e fechar programas**: Bloco de Notas, Calculadora, Chrome, Edge, Firefox
2. **Abrir sites**: com ou sem navegador específico (ex.: “Abrir YouTube no Chrome”)
3. **Controle de volume**: “Aumentar volume” / “Diminuir volume”
4. **Comandos do Windows**: Desligar, Reiniciar, Abrir Configurações
5. **Encerrar o assistente**: “Sair” ou “Encerrar”
6. Totalmente **Python**, sem softwares externos adicionais

---

Se quiser, posso te enviar também **uma lista completa de comandos de voz sugeridos**, pronta para treinar o uso diário do assistente, incluindo atalhos do Windows, navegação em sites e controle de multimídia.

Quer que eu faça isso?
---

