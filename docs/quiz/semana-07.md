# Quiz — Semana 7: Flight Computer & Helike

## Questões

### 1. (Múltipla escolha) Em uma FSM (Finite State Machine) de voo, qual estado normalmente vem depois do ASCENT?
- a) IDLE
- b) DESCENT
- c) LANDED
- d) BOOT

### 2. (Resposta curta) Liste os estados típicos de uma FSM de voo de foguete e descreva brevemente cada um.

### 3. (Verdadeiro ou Falso) No barramento I2C, é possível conectar múltiplos sensores no mesmo barramento, desde que cada um tenha um endereço único.
- Verdadeiro / Falso

### 4. (Múltipla escolha) Qual faixa de frequência o LoRa normalmente utiliza para comunicação em telemetria amadora no Brasil?
- a) 2.4 GHz
- b) 915 MHz
- c) 433 MHz ou 868 MHz
- d) 5.8 GHz

### 5. (Verdadeiro ou Falso) O formato PocketQube tem dimensões padronizadas de 5×5×5 cm por unidade (1P).
- Verdadeiro / Falso

### 6. (Múltipla escolha) Qual sistema de arquivos é mais adequado para armazenar dados de voo em um microcontrolador com memória flash interna?
- a) FAT32 em cartão SD
- b) LittleFS na flash interna
- c) NTFS
- d) ext4

### 7. (Resposta curta) Por que o LittleFS é preferível ao SD card convencional em aplicações de voo?

### 8. (Verdadeiro ou Falso) O estado LANDED de uma FSM de voo é ativado quando o foguete atinge o apogeu.
- Verdadeiro / Falso

## Respostas

### 1. b) DESCENT
### 2. IDLE (aguardando inicialização/lançamento), ASCENT (subindo), DESCENT (descendo, após apogeu), LANDED (pousado, detectado por impacto ou ausência de movimento).
### 3. Verdadeiro
### 4. c) 433 MHz ou 868 MHz
### 5. Verdadeiro
### 6. b) LittleFS na flash interna
### 7. LittleFS é mais robusto contra vibração e quedas de energia (sem partes móveis), tem menor consumo energético e não requer hardware adicional (slot de SD).
### 8. Falso — o estado LANDED é ativado após o pouso (detecção de impacto ou velocidade zero sustentada), não no apogeu. Apogeu marca a transição ASCENT → DESCENT.
