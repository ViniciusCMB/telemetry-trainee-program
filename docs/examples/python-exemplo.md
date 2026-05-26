# Exemplo Minimo — Python

## Objetivo

Ler um CSV simples de telemetria e imprimir um resumo.

## Entrada (CSV)

```csv
timestamp_ms,altitude_m,ax,ay,az
0,0.0,0.01,0.02,9.81
50,0.5,0.02,0.01,9.80
100,1.2,0.03,0.01,9.79
```

## Saida esperada (exemplo)

```
Linhas: 3
Altitude media: 0.57 m
```

## Dica

Use `csv` da biblioteca padrao e calcule medias simples.
