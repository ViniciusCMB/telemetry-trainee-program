# Semana 3 — Arduino IDE

## Objetivo

Programar um ESP32-C3 para ler sensores e enviar dados formatados pela serial. É aqui que você vai ver o hardware funcionando de verdade.

## Preparação

- [ ] Arduino IDE 2.x instalado
- [ ] Placa ESP32-C3 Super Mini + cabo USB-C
- [ ] Sensor BMP280 (ou BME280) + protoboard + jumpers
- [ ] Ler a [Trilha Arduino IDE](../trilhas/arduino-ide.md) (seções 1, 3, 4)
- [ ] Ver o [Slide deck](../slides/semana-03.html)
- [ ] Fazer o [Quiz](../quiz/semana-03.md)

## Tarefas

### 1. Blink com LED

Conecte um LED ao GPIO 1 do ESP32-C3 (ou use o LED onboard se disponível).

```cpp
#define LED_PIN 1

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
    delay(500);
}
```

**Verifique**: o LED pisca a 1 Hz.

### 2. Conexão do BMP280

Conecte o BMP280 ao ESP32-C3:

```
BMP280   →  ESP32-C3
VCC      →  3.3V
GND      →  GND
SDA      →  GPIO4
SCL      →  GPIO5
```

Rode o scan I2C para confirmar a comunicação:

```cpp
#include <Wire.h>

void setup() {
    Serial.begin(115200);
    Wire.begin(4, 5);
    for (byte addr = 1; addr < 127; addr++) {
        Wire.beginTransmission(addr);
        if (Wire.endTransmission() == 0) {
            Serial.print("Dispositivo em 0x");
            Serial.println(addr, HEX);
        }
    }
}

void loop() {}
```

**Saída esperada**: `Dispositivo em 0x76` (ou `0x77` dependendo do módulo).

### 3. Leitura do sensor

Com a biblioteca Adafruit BMP280, leia e exiba os valores no Serial Monitor:

```cpp
#include <Wire.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;

void setup() {
    Serial.begin(115200);
    Wire.begin(4, 5);
    if (!bmp.begin(0x76)) {
        Serial.println("ERRO: sensor nao encontrado");
        while (1);
    }
}

void loop() {
    Serial.print("Alt: ");
    Serial.print(bmp.readAltitude(1013.25));
    Serial.print(" m  Temp: ");
    Serial.print(bmp.readTemperature());
    Serial.println(" C");
    delay(1000);
}
```

### 4. Envio de pacotes formatados (20 Hz)

Adapte o código para enviar pacotes no formato `#campos#` a 20 Hz, sem bloquear com `delay()`:

```cpp
unsigned long last_sample = 0;
const unsigned long INTERVAL = 50; // 20 Hz

void loop() {
    unsigned long now = millis();
    if (now - last_sample >= INTERVAL) {
        last_sample = now;
        // formata e envia pacote
    }
}
```

**Formato do pacote:**

```
#timestamp_ms;altitude_m;temperatura_C;pressao_hPa#
```

### 5. Extra: debounce de botão

Adicione um botão no GPIO 2 que alterna o LED quando pressionado, com debounce de 50 ms.

## Critérios de aceite

- [ ] Código compila e faz upload sem erros
- [ ] BMP280 responde no scan I2C
- [ ] Serial envia pacotes formatados a 20 Hz constante
- [ ] Pacotes no formato `#campos#`
- [ ] Commit com tipo semântico (ex: `feat:`, `docs:`, `build:`)
- [ ] README com esquema de ligação dos pinos

## Armadilhas comuns

- **Baud rate errado**: configure o Serial Monitor para 115200
- **Fio solto**: confira todas as conexões do BMP280
- **Endereço I2C errado**: pode ser `0x76` ou `0x77` — o scan mostra o correto
- **delay() trava**: se usar `delay()`, a taxa de amostragem fica imprecisa — use `millis()`

## Conexão com projetos reais

Este é o mesmo sensor BMP280 usado no Flight Computer. O formato de pacote que você implementou é compatível com o parser Python da Semana 2. O barramento I2C com SDA=GPIO4 e SCL=GPIO5 é idêntico ao usado no FC.

## Referências

- [Trilha Arduino IDE](../trilhas/arduino-ide.md)
- [Exemplo Arduino IDE](../examples/arduino-ide-exemplo.md)
- [Slide deck](../slides/semana-03.html)
- [Quiz](../quiz/semana-03.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-03.md)
