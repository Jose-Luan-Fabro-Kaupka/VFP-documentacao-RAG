# Propriedade OLETypeAllowed

Retorna o tipo de objeto OLE (incorporado ou vinculado) contido em um controle. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Control.OLETypeAllowed[ = nValue]
```

# Valor de retorno
 **nValue**
Retorna um valor que indica o tipo de objeto OLE (incorporado ou vinculado) contido em um controle. Os valores possíveis são 0 (Vinculado), 1 (Incorporado), –1 (um controle OLE Bound que não contém um objeto OLE) e –2 (controle ActiveX (.ocx)).

# Observações

Aplica-se a: controle OLE Bound | controle OLE Container

OLETypeAllowed é útil apenas quando você especifica uma configuração para a propriedade DocumentFile.

> **Observação:** Você pode definir a propriedade OLETypeAllowed em código para criar um objeto OLE vinculado usando o comando DEFINE CLASS.
