# Exemplo Customize the Open Dialog Box

Arquivo: ...\Samples\Solution\OLE\Commdlog.scx

Este exemplo demonstra como você pode personalizar a aparência e o comportamento da caixa de diálogo Open exposta pelo controle Common Dialog.

Para especificar o comportamento da caixa de diálogo Open, você pode definir a propriedade Flags do controle Common Dialog como a soma de valores de sinalizador específicos. A tabela a seguir lista os possíveis valores individuais que você pode usar.

| Valor | Descrição |
| --- | --- |
| 1 | Faz com que a caixa de seleção somente leitura seja inicialmente marcada quando a caixa de diálogo é criada. Este sinalizador também indica o estado da caixa de seleção somente leitura quando a caixa de diálogo é fechada. |
| 2 | Faz com que a caixa de diálogo Save As gere uma caixa de mensagem se o arquivo selecionado já existir. O usuário deve confirmar se deseja substituir o arquivo. |
| 4 | Oculta a caixa de seleção somente leitura. |
| 8 | Força a caixa de diálogo a definir o diretório atual para o que era quando a caixa de diálogo foi aberta. |
| 16 | Faz com que a caixa de diálogo exiba o botão Help. |
| 256 | Especifica que a caixa de diálogo comum permite caracteres inválidos no nome de arquivo retornado. |
| 512 | Especifica que a caixa de listagem File Name permite seleções múltiplas. O usuário pode selecionar mais de um arquivo em tempo de execução pressionando a tecla SHIFT e usando as teclas UP ARROW e DOWN ARROW para selecionar os arquivos desejados. Quando isso é feito, a propriedade File Name retorna uma cadeia de caracteres contendo os nomes de todos os arquivos selecionados. Os nomes na cadeia de caracteres são delimitados por espaços. |
| 1024 | Indica que a extensão do nome de arquivo retornado é diferente da extensão especificada pela propriedade DefaultExt. Este sinalizador não é definido se a propriedade DefaultExt for Null, se as extensões coincidirem ou se o arquivo não tiver extensão. Este valor de sinalizador pode ser verificado ao fechar a caixa de diálogo. |
| 2048 | Especifica que o usuário pode inserir somente caminhos válidos. Se este sinalizador estiver definido e o usuário inserir um caminho inválido, uma mensagem de aviso é exibida. |
| 4096 | Especifica que o usuário pode inserir somente nomes de arquivos existentes na caixa de texto File Name. Se este sinalizador estiver definido e o usuário inserir um nome de arquivo inválido, um aviso é exibido. Este sinalizador define automaticamente o sinalizador 2048. |
| 8192 | Especifica que a caixa de diálogo solicita ao usuário que crie um arquivo que não existe atualmente. Este sinalizador define automaticamente os sinalizadores 4096 e 2048. |
| 16384 | Especifica que erros de violação de compartilhamento serão ignorados. |
| 32768 | Especifica o uso do modelo de caixa de diálogo Windows Explorer Open A File. |
| 524288 | Use o modelo de caixa de diálogo Explorer Open A File. |
| 1048576 | Não desreferencie links do shell (também conhecidos como atalhos). Por padrão, escolher um link do shell faz com que ele seja desreferenciado pelo shell. |
| 1048576 | Não desreferencie atalhos (links do shell). Por padrão, escolher um atalho faz com que ele seja desreferenciado pelo shell. |
| 2097152 | Permite que o usuário use nomes de arquivo longos. |

O código a seguir no evento Click de cmdFiles verifica os valores das várias caixas de seleção no formulário e define a propriedade Flags do controle Common Dialog.

# Definir o sinalizador da caixa de seleção Somente leitura

```foxpro
IF !thisform.chkRead.Value
   m.nFlags = m.nFlags + 4
ENDIF
```

# Definir o sinalizador de vários arquivos

```foxpro
IF thisform.chkMulti.Value
   m.nFlags = m.nFlags + 512
ENDIF
```

# Definir o sinalizador do botão Help

```foxpro
IF thisform.chkHelp.Value
   m.nFlags = m.nFlags + 16
ENDIF
```

# Definir o sinalizador de exigir existência de arquivo

```foxpro
IF thisform.chkMulti.Value
   m.nFlags = m.nFlags + 4096
ENDIF
```

# Definir a propriedade Flags do controle Common Dialog

```foxpro
THISFORM.oleCommDlog.Flags = m.nFlags
```

# Definir a propriedade Filter do controle Common Dialog

Você pode usar a propriedade Filter do controle Common Dialog para especificar quais arquivos um usuário pode escolher.

```foxpro
THISFORM.oleCommDlog.Filter = "All files" + ;
   "(*.*)|*.*|Text (*.txt)|*.txt" + ;
   "|Pictures(*.bmp;*.ico)|*.bmp;*.ico"
```
