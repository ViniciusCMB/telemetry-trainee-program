# Quiz — Semana 0: Onboarding & GitHub

## Questões

### 1. (Múltipla escolha) Qual é a diferença principal entre `git clone` e `git fork`?
- a) `clone` baixa um repositório local; `fork` copia um repositório remoto para sua conta no GitHub
- b) `clone` cria um branch novo; `fork` apaga o repositório original
- c) Ambos fazem a mesma coisa em repositórios diferentes
- d) `fork` só funciona em repositórios privados

### 2. (Múltipla escolha) Qual convenção de nomenclatura de branches é mais comum em projetos de telemetria?
- a) feature-nome-do-responsavel
- b) Feature_Nome_Do_Branch
- c) feat/nome-descritivo-em-ingles
- d) nome_do_autor/branch

### 3. (Verdadeiro ou Falso) Uma mensagem de commit deve ser vaga como "consertei um bug" para evitar expor detalhes internos.
- Verdadeiro / Falso

### 4. (Múltipla escolha) Qual campo NÃO é comum em um template de Pull Request?
- a) Descrição das mudanças
- b) Checklist de testes realizados
- c) Número da issue relacionada
- d) Senha do repositório

### 5. (Resposta curta) Explique a diferença entre a branch `main` e uma branch de feature.

### 6. (Verdadeiro ou Falso) O comando `git push` envia commits do repositório local para o remoto.
- Verdadeiro / Falso

### 7. (Múltipla escolha) O que significa um repositório estar em um estado "detached HEAD"?
- a) O HEAD aponta para um commit específico, não para um branch
- b) O repositório foi deletado
- c) O branch main foi renomeado
- d) O repositório está corrompido

### 8. (Resposta curta) Por que é importante escrever mensagens de commit no imperativo (ex.: "Adiciona validação de checksum" em vez de "Adicionou validação de checksum")?

## Respostas

### 1. a) `clone` baixa um repositório local; `fork` copia um repositório remoto para sua conta no GitHub
### 2. c) feat/nome-descritivo-em-ingles
### 3. Falso — mensagens de commit devem ser claras e descritivas para facilitar o entendimento do histórico do projeto
### 4. d) Senha do repositório
### 5. A branch `main` contém o código estável e pronto para produção. Branches de feature são criadas a partir da `main` para desenvolver funcionalidades específicas e depois são mescladas via Pull Request.
### 6. Verdadeiro
### 7. a) O HEAD aponta para um commit específico, não para um branch
### 8. O imperativo padroniza as mensagens e segue a convenção do Git, que aplica o imperativo nas descrições de merge. Isso mantém o histórico consistente e legível.
