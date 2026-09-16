# Estrutura do arquivo de recursos FoxUser

O arquivo de recursos FoxPro FoxUser.dbf armazena vários tipos de informações de recursos (por exemplo, posições de janelas, conjuntos de cores, configurações da janela Browse, definições de etiquetas etc.). FoxUser.dbf é uma tabela padrão do FoxPro com um arquivo de memo associado (.FPT). Se o arquivo de índice não existir, ele será criado quando FoxUser.dbf for aberto.

Ao contrário das versões anteriores do Visual FoxPro, o arquivo de recursos FoxUser.dbf é aberto como SHARED.

Enquanto RESOURCE estiver SET ON, o FoxPro cuidará de todo o gerenciamento de recursos. Você pode modificar os dados deste arquivo de duas maneiras:
 - Configurações especiais de janelas ou outras preferências, depois de definidas e salvas no arquivo de recursos, podem ser protegidas contra alterações interativas posteriores modificando-se o campo READONLY do recurso específico (consulte o exemplo na seção Predefinindo a configuração da janela Browse).
- Recursos que não sejam mais necessários podem ser excluídos, e o arquivo de recursos pode ser compactado.

Modificar o campo READONLY e/ou excluir registros do arquivo de recursos são as únicas ações que devem ser realizadas em FoxUser.dbf. Faça uma cópia do arquivo antes de modificá-lo.

A tabela FoxUser.dbf tem a seguinte estrutura:

| Campo | Nome do campo | Tipo | Largura |
| --- | --- | --- | --- |
| 1 | TYPE | Character | 12 |
| 2 | ID | Character | 12 |
| 3 | NAME | Memo | 4 |
| 4 | READONLY | Logical | 1 |
| 5 | CKVAL | Numeric | 6 |
| 6 | DATA | Memo | 4 |
| 7 | UPDATED | Date | 8 |
 **TYPE**
Identifica o tipo de informação armazenada pelo recurso.
**ID**
Identifica o registro com TYPE.
**NAME**
Contém o nome atribuído ao recurso, como o nome atribuído a conjuntos de cores, janelas BROWSE e janelas do sistema.
**READONLY**
Campo lógico que pode ser definido como verdadeiro (.T.) para indicar que o recurso deve ser usado somente para leitura e não pode ser alterado.
**CKVAL**
Usado pelo FoxPro para verificar se os dados (no campo de memo DATA) são válidos.
**DATA**
Campo de memo que contém os dados efetivos do recurso.
**UPDATED**
A data da última alteração do recurso atual.

Você pode tornar o arquivo FoxUser.dbf somente leitura marcando-o no nível do MS-DOS. O comando ATTRIB do MS-DOS usa a configuração <+R> para marcar um arquivo como somente leitura. Isso é útil em ambientes multiusuário, pois FoxUser.dbf pode ser compartilhado em uma rede.

# Modificando o arquivo de recursos FoxUser.dbf

Os comandos SET RESOURCE a seguir permitem abrir e modificar facilmente o conteúdo de FoxUser.dbf, além de usar outro arquivo de recursos.

SET RESOURCE TO <resourcefile>

SET RESOURCE TO

SET RESOURCE ON

SET RESOURCE OFF

Para alterar os recursos, use os seguintes comandos na janela Comando:

```foxpro
SET RESOURCE OFF
USE FOXUSER
BROWSE
```

Com o arquivo de recursos aberto, você pode usar CHANGE, EDIT, BROWSE, DELETE, REPLACE e outros comandos do FoxPro para modificar ou excluir dados. Também pode usar COPY TO para criar uma nova tabela de recursos. Ao terminar, compacte o arquivo se tiver marcado registros para exclusão e feche-o. Em seguida, ative o recurso com:

```foxpro
USE
SET RESOURCE ON
```

Você pode abrir FoxUser.dbf em uma área de trabalho sem definir RESOURCE como OFF emitindo USE SYS(2005) AGAIN. SYS(2005) - Current Resource File retorna o nome do arquivo de recursos atual.

# Predefinindo a configuração da janela Browse

Uma modificação útil em FoxUser.dbf é alterar o campo READONLY de configurações predefinidas da janela Browse.

Primeiro, ajuste uma janela BROWSE para exibir campos específicos dimensionados para facilitar a manipulação; posicione e dimensione a janela; divida-a em duas partes, uma no modo BROWSE e outra no modo CHANGE; depois, feche-a. Ao fechar a janela BROWSE, sua configuração será salva no arquivo de recursos atual, desde que READONLY não esteja definido como T e que a janela não tenha sido fechada com Ctrl+Q.

Em seguida, emita USE SYS(2005) AGAIN e edite READONLY, definindo-o como verdadeiro ("T"). Procure o recurso da janela BROWSE cujo TYPE seja PREFW, ID seja WINDBROW e cujo campo NAME contenha o alias da tabela que você acabou de consultar. Quando READONLY for verdadeiro (T), os dados correspondentes do recurso não serão sobrescritos se a configuração da janela Browse for posteriormente alterada de forma interativa.

Agora, sempre que a tabela for consultada com BROWSE LAST, a janela Browse aparecerá na mesma posição e com as mesmas configurações de campos, tamanho e disposição da última sessão. Não importa quanto o usuário altere a janela: ela sempre retornará à configuração dos dados do recurso quando BROWSE LAST for usado.
