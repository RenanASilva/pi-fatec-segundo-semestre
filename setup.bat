@echo off
REM Cria o ambiente virtual
py -m venv venv

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala todas as dependências do requirements.txt
pip install -r requirements.txt

echo Ambiente pronto!