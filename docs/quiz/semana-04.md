# Quiz — Semana 4: PlatformIO

## Questões

### 1. (Múltipla escolha) Qual seção do `platformio.ini` é usada para definir configurações que se aplicam a todos os ambientes?
- a) `[env]`
- b) `[platformio]`
- c) `[common]`
- d) `[default]`

### 2. (Verdadeiro ou Falso) A diretiva `lib_deps` no `platformio.ini` baixa e instala bibliotecas automaticamente, enquanto a instalação manual requer copiar arquivos para a pasta `lib/`.
- Verdadeiro / Falso

### 3. (Múltipla escolha) Qual é a diferença entre as pastas `src/` e `lib/` em um projeto PlatformIO?
- a) `src/` contém o código-fonte principal; `lib/` contém bibliotecas (próprias ou de terceiros)
- b) `src/` contém bibliotecas; `lib/` contém o código principal
- c) Ambas contêm a mesma coisa
- d) `lib/` é para arquivos binários compilados

### 4. (Resposta curta) O que é o Unity Test Framework e como ele é usado no PlatformIO?

### 5. (Múltipla escolha) Para que serve a opção `build_flags` no `platformio.ini`?
- a) Definir flags de compilação adicionais (ex.: `-DDEBUG`)
- b) Definir a velocidade do processador
- c) Configurar o nome do firmware
- d) Alterar a taxa de transmissão serial

### 6. (Resposta curta) Explique a diferença entre um ambiente `native` e um ambiente embarcado (ex.: `teensy41`) no PlatformIO.

### 7. (Verdadeiro ou Falso) No PlatformIO, é possível ter múltiplos ambientes de build no mesmo `platformio.ini`.
- Verdadeiro / Falso

### 8. (Múltipla escolha) Qual opção no `platformio.ini` especifica o microcontrolador alvo (ex.: ESP32, STM32)?
- a) `board = `
- b) `platform = `
- c) `framework = `
- d) `target = `

## Respostas

### 1. a) `[env]`
### 2. Verdadeiro
### 3. a) `src/` contém o código-fonte principal; `lib/` contém bibliotecas (próprias ou de terceiros)
### 4. Unity é um framework de testes unitários em C. No PlatformIO, usa-se a test framework `unity` e os testes vão na pasta `test/` com funções `TEST_ASSERT_*`.
### 5. a) Definir flags de compilação adicionais (ex.: `-DDEBUG`)
### 6. O ambiente `native` compila para o sistema do computador (Linux/Windows/macOS) para testes rápidos. O ambiente embarcado compila para o microcontrolador alvo com seu conjunto de instruções e limitações específicas.
### 7. Verdadeiro
### 8. a) `board = `
