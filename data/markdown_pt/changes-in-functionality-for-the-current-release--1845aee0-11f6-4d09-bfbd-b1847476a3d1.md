# Changes in Functionality for the Current Release

Visual FoxPro includes functionality that differs from previous versions and might affect existing code. These behavior changes are organized according to the following categories:
 - Critical Changes Functionality changes most likely to affect existing code when running under this version of Visual FoxPro. It is extremely important that you read this section.
- Important Changes Functionality changes that might affect existing code when running under this version of Visual FoxPro.
- Miscellaneous Changes Functionality changes you should know about but are not likely to impact existing code.
- Removed Items Features or files that existed in prior versions of Visual FoxPro but are no longer included.

# Critical Changes

Critical behavior changes will most likely to affect existing code when running under this version of Visual FoxPro.

### SQL SELECT IN (Value_Set) Clause

In previous versions of Visual FoxPro, the IN (Value_Set) clause for the WHERE clause in the SQL SELECT command is mapped to INLIST( ) function. In the current release, Visual FoxPro might stop evaluating values and expressions in the Value_Set list when the first match is found. Therefore, if the IN clause is not Rushmore-optimized, you can improve performance by placing values most likely to match in the beginning of the Value_Set list. For more information, see the description for the IN clause in the SELECT - SQL Command topic and the INLIST( ) Function.

### Conversion of INLIST( ) Function in the Query Designer and View Designer

In previous versions of Visual FoxPro, the Query Designer and View Designer convert INLIST( ) function calls in the WHERE clause of the SQL SELECT command into IN (Value_Set) clauses. In the current release, this conversion no longer occurs due to the differences between INLIST( ) and the SQL IN clause. INLIST( ) remains restricted to 24 arguments. For more information, see the description for the IN clause in the SELECT - SQL Command topic and the INLIST( ) Function.

### Grids and RecordSource and ControlSource Properties

In Visual FoxPro 9.0 there is a change in Grid Control behavior. When the RecordSource Property for a Grid control is set, Visual FoxPro 9.0 resets all ControlSource Property to the empty string ("") for all columns. In earlier versions of Visual FoxPro, the ControlSource properties were not properly reset, so problems could occur when a RecordSource with a different structure was later bound. This change may impact scenarios involving Access and Assign methods or BINDEVENT( ) Function calls made against a Grid column's ControlSource property.

# Important Changes

Important changes might affect existing code when running under Visual FoxPro 9.0.

### Reporting

Visual FoxPro contains many improvements for reporting. The following are behavior changes that could impact existing reports:
 - The Report Designer and Engine now make use of extensible components. You can control or eliminate use of design-time extensions by altering the value of _REPORTBUILDER System Variable . You control run-time extension use with the SET REPORTBEHAVIOR Command .
- In Visual FoxPro 9's new object-assisted reporting mode, report fields may need to be adjusted (widened) slightly. This is especially important for numeric data where a field that is not wide enough to display the entire number will show it instead as asterisks ( ***** ). For more information about the changes to the Report System that required this change, and features of the GDI+ rendering engine and other changes related to it, see Using GDI+ in Reports . For migration strategy and recommendations, see Guide to Reporting Improvements .
- For a table of additional, minor rendering differences between backward-compatible reporting mode and object-assisted reporting mode, see the table below. Rendering feature Behavior in backward-compatible mode Behavior in object-assisted mode Recommendations Tab stops ( CHR(9) values included in report data) The width of a tab stop is determined by a number of characters in the font used. Tab stops are set at fixed-width positions, regardless of font. If you concatenated tabs with data in a stretching report layout element to create a table format within the element, you can often fulfill the same requirements using a second detail band in Visual FoxPro 9. Alternatively, change the number of tabs you concatenate with your data. Special characters and word-wrapping Non-breaking spaces are not respected; they are treated as normal space characters. Special characters such as non-breaking spaces ( CHR(160) ) and soft hyphens ( CHR(173) ) are correctly interpreted. As a result, words may wrap differently in output. Evaluate the results. In most cases, users will appreciate the change, because it more faithfully representing their original intentions in the text. If necessary, use the CHRTRAN( ) Function or STRTRAN( ) Function to replace these special characters with standard spaces and hyphens. Line spacing of multi-line objects Line spacing is determined by a formula that does not take font properties into consideration. Lines in a multi-line object are individually rendered, so background colors for each line may appear to have a different width. GDI+ line spacing is dynamically determined using font characteristics. A multi-line object is rendered as a single block of text. Evaluate the results. In most cases, the change in line spaces will provide a more polished appearance, and in all cases this method of handling multi-line text provides better performance. If a report depends on the old style of spacing lines, you can adjust the ReportListener's DynamicLineHeight Property to revert to the old behavior. Cursor images (.CUR files) .CUR files can be used as image sources in reports. .CUR files are not supported as image sources. Convert the cursor file to another, supported image format. Shape (Rounded Rectangle) curvature Limited choices for curvature. More choices are available through the Report Builder Application dialog box interface, but some will not look the same way in backward-compatible mode and object-assisted mode. If reports have to run in both backward-compatible mode and object-assisted mode, or if they are designed in version 9.0 but must run in earlier versions, limit your choices of values of shape curvature to those allowed in the native Round Rectangle Dialog Box . If you are using the Style Tab, Report Control Properties Dialog Box (Report Builder) to design such reports, use the values 12, 16, 24, 32, and 99, to represent the native buttons, selecting the buttons from left to right. The default value in the Round Rectangle dialog box (second button) is 16.
- When you create a Quick Report, by using the CREATE REPORT - Quick Report Command or by invoking the Quick Report… option on the Report menu, and if you have SET REPORTBEHAVIOR 90 , the layout elements created by the Report Designer are sized differently from ones created for the same fields in previous versions. This change handles the additional width required by the new rendering mechanism of the report engine.
- If you use the KEYBOARD Command or PLAY MACRO Command statements to address options on the Report menu, you may need to revise the keystrokes in these statements, as the menu has been reorganized.
- Reports may take longer to open in the Report Designer if the report was previously saved with the Printer Environment setting enabled. You can improve performance by unchecking the Printer Environment menu item from the Report menu and re-saving the report. The saved Printer Environment is not critical for functioning of a report and is typically not recommended. Object-assisted report mode also respects different printers' resolution settings, so saving resolution information for one printer in your report may have adverse effects in an environment with printers that have different resolutions. A saved Printer Environment may also have more adverse affects on REPORT FORM or LABEL commands invoked with the TO FILE option than they did in previous versions, if the associated printer setup is not available in the environment at runtime. In Visual FoxPro 9, the global default for this setting in the Reports Tab, Options Dialog Box , and for reports created in executable applications (.exe files), has been changed to unchecked.
- Because of changes to the way Visual FoxPro 9 uses current printer settings to determine items such as print resolution and page height dynamically, a REPORT FORM or LABEL command will not run in object-assisted mode if there are no available printer setups in the environment or if the print spooler has been stopped. You will receive Error loading printer driver (Error 1958) . If you need to run reports in an environment with no printer information, perhaps creating custom types of output that do not require printers, you can supply Visual FoxPro with the minimal set of information it needs to run your report by supplying a page height and page width from the appropriate Report Listener methods. For more information, see GetPageHeight Method and GetPageWidth Method .
- By default, and by design, the Report Builder Application does not automatically show tables in the report's Data Environment when you build report expressions. To better protect end-user design sessions, only tables you have explicitly opened, not all tables from the DataEnvironment, are available in the Expression Builder. With this change, you have the opportunity to set up the design session's data exactly the way you want the end-user to see it, before you issue a MODIFY REPORT Command in your application. If you prefer the Report Designer's old behavior, you can change the Report Builder Application to emulate it. For more information, see How to: Replace the Report Builder's Expression Builder Dialog Box .
- The ASCII keyword on the REPORT FORM Command is documented as following the <filename> parameter of the TO FILE <filename> clause. In earlier versions of Visual FoxPro, you could safely use the incorrect and unsupported syntax TO FILE ASCII <filename> instead. This incorrect syntax triggers an error in Visual FoxPro 9. Note that the ASCII keyword has no effect on object-assisted mode output provided by the Report Engine, although a ReportListener Object can be written to implement it.
- The keyword NOCONSOLE has no default meaning in object-assisted reporting mode, because ReportListeners do not echo their rendering output to the current output window by default. However, a ReportListener can mimic backward-compatible mode in this respect, if desired. Refer to OutputPage Method for a complete example.
- To facilitate development of run-time reporting extensions, the Report Engine now allows normal debugging procedures during a report run. If your error handling routine assumes it is impossible for a report to be suspended, this assumption will now be challenged. Refer to Handling Errors During Report Runs for a detailed look at the associated changes, and some suggestions for strategy.
- REPORT FORM and LABEL commands are no longer automatically prohibited as user-interface-related commands in COM objects compiled into DLLs, when you run the commands in object-assisted mode. The restriction still applies to these commands when they are run in backward-compatible mode. (The topic Selecting Process Types explains why user-interface-related commands are prohibited in DLLs.) This change is not applicable to multi-threaded DLLs. A number of user-interface-related facilities also are not available in DLLs (whether single- or multi-threaded). For example, the TXTWIDTH( ) Function and TextWidth Method depend on a window handle to function, so they are not available in a DLL. The CREATE REPORT - Quick Report Command relies on the same facilities as TXTWIDTH() , and therefore is not available in a DLL. However, in many instances, creating custom output using a ReportListener does not require any user-interface activity, so a REPORT FORM or LABEL command can now be used productively in a DLL. Using the SYS(2335) - Unattended Server Mode function to trap for potential modal states, as well as the new SET TABLEPROMPT Command , is recommended. Refer to Server Design Considerations and Limitations for more information.
- Changes have occurred to the handling of group headers and footers in multi-column reports, when the columns flow from left to right ( label-style layout). The revised behavior is more useful and behaves consistently with the new detail header and footer bands as well. For a description of the change, see How to: Define Columns in Reports .
- In previous versions, the NOWAIT keyword on the REPORT FORM and LABEL commands was not significant when the commands were issued in the Command window rather than in a program. In Visual FoxPro 9's object-assisted mode, when previewing instructions are interpreted by the Report Preview Application, this keyword is significant no matter where you issue the command. The Report Preview Application uses the NOWAIT keyword, consistently, as an instruction to provide a modeless preview form. For more information about the Report Preview Application, see Extending Report Preview Functionality .
- Visual FoxPro 8 introduced the NOPAGEEJECT keyword on the REPORT FORM and LABEL commands, but applied the keyword only to printed output. In Visual FoxPro 9, NOPAGEEJECT has significance for all output targets, including PREVIEW . This keyword provides chained or continued report runs for multiple REPORT FORM and LABEL commands. To facilitate this behavior in preview mode, and to allow you to apply customization instructions to multiple previews, the Report Output Application caches a single ReportListener object instance for preview output, causing a change in behavior for multiple modeless report commands ( REPORT FORM … PREVIEW NOWAIT ). In the past, you used multiple REPORT FORM… PREVIEW NOWAIT statements in a sequence, your commands resulted in multiple report preview windows. In Visual FoxPro 9, when SET REPORTBEHAVIOR 90 , these commands will result in successive report previews being directed to a single report preview window. Tip You can easily invoke the old behavior by creating multiple ReportListener object references and associating one with each separate REPORT FORM or LABEL command, using the OBJECT keyword. For more information about using the OBJECT syntax, see REPORT FORM Command . For information about receiving multiple object references of the appropriate type from the Report Output Application, see Understanding the Report Output Application .
- In the process of reviewing and overhauling the native Report Engine, a number of outstanding issues regarding band and layout element positioning were addressed. For example, a field element marked to stretch and sized to take up more than one text line's height in the report layout might have inappropriately pushed its band's exit events to the next page in Visual FoxPro 8. In Visual FoxPro 9, the band's exit events occur on the same page. Additional revisions improve record-pointer-handling in footer bands, when bands stretch across pages. These changes are not specific to object-assisted output rendering. If you have relied on undocumented behavior providing exact band or layout control placement in a particular report, you should review that report's behavior in Visual FoxPro 9.

### Rushmore Optimization

When character values are indexed, all values are considered to be encoded using the table's code page. In previous versions of Visual FoxPro, when the current Visual FoxPro code page differed from a table's code page, any attempt to look for a character value within that table's index resulted in an implicit translation of the value from the current Visual FoxPro code page into the table's code page. This could cause SQL or other Rushmore optimizable commands to return or act upon incorrect records.

In Visual FoxPro 9 and later, by default, the optimization engine no longer uses existing character indexes for tables created with a non-current code page. Instead, Visual FoxPro builds temporary indexes to ensure correct results. This can result in a loss of optimization of SQL or other commands which were optimized in earlier VFP versions. To prevent this, ensure that the current Visual FoxPro code page returned by CPCURRENT( ) Function matches the table's code page returned by CPDBF( ) Function. This requires either changing the current Visual FoxPro code page, or changing the table's code page. For information on specifying the current Visual FoxPro code page, see Understanding Code Pages in Visual FoxPro. For information on specifying the code page for a table, see How to: Specify the Code Page of a .dbf File. If you cannot change either the Visual FoxPro codepage or the table codepage to match, you can force optimization to work as it did in Visual FoxPro 8 and prior versions using the SET ENGINEBEHAVIOR Command with either 80 or 70 as a parameter.

### SQL SELECT Statements
 - A SELECT - SQL Command containing DISTINCT and ORDER BY clauses in which the ORDER BY field is not in the SELECT field list will generate an error in Visual FoxPro 9.0 with SET ENGINEBEHAVIOR 90 (Error 1808: SQL: ORDER BY clause is invalid.). The following example shows this: SET ENGINEBEHAVIOR 90 CREATE CURSOR foo (f1 int, f2 int) SELECT DISTINCT f1 FROM foo ORDER BY f2 INTO CURSOR res
- A SELECT - SQL Command containing DISTINCT and HAVING clauses in which the HAVING field is not in the SELECT field list will now generate an error in Visual FoxPro 9.0 with SET ENGINEBEHAVIOR 90 (Error 1803: SQL: HAVING clause is invalid.). An error is reported because the HAVING field is not in projection and DISTINCT is used. The following example shows this: SET ENGINEBEHAVIOR 90 CREATE CURSOR foo (f1 int, f2 int) SELECT DISTINCT f1 FROM foo HAVING f2>1 INTO CURSOR res
- The number of UNION statements that can be used in a SELECT - SQL Command is no longer limited to 9. Parentheses are not completely supported with UNION statements and unlike previous versions may generate an error. If two or more SELECT statements are enclosed in parenthesis, an error is generated during compile (Error 2196: Only a single SQL SELECT statement can be enclosed in parentheses.). This behavior is not tied to any SET ENGINEBEHAVIOR Command level. The following example shows this error: SELECT * FROM Table1 ; UNION ; (SELECT * FROM Table2 ; UNION ; SELECT * FROM Table3) The following example compiles without an error: SELECT * FROM Table1 ; UNION ; (SELECT * FROM Table2) ; UNION ; (SELECT * FROM Table3)

For more information, see SET ENGINEBEHAVIOR Command.

### Disabling TABLEREVERT( ) Operations During TABLEUPDATE( ) Operations

For CursorAdapters, Visual FoxPro does not permit TABLEREVERT( ) operations during operations.

For more information, see TABLEREVERT( ) Function and TABLEUPDATE( ) Function.

### Index Key Truncation during Index Updates

An error (Error 2199) is now generated when index key truncation is about to occur, typically during index creation or modification. This can happen with use of a key that contains an expression involving a Memo field, whose length in not fixed, such as in the following example:

`INDEX ON charfld1 + memofld1 TAG mytag`

Similar issues can also occur with the SQL engine (such as during a SQL SELECT command or View creation) where it might fail to build a temporary index to optimize a join evaluation if it is unable to accurately determine the maximum size of the key.

For more information, see Error building key for index "name". (Error 2199).

### Memo Field Corruption

Visual FoxPro will now detect if a Memo field in a class library (.vcx) or form (.scx) is corrupt when you try to open up that file in the designer. If the file contains a corrupt Memo field, an Error 41 such as following will occur:

Memo file <path>\myclass.VCT is missing or is invalid.

Additionally, similar Memo errors may occur if you have a Visual FoxPro table open and try to access contents of a corrupt Memo. The following sample code shows how you can detect the Error 41 memo file corruption:

```foxpro
TRY
  USE myTable EXCLUSIVE NOUPDATE
  SCAN
    SCATTER MEMO MEMVAR
  ENDSCAN
CATCH TO loError
  IF loError.ErrorNo=41
    * handle error here
  ENDIF
ENDTRY
USE IN myTable
```

While it is possible that loss of data may occur, the following sample code may assist in repairing some or the entire file:

```foxpro
ON ERROR *
USE myclass.vcx
COPY TO myclass_bkup.vcx&&backup
COPY TO myclass2.vcx
USE
DELETE FILE myclass.vc*
RENAME myclass2.vcx TO myclass.vcx
RENAME myclass2.vct TO myclass.vct
COMPILE CLASSLIB myclass.vcx
ON ERROR
```

### Visual Form and Class Extended Property Support

Visual FoxPro 9 allows you to create custom properties in your visual class (SCX or VCX file) whose values can contain carriage returns and/or be of length greater than 255 characters. If you specify a property with a value like this through the Properties Window (i.e., the Zoom dialog box), Visual FoxPro will store it in a format such that you will no longer be able to edit that class in older versions of Visual FoxPro.

### Class Definitions

The ability to have a property assignment set to instantiated object is no longer supported in a class definition and will generate an error. The following example shows this.

```foxpro
LOCAL oCustom
oCustom = CREATEOBJECT('cusTest')
DEFINE CLASS cusTest AS CUSTOM
    oRef = CREATEOBJECT('myclass')
ENDDEFINE
DEFINE CLASS myclass AS CUSTOM
ENDDEFINE
```

You can instead assign a property to an instantiated object reference in the Init event of your class.

### Merge Modules for Redistributable Components

Visual FoxPro includes merge modules (MSM files) for use in redistributing shared components with your runtime applications. Merge modules are used by applications that can create Windows Installer based setups. For example, Visual FoxPro ships with merge modules that contain the Visual FoxPro runtime libraries as well as some common components including a number of ActiveX controls.

For Visual FoxPro 9, the VFP9RUNTIME.MSM merge module contains the runtime libraries that you will need for your custom redistributable application. The VFP9RUNTIME.MSM merge module also has dependencies on the merge modules containing the Microsoft VC 7.1 runtime library (MSVCR71.DLL) and the GDI+ graphics library (GDIPLUS.DLL). Because of these dependencies, if you select the VFP9RUNTIME.MSM merge module in a Windows Installer tool such as InstallShield, the other dependent merge modules will automatically be selected as well.

Note For Windows XP and higher operating systems, Visual FoxPro uses the GDI+ graphics library that is installed in your Windows System folder.

For Visual FoxPro 9, the merge module containing the VC runtime library no longer installs to the Windows System directory. Instead, this file is installed to your application's directory. This is done in compliance with recommended component versioning strategies for Windows operating systems. The GDI+ library is installed into the same directory as your Visual FoxPro runtime libraries and is only installed on operating systems later than Windows XP (XP already includes the GDI+ library in its Windows System directory).

Tip There may be circumstances where you will want to install the VC or GDI+ library to another location such as the Windows System directory. You can do this with your Windows Installer application (e.g., InstallShield) by first selecting the merge module before selecting the VFP9RUNTIME.MSM one. Once you have selected a merge module, you can change its installation path.

There are new merge modules for MSXML3 and MSXML4 XML parser components. The MSXML 3.0 component consists of the following merge modules:
 - MSXML 3.0 (msxml3_wim32.msm)
- Msxml3 Exception INF Merge Module (msxml3inf_wim32.msm)
- WebData std library (wdstddll_wim32.msm)

There are two MSXML 4.0 modules that should be included with any custom setup:
 - MSXML 4.0 (msxml4sxs32.msm)
- MSXML 4.0 (msxml4sys32.msm)

### MTDLL Memory Allocation

Visual FoxPro contains a new PROGCACHE configuration file setting which specifies the amount of memory Visual FoxPro allocates at startup for running programs (program cache). This setting also determines memory allocated per thread for Visual FoxPro MTDLL COM Servers. In prior versions, this setting was not configurable and memory was allocated as a fixed program cache of a little over 9MB (144 * 64K). The new PROGCACHE setting allows you to set the exact size of the program cache or specify that dynamic memory allocation be used.

Since MTDLL COM Servers can use up a great amount of memory if many threads are created, it is important that memory be allocated more efficiently for these scenarios. In Visual FoxPro 9, the new default setting for MTDLL COM Servers is -2 (dynamic memory allocation). For more information, see Special Terms for Configuration Files.

# Miscellaneous Changes

The following are miscellaneous changes that you should know about but are not likely to impact existing code.

### CursorAdapter Changes

In the current version of Visual FoxPro, the following behavior changes apply to the CursorAdapter object:
 - You can no longer call TABLEREVERT( ) Function while a TABLEUPDATE( ) Function operation is in progress.
- The ConversionFunc Property setting is now respected during ADODB.Recordset based updates.
- The target record is now kept current in the ADODB.Recordset during CursorAdapter.After… events.

### Grid SetFocus Supported for AllowCellSelection

You can now call a Grid control's SetFocus Method and have the Grid receive focus when the AllowCellSelection Property is set to False (.F.) and the grid contains no records.

### EXECSCRIPT Function

The EXECSCRIPT( ) Function now allows you to pass parameters by reference.

Additionally, Visual FoxPro 9.0 tightens syntax validation of calls made from concatenation of parameters. The following code, which worked in prior versions of Visual FoxPro, now properly causes an error because the CHR(13) character breaks the call into two lines whereas it is supposed to be part of the parameter for the EXECSCRIPT call.

```foxpro
  cRecPauseScript = "EXECSCRIPT('" + ;
    "?123" + CHR(13) + ;
    "?456" + ;
    "')"
  _VFP.DoCmd(cRecPauseScript)
```

To make a valid call that does not cause a syntax error, you can use the following code:

```foxpro
  cRecPauseScript = "EXECSCRIPT('?123'+CHR(13)+ '?456')"
  _VFP.DoCmd(cRecPauseScript)
```

### Listbox Control Click Event

In the current version of Visual FoxPro, the PageUp, PageDown, Home and End keyboard keys now cause a Listbox control's Click event to fire. In previous versions, these keys did not trigger the Click event to fire, unlike the arrow keys.

### PEMSTATUS( ) Function Returns False for Hidden Native Properties

In previous versions of Visual FoxPro, the PEMSTATUS( ) function returned True (.T.) for hidden native properties of Visual FoxPro base classes when specifying a value of 5 for nAttribute. In the current release, PEMSTATUS( ) returns False (.F.) for these hidden native properties. For more information, see PEMSTATUS( ) Function.

### Changes to Options Dialog Box
 - In the Options dialog box, the List display count option has been moved from the Editor tab to the View tab. For more information, see View Tab, Options Dialog Box .
- In previous versions of Visual FoxPro, you could output all the settings in the Options Dialog Box (Visual FoxPro) to the Command Window by pressing the SHIFT key when choosing the OK button to close the dialog. In the current release, these settings are now sent to the Debug Output Window . The Debug Output window must be opened in order for the settings to be directed there.

### FOXRUN.PIF

The FOXRUN.PIF file that is used by the RUN | ! Command is no longer installed in the Visual FoxPro root directory. If Visual FoxPro detects the presence of a FOXRUN.PIF file during a RUN command, it will use COMMAND.COM to execute the specified RUN command. This may not be the desired SHELL program to use for a particular operating system, especially newer ones like Windows XP in which CMD.EXE is preferable.

The current behavior for a RUN command without the existence of a FOXRUN.PIF file is that the RUN command will use the SHELL program specified by the operating system COMSPEC environment variable. With Windows XP, you can view and edit this variable by right-clicking your computer desktop's My Computer icon and selecting the Properties dialog box (Advanced tab).

The FOXRUN.PIF file is still available in the Tools directory if you need it for a particular reason.

For more information, see RUN | ! Command.

### SCATTER Command

The SCATTER command no longer allows for ambiguous use of both MEMVAR and NAME clauses in the same command. You can only include one of these clauses. In prior versions, the following code would not generate an error:

```foxpro
USE HOME()+"SAMPLES\Data\customer.dbf"
SCATTER MEMVAR NAME oCust
```

For more information, see SCATTER Command.

### SET DOHISTORY

The SET DOHISTORY command, which is included for backward compatibility, was updated to send output to the Debug Output Window instead of the Command Window as in prior versions.

### SCREEN ShowTips Property

The default value for _SCREEN ShowTips Property has been changed from False (.F.) to True (.T.). This change was made because new Memo and Field Tips support is now dependent on this setting.

### AllowCellSelection Does Not Permit Deleting Grid Rows When Set to False

When the AllowCellSelection Property is set to False (.F.) for a Grid control, you cannot select a row for deletion by clicking the deletion column. For more information, see AllowCellSelection Property.

### Northwind Database

The sample Northwind database has been updated. Five of the stored procedures now include calls to the SETRESULTSET( ) Function so that the Visual FoxPro OLE DB Provider will return a cursor when they are executed.

### Foundation Classes

The _ShellExecute class contained in the _Environ.vcx FFC class library has been updated to include an additional parameter in the ShellExecute method.

### Wizards and Builders

The Wizard/Builder selection dialog box now properly hides deleted entries in the Wizard and Builder registration tables.

### Specifying Western Language Script Values for GETFONT( ) Function

In versions prior to this release, passing `0` as the nFontCharSet value for GETFONT( ) opened the Font Picker dialog box and displayed the Script list as unavailable. You could not specify `0` (Western) as the language script value, and setting it to `1` (Default) sets nFontCharSet to the default font setting only, which is determined by the operating system.

In this release, passing `0` to GETFONT( ) opens the Font Picker dialog box with the Script list available and Western selected. The return value for GETFONT( ) also includes the return value for nFontCharSet.

# Removed Items

### HTML Help SDK

The HTML Help 1.3 SDK no longer ships with Visual FoxPro.

# See Also
- Guide to Reporting Improvements
- Data and XML Feature Enhancements
- SQL Language Improvements
- Class Enhancements
- Language Enhancements
