# Comando SET VARCHARMAPPING

Especifica como expressões de dados de caractere são mapeadas para conjuntos de resultados de consulta.

```foxpro
SET VARCHARMAPPING ON | OFF
```

#### Parâmetros
 **ON**
Expressões de dados de caractere são mapeadas para Varchar Field Type em conjuntos de resultados de consulta.
**OFF**
(Padrão) Expressões de dados de caractere são mapeadas para campos de tipo caractere em conjuntos de resultados de consulta.

# Observações

A configuração VARCHARMAPPING determina como expressões de dados de caractere são mapeadas em conjuntos de resultados de consulta criados com o SELECT - SQL Command e os Query and View Designers.

Em cenários em que você deseja que um resultado de consulta use campos de caractere de comprimento fixo, defina SET VARCHARMAPPING como OFF para que campos de caractere não sejam mapeados para campos de tipo varchar de comprimento variável.

No exemplo a seguir, a ausência de expressões de dados de caractere implica que os dados de caractere devem ser preservados em seu formato original, incluindo preenchimento para manter o comprimento fixo dos campos de caractere. Neste caso, você deve definir SET VARCHARMAPPING como OFF. Defina SET VARCHARMAPPING como OFF para imitar o comportamento no Visual FoxPro 8.0 e versões anteriores.

```foxpro
SELECT * FROM customers
***   -or-
SELECT companyname, contactname FROM customers
```

No próximo exemplo, a presença de expressões de dados de caractere significa que o conjunto de resultados da consulta conterá dados de caractere de comprimento variável. Aqui você pode querer que o conjunto de resultados use campos de tipo Varchar de comprimento variável para evitar que os resultados sejam preenchidos com caracteres extras. Neste caso, você deve definir SET VARCHARMAPPING como ON.

```foxpro
SELECT ALLTRIM(companyname), ALLTRIM(contactname) FROM customers
```

A configuração VARCHARMAPPING também controla o mapeamento de expressões de campo usando PADL( ) | PADR( ) | PADC( ) Functions em que o segundo parâmetro não é constante.

```foxpro
SELECT LEN(PADR(field1,field2)) FROM customers INTO CURSOR tmpcusts
```

A configuração VARCHARMAPPING tem escopo na sessão de dados atual. Este comando é suportado tanto em tempo de design quanto em tempo de execução, e também pode ser definido em Config.fpw, o arquivo de configuração do Visual FoxPro. Consulte Special Terms for Configuration Files para obter informações sobre como definir VARCHARMAPPING em Config.fpw.

Se você estiver usando campos calculados, como aqueles criados usando o SET FIELDS Command, a configuração VARCHARMAPPING afetará como esse campo é tratado. Se o campo calculado resultar em uma expressão de caractere de comprimento variável, como no exemplo a seguir, o campo será tratado como um tipo Varchar se SET VARCHARMAPPING estiver ON. Isso pode impactar o uso subsequente desse campo, como com o COPY TO Command.

```foxpro
SET VARCHARMAPPING ON
SET SAFETY OFF
CLOSE DATABASES ALL
USE HOME(2) + 'Northwind\Customers'
SET FIELDS GLOBAL
SET FIELDS TO cField = ALLTRIM(CompanyName)
COPY TO crsTemp
SET FIELDS LOCAL
SET FIELDS OFF
SET FIELDS TO
SELECT 0
USE crsTemp
LIST STRUCTURE
```
