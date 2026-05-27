```mermaid
graph TD
    subgraph Treinamento
        S0[Semana 0<br>Onboarding & Git]
        S1[Semana 1<br>Python básico]
        S2[Semana 2<br>Python aplicado]
        S3[Semana 3<br>Arduino IDE]
        S4[Semana 4<br>PlatformIO]
        S5[Semana 5<br>Integração Python ↔ Arduino]
        S6[Semana 6<br>KiCad]
        S7[Semana 7<br>Projetos Reais]
        S8[Semana 8<br>Capstone]
    end

    subgraph Projetos
        FC[Flight Computer]
        HELIKE[Helike PocketQube]
    end

    S0 --> S1
    S1 --> S2 --> S5
    S3 --> S4 --> S5
    S5 --> S8
    S6 --> S8
    S7 --> S8

    S0 -.->|fluxo git| FC
    S0 -.->|fluxo git| HELIKE
    S1 -.->|análise de dados| FC
    S2 -.->|parser e validação| FC
    S2 -.->|parser| HELIKE
    S3 -.->|GPIO, I2C, sensores| FC
    S3 -.->|I2C, sensores| HELIKE
    S4 -.->|estrutura PlatformIO| HELIKE
    S5 -.->|pipeline telemetria| FC
    S6 -.->|PCB| HELIKE

    style Treinamento fill:#1c2333,stroke:#ff6b35,color:#e6edf3
    style Projetos fill:#1c2333,stroke:#2ea043,color:#e6edf3
    style S0 fill:#ff6b35,color:#fff
    style S8 fill:#ff6b35,color:#fff
    style FC fill:#2ea043,color:#fff
    style HELIKE fill:#2ea043,color:#fff
```

## Conexão das semanas

| Semana | Habilidades | Projeto real |
|---|---|---|
| 0 | Git, GitHub, PRs | Fluxo de desenvolvimento de ambos |
| 1 | Python: CSV, estatísticas | Análise pós-voo do FC |
| 2 | Python: parser, validação | Parsing de telemetria do Helike |
| 3 | Arduino: GPIO, I2C, serial | Testes de hardware de ambos |
| 4 | PlatformIO: estrutura, testes | Organização do firmware Helike |
| 5 | Integração Arduino ↔ Python | Pipeline de telemetria do FC |
| 6 | KiCad: esquemático, ERC | CDB do Helike |
| 7 | Arquitetura de sistemas | Visão geral de ambos |
| 8 | Pipeline completo | Síntese de tudo |
