# SYS(3056) - Ler configurações do registro

Força o Visual FoxPro a ler novamente suas configurações do registro e atualizar-se com as configurações atuais do registro, ou a gravar suas configurações no registro.

```foxpro
SYS(3056 [, nValue])
```

#### Parâmetros
 **nValue**
A tabela a seguir descreve os valores de nValue . Valor Descrição 1 (Padrão) Inclua a opção 1 para atualizar apenas a partir das configurações do registro, com exceção dos comandos SET e dos locais de arquivos. 2 Inclua a opção 2 para gravar as configurações do Visual FoxPro no registro. Incluir a opção 2 é idêntico a escolher Definir como padrão na caixa de diálogo Opções (Visual FoxPro) .

# Valor de retorno

Caractere

# Observações

Retorna a cadeia de caracteres vazia.

O Visual FoxPro armazena as configurações da caixa de diálogo Opções no registro do Windows. Você também pode armazenar configurações adicionais do Visual FoxPro em um arquivo de texto, normalmente chamado Config.fpw. O Visual FoxPro é configurado na inicialização lendo essas configurações do registro e seu arquivo de configuração (se existir).

As configurações especificadas na caixa de diálogo Opções são gravadas no registro quando você escolhe Definir como padrão. Algumas configurações, como as de Coloração de sintaxe, são armazenadas no registro, mas não possuem comandos SET correspondentes. Outras configurações possuem comandos SET correspondentes (como SET BELL, SET CLOCK e assim por diante) que afetam o ambiente do Visual FoxPro. As configurações feitas na guia Locais de arquivo da caixa de diálogo Opções também são armazenadas no registro, e algumas são acessíveis por variáveis de sistema como _COVERAGE e _SAMPLES.

Emitir SYS(3056) atualiza informações das configurações do registro e dos comandos SET correspondentes, configurações do registro da guia Locais de arquivo da caixa de diálogo Opções e o arquivo de configuração do Visual FoxPro (se existir). SYS(3056) lê as informações do registro primeiro e depois o arquivo de configuração.

Emitir SYS(3056,1) atualiza informações das configurações do registro do Visual FoxPro que não possuem comandos SET correspondentes. Os comandos SET, as configurações do registro da guia Locais de arquivo e as informações do arquivo de configuração não são atualizados se o argumento 1 for incluído.

Emitir SYS(3056,2) grava as configurações da caixa de diálogo Opções no registro do Windows.

Observe que as configurações do registro também podem ser alteradas diretamente pela API do Windows. Consulte a seção API do Windows de Solution.app, localizada no diretório Visual FoxPro ...\Samples\Solution, para um exemplo de como usar a API do Windows para modificar configurações do registro.
