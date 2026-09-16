# Variável de sistema _DBLCLICK

Especifica o intervalo de tempo entre cliques duplos e triplos do mouse.

```foxpro
_DBLCLICK = nTicks
```

#### Parâmetros
 **nTicks**
Especifica o intervalo de tempo em segundos. A medição interna de tempo é feita em "ticks" de relógio, cada um com cerca de 1/18 de segundo. Se você armazenar um valor inteiro ou decimal em _DBLCLICK, o Visual FoxPro pode armazená-lo como um valor ligeiramente diferente devido ao arredondamento para ticks. Na inicialização do Visual FoxPro, a configuração de clique duplo no Painel de Controle Propriedades do Mouse do Windows determina o valor padrão de _DBLCLick. _DBLCLICK pode variar de 0,05 a 5,5 segundos (1 a 100 ticks). _DBLCLICK se aplica apenas à taxa de clique duplo e não ao período de captura de tecla de pesquisa incremental como em versões do Visual FoxPro anteriores à versão 7.

# Observações

A configuração de _DBLCLICK substitui a configuração especificada no Painel de Controle do Mouse do Windows.

_DBLCLICK contém um valor numérico que determina o intervalo de tempo que o Visual FoxPro usa para verificar um clique duplo ou triplo do mouse. _DBLCLICK é o intervalo de tempo entre cliques do mouse. Por exemplo, se _DBLCLICK estiver definido como 0,5 segundos, você tem meio segundo para clicar duas vezes para um clique duplo e 1 segundo para clicar três vezes para um clique triplo.

Quanto maior o valor de _DBLCLICK, mais tempo você pode esperar entre o primeiro e o segundo clique para o Visual FoxPro interpretar os dois cliques como um clique duplo. Se _DBLCLICK estiver definido com um valor muito pequeno, mesmo cliques duplos (ou triplos) rápidos podem ser interpretados como dois (ou três) cliques simples.
