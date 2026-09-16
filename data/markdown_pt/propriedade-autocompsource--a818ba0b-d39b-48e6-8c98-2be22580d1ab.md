# Propriedade AutoCompSource

Especifica o campo Source na tabela que rastreia texto para a funcionalidade de preenchimento automático em um controle Text box. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
cTextbox.AutoCompSource [= cValue]
```

# Valor de retorno
 **cValue**
Nome do campo na tabela de preenchimento automático associada à text box.

# Observações

Aplica-se a: TextBox Control (Visual FoxPro)

Especifica o nome Source usado para procurar dados na tabela AutoComp. Este campo não diferencia maiúsculas de minúsculas e é armazenado em maiúsculas na tabela AutoComp.

Quando entradas são gravadas ou lidas da tabela AutoComp, elas usam uma chave, que é o campo Source. Por padrão, se esta propriedade não for especificada, o nome da text box se torna o valor de chave nesse campo da tabela AutoComp.

Você pode escrever aplicativos que usam uma única tabela AutoComp que fornece valores a vários controles text box dentro de um único aplicativo.

O campo Source na tabela AutoComp é limitado a 20 caracteres. Você deve garantir que sua propriedade AutoCompSource seja limitada a essa quantidade. A propriedade Name do controle é usada se você não especificar um valor AutoCompSource. Se a origem usada for maior que 20 caracteres, ela é truncada para seus primeiros 20 caracteres para consulta contra o campo Source na tabela Autocomp.

# Exemplo

Por exemplo, você pode ter muitos formulários que têm um campo Address. Definindo a propriedade AutoCompSource como "myAddress" para cada text box que exibe um campo de endereço, você pode reutilizar as entradas da tabela AutoComp em todo o seu aplicativo.

```foxpro
AddressForm.AddressText1.AutoCompSource = 'myAddress'
```
