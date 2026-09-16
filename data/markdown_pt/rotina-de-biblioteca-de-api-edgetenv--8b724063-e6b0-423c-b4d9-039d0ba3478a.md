# Rotina de biblioteca de API _EdGetEnv( )

_EdGetEnv( ) fornece as informações do ambiente do editor em *EDENV.

```foxpro
int _EdGetEnv(WHANDLE wh, *EDENV theEdEnv)
WHANDLE wh;            /* Handle of editing window. */
*EDENV theEdEnv;         /* Environment settings. */
```

# Observações

A estrutura de *EDENV está listada abaixo.

> **Observação:** Nos comentários abaixo, um (R) indica que este membro é somente leitura e não pode ser definido usando _EdSetEnv( ). Um (B) indica que este membro assume um de dois valores Booleanos: 1 (True) ou 0 (False).

```foxpro
typedef struct
{
   char            filename[MAXFILENAME];   // (R)
   EDPOS         length;         // # of bytes in text. (R)
   unsigned short   lenLimit;         // Max allowable length.
 0 = infinite.
   unsigned short   dirty,            // Has the file been changed?
 (R, B)
                  autoIndent,      // Auto indent? (B)
                  backup,         // Make backup files? (B)
                  addLineFeeds,   // Add line feeds when saving? (B)
                  autoCompile,      // Shall we auto compile this thing?
 (B)
                  addCtrlZ,         // Add end of file ctrl-z? (B)
                  savePrefs,      // Save edit preferences? (B)
                  dragAndDrop,   // Allow drag-and-drop. (B)
                  readOnly,         // 0 = not r/o, 1 = file is r/o,
                                 // 2 = file is r/w, opened r/o,
                                 // 3 = file is r/o, opened r/o. (R)
                  status,            // Display status bar? (B)
                  lockPrefs,         // Can update the preferences ? (B)
                  insertMode;      // (B)
   short            wrap;            // If < 0, new line at Return only.
   EDPOS         selStart;         // Selection start. (R)
   EDPOS         selEnd;         // Selection end. (R)
   EDPOS         selAnchor;      // Selection anchor point. (R)
   short            justMode;      // Justification (0 = left, 1 =
 right, 2 = center).
   short            tabWidth;      // TAB size in spaces.
   char            fontName[MAXFONTNAME];
   short            fontSize;
   short            fontStyle;      // 0 = plain, 1 = bold, 2 =
 italic, 3 = bold italic.
   short            kind;         // Kind of editor session (R);
                              // EDCOMMAND, EDPROGRAM, etc.
} EDENV;
```

1 é retornado se chamado em uma sessão Command ou Editor, caso contrário 0 é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre uma sessão de edição para um arquivo especificado por um parâmetro e exibe cada campo da estrutura EDENV para esse arquivo conforme retornado por _EdGetEnv( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDGETENV
= EDGETENV("x")
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(unsigned long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 6;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDENV EdEnv;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdGetEnv(wh, &EdEnv);
   _PutStr("\nfilename: ");    _PutStr(EdEnv.filename);
   _PutStr("\nlength: ");    putLong(EdEnv.length);
   _PutStr("\nlenLimit: ");    putLong(EdEnv.lenLimit);
   _PutStr("\ndirty: ");     putLong(EdEnv.dirty);
   _PutStr("\nautoIndent: ");  putLong(EdEnv.autoIndent);
   _PutStr("\nbackup: ");    putLong(EdEnv.backup);
   _PutStr("\naddLineFeeds: ");  putLong(EdEnv.addLineFeeds);
   _PutStr("\nautoCompile: ");   putLong(EdEnv.autoCompile);
   _PutStr("\naddCtrlZ: ");    putLong(EdEnv.addCtrlZ);
   _PutStr("\nsavePrefs: ");   putLong(EdEnv.savePrefs);
   _PutStr("\ndragAndDrop: ");   putLong(EdEnv.dragAndDrop);
   _PutStr("\nreadOnly: ");    putLong(EdEnv.readOnly);
   _PutStr("\nstatus: ");    putLong(EdEnv.status);
   _PutStr("\nlockPrefs: ");   putLong(EdEnv.lockPrefs);
   _PutStr("\ninsertMode: ");  putLong(EdEnv.insertMode);
   _PutStr("\nwrap: ");    putLong(EdEnv.wrap);
   _PutStr("\nselStart: ");    putLong(EdEnv.selStart);
   _PutStr("\nselEnd: ");    putLong(EdEnv.selEnd);
   _PutStr("\nselAnchor: ");   putLong(EdEnv.selAnchor);
   _PutStr("\njustMode: ");    putLong(EdEnv.justMode);
   _PutStr("\ntabWidth: ");    putLong(EdEnv.tabWidth);
   _PutStr("\nfontName: ");    _PutStr(EdEnv.fontName);
   _PutStr("\nfontSize: ");    putLong(EdEnv.fontSize);
   _PutStr("\nfontStyle: ");   putLong(EdEnv.fontStyle);
   _PutStr("\nkind: ");    putLong(EdEnv.kind);
}
FoxInfo myFoxInfo[] = {
   {"EDGETENV", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
