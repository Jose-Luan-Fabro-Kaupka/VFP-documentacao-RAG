# Função EDITSOURCE( )

Abre o editor do Visual FoxPro e, opcionalmente, posiciona o cursor.

```foxpro
EditSource(cShortCutID | [ cFilename [, nLineNo] [, cClassName]
[, cMethodName|cProcName]])
```

#### Parâmetros
 **cShortCutID**
Especifica o ID de atalho válido.
**cFileName**
Especifica o nome do arquivo a abrir. Se o arquivo já estiver aberto, o Visual FoxPro o ativa.
**nLineNo**
Especifica a linha na qual posicionar o cursor. Se você usar 0, o cursor é posicionado na última localização salva no arquivo de recursos. Se você fornecer um nlineno inválido ou inexistente, o cursor é posicionado no início do arquivo atual. Um valor nlineno negativo gerará um erro.
**cClassName**
Especifica o nome de uma classe ou data environment a ser editada. Se você abrir um arquivo de classe (.vcx) sem nomear uma classe, o Class Designer abre em vez do editor.
**cMethodName**
Especifica o nome de um método a ser editado. Use um método referenciado por objeto válido no formulário cObject . nMethodName .
**cProcName**
Especifica o nome de um procedure a ser editado em um arquivo de tipo classe (.vcx, .scx, .frx, .lbx).

# Valor de retorno

Lógico. Retorna true (.T.) se o arquivo de destino abrir com sucesso; caso contrário, retorna códigos de erro de acordo com a tabela a seguir:

| Valor | Descrição |
| --- | --- |
| 0 | Abertura de arquivo bem-sucedida. |
| 132, 705 | Arquivo em uso. Não pode ser aberto. |
| 200 | Arquivo não aberto devido a referência de objeto inválida. Verifique a presença de cMethodName no objeto referenciado pelo parâmetro cClassName. |
| 901, 925 | Arquivo aberto, mas referência de objeto inválida em cMethodName. Verifique a referência no parâmetro cMethodName. Use uma referência como MyForm.MyList.CLICK. Forms e classes retornam 925; reports retornam 901. |

# Observações

Você pode passar cShortCutID sem informações adicionais e fazer o editor abrir nesse local. O cShortCutID é o valor de ID exclusivo para um registro de atalho armazenado na tabela de sistema Foxtask (_VFP.FoxTask). O aplicativo Task List usa esta tabela para garantir que possa obter a posição de linha mais recente do atalho. O Visual FoxPro mantém, internamente, informações de atalho atuais, mas grava atualizações de posição de linha no Foxtask apenas quando um arquivo é salvo.

A extensão do arquivo determina qual editor do Visual FoxPro abre, de acordo com a tabela a seguir:

| Extensão | Editor | Configurações padrão |
| --- | --- | --- |
| PRG | Text Editor | MODIFY COMMAND |
| MPR | Text Editor | MODIFY COMMAND |
| QPR | Text Editor | MODIFY COMMAND |
| TXT | Text Editor | MODIFY FILE |
| SCX | Code Editor | MODIFY FORM |
| VCX | Code Editor | MODIFY CLASS |
| FRX | Code Editor | MODIFY REPORT |
| LBX | Code Editor | MODIFY LABEL |
| MNX | Menu Editor | MODIFY MENU |
| DBC | Stored Procedures | MODIFY PROCEDURE |
| <other> | Text Editor | MODIFY FILE |

Arquivos de programa (.prg), banco de dados (.dbc stored procedures) e arquivos de texto suportam apenas o parâmetro nLineNo.

Arquivos de menu (.mnx) são abertos como arquivos de texto sem referência a objetos ou a números de linha.
