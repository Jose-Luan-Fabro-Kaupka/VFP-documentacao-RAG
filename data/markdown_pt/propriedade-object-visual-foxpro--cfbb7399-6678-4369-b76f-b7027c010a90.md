# Propriedade Object (Visual FoxPro)

Fornece acesso às propriedades e métodos do servidor Automation para um objeto OLE. Não disponível em tempo de design. Dependendo do servidor Automation, as propriedades do objeto OLE podem ser somente leitura ou leitura/gravação em tempo de execução.

```foxpro
OLEObject.Object[.Property] [= eValue]
-or-
OLEObject.Object[.Method]
```

# Valor de retorno
 **Property**
Especifica uma propriedade que o servidor Automation suporta para o objeto OLE.
**eValue**
Especifica um valor para uma propriedade que o servidor Automation suporta para o objeto OLE.
**Method**
Especifica um método que o servidor Automation suporta para o objeto OLE

# Observações

Aplica-se a: OLE Bound Control | OLE Container Control

Para obter informações sobre as propriedades e métodos suportados pelo servidor Automation, consulte a documentação do aplicativo habilitado para OLE que criou o objeto. Por exemplo, se o objeto OLE for uma planilha do Microsoft Excel, consulte a documentação do Excel para as propriedades e métodos suportados pelo Excel (um aplicativo habilitado para OLE).
