Set fso = CreateObject("Scripting.FileSystemObject")
set WshShell = WScript.CreateObject("WScript.Shell")
set cliet = WScript.CreateObject("WScript.Shell")
strUser = CreateObject("WScript.Network").UserName

fso.DeleteFile "C:\Users\"& strUser &"\.ssh\*"
set WshShell = WScript.CreateObject("WScript.Shell")



blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then  
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys "cat /etc/config/test"
        WshShell.SendKeys("{ENTER}")
        
        'WshShell.SendKeys "echo \"(sleep 5;. /etc/config/test.sh;test) &\" > /sbin/checkmodem.sh"
    Else
        Msgbox("No network")
    End If    


Function Ping(strComputer)
    Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
    Set colItems = objWMIService.ExecQuery("Select * From Win32_PingStatus Where Address='" & strComputer & "'")
    For Each objItem In colItems
        Select case objItem.StatusCode
                    Case 0
                          Ping = True
                    Case Else
                          Ping = False
         End select
         Exit For
    Next
End Function

       