Set fso = CreateObject("Scripting.FileSystemObject")
set WshShell = WScript.CreateObject("WScript.Shell")
strUser = CreateObject("WScript.Network").UserName

fso.DeleteFile "C:\Users\"& strUser &"\.ssh\*"
set WshShell = WScript.CreateObject("WScript.Shell")

Dim name,msg
Dim tmp

test = createobject("Scripting.FileSystemObject").GetFolder(".").Path
tmp=test+"\default.txt"
set fs =createobject("scripting.filesystemobject")
set ts=fs.opentextfile(tmp,1,true)
tmp=ts.readline

msg="Please enter the device model as follow(default "& tmp &"):"&vbcrlf&"X4 Q31 M28 M28_xhf"
name=Inputbox(msg,"名称")

if name = "" Then
    name=tmp
End if

'Msgbox("1111111")
If name = "X4" Then  
     Msgbox("X4")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/X4/X4_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If      
End If

If name = "X5" Then  
     Msgbox("X5")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/X5/X5_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If      
End If

If name = "Q60" Then  
     Msgbox("Q60")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/Q60/Q60_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If      
End If

If name = "Q31" Then  
    Msgbox("Q31")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
         WScript.Sleep 1000

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/9531/9531_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If 
End If      

If name = "M28" Then  
    Msgbox("M28")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
         WScript.Sleep 1000
        WshShell.SendKeys"admin@cx2021"
        WshShell.SendKeys("{ENTER}")
         WScript.Sleep 1000

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/7628/7628_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If 
End If    

If name = "M28_xhf" Then  
    Msgbox("M28_xhf")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
         WScript.Sleep 1000
        WshShell.SendKeys"admin@cx2021"
        WshShell.SendKeys("{ENTER}")
         WScript.Sleep 1000

        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/xhf/test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If 
End If    

If name = "M21L2" Then  
    Msgbox("M21L2")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        
        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/7621/7621_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If 
End If 

If name = "M21L4" Then  
    Msgbox("M21L4")
    strSubNet = "192.168.11.1"   '定义一个网段
    blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
        WshShell.run("ssh root@192.168.11.1")
        WScript.Sleep 2000
        '切换英文输入法
        'WshShell.SendKeys "+"
        WshShell.SendKeys"yes"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        WshShell.SendKeys"link4all123456"
        WshShell.SendKeys("{ENTER}")
        WScript.Sleep 1000
        
        WshShell.SendKeys "cd /tmp/"
        WshShell.SendKeys("{ENTER}") 
        WshShell.SendKeys "wget 192.168.11.100/M21L4/M21L4_test.sh -O test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "chmod +x /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys ". /tmp/test1.sh"
        WshShell.SendKeys("{ENTER}")
        WshShell.SendKeys "test_start"
        WshShell.SendKeys("{ENTER}")
    Else
        Msgbox("No network")
    End If 
End If    







If name = "ping" Then  
    WshShell.run("ping 192.168.11.1 -t")
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

       