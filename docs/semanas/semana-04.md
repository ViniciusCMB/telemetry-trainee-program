# Semana 4 — PlatformIO

## Objetivo

Migrar o projeto da Semana 3 do Arduino IDE para uma estrutura profissional com PlatformIO, separando o código em módulos e configurando ambientes de build.

## Preparação

- [ ] Semana 3 concluída (código funcional no Arduino IDE)
- [ ] VS Code + PlatformIO extension instalados
- [ ] Ler a [Trilha PlatformIO](../trilhas/platformio.md) (seções 1 a 5)
- [ ] Ver o [Slide deck](../slides/semana-04.html)
- [ ] Fazer o [Quiz](../quiz/semana-04.md)

## Tarefas

### 1. Criar projeto PlatformIO

1. VS Code → Command Palette → `PlatformIO: New Project`
2. Name: `telemetria-pio`
3. Board: `Espressif ESP32-C3 Dev Module`
4. Framework: `Arduino`
5. Location: dentro da sua branch no repositório

### 2. Configurar platformio.ini

```ini
[env:esp32c3]
platform = espressif32
board = esp32-c3-devkitm-1
framework = arduino
monitor_speed = 115200
build_flags =
    -DI2C_SDA=4
    -DI2C_SCL=5
    -DSEALEVEL=1013.25

lib_deps =
    adafruit/Adafruit BMP280 Library

[env:native]
platform = native
framework = unity
build_flags = -I lib
```

### 3. Migrar o código

Separe o sketch da Semana 3 na estrutura PlatformIO:

```
telemetria-pio/
├── platformio.ini
├── src/
│   └── main.cpp          # código principal (antes era o .ino)
├── lib/
│   └── calc/
│       └── SensorData.h  # struct com dados do sensor
└── test/
    └── test_sensor/
        └── test_sensor.cpp
```

**src/main.cpp** — adicione `#include <Arduino.h>` no topo:

```cpp
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>

#define I2C_SDA 4
#define I2C_SCL 5
#define SEALEVEL 1013.25

Adafruit_BMP280 bmp;
unsigned long last_sample = 0;

void setup() { /* ... */ }
void loop() { /* ... */ }
```

### 4. Criar módulo em lib/calc/

`lib/calc/SensorData.h`:

```cpp
#pragma once

struct SensorData {
    unsigned long timestamp_ms;
    float altitude_m;
    float temperatura_C;
    float pressao_hPa;

    bool isValid() const {
        return altitude_m >= -100 && altitude_m <= 10000
            && temperatura_C >= -40 && temperatura_C <= 85
            && pressao_hPa >= 300 && pressao_hPa <= 1100;
    }
};
```

### 5. Compilar e testar

```bash
# Build para ESP32-C3
pio run -e esp32c3

# Upload
pio run -e esp32c3 -t upload --upload-port /dev/ttyACM0

# Verificar saída no monitor
pio device monitor -b 115200
```

### 6. Extra: teste nativo

Crie um teste em `test/test_sensor/test_sensor.cpp`:

```cpp
#include <unity.h>
#include "SensorData.h"

void test_sensor_valido() {
    SensorData d { 0, 100.0f, 25.0f, 1013.25f };
    TEST_ASSERT_TRUE(d.isValid());
}

void test_sensor_altitude_invalida() {
    SensorData d { 0, 99999.0f, 25.0f, 1013.25f };
    TEST_ASSERT_FALSE(d.isValid());
}

void setup() {
    UNITY_BEGIN();
    RUN_TEST(test_sensor_valido);
    RUN_TEST(test_sensor_altitude_invalida);
    UNITY_END();
}

void loop() {}
```

Rode: `pio test -e native`

## Critérios de aceite

- [ ] Build sem erros (`pio run -e esp32c3`)
- [ ] Upload funciona e serial exibe dados
- [ ] Código organizado em `src/`, `lib/`, `test/`
- [ ] `platformio.ini` com dois ambientes (esp32c3 + native)
- [ ] Testes nativos passam (`pio test -e native`)
- [ ] Commit com prefixo `pio:`
- [ ] README com instruções de build

## Armadilhas comuns

- **Falta `#include <Arduino.h>`**: no PlatformIO, o `.ino` não existe mais — você precisa incluir manualmente
- **Pino errado**: as `build_flags` definem os pinos — use `I2C_SDA` em vez de `4` hardcoded
- **Biblioteca não encontrada**: confira se o nome em `lib_deps` está correto

## Conexão com projetos reais

O Helike usa PlatformIO com esta mesma estrutura: ambiente `helike_esp32c3` para firmware e `native` para testes. Os módulos em `lib/calc/` do Helike (VerticalVelocity, ApogeeDetection, DataValidation) seguem este mesmo padrão.

## Referências

- [Trilha PlatformIO](../trilhas/platformio.md)
- [Exemplo PlatformIO](../examples/platformio-exemplo.md)
- [Slide deck](../slides/semana-04.html)
- [Quiz](../quiz/semana-04.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-04.md)
