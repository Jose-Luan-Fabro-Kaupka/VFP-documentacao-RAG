# Referência de objeto THISFORMSET

Fornece uma referência ao conjunto de formulários atual em código de evento ou em uma definição de classe.

```foxpro
THISFORMSET.PropertyName | ObjectName
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade do conjunto de formulários.
**ObjectName**
Especifica um objeto no conjunto de formulários.

# Observações

THISFORMSET fornece uma maneira conveniente de referenciar o conjunto de formulários atual ao escrever programas de tratamento de eventos em um formulário. Usar THISFORMSET em vez de referenciar explicitamente o formulário atual pelo nome (por exemplo, `form1.command1.caption`) torna o código do programa portável entre formulários.

Ao criar definições de classe, THISFORMSET também fornece um meio de referenciar o conjunto de formulários atual dentro de um método. THISFORMSET permite referenciar um objeto no formulário ou uma propriedade sem usar várias propriedades Parent.
