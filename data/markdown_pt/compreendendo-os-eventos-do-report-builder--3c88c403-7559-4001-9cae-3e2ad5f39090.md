# Compreendendo os eventos do Report Builder

Os designers Report e Label do Visual FoxPro expõem operações selecionadas de interface do usuário (UI) como eventos de builder que podem ser interceptados e tratados por um aplicativo report builder.

O aplicativo builder invocado pelo designer é especificado pela variável de sistema _REPORTBUILDER, which by default references reportbuilder.app, located in the Visual FoxPro install directory. This application is invoked both from the Report Designer and the Label Designer - there is no corresponding "_LABELBUILDER" variable. In this topic and the ones that follow, you may assume that any discussion involving the Report Designer applies equally to the Label Designer.

The report builder application has the opportunity to augment or replace the native designer dialog boxes, and the entire underlying source file of the layout currently open in the Report Designer is available to the report builder as a cursor in a private data session.

If _REPORTBUILDER is empty or refers to a non-existent file, no error is raised. The designers will respond to user actions normally, as in previous versions of Visual FoxPro.

Quando ocorre um evento do report builder, o Report Designer faz o seguinte:
 - Creates a private data session.
- Opens a copy of the source (.frx or lbx) file currently being edited in the designer, with the alias "FRX."
- Invokes the application specified by _REPORTBUILDER, passing it four parameters.

Um aplicativo report builder deve obedecer à seguinte API:
 - It must accept at least four parameters (passed by reference) in the main program.
- It must return a value to the Report Designer by changing the value of the first parameter.
- It must be modal, because the designer will be waiting for the return value to indicate what action it should take next.

# Parâmetros passados pelo Designer

The Designer passes four parameters, by reference, to the builder application:

| Index | Parameter | DataType | Descrição |
| --- | --- | --- | --- |
| 1 | ReturnFlags | I | Passed by reference so that the builder application can return values to the Report or Label Designer. |
| 2 | EventType | I | An integer representing the type of event that occurred. |
| 3 | CommandClauses | O | An object (of Empty class) with properties indicating what clauses were used on the command that launched the designer. |
| 4 | DesignerSessionId | I | The DataSession Id that the Report Designer is in. |

### ReturnFlags

This passed-by-reference parameter is -1 when passed to the report builder, but the designer expects to receive a different value back. Possible return values consist of summed binary flags:

| #define constant | Bit number | Bits | Value | Descrição |
| --- | --- | --- | --- | --- |
| FRX_REPBLDR_HANDLE_EVENT | 0 | 01 | 1 | If set, this flag tells the Report Designer that the event has been handled by the report builder, and to suppress the default action the designer would normally do in response to the event. This flag is similar to the operation of NODEFAULT in Visual FoxPro method code. |
| FRX_REPBLDR_RELOAD_CHANGES | 1 | 10 | 2 | If set, this flag tells the Report Designer that the builder made changes to the FRX cursor, and that the changes should be reloaded into the designer, and reflected in the layout. |

> **Observação:** The #define constants shown in the tables are defined in foxpro_reporting.h in the FFC\ directory under the Visual FoxPro home directory.

### EventType

This parameter is an enumerated type, representing the event that caused the Report Designer to invoke the report builder application.

| #define constant | Value | Event Descrição |
| --- | --- | --- |
| FRX_BLDR_EVENT_PROPERTIES | 1 | A Properties dialog box is being invoked, by double-clicking or a menu action. |
| FRX_BLDR_EVENT_OBJECTCREATE | 2 | A control is being created in the layout. |
| n/a | 3 | (Reserved for future use.) |
| FRX_BLDR_EVENT_OBJECTREMOVE | 4 | A control is being removed from the layout by deletion or by CTRL-X/Cut. |
| FRX_BLDR_EVENT_OBJECTPASTE | 5 | A control is being pasted into the layout from the clipboard. |
| FRX_BLDR_EVENT_REPORTSAVE | 6 | The layout is being saved to disk. |
| FRX_BLDR_EVENT_REPORTOPEN | 7 | The layout is being opened. |
| FRX_BLDR_EVENT_REPORTCLOSE | 8 | The layout is being closed. |
| FRX_BLDR_EVENT_DATAENV | 9 | The Data Environment window is being opened. |
| FRX_BLDR_EVENT_PREVIEWMODE | 10 | The print preview mode is being invoked. |
| FRX_BLDR_EVENT_OPTIONALBANDS | 11 | The Optional Bands dialog box is being invoked. |
| FRX_BLDR_EVENT_DATAGROUPING | 12 | The Data Grouping dialog box is being invoked. |
| FRX_BLDR_EVENT_VARIABLES | 13 | The Variables dialog box is being invoked. |
| FRX_BLDR_EVENT_EDITINPLACE | 14 | CTRL-E was pressed on a selected Label control. |
| FRX_BLDR_EVENT_SETGRIDSCALE | 15 | The Set grid scale dialog box is being invoked. |
| FRX_BLDR_EVENT_OBJECTDROP | 16 | Object(s) are being created from a drag-and-drop operation from the Data Environment window, a Database Container, or a Project window. |
| FRX_BLDR_EVENT_IMPORTDE | 17 | Import data environment was selected from the Report menu. |
| FRX_BLDR_EVENT_PRINT | 18 | Print was selected from the File menu or Run Report was selected from the designer's context menu. |
| FRX_BLDR_EVENT_QUICKREPORT | 19 | Quick Report was selected from the Report menu. |

### CommandClauses

This parameter is an object reference to an instance of an Empty class with a number of additional properties indicating the various possible clauses on the Visual FoxPro command that launched the Report or Label Designer:

| Property | Data Type | Descrição |
| --- | --- | --- |
| AddTableToDE | L | Indicates that the Add table to data environment check box is selected in the Quick Report dialog box. |
| Alias | L | Indicates that the ALIAS keyword was specified in the CREATE REPORT | LABEL FROM.. command, or that Add alias was checked in the Quick Report dialog box. |
| FieldList | O | Contains a collection of numeric field numbers, representing the field list of the quick report command. |
| File | C | Contains the filename of the source (.frx or .lbx) file open in the Designer. This file may not actually exist if CREATE REPORT was used. |
| Form | L | Indicates the layout of the quick report: .T. if FORM layout was specified. .F. if COLUMN layout was specified. |
| From | C | Contains the table name specified in the CREATE REPORT FROM < filename > clause. |
| InScreen | L | Indicates that the IN SCREEN clause was used in the command. |
| InWindow | C | Especifica the window name of the IN < windowname > clause, if used. |
| IsCreate | L | Indicates the layout is newly created: .T. if CREATE REPORT | LABEL. .F. if MODIFY REPORT | LABEL. |
| IsReport | L | Indicates the type of layout open in the Designer: .T. if CREATE | MODIFY REPORT. .F. if CREATE | MODIFY LABEL. |
| IsQuickReportFromMenu | L | Indicates that the Quick Report option on the Report menu was invoked. |
| NoEnvironment | L | Especifica that the NOENVIRONMENT keyword was included in the command. |
| NoOverwrite | L | Especifica that the NOOVERWRITE keyword was included in the command. |
| NoWait | L | Especifica that the NOWAIT keyword was included in the command. |
| Protected | L | Especifica that the PROTECTED keyword was included in the command. |
| Save | L | Especifica that the SAVE keyword was included in the command. |
| Titles | L | Indicates that label controls should be added to the quick report layout. |
| Width | N | Especifica the number of columns specified on the quick report command. |
| Window | C | Contains the window name specified in the WINDOW < windowname > clause of the command. |

### DesignerSessionId

Because the report builder is invoked from inside a private data session, the Report or Label Designer also passes in the data session id of the data session that the designer is open in. This allows the report builder to switch to the designer's data session whenever it needs to access tables that might be open in the layout's data environment.

# O cursor FRX

A working copy of the report file being edited will be open with the alias "FRX" in a private data session when the report builder application is called. Additionally:
 - The record pointer will be located on the FRX record that represents the report layout object on which the event occurred. In some cases this might be the report header record itself, representing a report-specific event rather than a control-specific event.
- Any records in the FRX cursor representing layout objects that are currently selected (highlighted with the mouse and showing object "handles") will have the CURPOS field set to .T..

> **Observação:** The report header (record 1) may also have CURPOS=.T. because that is used to store the value of "Show Position" from the View menu option. If the builder application is required to identify how many objects are currently selected, it should use code similar to COUNT FOR CURPOS AND RECNO() > 1 .
