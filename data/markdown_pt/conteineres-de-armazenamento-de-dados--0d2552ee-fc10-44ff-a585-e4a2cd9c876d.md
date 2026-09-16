# Contêineres de armazenamento de dados

Você escolhe um contêiner de armazenamento de dados de acordo com a quantidade e o tipo de dados a armazenar e com a forma como deseja usá-los. A disponibilidade dos dados é determinada pela maneira como eles são declarados e pelo local em que são criados no programa. Esse intervalo de disponibilidade ou efetividade é chamado de escopo.

A maioria das linguagens de programação permite armazenar dados em constantes, variáveis e matrizes. No Visual FoxPro, também é possível armazená-los em registros e objetos. Para obter mais informações sobre as diferenças, consulte Visual FoxPro e outras linguagens de programação.

# Escopo dos contêineres de dados

A tabela a seguir resume as diferenças de escopo entre os contêineres de dados.

| Contêiner | Escopo | Exemplo |
| --- | --- | --- |
| Matrizes | Público, privado ou local | ArrayName[1,1] = "John Brown" |
| Constantes | Comando PRIVATE | #DEFINE ERRSTR "Error!" |
| Campos | Armazenamento permanente, acessível enquanto a tabela que contém os registros estiver aberta | REPLACE name WITH "John Brown" |
| Variáveis | Comando PUBLIC, privado ou comando LOCAL | Var = 7 |
| Objetos | Referenciados por meio do objeto e da hierarquia de contêineres do objeto | txtCustomer.Value = "John Brown" |
