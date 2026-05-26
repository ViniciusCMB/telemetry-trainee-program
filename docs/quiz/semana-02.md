# Quiz — Semana 2: Python aplicado

## Questões

### 1. (Múltipla escolha) Dada a string `"12.5,23.8,10.2"`, qual código a divide corretamente em uma lista de três valores?
- a) `"12.5,23.8,10.2".split(",")`
- b) `"12.5,23.8,10.2".split(".")`
- c) `"12.5,23.8,10.2".split()`
- d) `"12.5,23.8,10.2".partition(",")`

### 2. (Verdadeiro ou Falso) O valor `float('nan')` é igual a ele mesmo segundo o operador `==` em Python.
- Verdadeiro / Falso

### 3. (Resposta curta) Como verificar se um valor de ponto flutuante é NaN em Python?

### 4. (Múltipla escolha) Em um sistema de telemetria, para que serve um checksum?
- a) Compactar os dados transmitidos
- b) Verificar a integridade dos dados recebidos
- c) Criptografar a comunicação
- d) Aumentar a taxa de transmissão

### 5. (Resposta curta) Dado um pacote de telemetria no formato `"temperatura=25.3;pressao=1013;altitude=500"`, escreva o código para converter essa string em um dicionário.

### 6. (Múltipla escolha) Qual biblioteca Python é mais adequada para escrever logs com níveis (INFO, WARNING, ERROR) em um arquivo?
- a) `print()`
- b) `csv`
- c) `logging`
- d) `json`

### 7. (Verdadeiro ou Falso) A validação de faixa (range check) verifica se um valor está dentro de limites superior e inferior esperados.
- Verdadeiro / Falso

### 8. (Resposta curta) Suponha um dicionário `pacote = {"tempo": 10, "temperatura": 30.5}`. Escreva o código para acessar a temperatura e, caso a chave não exista, retornar `None`.

### 9. (Múltipla escolha) Qual é a ordem recomendada ao processar dados de telemetria?
- a) Validar, depois processar, depois armazenar
- b) Armazenar, depois validar, depois processar
- c) Processar, depois armazenar, depois validar
- d) A ordem não importa

## Respostas

### 1. a) `"12.5,23.8,10.2".split(",")`
### 2. Falso — NaN não é igual a nada em Python, incluindo ele mesmo. Use `math.isnan()` para verificar.
### 3. `import math; math.isnan(valor)`
### 4. b) Verificar a integridade dos dados recebidos
### 5. 
```python
pacote = dict(item.split("=") for item in dados.split(";"))
```
### 6. c) `logging`
### 7. Verdadeiro
### 8. `pacote.get("temperatura", None)`
### 9. a) Validar, depois processar, depois armazenar
