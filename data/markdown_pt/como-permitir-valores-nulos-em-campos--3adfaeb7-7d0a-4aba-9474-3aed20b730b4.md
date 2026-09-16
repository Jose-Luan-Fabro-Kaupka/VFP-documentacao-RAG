# Como: permitir valores nulos em campos

Ao especificar campos para uma tabela, você pode decidir se um ou mais campos podem aceitar valores nulos (.NULL.). Normalmente, um valor nulo indica que as informações normalmente armazenadas no campo ou registro não estão disponíveis no momento.

Por exemplo, os benefícios de saúde ou o status fiscal de um funcionário podem ser desconhecidos no momento em que um registro é preenchido. Em vez de armazenar um zero ou um espaço em branco, que poderia ser interpretado como tendo significado, você pode armazenar um valor nulo no campo até que mais informações estejam disponíveis.

> **Observação:** Valores nulos em campos afetam o comportamento de tabelas e índices. Por exemplo, se você usar APPEND FROM ou INSERT INTO para copiar registros de uma tabela que contém valores nulos para uma tabela que não permite valores nulos, os campos anexados que contêm valores nulos ficam em branco, vazios ou zero na tabela de destino.

### Para permitir valores nulos em um campo
- Abra a tabela no Table Designer.
- Na guia Fields, clique na coluna NULL do campo. Quando valores nulos são permitidos para o campo, a coluna NULL exibe uma marca de seleção para esse campo. Para deixar de permitir valores nulos no campo, clique no botão na coluna NULL para que a marca de seleção seja removida.

Para obter mais informações, consulte a guia Fields, Table Designer.

### Para permitir valores nulos em um campo programaticamente
- Ao criar a tabela usando o comando SQL CREATE TABLE, inclua as cláusulas NULL ou NOT NULL.

-OU-
 - Para editar uma tabela existente, abra a tabela com o comando USE e, em seguida, use o comando SQL ALTER TABLE com as cláusulas NULL ou NOT NULL.

Para obter mais informações, consulte o comando CREATE TABLE - SQL e o comando ALTER TABLE - SQL.

Por exemplo, o código a seguir cria e abre uma tabela que permite valores nulos em um dos campos, mas não nos outros dois campos:

```foxpro
CREATE TABLE Customer (Cust_ID C(6) NOT NULL, ;
   Company C(40) NOT NULL, Contact C(30) NULL)
```

### Para permitir valores nulos em todos os campos da tabela
- Abra a tabela no Table Designer.
- Na guia Fields, clique na coluna NULL de cada campo.

Para obter mais informações, consulte a guia Fields, Table Designer.

### Para permitir valores nulos em todos os campos da tabela programaticamente
- Use SET NULL ON antes de chamar o comando SQL CREATE TABLE.

Usar SET NULL ON também seleciona automaticamente a coluna NULL para cada novo campo que você adiciona à tabela usando o Table Designer e permite que você não precise incluir as cláusulas NULL ou NOT NULL em CREATE TABLE.

Para obter mais informações, consulte o comando SET NULL.
