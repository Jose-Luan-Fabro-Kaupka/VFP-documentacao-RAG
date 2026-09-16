# Mapeamento de tipos de dados entre Visual FoxPro e XML Schema

As tabelas a seguir descrevem os seguintes mapeamentos padrão de tipos de dados entre Visual FoxPro e tipos de dados de esquema XML:
 - Tipos de dados primitivos XML Schema para tipos de dados Visual FoxPro
- Tipos derivados XML Schema para tipos de dados Visual FoxPro
- Tipos de dados Visual FoxPro para tipos de dados XML Schema Definition (XSD)
- Tipos de dados XML Schema Definition (XSD) para tipos de dados Visual FoxPro
- Tipos de dados XML Data Reduced (XDR) Schema para tipos de dados Visual FoxPro
 Tipos de dados primitivos XML Schema para tipos de dados Visual FoxPro
| Tipo de dados XML | Facets | Descrição | Tipo de dados Visual FoxPro |
| --- | --- | --- | --- |
| anyURI | length, pattern, maxLength, minLength, enumeration, whiteSpace | Representa um Uniform Resource Identifier (URI) conforme definido pela RFC 2396. An anyURI value can be absolute or relative and might have an optional fragment identifier. | Memo. Visual FoxPro applies a hyperlink to a URI in a Memo. |
| base64Binary | length, pattern, maxLength, minLength, enumeration, whiteSpace | Representa dados binários arbitrários codificados em base64. A base64Binary is the set of finite-length sequences of binary octets. | Memo (Binary), Varbinary or Blob |
| boolean | pattern, whiteSpace | Representa valores Boolean, que são true ou false. | Logical |
| date | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa uma data de calendário. The pattern for date is CCYY-MM-DD with an optional time zone indicator as allowed for dateTime . | Date |
| dateTime | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa uma instância específica de tempo. The pattern for dateTime is CCYY-MM-DDThh:mm:ss where CC represents the century, YY the year, MM the month, and DD the day, preceded by an optional leading negative (-) character to indicate a negative number. If the negative character is omitted, positive (+) is assumed. The T is the date/time separator and hh, mm, and ss represent hour, minute, and second respectively. Additional digits can be used to increase the precision of fractional seconds if desired. For example, the format ss.ss... with any number of digits after the decimal point is supported. The fractional seconds part is optional. This representation may be immediately followed by a "Z" to indicate Coordinated Universal Time (UTC) or to indicate the time zone. For example, the difference between the local time and Coordinated Universal Time, immediately followed by a sign, + or -, followed by the difference from UTC represented as hh:mm (minutes is required). If the time zone is included, both hours and minutes must be present. | DateTime |
| decimal | enumeration, pattern, totalDigits, fractionDigits, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa números de precisão arbitrária. | Numeric, Currency, or Character |
| double | pattern, enumeration, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa números de ponto flutuante de 64 bits de precisão dupla. | Double |
| duration | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa duração de tempo. The pattern for duration is PnYnMnDTnHnMnS, where nY represents the number of years, nM the number of months, nD the number of days, T the date/time separator, nH the number of hours, nM the number of minutes, and nS the number of seconds. For example, to indicate a duration of 1 year, 2 months, 3 days, 10 hours, and 30 minutes, you write: P1Y2M3DT10H30M. You could also indicate a duration of minus 120 days as -P120D. | Character (C(30)) |
| float | pattern, enumeration, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Representa números de ponto flutuante de 32 bits de precisão simples. | Double |
| gDay | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents a Gregorian day that recurs, specifically a day of the month, such as the fifth day of the month. A gDay is the space of a set of calendar dates. Specifically, it is a set of one-day long, monthly periodic instances. The pattern for gDay is --DD with an optional time zone indicator as allowed for date . | Character (C(10)) |
| gMonth | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents a Gregorian month that recurs every year. A gMonth is the space of a set of calendar months. Specifically, it is a set of one-month long, yearly periodic instances. The pattern for gMonth is -MM- with an optional time zone indicator as allowed for date . | Character (C(10)) |
| gMonthDay | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents a specific Gregorian date that recurs, specifically a day of the year, such as the third of May. A gMonthDay is the set of calendar dates. Specifically, it is a set of one-day long, annually periodic instances. The pattern for gMonthDay is --MM-DD with an optional time zone indicator as allowed for date . | Character (C(10)) |
| gYear | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents a Gregorian year. A set of one month-long, nonperiodic instances. The pattern for gYear is CCYY with an optional time zone indicator as allowed for dateTime . | Character (C(15)) |
| gYearMonth | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents a specific Gregorian month in a specific Gregorian year. A set of one month-long, nonperiodic instances. The pattern for gYearMonth is CCYY-MM with an optional time zone indicator. | Character (C(15)) |
| hexBinary | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents arbitrary hex-encoded binary data. A hexBinary is the set of finite-length sequences of binary octets. Each binary octet is encoded as a character tuple, consisting of two hexadecimal digits ([0-9a-fA-F]) representing the octet code. | Memo (Binary) |
| NOTATION | length, enumeration, pattern, maxLength, minLength, whiteSpace | Represents a NOTATION attribute type. A set of QNames. | Memo |
| QName | length, enumeration, pattern, maxLength, minLength, whiteSpace | Represents a qualified name. A qualified name is composed of a prefix and a local name separated by a colon. Both the prefix and local names must be an NCName. The prefix must be associated with a namespace Uniform Resource Identifier (URI) reference, using a namespace declaration. | Memo |
| string | length, pattern, maxLength, minLength, enumeration, whiteSpace | Representa cadeias de caracteres. | Character when maxLength is specified and less than 255 characters. Otherwise, Memo. |
| time | enumeration, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, whiteSpace | Represents an instance of time that recurs every day. The pattern for time is hh:mm:ss.sss with an optional time zone indicator. | Character (C(20)) |
 Tipos derivados XML Schema para tipos de dados Visual FoxPro
| Tipo de dados XML | Facets | Descrição | Tipo de dados Visual FoxPro |
| --- | --- | --- | --- |
| byte | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum value of -128 and maximum of 127. This data type is derived from short. | Integer |
| ENTITIES | length, maxLength, minLength, enumeration, whiteSpace | Represents the ENTITIES attribute type and contains a set of values of type ENTITY. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| ENTITY | length, enumeration, pattern, maxLength, minLength, whiteSpace | Represents the ENTITY attribute type in XML 1.0 Recommendation. This is a reference to an unparsed entity with a name that matches the specified name. An ENTITY must be an NCName and must be declared in the schema as an unparsed entity name. This data type is derived from NCName. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| ID | length, enumeration, pattern, maxLength, minLength, whiteSpace | Represents the ID attribute type defined in the XML 1.0 Recommendation. The ID must be a no-colon-name (NCName) and must be unique within an XML document. This data type is derived from NCName. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| IDREF | length, enumeration, pattern, maxLength, minLength, whiteSpace | Represents a reference to an element that has an ID attribute that matches the specified ID. An IDREF must be an NCName and must be a value of an element or attribute of type ID within the XML document. This data type is derived from NCName. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| IDREFS | length, maxLength, minLength, enumeration, whiteSpace | Represents the IDREFS attribute type and contains a set of values of type IDREF. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| int | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum value of -2147483648 and maximum of 2147483647. This data type is derived from long. | Integer |
| integer | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents a sequence of decimal digits with an optional leading sign (+ or -). This data type is derived from decimal. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| language | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents natural language identifiers (defined by RFC 1766). This data type is derived from token. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| long | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum value of -9223372036854775808 and maximum of 9223372036854775807. This data type is derived from integer. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| Name | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents names in XML. A Name is a token that begins with a letter, underscore, or colon and continues with name characters (letters, digits, and other characters). This data type is derived from token. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| NCName | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents noncolonized names. This data type is the same as Name, except it cannot begin with a colon. This data type is derived from Name. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| negativeInteger | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer that is less than zero and consists of a negative sign (-) and sequence of decimal digits. This data type is derived from nonPositiveInteger. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| NMTOKEN | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents the NMTOKEN attribute type. An NMTOKEN is set of name characters, such as letters, digits, and other characters, in any combination. Unlike Name and NCName, NMTOKEN has no restrictions on the starting character. This data type is derived from token. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| NMTOKENS | length, maxLength, minLength, enumeration, whiteSpace | Represents the NMTOKENS attribute type and contains a set of values of type NMTOKEN. | Memo |
| nonNegativeInteger | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer that is greater than or equal to zero. This data type is derived from integer. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| nonPositiveInteger | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer that is less than or equal to zero and A nonPositiveInteger consists of a negative sign (-) and sequence of decimal digits. This data type is derived from integer. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| normalizedString | length, pattern, maxLength, minLength, enumeration, whiteSpace | Represents white space normalized strings. This data type is derived from string. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| positiveInteger | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer that is greater than zero. This data type is derived from nonNegativeInteger. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| token | enumeration, pattern, length, minLength, maxLength, whiteSpace | Represents tokenized strings. This data type is derived from normalizedString. | Character, if maxLength is specified and less than 255. Otherwise, Memo. |
| short | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum value of -32768 and maximum of 32767. This data type is derived from int. | Integer |
| unsignedByte | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum of zero and maximum of 255. This data type is derived from unsignedShort. | Integer |
| unsignedInt | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum of zero and maximum of 4294967295. This data type is derived from unsignedLong. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| unsignedLong | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum of zero and maximum of 18446744073709551615. This data type is derived from nonNegativeInteger. | Integer, if totalDigits is less than 10. Otherwise, Character with totalDigits respected. |
| unsignedShort | enumeration, fractionDigits, pattern, minInclusive, minExclusive, maxInclusive, maxExclusive, totalDigits, whiteSpace | Represents an integer with a minimum of zero and maximum of 65535. This data type is derived from unsignedInt. | Integer |
 Tipos de dados Visual FoxPro para tipos de dados XML Schema Definition (XSD)
| Tipo de dados Visual FoxPro | Tipo de dados XSD e exemplos | Restrições e restrição de exemplo | Comentários |
| --- | --- | --- | --- |
| Blob | xs:base64Binary | <xs:element name="ts12" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:base64Binary"/> </xs:simpleType> </xs:element> | O conteúdo é traduzido para codificação base64. Mapeia para SQL Binary. |
| Character | xs:string Confirm this is electric | <xs:element name="cc04" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:string"> <xs:maxLength value="128"/> </xs:restriction> </xs:simpleType> </xs:element> | |
| Character (Binary) | xs:string Confirm this is electric | <xs:element name="cc04" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:string"> <xs:maxLength value="128"/> </xs:restriction> </xs:simpleType> </xs:element> | |
| Currency | xs:decimal -1.23, 0, 123, 4, 1000.00 | <xs:element name="yc07" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:decimal"> <xs:totalDigits value="19"/> <xs:fractionDigits value="4"/> </xs:restriction> </xs:simpleType> </xs:element> | Currency é sempre 19,4. |
| Date | xs:date 1999-05-31 | None | |
| DateTime | xs:dateTime 1999-05-31T13:20:00.000-05:00 | None | |
| Double | xs:double -INF, -1E4, -0, 0, 12.78E-2, 12, INF, NaN | None | The export value should include the maximum scale allowed for double and not be limited to display scale (internal value of double). |
| Float | xs:decimal | <xs:element name="fc06" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:decimal"> <xs:totalDigits value="14"/> <xs:fractionDigits value="4"/> </xs:restriction> </xs:simpleType> </xs:element> | totalDigits é o número de dígitos não incluindo o ponto decimal. |
| General | Não suportado | | |
| Integer | xs:int -1, 126789675 | | |
| Logical | xs:boolean true, false, 1, 0 | Os valores são true e false ou 1 e 0. | |
| Memo | xs:string | <xs:element name="mc03" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:string"> <xs:maxLength value="2147483647"/> </xs:restriction> </xs:simpleType> </xs:element> | |
| Memo (Binary) | xs:base64Binary | <xs:element name="ts12" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:base64Binary"/> </xs:simpleType> </xs:element> | O conteúdo é traduzido para codificação base64. Mapeia para SQL Binary. |
| Numeric | xs:decimal -1.23, 0, 123, 1000.00 | <xs:element name="nc00" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:decimal"> <xs:totalDigits value="10"/> <xs:fractionDigits value="4"/> </xs:restriction> </xs:simpleType> </xs:element > | totalDigits é o número de dígitos não incluindo o ponto decimal. |
| Varbinary | xs:base64Binary | <xs:element name="cc04" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:base64Binary"> <xs:maxLength value="128"/> </xs:restriction> </xs:simpleType> </xs:element> | Content is translated to base64 encoding. |
| Varchar | xs:string Confirm this is electric | <xs:element name="cc04" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:string"> <xs:maxLength value="128"/> </xs:restriction> </xs:simpleType> </xs:element> | |
| Varchar (Binary) | xs:string Confirm this is electric | <xs:element name="cc04" minOccurs="0"> <xs:simpleType> <xs:restriction base="xs:string"> <xs:maxLength value="128"/> </xs:restriction> </xs:simpleType> </xs:element> | |

Tipos de dados XML Schema Definition (XSD) para tipos de dados Visual FoxPro

| Tipo de dados XSD | Tipo de dados Visual FoxPro |
| --- | --- |
| xsd:binaryBase64 | Memo (Binary) |
| xsd:boolean | Logical |
| xsd:date | Date |
| xsd:dateTime | DateTime |
| xsd:decimal | Numeric |
| xsd:double | Double |
| xsd:int | Integer |
| xsd:string | Character |
| xsd:string (more than 254 characters in length) | Memo |
 Tipos de dados XML Data Reduced (XDR) Schema para tipos de dados Visual FoxPro
| Tipo de dados XDR | Descrição | Tipo de dados Visual FoxPro | Tipo XSD |
| --- | --- | --- | --- |
| bin.base64 | Specifies MIME-style Base64-encoded binary data. | Memo (Binary) | base64Binary |
| bin.hex | Specifies hexadecimal-encoded binary data. | Memo (Binary) | hexBinary |
| boolean | Especifica um valor Boolean de 0 ou 1. Exemplo: 0 é false e 1 é true. | Logical | boolean |
| char | Specifies a number corresponding to the Unicode representation of a single character. | None | Não suportado |
| date | Especifica a data em um subconjunto do formato ISO 8601 sem os dados de hora. Exemplo: "1994-11-05" | Date | date |
| dateTime | Specifies a date in a subset of the ISO 8601 format with optional time and no optional zone. Fractional seconds can be as precise as nanoseconds. Example: "1988-04-07T18:39:09" | DateTime | dateTime |
| dateTime.tz | Specifies a date in a subset of the ISO 8601 format with optional time and optional zone. Fractional seconds can be as precise as nanoseconds. Example: "1988-04-07T18:39:09-08:00" | None | None |
| entity | Specifies a reference to an unparsed entity, requiring a matching <!ENTITY> declaration for each instance of the entity. | None | None |
| entities | Specifies a list of entities delimited by white space. | None | None |
| enumeration | Similar to nmtoken but with an explicit list of allowed values. Supported on attributes only. Example: "Red Blue Green" | None | None |
| fixed.14.4 | Specifies a number with no more than fourteen digits to the left of the decimal point and no more than four to the right of the decimal point. Example: 9999.0044 | Currency | decimal 19,4 |
| float | Specifies a real floating point number. Examples: 111, 3.14, -123.456E+10 | Double | double |
| i1 | Specifies a 1-byte integer with an optional sign ranging from -128 to 127. Examples: 1, 127, -128 | Integer | byte |
| i2 | Specifies a 2-byte integer with optional sign ranging from -32768 to 32767. Examples: 1, 703, -32768 | Integer | short |
| i4 | Specifies a 4-byte integer with optional sign ranging from -2147483648 to 2147483647 Examples: 1, 703, -32768, 148343, -1000000000 | Integer | int |
| i8 | Specifies an 8-byte integer with optional sign ranging from -9223372036854775808 to 9223372036854775807. Examples: 1, 703, -32768, 1483433434334, -1000000000000000 | Character or Integer | long |
| id | Specifies a value that identifies an attribute as an id type attribute. The id values must be unique throughout the document. In a document, idref(s) attributes refer to an id type attribute, forming a relationship similar to primary key and foreign key in relational databases. Example: Cust1 | None | None |
| idref | Specifies a value corresponding to an id type, enabling intra-document links. Example: Cust1 | None | None |
| idrefs | Similar to idref, except it contains multiple id type values separated by white space. Example: Cust1 Cust2 Cust3 | None | None |
| int | Specifies a signed integer. Examples 11123, -123 | Integer | int |
| nmtoken | Contains values that conform to the rules of the name token. Example: Cust1 | None | None |
| nmtokens | Similar to nmtoken except it can have a list of nmtoken values separated by white space. Example: Cust1 Cust2 Cust3 | None | None |
| notation | A NOTATION type | None | None |
| number | A number with no limits on the digits Examples: 111, 3.14, -123.456E+10 Note For ADO RecordSets, a special case exists where the number might have Currency type. When dt:type='number' in an ADO XDR Schema, Visual FoxPro checks for the existence of rs:dbtype='currency' . | Character, Currency, or Numeric as appropriate | decimal |
| r4 | Same as float but only 4-byte encoding. Value ranges from 1.17549435E-38F to 3.40282347E+38F. | Double | float |
| r8 | Specifies a floating point number. This data type supports only 15 digits of precision and value ranges from 2.2250738585072014E-308 to 1.7976931348623157E+308. | Double | double |
| string | Especifica uma cadeia de caracteres. Exemplo: "This is a string" | Character, if maxLength is less than 255. Otherwise, Memo. | string |
| time | Specifies a time in a subset of the ISO 8601 format with no date and no time zone. Example: "08:15:27" | None | None |
| time.tz | Specifies a time in a subset of the ISO 8601 format with no date but optional time zone. Example: "08:15:27-05:00" | None | None |
| ui1 | Specifies a 1-byte unsigned integer ranging from 0 to 255. Examples: 1, 255 | Integer | unsignedByte |
| ui2 | Specifies a 2-byte unsigned integer ranging from 0 to 65535. Examples: 1, 255, 65535 | Integer | unsignedShort |
| ui4 | Specifies a 4-byte unsigned integer ranging from 0 to 4294967296. Examples: 1, 703, 3000000000 | Character or Integer | unsignedInt |
| ui8 | Specifies an 8-byte unsigned integer ranging from 0 to 18446744073709551615. Example: 1483433434334 | Character or Integer | unsignedLong |
| uri | Identifica um Uniform Resource Identifier (URI). Exemplo: "urn:schemas-microsoft-com:Office9" | Memo | anyURI |
| uuid | Contains hexadecimal digits representing octets with optional embedded hyphens that are ignored. Example: 333C7BC4-460F-11D0-BC04-0080C7055A83 | Character (C(40)) | string |
