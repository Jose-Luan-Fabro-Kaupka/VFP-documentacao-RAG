# Função XMLUPDATEGRAM( )

Espelha alterações feitas em uma tabela ou cursor em buffer em um XML UpdateGram e retorna uma cadeia de caracteres que contém o UpdateGram.

Um XML UpdateGram representa as condições antes e depois da porção alterada de uma tabela ou cursor Visual FoxPro. Por meio de processos adicionais, você pode usar um UpdateGram para confirmar essas alterações nos dados representados pelo documento XML UpdateGram.

> **Observação:** Para usar XMLUPDATEGRAM( ) , você deve usar SET MULTILOCKS ON e habilitar o buffer de tabela.

> **Dica:** Antes de chamar XMLUPDATEGRAM( ) , você deve especificar a lista de campos-chave chamando CURSORSETPROP( ) com a propriedade KeyFieldList em cursores e tabelas existentes. Se você não especificar campos-chave, ambas as representações antes e depois contêm todos os campos da tabela. Se você especificar um ou mais campos-chave, apenas esses campos aparecem na seção before.

```foxpro
XMLUPDATEGRAM( [ cAliasList [, nFlags [, cSchemaLocation]]])
```

#### Parâmetros
 **cAliasList**
Especifica uma lista separada por vírgulas de tabelas ou cursores abertos, listados por nome ou números de área de trabalho em qualquer combinação, para incluir no XML UpdateGram. Se você especificar nenhum valor ou uma cadeia de caracteres vazia ("") para cAliasList , o Visual FoxPro usa todas as tabelas e cursores abertos na sessão de dados atual que contêm alterações em buffer.
**nFlags**
Especifica se retornar um arquivo formatado. A tabela a seguir lista os flags aditivos para nFlags . nFlag Bit Descrição da saída 0 0000 (Padrão) Usar XML formatado em UTF-8. 1 0001 Usar XML não formatado, por exemplo, XML de cadeia de caracteres contínua. 2 0010 Encerrar elementos vazios com elementos de abertura e fechamento, por exemplo, <cc04><cc04/>. 4 0100 Preservar espaço em branco em campos. 8 1000 Envolver campos Memo em seções CDATA. 16 10000 Codificação de saída. 32 100000 Codificação de saída. 32768 none Indica que uma página de código deve ser usada. Observação Quando a codificação de saída é UTF-8 (padrão), a Declaração XML não contém um atributo Encoding= (nenhum atributo de codificação = UTF-8). Quando a codificação de saída é definida como padrão para a página de código do cursor ou tabela, o atributo de codificação será gravado de acordo com a tabela a seguir. Observação Os flags de codificação são definidos combinando os bits 4 e 5 (0010000). Flag de codificação Bits 4 e 5 Descrição +0 00 (Padrão) Windows 1252 +16 01 Definir atributo de codificação de saída para a página de código do cursor. +32 10 Definir atributo de codificação de saída para UTF-8 (sem tradução de caracteres). +48 11 Definir atributo de codificação de saída para UTF-8 e traduzir caracteres de byte duplo para UTF-8.
**cSchemaLocation**
Especifica o nome e a localização do esquema de mapeamento, se existir. Observação Você deve fornecer o esquema de mapeamento. Por exemplo, suponha que você passe um esquema chamado mySchema.xsd para cSchemaLocation , o UpdateGram criado contém um atributo de esquema de mapeamento conforme aparece no XML a seguir: <ROOT xmlns:updg="urn:schemas-microsoft-com:xml-updategram"> <updg:sync mapping-schema="mySchema.xsd" > <updg:before>

# Valor de retorno

Tipo de dados Character. XMLUPDATEGRAM( ) retorna uma cadeia de caracteres que contém o XML UpdateGram.

# Observações

Você pode usar XMLUPDATEGRAM( ) com o Provedor OLE DB para Visual FoxPro. No entanto, a propriedade VFPXMLProgID _VFP não é suportada porque a variável de sistema _VFP não é suportada no Provedor OLE DB antigo.

> **Observação:** Para usar o Provedor OLE DB do Visual FoxPro com XMLUPDATEGRAM( ) , você deve instalar o MSXML 3.0 no computador com o Provedor OLE DB.

SQL Server e Visual Studio suportam o formato DiffGram para atualizar XML. No entanto, o SQL XML requer um esquema de mapeamento para suportar este formato. Portanto, XMLUPDATEGRAM( ) não suporta este formato.

Para evitar possíveis erros gerados por XMLUPDATEGRAM( ) em tabelas contendo campos Memo ou General, use a função CURSORSETPROP( ). O exemplo a seguir mostra como incluir dados memo em um XML UpdateGram definindo a propriedade KeyFieldList usando CURSORSETPROP( ):

```foxpro
SET MULTILOCKS ON
CREATE CURSOR Test (mField M, cField I AUTOINC)
INSERT INTO Test (mField) VALUES ("123456789")
INSERT INTO Test (mField) VALUES ("23456789")
INSERT INTO Test (mField) VALUES ("3456789")
INSERT INTO Test (mField) VALUES ("456789")
CURSORSETPROP("Buffering",5)
CURSORSETPROP("keyfieldlist",'cField')
UPDATE Test SET mField = "XXXXXXX" WHERE cField < 3
STRTOFILE(XMLUPDATEGRAM(),'xmlupdate.txt')
MODIFY FILE xmlupdate.txt
RETURN
```

Para gravar dados memo no XML UpdateGram no SQL Server, você deve usar um esquema explícito no SQL Server e referenciar o esquema no XML UpdateGram.

Diferentemente da função CURSORTOXML( ), XMLUPDATEGRAM( ) ignora instruções SET FIELDS e lê diretamente do cursor subjacente. Para alterar a estrutura da tabela antes de chamar XMLUPDATEGRAM( ), você deve copiar os dados em um novo cursor. Por exemplo, para alterar um campo Numeric para um campo Currency, o exemplo a seguir usa uma instrução SQL SELECT para criar um novo cursor e usa esse cursor com XMLUPDATEGRAM( ). O exemplo torna o campo Total_Price um campo currency, habilita o buffer com CURSORSETPROP( ), adiciona imposto sobre vendas com o comando REPLACE e cria um XML UpdateGram usando a função XMLUPDATEGRAM( ).

```foxpro
SELECT OrderID, CustID, NTOM(Total_Price) as Total_Price;
      FROM Orders INTO CURSOR New_Orders READWRITE
   CURSORSETPROP("Buffering", 5, "New_Orders")
   REPLACE Total_Price WITH (Total_Price * 1.083)
   cXMLUpdg = XMLUPDATEGRAM("New_Orders")
```

Ao usar o flag 32768, as configurações 16 e 32 do flag podem afetar qual página de código é aplicada dependendo do tipo de dados que você está gravando em XML. As tabelas a seguir mostram as combinações possíveis de configurações e a página de código que cada combinação aplica.

Para documentos XML gravados com o flag 32768 definido, as seguintes páginas de código são aplicadas.

| Flag 16 | Flag 32 | Flag 32768 está Definido |
| --- | --- | --- |
| Não definido | Não definido | Documentos XML: Window-1252. Dados Unicode: página de código 1252. Dados de caracteres: página de código padrão, a menos que um campo esteja marcado como NOCPTRANS . |
| True (.T) | Não definido | Documentos XML: Plus- Propriedade CodePage do cursor. Se a propriedade CodePage do XMLField for maior que zero (0) e não corresponder à página de código do cursor, um erro é relatado. Dados Unicode: a propriedade Code page do objeto cursor. Dados de caracteres: nenhum. Dados brutos das tabelas Visual FoxPro (.dbf) são usados em vez disso. |
| Não definido | Definido | Documentos XML: página de código UTF-8. Dados Unicode: página de código UTF-8. Dados de caracteres: Página de código padrão, a menos que o campo esteja marcado como NOCPTRANS , caso em que nenhuma tradução adicional de caracteres para UTF-8 ocorre. |
| Definido | Definido | Documentos XML: página de código UTF-8. Dados Unicode: página de código UTF-8. Dados de caracteres: página de código padrão, a menos que um campo esteja marcado como NOCPTRANS , caso em que os dados são traduzidos para UTF-8 usando a configuração SYS(3005). |

Para documentos XML gravados sem definir o flag 32768, as seguintes páginas de código são aplicadas.

| Flag 16 | Flag 32 | Sem o flag 32768 |
| --- | --- | --- |
| Não definido | Não definido | Documentos XML: Window-1252. Dados Unicode: página de código 1252. Dados de caracteres: página de código padrão, a menos que um campo esteja marcado como NOCPTRANS . |
| True (.T) | Não definido | Documentos XML: Propriedade CodePage do cursor. Dados de caracteres: nenhum. Dados brutos das tabelas Visual FoxPro (.dbf) são usados em vez disso. Dados Unicode: propriedade code page do objeto cursor. |
| Não definido | Definido | Documentos XML: página de código UTF-8. Dados Unicode: página de código UTF-8. Dados de caracteres: página de código padrão, a menos que o campo esteja marcado como NOCPTRANS , caso em que nenhuma tradução adicional de caracteres para UTF-8 ocorre. |
| Definido | Definido | Documentos XML: página de código UTF-8. Dados Unicode: página de código UTF-8. Dados de caracteres: página de código padrão, a menos que um campo esteja marcado como NOCPTRANS , caso em que são traduzidos para UTF-8 usando a página de código da configuração SYS(3005) atual. |

Para obter mais informações sobre a conversão de XML para dados Visual FoxPro, consulte Conversão entre XML e Dados Visual FoxPro.
