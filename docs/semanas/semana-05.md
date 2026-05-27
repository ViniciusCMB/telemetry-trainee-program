# Semana 5 — Integração Arduino ↔ Python

## Objetivo

Integrar o Arduino (que envia dados) com o Python (que recebe, parseia e salva). É o primeiro pipeline completo de telemetria.

## Preparação

- [ ] Semanas 3 e 4 concluídas (Arduino enviando pacotes)
- [ ] Semanas 1 e 2 concluídas (parser Python funcional)
- [ ] ESP32-C3 conectado via USB
- [ ] Rever seções de [serial no Arduino](../trilhas/arduino-ide.md#3-serial--comunicao-com-o-pc) e [parsing no Python](../trilhas/python.md#12-parsing-de-pacotes-serial)
- [ ] Ver o [Slide deck](../slides/semana-05.html)
- [ ] Fazer o [Quiz](../quiz/semana-05.md)

## Tarefas

### 1. Lado Arduino — envio contínuo

Use o código da Semana 3/4 para enviar pacotes a 20 Hz no formato:

```
#timestamp_ms;altitude_m;temperatura_C;pressao_hPa;ax;ay;az#
```

Mantenha o ESP32-C3 conectado e enviando dados.

### 2. Lado Python — leitor serial

Crie `leitor_serial.py` que lê da porta serial em tempo real:

```python
import serial
import csv
from datetime import datetime

PORTA = "/dev/ttyACM0"  # Linux
BAUD = 115200

def main():
    with serial.Serial(PORTA, BAUD, timeout=1) as ser:
        with open("log_telemetria.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp_ms", "altitude_m",
                             "temperatura_C", "pressao_hPa"])

            while True:
                linha = ser.readline().decode("utf-8", errors="ignore").strip()
                if not linha:
                    continue
                # chamar o parser da Semana 2 aqui
                # se válido, escrever no CSV
```

### 3. Integrar parser da Semana 2

- Reaproveite a função `parse_packet()` da Semana 2
- Reaproveite a função `validate_packet()`
- Pacotes inválidos: registre em um log separado (`erros.log`) com timestamp e linha bruta

### 4. Logging resiliente

O programa deve rodar por tempo indeterminado:

- Trate desconexão da serial (`SerialException`)
- Trate linha corrompida (não quebrar o loop)
- Mostre estatísticas a cada 100 pacotes:
  ```
  [12:34:56] 500 pacotes recebidos | 480 válidos | 20 erros | 96% OK
  ```

### 5. Extra: plotagem em tempo real

Use matplotlib em modo interativo para mostrar o gráfico de altitude em tempo real:

```python
plt.ion()
fig, ax = plt.subplots()
# a cada pacote válido, atualiza o gráfico
```

## Critérios de aceite

- [ ] Arduino envia pacotes a 20 Hz constante
- [ ] Python lê, parseia e valida sem perder pacotes
- [ ] CSV de saída com dados limpos
- [ ] Log de erros separado
- [ ] Roda por 5+ minutos sem travar
- [ ] Commit com prefixo `py:` ou `ard:`
- [ ] README com instruções de execução

## Armadilhas comuns

- **Porta errada**: no Linux é `/dev/ttyACM0` ou `/dev/ttyUSB0`; no Windows `COM3`
- **Buffer overflow**: se o Python não ler rápido, o buffer serial enche — aumente o timeout ou diminua a taxa
- **Encoding**: use `errors="ignore"` no decode para não quebrar com caracteres estranhos
- **Parser da Semana 2**: teste localmente com uma linha antes de integrar com a serial

## Conexão com projetos reais

Este pipeline é a versão simplificada do que acontece no Helike e no Flight Computer: sensores → firmware → serial/LoRa →地面 station → log CSV. A diferença é que nos projetos reais a transmissão é sem fio (LoRa) e o processamento é mais robusto.

## Referências

- [Trilha Python](../trilhas/python.md)
- [Trilha Arduino IDE](../trilhas/arduino-ide.md)
- [Slide deck](../slides/semana-05.html)
- [Quiz](../quiz/semana-05.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-05.md)
