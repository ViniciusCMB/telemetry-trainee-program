# Quiz — Semana 1: Python básico

## Questões

### 1. (Múltipla escolha) Qual função do módulo `csv` é mais adequada para ler um arquivo CSV onde a primeira linha contém os nomes das colunas?
- a) `csv.reader()`
- b) `csv.DictReader()`
- c) `csv.writer()`
- d) `csv.DictWriter()`

### 2. (Verdadeiro ou Falso) O bloco `try/except` em Python só pode capturar um tipo de exceção por vez.
- Verdadeiro / Falso

### 3. (Resposta curta) Como você calcularia a média de uma lista de números chamada `valores` em Python? Escreva o código.

### 4. (Múltipla escolha) Ao abrir um arquivo CSV para leitura, qual modo de abertura é o mais indicado?
- a) `"w"`
- b) `"a"`
- c) `"r"`
- d) `"rb"`

### 5. (Múltipla escolha) Qual função da biblioteca `matplotlib` é usada para criar um gráfico de linha simples?
- a) `plt.bar()`
- b) `plt.scatter()`
- c) `plt.plot()`
- d) `plt.hist()`

### 6. (Resposta curta) Escreva um trecho de código que tenta abrir o arquivo `dados.csv` e, caso ele não exista, imprime "Arquivo não encontrado".

### 7. (Verdadeiro ou Falso) A função `max()` em Python pode ser usada tanto com listas de números quanto com listas de strings.
- Verdadeiro / Falso

### 8. (Múltipla escolha) O que a função `plt.show()` faz?
- a) Salva o gráfico em um arquivo
- b) Exibe o gráfico na tela
- c) Fecha todas as figuras abertas
- d) Limpa a figura atual

### 9. (Resposta curta) Dado um `DictReader`, como acessar o valor da coluna `"temperatura"` da primeira linha?

## Respostas

### 1. b) `csv.DictReader()`
### 2. Falso — é possível capturar múltiplos tipos com `except (Tipo1, Tipo2):` ou com múltiplos blocos `except`.
### 3. `sum(valores) / len(valores)`
### 4. c) `"r"`
### 5. c) `plt.plot()`
### 6. 
```python
try:
    with open("dados.csv", "r") as arquivo:
        print("Arquivo aberto com sucesso")
except FileNotFoundError:
    print("Arquivo não encontrado")
```
### 7. Verdadeiro — strings também são ordenáveis lexicograficamente.
### 8. b) Exibe o gráfico na tela
### 9. `next(reader)["temperatura"]` (onde `reader` é o objeto `DictReader`)
