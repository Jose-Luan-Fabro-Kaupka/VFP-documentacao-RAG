# Instruções IF

Você pode comparar como as instruções IF diferem entre o Visual FoxPro e outras linguagens de programação. A cláusula THEN é permitida apenas na instrução IF no Visual FoxPro.

| Visual FoxPro | BASIC |
| --- | --- |
| IF nCnt < nMax nTot = nTot * nCnt nCnt = nCnt + 1 ENDIF | If nCnt < nMax Then nTot = nTot * nCnt nCnt = nCnt + 1 End If |

| Pascal | C/C++ |
| --- | --- |
| if nCnt < nMax then begin nTot:=nTot * nCnt; nCnt:=nCnt + 1; end | if(nCnt < nMax) { nTot *= nCnt; nCnt++; } |
