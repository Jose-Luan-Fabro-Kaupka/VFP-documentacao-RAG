# Variável de sistema _INCSEEK

Especifica o intervalo de tempo aberto para pressionamentos de tecla dentro de uma busca incremental, como em um controle Listbox ou ComboBox.

```foxpro
_INCSEEK = nTicks
```

#### Parâmetros
 **nTicks**
Especifica o intervalo de tempo em segundos. A medição de tempo interna é feita em "ticks" do relógio, que são cada um cerca de 1/18 de segundo. Se você armazenar um valor inteiro ou decimal em _INCSEEK, o Visual FoxPro pode armazená-lo como um valor ligeiramente diferente devido ao arredondamento para ticks. _INCSEEK pode variar de 0,05 a 5,5 segundos (1 a 100 ticks).

# Observações

Aplica-se a: Propriedade IncrementalSearch

Em versões anteriores do Visual FoxPro, o valor de _DBLCLICK também determinava o intervalo de busca incremental. O valor padrão de _INCSEEK é 0,50.
