SelectedFile := A_ScriptDir . "\proxy.txt"


if SelectedFile = ""
    MsgBox "The dialog was canceled."
else
    MsgBox "The following file was selected:`n" SelectedFile

oText := Array()
try{
    Loop read, SelectedFile{
	oText.Push A_LoopReadLine
	} 
}
catch as Err
{
    MsgBox "Can't open '" SelectedFile "' for writing." . "`n`n" Type(Err) ": " Err.Message
    return
}

i := 1
sleep(100)




	!1::{
		if i >= oText.Length{
			MsgBox "all links were emptied"	
			return
		}
		temp := ClipboardAll()
 		A_Clipboard := oText[i]
		Send "^v"
		sleep 100
		A_Clipboard := temp
		global i += 1
	}

