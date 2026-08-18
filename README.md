# 🦊 Cryptopyfox – A Raposa da Criptografia

**Cryptopyfox** é uma ferramenta interativa de linha de comando para criptografar e descriptografar arquivos e textos utilizando o algoritmo **Fernet** (criptografia simétrica) da biblioteca `cryptography`. Com uma interface divertida e efeitos visuais no terminal, ela foi criada para facilitar o uso da criptografia no dia a dia, seja para proteger dados sensíveis ou para aprender sobre criptografia de forma prática.

---

## 📑 Índice

- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
  - [Dependências Python](#dependências-python)
  - [Efeitos visuais (opcionais)](#efeitos-visuais-opcionais)
- [Como Usar](#-como-usar)
- [Opções Disponíveis](#-opções-disponíveis)
- [Sobre o Fernet](#-sobre-o-fernet)
- [Funcionamento Interno](#-funcionamento-interno)
- [Segurança e Boas Práticas](#-segurança-e-boas-práticas)
- [Possíveis Erros e Soluções](#-possíveis-erros-e-soluções)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Autor](#-autor)

---

## 📋 Requisitos

- **Python 3.6** ou superior (recomendado Python 3.8+)
- **Biblioteca `Fernet`** (instalada via pip)
- **(Opcional)** Programas para efeitos visuais:
  - `figlet` – para gerar banners ASCII
  - `lolcat` – para colorir a saída
  - `cowsay` – para exibir mensagens com uma vaquinha (ou raposa)

> Os efeitos visuais são chamados via `os.system`. Se os programas não estiverem instalados, o terminal exibirá erros, mas a funcionalidade principal **continua funcionando normalmente**.

---

## ⚙️ Instalação

### 1. Clone ou baixe o repositório

```bash
git clone https://github.com/seu-usuario/cryptopyfox.git
cd cryptopyfox
```

### 2. Instale a dependência Python

```bash
pip install Fernet
```

> Se estiver usando um ambiente virtual, ative-o antes.

### 3. (Opcional) Instale os programas para efeitos visuais

Os comandos abaixo variam conforme a distribuição Linux. Escolha o que se aplica ao seu sistema:

| Distribuição            | Comando de instalação                                      |
|-------------------------|------------------------------------------------------------|
| **Ubuntu / Debian**     | `sudo apt install figlet lolcat cowsay`                    |
| **Fedora / RHEL**       | `sudo dnf install figlet lolcat cowsay`                    |
| **Arch Linux**          | `sudo pacman -S figlet lolcat cowsay`                      |
| **openSUSE**            | `sudo zypper install figlet lolcat cowsay`                 |
| **Alpine Linux**        | `apk add figlet lolcat cowsay` (verifique disponibilidade) |
| **macOS (Homebrew)**    | `brew install figlet lolcat cowsay`                        |
| **Windows**             | Instale via [Chocolatey](https://chocolatey.org/) ou [Scoop](https://scoop.sh/): <br> `choco install figlet cowsay` (lolcat pode não estar disponível) |

Se algum pacote não estiver disponível para sua distribuição, você pode ignorar a instalação – a ferramenta funcionará sem os efeitos.

---

## 🚀 Como Usar

Execute o script com Python:

```bash
python app.py
```

Ao iniciar, você verá uma tela de boas‑vindas e deverá escolher uma das três opções para definir a **chave de criptografia**:

1. **Importar uma chave existente** – Cole a chave (em formato `bytes`) que você já possui.
2. **Gerar uma nova chave** – O programa gera uma chave aleatória e a exibe na tela (**guarde‑a com segurança!**).
3. **Usar a chave padrão** – Utiliza a chave armazenada no arquivo `chave.key` (deve existir no mesmo diretório).

Após definir a chave, o programa entra em um loop principal com as opções descritas abaixo.

---

## 🧩 Opções Disponíveis

| Opção | Descrição |
|-------|-----------|
| **1** | Criptografa um texto digitado e salva o resultado no arquivo `crypt.txt` (sobrescreve). |
| **2** | Descriptografa o conteúdo do arquivo `crypt.txt` e exibe o texto original. |
| **3** | Criptografa um texto digitado e mostra o resultado criptografado na tela (não salva em arquivo). |
| **4** | Descriptografa um texto criptografado colado no terminal e exibe o original (pode apresentar erros com caracteres acentuados). |
| **5** | Criptografa um arquivo específico (informe o nome com extensão) – o arquivo é sobrescrito com o conteúdo criptografado. |
| **6** | Descriptografa um arquivo específico (informe o nome com extensão) – o arquivo é sobrescrito com o conteúdo original. |
| **7** | Cria um novo arquivo de texto com o nome informado, adiciona o conteúdo digitado e já o salva criptografado. |

> **Atenção:** As opções que envolvem arquivos (1, 2, 5, 6, 7) **sobrescrevem** os arquivos existentes sem aviso prévio. Utilize com cuidado.

### Exemplo prático

1. Inicie o programa e escolha a opção **2** para gerar uma nova chave.
2. Copie a chave exibida (ex.: `b'...'`) e guarde em um local seguro.
3. Escolha a opção **3** para criptografar um texto rapidamente. Digite `"Minha senha secreta"` e veja o resultado criptografado.
4. Para descriptografar, use a opção **4**, cole o texto criptografado e veja o original.

---

## 🔐 Sobre o Fernet

O **Fernet** é um esquema de criptografia simétrica fornecido pela biblioteca `Fernet` em Python. Ele garante:

- **Confidencialidade** – os dados são criptografados com AES-128 em modo CBC.
- **Integridade** – um HMAC com SHA-256 é usado para verificar se os dados não foram alterados.
- **Autenticidade** – a chave é necessária tanto para criptografar quanto para descriptografar, garantindo que apenas quem possui a chave possa acessar o conteúdo.

A chave gerada pelo Fernet é uma string de 32 bytes codificada em base64, o que a torna fácil de ser armazenada e compartilhada (com segurança). É uma escolha robusta para aplicações que exigem criptografia simétrica simples e segura.

---

## ⚙️ Funcionamento Interno

O script segue a seguinte lógica:

1. **Escolha da chave** – o usuário importa, gera ou usa a chave padrão.
2. **Criação do objeto `Fernet`** – a partir da chave, é criado um objeto que expõe os métodos `encrypt()` e `decrypt()`.
3. **Loop principal** – o usuário escolhe uma operação e o programa executa a ação correspondente:
   - Para textos, o conteúdo é codificado em UTF-8 antes de ser criptografado.
   - Para arquivos, o conteúdo binário é lido diretamente, criptografado e reescrito no mesmo arquivo.
   - A opção 7 cria um arquivo `.txt` e já o criptografa.

O código atual contém duplicação (as mesmas opções são repetidas três vezes), mas isso não afeta a funcionalidade – é apenas uma questão de refatoração futura.

---

## 🛡️ Segurança e Boas Práticas

- **Guarde a chave com segurança** – se perder a chave, os dados criptografados se tornam irrecuperáveis.
- **Use chaves diferentes para contextos diferentes** – não reutilize a mesma chave para múltiplos projetos.
- **Não compartilhe a chave publicamente** – ela é a única forma de descriptografar os dados.
- **Para dados altamente sensíveis**, considere usar criptografia assimétrica ou ferramentas especializadas (ex.: GPG).
- **O arquivo `chave.key`** – se usado, mantenha-o em um local com permissões restritas (ex.: `chmod 600`).

---

## 🐛 Possíveis Erros e Soluções

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: No module named 'cryptography'` | Instale a biblioteca com `pip install cryptography`. |
| Erro ao executar `figlet`, `lolcat` ou `cowsay` | Instale os programas ou ignore as mensagens – a funcionalidade principal não depende deles. |
| `InvalidToken` ao descriptografar | A chave usada é diferente da que criptografou o dado, ou o arquivo está corrompido. Verifique a chave e a integridade do arquivo. |
| `FileNotFoundError` ao ler `chave.key` | A opção 3 foi escolhida, mas o arquivo não existe. Gere uma nova chave (opção 2) e crie o arquivo. |
| A opção 7 cria arquivo com `.txt.txt` | O código atual adiciona `.txt` mesmo se o usuário já incluir a extensão. Para evitar, informe o nome **sem** extensão (ex.: `meu_arquivo`). |

---

## 🤝 Contribuição

Contribuições são bem‑vindas! Se você deseja melhorar o Cryptopyfox, siga os passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

Sugestões de melhorias:
- Refatorar o código para eliminar duplicação.
- Adicionar suporte a outros algoritmos (AES, RSA).
- Implementar uma interface gráfica (GUI).
- Permitir escolher o nome do arquivo de saída.
- Corrigir o bug da opção 7 (extensão duplicada).

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**. Sinta‑se à vontade para usar, modificar e distribuir.

---

## 👨‍💻 Autor

Desenvolvido por **Otavio OMG Dev**  
[GitHub](https://github.com/otavioomg) • [LinkedIn](https://linkedin.com/in/otavioomgdev)

---

## 🙏 Agradecimentos

- À biblioteca `cryptography` por fornecer uma implementação robusta e fácil de usar do Fernet.
- Aos criadores do `figlet`, `lolcat` e `cowsay` por tornarem o terminal mais divertido.

---

**Divirta‑se criptografando com a raposa!** 🦊🔐
