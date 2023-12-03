'这是一个关于ping某个网段的程序
strSubNet = "192.168.11.1"   '定义一个网段
Set objFSO= CreateObject("Scripting.FileSystemObject")   '创建objFOS文件对象

blnResult = Ping(strSubNet)  '调用自定义Ping函数来试试上面的IP的机器是否开机,返回一个布尔值,前提是对方机器没有防火墙等限制.
    If blnResult = True Then      '如果通则把结果写入文件对象流中.
            'objTS.WriteLine "Ping " & strComputer & " success!"

            set WshShell = WScript.CreateObject("WScript.Shell")
            WshShell.run("telnet 192.168.11.1")
            WScript.Sleep 2000
            '切换英文输入法
            'WshShell.SendKeys "+"
            WshShell.SendKeys"root"
            WshShell.SendKeys("{ENTER}")
            WScript.Sleep 1000
            WshShell.SendKeys"link4all123456"
            WshShell.SendKeys("{ENTER}")
            'WScript.Sleep 5000
            'WshShell.SendKeys"root"
            'WshShell.SendKeys("{ENTER}")
            'WScript.Sleep 1000
            'WshShell.SendKeys"link4all123456"
            'WshShell.SendKeys("{ENTER}")


            WshShell.SendKeys "cd /tmp/"
            WshShell.SendKeys("{ENTER}")
            WshShell.SendKeys "wget 192.168.11.100/9531/9531_test.sh -O test1.sh"
            WshShell.SendKeys("{ENTER}")
            WScript.Sleep 1000
            WshShell.SendKeys "chmod +x /tmp/test1.sh"
            WshShell.SendKeys("{ENTER}")
            WshShell.SendKeys ". /tmp/test1.sh"
            WshShell.SendKeys("{ENTER}")

            '开始测试
            WshShell.SendKeys "test_start"
            WshShell.SendKeys("{ENTER}")
            WScript.Sleep 1000

 Else
            wScript.Echo "Network is unconnect!"   '提示任务完成
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



