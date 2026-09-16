# Provedor OLE DB para Visual FoxPro

O Provedor OLE DB do Visual FoxPro (VfpOleDB.dll) expõe interfaces OLE DB que você pode usar para acessar bancos de dados e tabelas do Visual FoxPro a partir de outras linguagens de programação e aplicativos.

O Provedor OLE DB do Visual FoxPro inclui o seguinte:
 - Suporte à maior parte da funcionalidade do driver Open Database Connectivity (ODBC) de versões anteriores do FoxPro
- Modelo de threading aprimorado para escalabilidade Observação O Provedor OLE DB do Visual FoxPro não oferece suporte a vários conjuntos de resultados.
- Funcionalidade aprimorada e acesso a procedimentos armazenados Procedimentos armazenados retornam resultados escalares em conjuntos de linhas e podem aceitar parâmetros. O Provedor OLE DB do Visual FoxPro implementa a interface ICommandPersist para que você possa criar, modificar e excluir código e módulos de procedimentos armazenados.
- Suporte a eventos DBC e capacidade de criar, modificar e excluir funções e procedimentos no módulo de procedimentos armazenados do DBC
- Suporte aos seguintes Schema Rowsets: Table, Column, Provider Types, Indexes, Primary Keys, Procedures, Foreign Keys, Views, Table Constraints, Check Constraints, and Referential Constraints
- Reconhecimento de qualquer arquivo de configuração válido do Visual FoxPro (.fpw) armazenado no mesmo diretório do Provedor. No entanto, apenas as seguintes configurações no arquivo de configuração são reconhecidas pelo Provedor. MVCOUNT que define o número máximo de variáveis que o Visual FoxPro pode manter. ENGINEBEHAVIOR que especifica o nível de compatibilidade do Engine. TABLEVALIDATE que especifica o nível de validação de tabela a executar. REFRESH que especifica com que frequência os buffers de memória local são atualizados com alterações de outros usuários na rede.

Você pode executar as seguintes funções através do Provedor OLE DB do Visual FoxPro:
 - Acessar dados do Visual FoxPro a partir de aplicativos externos.
- Criar clientes thin e fat de n camadas que acessam dados legados do Visual FoxPro.
- Usar um subconjunto da linguagem Visual FoxPro em procedimentos armazenados de banco de dados.
- Criar e manter contêineres de banco de dados (DBCs) através de funcionalidade DML (Data Manipulation Language) ampliada e aprimoramentos ADOX ao ADO.

O Provedor OLE DB do Visual FoxPro é suportado pelos OLE DB System Components fornecidos pelo MDAC 2.6 ou posterior. Os requisitos para executar o Provedor OLE DB do Visual FoxPro são os mesmos desta versão do Visual FoxPro.

> **Observação:** Quando você usa o Provedor OLE DB do Visual FoxPro como um servidor vinculado do SQL Server, apenas consultas são suportadas. O Provedor OLE DB do Visual FoxPro não oferece suporte a operações de update, insert ou delete através de um servidor vinculado.

# Correlação Entre Métodos OLE DB do Visual FoxPro e Funções do Driver ODBC

OLE DB e ODBC são interfaces diferentes. Não existe correspondência um para um entre as propriedades de uma interface e os atributos da outra. OLE DB contém uma definição rica de conjuntos de propriedades e parâmetros de métodos de interface que fornecem serviços significativamente diferentes dos fornecidos pelo ODBC.

Para obter mais informações, consulte a documentação OLE DB de schema rowsets, conjuntos de propriedades e métodos. Para uma discussão sobre OLE DB em relação ao ODBC, consulte o artigo da MSDN "OLE DB for the ODBC Programmer."

# Procedimentos Armazenados no Provedor OLE DB

O Provedor OLE DB do Visual FoxPro aceita comandos de procedimentos armazenados nos seguintes formatos:
 - Chamando um procedimento armazenado usando a sintaxe convencional: myStoredProc( Param1, Param2, ... )
- Chamando um procedimento armazenado usando a palavra-chave SQL EXEC com a seguinte sintaxe: EXEC myStoredProc( Param1, Param2, ... ) onde cada parâmetro está no formato esperado para seu tipo de dados ou é uma expressão válida que retorna esse formato, como no exemplo a seguir: EXEC myStoredProc( 'characterparm', {^2002/09/09}, dateTime(), 100, 99.99, .T.) Observação Certifique-se de substituir myStoredProc pelo nome do procedimento armazenado desejado. Dica Quando você usa ADO ou ADO.NET e define o Command Type como Stored Procedure, não precisa incluir a palavra-chave EXEC. Se o Command Type não estiver definido como Stored Procedure, você deve usar a sintaxe convencional para procedimentos armazenados ou usar a palavra-chave EXEC.

# Entradas de Registro

Quando você instala o Provedor OLE DB do Visual FoxPro, o programa de instalação atualiza o registro do sistema, HKEY CLASSES_ROOT, e adiciona as seguintes novas chaves:

HKEY_CLASSES_ROOT\VFPOLEDB

HKEY_CLASSES_ROOT\VFPOLEDB.1

HKEY_CLASSES_ROOT\Vfpoledb.ConnectionPage

HKEY_CLASSES_ROOT\Vfpoledb.ConnectionPage.1

HKEY_CLASSES_ROOT\VFPOLEDB.ErrorLookup

HKEY_CLASSES_ROOT\VFPOLEDB.ErrorLookup.1

# Suporte Internacional

O Provedor OLE DB do Visual FoxPro fornece suporte a idiomas internacionais para o seguinte:
 - Conjuntos de caracteres de byte duplo (DBCS)
- Várias sequências de ordenação Uma sequência de ordenação define a ordem de classificação para dados armazenados em uma tabela ou banco de dados do Visual FoxPro. O Provedor OLE DB do Visual FoxPro é configurado para usar sequências de ordenação que suportam a versão de idioma do seu sistema operacional por padrão.
