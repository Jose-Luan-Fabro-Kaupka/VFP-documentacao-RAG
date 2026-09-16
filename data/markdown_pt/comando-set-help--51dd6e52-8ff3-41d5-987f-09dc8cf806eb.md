# Comando SET HELP

Habilita ou desabilita o arquivo de Ajuda do Microsoft Visual FoxPro ou especifica outro arquivo de Ajuda. Há duas versões da sintaxe.

```foxpro
SET HELP ON | OFF
```

```foxpro
SET HELP [TO [FileName]] [COLLECTION [cCollectionURL]] [SYSTEM]
```

#### Parâmetros
 **ON**
Exibe a janela de Ajuda quando você pressiona F1 ou emite HELP na janela Command. (Padrão)
**OFF**
Torna a Ajuda online do Visual FoxPro indisponível.
**TO [ FileName ]**
Especifica um arquivo de Ajuda que é exibido quando você pressiona F1 ou emite HELP. Você pode especificar um arquivo de Ajuda no estilo .dbf, um arquivo WinHelp (.hlp) ou um arquivo de ajuda HTML (.chm). A partir do Visual FoxPro 7.0, se você emitir SET HELP TO sem incluir um nome de arquivo, o Visual FoxPro procura o arquivo de ajuda padrão.
**COLLECTION [ cCollectionURL ]**
Especifica o nome de uma coleção de Ajuda HTML a ser usada como fonte de Ajuda.
**SYSTEM**
Especifica que um nome de coleção é usado como fonte de Ajuda.

# Observações

Você pode usar SET HELP para fornecer um arquivo de Ajuda online personalizado em uma aplicação personalizada ou para alternar entre os diferentes arquivos de Ajuda no Visual FoxPro.

O arquivo de Ajuda do Visual FoxPro, dv_FoxHelp.chm, é instalado por padrão com o produto Visual FoxPro. Se você realizar uma instalação completa da biblioteca Microsoft Developer's Network (MSDN) ou se realizar uma instalação personalizada da biblioteca MSDN e especificar a instalação da documentação do Visual FoxPro, o arquivo de Ajuda do Visual FoxPro é instalado.

A tabela a seguir descreve os valores de registro para configurações de Ajuda:

| Configuração | Chave de registro | Valor de registro |
| --- | --- | --- |
| SET HELP ON | OFF | HelpOn | 0 ou 1 |
| SET HELP TO cfilename | HelpTo | cFileName |
| SET HELP COLLECTION cCollectionURL | HelpCollection | cCollectionURL |
| SET HELP SYSTEM | HelpSystem | 0 ou 1 |

Você também pode usar a opção Arquivo de ajuda na guia Localizações de arquivo, Caixa de diálogo Opções da Caixa de diálogo Opções (Visual FoxPro) para especificar interativamente um arquivo de Ajuda.
