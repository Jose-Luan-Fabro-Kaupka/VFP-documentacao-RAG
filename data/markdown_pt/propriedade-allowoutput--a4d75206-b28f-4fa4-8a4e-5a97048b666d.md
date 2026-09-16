# Propriedade AllowOutput

Especifica se a saída padrão pode aparecer em um formulário. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Form.AllowOutput = lExpr
```

#### Parâmetros
 **lExpr**
Tipo de dados lógico. A tabela a seguir lista as configurações para lExpr . lExpr Descrição True (.T.) (Padrão) Envia a saída do usuário para o formulário se ele estiver ativo. False (.F.) Redireciona a saída do usuário para a área de trabalho se o formulário estiver ativo.

# Observações

Aplica-se a: Form Object

Se a propriedade AllowOutput for alterada programaticamente de True (.T.) para False (.F.) em tempo de execução, o Visual FoxPro redireciona automaticamente a saída para a área de trabalho.

> **Observação:** Usar a propriedade AllowOutput pode afetar código que depende da posição e do tamanho de uma janela. Isso inclui o uso de WOUTPUT( ) ou outros comandos, como DEFINE POPUP...FROM , que implicitamente baseiam suas coordenadas na janela de saída.

Definir a propriedade AllowOutput como False (.F.) em um formulário altera o seguinte comportamento do Visual FoxPro.
 - A pintura do formulário é redirecionada para a próxima janela de saída ou área de trabalho. Isso afeta comandos, como ? , ?? , DIR , LIST , DISPLAY , CLEAR e outros comandos que exibem saída em um formulário.
- A função WOUTPUT( ) não retorna o nome do formulário ativo. Ela retorna o nome do formulário de saída atual ou da área de trabalho.
- O comando BROWSE não herda o tamanho da janela e as configurações de janela do formulário.
- As funções MCOL( ) e MROW( ), sem o uso de seu parâmetro opcional, podem não ser relativas ao formulário em que são chamadas.

Quando um formulário é fechado com a propriedade AllowOutput definida como False (.F.), o Visual FoxPro usa por padrão o próximo formulário de saída ou a área de trabalho.
