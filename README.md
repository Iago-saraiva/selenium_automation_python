💻 Sistema de Automação Web com Selenium

Olá! Este é um projeto de automação web que eu desenvolvi usando Selenium. Ele simula um usuário fazendo login em um sistema e extraindo dados de uma tabela — tudo automaticamente!
O que esse projeto faz?

Basicamente, o script Python:

    Abre uma página de login

    Preenche as credenciais e faz login

    Acessa uma página com uma tabela de dados

    Extrai todas as informações da tabela

    Salva tudo num arquivo CSV

Bem útil para automatizar aquelas tarefas repetitivas de copiar e colar dados de sites, né?
Tecnologias que usei

    Python

    Selenium (para controlar o navegador)

    HTML/CSS/JavaScript (as páginas web)

    ChromeDriver (o motor por trás da automação)

📂 Arquivos do projeto
text

.
├── app.py                 # Código principal da automação
├── index.html            # Página de login
├── home.html            # Página inicial
├── data-page.html       # Página com os dados
├── extracted_data.csv   # Dados que extraí
└── README.md           # Este arquivo que você está lendo

🚀 Como rodar na sua máquina

    Primeiro, instala o Selenium:

bash

pip install selenium

    Baixa o ChromeDriver e coloca no PATH do seu sistema

    Roda o script:

bash

python app.py

E pronto! O script vai abrir o navegador sozinho e fazer toda a mágica acontecer. 🎩✨
🔐 Credenciais de teste

Use essas credenciais para testar:

    Usuário: test_user

    Senha: secure_password

📊 Dados que extraio

A tabela tem essas informações:
ID	Nome	Email	Cargo
1	João Silva	joao@123.com	Desenvolvedor
2	Maria Souza	maria@e123.com	Analista
3	Carlos Oliveira	carlos@123.com	Gerente
⚡ Features legais

    Wait inteligente: Espera até 20 segundos se a página for lenta

    Pausas estratégicas: Não sobrecarrega o sistema

    Screenshots automáticos: Se der erro, tira print para eu ver o que aconteceu

    Validações: Verifica se tudo está funcionando corretamente

🆘 Se der problema...

Não se preocupe! O script tira screenshot automaticamente quando encontra um erro. Os arquivos ficam com nomes como login_error.png — bem fácil de identificar o que deu errado.

🤝 Quer contribuir?

Fique à vontade! Pode:

    Fazer um fork do projeto

    Criar uma branch nova (git checkout -b feature/nova-feature)

    Commitar suas mudanças (git commit -m 'Adiciona coisa nova')

    Fazer push (git push origin feature/nova-feature)

    Abrir um Pull Request

📄 Licença

MIT License - pode usar à vontade!
