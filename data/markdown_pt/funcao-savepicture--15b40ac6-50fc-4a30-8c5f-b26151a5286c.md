# Função SAVEPICTURE( )

Cria um arquivo de bitmap (.bmp) a partir de uma referência a objeto de imagem.

```foxpro
SAVEPICTURE(oObjectReference, cFileName)
```

#### Parâmetros
 **oObjectReference**
Especifica a referência a objeto de imagem da qual SAVEPICTURE( ) cria o arquivo de bitmap.
**cFileName**
Especifica o nome do arquivo de bitmap criado por SAVEPICTURE( ). Se cFileName incluir um caminho, o arquivo será criado no diretório indicado. Se já existir um arquivo com o mesmo nome, ele será sobrescrito sem aviso, mesmo que SET SAFETY esteja ON.

# Valor de retorno

Logical

# Observações

Referências a objetos de imagem normalmente são criadas com LOADPICTURE( ). No entanto, determinadas propriedades, como PictureOpen do controle OLE Outline, usam uma referência padrão que pode ser usada para criar um arquivo de bitmap.
