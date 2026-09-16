# Comando SET NULL

Determina como os valores nulos são aceitos pelos comandos ALTER TABLE, CREATE TABLE e INSERT - SQL.

```foxpro
SET NULL ON | OFF
```

#### Parâmetros
**ON**
Especifica que todas as colunas de uma tabela criada com ALTER TABLE e CREATE TABLE permitirão valores nulos. Você pode substituir essa configuração para determinadas colunas incluindo a cláusula NOT NULL em suas definições. Também especifica que INSERT - SQL tentará inserir valores nulos nas colunas não incluídas na cláusula VALUE de INSERT - SQL. A inserção só será bem-sucedida em colunas que permitam nulos. Observação: se você adicionar suporte a nulos a uma ou mais colunas, o limite de colunas da tabela será reduzido de 255 para 254.
**OFF**
(Padrão) Especifica que todas as colunas de uma tabela criada com ALTER TABLE e CREATE TABLE não permitirão valores nulos. Você pode habilitar esse suporte para determinadas colunas incluindo a cláusula NULL em suas definições. Também especifica que INSERT - SQL inserirá valores em branco nas colunas não incluídas na cláusula VALUE de INSERT - SQL.

# Observações

SET NULL afeta apenas o suporte a valores nulos por ALTER TABLE, CREATE TABLE e INSERT - SQL. Outros comandos não são afetados. SET NULL tem escopo limitado à sessão de dados atual.

# Exemplo

O exemplo demonstra como SET NULL afeta o suporte a valores nulos. A primeira tabela, `employee`, é criada com SET NULL ON, portanto seus campos aceitam nulos. REPLACE coloca um valor nulo no campo `cLastName`. A segunda tabela, `staff`, é criada com SET NULL OFF, portanto seus campos não aceitam nulos. REPLACE coloca zero no campo `cLastName`.

```foxpro
CLOSE DATABASES
SET NULL ON        && Fields will support null values
CREATE TABLE employee (cLastName C(20), ySalary Y(12,2))
APPEND BLANK       && Add a new blank record
REPLACE cLastName WITH .NULL.  && cLastName supports null values
SET NULL OFF       && Fields will not support null values
CREATE TABLE staff (cLastName C(20), ySalary Y(12,2))
APPEND BLANK       && Add a new blank record
REPLACE cLastName WITH 0   && Doesn't support null values
```
