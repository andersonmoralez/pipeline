# 🚀 Iniciando o projeto

### 📄 Criando os arquivos de configuração: Pylint e Pre-commit (utf-8 encoding):

Comando para gerar o arquivo Pre-commit:
```
pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8
```

Comando para gerar o arquivo Pylint:
```
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
```
# ⚙️ Utils

Comando para executar pre-commit (rodar sempre ao clonar o projeto):
```
pre-commit install
```

Comando para criar ambiente virtual (necessário ter o virtualenv instalado):
> Rodar o comando na raiz do projeto
```
virtualenv <name>
```

Comando para ativar ambiente virtual (necessário ter o virtualenv instalado):
```
myvenv\Scripts\activate.ps1
```