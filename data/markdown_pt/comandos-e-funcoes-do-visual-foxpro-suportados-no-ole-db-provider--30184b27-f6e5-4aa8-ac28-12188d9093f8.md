# Comandos e funções do Visual FoxPro suportados no OLE DB Provider

O Visual FoxPro contém linguagem que você pode usar com o OLE DB Provider for Visual FoxPro. Alguns desses elementos de linguagem são para uso somente contra o OLE DB Provider; enquanto outros podem ser usados em stored procedures, triggers, rules e default values.

> **Observação:** Você pode determinar o estado de muitos comandos SET, suportados e não suportados, exceto SET ANSI, consultando o banco de dados. Por exemplo, a linha de código a seguir retorna o valor de SET PATH no cursor resultante:

> **Note:** SELECT SET('PATH') FROM Table WHERE RECNO()=1

# Comandos chamados contra o Visual FoxPro OLE DB Provider

O Visual FoxPro OLE DB Provider suporta a sintaxe nativa de linguagem do Visual FoxPro para comandos que você pode executar contra o provider. As tabelas a seguir listam esses comandos.

Para obter mais informações sobre a sintaxe desses comandos, consulte o Visual FoxPro Language Reference.

### Comandos SQL

| ALTER TABLE - SQL Command | CREATE TABLE - SQL Command | DELETE - SQL Command |
| --- | --- | --- |
| INSERT - SQL Command (O uso do comando SQL INSERT com uma matriz, variável de memória ou um objeto não é suportado.) | SELECT - SQL Command | UPDATE - SQL Command |

### Outros comandos

| DROP TABLE Command | SET ANSI Command | SET AUTOINCERROR Command |
| --- | --- | --- |
| SET BLOCKSIZE Command | SET COLLATE Command | SET DELETED Command |
| SET ENGINEBEHAVIOR Command | SET EXACT Command | SET EXCLUSIVE Command |
| SET FULLPATH Command | SET MULTILOCKS Command | SET NULL Command |
| SET PATH Command | SET REPROCESS Command | SET UNIQUE Command |

# Comandos e funções para stored procedures, rules, triggers e default values

Você pode usar um conjunto maior de comandos em stored procedures, rules, triggers e default values. As tabelas a seguir listam esses comandos e funções.

| $ Operator | % Operator | & Command |
| --- | --- | --- |
| && Command | * Command | = Command |

### A

| ABS( ) Function | ACOPY( ) Function | ACOS( ) Function |
| --- | --- | --- |
| ADATABASES( ) Function | ADBOBJECTS( ) Function | ADD TABLE Command |
| ADEL( ) Function | AELEMENT( ) Function | AERROR( ) Function |
| AFIELDS( ) Function | AINS( ) Function | ALEN( ) Function |
| ALIAS( ) Function | ALLTRIM( ) Function | ALTER TABLE - SQL Command |
| AND Operator | APPEND Command | APPEND FROM ARRAY Command |
| APPEND GENERAL Command | APPEND GENERAL Command | APPEND MEMO Command |
| APPEND PROCEDURES Command | ASC( ) Function | ASCAN( ) Function |
| ASIN( ) Function | ASORT( ) Function | ASQLHANDLES( ) Function |
| ASUBSCRIPT( ) Function | AT( ) Function | AT_C( ) Function |
| ATAN( ) Function | ATC( ) Function | ATCC( ) Function |
| ATCLINE( ) Function | ATLINE( ) Function | ATN2( ) Function |
| AUSED( ) Function | AVERAGE Command | |

### B

| BEGIN TRANSACTION Command | BETWEEN( ) Function | BITAND( ) Function |
| --- | --- | --- |
| BITCLEAR( ) Function | BITLSHIFT( ) Function | BITNOT( ) Function |
| BITOR( ) Function | BITRSHIFT( ) Function | BITSET( ) Function |
| BITTEST( ) Function | BITXOR( ) Function | BLANK Command |
| BOF( ) Function | | |

### C

| CALCULATE Command | CANDIDATE( ) Function | CDX( ) Function |
| --- | --- | --- |
| CEILING( ) Function | CHR( ) Function | CHRTRAN( ) Function |
| CHRTRANC( ) Function | CLEARRESULTSET( ) Function | CLOSE Commands |
| CMONTH( ) Function | CONTINUE Command | COPY INDEXES Command |
| COPY PROCEDURES Command | COPY STRUCTURE Command | COPY STRUCTURE EXTENDED Command |
| COPY TO Command | CURSORGETPROP("AutoIncError") Function | CURSORTOXML( ) Function |

### D

| DATE( ) Function | DATETIME( ) Function | DAY( ) Function |
| --- | --- | --- |
| DBC( ) Function | DBF( ) Function | DBUSED( ) Function |
| DELETE - SQL Command | DELETE Command | DELETE TAG Command |
| DELETED( ) Function | DESCENDING( ) Function | DIFFERENCE( ) Function |
| DIMENSION Command | DISKSPACE( ) Function | DMY( ) Function |
| DO CASE ... ENDCASE Command | DO Command | DO WHILE ... ENDDO Command |
| DOW( ) Function | DTOC( ) Function | DTOR( ) Function |
| DTOS( ) Function | DTOT( ) Function | |

### E

| EMPTY( ) Function | END TRANSACTION Command | EOF( ) Function |
| --- | --- | --- |
| ERROR( ) Function | EVALUATE( ) Function | EXIT Command |
| EXECSCRIPT( ) Function | EXP( ) Function | |

### F

| FCOUNT( ) Function | FDATE( ) Function | FIELD( ) Function |
| --- | --- | --- |
| FILE( ) Function | FILTER( ) Function | FLDLIST( ) Function |
| FLOCK( ) Function | FLOOR( ) Function | FLUSH Command |
| FOR ... ENDFOR Command | FOR( ) Function | FOUND( ) Function |
| FREE TABLE Command | FSIZE( ) Function | FTIME( ) Function |
| FULLPATH( ) Function | FUNCTION Command | FV( ) Function |

### G

| GATHER Command | GETCP( ) Function | GETFLDSTATE( ) Function |
| --- | --- | --- |
| GETNEXTMODIFIED( ) Function | GETRESULTSET( ) Function | GO | GOTO Command |
| GOMONTH( ) Function | | |

### H

| HEADER( ) Function | HOUR( ) Function |
| --- | --- |

### I

| ICASE( ) Function | IDXCOLLATE( ) Function | IF ... ENDIF Command |
| --- | --- | --- |
| IIF( ) Function | INDBC( ) Function | INDEX Command |
| INLIST( ) Function | INSERT - SQL Command | INT( ) Function |
| ISALPHA( ) Function | ISBLANK( ) Function | ISDIGIT( ) Function |
| ISEXCLUSIVE( ) Function | ISLEADBYTE( ) Function | ISLOWER( ) Function |
| ISREADONLY( ) Function | ISUPPER( ) Function | |

### K

| KEY( ) Function | KEYMATCH( ) Function |
| --- | --- |

### L

| LEFT( ) Function | LEFTC( ) Function | LEN( ) Function |
| --- | --- | --- |
| LENC( ) Function | LIKE( ) Function | LIKEC( ) Function |
| LOCAL Command | LOCATE Command | LOCK( ) Function |
| LOG( ) Function | LOG10( ) Function | LOOKUP( ) Function |
| LOWER( ) Function | LPARAMETERS Command | LTRIM( ) Function |
| LUPDATE( ) Function | | |

### M

| _MLINE System Variable | MAKETRANSACTABLE( ) Function | MAX( ) Function |
| --- | --- | --- |
| MDX( ) Function | MDY( ) Function | MEMLINES( ) Function |
| MESSAGE( ) Function | MIN( ) Function | MINUTE( ) Function |
| MLINE( ) Function | MOD( ) Function | MONTH( ) Function |
| MTON( ) Function | | |

### N

| NDX( ) Function | NORMALIZE( ) Function | NOT Operator |
| --- | --- | --- |
| NOTE Command | NTOM( ) Function | NVL( ) Function |

### O

| OCCURS( ) Function | OLDVAL( ) Function | ON ERROR Command |
| --- | --- | --- |
| ON KEY Command | ON( ) Function | OPEN DATABASE Command |
| OR Operator | ORDER( ) Function | OS( ) Function |

### P

| PACK Command | PADL( ) | PADR( ) | PADC( ) Functions | PARAMETERS Command |
| --- | --- | --- |
| PARAMETERS( ) Function | PAYMENT( ) Function | PI( ) Function |
| PRIMARY( ) Function | PRIVATE Command | PROCEDURE Command |
| PROGRAM( ) Function | PROPER( ) Function | PUBLIC Command |
| PV( ) Function | | |

### R

| RAND( ) Function | RAT( ) Function | RATC( ) Function |
| --- | --- | --- |
| RATLINE( ) Function | RECALL Command | RECCOUNT( ) Function |
| RECNO( ) Function | RECSIZE( ) Function | RELATION( ) Function |
| REMOVE TABLE Command | REPLACE Command | REPLACE FROM ARRAY Command |
| REPLICATE( ) Function | RETRY Command | RETURN Command |
| RIGHT( ) Function | RIGHTC( ) Function | RLOCK( ) Function |
| ROLLBACK Command | ROUND( ) Function | RTOD( ) Function |
| RTRIM( ) Function | | |

### S

| SCAN ... ENDSCAN Command | SCATTER Command | SEC( ) Function |
| --- | --- | --- |
| SECONDS( ) Function | SEEK Command | SEEK( ) Function |
| SELECT - SQL Command | SELECT Command | SELECT( ) Function |
| SET AUTOINCERROR Command | SET BLOCKSIZE Command | SET COLLATE Command |
| SET DATABASE Command | SET DEFAULT Command | SET DELETED Command |
| SET ENGINEBEHAVIOR Command | SET EXACT Command | SET EXCLUSIVE Command |
| SET FDOW Command | SET FIELDS Command | SET FILTER Command |
| SET FIXED Command | SET FULLPATH Command | SET FWEEK Command |
| SET HOURS Command | SET INDEX Command | SET LOCK Command |
| SET MULTILOCKS Command | SET NEAR Command | SET NOCPTRANS Command |
| SET NOTIFY Command | SET NULL Command | SET OPTIMIZE Command |
| SET ORDER Command | SET PATH Command | SET PROCEDURE Command |
| SET REFRESH Command | SET RELATION Command | SET RELATION OFF Command |
| SET REPROCESS Command | SET SKIP Command | SET UDFPARMS Command |
| SET UNIQUE Command | SET VOLUME Command | SET( ) Function |
| SETFLDSTATE( ) Function | SETRESULTSET( ) Function | SIGN( ) Function |
| SIN( ) Function | SKIP Command | SORT Command |
| SPACE( ) Function | SQRT( ) Function | STORE Command |
| STR( ) Function | STRCONV( ) Function | STRTRAN( ) Function |
| STUFF( ) Function | STUFFC( ) Function | SUBSTR( ) Function |
| SUBSTRC( ) Function | SUM Command | SYS(0) - Network Machine Information |
| SYS(1) - Julian System Date | SYS(2) - Seconds Since Midnight | SYS(3) - Legal File Name |
| SYS(5) - Default Drive | SYS(10) - String from Julian Day Number | SYS(11) - Julian Day Number |
| SYS(12) - Available Memory in Bytes | SYS(1104) - Purge Memory Cache | SYS(2001) – SET ... Command Status |
| SYS(2003) – Current Directory | SYS(2004) – Visual FoxPro Start Directory | SYS(2007) - Checksum Value |
| SYS(2011) - Current Lock Status | SYS(2015) - Unique Procedure Name | SYS(2029) - Table Type |
| SYS(3050) - Set Buffer Memory Size | | |

### T

| _TALLY System Variable | _TRIGGERLEVEL System Variable | TABLEREVERT( ) Function |
| --- | --- | --- |
| TABLEUPDATE( ) Function | TAG( ) Function | TAGCOUNT( ) Function |
| TAGNO( ) Function | TAN( ) Function | TARGET( ) Function |
| TIME( ) Function | TOTAL Command | TRIM( ) Function |
| TTOC( ) Function | TTOD( ) Function | TXNLEVEL( ) Function |
| TYPE( ) Function | | |

### U

| UNIQUE( ) Function | UNLOCK Command | UPDATE - SQL Command |
| --- | --- | --- |
| UPDATE Command | UPPER( ) Function | USE Command |
| USED( ) Function | | |

### V

| VAL( ) Function | VERSION( ) Function |
| --- | --- |

### W

| WEEK( ) Function |
| --- |

### X

| XMLTOCURSOR( ) Function | XMLUPDATEGRAM( ) Function |
| --- | --- |

### Y

| YEAR( ) Function |
| --- |

### Z

| ZAP Command |
| --- |
