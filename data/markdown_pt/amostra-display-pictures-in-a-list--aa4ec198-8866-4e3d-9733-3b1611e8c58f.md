# Amostra Display Pictures in a List

Arquivo: ...\Samples\Solution\Controls\Lists\Piclist.scx

Esta amostra ilustra como você pode aprimorar suas list boxes adicionando gráficos de imagem ao lado dos itens de texto individuais. Nesta amostra, você pode escolher qualquer arquivo de banco de dados (.dbc), e a list box mostrará imagens diferentes ao lado dos nomes de tabelas, local views e remote views.

O código a seguir de cmdDatabase.Click enumera um .dbc e adiciona seletivamente imagens aos itens da lista usando a propriedade Picture. A propriedade Picture depende de uma configuração de índice para determinar qual item da lista afetar.

```foxpro
FOR i = (m.nTblCount+1) TO thisform.lstDatabase.ListCount
IF DBGETPROP(ALLTRIM(thisform.lstDatabase.List[m.i]),; "view","sourcetype") = 1
       *Local view
      thisform.lstDatabase.Picture[m.i] = m.cLViewBMP
   ELSE
      * Remote view
      thisform.lstDatabase.Picture[m.i] = m.cRViewBMP
   ENDIF
ENDFOR
```

> **Observação:** Você precisa garantir que as imagens usadas tenham o tamanho correto para caber no espaço de um único item de list box, o que difere com o FontSize da lista.
