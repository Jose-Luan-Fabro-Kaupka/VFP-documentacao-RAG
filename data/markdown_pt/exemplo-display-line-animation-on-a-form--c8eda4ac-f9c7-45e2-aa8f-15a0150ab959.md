# Exemplo Display Line Animation on a Form

Arquivo: ...\Samples\Solution\Forms\Graphics\Anim.scx

Este exemplo ilustra o desenho de linhas em um formulário. Mais especificamente, demonstra salvar coordenadas de conjuntos de linhas desenhadas em um formulário e redesenhá-las, junto com linhas adicionais em posições intermediárias, dando a ilusão de movimento.

# Adicionando linhas à tabela

Cada vez que um usuário desenha uma linha no formulário, suas coordenadas são armazenadas em uma tabela com a seguinte estrutura:

| Nome | Tipo | Descrição |
| --- | --- | --- |
| Frameno | I | Incrementado cada vez que o usuário escolhe New Frame. |
| Objno | I | Incrementado cada vez que uma linha é adicionada a um frame. |
| X1 | I | A coordenada X inicial de uma linha. |
| X2 | I | A coordenada X final de uma linha. |
| Y1 | I | A coordenada Y inicial de uma linha |
| Y2 | I | A coordenada Y final de uma linha. |

# Reproduzindo os frames

O código a seguir reproduz os frames, usa a tabela novamente em outra área de trabalho, seleciona a segunda área de trabalho e vai para o próximo frame:

```foxpro
USE (lcTable) AGAIN IN 0 ALIAS shadow
SELECT shadow
LOCATE FOR frameno # &lcTable..frameno
```

A variável nBetween determina quantas linhas intermediárias são desenhadas no formulário entre uma linha em um frame e a linha correspondente no próximo frame.

```foxpro
FOR nb = 1 TO nBetween
```

Dentro do loop FOR, o código faz scan de todas as linhas associadas a um frame e calcula coordenadas para as linhas intermediárias, por exemplo:

```foxpro
nx1 = frames.x1 + nb * (shadow.x1 - frames.x1) / nBetween
ny1 = frames.y1 + nb * (shadow.y1 - frames.y1) / nBetween
```

O código então imprime cada linha intermediária e, após um WAIT de .05 segundos, limpa o formulário e continua o loop.

```foxpro
THISFORMSET.frmAnimation.line(nx1,ny1,nx2,ny2)
```
