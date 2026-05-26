# Quiz — Semana 5: Integração Arduino ↔ Python

## Questões

### 1. (Múltipla escolha) Qual é a diferença entre `Serial.parseInt()` e `Serial.readString()`?
- a) `parseInt()` lê um valor inteiro; `readString()` lê uma string completa até o terminador
- b) `parseInt()` lê caracteres individuais; `readString()` lê bytes brutos
- c) Ambos fazem a mesma coisa
- d) `readString()` só funciona no Python

### 2. (Resposta curta) O que é packet framing e por que ele é importante na comunicação serial?

### 3. (Múltipla escolha) Em um protocolo serial, para que servem os sync bytes (bytes de sincronização)?
- a) Aumentar a velocidade da transmissão
- b) Indicar o início de um pacote de dados
- c) Criptografar a mensagem
- d) Reduzir o consumo de energia

### 4. (Verdadeiro ou Falso) Um buffer overflow na serial pode ocorrer quando o microcontrolador recebe dados mais rápido do que consegue processá-los.
- Verdadeiro / Falso

### 5. (Múltipla escolha) Qual é a ordem correta ao processar um pacote recebido pela serial?
- a) Validar checksum → verificar sync bytes → interpretar dados
- b) Interpretar dados → validar checksum → verificar sync bytes
- c) Verificar sync bytes → validar checksum → interpretar dados
- d) A ordem não importa

### 6. (Resposta curta) Escreva um trecho de código Python que abre uma porta serial (`/dev/ttyACM0`, 115200 baud) e lê uma linha.

### 7. (Múltipla escolha) Qual função do lado Arduino envia dados para a porta serial em formato legível por humanos?
- a) `Serial.write()`
- b) `Serial.print()`
- c) `Serial.read()`
- d) `Serial.available()`

### 8. (Verdadeiro ou Falso) A função `Serial.available()` retorna o número de bytes disponíveis para leitura no buffer serial.
- Verdadeiro / Falso

## Respostas

### 1. a) `parseInt()` lê um valor inteiro; `readString()` lê uma string completa até o terminador
### 2. Packet framing é a técnica de delimitar pacotes com marcadores de início e fim (ex.: sync bytes). É importante porque a serial é um fluxo contínuo de bytes e sem framing não é possível saber onde um pacote começa e termina.
### 3. b) Indicar o início de um pacote de dados
### 4. Verdadeiro
### 5. c) Verificar sync bytes → validar checksum → interpretar dados
### 6. 
```python
import serial
ser = serial.Serial("/dev/ttyACM0", 115200)
linha = ser.readline().decode().strip()
```
### 7. b) `Serial.print()`
### 8. Verdadeiro
