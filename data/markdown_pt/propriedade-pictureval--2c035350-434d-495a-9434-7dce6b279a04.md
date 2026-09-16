# Propriedade PictureVal

Especifica uma expressão de cadeia de caracteres ou objeto que representa uma imagem para o controle Image.

```foxpro
Image.PictureVal [= eExpression]
```

# Valor de retorno
 **eExpression**
Especifica uma expressão de cadeia de caracteres ou objeto que representa uma imagem. Se eExpression for uma expressão de cadeia de caracteres, ela deve ser uma expressão válida que o GDI+ possa usar para renderizar uma imagem. Por exemplo, pode ser uma expressão derivada de código como no exemplo a seguir. cPict = FILETOSTR('myimage.bmp') oForm.Img1.PictureVal = cPict eExpression também pode ser uma expressão de cadeia de caracteres que representa um campo do tipo memo ou blob contendo dados binários estritos. Por exemplo, você pode usar o Comando APPEND MEMO para importar uma imagem em um campo memo. Você não pode usar um campo do tipo general para eExpression porque campos general armazenam dados binários adicionais não relacionados. Se eExpression for um objeto, o objeto deve implementar uma das seguintes interfaces: "Picture" ou "IPicture". A interface padrão "Picture" é a mesma retornada pela Função LOADPICTURE( ) . Se você precisar da interface "IPicture", pode obtê-la usando a Função GETINTERFACE() . oPict = LOADPICTURE("myimage.bmp") oForm.img1.PictureVal = oPict * or oPict = LOADPICTURE("myimage.bmp") oIPicture = GETINTERFACE(oPicture, 'iPicture') oform.img.PictureVal = oIPicture && IPICTURE is a secondary interface that can be useful calling COM objects.

# Observações

Aplica-se a: Controle Image (Visual FoxPro)

A propriedade PictureVal tem precedência sobre a Propriedade Picture (Visual FoxPro) se ambas estiverem especificadas.

Observe que o Visual FoxPro usa somente a memória necessária para renderizar uma imagem quando a imagem é armazenada em um campo memo ou blob. Esta é uma forma eficiente em memória de exibir imagens no Visual FoxPro. No entanto, usar uma referência de arquivo na propriedade PictureVal exige que o Visual FoxPro use até duas vezes a quantidade de memória do tamanho do arquivo. Por exemplo, se você referenciar um arquivo de imagem de 5 MB, o Visual FoxPro requer até 10 MB de memória para exibir o arquivo.

Você não pode especificar um arquivo de máscara (MSK) com a propriedade PictureVal. Se você estiver usando imagens BMP e desejar uma máscara, deve usar a propriedade Picture. Você também pode usar um formato de imagem diferente, como GIF, que possui transparência definida na imagem.
