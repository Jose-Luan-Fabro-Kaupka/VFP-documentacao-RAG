# Propriedade SizeBox

Incluída para compatibilidade retroativa com o Macintosh. Especifica se um formulário tem uma size box. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.SizeBox = lExpr
```

# Valores da propriedade
 **lExpr**
As configurações para a propriedade SizeBox são as seguintes: Setting Description True (.T.) Uma size box aparece no canto inferior direito do formulário se a propriedade BorderStyle do formulário estiver definida como 3 (o padrão). False (.F.) (Padrão) Nenhuma size box aparece no formulário.

# Observações

Aplica-se a: Form Object

A SizeBox fornece uma maneira para os usuários redimensionarem um formulário usando o mouse. A size box pode aparecer em um formulário somente se a propriedade BorderStyle do formulário estiver definida como 3 (Sizable Border), que é o padrão para novos formulários.
