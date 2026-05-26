# Quiz — Semana 3: Arduino IDE

## Questões

### 1. (Múltipla escolha) Qual é a diferença entre `digitalWrite()` e `analogWrite()`?
- a) `digitalWrite()` escreve em portas analógicas; `analogWrite()` em portas digitais
- b) `digitalWrite()` liga/desliga (HIGH/LOW); `analogWrite()` define um valor PWM (0-255)
- c) Ambos fazem a mesma coisa com nomes diferentes
- d) `analogWrite()` só funciona no pino 13

### 2. (Múltipla escolha) Qual função configura um pino como entrada ou saída?
- a) `pinConfig()`
- b) `pinSetup()`
- c) `pinMode()`
- d) `setPin()`

### 3. (Verdadeiro ou Falso) O endereço I2C de um dispositivo pode ser compartilhado por até 8 dispositivos no mesmo barramento.
- Verdadeiro / Falso

### 4. (Resposta curta) O que significa o parâmetro "baud rate" na função `Serial.begin()` e qual valor é comumente usado em telemetria?

### 5. (Múltipla escolha) Qual é a vantagem de usar `millis()` em vez de `delay()` para temporização?
- a) `millis()` consome menos memória
- b) `millis()` não bloqueia a execução do código, permitindo multitarefa
- c) `millis()` é mais preciso que `delay()`
- d) `millis()` só funciona no Arduino Uno

### 6. (Verdadeiro ou Falso) Um resistor pull-up mantém um pino digital em estado HIGH quando nenhum dispositivo está acionando o barramento.
- Verdadeiro / Falso

### 7. (Resposta curta) Explique o que é um endereço I2C de 7 bits e como dois dispositivos com o mesmo endereço se comportam no mesmo barramento.

### 8. (Múltipla escolha) Qual valor analógico representa 0 V em uma leitura analógica no Arduino (resolução de 10 bits)?
- a) 0
- b) 255
- c) 512
- d) 1023

## Respostas

### 1. b) `digitalWrite()` liga/desliga (HIGH/LOW); `analogWrite()` define um valor PWM (0-255)
### 2. c) `pinMode()`
### 3. Falso — cada dispositivo I2C precisa ter um endereço único no barramento
### 4. Taxa de transmissão de dados em bits por segundo (baud). Valores comuns em telemetria: 115200 ou 9600.
### 5. b) `millis()` não bloqueia a execução do código, permitindo multitarefa
### 6. Verdadeiro
### 7. Endereço I2C de 7 bits identifica um dispositivo no barramento (0-127). Dois dispositivos com o mesmo endereço causam conflito e nenhum dos dois funcionará corretamente.
### 8. a) 0
