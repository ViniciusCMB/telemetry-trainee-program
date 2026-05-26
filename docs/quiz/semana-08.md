# Quiz — Semana 8: Capstone (Revisão Geral)

## Questões

### 1. (Múltipla escolha) Qual é a ordem correta de operações ao receber um pacote de telemetria pela serial?
- a) Interpretar dados → validar checksum → verificar sync bytes
- b) Verificar sync bytes → validar checksum → interpretar dados
- c) Validar checksum → interpretar dados → verificar sync bytes
- d) Interpretar dados → verificar sync bytes → validar checksum

### 2. (Resposta curta) Explique como `git fork` e `git clone` se diferenciam e em qual situação cada um é usado.

### 3. (Múltipla escolha) No PlatformIO, qual diretiva do `platformio.ini` adiciona automaticamente uma biblioteca ao projeto?
- a) `lib_install`
- b) `lib_deps`
- c) `library`
- d) `dependencies`

### 4. (Verdadeiro ou Falso) A função `millis()` no Arduino retorna o tempo em microssegundos desde o início do programa.
- Verdadeiro / Falso

### 5. (Resposta curta) Dado o pacote `"temp=28.5;pres=1012;alt=450"`, escreva código Python para convertê-lo em um dicionário e validar que a altitude está entre 0 e 5000 metros.

### 6. (Múltipla escolha) Qual das alternativas abaixo é uma vantagem de usar um capacitor de desacoplamento em uma PCB?
- a) Aumentar a impedância da linha de alimentação
- b) Filtrar transientes de alta frequência próximos ao pino de alimentação do CI
- c) Substituir resistores pull-up
- d) Reduzir o número de camadas da placa

### 7. (Verdadeiro ou Falso) No KiCad, o arquivo Gerber contém as informações de conexões lógicas do esquemático.
- Verdadeiro / Falso

### 8. (Múltipla escolha) Em uma FSM de voo, a transição do estado ASCENT para DESCENT ocorre quando:
- a) O foguete toca o solo
- b) O foguete atinge o apogeu (altitude máxima)
- c) O paraquedas abre
- d) O motor é ligado

### 9. (Resposta curta) Escreva um trecho de código Arduino que lê um valor inteiro da serial e verifica se ele está dentro de uma faixa esperada (0-1023). Se sim, acende um LED; se não, envia "Erro" pela serial.

### 10. (Múltipla escolha) Qual sistema de arquivos é mais robusto para armazenar logs de voo em flash interna de microcontroladores?
- a) FAT32
- b) LittleFS
- c) NTFS
- d) ext4

## Respostas

### 1. b) Verificar sync bytes → validar checksum → interpretar dados
### 2. `git clone` baixa um repositório remoto para o computador local. `git fork` cria uma cópia do repositório na sua conta do GitHub. Usa-se `fork` para contribuir com projetos alheios sem permissão de escrita direta; `clone` é usado para obter uma cópia local de qualquer repositório.
### 3. b) `lib_deps`
### 4. Falso — `millis()` retorna o tempo em *milissegundos* desde o início do programa.
### 5. 
```python
dados = "temp=28.5;pres=1012;alt=450"
pacote = dict(item.split("=") for item in dados.split(";"))
altitude = float(pacote["alt"])
if 0 <= altitude <= 5000:
    print("Altitude válida")
else:
    print("Altitude fora do range")
```
### 6. b) Filtrar transientes de alta frequência próximos ao pino de alimentação do CI
### 7. Falso — Gerber contém informações de layout físico das camadas da PCB, não conexões lógicas (que estão no esquemático).
### 8. b) O foguete atinge o apogeu (altitude máxima)
### 9. 
```cpp
void loop() {
    if (Serial.available() > 0) {
        int valor = Serial.parseInt();
        if (valor >= 0 && valor <= 1023) {
            digitalWrite(13, HIGH);
        } else {
            Serial.println("Erro");
        }
    }
}
```
### 10. b) LittleFS
