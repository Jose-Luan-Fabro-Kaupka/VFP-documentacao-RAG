# Comandos e funções Visual FoxPro não suportados no OLE DB Provider

Determinados comandos e funções Visual FoxPro não são suportados pelo OLE DB Provider. O OLE DB Provider suporta a linguagem Visual FoxPro relacionada a dados e não suporta linguagem de objetos ou de interface do usuário.

As tabelas a seguir listam os comandos e funções mais comumente usados que não são suportados pelo OLE DB Provider.

# #, ::, !, ?, \, @

| #DEFINE ... #UNDEF | #IF ... #ENDIF Preprocessor Directive | #IFDEF | #IFNDEF |
| --- | --- | --- |
| #INCLUDE Preprocessor Directive | :: Scope Resolution Operator | ! Command (see RUN | ! Command) |
| ? | ?? Command | ??? Command | \ | \\ Command |
| @ ... BOX Command | @ ... CLASS Command | @ ... CLEAR Command |
| @ ... EDIT - Edit Boxes Command | @ ... FILL Command | @ ... GET |
| @ ... MENU Command | @ ... PROMPT Command | @ ... SAY Command |
| @ ... SCROLL Command | @ ... TO Command | |

# A

| _ALIGNMENT System Memory Variable | ACCEPT Command | ACLASS( ) Function |
| --- | --- | --- |
| ACTIVATE MENU Command | ACTIVATE POPUP Command | ACTIVATE SCREEN Command |
| ACTIVATE WINDOW Command | ActivateCell Method | ADD CLASS Command |
| ADIR( ) Function | AFONT( ) Function | AINSTANCE( ) Function |
| AMEMBERS( ) Function | ANSITOOEM( ) Function | APRINTERS( ) Function |
| ASELOBJ( ) Function | ASSIST Command | ATAGINFO( ) Function |

# B

| _BEAUTIFY System Memory Variable | _BOX System Memory Variable | _BROWSER System Memory Variable |
| --- | --- | --- |
| _BUILDER System Memory Variable | BAR( ) Function | BARCOUNT( ) Function |
| BARPROMPT( ) Function | BROWSE Command | BUILD APP Command |
| BUILD EXE Command | BUILD PROJECT Command | |

# C

| _CALCVALUE System Memory Variable | _CLIPTEXT System Memory Variable | _CONVERTER System Memory Variable |
| --- | --- | --- |
| _CUROBJ System Memory Variable | CALL Command | CANCEL Command |
| CAPSLOCK( ) Function | CAST( ) Function | CD Command |
| CHANGE Command | CHDIR Command | CHRSAW( ) Function |
| CLOSE MEMO Command | CNTBAR( ) Function | CNTPAD( ) Function |
| COL( ) Function | COMPILE Command | COMPOBJ( ) Function |
| Container Object | Control Object | COPY FILE Command |
| COPY MEMO Command | CREATE CLASS Command | CREATE CLASSLIB Command |
| CREATE COLOR SET Command | CREATE Command | CREATE CONNECTION Command |
| CREATE DATABASE Command | CREATE FORM Command | CREATE FROM Command |
| CREATE LABEL Command | CREATE MENU Command | CREATE PROJECT Command |
| CREATE QUERY Command | CREATE REPORT Command | CREATE SCREEN Command |
| CREATE SQL VIEW Command | CREATE TRIGGER Command | CREATE VIEW Command |
| CREATEOBJECT( ) Function | CURDIR( ) Function | |

# D

| _DBLCLICK System Memory Variable | _DIARYDATE System Memory Variable | DBSETPROP( ) Function |
| --- | --- | --- |
| DDE Functions | DEACTIVATE MENU Command | DEACTIVATE POPUP Command |
| DEACTIVATE WINDOW Command | DECLARE - DLL Command | DECLARE Command |
| DEFINE BAR Command | DEFINE BOX Command | DEFINE CLASS Command |
| DEFINE MENU Command | DEFINE PAD Command | DEFINE POPUP Command |
| DEFINE WINDOW Command | DELETE CONNECTION Command | DELETE DATABASE Command |
| DELETE FILE Command | DELETE TAG Command | DELETE TRIGGER Command |
| DELETE VIEW Command | DIR Command | DIRECTORY Command |
| DISPLAY Command | DISPLAY CONNECTIONS Command | DISPLAY DATABASE Command |
| DISPLAY DLLS Command | DISPLAY FILES Command | DISPLAY MEMORY Command |
| DISPLAY OBJECTS Command | DISPLAY PROCEDURES Command | DISPLAY STATUS Command |
| DISPLAY STRUCTURE Command | DISPLAY TABLES Command | DISPLAY VIEWS Command |
| DO FORM Command | | |

# E

| EDIT Command | EJECT Command | EJECT PAGE Command |
| --- | --- | --- |
| ERASE Command | ERROR Command | EXPORT Command |
| EXTERNAL Command | | |

# F

| _FOXDOC System Memory Variable | _FOXGRAPH System Memory Variable | FCHSIZE( ) Function |
| --- | --- | --- |
| FCLOSE( ) Function | FCREATE( ) Function | FEOF( ) Function |
| FERROR( ) Function | FFLUSH( ) Function | FGETS( ) Function |
| FILER Command | FIND Command | FKLABEL( ) Function |
| FKMAX( ) Function | FONTMETRIC( ) Function | FOPEN( ) Function |
| FPUTS( ) Function | FREAD( ) Function | FSEEK( ) Function |
| FWRITE( ) Function | | |

# G

| _GENGRAPH System Memory Variable | _GENMENU System Memory Variable | _GENPD System Memory Variable |
| --- | --- | --- |
| _GENSCRN System Memory Variable | _GENXTAB System Memory Variable | GETBAR( ) Function |
| GETCOLOR( ) Function | GETDIR( ) Function | GETENV( ) Function |
| GETEXPR Command | GETFILE( ) Function | GETFONT( ) Function |
| GETOBJECT( ) Function | GETPAD( ) Function | GETPICT( ) Function |
| GETPRINTER( ) Function | | |

# H

| HELP Command | HIDE MENU Command | HIDE POPUP Command |
| --- | --- | --- |
| HIDE WINDOW Command | HOME( ) Function | |

# I

| _INDENT System Memory Variable | IMESTATUS( ) Function | IMPORT Command |
| --- | --- | --- |
| INDEX ON Command | INKEY( ) Function | INPUT Command |
| INSERT - SQL Command (Applies only to using the SQL INSERT command with an array, memory variable, or an object.) | INSERT Command | INSMODE( ) Function |
| ISCOLOR( ) Function | ISMOUSE( ) Function | |

# J

| JOIN Command |
| --- |

# K

| KEYBOARD Command |
| --- |

# L

| _LMARGIN System Memory Variable | LABEL Command | LASTKEY( ) Function |
| --- | --- | --- |
| LINENO( ) Function | LIST Commands | LIST CONNECTIONS Command |
| LOAD Command | LOCFILE( ) Function | |

# M

| MCOL( ) Function | MD Command | MDOWN( ) Function |
| --- | --- | --- |
| MEMORY( ) Function | MENU Command | MENU TO Command |
| MENU( ) Function | MESSAGEBOX( ) Function | MKDIR Command |
| MODIFY CLASS Command | MODIFY COMMAND Command | MODIFY CONNECTION Command |
| MODIFY DATABASE Command | MODIFY FILE Command | MODIFY FORM Command |
| MODIFY GENERAL Command | MODIFY LABEL Command | MODIFY MEMO Command |
| MODIFY MENU Command | MODIFY PROCEDURE Command | MODIFY PROJECT Command |
| MODIFY QUERY Command | MODIFY REPORT Command | MODIFY SCREEN Command |
| MODIFY STRUCTURE Command | MODIFY VIEW Command | MODIFY WINDOW Command |
| MOUSE Command | MOVE POPUP Command | MOVE WINDOW Command |
| MRKBAR( ) Function | MRKPAD( ) Function | MROW( ) Function |
| MWINDOW( ) Function | | |

# N

| NEWOBJECT( ) Function | NUMLOCK( ) Function |
| --- | --- |

# O

| OBJNUM( ) Function | OBJTOCLIENT( ) Function | OBJVAR( ) Function |
| --- | --- | --- |
| OEMTOANSI( ) Function | ON APLABOUT Command | ON BAR Command |
| ON ESCAPE Command | ON EXIT BAR Command | ON EXIT MENU Command |
| ON EXIT PAD Command | ON EXIT POPUP Command | ON KEY = Command |
| ON KEY LABEL Command | ON MACHELP Command | ON PAD Command |
| ON PAGE Command | ON READERROR Command | ON SELECTION BAR Command |
| ON SELECTION MENU Command | ON SELECTION PAD Command | ON SELECTION POPUP Command |
| ON SHUTDOWN Command | | |

# P

| _PADVANCE System Memory Variable | _PAGENO System Memory Variable | _PBPAGE System Memory Variable |
| --- | --- | --- |
| _PCOLNO System Memory Variable | _PCOPIES System Memory Variable | _PDRIVER System Memory Variable |
| _PDSETUP System Memory Variable | _PECODE System Memory Variable | _PEJECT System Memory Variable |
| _PEPAGE System Memory Variable | _PLENGTH System Memory Variable | _PLINENO System Memory Variable |
| _PLOFFSET System Memory Variable | _PPITCH System Memory Variable | _PQUALITY System Memory Variable |
| _PRETEXT System Memory Variable | _PSCODE System Memory Variable | _PSPACING System Memory Variable |
| _PWAIT System Memory Variable | PACK DATABASE Command | PAD( ) Function |
| PCOL( ) Function | PEMSTATUS( ) Function | PLAY MACRO Command |
| POP KEY Command | POP MENU Command | POP POPUP Command |
| POPUP( ) Function | PRINTJOB ... ENDPRINTJOB Command | PRINTSTATUS( ) Function |
| PRMBAR( ) Function | PRMPAD( ) Function | PROMPT( ) Function |
| PROW( ) Function | PRTINFO( ) Function | PUSH KEY Command |
| PUSH MENU Command | PUSH POPUP Command | PUTFILE( ) Function |

# Q

| QUIT Command |
| --- |

# R

| _RMARGIN System Memory Variable | RD Command | RDLEVEL( ) Function |
| --- | --- | --- |
| READ Command | READ MENU Command | READKEY( ) Function |
| REFRESH() Function | REINDEX Command | RELEASE BAR Command |
| RELEASE CLASSLIB Command | RELEASE Command | RELEASE LIBRARY Command |
| RELEASE MENUS Command | RELEASE MODULE Command | RELEASE PAD Command |
| RELEASE POPUPS Command | RELEASE PROCEDURE Command | RELEASE WINDOWS Command |
| REMOVE CLASS Command | RENAME CLASS Command | RENAME Command |
| RENAME CONNECTION Command | RENAME TABLE Command | RENAME VIEW Command |
| REPORT FORM Command | REQUERY( ) Function | RESTORE FROM Command |
| RESTORE MACROS Command | RESTORE SCREEN Command | RESTORE WINDOW Command |
| RESUME Command | RGB( ) Function | RGBSCHEME( ) Function |
| RMDIR Command | ROW( ) Function | RUN | ! Command |

# S

| _SCREEN System Memory Variable | _SHELL System Memory Variable | _SPELLCHK System Memory Variable |
| --- | --- | --- |
| _STARTUP System Memory Variable | SAVE MACROS Command | SAVE SCREEN Command |
| SAVE TO Command | SAVE WINDOWS Command | SCHEME( ) Function |
| SCOLS( ) Function | SCROLL Command | SET ALTERNATE Command |
| SET APLABOUT Command | SET AUTOSAVE Command | SET BELL Command |
| SET BLINK Command | SET BORDER Command | SET BRSTATUS Command |
| SET CARRY Command | SET CLASSLIB Command | SET CLEAR Command |
| SET CLOCK Command | SET COLOR OF Command | SET COLOR OF SCHEME Command |
| SET COLOR SET Command | SET COLOR TO Command | SET Command |
| SET COMPATIBLE Command | SET CONFIRM Command | SET CONSOLE Command |
| SET CPCOMPILE | SET CPDIALOG | SET CURRENCY Command |
| SET CURSOR Command | SET DATASESSION Command | SET DATE Command |
| SET DATE Command | SET DEBUG Command | SET DECIMALS Command |
| SET DELIMITERS Command | SET DEVELOPMENT Command | SET DEVICE Command |
| SET DISPLAY Command | SET DOHISTORY Command | SET ECHO Command |
| SET ESCAPE Command | SET FORMAT Command | SET FUNCTION Command |
| SET HEADINGS Command | SET HELP Command | SET HELPFILTER Command |
| SET INTENSITY Command | SET KEY Command | SET KEYCOMP Command |
| SET LOGERRORS Command | SET MACDESKTOP Command | SET MACHELP Command |
| SET MACKEY Command | SET MARGIN Command | SET MARK OF Command |
| SET MARK TO Command | SET MEMOWIDTH Command | SET MESSAGE Command |
| SET MOUSE Command | SET ODOMETER Command | SET OLEOBJECT Command |
| SET PALETTE Command | SET PDSETUP Command | SET POINT Command |
| SET PRINTER Command | SET READBORDER Command | SET REFRESH Command |
| SET RESOURCE Command | SET SAFETY Command | SET SCOREBOARD Command |
| SET SECONDS Command | SET SEPARATOR Command | SET SHADOWS Command |
| SET SKIP OF Command | SET SPACE Command | SET STATUS BAR Command |
| SET STATUS Command | SET STEP Command | SET STICKY Command |
| SET SYSFORMATS Command | SET SYSMENU Command | SET TALK Command |
| SET TEXTMERGE Command | SET TEXTMERGE DELIMITERS Command | SET TOPIC Command |
| SET TOPIC ID Command | SET TRBETWEEN Command | SET TYPEAHEAD Command |
| SET VIEW Command | SET WINDOW OF MEMO Command | SET XCMDFILE Command |
| SHOW GET Command | SHOW GETS Command | SHOW MENU Command |
| SHOW OBJECT Command | SHOW POPUP Command | SHOW WINDOW Command |
| SIZE POPUP Command | SIZE WINDOW Command | SKPBAR( ) Function |
| SKPPAD( ) Function | SOUNDEX( ) Function | SQL functions |
| SROWS( ) Function | STRTOFILE( ) function | SUSPEND Command |
| SYSMETRIC( ) Function | | |

# T

| _TABS System Memory Variable | _THROTTLE System Memory Variable | _TRANSPORT System Memory Variable |
| --- | --- | --- |
| TEXT ... ENDTEXT Command | TRANSFORM( ) Function | TXTWIDTH( ) Function |
| TYPE Command | | |

# U

| UPDATED( ) Function |
| --- |

# V

| VALIDATE DATABASE Command | VARREAD( ) Function |
| --- | --- |

# W

| _WINDOWS System Memory Variable | _WIZARD System Memory Variable | _WRAP System Memory Variable |
| --- | --- | --- |
| WAIT Command | WBORDER( ) Function | WCHILD( ) Function |
| WCOLS( ) Function | WEXIST( ) Function | WFONT( ) Function |
| WITH ... ENDWITH Command | WLAST( ) Function | WLCOL( ) Function |
| WLROW( ) Function | WMAXIMUM( ) Function | WMINIMUM( ) Function |
| WONTOP( ) Function | WOUTPUT( ) Function | WPARENT( ) Function |
| WREAD( ) Function | WROWS( ) Function | WTITLE( ) Function |
| WVISIBLE( ) Function | | |

# X

# Z

| ZOOM WINDOW Command |
| --- |
