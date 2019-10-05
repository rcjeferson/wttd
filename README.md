# Eventex

Sistema de Eventos encomendado pela Morena.

**PS:** Esse é um projeto desenvolvido no curso [Welcome to the Django](https://welcometothedjango.com.br).

[![Build Status](https://travis-ci.org/rcjeferson/wttd.svg?branch=master)](https://travis-ci.org/rcjeferson/wttd)

## Como desenvolver

1. Clone o repositório;
2. Crie um virtualenv com Python 3.5;
3. Ative o virtualenv;
4. Instale as dependências;
5. Configura a instância com o `.env`;
6. Execute os testes.

### Linux

```console
git clone https://github.com/rcjeferson/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

### Windows

```powershell
git clone https://github.com/rcjeferson/wttd.git wttd
cd wttd
python -m venv .wttd
& ".wttd\Scripts\Activate.ps1"
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy

1. Crie uma instância no Heroku;
2. Conecte a instância do Heroku ao repositório no GitHub;
3. Habilite o deploy automático ao fazer push no repositório;
4. Defina uma `SECRET_KEY` segura para a instância utilizando o script `contrib/secret_gen.py` e configure como variável de ambiente na instância;
5. Defina `DEBUG=False` como variável de ambiente da instância;
6. Configure o serviço de Email como variável de ambiente da instância;
