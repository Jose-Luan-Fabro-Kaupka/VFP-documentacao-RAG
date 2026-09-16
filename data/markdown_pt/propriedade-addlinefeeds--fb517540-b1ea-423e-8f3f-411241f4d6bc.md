# Propriedade AddLineFeeds

Especifica que o EditBox deve inserir caracteres de avanço de linha (CHR(10)) após caracteres de retorno de carro (CHR(13)) dentro do texto de um EditBox sempre que a propriedade Value for lida ou sempre que o valor for armazenado no ControlSource. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.AddLineFeeds[ = lExpr]
```

#### Parâmetros
 **lExpr**
True (.T.) (Padrão) Caracteres de avanço de linha são inseridos no texto do EditBox após caracteres de retorno de carro quando a propriedade Value é lida ou armazenada no ControlSource. False (.F.) O texto do EditBox não é modificado quando a propriedade Value é lida ou armazenada no ControlSource.

# Observações

Aplica-se a: Controle EditBox

O EditBox, por padrão, garante que as terminações de linha tenham caracteres de retorno de carro e avanço de linha inserindo caracteres de avanço de linha se eles não estiverem presentes quando a propriedade Value for lida. Além de quando o código do usuário lê a propriedade Value, isso também pode ocorrer sempre que o EditBox perde o foco, já que o Visual FoxPro automaticamente lê o conteúdo Value e armazena no ControlSource nesse momento.

Inserir caracteres de avanço de linha desloca o texto, mas o valor SelStart não muda; portanto, a propriedade SelStart pode apontar para o local errado no buffer de texto. Defina a propriedade AddLineFeeds como False (.F.) para garantir que nenhum caractere seja inserido no buffer de texto. A propriedade AddLineFeeds é forçada como True (.T.) quando o controle Editbox está vinculado.

Ler a propriedade Text nunca causa a inserção de caracteres de avanço de linha, independentemente da configuração de AddLineFeeds.
