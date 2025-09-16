# Assistente de Voz em Python – Controle Completo do PC

![Banner do Assistente](imagens/banner_assistente.png)
*Controle seu PC usando apenas a voz!*

---

## ✅ Descrição do Projeto

Este projeto implementa um **assistente de voz completo em Python** capaz de:

* Abrir e fechar **programas instalados**
* Abrir **sites** em qualquer navegador
* Controlar o **volume do sistema**
* Executar **comandos do Windows**: desligar, reiniciar, abrir configurações e Explorer
* Capturar a tela (**Print Screen**)
* Encerrar o assistente por voz

Ele utiliza **reconhecimento de voz** e **síntese de voz** para interação natural.

---

## 🎯 Funcionalidades

| Categoria           | Comandos de Voz                                                                        |
| ------------------- | -------------------------------------------------------------------------------------- |
| Abrir Programas     | “Abrir Chrome”, “Abrir Bloco de Notas”, “Abrir VLC”                                    |
| Fechar Programas    | “Fechar Firefox”, “Fechar Calculadora”                                                 |
| Abrir Sites         | “Abrir YouTube”, “Abrir Gmail no Edge”                                                 |
| Controle de Volume  | “Aumentar volume”, “Diminuir volume”                                                   |
| Comandos do Windows | “Desligar computador”, “Reiniciar computador”, “Abrir Configurações”, “Abrir Explorer” |
| Captura de Tela     | “Print Screen”, “Capturar tela”                                                        |
| Encerrar Assistente | “Sair”, “Encerrar”                                                                     |

---

## 🛠 Pré-requisitos

* Python 3.7+
* Microfone funcional
* VSCode ou outro editor de código

---

## ⚡ Passo a Passo – Configuração no VSCode

### 1️⃣ Criar Projeto e Arquivo Python

1. Abra o VSCode.
2. Crie uma pasta para o projeto.
3. Crie o arquivo `assistente_voz.py` e cole o código do assistente.

![Criar arquivo Python](imagens/criar_arquivo.png)

---

### 2️⃣ Abrir Terminal no VSCode

* Pressione **Ctrl + \`** ou vá em **Terminal → Novo Terminal**

![Abrir terminal](imagens/terminal_vscode.png)

---

### 3️⃣ Criar e Ativar Ambiente Virtual (Opcional)

```bash
python -m venv venv
venv\Scripts\activate
```

> **Dica:** O ambiente virtual mantém as bibliotecas organizadas e isoladas.

![Ativar venv](imagens/ativar_venv.png)

---

### 4️⃣ Instalar Bibliotecas Necessárias

```bash
pip install SpeechRecognition pyttsx3 psutil pycaw comtypes
pip install pyaudio
```

> ⚠️ **Atenção Windows:** Se `pyaudio` der erro, baixe o `.whl` aqui: [PyAudio Windows](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
> Depois instale com:

```bash
pip install PyAudio‑<versão>.whl
```

![Instalar bibliotecas](imagens/instalar_bibliotecas.png)

---

### 5️⃣ Executar o Assistente

```bash
python assistente_voz.py
```

* O assistente ouvirá seus comandos de voz em tempo real.
* Exemplos:

  * Abrir programas: “Abrir Chrome”
  * Abrir sites: “Abrir YouTube no Firefox”
  * Controle de volume: “Aumentar volume”
  * Comandos Windows: “Desligar computador”
  * Captura de tela: “Print Screen”
  * Encerrar: “Sair”

![Assistente funcionando](imagens/assistente_funcionando.png)

---

## 💡 Dicas de Uso

* Fale próximo ao microfone e com clareza.
* Ajuste os caminhos dos programas no código conforme o seu PC.
* Expanda os dicionários de programas e sites para adicionar novos favoritos.
* Adicione mais comandos e atalhos personalizados conforme necessário.

---

Perfeito! 😎
Vou te passar uma **versão completa do projeto pronta para GitHub**, incluindo:

* **README ilustrado** com imagens e passo a passo
* **GIF demonstrativo** mostrando o assistente funcionando
* **Código do assistente com GUI avançada**
* **Instruções completas de instalação e execução**

Isso vai deixar seu repositório **profissional, didático e visualmente atraente**.

---

## Estrutura sugerida do repositório

```
assistente-voz/
│
├─ imagens/
│   ├─ banner.png
│   ├─ criar_arquivo.png
│   ├─ terminal_vscode.png
│   ├─ ativar_venv.png
│   ├─ instalar_bibliotecas.png
│   ├─ assistente_funcionando.gif
│
├─ assistente_voz_gui.py
├─ README.md
```

---

## README.md – Versão Profissional para GitHub

````markdown
# 🎙 Assistente de Voz em Python – Controle Completo do PC

![Banner](imagens/banner.png)

Controle seu computador usando apenas a sua voz! Abra programas, sites, controle o volume, capture telas e execute comandos do Windows.

---

## 🔹 Funcionalidades

- Abrir/Fechar Programas: Bloco de Notas, Calculadora, Chrome, Edge, Firefox, VLC  
- Abrir Sites: YouTube, Google, Gmail, GitHub, Netflix, Globo  
- Controle de Volume: Aumentar ou Diminuir  
- Comandos Windows: Desligar, Reiniciar, Abrir Configurações, Explorer  
- Captura de Tela: Print Screen / Snipping Tool  
- Encerrar Assistente por Voz  

![Assistente Funcionando](imagens/assistente_funcionando.gif)

---

## ⚡ Pré-requisitos

- Python 3.7 ou superior  
- Microfone funcional  
- VSCode ou outro editor de código  

---

## 🛠 Passo a Passo – Configuração

### 1️⃣ Criar projeto e arquivo Python
- Crie uma pasta para o projeto  
- Crie o arquivo `assistente_voz_gui.py` e cole o código do assistente  

![Criar arquivo](imagens/criar_arquivo.png)

---

### 2️⃣ Abrir terminal no VSCode
- Pressione **Ctrl + `** ou vá em **Terminal → Novo Terminal**  

![Abrir terminal](imagens/terminal_vscode.png)

---

### 3️⃣ Criar e ativar ambiente virtual (opcional)
```bash
python -m venv venv
venv\Scripts\activate
````

![Ativar venv](imagens/ativar_venv.png)

---

### 4️⃣ Instalar bibliotecas

```bash
pip install SpeechRecognition pyttsx3 psutil pycaw comtypes
pip install pyaudio
```

> ⚠️ Se `pyaudio` der erro, baixe o `.whl` compatível aqui: [PyAudio Windows](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
> Depois instale:

```bash
pip install PyAudio‑<versão>.whl
```

![Instalar bibliotecas](imagens/instalar_bibliotecas.png)

---

### 5️⃣ Executar o assistente

```bash
python assistente_voz_gui.py
```

* Clique em **🎤 Falar** ou use os botões para executar funções rapidamente
* Fale os comandos de voz conforme listado nas funcionalidades

---

## 💡 Dicas

* Fale próximo ao microfone e de forma clara
* Ajuste os caminhos dos programas no código conforme seu computador
* Expanda os dicionários de programas e sites para adicionar novos favoritos
* Adicione mais comandos e atalhos conforme necessário

---

## 🖼 Demonstração

![Assistente Funcionando](imagens/assistente_funcionando.gif)

---

## 🏷 Licença

Este projeto é gratuito e pode ser usado, modificado e distribuído livremente.

```

---

Se você quiser, posso **gerar também o GIF de demonstração já pronto**, com uma simulação mostrando a interface funcionando, para você colocar diretamente na pasta `imagens/` e deixar o repositório totalmente completo.  

Quer que eu faça isso?
```

