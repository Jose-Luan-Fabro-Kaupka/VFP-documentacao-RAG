# Função CREATEBINARY( )

Converte dados de tipo caractere criados no Visual FoxPro em uma cadeia de caracteres de tipo binário que você pode passar a um controle ActiveX ou objeto de automação.

```foxpro
CREATEBINARY(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere para a qual uma cadeia de caracteres de tipo binário é retornada.

# Valor de retorno

Caractere

# Observações

Cadeias de caracteres do Visual FoxPro podem conter dados binários. No entanto, uma cadeia de caracteres de controle ActiveX ou objeto de automação (dados do tipo OLE VT_BSTR) não pode conter dados binários. Um controle ActiveX ou objeto de automação passa dados binários para aplicações como o Visual FoxPro como uma matriz de dados do tipo VT_UI1.

O Visual FoxPro converte automaticamente dados binários passados de um controle ActiveX ou objeto de automação como uma matriz de dados do tipo VT_UI1 em uma cadeia de caracteres do Visual FoxPro. O Visual FoxPro marca internamente essa cadeia de caracteres como dados binários passados de um controle ActiveX ou objeto de automação. Quando a cadeia de caracteres é passada de volta a um controle ActiveX ou objeto de automação, o Visual FoxPro converte automaticamente a cadeia de caracteres em uma matriz de dados do tipo VT_UI1 que o controle ActiveX ou objeto de automação espera.

Use CREATEBINARY( ) para converter dados de tipo caractere criados no Visual FoxPro em uma cadeia de caracteres de tipo binário que você pode passar a um controle ActiveX ou objeto de automação. O número mínimo de caracteres para o qual CREATEBINARY( ) pode ser abreviado é 7.

Para mais informações sobre controles ActiveX e objetos de automação, consulte Compartilhando informações e adicionando OLE.
