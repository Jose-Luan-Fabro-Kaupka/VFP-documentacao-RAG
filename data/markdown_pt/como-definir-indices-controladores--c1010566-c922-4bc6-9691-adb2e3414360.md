# Como: definir índices controladores

Uma tabela pode ter muitos arquivos de índice abertos simultaneamente; no entanto, somente um arquivo ou tag de índice mestre, ou controlador, especifica a ordem em que o Visual FoxPro exibe ou acessa a tabela. Além disso, certos comandos, como o comando SEEK, usam o arquivo ou tag de índice controlador para pesquisar registros.

> **Observação:** Você não pode selecionar índices binários como índices controladores. O Visual FoxPro não suporta o comando SET ORDER ao definir para uma tag de índice binário. Se você tentar definir a ordem para uma tag binária, o Visual FoxPro gera um erro e a ordem atual permanece em sua configuração anterior. Os registros na tabela são exibidos e acessados na ordem do número do registro e não em uma ordem indexada. Portanto, o Visual FoxPro não suporta operações SEEK para índices binários.

Depois de criar um ou mais índices para uma tabela, você precisa atribuir um índice controlador para organizar registros em sua tabela. Você pode designar uma tag de índice em um arquivo de índice composto (.cdx) ou um arquivo de índice independente (.idx) como tag ou arquivo de índice controlador. Quando alterações são feitas na tabela, todos os arquivos .idx e .cdx abertos são atualizados.

Você pode selecionar um índice controlador usando a IDE do Visual FoxPro ou a linguagem.

### Para designar um índice controlador
- Abra a janela de navegação para sua tabela.
- No menu Table, escolha Properties.
- Na caixa Index order da caixa de diálogo Work Area Properties, selecione o índice que deseja usar.
- Escolha OK.

A janela de navegação exibe registros na ordem que o índice especifica.

### Para definir índices controladores programaticamente
- Escolha uma das opções a seguir: Para definir o índice controlador de uma tabela, use o comando SET ORDER. Dica Ao abrir uma tabela usando o comando USE, incluir a cláusula ORDER realiza a mesma função que SET ORDER. Você não precisa usar SET ORDER para executar consultas. Para definir o índice controlador da tabela atualmente aberta, use o comando SET INDEX. Dica Ao abrir uma tabela usando o comando USE, incluir a cláusula INDEX realiza a mesma função que SET INDEX.

Por exemplo, suponha que um índice com o nome de tag Country seja criado para a tabela Customer no banco de dados de amostra do Visual FoxPro, TestData. O código a seguir usa o comando SET ORDER para especificar Country como índice controlador para exibir os registros na tabela. O comando BROWSE abre uma janela de navegação e exibe os registros por nome de país:

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
SET ORDER TO Country
BROWSE
```

Para obter mais informações, consulte Comando SET ORDER, Comando SET INDEX, Comando USE e Comando BROWSE.
