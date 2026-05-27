# Semana 2 — Python aplicado (pacotes)

## Objetivo

Implementar um parser de pacotes de telemetria e um validador de dados. Na vida real, os dados não chegam limpos em CSV — chegam como strings cruas pela serial.

## Preparação

- [ ] Semana 1 concluída
- [ ] Ler a [Trilha Python](../trilhas/python.md) (seções 1.2 e 1.3)
- [ ] Ver o [Slide deck](../slides/semana-02.html)
- [ ] Fazer o [Quiz](../quiz/semana-02.md)

## Tarefas

### 1. Parser de pacote

Crie uma função que recebe uma string bruta da serial e retorna um dicionário estruturado.

**Formato do pacote:**

```
#timestamp_ms;altitude_m;temperatura_C;pressao_hPa;ax;ay;az#
```

**Exemplo:**

```
#0;0.0;25.0;1013.25;0.01;0.02;9.81#
#50;0.5;24.9;1012.80;0.02;0.01;9.80#
```

**Implementação:**

```python
def parse_packet(line: str) -> dict | None:
    if not line.startswith("#") or not line.endswith("#"):
        return None
    parts = line.strip("#").split(";")
    if len(parts) != 7:
        return None
    try:
        return {
            "timestamp_ms": int(parts[0]),
            "altitude_m": float(parts[1]),
            "temperatura_C": float(parts[2]),
            "pressao_hPa": float(parts[3]),
            "ax": float(parts[4]),
            "ay": float(parts[5]),
            "az": float(parts[6]),
        }
    except ValueError:
        return None
```

### 2. Validador de dados

Crie uma função que valida os campos do pacote:

```python
def validate_packet(data: dict) -> bool:
    # Verifica range físico de cada campo
    if data["altitude_m"] < -100 or data["altitude_m"] > 10000:
        return False
    if data["temperatura_C"] < -40 or data["temperatura_C"] > 85:
        return False
    if data["pressao_hPa"] < 300 or data["pressao_hPa"] > 1100:
        return False
    # Verifica gravidade (deve ser ~9.81 m/s² em repouso)
    g = (data["ax"]**2 + data["ay"]**2 + data["az"]**2) ** 0.5
    if g < 8.0 or g > 11.0:
        return False
    return True
```

### 3. Processador de arquivo

Crie um script que:

1. Lê um arquivo linha por linha
2. Para cada linha, tenta fazer parse
3. Se o parse funcionar, valida os dados
4. Conta pacotes: válidos, inválidos (parser) e rejeitados (validação)
5. Exibe estatísticas no final

**Saída esperada:**

```
Processando pacotes...
Linha 1: OK
Linha 2: OK
Linha 3: FALHA (parser) — formato invalido
Linha 4: OK
Linha 5: REJEITADO (validacao) — altitude fora do range
...

Resumo:
  Total de linhas: 100
  Pacotes validos: 78
  Erros de parser: 12
  Rejeitados:      10
  Taxa de sucesso: 78%
```

### 4. Extra: checksum simples

Adicione um byte de checksum ao final do pacote:

```
#timestamp;alt;temp;pres;ax;ay;az;CHK#
```

O checksum é o XOR de todos os bytes entre `#...#`. Rejeite pacotes com checksum inválido.

## Critérios de aceite

- [ ] Parser rejeita formatos inválidos (sem `#`, campos a menos, NaN)
- [ ] Validador rejeita valores fora do range físico
- [ ] Estatísticas de parse × validação no final
- [ ] Commit com prefixo `py:`
- [ ] README com exemplos de uso

## Armadilhas comuns

- **String vazia**: `parse_packet("")` deve retornar `None`, não quebrar
- **Timestamp negativo**: pode acontecer? Decida se aceita ou rejeita
- **Parser vs validação**: são duas etapas separadas — não misture

## Conexão com projetos reais

No Helike, os testes de hardware enviam pacotes pela serial com 15 campos. O parser que você está construindo é a versão simplificada do que está no `DataValidation.h` da `lib/calc/`.

## Referências

- [Trilha Python](../trilhas/python.md)
- [Exemplo Python](../examples/python-exemplo.md)
- [Slide deck](../slides/semana-02.html)
- [Quiz](../quiz/semana-02.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-02.md)
