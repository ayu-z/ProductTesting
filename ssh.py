import sys
import select
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
from PyQt5.QtGui import QTextCursor
from ansi2html import Ansi2HTMLConverter
import paramiko

class SSHWindow(QWidget):
    # Set your default SSH connection parameters
    DEFAULT_HOST = "192.168.111.1"
    DEFAULT_PORT = 22
    DEFAULT_USERNAME = "root"
    DEFAULT_PASSWORD = "root"

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('SSH连接示例')

        # Create UI elements
        self.host_label = QLabel('主机:')
        self.host_edit = QLineEdit()
        self.host_edit.setText(self.DEFAULT_HOST)
        self.port_label = QLabel('端口:')
        self.port_edit = QLineEdit()
        self.port_edit.setText(str(self.DEFAULT_PORT))
        self.username_label = QLabel('用户名:')
        self.username_edit = QLineEdit()
        self.username_edit.setText(self.DEFAULT_USERNAME)
        self.password_label = QLabel('密码:')
        self.password_edit = QLineEdit()
        self.password_edit.setText(self.DEFAULT_PASSWORD)
        self.command_label = QLabel('命令:')
        self.command_edit = QLineEdit()
        self.output_label = QLabel('输出:')
        self.output_text = QTextBrowser()
        self.connect_button = QPushButton('连接并执行命令')
        self.connect_button.clicked.connect(self.connectAndExecute)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.host_label)
        layout.addWidget(self.host_edit)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_edit)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.command_label)
        layout.addWidget(self.command_edit)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

    def connectAndExecute(self):
        host = self.host_edit.text()
        port = int(self.port_edit.text())
        username = self.username_edit.text()
        password = self.password_edit.text()
        command = self.command_edit.text()

        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the remote host
            client.connect(host, port, username, password)

            # Execute the command
            stdin, stdout, stderr = client.exec_command(command, get_pty=True)

            # Get the command output's file descriptor
            channel = stdout.channel

            # Set non-blocking mode
            channel.setblocking(0)

            # Use select module to asynchronously get output
            while True:
                read_ready, _, _ = select.select([channel], [], [])
                if channel in read_ready:
                    # Read output
                    output = channel.recv(1024).decode('utf-8')
                    if not output:
                        break

                    # Get user and current path information
                    user_and_path = f"{username}@{client.get_transport().getpeername()[0]}:{client.get_transport().getpeername()[1]}"
                    prompt = f"{user_and_path}$ {command}\n"

                    # Convert ANSI escape codes to HTML
                    html_output = self.convert_ansi_to_html(prompt,output)

                    # Append HTML-formatted output to the QTextBrowser
                    self.output_text.append(html_output)
                    QApplication.processEvents()

            # Wait for the command to finish and get the exit status
            exit_status = channel.recv_exit_status()
            # self.output_text.append(f"Command exit status: {exit_status}")

        except Exception as e:
            # Handle connection and command execution exceptions
            self.output_text.append(f"Error occurred: {str(e)}")
        finally:
            # Close the SSH connection
            client.close()

    def convert_ansi_to_html(self, ansi_output, prompt):
        conv = Ansi2HTMLConverter()
        ansi = ansi_output + prompt
        html_output = conv.convert(ansi)
        return html_output

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SSHWindow()
    window.show()
    sys.exit(app.exec_())
