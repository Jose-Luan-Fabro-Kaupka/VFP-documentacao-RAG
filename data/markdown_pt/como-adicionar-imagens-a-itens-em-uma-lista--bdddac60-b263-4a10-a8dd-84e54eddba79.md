# Como: adicionar imagens a itens em uma lista

Você pode exibir imagens ao lado de itens em listas.

### Para exibir imagens ao lado de itens em uma lista
- Defina a propriedade Picture como um arquivo gráfico para a caixa de lista.

Para obter mais informações, consulte Picture Property (Visual FoxPro) e Graphics Support in Visual FoxPro.

Por exemplo, suponha que você preencha uma caixa de lista com arquivos e deseje exibir um arquivo gráfico diferente ao lado de cada arquivo, dependendo se o arquivo é uma tabela, um programa ou outro tipo de arquivo.
 List box with pictures

O código a seguir usa o comando FOR ... ENDFOR para

exibir um arquivo gráfico diferente para cada item na lista e aparece no evento Click desta caixa de lista:

```foxpro
FOR iItem = 5 TO THIS.ListCount      && files start at the 5th item
   cExtension = UPPER(RIGHT(THIS.List(iItem),3))
   DO CASE
      CASE cExtension = "DBF"
         THIS.Picture(iItem) = "tables.bmp"
      CASE cExtension = "BMP"
         THIS.Picture(iItem) = "other.bmp"
      CASE cExtension = "PRG"
         THIS.Picture(iItem) = "programs.bmp"
      CASE cExtension = "SCX"
         THIS.Picture(iItem) = "form.bmp"
      OTHERWISE
         THIS.Picture(iItem) = IIF("]" $ cExtension, ;
            "", "textfile.bmp")
   ENDCASE
ENDFOR
```

Para obter mais informações, consulte Click Event.
