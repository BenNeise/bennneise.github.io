---
layout: post
title: Using an Ubuntu CrashPlan appliance to backup a NAS
image: "/content/images/2016/01/download.png"
date: '2014-07-24 09:59:37'
---

I've recently upgraded some of my home setup; instead of [Windows Home Server 2011](http://windows.microsoft.com/en-gb/windows/windows-home-server) managing everything, I'm now using a [NetGear ReadyNAS 104](http://www.netgear.co.uk/home/products/connected-storage/RN10400.aspx#tab-techspecs), to serve files and using Windows Server 2012 R2 for the other functions.

Moving my files to the Network Attached Storage (NAS) fixed some of my issues (NFS performs better for serving media to XMBC), but it left me with a small problem: I previously used [CrashPlan ](http://www.code42.com/crashplan/)for backing up files from the Windows Home Server's local disks. However, (on Windows), CrashPlan [doesn't support backing up NAS](http://support.code42.com/CrashPlan/Latest/Backup/Mounting_Networked_Storage_Or_NAS_Devices_For_Backup). While there are a [couple of workarounds](https://helpdesk.crashplan.com/entries/24338-Ability-to-backup-network-shares-Network-Attached-Storage-), they are a little ... inelegant.

I decided that the best solution would be to use an Ubuntu agent, running as a Hyper-V machine on the server to back-up the NAS. This headless appliance could be managed by the CrashPlan client running on a separate machine. The bulk of the work was already detailed in Bryan Ross's articles [Installing CrashPlan on a headless Linux Server](http://www.liquidstate.net/how-to-manage-your-crashplan-server-remotely/) and [How to Manage Your CrashPlan Server Remotely](http://www.liquidstate.net/blog/technology/how-to-manage-your-crashplan-server-remotely/), but I thought it'd be worth adding some specifics

1. Download [Ubuntu server](http://www.ubuntu.com/download/server) and install on your platform of choice. I used Hyper-V and pretty much accepted all the defaults.
2. Once the Ubuntu installation process has completed, log in and install NFS services sudo apt-get install nfs-common
3. Install CrashPlan as per Bryan's instructions [here](http://www.liquidstate.net/blog/technology/installing-crashplan-on-a-headless-linux-server/).
4. On your Linux server, open CrashPlan's configuration file with `sudo nano -w /usr/local/crashplan/conf/my.service.xml`
5. Search for the **serviceHost** parameter and change it from `127.0.0.1` to `0.0.0.0`. This allows CrashPlan to accept commands from machines other than the local host.
6. Save the file and then restart the CrashPlan daemon with `sudo /etc/init.d/crashplan restart`
7. Install the CrashPlan client on the machine you're going to use to manage it.
8. Open the client configuration file. On Windows, the default location would be `C:\Program Files\CrashPlan\conf\ui.properties`. Look for the following line: `#serviceHost=127.0.0.1`
9. Remove the comment character (#) and change the IP address to that of your of your Ubuntu server. For example: `serviceHost=192.168.1.29`
10. On the server, create the folders where you're going to mount the NFS shares and manually mount them to make sure they work. You'll need to know the IP address to that of your NAS, and the path to the share(s). mkdir -p /mnt/nfs/videos sudo mount 192.168.0.13:/data/Videos /mnt/nfs/videos mkdir -p /mnt/nfs/pictures sudo mount 192.168.0.13:/data/Pictures /mnt/nfs/pictures mkdir -p /mnt/nfs/software sudo mount 192.168.0.13:/data/Software /mnt/nfs/software mkdir -p /mnt/nfs/ebooks sudo mount 192.168.0.13:/data/eBooks /mnt/nfs/ebooks
11. Now we need to make sure that when the server is restarted, it will automatically re-mount these shares. Edit **fstab** with the following command:- `sudo nano -w /etc/fstab`
12. Add a line for each share you wish to mount, like this 

```
192.168.0.13:/data/Videos /mnt/nfs/videos nfs auto 0 0
192.168.0.13:/data/Pictures /mnt/nfs/pictures nfs auto 0 0
192.168.0.13:/data/Software /mnt/nfs/software nfs auto 0 0
192.168.0.13:/data/eBooks /mnt/nfs/ebooks nfs auto 0 0
```
13. Reboot the server and ensure that the NFS shares map correctly (you can see existing mounts by running the command **mount**)
14. Now, on the client machine, open the CrashPlan GUI, and select the mount points which you wish to be backed-up.

This is now working well  - although the change in method means that I need to send all of my data up to CrashPlan again, I was hoping that it'd be able to map the previously uploaded files to the same files on their new paths.


