# Função XMLTOCURSOR( )

Converte texto XML em um cursor ou tabela do Visual FoxPro.

```foxpro
XMLTOCURSOR(eExpression | cXMLFile [, cCursorName [, nFlags ]])
```

#### Parâmetros
 **eExpression**
Especifica o texto XML ou uma expressão que avalia para dados XML válidos. O parâmetro eExpression pode ser uma variável de memória do Visual FoxPro, conteúdo de campo memo, o retorno de uma solicitação HTTP, o resultado de retorno de uma chamada de método SOAP, XML do XMLDOM ou um fluxo ADO. Observação XMLTOCURSOR( ) gera um erro se eExpression não for encontrado ou se eExpression não for analisado como XML válido.
**cXMLFile**
Especifica o nome e, opcionalmente, o caminho de um arquivo XML físico que reside no computador local ou na rede. Se você não especificar um caminho, o Visual FoxPro pesquisa o caminho ao longo do diretório do Visual FoxPro pelo arquivo XML.
**cCursorName**
Especifica o nome do cursor para armazenar o resultado e cria o cursor na área de trabalho atual. Se o nome do cursor já existir ou estiver aberto, o Visual FoxPro fecha o cursor e cria um novo em uma área de trabalho não utilizada. Se você omitir ou passar uma cadeia vazia ("") para cCursorName, o Visual FoxPro cria um cursor chamado "XMLRESULT" para retornar o resultado. Se cCursorName contiver dados e nFlags estiver definido como 8192, o Visual FoxPro acrescenta os dados sendo importados do arquivo XML à tabela ou cursor existente. A tabela ou cursor deve estar aberta ou em uso. Se cCursorName for uma cadeia vazia (""), o Visual FoxPro importa XML para a tabela ou cursor aberto na área de trabalho atual.
**nFlags**
Especifica como XMLSource eExpression é tratado em XMLTOCURSOR( ) . A tabela a seguir descreve os valores para nFlags . nFlags Bit Descrição 0 0000 (Padrão) Trata o primeiro parâmetro como uma cadeia contendo dados XML. 4 0100 Preserva espaço em branco nos dados e substitui o atributo xml:space dos dados XML. 512 01000000000 Especifica que o primeiro parâmetro, seja um eExpression ou um cXMLFile , é uma cadeia contendo o nome e o caminho de um arquivo de dados XML. 1024 10000000000 NOCPTRANS – Cria campos Character e Memo no cursor resultante com a opção NOCPTRANS e insere os valores de texto ou XML nos elementos recebidos no campo Character ou Memo de forma não traduzida, byte a byte. Quando usado com a flag 1024, XMLTOCURSOR( ) retorna uma cadeia preenchida com espaços à direita iguais à cadeia real, ou seja, uma cadeia com o dobro do comprimento. 2048 100000000000 Use quando o esquema importado tiver uma definição de esquema XML (XSD) contendo tipo de dados decimal com restrições, ou facetas, de totalDigits="19" e fractionDigits="4." Os valores de tipo de dados XSD são mapeados para o tipo de dados Currency do Visual FoxPro no cursor resultante. 4096 1000000000000 Desabilita a decodificação base64. No Visual FoxPro, a codificação base64 destina-se apenas à codificação de dados binários. 8192 1100000000 Especifica que cCursorName é o nome ou alias de uma tabela ou cursor existente e importa os dados do arquivo XML especificado para uma tabela ou cursor predefinido. Se cCursorName contiver dados, os dados importados do arquivo XML são acrescentados aos dados existentes. Se cCursorName for uma cadeia vazia (""), os dados do arquivo XML são importados para a tabela ou cursor na área de trabalho atual. Definir nFlags como 8192 pode ser útil quando um esquema XML não está disponível ou não é prático para uso. 32768 0x8000 Indica que uma página de código deve ser usada. 65536 0x10000 Mapeia campos XML Char para campos Varchar nativos do Fox. Se não especificado, campos XML Char são mapeados para campos Character do Fox. 131072 0x20000 Mapeia campos XML base64Binary para campos Varbinary nativos do Fox se menores que 255 bytes ou campos Blob se maiores que este comprimento. Se não especificado, campos XML base64Binary são mapeados para campos Memo do Fox. Ao usar a flag 8192, esteja ciente do seguinte: Você deve garantir que o esquema da tabela corresponda aos elementos XML recebidos da maneira apropriada. O Visual FoxPro impõe os tipos de dados em cCursorName conforme descrito na tabela Correspondência de tipos de dados neste tópico, mas não faz outras suposições sobre tipos de dados. Tentar importar valores incompatíveis gera a mensagem apropriada. Se o XML contiver ou referenciar um esquema, e os tipos de dados no esquema conflitarem com os tipos de dados do cursor ou tabela, os tipos de dados no cursor ou tabela são usados. Os nomes dos elementos no arquivo XML são mapeados para os nomes das colunas em cCursorName . Além disso, o Visual FoxPro importa apenas dados dos nomes de elementos no arquivo XML que correspondam aos nomes das colunas em cCusorName . O cursor ou tabela pode ter menos colunas do que as do arquivo XML, mas deve ter pelo menos uma coluna correspondente. O cursor ou tabela pode ter colunas adicionais que não correspondam a um elemento no arquivo XML. Se a tabela contiver campos de autoincremento, XMLTOCURSOR( ) falha se AUTOINCERROR estiver definido como ON . Definir AUTOINCERROR como OFF ou desativar autoincremento na tabela de destino usando CURSORSETPROP( ) permite que XMLTOCURSOR( ) tenha sucesso. O campo ou campos de autoincremento da tabela de destino são incrementados conforme os valores especificados, e os valores na tabela de origem não são copiados.

A tabela a seguir descreve as restrições de correspondência de tipos de dados ao definir nFlags como 8192.

| Tipo de dados do Visual FoxPro | Comportamento |
| --- | --- |
| Character , Character (Binary), Memo , Memo (Binary) | Aceita qualquer dado, mas trunca qualquer dado que exceda o comprimento de uma coluna Character. |
| Currency | Aceita dados numéricos dentro do intervalo aceito do tipo Currency, mas trunca números fora deste intervalo. |
| Date | Aceita valores date e dateTime no formato XML. O Visual FoxPro converte os formatos date e dateTime XML para a data correspondente do Visual FoxPro. O Visual FoxPro preserva apenas a parte M/D/Y do valor date ou dateTime XML. |
| DateTime | Aceita valores date e dateTime no formato XML. O Visual FoxPro converte os formatos date e dateTime XML para a data e hora correspondentes do Visual FoxPro e descarta a precisão além do suportado pelo Visual FoxPro. |
| Double | Aceita dados numéricos dentro do intervalo aceito do tipo Double, mas trunca números fora deste intervalo. |
| Integer | Aceita dados inteiros dentro do intervalo aceito do tipo Integer, mas trunca números fora deste intervalo. |
| Logical | Aceita os valores True, .T., 1, False, .F. e 0. |
| Numeric , Float | Aceita dados numéricos com ou sem decimais, mas trunca números fora do intervalo aceito para esses tipos conforme as regras do Visual FoxPro ou substitui pelo indicador de overflow numérico ("*************"). |

# Valor de retorno

Tipo de dados numérico. XMLTOCURSOR( ) retorna o número de registros criados.

# Observações

Você pode usar XMLTOCURSOR( ) com o Provedor OLE DB para Visual FoxPro. No entanto, a propriedade _VFP VFPXMLProgID não é suportada porque a variável de sistema _VFP não é suportada no Provedor OLE DB.

> **Observação:** Para usar o Provedor OLE DB do Visual FoxPro com XMLTOCURSOR( ) , você deve instalar o MSXML 3.0 no computador com o Provedor OLE DB.

XMLTOCURSOR( ) gera um erro de sintaxe para comprimentos de registro maiores que aproximadamente 160 colunas. O número exato de colunas que causam um erro depende do comprimento dos nomes das colunas.

XMLTOCURSOR( ) não usa o tipo Varchar ao criar um cursor de um documento XML. No entanto, XMLTOCURSOR( ) suporta acrescentar dados em um cursor existente com campos Varchar.

Ao chamar XMLTOCURSOR( ) no modo de acrescentar, o Visual FoxPro adiciona uma linha vazia se nenhum nome de elemento XML corresponder a qualquer coluna de tabela ou cursor.

XMLTOCURSOR( ) converte o tipo de dados Decimal para Numeric 20,19 (largura, precisão). Em versões anteriores ao Visual FoxPro 8.0, Decimal era mapeado para Numeric 8,0.

Condições de overflow numérico XMLTOCURSOR( ) importa dados XML contendo condições de overflow numérico do Visual FoxPro, por exemplo, "*******", no lugar de um valor numérico ou inteiro. Se um esquema for fornecido, o Visual FoxPro cria o tipo de dados correto no cursor resultante, mas altera o overflow de caracteres asterisco (*) para valores 0.0 ou 0. Portanto, o analisador XML usado por XMLTOCURSOR( ) não gera um erro como resultado de valores de caracteres armazenados em um elemento de tipo decimal.

Para obter mais informações sobre conversão de XML para dados do Visual FoxPro, consulte Conversão entre XML e dados do Visual FoxPro.
