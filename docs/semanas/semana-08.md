# Semana 8 — Capstone

## Objetivo

Integrar tudo que você aprendeu em um pipeline end-to-end de telemetria. Da geração dos dados no Arduino até a análise final em Python.

## Preparação

- [ ] Semanas 0 a 7 concluídas
- [ ] ESP32-C3 + BMP280 montados na protoboard
- [ ] Ver o [Slide deck](../slides/semana-08.html)
- [ ] Fazer o [Quiz](../quiz/semana-08.md)

## Tarefas

### Pipeline completo

### Fase 1: Arduino — aquisição e transmissão

Configure o ESP32-C3 para:

1. Ler BMP280 a **20 Hz** via I2C
2. Piscar o LED como heartbeat (1 Hz)
3. Enviar pacotes formatados pela serial:

```
#timestamp_ms;altitude_m;ax;ay;az;temperatura_C;pressao_hPa#
```

4. Calcular e incluir um **checksum simples** no pacote
5. Incluir **detecção de apogeu** (se altitude cair 3 amostras consecutivas, aciona um LED de aviso)

### Fase 2: Python — recepção, parsing e logging

Crie um script Python que:

1. Conecta na serial do ESP32-C3
2. Parseia cada pacote em tempo real
3. Valida os campos (range físico, checksum)
4. Salva em CSV com timestamp do sistema
5. Mostra estatísticas ao vivo a cada 50 pacotes:

```
[10:30:15] 150 pacotes | 142 OK | 5 parser err | 3 val rej | 94.7%
```

### Fase 3: Python — análise

Após coletar pelo menos 200 pacotes, gere:

1. **Resumo estatístico** (média, max, min de cada campo)
2. **Gráfico de altitude × tempo** (salvar como PNG)
3. **Detecção de apogeu** marcada no gráfico

### Fase 4: Documentação

Crie um README.md completo:

```markdown
# Pipeline de Telemetria — Capstone

## Como executar

### Arduino
1. Conecte o ESP32-C3 via USB
2. Faça upload do firmware
3. Verifique LEDs e serial

### Python
```bash
python3 receptor.py
```

## Resultados

Gráfico de altitude: ![perfil](perfil_voo.png)

## Estatísticas
| Métrica | Valor |
|---|---|
| Amostras | 200 |
| Taxa | 20 Hz |
| Pacotes OK | 95% |

## Lições aprendidas
- O que foi mais difícil?
- O que você faria diferente?
```

## Critérios de aceite

- [ ] Arduino envia pacotes a 20 Hz com checksum
- [ ] Python recebe e loga sem perder pacotes
- [ ] Gráfico de altitude gerado
- [ ] Apogeu detectado e marcado
- [ ] README completo com instruções e resultados
- [ ] Repositório organizado (src/, lib/, test/ se PlatformIO)
- [ ] Commits com tipo semântico (`feat:`, `build:`, `docs:`, `fix:`, `test:`, ...)

## Entregáveis

```
capstone/
├── firmware/               # Código do Arduino/PlatformIO
│   ├── src/main.cpp
│   └── platformio.ini
├── script/                 # Código Python
│   ├── receptor.py
│   ├── analise.py
│   └── requirements.txt
├── dados/
│   └── log_telemetria.csv
├── resultados/
│   └── perfil_voo.png
└── README.md
```

## Avaliação

O capstone será avaliado em:

| Critério | Peso |
|---|---|
| Pipeline funcional | 40% |
| Qualidade do código | 25% |
| Documentação | 20% |
| Organização do repo | 15% |

## Referências

- [Trilha Python](../trilhas/python.md)
- [Trilha Arduino IDE](../trilhas/arduino-ide.md)
- [Trilha PlatformIO](../trilhas/platformio.md)
- [Slide deck](../slides/semana-08.html)
- [Quiz](../quiz/semana-08.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-08.md)
