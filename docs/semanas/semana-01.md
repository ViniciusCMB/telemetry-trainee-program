# Semana 1 — Python básico

## Objetivo

Ler dados de telemetria de um arquivo CSV, calcular estatísticas simples e salvar um resumo. Este é o primeiro contato com dados reais de sensores.

## Preparação

- [ ] Python 3.10+ instalado (`python3 --version`)
- [ ] Ler a [Trilha Python](../trilhas/python.md) (seções 1.1 e 2.1)
- [ ] Ver o [Slide deck](../slides/semana-01.html)
- [ ] Fazer o [Quiz](../quiz/semana-01.md)

## Tarefas

### 1. Criar arquivo CSV de teste

Crie `dados.csv` com dados simulados de telemetria:

```csv
timestamp_ms,altitude_m,temperatura_C,pressao_hPa,ax,ay,az
0,0.0,25.0,1013.25,0.01,0.02,9.81
50,0.5,24.9,1012.80,0.02,0.01,9.80
100,1.2,24.8,1012.30,0.03,0.01,9.79
150,2.0,24.7,1011.75,0.02,0.02,9.81
200,3.1,24.6,1011.20,0.01,0.01,9.80
```

Comece com 5 linhas. Depois expanda para 50+ linhas com valores variados.

### 2. Script de leitura

Crie `leitor_csv.py` que:

1. Abre o CSV usando `csv.DictReader`
2. Lê todas as linhas para uma lista de dicionários
3. Extrai os valores de `altitude_m` para uma lista separada

**Estrutura esperada:**

```python
import csv

dados = []
with open("dados.csv") as f:
    for linha in csv.DictReader(f):
        dados.append(linha)

altitudes = [float(linha["altitude_m"]) for linha in dados]
```

### 3. Calcular estatísticas

Calcule e exiba:

- Número total de amostras
- Altitude média (com 2 casas decimais)
- Altitude máxima
- Altitude mínima
- Duração total em segundos (último timestamp - primeiro) / 1000

**Saída esperada:**

```
Amostras: 5
Altitude media: 1.36 m
Altitude max: 3.10 m
Altitude min: 0.00 m
Duracao: 0.20 s
```

### 4. Salvar resumo

Crie uma função `salvar_resumo(estatisticas, caminho="resumo.txt")` que escreve as estatísticas em um arquivo texto legível.

### 5. Extra: gráfico simples

Se tiver `matplotlib` instalado, gere um gráfico de altitude × tempo:

```python
import matplotlib.pyplot as plt

# ... depois de ter as listas times e altitudes ...
plt.plot(times, altitudes)
plt.xlabel("Tempo (s)")
plt.ylabel("Altitude (m)")
plt.title("Perfil de Voo")
plt.grid(True)
plt.savefig("perfil_voo.png")
```

## Critérios de aceite

- [ ] Script roda sem erros em diferentes CSVs
- [ ] Estatísticas corretas (confira na mão para 3 linhas)
- [ ] Resumo salvo em arquivo
- [ ] Commit com tipo semântico (ex: `feat:`, `docs:`, `test:`)
- [ ] README com instruções de execução

## Armadilhas comuns

- **CSV vazio**: trate o caso de arquivo sem linhas
- **Valores não numéricos**: use `try/except` em volta do `float()`
- **Caminho do arquivo**: use `sys.argv` para receber o caminho como argumento

## Conexão com projetos reais

O Flight Computer gera logs CSV durante os voos de teste. As mesmas funções de leitura e estatísticas que você implementou aqui são usadas para analisar dados reais pós-missão.

## Referências

- [Trilha Python](../trilhas/python.md)
- [Exemplo Python](../examples/python-exemplo.md)
- [Slide deck](../slides/semana-01.html)
- [Quiz](../quiz/semana-01.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-01.md)
