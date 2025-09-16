import speech_recognition as sr
import pyttsx3
import subprocess
import psutil
import webbrowser

# Inicializa o motor de voz
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

# Programas instalados (ajuste caminhos conforme seu PC)
programas = {
    "bloco de notas": r"C:\Windows\System32\notepad.exe",
    "calculadora": r"C:\Windows\System32\calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe"
}

# Sites favoritos
sites = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "netflix": "https://www.netflix.com",
    "globo": "https://www.globo.com"
}

while True:
    comando = ouvir_comando()

    # --- ABRIR PROGRAMAS ---
    if "abrir" in comando:
        aberto = False

        # Caso: "abrir site do X no navegador Y"
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

        # Caso: "abrir programa"
        if not aberto:
            for nome, caminho in programas.items():
                if nome in comando:
                    abrir_programa(nome, caminho)
                    aberto = True
                    break

        # Caso: "abrir site simples" (sem navegador especificado)
        if not aberto:
            for nome, url in sites.items():
                if nome in comando:
                    webbrowser.open(url)
                    falar(f"Abrindo {nome}")
                    aberto = True
                    break

        if not aberto:
            falar("Não reconheci o programa ou site que você pediu.")

    # --- FECHAR PROGRAMAS ---
    elif "fechar" in comando:
        fechado = False
        for nome in programas.keys():
            if nome in comando:
                fechar_programa(nome)
                fechado = True
                break
        if not fechado:
            falar("Não reconheci o programa para fechar.")

    # --- SAIR DO ASSISTENTE ---
    elif "sair" in comando or "encerrar" in comando:
        falar("Encerrando o assistente. Até mais!")
        break

