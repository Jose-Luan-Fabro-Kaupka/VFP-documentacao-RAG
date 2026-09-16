# Como: executar o Class Browser

Você pode executar várias instâncias do Class Browser ao mesmo tempo.

### Para executar o Class Browser
- No menu Ferramentas, escolha Class Browser .

Para obter mais informações, consulte Janela Class Browser e Botões do Class Browser.

### Para executar o Class Browser programaticamente
- Na janela Command, use o comando DO com a variável de sistema _BROWSER, que especifica o nome do aplicativo class browser, conforme mostrado na linha de código a seguir: DO (_BROWSER)

Para obter mais informações, consulte Variável de sistema _BROWSER.

Ao executar o Class Browser usando o comando DO, você pode usar os parâmetros e a sintaxe adicionais a seguir:

```foxpro
DO (_BROWSER) [WITH [tcFileName][, tcDefaultClass[.member]][, tlListBox][, tcClassType][, tnWindowState]]
```

A tabela a seguir descreve os parâmetros opcionais que você pode usar ao executar o Class Browser usando o comando DO.

| Parâmetro | Descrição |
| --- | --- |
| tcFileName | O nome do arquivo .vcx, .scx, .olb, .tlb, .pjx ou .exe a abrir no Class Browser. Para obter mais informações, consulte Extensões de arquivo e tipos de arquivo . |
| tcDefaultClass [ .member ] | Especifica a classe a selecionar por padrão no arquivo .vcx. Se nenhuma classe padrão for especificada, a biblioteca de classes é selecionada. Se um membro de classe for especificado, o membro de classe aparece selecionado na lista de membros do Class Browser. |
| tlListBox | Especifica se as classes e os membros são exibidos em list boxes em vez de usar controles tree-view. Para exibir list boxes, especifique True (.T.). Padrão : False (.F.) |
| tcClassType | Especifica o filtro de tipo inicial para as classes exibidas no Class Browser. Para alterar o filtro no Class Browser, escolha outro valor na lista de tipos do Class Browser. Padrão : Sem filtro. |
| tnWindowState | Especifica o estado da janela Class Browser quando aberta. 0 - Normal (Padrão) 1 - Minimizada 2 – Maximizada |
| tlGallery | Especifica se o Component Gallery é aberto em vez do Class Browser. Para abrir o Component Gallery, especifique True (.T.). Padrão: False (.F.) |

Por exemplo, você pode executar o Class Browser com um arquivo de biblioteca de classes visual (.vcx) específico ou uma referência de objeto. Você também pode incluir o nome da classe a ser selecionada inicialmente. A linha de código a seguir abre o Class Browser, a biblioteca de classes Buttons.vcx e seleciona a classe VCR:

```foxpro
DO (_BROWSER) WITH HOME(2) + 'Classes\Buttons.vcx', 'VCR'
```

Como outro exemplo, você pode executar o Class Browser e especificar a seleção do objeto cmdOK da classe Print_Report na biblioteca de classes Samples.vcx, exibir os formulários e membros em Samples.vcx em list boxes, filtrar as classes exibidas usando a classe Form e abrir a janela Class Browser maximizada:

```foxpro
DO (_BROWSER) WITH "Samples.vcx", "Print_Report.cmdOK", .T., "form", 2
```
