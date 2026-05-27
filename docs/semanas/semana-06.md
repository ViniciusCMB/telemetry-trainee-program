# Semana 6 — KiCad básico

## Objetivo

Criar um esquemático de MCU + sensor I2C no KiCad, rodar ERC e exportar PDF. É o primeiro passo para projetar sua própria placa.

## Preparação

- [ ] KiCad 8+ instalado
- [ ] Ler a [Trilha KiCad](../trilhas/kicad.md) (seções 1 a 5)
- [ ] Ver o [Slide deck](../slides/semana-06.html)
- [ ] Fazer o [Quiz](../quiz/semana-06.md)

## Tarefas

### 1. Criar projeto

File → New → Project → `semana-6-kicad`

O KiCad cria automaticamente:
- `semana-6-kicad.kicad_pro` (projeto)
- `semana-6-kicad.kicad_sch` (esquemático)
- `semana-6-kicad.kicad_pcb` (PCB)

### 2. Adicionar componentes

Abra o Eeschema e adicione:

| Componente | Símbolo | Quantidade |
|---|---|---|
| ESP32-C3 (ou conector para módulo) | Criar símbolo ou usar conector | 1 |
| BMP280 | `Sensor_Temperature:BMP280` | 1 |
| Resistor | `Device:R` (10k) | 2 |
| Capacitor | `Device:C_Small` (100nF) | 1 |
| Conector 2x4 | `Connector:Conn_02x04` | 1 |

### 3. Fazer as conexões

Conecte os componentes:

```
BMP280:
  VCC → 3.3V
  GND → GND
  SDA → label I2C_SDA (conectado ao ESP)
  SCL → label I2C_SCL (conectado ao ESP)

Pull-ups:
  R1 entre I2C_SDA e 3.3V (10k)
  R2 entre I2C_SCL e 3.3V (10k)

ESP32-C3:
  GPIO4 → I2C_SDA
  GPIO5 → I2C_SCL
  3.3V → alimentação
  GND → terra

C1 (100nF):
  entre 3.3V e GND (próximo ao ESP)
```

### 4. Power flags

Coloque `PWR_FLAG` no 3.3V e no GND (Place → Power Port → PWR_FLAG). Sem eles, o ERC acusa erro de alimentação.

### 5. Anotar e verificar ERC

1. Tools → Annotate Schematic (autonumera R1, R2, C1, U1...)
2. Inspect → Electrical Rules Check
3. Corrija todos os erros (não warnings)

**ERCs comuns e soluções:**

| Erro | Causa | Solução |
|---|---|---|
| "Power pin not connected" | Faltou PWR_FLAG | Adicione PWR_FLAG em VCC e GND |
| "Input pin not driven" | Pino de entrada flutuando | Conecte a um net ou adicione pull-up |
| "Pin connected to other pin" | Dois outputs ligados | Revise a conexão |

### 6. Exportar PDF

File → Plot → selecione "PDF" → Plot current page → salve como `esquematico.pdf`

### 7. Extra: PCB simples

Vá para o Pcbnew (F8 para importar do esquemático):

1. Posicione os componentes (não sobreponha)
2. Roteie VCC (0.5mm) e GND (0.5mm) primeiro
3. Roteie SDA e SCL (0.25mm)
4. Adicione um plano de GND (Zones → Add Filled Zone)
5. Exporte Gerber

## Critérios de aceite

- [ ] Esquemático com todos os componentes e conexões
- [ ] ERC sem erros críticos
- [ ] PDF do esquemático exportado
- [ ] Componentes com footprints atribuídos
- [ ] Commit com tipo semântico (ex: `feat:`, `docs:`, `raw:`)
- [ ] README descrevendo o circuito

## Armadilhas comuns

- **PWR_FLAG esquecido**: o ERC não passa sem ele — é o erro mais comum
- **Pull-ups I2C faltando**: sem os resistores de 10k, o barramento I2C não funciona
- **Símbolo vs footprint**: símbolo é a representação lógica, footprint é o físico na PCB — os dois precisam estar corretos

## Conexão com projetos reais

O CDB do Helike (`hardware/CDB/`) tem um esquemático real no KiCad com ESP32-C3 + ICM-20602 + BME280 + RFM95W + GPS. Seu esquema desta semana é uma versão reduzida que usa o mesmo barramento I2C e os mesmos conceitos.

## Referências

- [Trilha KiCad](../trilhas/kicad.md)
- [Exemplo KiCad](../examples/kicad-exemplo.md)
- [Slide deck](../slides/semana-06.html)
- [Quiz](../quiz/semana-06.md)
- [Issue semanal (exemplo)](../issues-semanais/issue-semana-06.md)
