# Getting Started Guide
## Setting Up Virtual Environment (Windows 64-bit based)

### Download and Install the following Tools (64-bit where applicable):
* [VirtualBox](https://www.virtualbox.org/)
* [Ubuntu](https://ubuntu.com/download/desktop)
*	[VSCode](https://code.visualstudio.com/)
*	[git](https://git-scm.com/)

## Installing VirtualBox
1.	Open VirtualBox and click on **New**
2.	Give a name for your virtual machine
3.  Select **Linux** and **Ubuntu (64-bit)** under Type and Version respectively
3.	Follow the instructions and select
   + Hard Disk: **Create a virtual hard disk now**
   + Hard disk file type: **VDI**
   + Storage on physical hard disk: **Dynamically allocated** *(if you have limited space Fixed size should be selected. Seek further help from TA or instructor with Fixed size, this documentation will not cover it).*
4.	File location and size: Based in class, I believe the instructor has chosen **10GB** but base your RAM, CPU, and file size using the specs of your computer

Video File (if you would prefer visual format): https://www.youtube.com/watch?v=QbmRXJJKsvs

## Setting up Ubuntu in VirtualBox
1.	Select your Virtual Machine (VM) and Click **Start**
2.	Under Select Start-up disk, select the Ubuntu image file downloaded earlier *(by default located in My Downloads folder on your PC).*
3.	Hit Start and allow time for the image file to be layered on top of VirtualBox
4.	Once Ubuntu image has loaded, click **Install Ubuntu** *(it will take time to install)*
5.	Once installation complete, there will be a prompt to restart your VM
6. You’ll receive a message saying **“Please remove installation medium, then reboot”** on the loading screen. Close the VM window and restart VM from VirtualBox (Use https://youtu.be/QbmRXJJKsvs?t=607 for step by step instructions if you are having issues)
7.	Under Devices > Shared Clipboard **and** Devices > Drag and Drop select **Bidirectional** 
8.	Select Devices > **Insert Guest Additions CD image…** *(If you get an error message follow this tutorial: https://www.youtube.com/watch?v=RxmGFsaOyks)*
8.	Close your VM. Select your VM in VirtualBox and Select **Settings**
9.	Go to **Network > Advanced** and click on **Port Forwarding**
10. Click on **Add** symbol (Plus sign) and fill in the following:
   +	Host Port: 3333
   +	Guest Port: 22
11. Restart Your VM and login to Ubuntu
12. Select the Terminal application and update and upgrade Ubuntu using the following:
  
  `sudo apt-get update`
**and**
  `sudo apt-get upgrade`
  
13. To install ssh server and git in the ubuntu environment, type the following in the terminal:

`sudo apt-get install -y openssh-server`
**and**
`sudo apt-get install git -y`

14. For TLDR `sudo apt-get install tldr -y`

## Setting up Remote Development between local and remote computer (Tools: cmd, Ubuntu Terminal)
1.	In remote terminal (Ubuntu) enter:
`ssh-keygen` and **Hit enter 3 times**
`ssh-copy-id yourusername@127.0.0.1`
Enter 'yes' and enter password when prompted
2.	Open the **id_rsa** file *(default it would be a MS Publisher file)* with notepad or text based editor located in C:\Users\*yourusername*\.ssh\ and copy all the text
3.	In remote (Ubuntu) terminal enter `vi ~/.ssh/authorized_keys`
4.	Paste the key copied from Notepad and type in `:wq` to exit
5.	Your connection is complete! You can type the following in your cmd to connect:
`ssh ubuntuusername@127.0.0.1 -p 3333`
Enter password when prompted

## Setting up Remote Development using VSCode (Tools: VSCode, Ubuntu Terminal)
1.	Install **‘Remote Development’** extension in VSCode
2.	Select the Remote Development icon *(computer monitor with <>)*
3.	Under Remote Explorer, select **SSH Targets** in dropdown menu
4.	Select **Settings** *(gear icon)*
5.	Select **C:\Users\(yourusername)\ssh\config**
6.	Make sure the config file has the following:
  + Host remote-virtual *(user-defined, can be anything you want)*
  + HostName 127.0.0.1
  + User yourusername *(your Ubuntu username)*
  + Port 3333
7.	Save and right click on ‘remote-virtual’ and select any of the options and enter password. And you're connected!






