# Como: formatar saída para campos

Você pode especificar o formato usado pelos valores em campos de tabelas de banco de dados quando esses valores aparecem em formulários, janelas browse ou relatórios. Você pode usar códigos e caracteres de formato para especificar o formato. Para obter mais informações sobre códigos e caracteres de formato, consulte a propriedade Format.

### Para especificar o formato para saída de campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer.
- Na guia Fields, selecione o campo desejado.
- Na caixa Format da área Display, digite os caracteres de formato desejados.

Para obter mais informações, consulte a guia Fields, Table Designer.

### Para especificar o formato para saída de campo programaticamente
- Use a função DBSETPROP( ) para definir a propriedade Format do campo.

Para obter mais informações, consulte a função DBSETPROP( ).

Por exemplo, o código a seguir especifica o formato de saída para um código postal:

```foxpro
DBSETPROP("Orders.Postalcode","Field","Format","@R 99999-9999")
```
