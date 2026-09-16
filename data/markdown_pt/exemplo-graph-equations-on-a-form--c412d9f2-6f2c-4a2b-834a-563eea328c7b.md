# Exemplo Graph Equations on a Form

Arquivo: ...\Samples\Solution\Forms\Graphics\Graph.scx

Este exemplo mostra como graficar equações com gráficos de formulário. O usuário pode dimensionar a equação escolhendo os botões de comando Zoom. O usuário também pode mover a origem do gráfico clicando e arrastando.

Os mecanismos de grafia deste exemplo estão em dois programas: Cgraph.prg e Pgraph.prg. CGRAPH grafica equações com base em coordenadas cartesianas. PGRAPH grafica equações com base em coordenadas polares. Esses programas usam os métodos PSet e Line de um formulário para desenhar a equação.

O código a seguir, associado ao método OneGraph do conjunto de formulários, executa o programa CGRAPH quando um usuário escolhe o botão Graph:

```foxpro
THISFORMSET.frmGraph.Draw
   DO cgraph WITH ;
      graph.equation, ;
      graph.step, ;
      graph.ecolor, ;
      graph.connect, ;
      THISFORMSET.nFormX, ;
      THISFORMSET.nFormY, ;
      .F., ;
      THISFORMSET.frmgraph, ;
      THISFORMSET.nFormScale
```

A tabela a seguir lista os parâmetros de CGRAPH:

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| equation | C | A equação em termos de X. Plota a resposta como Y. |
| step | N | Incremento de passo. |
| ecolor | N | Cor da equação. |
| connect | L | Se o ponto anterior é conectado ao ponto atual com uma linha. |
| nFormX | N | Ponto no formulário onde x = 0 |
| nFormY | N | Ponto no formulário onde y = 0 |
| lAddCoords | Se deve desenhar linhas de coordenadas. | |
| frmgraph | C | Nome do formulário no qual gravar. |
| nFormScale | N | Escala na qual graficar a equação. |
