# Variável de sistema _FOXDOC

Incluída para compatibilidade com versões anteriores. Em seu lugar, use o Documenting Wizard.

Especifica o nome e o local do FoxDoc, o documentador automático de programas.

```foxpro
_FOXDOC = program name
```

# Observações

Com _FOXDOC, você pode especificar o programa que o FoxPro usa ao documentar programas do FoxPro. Por padrão, _FOXDOC usa FOXDOC.APP. Você pode incluir um caminho com o nome do programa.

Se optar por instalar o FoxDoc durante a instalação de programas suplementares, o FoxDoc e seus arquivos associados serão instalados no diretório do FoxPro. Se você renomear FOXDOC.APP ou mover o FoxDoc e seus arquivos associados para outro diretório, armazene o novo nome de arquivo FOXDOC.APP e o nome do diretório em _FOXDOC.

Para obter mais informações sobre o FoxDoc, consulte o capítulo "Documentando aplicativos com o FoxDoc" no Guia do Desenvolvedor do FoxPro.
