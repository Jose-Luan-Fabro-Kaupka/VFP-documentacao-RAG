# Referência de Objeto THISFORM

Fornece uma referência ao formulário atual em código de evento de formulário ou em uma definição de classe.

```foxpro
THISFORM.PropertyName | ObjectName
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade do formulário.
**ObjectName**
Especifica um objeto no formulário.

# Observações

THISFORM fornece uma maneira conveniente de se referir ao formulário atual ao escrever programas de tratamento de eventos em um formulário. Por exemplo, este programa do evento Click para um botão de comando define o caption do botão para a hora atual:

```foxpro
thisform.command1.caption = time()
```

Usar THISFORM em vez de se referir explicitamente ao formulário atual pelo nome (por exemplo, `form1.command1.caption`) torna o código de programa portável entre formulários.

Ao criar definições de classe, THISFORM também fornece um meio de se referir ao formulário atual dentro de um método. THISFORM permite referenciar um objeto no formulário ou propriedade sem usar várias propriedades Parent.
