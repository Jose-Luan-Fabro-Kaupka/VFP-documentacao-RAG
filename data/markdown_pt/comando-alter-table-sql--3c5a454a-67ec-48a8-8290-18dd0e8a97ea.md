# Comando ALTER TABLE - SQL

Modifica programaticamente a estrutura de uma tabela. Há várias versões da sintaxe.

```foxpro
ALTER TABLE TableName1 ADD | ALTER [COLUMN] FieldName1
      FieldType [( nFieldWidth [, nPrecision])] [NULL | NOT NULL] [CHECK lExpression1 [ERROR cMessageText1]]
   [AUTOINC [NEXTVALUE NextValue [STEP StepValue]]] [DEFAULT eExpression1]
   [PRIMARY KEY | UNIQUE [COLLATE cCollateSequence]]
   [REFERENCES TableName2 [TAG TagName1]] [NOCPTRANS] [NOVALIDATE]
```

```foxpro
ALTER TABLE TableName1 ALTER [COLUMN] FieldName2 [NULL | NOT NULL] [SET DEFAULT eExpression2]
   [SET CHECK lExpression2 [ERROR cMessageText2]] [ DROP DEFAULT ] [ DROP CHECK ] [ NOVALIDATE ]
```

```foxpro
ALTER TABLE TableName1 [DROP [COLUMN] FieldName3]
   [SET CHECK lExpression3 [ERRORcMessageText3]] [DROP CHECK]
   [ADD PRIMARY KEY eExpression3 [FOR lExpression4] TAG TagName2
   [COLLATE cCollateSequence]] [DROP PRIMARY KEY]
   [ADD UNIQUE eExpression4 [[FOR lExpression5] TAG TagName3
      [COLLATE cCollateSequence]]] [DROP UNIQUE TAG TagName4]
   [ADD FOREIGN KEY [eExpression5] [FOR lExpression6] TAG TagName4
      REFERENCES TableName4 [TAG TagName4][COLLATE cCollateSequence]
      REFERENCES TableName2 [TAG TagName5]]
   [DROP FOREIGN KEY TAG TagName6 [SAVE]]
   [RENAME COLUMN FieldName4 TO FieldName5] [NOVALIDATE]
```

#### Parâmetros
 **ALTER TABLE TableName1**
Modifica a estrutura de uma tabela. The TableName1 parameter especifica the name of the table to be modified.
**ADD | ALTER [COLUMN] FieldName1**
Especifica the name of the field to add or modify. A single table can contain up to 255 fields. If one or more fields allow null values, the limit decreases by one field to 254 fields. Using ALTER COLUMN resets the collating sequence to the default. You should index the table again with the desired collating sequence after performing ALTER COLUMN . You can also use the COLLATE clause in the ALTER TABLE command when appropriate (primary key or foreign key).
**FieldType [( nFieldWidth [, nPrecision ])]**
Especifica the field type, field width, and field precision (number of decimal places) for the new or modified field. FieldType can be a single letter indicating the field's data type, or a long name indicating the field's data type. Some field data types require that you specify nFieldWidth or nPrecision , or both. The following table lists the values for FieldType and whether nFieldWidth and nPrecision are required: FieldType nFieldWidth nPrecision Data type W, Blob - - Blob C, Char, Character N – Character field of width n Y, Currency – – Currency D, Date – – Date T, DateTime – – DateTime B, Double – D Double G, General – – General I, Int, Interger – – Integer L, Logical – – Logical M, Memo – – Memo N, Num, Numeric N D Numeric field of width n with d decimal places F, Float N D Floating Numeric field of width n with d decimal places Q, Varbinary n - Varbinary field of width n V, Varchar n - Varchar field of width n The nFieldWidth and nPrecision parameters are ignored for the W, Y, D, T, G, I, L, and M types. If nPrecision is not included for the N, F, or B types, the nPrecision parameter defaults to zero (no decimal places).
**NULL | NOT NULL**
Especifica whether null values are allowed in the field. NULL permits null values, while NOT NULL does not allow null values. If one or more fields can contain null values, the maximum number of fields the table can contain is reduced from 255 to 254. Note Changing the structure of a field that is used by a binary index so that it can contain null values generates an error.
**CHECK lExpression1**
Especifica a validation rule for the field. The lExpression1 parameter must evaluate to a logical expression and can be a user-defined function or a stored procedure. Visual FoxPro checks the validation rule specified in the CHECK clause when a blank record is appended.
**ERROR cMessageText1**
Especifica an error message. Visual FoxPro displays this message when the validation rule specified with the CHECK clause generates an error. The message displays only when data is changed within a Browse window or Edit window.
**AUTOINC [NEXTVALUE NextValue [STEP StepValue ]]**
Enables automatic incrementing for the field. NextValue especifica the start value and can be a positive or a negative integer value ranging from 2,147,483,647 to -2,147,483,647. The default value is 1. You can set NextValue using the Next Value spin box in Fields tab of the Table Designer. StepValue especifica the increment value for the field and can be a positive, nonzero integer value ranging from 1 to 255. The default value is 1. You can set StepValue using the Step spin box in the Fields tab of the Table Designer. Autoincrementing values cannot be NULL . Note Tables containing automatically incrementing field values append table-buffered records approximately 35% slower than tables without automatically incrementing field values, which might affect performance. When using table buffering, the table header is locked when the record is appended.
**DEFAULT eExpression1**
Especifica a default value for the field specified in FieldName1 . The data type of eExpression1 must be the same as the data type for the field. You cannot specify a default value if you use the AUTOINC clause to turn on autoincrementing for a field. Visual FoxPro generates an error message if you specify values for both the AUTOINC and DEFAULT clauses.
**PRIMARY KEY | UNIQUE**
PRIMARY KEY creates a primary index for the field specified in FieldName1 . UNIQUE creates a candidate index for the field specified in FieldName1 . The primary index tag or candidate index tag has the same name as the field. For more information about primary and candidate indexes, see Visual FoxPro Index Types .
**COLLATE cCollateSequence**
Especifica a collation sequence other than the default setting, MACHINE. The cCollateSequence parameter must be a valid Visual FoxPro collation sequence. For more information about setting collation sequences, see Optimizing International Applications and SET COLLATE Command .
**REFERENCES TableName2 [TAG TagName1 ]**
Especifica the parent table to which a persistent relationship is established. The parent table cannot be a free table. The TagName1 parameter clause especifica an index tag name for the parent table in TableName2 . Index tag names can contain up to 10 characters. If you omit the TAG clause, the relationship is established using the primary index key of the parent table. If the parent table does not have a primary index, Visual FoxPro generates an error.
**NOCPTRANS**
Prevents translation to a different code page for Character , Memo , and Varchar fields. You can specify NOCPTRANS only for Character , Memo , and Varchar fields. This creates what appears as Character (Binary), Memo (Binary), and Varchar (Binary) data types in the Table Designer.
**NOVALIDATE**
Especifica that Visual FoxPro allows changes to the table structure that can violate the data integrity of the table. By default, Visual FoxPro prevents ALTER TABLE from making such changes to the table structure. To override the default behavior, include the NOVALIDATE option.
**ALTER [COLUMN] FieldName2**
Especifica the name of a field to modify. You need to include multiple ALTER COLUMN clauses to change more than one property of a field in a single ALTER TABLE command. For more information about how ALTER COLUMN clauses are structured, see the examples in this topic.
**SET DEFAULT eExpression2**
Especifica a new default value for an existing field. The data type of eExpression2 must be the same as the data type for the field. You cannot specify a default value if you use the AUTOINC clause to turn on autoincrementing for a field. Visual FoxPro generates an error message if you specify values for both the AUTOINC and SET DEFAULT clauses.
**SET CHECK lExpression2**
Especifica a new validation rule for an existing field. The lExpression2 parameter must evaluate to a logical expression and can be a user-defined function or a stored procedure.
**ERROR cMessageText2**
Especifica an error message for the field validation rule in lExpression2 . Visual FoxPro displays this message when the field validation rule generates an error. The message displays only when data is changed within a Browse window or Edit window.
**DROP DEFAULT**
Removes the default value for an existing field.
**DROP CHECK**
Removes the validation rule for an existing field.
**DROP [COLUMN] FieldName3**
Especifica a field to remove from the table. Removing a field from the table also removes the field's default value setting and field validation rule. If index key or trigger expressions reference the field, the expressions become invalid when the field is removed. In this case, an error is not generated when the field is removed, but the invalid index key or trigger expressions generate errors at run time.
**SET CHECK lExpression3**
Especifica the table validation rule. The lExpression3 parameter must evaluate to a logical expression and can be a user-defined function or a stored procedure.
**ERRORcMessageText3**
Especifica an error message for the table validation rule in lExpression3 . Visual FoxPro displays this message when the table validation rule generates an error. The message displays only when data is changed within a Browse window or Edit window.
**DROP CHECK**
Removes the table validation rule.
**ADD PRIMARY KEY eExpression3 [FOR lExpression4 ] TAG TagName2**
Adds a primary index to the table. The eExpression3 especifica the primary index key expression. You can use lExpression4 to specify a filter expression where only records that satisfy the condition are available for display and access. Primary index keys are created in the index file just for those records that match the filter expression. You should avoid using the FOR clause to create a primary index; the uniqueness of a primary key is enforced only for those records that match the condition specified in the FOR clause. Instead, use the INDEX command with a FOR clause to create a filtered index. Rushmore Query Optimization optimizes an ALTER TABLE ... FOR lExpression4 command if the lExpression4 expression can be optimized. For the best performance, use an optimizable expression in the FOR clause. Para obter mais informações, consulte SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access . The TagName2 parameter especifica the name of the primary index tag. Index tag names can contain up to 10 characters. If you omit TAG TagName2 , and eExpression3 is a single field, the primary index tag has the same name as the field specified in eExpression3 .
**DROP PRIMARY KEY**
Removes the primary index and its index tag. A table can have only one primary key, so you do not need to specify the name of the primary key. Removing the primary index also deletes any persistent relations based on the primary key.
**ADD UNIQUE eExpressio n4 [TAG TagName3 [FOR lExpression5 ]]**
Adds a candidate index to the table. The eExpression4 parameter especifica the candidate index key expression. The TagName3 parameter especifica the name of the candidate index tag. Index tag names can contain up to 10 characters. If you omit TAG TagName3, and if eExpression4 is a single field, the candidate index tag has the same name as the field specified in eExpression4 . You can use the lExpression5 parameter to specify a filter expression where only records that satisfy the condition are available for display and access. Candidate index keys are created in the index file just for those records that match the filter expression. Rushmore optimizes an ALTER TABLE ... FOR lExpression5 command if the lExpression5 expression can be optimized. For the best performance, use an optimizable expression in the FOR clause. Para obter mais informações, consulte SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access .
**DROP UNIQUE TAG TagName4**
Removes the candidate index and its index tag. A table can have multiple candidate keys, so you must specify the name of the candidate index tag.
**ADD FOREIGN KEY [ eExpression5 ] TAG TagName4 [FOR lExpression6 ]**
Adds a foreign (non-primary) index to the table. The eExpression5 parameter especifica the foreign index key expression. The TagName4 parameter especifica the name of the foreign index tag. Index tag names can contain up to 10 characters. You can use the lExpression6 parameter to specify a filter expression where only records that satisfy the condition are available for display and access. Foreign index keys are created in the index file just for those records that match the filter expression. Rushmore optimizes an ALTER TABLE ... FOR lExpression6 command if the lExpression6 expression can be optimized. For the best performance, use an optimizable expression in the FOR clause. Para obter mais informações, consulte SET OPTIMIZE Command and Using Rushmore Query Optimization to Speed Data Access .
**REFERENCES TableName2 [TAG TagName5 ]**
Especifica the parent table to which a persistent relationship is established. You can use the TAG TagName5 clause to establish a relationship based on an existing index tag for the parent table. Index tag names can contain up to 10 characters. If you omit the TAG clause, Visual FoxPro establishes the relationship using the parent table's primary index tag.
**DROP FOREIGN KEY TAG TagName6 [SAVE]**
Deletes a foreign key whose index tag is TagName6 . You can use SAVE to keep the index tag in the structural index. If you omit SAVE , the index tag is deleted from the structural index.
**RENAME COLUMN FieldName4 TO FieldName5**
Makes it possible for you to change the name of a field in the table. The FieldName4 parameter especifica the name of the field to be renamed. The FieldName5 paramter especifica the new name of the field. Cuidado Tenha cuidado ao renomear campos de tabela porque expressões de índice, regras de validação de campo e tabela, comandos, funções e assim por diante podem fazer referência aos nomes de campo originais.

# Observações

Você pode usar ALTER TABLE para modificar a estrutura de uma tabela que não foi adicionada a um banco de dados. However, Visual FoxPro generates an error if you include the DEFAULT, FOREIGN KEY, PRIMARY KEY, REFERENCES, or SET clauses when modifying a free table.

ALTER TABLE might rebuild the table by creating a new table header and appending records to the table header. For example, changing the type or width of a field can cause the table to rebuild.

After a table is rebuilt, field validation rules are executed for any fields whose type or width is changed. If you change the type or width of any field in the table, the table rule is executed.

If you modify field or table validation rules for a table that has records, Visual FoxPro tests the new field or table validation rules against the existing data and issues a warning on the first occurrence of a field or table validation rule or of a trigger violation.

You cannot specify a value or expression in the DEFAULT clause if you turn on autoincrementing for a field.

To remove autoincrementing, use ALTER TABLE - SQL to change COLUMN but do not include the AUTOINC clause.

Field validation should remain enabled for autoincrementing fields. You might want to use validation to return a new autoincrementing value.

When you change a table that does not contain an autoincrementing field to include one, either by using ALTER TABLE or the Table Designer, autoincrementing begins with the next added row. Previous rows in the table are not updated with autoincrementing values starting with the first record. You need to make sure that no conflicts occur as a result.

ALTER TABLE might not produce consistent results when used with Visual FoxPro cursors created by the CREATE CURSOR command. In particular, you can create a Visual FoxPro cursor with features, such as long field names, that are normally available only with tables that are part of a database container. ALTER TABLE saves a temporary copy of the cursor, so the rules that apply to free tables also apply, and any features requiring database support are lost or changed in an unpredictable manner. Therefore, you should generally avoid using ALTER TABLE with Visual FoxPro cursors unless you have tested and understood the outcome.

If you omit NULL and NOT NULL, the current setting of the SET NULL command determines if null values are allowed in the field. However, if you omit NULL and NOT NULL but include the PRIMARY KEY or UNIQUE clause, Visual FoxPro disregards the current setting of SET NULL, and the field defaults to NOT NULL.

Visual FoxPro generates an error if the validation rule specified in the CHECK clause does not allow for a blank field value in an appended record.

Null values and duplicate records are not permitted in a field used for a primary or candidate index. If you are creating a new field using ADD COLUMN, Visual FoxPro does not generate an error if you create a primary or candidate index for a field that supports null values. However, Visual FoxPro generates an error if you attempt to enter a null or duplicate value into a field used for a primary or candidate index.

> **Observação:** Candidate indexes, created by including the UNIQUE option (provided for ANSI compatibility) in CREATE TABLE – SQL or ALTER TABLE – SQL commands, are not the same as indexes created in the INDEX command with the UNIQUE option. An index created in the INDEX command using the UNIQUE option allows duplicate index keys; candidate indexes do not allow duplicate index keys. For more information about the UNIQUE option in the INDEX command, see INDEX Command . The term CANDIDATE is a synonym of UNIQUE and can be used instead if you choose.

If you modify an existing field, and the primary index expression or candidate index expression consists of fields in the table, Visual FoxPro checks the fields to see if they contain null values or duplicate records. If they do, Visual FoxPro generates an error and the table is not altered.

If the table is converted to another code page, the fields for which NOCPTRANS has been specified are not translated.

# Exemplo

O Exemplo 1 adiciona a field called `Fax` to a `Customer` table and allows the field to have null values.

O Exemplo 2 torna the `Cust_id` field the primary key of the `Customer` table.

O Exemplo 3 adiciona a field validation rule to the `Quantity` field of the `Orders` table so that values in the `Quantity` field must be non-negative.

O Exemplo 4 adiciona a one-to-many persistent relation between the `Customer` and `Orders` tables based on the primary key `Cust_id` in the `Customer` table and a new foreign key index `Cust_id` in the `Orders` table.

O Exemplo 5 remove the field validation rule from the `Quantity` field in the `Orders` table.

O Exemplo 6 remove the persistent relation between the `Customer` and `Orders` tables, but keeps the `Cust_id` index tag in the `Orders` table.

O Exemplo 7 adiciona a field called `Fax2` to the `Customer` table and prevents the field from containing null values. The new structure of the table is displayed. Two ALTER COLUMN clauses are used to allow the field to have null values and set the default value for the field to the null value. Note that multiple ALTER COLUMN clauses are required to change more than one property of a field in a single ALTER TABLE command. The new field is then removed from the table to restore the table to its original state.

```foxpro
* Example 1
SET PATH TO (HOME(2) + 'Data\')     && Sets path to table.
ALTER TABLE Customer ADD COLUMN Fax c(20) NULL
* Example 2
ALTER TABLE Customer ADD PRIMARY KEY Cust_id TAG Cust_id
ALTER TABLE Customer ALTER COLUMN Cust_id Character(5) PRIMARY KEY
* Example 3
ALTER TABLE Orders;
    ALTER COLUMN Quantity SET CHECK Quantity >= 0;
    ERROR "Quantities must be non-negative"
* Example 4
ALTER TABLE Orders;
   ADD FOREIGN KEY Cust_id TAG Cust_id REFERENCES Customer
* Example 5
ALTER TABLE Orders ALTER COLUMN Quantity DROP CHECK
* Example 6
ALTER TABLE Orders DROP FOREIGN KEY TAG Cust_id SAVE
* Example 7
CLEAR
ALTER TABLE Customer ADD COLUMN Fax2 c(20) NOT NULL
DISPLAY STRUCTURE
ALTER TABLE Customer;
   ALTER COLUMN Fax2 NULL;
   ALTER COLUMN Fax2 SET DEFAULT .NULL.
ALTER TABLE Customer DROP COLUMN Fax2
```
