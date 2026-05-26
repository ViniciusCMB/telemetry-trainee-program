# Exemplo Minimo — Arduino IDE

## Objetivo

Enviar um pacote simples pela serial com leituras simuladas.

## Formato do pacote (exemplo)

```
T=1234,ALT=12.3,AX=0.01,AY=0.02,AZ=9.81
```

## Resultado esperado

- Serial Monitor exibindo pacotes a cada 1s

## Dica

Use `millis()` para controlar o intervalo.
