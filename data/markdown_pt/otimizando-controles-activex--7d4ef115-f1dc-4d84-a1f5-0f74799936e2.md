# Otimizando controles ActiveX

Se você usa automação ou controles ActiveX no seu aplicativo, pode ajustar o aplicativo para obter o melhor desempenho tanto dos controles ActiveX quanto da automação.

# Usando controles ActiveX com eficiência

Para melhor desempenho ao usar controles ActiveX nos seus formulários, use as seguintes sugestões:
 - Inicie servidores de automação antecipadamente. Controles vinculados a campos gerais geralmente terão melhor desempenho quando os servidores para esses tipos de dados (como Microsoft Excel ou Word) já estiverem em execução na máquina do cliente.
- Insira objetos "As Icon." Quando você insere um controle ActiveX em um campo, insira-o como ícone ou espaço reservado em vez de como um objeto inteiro. Isso reduz a quantidade de espaço de armazenamento necessário porque o Visual FoxPro armazena uma imagem de apresentação com o objeto, o que pode consumir muito espaço de armazenamento. Inserir um objeto como ícone também aumenta o desempenho para desenhar o objeto.
- Use controles image. Se você deseja exibir um bitmap (como um logotipo da empresa), controles image são muito mais rápidos que controles OLEBound.
- Use vínculos manuais sempre que possível. Vínculos manuais a objetos são mais rápidos porque evitam o tempo de notificação necessário para vínculos automáticos e porque o servidor não precisa ser iniciado para desenhar o objeto. Se você não precisa atualizar um objeto com frequência, use vínculos manuais.

# Otimizando o desempenho de automação

Se o seu aplicativo interage com outros aplicativos, você pode obter o melhor desempenho usando as seguintes técnicas.

### Evitando múltiplas instâncias do servidor

Em alguns casos, servidores de automação (como o Microsoft Excel) sempre iniciarão uma nova instância, mesmo se uma já estiver em execução. Para corrigir isso e melhorar o desempenho, use a função GETOBJECT( ) em vez da função CREATEOBJECT( ). Por exemplo, a chamada a seguir sempre usará uma instância existente, se existir:

```foxpro
x = GetObject(,"excel.Application")
```

Em contraste, a chamada a seguir cria uma nova instância:

```foxpro
x = CreateObject("excel.Application")
```

Se você chamar GetObject( ), mas o servidor ainda não estiver em execução, receberá o erro 1426. Nesse caso, você pode tratar o erro e chamar CreateObject( ):

```foxpro
ON ERROR DO oleErr WITH ERROR()
x = GetObject(,"excel.application")
ON ERROR  && restore system error handler
PROCEDURE oleErr
PARAMETER mError
IF mError = 1426 then
 x = CreateObject("excel.application")
ENDIF
```

### Referenciando objetos com eficiência

Executar expressões que usam objetos dentro do servidor de automação pode ser custoso, particularmente quando avaliadas várias vezes. É muito mais rápido armazenar referências de objetos em variáveis para referência.
