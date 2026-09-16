# Comando SET PROCEDURE

Abre um arquivo de procedimento.

```foxpro
SET PROCEDURE TO [FileName1 [, FileName2, ...]] [ADDITIVE]
```

#### Parâmetros
 **FileName1 [, FileName2 , ...]**
Especifica a sequência na qual os arquivos serão abertos. SET PROCEDURE pode receber mais de um nome de arquivo, permitindo abrir vários arquivos de procedimento ao mesmo tempo. Esta opção permite criar bibliotecas autônomas de funções e especificá-las separadamente.
**ADDITIVE**
Abre arquivos de procedimento adicionais sem fechar os arquivos de procedimento atualmente abertos.

# Observações

Emitir SET PROCEDURE TO sem nenhum nome de arquivo fecha todos os arquivos de procedimento abertos. Use RELEASE PROCEDURE para fechar arquivos individuais.

Quando você executa um procedimento, os arquivos de procedimento são pesquisados se o procedimento não for localizado no programa atualmente em execução.

Para mais informações sobre arquivos de procedimento, consulte PROCEDURE Command e DO Command.

Se uma biblioteca de vínculo dinâmico (DLL) COM que usa SET PROCEDURE TO for instanciada mais de uma vez, o método Init da segunda instância pode falhar com uma das seguintes mensagens:

OLE error code 0x80004005: Unspecified error.

OLE error code 0x80020009: Exception occurred.

Para instanciar uma classe OLEPUBLIC, o Visual FoxPro deve ser capaz de encontrar todo o código da classe. Há um SET PROCEDURE/SET CLASSLIB interno para detectar todo o código relacionado; se você tentar alterar esta configuração, ocorre um erro. Para evitar isso, use SET PROCEDURE TO com a palavra-chave ADDITIVE.
