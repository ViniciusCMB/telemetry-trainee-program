# Semana 0 — Onboarding & GitHub

## Objetivo

Configurar seu ambiente de desenvolvimento e aprender o fluxo de trabalho com Git, issues e PRs que será usado durante todo o treinamento.

## Preparação

- [ ] Criar conta no GitHub (se não tiver)
- [ ] Instalar Git no seu computador
- [ ] Verificar instalação: `git --version`
- [ ] Ler a [Trilha GitHub](../trilhas/github.md)

## Tarefas

### 1. Setup do ambiente

Instale e verifique cada ferramenta:

```
VSCode     → code --version
Python     → python3 --version
Git        → git --version
Arduino IDE → abrir e verificar instalação
PlatformIO → instalar extensão no VSCode
KiCad      → abrir e verificar instalação
```

### 2. Configurar Git

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### 3. Clonar e criar branch

```bash
git clone https://github.com/ViniciusCMB/telemetry-trainee-program.git
cd telemetry-trainee-program
git checkout -b seu-nome-sobrenome
```

### 4. Criar README pessoal

Crie um arquivo `README.md` na raiz do projeto com:

```markdown
# Seu Nome — Trainee Telemetria

## Objetivos
Quero aprender Python e Arduino para contribuir com o Flight Computer.

## Experiência prévia
- Já programei em C na faculdade
- Nunca trabalhei com Arduino
```

### 5. Commit e push

```bash
git add README.md
git commit -m "git: adiciona README pessoal com objetivos"
git push -u origin seu-nome-sobrenome
```

### 6. Abrir Pull Request

1. No GitHub, clique em "Pull Request"
2. Base: `main` ← Compare: `seu-nome-sobrenome`
3. Preencha o template
4. Atribua o instrutor como reviewer

## Critérios de aceite

- [ ] Branch nomeada como `seu-nome-sobrenome`
- [ ] README pessoal na raiz do projeto
- [ ] Commit com tipo semântico (`docs:`, `feat:`, ...)
- [ ] PR segue o template
- [ ] Instrutor consegue fazer checkout da branch

## Dicas

- Se der conflito no PR, resolva localmente com `git pull origin main` e resolva os conflitos
- Use `git status` antes de qualquer commit para saber o que vai entrar
- Commits pequenos e frequentes são melhores que um commit gigante

## Conexão com projetos reais

No Flight Computer e no Helike, todo o desenvolvimento segue o mesmo fluxo: branch pessoal, commits semânticos, PR com revisão. A Semana 0 é a base para tudo que vem a seguir.

## Referências

- [Trilha GitHub](../trilhas/github.md)
- [Exemplo GitHub](../examples/github-exemplo.md)
- [Slide deck](../slides/semana-00.html)
- [Quiz](../quiz/semana-00.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-00.md)
