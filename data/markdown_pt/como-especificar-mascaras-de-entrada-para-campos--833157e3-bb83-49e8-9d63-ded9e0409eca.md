# Como: especificar máscaras de entrada para campos

Você pode tornar possível inserir e armazenar valores em campos de tabelas de banco de dados de maneira uniforme, reduzindo erros de entrada de dados e tornando o processamento mais eficiente. Você pode fazer isso definindo a pontuação, o espaçamento e outros atributos de formato para valores inseridos em um campo usando uma máscara de entrada.

Por exemplo, você pode tornar possível inserir e armazenar números de telefone em um campo adicionando uma máscara de entrada apropriada para números de telefone a um campo numérico, por exemplo (999) 999-9999. A máscara de entrada ajuda o usuário a inserir números de telefone mais rapidamente porque a formatação é fornecida. Para mais informações sobre caracteres de máscara de entrada, consulte InputMask Property.

### Para especificar uma máscara de entrada para um campo
- Abra o banco de dados que contém a tabela.
- Abra a tabela no Table Designer (Visual FoxPro).
- Na guia Fields, selecione o campo desejado.
- Na caixa Input mask da área Display, digite os caracteres de máscara de entrada desejados.

Para mais informações, consulte Fields Tab, Table Designer.

### Para especificar uma máscara de entrada para um campo programaticamente
- Use a função DBSETPROP( ) para definir a propriedade InputMask do campo.

Para mais informações, consulte DBSETPROP( ) Function.

Por exemplo, o código a seguir especifica uma máscara de entrada para uma data:

```foxpro
DBSETPROP("Orders.Postalcode","Field","InputMask", "99999-9999")
```
