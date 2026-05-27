# Semana 7 — Contexto dos projetos (Flight Computer + Helike)

## Objetivo

Entender a arquitetura dos dois projetos principais do setor — Flight Computer e satélite Helike — e como o que você aprendeu se conecta com eles.

## Preparação

- [ ] Semanas 0 a 6 concluídas
- [ ] Acesso aos repositórios: `flight-computer` e `satellite`
- [ ] Ver o [Slide deck](../slides/semana-07.html)
- [ ] Fazer o [Quiz](../quiz/semana-07.md)

## Tarefas

### 1. Resumo do Flight Computer

Explore o repositório do Flight Computer e responda:

**Arquitetura:**
- Qual o microcontrolador usado? E o barômetro? E a IMU?
- Quais protocolos de comunicação são usados (I2C, SPI, UART)?
- Como é a FSM de voo (IDLE → ASCENT → DESCENT → LANDED)?
- O que dispara o paraquedas?

**Código:**
- Como os sensores são organizados (v1.0 procedural vs v2.0 OOP)?
- O que é a interface `ISensor`?
- Como os dados são logados (SD, LittleFS)?
- Como a telemetria é transmitida (LoRa)?

**Crie um resumo de 1 página** com:
- Diagrama da arquitetura (pode ser ASCII ou Mermaid)
- Tabela de hardware (componente, interface, função)
- Mapa conceitual: como os dados fluem (sensor → processamento → log → LoRa)

### 2. Resumo do Helike (satélite PocketQube)

Explore o repositório do satélite Helike e responda:

**Arquitetura:**
- Qual o formato do satélite (PocketQube 1P)?
- Qual o microcontrolador? Quais sensores?
- Como é o sistema de recuperação (SRAB)?
- Qual a frequência do LoRa?

**Código:**
- Como o projeto está organizado (PlatformIO)?
- O que tem em `lib/calc/`?
- Como os testes são estruturados (Unity)?
- O que são os `test_hardware/`?

**Crie um resumo de 1 página** com:
- Diagrama do satélite (componentes principais)
- Tabela de sensores e interfaces
- Fluxo de dados: sensor → firmware → SD → LoRa → estação terrestre

### 3. Mapa conceitual

Crie um mapa (Mermaid, draw.io, ou diagrama de caixas) mostrando:

```
SENSORES (I2C/SPI/UART)
    ↓
FIRMWARE (ESP32-C3, FreeRTOS)
    ↓
LOG (SD / LittleFS)  ──→  LORA (RFM95W)
    ↓                        ↓
PÓS-VOO (Python)        ESTAÇÃO TERRESTRE
```

Destaque onde cada semana do treinamento se encaixa:

| Semana | Onde se aplica |
|---|---|
| 0, GitHub | Fluxo de desenvolvimento de ambos os projetos |
| 1, 2, Python | Análise pós-voo, simulação SRAB |
| 3, Arduino IDE | Testes de hardware, prototipação |
| 4, PlatformIO | Estrutura do Helike |
| 5, Integração | Pipeline de telemetria |
| 6, KiCad | CDB do Helike, PCB do FC |

## Critérios de aceite

- [ ] Resumo do Flight Computer com diagrama e tabela de hardware
- [ ] Resumo do Helike com diagrama e fluxo de dados
- [ ] Mapa conceitual mostrando a conexão entre as áreas
- [ ] Commits com tipo semântico (ex: `docs:`, `feat:`, `refactor:`)
- [ ] README com links para os repositórios

## Dicas

- Não precisa entender cada linha de código — foque na arquitetura e no fluxo de dados
- Use os `docs/` de cada repositório (em especial `software.md` e `hardware.md`)
- O slide deck tem diagramas prontos que podem ajudar

## Referências

- [Repositório Flight Computer](https://github.com/ViniciusCMB/flight-computer)
- [Repositório Helike](https://github.com/ViniciusCMB/satellite)
- [Slide deck](../slides/semana-07.html)
- [Quiz](../quiz/semana-07.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-07.md)
