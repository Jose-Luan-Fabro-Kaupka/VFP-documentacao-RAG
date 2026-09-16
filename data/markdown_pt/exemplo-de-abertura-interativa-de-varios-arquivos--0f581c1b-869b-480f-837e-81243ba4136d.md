# Exemplo de abertura interativa de vários arquivos

Arquivo: ...\Samples\Solution\Controls\Lists\Multfile.scx

Este exemplo mostra como preencher uma lista com arquivos. Ao preencher uma lista com arquivos, a funcionalidade interna permite ao usuário selecionar novas unidades e diretórios. Neste exemplo, o usuário pode selecionar um ou mais arquivos na lista e abri-los para edição.

O código a seguir percorre os itens da caixa de listagem e abre os arquivos selecionados para edição:

```foxpro
FOR nFile = 5 to THISFORM.lstFiles.ListCount
   IF THISFORM.lstFiles.Selected(nFile)
      MODIFY FILE (THISFORM.lstFiles.List(2) + ;
         THISFORM.lstFiles.List(nFile)) NOWAIT
   ENDIF
ENDFOR
```

Quando a propriedade RowSourceType é definida como 7 - Files:
 - lstFiles.List(1) refere-se à unidade.
- lstFiles.List(2) refere-se ao caminho.
- lstFiles.List(3) é uma linha separadora.
- lstFiles.List(4) é [..]. Clique para ir ao diretório pai.

Os arquivos podem começar em lstFiles.List(5)
