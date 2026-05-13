# =========================
# PARTE 1 - CONFIGURAÇÃO
# =========================

# Configure seu nome e email no Git
# Exemplo:
# git config --global user.name "SeuNome"
# git config --global user.email "seu@email.com"

git config --global user.name "SeuNome"
git config --global user.email "seu@email.com"


# =========================
# PARTE 2 - CRIANDO PROJETO
# =========================

# Crie uma pasta chamada atividade-git
# Entre dentro dela

# Exemplo:
# mkdir atividade-git
# cd atividade-git

mkdir atividade-git
cd atividade-git


# =========================
# PARTE 3 - INICIANDO GIT
# =========================

# Inicie um repositório Git na pasta

# Exemplo:
# git init

git init


# =========================
# PARTE 4 - CRIANDO ARQUIVO
# =========================

# Crie um arquivo chamado index.txt
# Coloque um texto dentro dele

# Exemplo:
# echo Olá mundo > index.txt

echo Olá mundo > index.txt


# =========================
# PARTE 5 - VERIFICANDO STATUS
# =========================

# Veja o status do Git

# Exemplo:
# git status

git status


# =========================
# PARTE 6 - PRIMEIRO COMMIT
# =========================

# Adicione o arquivo ao Git
# Faça o commit

# Exemplo:
# git add .
# git commit -m "Primeiro commit"

git add .
git commit -m "Primeiro commit"


# =========================
# PARTE 7 - CONECTANDO GITHUB
# =========================

# Crie um repositório no GitHub (site)

# Depois conecte usando o link

# Exemplo:
# git remote add origin https://github.com/user/repositorio.git

git remote add origin LINK_DO_SEU_REPOSITORIO


# =========================
# PARTE 8 - ENVIANDO PRO GITHUB
# =========================

# Envie o projeto

# Exemplo:
# git branch -M main
# git push -u origin main

git branch -M main
git push -u origin main


# =========================
# PARTE 9 - ALTERANDO ARQUIVO
# =========================

# Adicione mais conteúdo no arquivo

# Exemplo:
# echo Aprendendo Git >> index.txt

echo Aprendendo Git >> index.txt


# =========================
# PARTE 10 - NOVO COMMIT
# =========================

# Salve e envie novamente

# Exemplo:
# git add .
# git commit -m "Atualização"
# git push

git add .
git commit -m "Atualização"
git push


# =========================
# PARTE 11 - DESAFIO FINAL
# =========================

# Crie um novo arquivo chamado aluno.txt
# Coloque seu nome dentro

# Exemplo:
# echo Meu nome é João > aluno.txt

echo Meu nome é SEU_NOME > aluno.txt


# Faça commit e envie

git add .
git commit -m "Adicionando aluno"
git push


# =========================
# EXTRA (DESAFIO HARD)
# =========================

# Crie outro arquivo chamado notas.txt
# Faça pelo menos 2 commits diferentes alterando ele

# Exemplo:
# echo Nota 10 > notas.txt
# echo Melhorando >> notas.txt

https://github.com/motinha15614/sla  https://github.com/motinha15614/atividade-git.git

echo "# t" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/motinha15614/aula-10
git push -u origin main


Puxar um repositorio existente

git remote add origin https://github.com/motinha15614/aula-10
git branch -M main
git push -u origin main

git push origin https://github.com/motinha15614/aula-10