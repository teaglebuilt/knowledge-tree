---
title: Linux Cookbook Essential Skills for Linux Users and System Network Administrators
  (Carla Schroder)
source: books/pdf/Linux Cookbook Essential Skills for Linux Users and System  Network
  Administrators (Carla Schroder) (z-library.sk, 1lib.sk, z-lib.sk).pdf
source_type: book
source_hash: 3f5d777be44ffeb5e990fa6535ac180b01c365f5c98ce7b0376a68a28cb25c75
tags:
- linux
- book
extracted: '2026-10-04'
---

**SECOND EDITION**
## **Linux Cookbook**

**_Essential Skills for Linux Users and_**
**_System and Network Administrators_**

**_Carla Schroder_**

**Linux Cookbook**
by Carla Schroder

Copyright © 2021 Carla Schroder. All rights reserved.

Printed in the United States of America.

Published by O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.

O’Reilly books may be purchased for educational, business, or sales promotional use. Online editions are
also available for most titles ( _[http://oreilly.com](http://oreilly.com)_ ). For more information, contact our corporate/institutional
sales department: 800-998-9938 or _corporate@oreilly.com_ .

**Acquisitions Editor:** Suzanne McQuade
**Development Editor:** Jeff Bleiel
**Production Editor:** Daniel Elfanbaum
**Copyeditor:** Sonia Saruba
**Proofreader:** Tom Sullivan

December 2004: First Edition
September 2021: Second Edition

**Revision History for the Second Edition**
2021-08-12: First Release

**Indexer:** nSight, Inc.
**Interior Designer:** David Futato
**Cover Designer:** Karen Montgomery
**Illustrator:** Kate Dullea

See _[http://oreilly.com/catalog/errata.csp?isbn=9781492087168](http://oreilly.com/catalog/errata.csp?isbn=9781492087168)_ for release details.

The O’Reilly logo is a registered trademark of O’Reilly Media, Inc. _Linux Cookbook_, the cover image, and
related trade dress are trademarks of O’Reilly Media, Inc.

The views expressed in this work are those of the author, and do not represent the publisher’s views.
While the publisher and the author have used good faith efforts to ensure that the information and
instructions contained in this work are accurate, the publisher and the author disclaim all responsibility
for errors or omissions, including without limitation responsibility for damages resulting from the use of
or reliance on this work. Use of the information and instructions contained in this work is at your own
risk. If any code samples or other technology this work contains or describes is subject to open source
licenses or the intellectual property rights of others, it is your responsibility to ensure that your use
thereof complies with such licenses and/or rights.

978-1-492-08716-8

[LSI]

#### **Table of Contents**

**Preface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xiii**

**1.** **Installing Linux. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1**
Booting from Installation Media                                           2
Where to Download Linux                                                3
Best Linux for Newbies                                                   3
1.1 Entering your System BIOS/UEFI Setup                                 4
1.2 Downloading a Linux Installation Image                                 6
1.3 Creating a Linux Installation USB Stick with UNetbootin                  7
1.4 Creating a Linux Installation DVD with K3b                             9
1.5 Using the wodim Command to Create a Bootable CD/DVD               12
1.6 Creating a Linux Installation USB Stick with the dd Command            13
1.7 Trying a Simple Ubuntu Installation                                   15
1.8 Customizing Partitioning                                             18
1.9 Preserving Existing Partitions                                         22
1.10 Customizing Package Selection                                       23
1.11 Multibooting Linux Distributions                                     29
1.12 Dual-boot with Microsoft Windows                                   31
1.13 Recovering an OEM Windows 8 or 10 Product Key                     34
1.14 Mounting Your ISO Image on Linux                                  35

**2.** **Managing the GRUB Bootloader. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37**
2.1 Rebuilding Your GRUB Configuration File                              40
2.2 Unhiding a Hidden GRUB Menu                                      40
2.3 Booting to a Different Linux Kernel                                    41
2.4 Understanding GRUB Configuration Files                              43
2.5 Writing a Minimal GRUB Configuration File                            44
2.6 Setting a Custom Background for Your GRUB Menu                     48

**iii**

2.7 Changing Font Colors in the GRUB Menu                              49
2.8 Applying a Theme to Your GRUB Menu                                52
2.9 Rescuing a Nonbooting System from the grub> Prompt                  54
2.10 Rescuing a Nonbooting System from the grub rescue> Prompt           56
2.11 Reinstalling Your GRUB Configuration                                58

**3.** **Starting, Stopping, Restarting, and Putting Linux into Sleep Modes. . . . . . . . . . . . . . . 59**
3.1 Shutting Down with systemctl                                         60
3.2 Shutting Down, Timed Shutdowns, and Rebooting with the shutdown
Command                                                           61
3.3 Shutting Down and Rebooting with halt, reboot, and poweroff            63
3.4 Sending Your System into Sleep Modes with systemctl                    64
3.5 Rebooting Out of Trouble with Ctrl-Alt-Delete                          66
3.6 Disabling, Enabling, and Configuring Ctrl-Alt-Delete in the Linux
Console                                                             68
3.7 Creating Scheduled Shutdowns with cron                               69
3.8 Scheduling Automated Startups with UEFI Wake-Ups                    71
3.9 Scheduling Automated Startups with RTC Wake-ups                     73
3.10 Setting Up Remote Wake-Ups with Wake-on-LAN over Wired Ethernet   75
3.11 Setting Up Remote Wake-Ups over WiFi (WoWLAN)                   77

**4.** **Managing Services with systemd. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79**
4.1 Learning if Your Linux Uses systemd                                   82
4.2 Understanding PID 1, the Mother of All Processes                       84
4.3 Listing Services and Their States with systemctl                          86
4.4 Querying the Status of Selected Services                                89
4.5 Starting and Stopping Services                                        91
4.6 Enabling and Disabling Services                                       92
4.7 Stopping Troublesome Processes                                      94
4.8 Managing Runlevels with systemd                                     95
4.9 Diagnosing Slow Startups                                             98

**5.** **Managing Users and Groups. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99**
5.1 Finding a User’s UID and GID                                       101
5.2 Creating a Human User with useradd                                 103
5.3 Creating a System User with useradd                                  105
5.4 Changing the useradd Default Settings                                106
5.5 Customizing the Documents, Music, Video, Pictures, and Downloads
Directories                                                          108
5.6 Creating User and System Groups with groupadd                       110
5.7 Adding Users to Groups with usermod                                112
5.8 Creating Users with adduser on Ubuntu                               113

**iv** **|** **Table of Contents**

5.9 Creating a System User with adduser on Ubuntu                        114
5.10 Creating User and System Groups with addgroup                      115
5.11 Checking Password File Integrity                                    116
5.12 Disabling a User Account                                           117
5.13 Deleting a User with userdel                                        118
5.14 Deleting a User with deluser on Ubuntu                              119
5.15 Removing a Group with delgroup on Ubuntu                         120
5.16 Finding and Managing All Files for a User                            120
5.17 Using su to Be Root                                                122
5.18 Granting Limited Root Powers with sudo                             123
5.19 Extending the sudo Password Timeout                               126
5.20 Creating Individual sudoers Configurations                           127
5.21 Managing the Root User’s Password                                  127
5.22 Changing sudo to Not Ask for the Root Password                      128

**6.** **Managing Files and Directories. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131**
6.1 Creating Files and Directories                                        133
6.2 Quickly Creating a Batch of Files for Testing                           134
6.3 Working with Relative and Absolute Filepaths                          136
6.4 Deleting Files and Directories                                        137
6.5 Copying, Moving, and Renaming Files and Directories                  139
6.6 Setting File Permissions with chmod’s Octal Notation                   140
6.7 Setting Directory Permissions with chmod’s Octal Notation              142
6.8 Using the Special Modes for Special Use Cases                          143
6.9 Removing the Special Modes in Octal Notation                         146
6.10 Setting File Permissions with chmod’s Symbolic Notation               146
6.11 Setting the Special Modes with chmod’s Symbolic Notation             148
6.12 Setting Permissions in Batches with chmod                           150
6.13 Setting File and Directory Ownership with chown                     151
6.14 Changing Ownership on Batches of Files with chown                  152
6.15 Setting Default Permissions with umask                              153
6.16 Creating Shortcuts (Soft and Hard Links) to Files and Directories        154
6.17 Hiding Files and Directories                                        157

**7.** **Backup and Recovery with rsync and cp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159**
7.1 Selecting Which Files to Back Up                                     161
7.2 Selecting Files to Restore from Backups                               162
7.3 Using the Simplest Local Backup Method                              163
7.4 Automating Simple Local Backups                                    164
7.5 Using rsync for Local Backups                                        166
7.6 Making Secure Remote File Transfers with rsync over SSH               168
7.7 Automating rsync Transfers with cron and SSH                        170

**Table of Contents** **|** **v**

7.8 Excluding Files from Backup                                         170
7.9 Including Selected Files to Backup                                    172
7.10 Managing Includes with a Simple Include File                         173
7.11 Managing Includes and Excludes with an Exclude File                  174
7.12 Limiting rsync’s Bandwidth Use                                     176
7.13 Building an rsyncd Backup Server                                   177
7.14 Limiting Access to rsyncd Modules                                  180
7.15 Creating a Message of the Day for rsyncd                             182

**8.** **Managing Disk Partitioning with parted. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185**
Overview                                                             185
8.1 Unmounting Your Partitions Before Using parted                       190
8.2 Choosing the Command Mode for parted                             191
8.3 Viewing Your Existing Disks and Partitions                            192
8.4 Creating GPT Partitions on a Nonbooting Disk                         195
8.5 Creating Partitions for Installing Linux                                197
8.6 Removing Partitions                                                198
8.7 Recovering a Deleted Partition                                       199
8.8 Increasing Partition Size                                             200
8.9 Shrinking a Partition                                                202

**9.** **Managing Partitions and Filesystems with GParted. . . . . . . . . . . . . . . . . . . . . . . . . . . . 205**
9.1 Viewing Partitions, Filesystems, and Free Space                        207
9.2 Creating a New Partition Table                                       209
9.3 Deleting a Partition                                                 210
9.4 Creating a New Partition                                            211
9.5 Deleting a Filesystem Without Deleting the Partition                    213
9.6 Recovering a Deleted Partition                                       214
9.7 Resizing Partitions                                                  215
9.8 Moving a Partition                                                  216
9.9 Copying a Partition                                                 218
9.10 Managing Filesystems with GParted                                 220

**10.** **Getting Detailed Information About Your Computer Hardware. . . . . . . . . . . . . . . . . . . 223**
10.1 Collecting Hardware Information with lshw                          224
10.2 Filtering lshw Output                                              226
10.3 Detecting Hardware, Including Displays and RAID Devices, with hwinfo 227
10.4 Detecting PCI Hardware with lspci                                  228
10.5 Understanding lspci Output                                        230
10.6 Filtering lspci Output                                              231
10.7 Using lspci to Identify Kernel Modules                               234
10.8 Using lsusb to List USB Devices                                     235

**vi** **|** **Table of Contents**

10.9 Listing Partitions and Hard Disks with lsblk                           237
10.10 Getting CPU Information                                         238
10.11 Identifying Your Hardware Architecture                             240

**11.** **Creating and Managing Filesystems. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243**
Filesystem Overview                                                   244
11.1 Listing Supported Filesystems                                       246
11.2 Identifying Your Existing Filesystems                                248
11.3 Resizing Filesystems                                               249
11.4 Deleting Filesystems                                               250
11.5 Using a New Filesystem                                            251
11.6 Creating Automatic Filesystem Mounts                               253
11.7 Creating Ext4 Filesystems                                          256
11.8 Configuring the Ext4 Journal Mode                                  257
11.9 Finding Which Journal Your Ext4 Filesystem Is Attached To            259
11.10 Improving Performance with an External Journal for Ext4             260
11.11 Freeing Space from Reserved Blocks on Ext4 Filesystems              262
11.12 Creating a New XFS Filesystem                                     263
11.13 Resizing an XFS Filesystem                                        264
11.14 Creating an exFAT Filesystem                                      266
11.15 Creating FAT16 and FAT32 Filesystems                             267
11.16 Creating a Btrfs Filesystem                                        269

**12.** **Secure Remote Access with OpenSSH. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273**
12.1 Installing OpenSSH Server                                         275
12.2 Generating New Host Keys                                         276
12.3 Configuring Your OpenSSH Server                                  276
12.4 Checking Configuration Syntax                                     279
12.5 Setting Up Password Authentication                                 279
12.6 Retrieving a Key Fingerprint                                        281
12.7 Using Public Key Authentication                                    282
12.8 Managing Multiple Public Keys                                     284
12.9 Changing a Passphrase                                             285
12.10 Automatic Passphrase Management with Keychain                   286
12.11 Using Keychain to Make Passphrases Available to Cron                287
12.12 Tunneling an X Session Securely over SSH                           288
12.13 Opening an SSH Session and Running a Command in One Line        290
12.14 Mounting Entire Remote Filesystems with sshfs                      291
12.15 Customizing the Bash Prompt for SSH                              292
12.16 Listing Supported Encryption Algorithms                           294

**Table of Contents** **|** **vii**

**13.** **Secure Remote Access with OpenVPN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297**
OpenVPN Overview                                                   297
13.1 Installing OpenVPN, Server and Client                               299
13.2 Setting Up a Simple Connection Test                                 300
13.3 Setting Up Easy Encryption with Static Keys                          302
13.4 Installing EasyRSA to Manage Your PKI                              304
13.5 Creating a PKI                                                    306
13.6 Customizing EasyRSA Default Options                               311
13.7 Creating and Testing Server and Client Configurations                 312
13.8 Controlling OpenVPN with systemctl                                315
13.9 Distributing Client Configurations More Easily with .ovpn Files         316
13.10 Hardening Your OpenVPN Server                                  320
13.11 Configuring Networking                                          323

**14.** **Building a Linux Firewall with firewalld. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325**
firewalld Overview                                                     325
14.1 Querying Which Firewall Is Running                                328
14.2 Installing firewalld                                                 330
14.3 Finding Your firewalld Version                                      331
14.4 Configuring iptables or nftables as the firewalld Backend               332
14.5 Listing All Zones and All Services Managed by Each Zone              332
14.6 Listing and Querying Services                                       335
14.7 Selecting and Setting Zones                                         336
14.8 Changing the Default firewalld Zone                                 338
14.9 Customizing firewalld Zones                                        339
14.10 Creating a New Zone                                             340
14.11 Integrating NetworkManager and firewalld                          342
14.12 Allowing or Blocking Specific Ports                                 343
14.13 Blocking IP Addresses with Rich Rules                              345
14.14 Changing a Zone Default Target                                    346

**15.** **Printing on Linux. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347**
Overview                                                             347
15.1 Using the CUPS Web Interface                                      350
15.2 Installing a Locally Attached Printer                                 350
15.3 Giving Printers Useful Names                                       354
15.4 Installing a Network Printer                                        355
15.5 Using Driverless Printing                                           357
15.6 Sharing Nonnetworked Printers                                     359
15.7 Correcting the “Forbidden” Error Message                            360
15.8 Installing Printer Drivers                                           362
15.9 Modifying an Installed Printer                                      364

**viii** **|** **Table of Contents**

15.10 Saving Documents by Printing to a PDF File                         365
15.11 Troubleshooting                                                 366

**16.** **Managing Local Name Services with Dnsmasq and the hosts File. . . . . . . . . . . . . . . . . 367**
16.1 Simple Name Resolution with /etc/hosts                              368
16.2 Using /etc/hosts for Testing and Blocking Annoyances                 371
16.3 Finding All DNS and DHCP Servers on Your Network                 372
16.4 Installing Dnsmasq                                                374
16.5 Making systemd-resolved and NetworkManager Play Nice with
Dnsmasq                                                           375
16.6 Configuring Dnsmasq for LAN DNS                                 376
16.7 Configuring firewalld to Allow DNS and DHCP                       379
16.8 Testing Your Dnsmasq Server from a Client Machine                   380
16.9 Managing DHCP with Dnsmasq                                    381
16.10 Advertising Important Services over DHCP                          383
16.11 Creating DHCP Zones for Subnets                                 384
16.12 Assigning Static IP Addresses from DHCP                           385
16.13 Configuring DHCP Clients for Automatic DNS Entries                386
16.14 Managing Dnsmasq Logging                                       388
16.15 Configuring Wildcard Domains                                    389

**17.** **Keeping Time with ntpd, chrony, and timesyncd. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391**
17.1 Finding Which NTP Client Is on Your Linux System                   392
17.2 Using timesyncd for Simple Time Synchronization                     394
17.3 Setting Time Manually with timedatectl                              396
17.4 Using chrony for Your NTP Client                                   397
17.5 Using chrony as a LAN Time Server                                 398
17.6 Viewing chrony Statistics                                           400
17.7 Using ntpd for Your NTP Client                                     401
17.8 Using ntpd for Your NTP Server                                     403
17.9 Managing Time Zones with timedatectl                              404
17.10 Managing Time Zones Without timedatectl                          405

**18.** **Building an Internet Firewall/Router on Raspberry Pi. . . . . . . . . . . . . . . . . . . . . . . . . . . 407**
Overview                                                             407
18.1 Starting and Shutting Down Raspberry Pi                            410
18.2 Finding Hardware and How-Tos                                    411
18.3 Cooling the Raspberry Pi                                           413
18.4 Installing Raspberry Pi OS with Imager and dd                        413
18.5 Installing Raspberry Pi with NOOBS                                 415
18.6 Connecting to a Video Display Without HDMI                        417
18.7 Booting into Recovery Mode                                        420

**Table of Contents** **|** **ix**

18.8 Adding a Second Ethernet Interface                                  420
18.9 Setting Up an Internet Connection Sharing Firewall with firewalld       424
18.10 Running Your Raspberry Pi Headless                               427
18.11 Building a DNS/DHCP Server with Raspberry Pi                     428

**19.** **System Rescue and Recovery with SystemRescue. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 431**
19.1 Creating Your SystemRescue Bootable Device                         432
19.2 Getting Started with SystemRescue                                  432
19.3 Understanding SystemRescue’s Two Boot Screens                      434
19.4 Understanding SystemRescue’s Boot Options                          437
19.5 Identifying Filesystems                                             438
19.6 Resetting a Linux Root Password                                    439
19.7 Enabling SSH in SystemRescue                                      440
19.8 Copying Files over the Network with scp and sshfs                     442
19.9 Repairing GRUB from SystemRescue                                445
19.10 Resetting a Windows Password                                     446
19.11 Rescuing a Failing Hard Disk with GNU ddrescue                    448
19.12 Managing Partitions and Filesystems from SystemRescue              450
19.13 Creating a Data Partition on Your SystemRescue USB Drive            451
19.14 Preserving Changes in SystemRescue                               453

**20.** **Troubleshooting a Linux PC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 455**
Overview                                                             455
20.1 Finding Useful Information in Logfiles                               457
20.2 Configuring journald                                              461
20.3 Building a Logging Server with systemd                              462
20.4 Monitoring Temperatures, Fans, and Voltages with lm-sensors          465
20.5 Adding a Graphical Interface to lm-sensors                           467
20.6 Monitoring Hard Disk Health with smartmontools                    470
20.7 Configuring smartmontools to Send Email Reports                    473
20.8 Diagnosing a Sluggish System with top                               475
20.9 Viewing Selected Processes in top                                    477
20.10 Escaping from a Frozen Graphical Desktop                          478
20.11 Troubleshooting Hardware                                        479

**21.** **Troubleshooting Networks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481**
Diagnostic Hardware                                                  481
21.1 Testing Connectivity with ping                                      482
21.2 Profiling Your Network with fping and nmap                         484
21.3 Finding Duplicate IP Addresses with arping                           487
21.4 Testing HTTP Throughput and Latency with httping                   488
21.5 Using mtr to Find Troublesome Routers                              490

**x** **|** **Table of Contents**

**Appendix. Software Management Cheatsheets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493**

**Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501**

**Table of Contents** **|** **xi**

#### **Preface**

Way back in olden times I wrote the first edition of the _Linux Cookbook_, which was
released unto a joyous world in 2004. It sold well, I heard from many happy readers,
and some are still my friends.

For a Linux book, 17 years old is ancient. Linux was 14 years old in 2004, a wee baby
computer operating system. Even so, it was already a popular and widely used power‐
house, adapting to any role, from tiny embedded devices to mainframes and super‐
computers. The rapid growth of Linux is partly due to it being a free clone of Unix,
the most mature and powerful operating system of all. The other major factor in the
speedy growth and adoption of Linux is the absence of barriers. Anyone can down‐
load and try it, and the source code is freely available to anyone who wants to use and
contribute to it.

At the time it was a great example of form following function, like my first car. It ran,
it was reliable, but it wasn’t pretty, and it needed a lot of custom wiggling of this and
jiggling of that to keep going. Running a Linux system back then meant learning your
way around a hodgepodge of commands, scripts, and configuration files, and a fair
bit of wiggling and jiggling. Software management, storage management, networking,
audio, video, kernel management, process management…everything required a lot of
hands-on work and continual study.

Some 17 years later, every important subsystem in Linux has substantially changed
and improved. Now all those manual chores we had to do for basic administration
are replaced by what I call “It Just Works Subsystems.” Every aspect of running a
Linux system is many times easier, and we can focus on using Linux to do cool things
instead of having to wiggle and jiggle this and that just to keep it running.

I am delighted to present this greatly updated _Linux Cookbook_ second edition, and I
hope you enjoy learning about all of this cool new goodness.

**xiii**

**Who Should Read This Book**

This book is for people with some computer experience, though not necessarily Linux
experience. I’ve done my best to make it as accessible as possible for Linux beginners.
You should understand some basic networking concepts, such as IP addressing,
Ethernet, WiFi, client, and server. You should know basic computer hardware and
have some understanding of using the command line. If you need some help with
these, there are abundant resources for learning them; I did not want to get bogged
down in teaching material that is already well documented.

The recipes in this book are hands-on. My goal is for the reader to be successful on
the first try, though don’t feel badly if you are not. A general-purpose Linux computer
is an extremely complex machine, and there is a lot to learn. Be patient, take your
time, and read more than you want to. Chances are the answers you want are just a
few sentences away.

Every Linux has built-in documentation for commands called _man pages_ (short for
“manual pages”). For example, _man 1 ls_ documents the _ls_, or list directory contents,
command. Type these commands exactly as shown in the book to open the correct
man page. You can also find this information online.

**Why I Wrote This Book**

I have long wanted to write a book like this, that collects what I think are the most
necessary Linux skills in one book. Linux is everywhere, and no matter where you
find it, Linux is Linux, and the needed skills are the same. The tech world moves fast,
and I think you will find this book provides a solid foundation that you can build on,
no matter what direction your interests take you.

The cookbook format is especially good for teaching fundamentals because it shows
how to solve specific real-world problems and separates the wordy explanations from
the steps needed to accomplish a task.

**Navigating This Book**

This book is not a formal training course, where you start at the beginning and work
your way to the end. Instead, you can jump in anywhere and hopefully find what you
need.

**xiv** **|** **Preface**

It is roughly organized like this:

 - Chapters 1, 2, and 3 cover installing Linux, managing the bootloader, stopping
and starting, and answer the “Where do I get Linux and how do I make it go”
questions.

 - Chapter 4 provides an introduction to managing services with systemd, which is
a big improvement from the old way of having to learn all manner of scripts,
configuration files, and commands.

 - Chapter 5 covers managing users and groups, Chapter 6 is about managing files
and directories, and Chapter 7 covers backups and recovery. These three chapters
are fundamental to system operations and security.

 - Chapters 8, 9, and 11 are all about partitioning and filesystems, which are funda‐
mental to managing data storage. Data management is the most important aspect
of computing.

 - Chapter 10 is fun. This chapter is about finding detailed information about your
computer hardware without opening the case. Modern PC hardware self-reports
a lot of information, and Linux supplements this self-reporting with databases of
additional information.

 - Chapters 12 and 13 teach setting up secure remote access, and Chapter 14 intro‐
duces the excellent firewalld, the dynamic firewall that easily handles all kinds of
complicated scenarios, like roaming between different networks and managing
multiple network interfaces.

 - Chapter 15 introduces new features in CUPS, the Common Unix Printing Sys‐
tem, including “driverless” printing, which is especially good for mobile devices
because they can connect to a printer without having to download a lot of
software.

 - Chapter 16 shows how to control your own LAN name services with the excel‐
lent Dnsmasq. Dnsmasq has stayed current with support for new protocols, and
the old commands and configuration options have not changed. It is a first-rate
name server that seamlessly integrates DNS and DHCP for central management
of IP addressing and advertising network services.

 - Chapter 17 introduces chrony and timesyncd, two new implementations of the
Network Time Protocol (NTP). It also includes the old tried-and-true _ntp_ server
and client.

 - Chapter 18 introduces installing Linux on the Raspberry Pi, the popular little
inexpensive single-board computer, and using it to build an internet firewall/
gateway.

**Preface** **|** **xv**

 - Chapter 19 shows how to use SystemRescue to reset lost Linux and Windows
passwords, rescue nonbooting systems, rescue data on a failing system, and cus‐
tomize SystemRescue to make it even more useful.

 - Chapters 20 and 21 teach basic troubleshooting, with emphasis on searching log
files, probing networks, and probing and monitoring hardware.

 - The Appendix contains cheat sheets for managing software installation and
maintenance.

**Conventions Used in This Book**

The following typographical conventions are used in this book:

_Italic_

Indicates new terms, URLs, email addresses, filenames, and file extensions, as
well as to refer to program elements such as Linux variable or function names,
databases, data types, environment variables, statements, and keywords.

```
Constant width
```

Used for program listings and some command options.

```
Constant width bold
```

Shows commands or other text that should be typed literally by the user.

```
Constant width italic
```

Shows text that should be replaced with user-supplied values or by values deter‐
mined by context.

This element signifies a tip or suggestion.

This element signifies a general note.

This element indicates a warning or caution.

**xvi** **|** **Preface**

**Using Code Examples**

This book is here to help you get your job done. In general, if example code is offered
with this book, you may use it in your programs and documentation. You do not
need to contact us for permission unless you’re reproducing a significant portion of
the code. For example, writing a program that uses several chunks of code from this
book does not require permission. Selling or distributing examples from O’Reilly
books does require permission. Answering a question by citing this book and quoting
example code does not require permission. Incorporating a significant amount
of example code from this book into your product’s documentation does require
permission.

We appreciate, but generally do not require, attribution. An attribution usually
includes the title, author, publisher, and ISBN. For example: “ _Linux Cookbook_,
Second Edition, by Carla Schroder (O’Reilly). Copyright 2021 Carla Schroder,
978-1-492-08716-8.”

If you feel your use of code examples falls outside fair use or the permission given
above, feel free to contact us at _[permissions@oreilly.com](mailto:permissions@oreilly.com)_ .

**O’Reilly Online Learning**

For more than 40 years, _[O’Reilly Media](http://oreilly.com)_ has provided technol‐
ogy and business training, knowledge, and insight to help
companies succeed.

Our unique network of experts and innovators share their knowledge and expertise
through books, articles, and our online learning platform. O’Reilly’s online learning
platform gives you on-demand access to live training courses, in-depth learning
paths, interactive coding environments, and a vast collection of text and video from
O’Reilly and 200+ other publishers. For more information, visit _[http://oreilly.com](http://oreilly.com)_ .

**How to Contact Us**

Please address comments and questions concerning this book to the publisher:

O’Reilly Media, Inc.
1005 Gravenstein Highway North
Sebastopol, CA 95472

**Preface** **|** **xvii**

800-998-9938 (in the United States or Canada)
707-829-0515 (international or local)
707-829-0104 (fax)

We have a web page for this book, where we list errata, examples, and any additional
information. You can access this page at _[https://oreil.ly/linux-cookbook-2e](https://oreil.ly/linux-cookbook-2e)_ .

Email _[bookquestions@oreilly.com](mailto:bookquestions@oreilly.com)_ to comment or ask technical questions about this
book.

For news and information about our books and courses, visit _[http://oreilly.com](http://oreilly.com)_ .

Find us on Facebook: _[http://facebook.com/oreilly](http://facebook.com/oreilly)_ .

Follow us on Twitter: _[http://twitter.com/oreillymedia](http://twitter.com/oreillymedia)_ .

Watch us on YouTube: _[http://www.youtube.com/oreillymedia](http://www.youtube.com/oreillymedia)_ .

**Acknowledgments**

I really lucked out with this book. My editor, Jeff Bleiel, has been unfailingly suppor‐
tive and helpful, contributed numerous improvements, and kept the whole project
organized and on track. If you think herding cats is difficult, try being a book editor.

My intern, Kate Urness, was a Linux newbie at the start of this adventure, which
made her the perfect reviewer. She tested every recipe and contributed substantially
to the accuracy and clarity of the recipes. We drank gallons of coffee and had fun
together, which was also a substantial contribution.

Technical editor Daniel Barrett has a fabulous eye for detail, and relentlessly pressed
for more precision in wording and descriptions, and provided many improvements.
Providing a book full of commands is the easy part, explaining how they work is the
hard part. Every writer should be fortunate to have such a technical editor.

Technical editor Jonathan Johnson found things everyone else missed, contributed
some super-cool command incantations, and provided humor, and let me tell you, I
needed it.

Zan McQuade, acquisitions editor, started this whole crazy deal. There were talks
over the years about updating the _Linux Cookbook_, but Zan made it happen.

Great thundering herds of thanks to my wife, Terry, who fed the mules and cats and
dogs and me, provided much encouragement, and kept me from running away from
home because I lost my mind and agreed to write another book.

Special thanks to our cats, Duchess (Figure P-1), Stash (Figure P-2), and Mad Max
(Figure P-3), who appear in this book. They helped greatly by sleeping on my key‐
board, not letting me have my chair, and making mysterious loud crashes a lot.

**xviii** **|** **Preface**

_Figure P-1. Duchess holds my feet down, for my own good_

_Figure P-2. Stash cat, our glamour boy_

**Preface** **|** **xix**

_Figure P-3. Mad Max rests up for the next mayhem_

**xx** **|** **Preface**

**<u>CHAPTER 1</u>**
#### **Installing Linux**

One of the hurdles for new Linux users is installing Linux. Linux is the easiest com‐
puter operating system to install: pop in your installation disk, answer a few ques‐
tions, and then do something else until it finishes. In this chapter you will learn how
to install Linux by itself, how to run a live Linux, how to multiboot multiple Linux
distributions on one computer, and how to dual-boot with Microsoft Windows.

**Experimenting with Linux**

You need the freedom to make mistakes, so if it is possible, use a
second computer for getting acquainted with Linux. If this is not
possible, make sure you always have fresh backups of your data.
You can always restore a broken Linux installation, but your data is
irreplaceable. If you are setting up dual-boot with Windows, be
sure you have your Windows installation and recovery media.

Most Linux distributions provide dual-purpose installation images: you can run them
live from a USB stick and install them to your hard drive from the same image. A live
Linux makes no changes to your computer—just boot it up, check it out, then reboot
to your host system. Some live Linuxes, such as Ubuntu, support storing your data on
the USB stick, so you have a completely portable Linux that you can run from any
computer.

Multiboot is installing more than one operating system on a computer, and then
picking the one you want to use from your boot menu. You can multiboot any Linux
system, any of the free Unixes (FreeBSD, NetBSD, OpenBSD), and you can multiboot
Linux and Microsoft Windows. Dual-booting Linux and Windows is a common way
for Windows users to get acquainted with Linux, and for users who need both.

**1**

What about Apple’s macOS, you ask? Sorry, but dual-booting Linux and macOS is an
unreliable endeavor that gets more difficult with every macOS release. One alterna‐
tive for running both on a single machine is to run Linux in Parallels, the macOS vir‐
tual machine host.

Rather than installing Linux yourself, you could buy a PC with Linux already
installed. There are a number of good Linux specialists that sell Linux laptops, desk‐
tops, and servers. System76, ZaReason, Linux Certified, Think Penguin, Entroware,
and Tuxedo Computers are all Linux specialists. Dell has been expanding its Linux
lineup, and enterprise Linux vendors Red Hat, SUSE, and Ubuntu all partner with
hardware vendors, including Dell, Hewlett-Packard, and IBM.

Still, it pays to know how to install Linux. This opens up a whole world of experimen‐
tation, customization, and disaster recovery. _Distro-hopping_ is a time-honored pas‐
time, where you download and try different Linux distributions.

Even though installing Linux takes just a few steps, you need a certain amount of
knowledge, especially when you want to customize your installation, like setting up
disk partitions in a particular way or multibooting with other Linux distributions or
with Microsoft Windows. You need to know how to enter your system Basic Input
Output System (BIOS) or Unified Extensible Firmware Interface (UEFI) setup. You
need good internet access. All Linux distributions are freely downloadable, even the
commercial enterprise distributions like Red Hat, SUSE, and Ubuntu. Download sizes
range from a few megabytes for super-small Linuxes like Tiny Core Linux, which
bundles a complete operating system with a graphical desktop into 12 MB, to 10+ GB
for SUSE Linux Enterprise Server. Most Linux distros provide 2–4 GB installation
images, which fit perfectly on a DVD or small USB stick.

Most Linux distributions provide a network installer image; for example, Debian’s is
around 200 megabytes. This installs enough of a Debian system to boot up, connect
to the internet, and then download only the packages you want, rather than down‐
loading a complete installation image.

You can freely share any Linux distribution that you download.

You also have the option to buy Linux distributions on DVD and USB media. Visit
[Shop Linux Online and Linux Disc Online to find physical installation media for vari‐](https://shoplinuxonline.com)
ous Linux distributions.

**Booting from Installation Media**

You must be able to boot your system from your USB or DVD installation disk. You
may have to enter your system’s BIOS or UEFI setup to enable booting from a remov‐
able device. Some have an option to select an alternate boot device without entering
the BIOS/UEFI; for example, my laptop’s UEFI displays a screen at startup that lists all

**2** **|** **Chapter 1: Installing Linux**

the relevant keypresses: F2 or Delete to enter setup, and F11 to enter the alternate
boot device menu. Dell systems use F12 to open their one-time boot menu. Every one
is special and unique, so check out your motherboard manual to learn how.

You may have to disable Secure Boot in your UEFI setup to enable booting from
removable media. Fedora, openSUSE, and Ubuntu all have their own signing keys
and will boot with Secure Boot enabled. Other Linux distributions, such as
SystemRescue (Chapter 19), do not.

**Secure Boot**

Secure Boot is a security feature of your UEFI setup. When Secure
Boot is enabled, it allows booting only operating systems that pro‐
vide special signed keys. The idea is to prevent malicious code from
controlling your bootloader.

Most Linux distributions do not provide signed keys, so Secure
Boot must be disabled to run them.

**Where to Download Linux**

There are hundreds of Linux distributions, and a great place to learn about them is
[DistroWatch.com, the most comprehensive Linux distribution resource. DistroWatch](https://distrowatch.com)
publishes reviews, detailed information, and news, and their popular list of the top
100 distributions.

**Best Linux for Newbies**

Linux provides rather a lot of a good thing, maybe too much. The recipes in this book
were tested on openSUSE, Fedora Linux, and Ubuntu Linux. These three are wellestablished, popular, and well-maintained, and they represent three different Linux
families (see the Appendix). In my experience Ubuntu is perfect for a Linux newbie
because it has the easiest installer, good documentation, and a large and supportive
user community.

Every Linux has its differences: different software installers, different defaults, differ‐
ent file locations…but the fundamentals are all similar. Most of what you learn on any
particular distro is applicable to all of them.

**Where to Download Linux** **|** **3**

**Hardware Architectures**

How-to authors used to be able to take it for granted that readers
were using x86 hardware. With the rise in popularity of ARM pro‐
cessors this is no longer true. Linux supports a large number of
hardware architectures, and Recipe 10.11 shows how to detect what
you have. You cannot accidentally install the wrong Linux version
because the installation will fail at the beginning, and you will see
an error message telling why.

Linux installation images are packaged in the ISO 9660 format, and have a _*.iso_
extension, for example, _ubuntu-20.04.1-desktop-amd64.iso_ for x86-64 machines, and
_ubuntu-20.04.1-live-server-arm64.iso_ for ARM machines. This is a compressed
archive that contains the entire filesystem and the installation program. When you
copy this archive to your installation medium, it is uncompressed and you can see all
the files.

The _*.iso_ format was originally for CDs and DVDs. Once upon a time, Linux fit on a
single CD. (Once upon a time, it fit on a few 3.5” diskettes!) Now most Linux distri‐
butions are too large for CDs. USB sticks are perfect for Linux installations, as they
are inexpensive, reusable, and much faster than optical media.

**1.1 Entering your System BIOS/UEFI Setup**

**Problem**

You want to enter your system’s BIOS/UEFI setup.

**Solution**

Enter your BIO/UEFI setup by pressing the appropriate F _n_ key at startup. On Dell,
ASUS, and Acer systems this is usually F2, and Lenovo uses F1. However, this varies;
for example, some systems use the Delete key, so check your machine’s documenta‐
tion. Some systems tell which key to press on their startup screens. It can be a bit
tricky to press the key at the right time, so start pressing it right after you press the
power button, just like banging on an elevator button to make it arrive faster.

Every UEFI looks different; for example, Lenovo’s is bright and well organized
(Figure 1-1).

The ASRock UEFI on my test system is dark and dramatic (Figure 1-2). This particu‐
lar motherboard targets gamers and has many settings for overclocking the CPU and
other performance enhancements. This screen shows the motherboard browser;
hover the cursor over any item and it provides information about that item.

**4** **|** **Chapter 1: Installing Linux**

_Figure 1-1. Lenovo’s UEFI on a new ThinkPad_

_Figure 1-2. ASRock UEFI has a motherboard browser_

**1.1 Entering your System BIOS/UEFI Setup** **|** **5**

**Discussion**

When you boot up your computer, the first startup instructions come from the BIOS
or UEFI firmware, stored on the computer’s motherboard. BIOS is the old legacy sys‐
tem that has been with us since 1980. UEFI is its modern replacement. UEFI includes
legacy BIOS support. Nearly all computers made after the mid-2000s have UEFI.

UEFI has considerably more features than the old BIOS and is like a little operating
system. The UEFI setup screens control boot order, boot devices, security options,
Secure Boot, overclocking, displaying hardware health, networking, and many more
functions.

**See Also**

 - The documentation for your motherboard

 - [Unified Extensible Firmware Interface Forum](https://uefi.org)

**1.2 Downloading a Linux Installation Image**

**Problem**

You want to find and download a Linux installation image.

**Solution**

First, you need to choose which Linux you want to try. If you don’t know where to
[start, I recommend Ubuntu Linux. Fedora Linux and openSUSE Linux are also excel‐](https://ubuntu.com)
lent for anyone new to Linux.

After your download is completed, verify that you have a good download. This is an
important step that ensures you have an image that did not get damaged during the
download or was otherwise altered in some way.

Every Linux distribution provides signed keys and checksums for its download
images. Ubuntu provides copy-and-paste instructions. Open a terminal and change
to the directory where you downloaded Ubuntu. For Ubuntu 21.04, verifying the
installation image looks like this:

```
  $ echo "fa95fb748b34d470a7cfa5e3c1c8fa1163e2dc340cd5a60f7ece9dc963ecdf88 \
  *ubuntu-21.04-desktop-amd64.iso" | shasum -a 256 --check

  ubuntu-21.04-desktop-amd64.iso: OK

```

**6** **|** **Chapter 1: Installing Linux**

If you see “shasum: WARNING: 1 computed checksum did NOT match,” then your
download is no good, assuming you copied the correct checksum. In most cases the
image was corrupted during the download, so try downloading it again.

Other Linux distributions provide slightly different verification methods, so follow
their instructions.

**Discussion**

A great site to learn about the hundreds of Linux distributions is [Distrowatch.com.](https://distrowatch.com)
Distrowatch provides news and information about more Linux distros than anyone.

**See Also**

 - _man 1 sha256sum_

 - [Ubuntu Linux](https://ubuntu.com)

 - [Fedora Linux](https://getfedora.org)

 - [openSUSE Linux](https://opensuse.org)

**1.3 Creating a Linux Installation USB Stick with**
**UNetbootin**

**Problem**

You have downloaded a Linux installation _*.iso_ image, and you want to transfer it to a
USB stick to create your own installation media. You prefer a graphical tool to create
your installation media.

**Solution**

[Try UNetbootin, Universal Netboot Installer. It runs on Linux, macOS, and Windows,](https://oreil.ly/8CXp9)
so you can download and create a Linux installation disk on any of these operating
systems. UNetbootin creates an installation USB drive from your downloaded _*.iso_
file or downloads a fresh _*.iso_ file (Figure 1-3).

You may use any size USB stick (that is larger than your _*.iso_ file, of course). The _*.iso_
overwrites the entire device, so you can’t use it for anything else, and you must use a
separate USB stick for each _*.iso_ file.

**1.3 Creating a Linux Installation USB Stick with UNetbootin** **|** **7**

_Figure 1-3. Using UNetbootin to create an installable Linux USB stick_

The UNetbootin site provides downloads and instructions. Some Linux distributions
[provide UNetbootin packages, but downloading from the UNetbootin site is simple](https://unetbootin.github.io)
and always up-to-date.

**Discussion**

Other good graphical apps are USB Creator, ISO Image Writer, and GNOME Multi‐
Writer, which copies to multiple USB drives at one time.

After you have created your installation USB drive, you can view the files on it. The
single _*.iso_ expands into a complete filesystem full of files and directories, like this
example for Ubuntu:

```
  $  ls -C1 /media/duchess/'Ubuntu 21.04.1 amd64'/
  boot
  casper
  dists
  EFI
  install
  isolinux
  md5sum.txt
  pics
  pool
  preseed
  README.diskdefines
  ubuntu

```

**8** **|** **Chapter 1: Installing Linux**

Every Linux distribution sets up its installers in its own way. This example shows
Fedora’s installation files:

```
  $  ls -C1 /media/duchess/Fedora-WS-Live-34-1-6/
  EFI
  images
  isolinux
  LiveOS
```

It would be lovely to have a single USB stick with a herd of Linux installation files,
[and there are some programs that do this. My favorite is Ventoy. Ventoy supports a](https://ventoy.net)
large number of Linux distributions. It runs on both Linux and Windows, and you
can create a USB stick full of Linux installers for running live Linuxes, and for perma‐
nent installations to hard disks.

**See Also**

 - [UNetbootin](https://oreil.ly/8CXp9)

 - Chapter 9

 - [Ventoy](https://ventoy.net)

**1.4 Creating a Linux Installation DVD with K3b**

**Problem**

You want to create a Linux DVD installation disk with a graphical tool.

**Solution**

Use K3b (KDE Burn Baby Burn). K3b is the best graphical CD/DVD writing app for
Linux.

If you do not have a Linux system, then use any CD/DVD writing program that
writes an ISO 9660 image. Your chosen CD/DVD writer will phrase this as something
like “burn an existing image to disk.”

You will see something like Figure 1-4 on K3b. Click “Burn Image,” and note the con‐
firmation on the bottom left that says “Write an ISO 9660…image to an optical disk.”

On the next screen (Figure 1-5), in the top left drop-down selector, select your _*.iso_
image. Then on the top right select “ISO 9660 filesystem image.” At the bottom under
Settings, check “Verify written data.” This computes a checksum after your image is
written and compares it to the checksum of the original _*.iso_ . This is an important
step because if the checksums do not match you have a corrupted disk, which is
unusable.

**1.4 Creating a Linux Installation DVD with K3b** **|** **9**

_Figure 1-4. Creating an installation DVD with K3b_

_Figure 1-5. Configuring the burn_

**10** **|** **Chapter 1: Installing Linux**

When the disk is successfully written, you will see a success message like the one
shown in Figure 1-6. If there were any errors, this screen will show some helpful error
messages.

_Figure 1-6. Success!_

**Discussion**

Brasero and XFBurn are also great CD/DVD writing apps for Linux, with simpler
interfaces than K3b, but still plenty of functionality.

The tech world changes fast. Just a few years ago I was burning CDs and DVDs for
everything. Then USB devices swept the market, and I haven’t burned a disk for
years, until I started writing this chapter.

Take heart, for CDs and DVDs are not obsolete, despite the efforts of computer mak‐
ers to make them obsolete by not including CD/DVD drives in their machines. This
is not a problem because you can purchase an external USB CD/DVD drive. You can
even find bus-powered drives, so you only need a USB cable, and don’t have to hassle
with a power cable. CD/DVD blanks are still good quality, so if you prefer optical
disks, they are a reliable choice.

**1.4 Creating a Linux Installation DVD with K3b** **|** **11**

**See Also**

 - [K3b](https://oreil.ly/MJmXF)

 - [Brasero](https://oreil.ly/a9Dxx)

**1.5 Using the wodim Command to Create a**
**Bootable CD/DVD**

**Problem**

You want a command-line tool to create a bootable CD/DVD.

**Solution**

Try the _wodim_ command. Your optical drive is most likely _/dev/cdrom_, symlinked
to _/dev/sr0_ . Use the symlink because it has correct permissions:

```
  $ ls -l /dev | grep cdr
  lrwxrwxrwx 1 root root      3 Mar 7 12:38 cdrom -> sr0
  lrwxrwxrwx 1 root root      3 Mar 7 12:38 cdrw -> sr0
  crw-rw----+ 1 root cdrom  21,  2 Mar 7 08:34 sg2
  brw-rw----+ 1 root cdrom  11,  0 Mar 7 12:57 sr0
```

Then copy your installation image to disk:

```
  $ wodim dev=/dev/cdrom -v ubuntu-21.04-desktop-amd64.iso
```

**Discussion**

In the _ls -l_ example, there are _sg2_ and _sr0_ devices. _sg2_ is a character device, and _sr0_ is a
block device. Character devices provide raw access to a hardware device using the raw
kernel drivers. Block devices provide buffered access to a hardware device through
various software programs that handle reading and writing to physical media. Users
interact with storage devices, like DVDs and hard disks, through the kernel’s block
device drivers. You can see raw and block kernel modules listed in your _/boot/config-*_
file.

**See Also**

 - _man 1 wodim_

**12** **|** **Chapter 1: Installing Linux**

**1.6 Creating a Linux Installation USB Stick with**
**the dd Command**

**Problem**

You want to create your installation USB drive from the command line, rather than
using a graphical tool.

**Solution**

Use the _dd_ command. _dd_ is on every Linux and works the same way on all of them.

First, verify the dev name for your USB stick with the _lsblk_ command, so that you
copy your image to the correct device. In the following example, that is _/dev/sdb_ :

```
  $ lsblk -o NAME,FSTYPE,LABEL,MOUNTPOINT

  NAME  FSTYPE LABEL    MOUNTPOINT
  sda
  ├─sda1 vfat        /boot/efi
  ├─sda2 xfs   osuse15-2  /boot
  ├─sda3 xfs         /
  ├─sda4 xfs         /home
  └─sda5 swap        [SWAP]
  sdb
  └─sdb1 xfs   32gbusb
  sr0
```

The following example creates a USB installation stick and shows its progress:

```
  $ sudo dd status=progress if=ubuntu-20.04.1-LTS-desktop-amd64.iso of=/dev/sdb
  211509760 bytes (212 MB, 202 MiB) copied, 63 s, 3.4 MB/s
```

This takes a few minutes. When it’s finished, it looks like this:

```
  2782257664 bytes (2.8 GB, 2.6 GiB) copied, 484 s, 5.7 MB/s
  5439488+0 records in
  5439488+0 records out
  2785017856 bytes (2.8 GB, 2.6 GiB) copied, 484.144 s, 5.8 MB/s
```

Remove the drive, then reinsert it and take a quick look at the files. Figure 1-7 shows
the installation files for Ubuntu Linux in the Thunar file manager.

**1.6 Creating a Linux Installation USB Stick with the dd Command** **|** **13**

_Figure 1-7. Ubuntu Linux installation files in Thunar_

The files are marked with padlocks because the Ubuntu installer uses the SquashFS
read-only filesystem. You can read them, but not delete or edit them.

The installation USB stick is ready to use.

**Discussion**

Identifying the correct device to copy your installation to is super important. In the
_lsblk_ example, there are only two storage devices. Note the LABEL column; you can
create labels on filesystems so you know what they are. (See Recipe 9.2 and the filesys‐
tem creation recipes in Chapter 11 to learn how to create filesystem labels.)

The graphical installation media creators are good, but I prefer the _dd_ command
because it is simple and reliable. _dd_ is short for Disk Duplicator. This is one of those
ancient useful GNU commands, in the GNU _coreutils_ package, that has been around
forever.

**See Also**

 - _man 1 dd_

**14** **|** **Chapter 1: Installing Linux**

**1.7 Trying a Simple Ubuntu Installation**

**Problem**

You want to try a simple Ubuntu installation. You have your installation medium
ready, and you know how to boot to your installation medium. There is nothing on
the computer that you want to keep, so Ubuntu can take over the hard drive.

**Solution**

The following example demonstrates a fast, simple installation of Ubuntu Linux
21.04, Hirsute Hippo. All Ubuntu releases have alliterative animal names.

Insert your installation device, power on the machine, and open your system’s onetime boot menu. Select the installation device and boot up (Figure 1-8).

_Figure 1-8. Booting to an installation USB stick_

**All UEFI Screens Look Different**

Every vendor’s UEFI looks different, and every release changes in
appearance. The preceding example is a Dell UEFI one-time boot
screen.

When the GRUB menu appears, select the default option. For Ubuntu 21.04 this is
_Ubuntu_, and it boots by default when you make no selection (Figure 1-9).

**1.7 Trying a Simple Ubuntu Installation** **|** **15**

_Figure 1-9. Ubuntu installer’s GRUB boot menu_

Then you will have a choice of Try Ubuntu and Install Ubuntu. Try Ubuntu launches
the live version, and Install Ubuntu opens the installer (Figure 1-10). It doesn’t matter
which one you select because there is a big installation button on the live desktop.

_Figure 1-10. Choosing the live image or the installer_

When you launch the installer, it walks you through a few steps. First, language and
keyboard layout.

Then, if you have a wireless network interface, you have the option to set it up or wait
until after installation.

**16** **|** **Chapter 1: Installing Linux**

Then configure your installation. On the “Updates and other software” screen, select
“Normal installation” (Figure 1-11).

_Figure 1-11. Select Normal installation_

On the next screen, select “Erase disk and install Ubuntu,” then click Install Now
(Figure 1-12).

_Figure 1-12. Select Erase disk and install Ubuntu_

The next screen asks “Write the changes to disk?” Click Continue. There are a few
more screens: set your time zone, create your username, password, and hostname,
and then the installation starts. You do not have to do anything until the installation
is finished, then restart the computer, remove your installation device when promp‐
ted, and press the Enter key. After restart you will have a few setup screens, then you
can play with your nice new Ubuntu Linux.

**1.7 Trying a Simple Ubuntu Installation** **|** **17**

**Discussion**

Most Linux distributions have a similar installation process: boot your installation
medium, then choose a default simple installation or choose a customizable installa‐
tion. Some ask all the questions at the beginning, such as username and password;
others do the final setup after reboot.

Linux installers typically have back buttons to go back and make changes. You may
quit at any time, though this may leave your system in an unusable state. This is not
fatal; just start over and do a complete installation.

You may reinstall as many times on as many machines as you want without worrying
about license keys, except for the enterprise distros that require registration keys (Red
Hat, SUSE, or Ubuntu with paid support).

**See Also**

 - [Ubuntu documentation](https://help.ubuntu.com)

**1.8 Customizing Partitioning**

**Problem**

You want to set up your own partitioning scheme.

**Solution**

In this recipe we will redo the example Ubuntu installation in Recipe 1.7 and set up
our own partitioning scheme.

**Entire Disk Will Be Erased**

In this recipe a new partition table is created, which erases the
entire disk.

You can set up partitioning in any number of ways. Table 1-1 shows how I prefer to
set up my Linux workstations.

_Table 1-1. Example partitioning scheme_

**<mark>Partition name</mark>** **<mark>Filesystem type</mark>** **<mark>Mountpoint</mark>**
/dev/sda1 ext4 /boot

/dev/sda2 ext4 /

**18** **|** **Chapter 1: Installing Linux**

**<mark>Partition name</mark>** **<mark>Filesystem type</mark>** **<mark>Mountpoint</mark>**
/dev/sda3 ext4 /home

/dev/sda4 ext4 /tmp

/dev/sda5 ext4 /var

/dev/sda6 swap

When you get to the Installation Type screen, select “Something else” to start your
customized installation (Figure 1-13).

_Figure 1-13. Selecting the installation type_

When you get to the partitioning screen, erase the entire disk by clicking New Parti‐
tion Table. Then you will see something like Figure 1-14.

_Figure 1-14. Creating a new partition table_

**1.8 Customizing Partitioning** **|** **19**

To create new partitions click on the “free space” line to select it, then click the plus
sign, +, to add a new partition. Set the size, filesystem, and mountpoint. Figure 1-15
creates a 500 MB _/boot_ partition.

_Figure 1-15. Creating the boot partition_

Click on “free space” again, click the plus sign, and keep going until you have created
all of your partitions. Figure 1-16 shows the result: _/boot_, _/home_, _/var_, _/tmp_, and the
swap file are all on their own partitions.

_Figure 1-16. Partitions set up and ready to continue the installation_

**20** **|** **Chapter 1: Installing Linux**

**Selecting Partitions to Format**

Note the “Format?” checkboxes in the partitioning screen. All new
partitions must be formatted with a filesystem.

**Discussion**

The examples are from a virtual machine, so the hard disk is _vda_ instead of _sda_ .

The example in the recipe uses the Ext4 filesystem on all the partitions. You may use
whatever filesystems you want; see Chapter 11 to learn more.

Disk partitions are like having a bunch of separate physical disks. Each one is an
independent section of the hard disk, and each partition can have a different filesys‐
tem. The filesystems you select, and their sizes, all depend on how you use your sys‐
tem. If you need a lot of data storage, then _/home_ needs to be large. It could even be a
separate disk.

Giving _/boot_ its own partition makes managing multiboot systems easier because this
makes the boot files independent of whatever operating systems you install or
remove. 500 MB is more than enough.

Putting _/_, root, in its own partition makes it easy to restore or to nuke and replace
with a different Linux. 30 GB is more than enough for most distros, except when you
use the Btrfs filesystem, then you should make it 60 GB to make room for storing
snapshots.

Put _/home_ on its own partition to isolate it from the root filesystem, so you can
replace your Linux installation without touching _/home_ . _/home_ could even be on a
separate disk.

_/var_ and _/tmp_ can fill up from runaway processes. Putting them on their own parti‐
tions prevents them from crashing the other filesystems. Mine are usually 20 GB
each, and for a busy server they need to be larger.

Putting a swap file equal to the size of your RAM on its own partition enables
suspend-to-disk.

**See Also**

 - The discussion in Recipe 3.9 to learn about suspend and sleep states

 - Chapter 8

 - Chapter 9

**1.8 Customizing Partitioning** **|** **21**

**1.9 Preserving Existing Partitions**

**Problem**

You have _/home_ on its own partition and want to preserve it for the new Linux
installation.

**Solution**

In Recipes 1.7 and 1.8 we erased the existing installation by creating a new partition
table. When you have partitions that you want to preserve, such as _/home_ or any
shared directory, do not create a new partition table. Instead, edit the existing parti‐
tions. You can delete existing partitions, create new partitions, and reuse existing
partitions.

In the following example in the Ubuntu installer, _/dev/sda3_ is a separate _/home_ parti‐
tion. Right-click on it, then click “Change…” Then you can set its mountpoint to _/_
_home_, and make sure that the “Format?” box is NOT checked (Figure 1-17). If you
format it or change the filesystem type, all data on the partition will be erased.

_Figure 1-17. Saving /dev/sda3, instead of overwriting it_

**Discussion**

The Discussion in Recipe 1.8 goes into some detail on customizing your partitioning
scheme and which filesystems benefit from being isolated on their own partitions.

**22** **|** **Chapter 1: Installing Linux**

**See Also**

 - Chapter 8

 - Chapter 9

**1.10 Customizing Package Selection**

**Problem**

You don’t want the default package installation, but prefer to select your own software
to install. For example, you might want to set up a development workstation, a web
server, a central backup server, a multimedia production workstation, a desktop pub‐
lishing workstation, or choose your own office productivity applications.

**Solution**

Every Linux distro manages installation options a little differently. In this recipe you
will see examples for openSUSE and Fedora Linux. openSUSE supports multiple
installation types from a single installation image, and Fedora Linux has several dif‐
ferent installation images.

These two examples are typical of the general-purpose Linux distributions.

Remember, you can install and remove software all you want after installation.

**openSUSE**

The openSUSE installer supports both a simple installation from defaults and exten‐
sive customization options. It has two screens that control package selection. The first
screen (Figure 1-18) provides a selection of system roles to choose from, such as a
desktop system with the KDE or GNOME graphical environment, a generic desktop
with the IceWM window manager, a server with no graphical environment, or a
transactional server with no graphical environment. Each role comes with a prefab
set of packages. You can install one of these as is or select packages to install or
remove.

Each role is customizable, as you will see a few screens later (Figure 1-19).

**1.10 Customizing Package Selection** **|** **23**

_Figure 1-18. openSUSE installation roles_

_Figure 1-19. openSUSE installation settings_

**24** **|** **Chapter 1: Installing Linux**

Click Software to open the package selection screen. This screen displays the open‐
SUSE _patterns_, which are related groups of packages you can install with a single
command. I like the Xfce desktop, so I am adding it to my installation (Figure 1-20).

Note the Details button at the bottom left. Click this to open a screen with multiple
tabs for more fine-grained package selection (Figure 1-21). In this screen you will
find a massive amount of information: the individual packages in each pattern, pack‐
age groups, download repositories, installation summary, dependencies, and infor‐
mation on every package. Use the window on the right to select or deselect packages
from each pattern. The installer will automatically resolve dependencies after your
changes.

_Figure 1-20. openSUSE software patterns_

**1.10 Customizing Package Selection** **|** **25**

_Figure 1-21. openSUSE individual package selection_

When you are finished with software selection, you are returned to the Installation
Summary screen, giving you another chance to change your installation settings.
Click the green Next button to complete the installation.

**Fedora Linux**

The Fedora Linux Workstation and Server installers provide only partitioning
options and no package customization. You need the 600 MB network installer image
for a customizable installation, from [Fedora Alternative Downloads. It is labeled as](https://oreil.ly/JW9J8)
Fedora Server, but it provides complete package selection for any type of Fedora
installation. Set up all your installation choices from the Installation Summary screen
(Figure 1-22).

Take note of all the installation options on the Installation Summary screen: software
selection, user creation, partitioning, keyboard and language, time zone, network,
and hostname. Click Software Selection to open the screen for selecting the packages
you want to install (Figure 1-23).

**26** **|** **Chapter 1: Installing Linux**

_Figure 1-22. Fedora Linux network installer_

_Figure 1-23. Fedora Linux package selection_

**1.10 Customizing Package Selection** **|** **27**

When you are finished, click Done; you are returned to the Installation Summary
screen. When you are finished setting up your installation, click Begin Installation,
and the rest of the installation runs unattended.

**Discussion**

Whatever Linux you want to try, read its documentation and release notes. This is
important information that saves a lot of aggravation. Also look for forums, mailing
lists, and wikis to find help.

You may install as many desktop environments as you want, and then select the one
you want to use when you log in. The button to select desktops is usually small and
not obvious; for example, the default Ubuntu login screen (Figure 1-24) hides the
desktop selector button until you click on a username. Xfce, Lxde, GNOME, and
KDE are some of the popular graphical desktops. GNOME is the default on Ubuntu,
openSUSE, and Fedora.

_Figure 1-24. Selecting a different graphical environment_

**See Also**

 - [openSUSE documentation](https://oreil.ly/AupNr)

 - [SUSE Transactional Updates](https://oreil.ly/mTyuV)

**28** **|** **Chapter 1: Installing Linux**

**1.11 Multibooting Linux Distributions**

**Problem**

You want to install more than one Linux distribution on your computer in a multi‐
boot setup, then select the one you want to run from your boot menu.

**Solution**

No worries, for you can install as many Linuxes as your hard disk (or disks) will hold.
You must already have one Linux installed, and it must have a separate _/boot_ parti‐
tion. Then the steps are:

1. Provide sufficient free disk space for the new Linux, which can be on the same
hard disk as your existing Linux, or on a separate hard disk, either internal or
external.

2. Make careful note of the partitions that belong to your first installed Linux, so
that you do not accidentally overwrite or delete any partitions you want to keep.

3. Mount the _/boot_ partition in every new Linux that you install, and do not format
it.

4. Boot to your installation medium, then configure the new installation to install
on the free disk space.

The installer will automatically find your existing Linux installation and add the new
Linux to the boot menu. After the installation is completed, you will see a boot menu
like Figure 1-25, which has options to boot to Linux Mint or Ubuntu.

**1.11 Multibooting Linux Distributions** **|** **29**

_Figure 1-25. New boot menu with Linux Mint and Ubuntu_

**Discussion**

If you need to free up space on your hard disk, you can shrink existing partitions
safely (see Recipe 9.7) before you launch the installer. It is safest to do this on
unmounted partitions, and some filesystems cannot be shrunk while they are moun‐
ted. Use SystemRescue to shrink partitions, see Recipe 19.12.

Most Linux installers are smart enough to recognize existing Linux installations and
to offer the option to preserve them. In Figure 1-26 you see the Linux Mint installer,
providing the options to take over your whole hard disk or to install next to Ubuntu
without deleting it.

**30** **|** **Chapter 1: Installing Linux**

_Figure 1-26. Installing Linux Mint next to Ubuntu_

**See Also**

 - Recipe 8.9

 - Recipe 9.7

 - Recipe 19.12

 - The installation documentation for your Linux distribution

**1.12 Dual-boot with Microsoft Windows**

**Problem**

You want to dual-boot Linux and Windows on your computer.

**Solution**

Dual-booting Linux and Windows installs both systems on one computer, and then
you choose the one you want to use from your boot menu at startup.

It is best to install Windows first, if it is not already installed, and install Linux sec‐
ond. Windows likes to control the bootloader, so installing Linux second allows Linux
to take control.

As always, make sure you have fresh backups and Windows recovery media.

**1.12 Dual-boot with Microsoft Windows** **|** **31**

After Windows is installed, start your Linux installation. You will install Linux in
whatever way you want: a simple installation or a customized installation where you
set up partitioning and package selection. There is an important option specific to
multibooting:

1. If you have a single hard drive, then the “Device for boot loader installation”
is _/dev/sda_ .

2. If you have Windows on one hard disk and are installing Linux to a second hard
disk, the “Device for boot loader installation” is the Linux disk. Use the device
name, for example _/dev/sdb_, not a partition name, like _/dev/sdb1_ .

In Figure 1-27, there are two hard drives, with Windows on _/dev/sda_ and Linux
on _/dev/sdb_ .

_Figure 1-27. Installing Ubuntu next to Windows_

Be very certain you are installing Linux to the correct location and not overwriting
Windows. You may partition for Linux just as you would if you were installing it
standalone, and again, be careful which partitions you change.

Once you have your partitioning set up and are satisfied with your installation config‐
uration, go ahead and complete your Linux installation. After it is finished and you
have rebooted, your GRUB menu will have entries for both systems (Figure 1-28).

**32** **|** **Chapter 1: Installing Linux**

_Figure 1-28. openSUSE and Windows in the GRUB boot menu_

**Discussion**

You can install as many Linux and Windows systems on your system in a multiboot
setup as you have room for on your hard drives.

There are other ways to run Linux and Windows on the same machine. Windows 10
includes the Windows Subsystem for Linux 2 (WSL 2), which runs supported Linux
distributions in a virtual environment. You can run Windows in virtual machines on
Linux if you have Windows installation media. Virtual machines are lovely because
you can run multiple operating systems at the same time, though you need higherend CPUs and lots of memory.

VirtualBox and QEMU/KVM/Virtual Machine Manager are good free virtual
machine hosts that run on Linux.

**See Also**

 - [Windows Subsystem for Linux Documentation](https://oreil.ly/4cbnk)

 - [VirtualBox](https://oreil.ly/pI6J6)

 - [KVM](https://oreil.ly/gNdi9e)

**1.12 Dual-boot with Microsoft Windows** **|** **33**

 - [Virtual Machine Manager](https://oreil.ly/5vj6m)

 - [QEMU](https://oreil.ly/VKBkf)

**1.13 Recovering an OEM Windows 8 or 10 Product Key**

**Problem**

You purchased a computer with Windows 8 or 10 preinstalled, and you can’t find
your product key.

**Solution**

Let Linux find it for you. Run the following command from a Linux system installed
on the same computer with Windows, or from SystemRescue:

```
  $ sudo cat /sys/firmware/acpi/tables/MSDM
  MSDMU
  DELL CBX3
  AMI
  FAKEP-RODUC-TKEY1-22222-33333
```

And there it is on the last line.

If you can log in to Windows, run the following command in Windows to retrieve
your product key:

```
  C:\Users\Duchess> wmic path softwarelicensingservice get OA3xOriginalProductKey
  OA3xOriginalProductKey
  FAKEP-RODUC-TKEY1-22222-33333
```

**Discussion**

If you have no recovery media, Windows 10 is a free download. You will need your
25-digit OEM product key for a fresh installation.

**See Also**

 - [Download Windows 10](https://oreil.ly/rz157)

**34** **|** **Chapter 1: Installing Linux**

**1.14 Mounting Your ISO Image on Linux**

**Problem**

You have downloaded a Linux _*.iso_ file and are curious to see what it looks like after it
is unpacked. You could go ahead and create a bootable DVD or USB stick, and then
inspect the files, but you really want to unpack it without copying it to another
device.

**Solution**

Linux has a pseudodevice called the _loop_ device. This makes your _*.iso_ image accessi‐
ble like any other filesystem. Follow these steps to mount your _*.iso_ image file in a
loop device.

First, create a mountpoint in your home directory, giving it whatever name you want.
In the example it is called _loopiso_ :

```
  $ mkdir loopiso
```

Mount your _*.iso_ in this new directory. In the example it is a Fedora Linux installation
image:

```
  $ sudo mount -o loop Fedora-Workstation-Live-x86_64-34-1.2.iso loopiso
  mount: /home/duchess/loopiso: WARNING: device write-protected, mounted read-only
```

See the mounted filesystem in a file manager (Figure 1-29).

_Figure 1-29. A mounted .iso in Fedora Linux 34_

You can enter the directories and read the files. You won’t be able to edit any files
because they are mounted read-only.

When you are finished, unmount it:

```
  $ sudo umount loopiso

```

**1.14 Mounting Your ISO Image on Linux** **|** **35**

**Discussion**

The loop device maps a regular file to a virtual partition, and you can set up a virtual
filesystem in this file. If you want try to creating your own, a little bit of web search‐
ing will find a lot of how-tos. Start with _man 8 losetup_ .

**See Also**

 - _man 8 mount_

 - _man 8 losetup_

**36** **|** **Chapter 1: Installing Linux**

**<u>CHAPTER 2</u>**
#### **Managing the GRUB Bootloader**

The _bootloader_ is the software that loads your operating system after you power up
your computer. The GRUB (GRand Unified Bootloader) bootloader is the most com‐
monly used bootloader on Linux.

GRUB supports a number of useful features: boot multiple operating systems on a
single PC, live configuration editing, themeable interface, and rescue modes. In this
chapter you will learn about all of these.

**GRUB versus GRUB 2**

There are two major GRUB releases, legacy GRUB and GRUB 2.
GRUB 2 is version 1.99 and up. Legacy GRUB ended at version
0.97 in 2005. A lot of GRUB how-tos still reference legacy GRUB
and compare it with GRUB 2. In this chapter I’m not going to talk
about legacy GRUB. It’s been retired for a long time and has little
relevance to using GRUB 2, so this chapter will focus exclusively on
GRUB 2.

Some Linux distros use plain GRUB naming, some use GRUB 2.
For example, Ubuntu has the _/boot/grub/_ directory and _grub-_
_mkconfig_ command, and Fedora calls them _/boot/grub2/_ and _grub2-_
_mkconfig_ . Check your filepaths and names. In this chapter I use the
Ubuntu naming scheme, except in distro-specific examples.

Starting a computer hasn’t changed all that much since UNIVAC was first built, back
in the 1940s in the last millennium. Starting a computer is called _bootstrapping_, a ref‐
erence to “pulling yourself up by your own bootstraps,” which is impossible. The dif‐
ficulty with a programmable computer is it needs software instructions to tell it what
to do, but where will those instructions come from before the operating system is
loaded?

**37**

The solution for the modern x86_64 PC architecture is to store the initial startup
instructions on a chip on the motherboard and program the CPU with the address of
these instructions. You could say the CPU is hardwired to receive the startup instruc‐
tions. This address is the same on all x86_64 machines, and that is why you can mix
and match motherboards and CPUs. (This address is called the _reset vector_, if you feel
like doing some research.)

This is a simplified description of how it all works:

The first stage is launched when the system is powered up. The CPU fetches instruc‐
tions from the BIOS/UEFI firmware, and then initializes CPU caches and system
memory. When the system memory is initialized, the Power On Self-Test (POST)
runs, testing the memory and testing connectivity with other hardware such as key‐
board, mouse, display, and disk drives. You have probably noticed the LEDs on your
keyboard and mouse lighting up and heard the noises from inside your computer’s
case as your disk drives are probed.

After the POST, the BIOS/UEFI firmware launches the second stage of startup and
looks for the boot files on your hard disk. The GRUB bootloader loads the necessary
files to launch your operating system and complete system startup.

When your boot screen appears (Figure 2-1), GRUB waits a configured amount of
time for your input, usually 5–10 seconds, then boots the default if you do nothing.
Navigate the boot menu with your arrow keys. When you press any key, it stops the
countdown, and then you can explore your boot options at your leisure.

In Figure 2-1, the first entry boots the system. The next two entries open submenus
with more boot options. When you are exploring submenus, press the Esc key to get
back to the main menu.

Some Linux distros, such as Fedora and Ubuntu, do not display the boot screen when
there is only one installed operating system. In this case, press the Shift key at startup
to see the boot screen. There is a configuration option to always display the boot
screen.

You may wish to customize the appearance and behavior of your GRUB menu by
adjusting a few options in the GRUB configuration files.

If you prefer a graphical tool for customizing your GRUB menu, try GRUB Custom‐
izer (Figure 2-2). This is available in most Linux distributions as the _grub-customizer_
package, except openSUSE, which has a GRUB module (labeled Boot Loader) in the
YaST system configuration utility.

**38** **|** **Chapter 2: Managing the GRUB Bootloader**

_Figure 2-1. openSUSE GRUB boot screen_

_Figure 2-2. GRUB Customizer_

**Managing the GRUB Bootloader** **|** **39**

**2.1 Rebuilding Your GRUB Configuration File**

**Problem**

Whenever you change your GRUB configuration, you need to rebuild it.

**Solution**

The command to rebuild your GRUB configuration varies. On Fedora and open‐
SUSE, use this command:

```
  $ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Some distros, such as Ubuntu, use:

```
  $ sudo grub-mkconfig -o /boot/grub/grub.cfg
```

Ubuntu Linux also has a script that runs _grub-mkconfig_, _update-grub_ :

```
  $ sudo update-grub
```

**Discussion**

Some Linux distributions helpfully provide the correct command at the top of _/etc/_
_default/grub_ .

Remember to always verify your correct filenames and paths when you edit your
GRUB configuration because they vary on the different Linuxes.

**See Also**

 - Your motherboard documentation, to learn about your system’s BIOS/UEFI

 - [GNU GRUB Manual](https://oreil.ly/szAiR)

 - GRUB has multiple single-purpose man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

**2.2 Unhiding a Hidden GRUB Menu**

**Problem**

Your favorite Linux distribution hides the GRUB menu when you have only one
operating system installed on your computer, and you want it to appear every time
you boot up.

**40** **|** **Chapter 2: Managing the GRUB Bootloader**

**Solution**

Several Linux distros do this, including Ubuntu and Fedora. You can unhide your
GRUB menu temporarily by pressing and holding the Shift key at startup.

Edit _/etc/default/grub_ to unhide it permanently with the following options:

```
  GRUB_TIMEOUT="10"
  GRUB_TIMEOUT_STYLE=menu
```

If the lines `GRUB_HIDDEN_TIMEOUT=0` and `GRUB_HIDDEN_TIMEOUT_QUIET=true` are in
your file, comment them out.

After changing _/etc/default/grub_, rebuild your GRUB configuration (Recipe 2.1).

**Discussion**

`GRUB_HIDDEN_TIMEOUT=0` means do not display the GRUB menu, while
`GRUB_HIDDEN_TIMEOUT_QUIET=true` means do not display the countdown timer.

If you install another operating system in a multiboot configuration, then the GRUB
menu should unhide itself.

**See Also**

 - Recipe 2.1

 - [GNU GRUB Manual](https://oreil.ly/DqiwS)

 - GRUB has multiple single-purpose man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

**2.3 Booting to a Different Linux Kernel**

**Problem**

You are wondering about the extra entries in your GRUB menu that reference specific
Linux kernel versions, like in Figure 2-3. You want to know what they are for and
what to do with them.

**2.3 Booting to a Different Linux Kernel** **|** **41**

_Figure 2-3. GRUB kernel boot options_

**Solution**

Over time, as you update your Linux system, older Linux kernels are retained and
added to your GRUB menu. This provides an easy way to boot to a known good older
kernel if something goes awry with a newer kernel. You don’t have to keep the older
kernels and can remove them with your package manager.

**Discussion**

In olden times kernel updates were a big deal, because they often meant bug fixes,
additional support for hardware, such as video, network, and audio interfaces, and
support for software features, such as proprietary file formats and new protocols. The
rate of change was rapid, and it was not unusual for a new kernel to not work cor‐
rectly, so keeping the option to boot to an older kernel was routine. These days such
troubles are less common, and kernel updates are generally undramatic.

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/qxk2m)

 - [The Linux Kernel Archives](https://oreil.ly/l5xyK)

**42** **|** **Chapter 2: Managing the GRUB Bootloader**

**2.4 Understanding GRUB Configuration Files**

**Problem**

You know that configuring GRUB is done a little differently than most programs, and
you want to know where the GRUB configuration files are and which ones you use to
manage GRUB.

**Solution**

GRUB configuration files are in _/boot/grub/_, _/etc/default/grub_, and _/etc/grub.d/_ . The
GRUB configuration is complex, with many scripts and modules.

**GRUB versus GRUB 2**

Remember, as discussed in the introduction to this chapter, some
Linux distros use plain GRUB naming, and some use GRUB2 in
filenames and commands. In this chapter I use plain GRUB nam‐
ing, except in distro-specific examples.

_/etc/default/grub_ is for configuring the appearance of the GRUB menu you see at
startup, such as hiding or showing the boot menu, applying themes and background
images, menu timeout, and kernel options.

The files in _/etc/grub.d/_ support more complex configurations, and _/boot/grub/_ stores
image and theme files for customizing the appearance of your GRUB menu.

The main GRUB configuration file is _/boot/grub/grub.cfg_, which GRUB reads at
startup. You do not edit this file because it is built from _/etc/grub.d/_ and _/etc/default/_
_grub_ ; every time you make configuration changes you must rebuild the GRUB
configuration.

The GRUB configuration is automatically rebuilt when you install any updates that
affect the boot process, such as installing newer kernels and removing older kernels.

**Discussion**

If you are interested in scripting, studying the GRUB files is an excellent course in
organizing large numbers of interdependent scripts.

The files in _/etc/grub.d/_ are called _drop-in_ files. Rather than dealing with a giant single
configuration file, each drop-in file contains a configuration for a specific task. These
files are numbered in the order that GRUB should read them, with lower numbers
indicating higher priority. The following example is from Fedora 32:

```
  $ sudo ls -C1 /etc/grub.d/
  00_header

```

**2.4 Understanding GRUB Configuration Files** **|** **43**

```
  01_users
  08_fallback_counting
  10_linux
  10_reset_boot_success
  12_menu_auto_hide
  20_linux_xen
  20_ppc_terminfo
  30_os-prober
  30_uefi-firmware
  40_custom
  41_custom
  backup
  README
```

Each of these files is a script, and each must have the executable bit set. You can dis‐
able any of them by clearing the executable bit, like this:

```
  $ sudo chmod -x 20_linux_xen
```

Re-enable a script by adding the executable bit:

```
  $ sudo chmod +x 20_linux_xen
```

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/RWh6k)

 - GRUB has numerous man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

 - Chapter 6

**2.5 Writing a Minimal GRUB Configuration File**

**Problem**

You want to write the most minimal working GRUB configuration.

**Solution**

This is the most basic _/etc/default/grub_ file, with only the necessary entries to boot a
Linux system and show the GRUB menu. The following example is for openSUSE
Leap 15.2:

```
  # If you change this file, run 'grub2-mkconfig -o /boot/grub2/grub.cfg'
  # afterwards to update /boot/grub2/grub.cfg.

  GRUB_DEFAULT=0
  GRUB_TIMEOUT=10
  GRUB_TIMEOUT_STYLE=menu

```

**44** **|** **Chapter 2: Managing the GRUB Bootloader**

Remember Figure 2-1? Figure 2-4 is the same system, but with a minimal GRUB
configuration.

_Figure 2-4. Minimal GRUB menu_

There are more options you can try, such as different ways to set the default boot
option, change background images and themes, change the colors, and change the
screen resolution. See the Discussion to learn about these.

**Discussion**

There are numerous options you can use in _/etc/default/grub_, and you can ignore
most of them. These are the options that I think are the most useful:

```
GRUB_DEFAULT=
```

Sets the default boot entry. The boot entries are counted from 0 in _grub.cfg_, but
not numbered. How do you know what numbers each boot option has? There is
no obvious way to figure this out; you have to count your boot options manually.
Count the “menuentry” sections to figure out the numbering. A menu entry
looks like this:

```
    menuentry 'openSUSE Leap 15.2' --class opensuse --class gnu-linux
    --class gnu --class os
    menuentry_id_option 'gnulinux-simple-102a6fce-8985-4896-a5f9-e5980cb21fdb' {
    load_video
    set gfxpayload=keep
    insmod gzio
    [...]
```

Or use the _awk_ command to list them for you, like this example for Ubuntu
20.04:

**2.5 Writing a Minimal GRUB Configuration File** **|** **45**

```
    $ sudo awk -F\' '/menuentry / {print i++,$2}' /boot/grub/grub.cfg
    0 Ubuntu
    1 Ubuntu, with Linux 5.8.0-53-generic
    2 Ubuntu, with Linux 5.8.0-53-generic (recovery mode)
    3 Ubuntu, with Linux 5.8.0-50-generic
    4 Ubuntu, with Linux 5.8.0-50-generic (recovery mode)
    5 UEFI Firmware Settings
```

You probably don’t want to use a recovery mode entry as the default, or a mem‐
ory test, though it doesn’t hurt anything if you do. UEFI Firmware Settings is a
shortcut to your system’s BIOS/UEFI.

```
GRUB_TIMEOUT=10
```

Sets the number of seconds the GRUB menu waits before booting the default,
and `GRUB_TIMEOUT_STYLE=menu` displays the menu during the countdown.
`GRUB_TIMEOUT=0` boots immediately without displaying the menu, and
`GRUB_TIMEOUT=-1` disables automatic booting and waits for the user to select a
boot entry.

```
GRUB_DEFAULT=saved
```

Together with `GRUB_SAVEDEFAULT=true`, `GRUB_DEFAULT=saved` makes the last
menu entry that you booted the default for the next boot.

```
GRUB_CMDLINE_LINUX=
```

Adds Linux kernel options for all menu entries.

```
GRUB_CMDLINE_LINUX_DEFAULT=
```

Passes kernel options only to the default menu entries. `GRUB_CMDLINE_LIN`
`UX_DEFAULT="quiet splash"` is a common default option that disables the ver‐
bose output at startup and displays a graphical splash screen. Figure 2-5 shows
what the verbose output looks like. If you have `GRUB_CMDLINE_LINUX_DEF`
`AULT="quiet splash"` configured, you can see this output without changing
your configuration by pressing the Esc key during startup.

```
GRUB_TERMINAL=gfxterm
```

Sets the your GRUB screen to a graphical mode that supports colors and images.
`GRUB_TERMINAL=console` disables graphical mode.

```
GRUB_GFXMODE=
```

Sets the screen resolution for the graphical mode, for example,
`GRUB_GFXMODE=1024x768` . Run the _set pager=1_ command, and then run _videoinfo_
from your GRUB command line to see your supported modes (Figure 2-6). _set_
_pager=1_ lets you use the arrow keys to page up and down long command output.
`GRUB_GFXMODE=auto` calculates a reasonable default.

**46** **|** **Chapter 2: Managing the GRUB Bootloader**

_Figure 2-5. Startup messages_

_Figure 2-6. Supported video modes_

**2.5 Writing a Minimal GRUB Configuration File** **|** **47**

```
GRUB_BACKGROUND=
```

Sets a background image on the GRUB menu, using the image of your choice
(see Recipe 2.6).

```
GRUB_THEME=
```

Decorates your GRUB menu with a complete theme (see Recipe 2.8).

**See Also**

 - Recipe 2.6

 - Recipe 2.8

 - [GNU GRUB Manual](https://oreil.ly/zIbDg)

 - GRUB has multiple single-purpose man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

**2.6 Setting a Custom Background for Your GRUB Menu**

**Problem**

You don’t care for the appearance of your GRUB menu, and you want to pretty it up.

**Solution**

You need an image in PNG, 8-bit JPG, or TFA format. It can be any size, and GRUB
will scale it to fit. In the following example, a photo of Duchess enjoying the book‐
shelves graces our GRUB menu.

Copy your image to _/boot/grub/_, and add the full filepath of your image to _/etc/_
_default/grub_ . The photo of Duchess is _/boot/grub/duchess-books.jpg_ :

```
  GRUB_BACKGROUND="/boot/grub/duchess-books.jpg"
```

If there is a `GRUB_THEME=` line, make sure it is commented out, then rebuild your
GRUB configuration (Recipe 2.1).

You should see a line like “Found background: /boot/grub/duchess-books.jpg” in the
output of your rebuild command. If you do not see this, there is an error in your con‐
figuration.

When it looks correct, rebuild, reboot, and enjoy your new GRUB menu background
(Figure 2-7).

**48** **|** **Chapter 2: Managing the GRUB Bootloader**

_Figure 2-7. Duchess the literacy cat gracing the GRUB menu_

The fonts in the example are barely readable, so jump ahead to Recipe 2.7 to learn
how to change their colors.

**Discussion**

You may use any image on your system; it does not have to be in _/boot/grub/_ . Putting
your image files in _/boot/grub/_ keeps all your GRUB customizations in one place and
makes them available to all installed Linux systems on a multiboot setup.

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/xv9AE)

 - GRUB has multiple single-purpose man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

**2.7 Changing Font Colors in the GRUB Menu**

**Problem**

Your new background is lovely (Figure 2-7), but your fonts are barely visible, and you
need to change the colors so you can read your GRUB menu.

**2.7 Changing Font Colors in the GRUB Menu** **|** **49**

**Solution**

This is fun because you can quickly preview colors from the GRUB command line.
Then, when you know what colors you want, edit _/etc/default/grub_ and create a new
file in _/etc/grub.d/_ to load your colors, then rebuild _/boot/grub/grub/cfg_ . Reboot to
enjoy your background image with pretty colored fonts.

Start up your computer, and when the GRUB menu appears, press C to open the
GRUB command line (Figure 2-8).

_Figure 2-8. The GRUB command line_

The following two commands set the colors in Figure 2-9:

```
  grub> menu_color_highlight=cyan/blue
  grub> menu_color_normal=yellow/black

```

_Figure 2-9. Setting GRUB menu colors from the GRUB command line_

**50** **|** **Chapter 2: Managing the GRUB Bootloader**

You may set and test each color pair one pair at a time. From the GRUB menu, press
C to open the GRUB command shell. Type your command (sorry, no copy-paste),
press Enter, then press Esc to return to the menu to see how it looks. You can list your
previous commands with the up and down arrow keys, and edit and reuse them
rather than retyping everything.

You must specify two colors in this order: foreground/background. All the colors are
solid, with no transparency, with one exception: when you select _black_ as a back‐
ground color it is transparent. That is why `menu_color_normal=` must have black as
the background color, when you have a background image. If you use any other color,
your image will be covered by the background color. The `menu_color_highlight=`
background color only applies to whatever line is currently selected.

When you figure out your colors, make them permanent. Boot up and create a new
script in _/etc/grub.d/_ . In the following example, it is called _07_font_colors_ . Copy this
exactly:

```
  #!/bin/sh

  if [ "x${GRUB_BACKGROUND}" != "x" ] ; then
  if [ "x${GRUB_COLOR_NORMAL}" != "x" ] ; then
  echo "set color_normal=${GRUB_COLOR_NORMAL}"
  fi

  if [ "x${GRUB_COLOR_HIGHLIGHT}" != "x" ] ; then
  echo "set color_highlight=${GRUB_COLOR_HIGHLIGHT}"
  fi
  fi
```

Then make it executable:

```
  $ sudo chown +x 07_font_colors
```

Now add these lines to your _/etc/default/grub_ file, using your colors:

```
  export GRUB_COLOR_NORMAL="yellow/black"
  export GRUB_COLOR_HIGHLIGHT="cyan/blue"
```

Rebuild your GRUB configuration (Recipe 2.1) and reboot to see if it worked.

**Discussion**

See Recipe 2.4 to learn about the files in _/etc/grub.d/_ and why the filenames must start
with numbers. In my experience it doesn’t matter if your fonts script starts early or
late, but if it doesn’t work for you, try changing the priority. Make sure it is exe‐
cutable. The options are as follows:

**2.7 Changing Font Colors in the GRUB Menu** **|** **51**

 - _menu_color_highlight_ controls the colors of the highlighted lines inside the menu
box.

 - _menu_color_normal_ controls the colors of the not-highlighted lines.

Use these colors exactly as they are written in Table 2-1, all lowercase and with this
exact spelling.

_Table 2-1. GRUB color options_

**<mark>Color options</mark>**
black dark-gray light-green magenta
blue green light-gray red
brown light-cyan light-magenta white
<u>cyan</u> <u>light-blue</u> <u>light-red</u> <u>yellow</u>

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/BZHWt)

 - GRUB has multiple single-purpose man pages; run _man -k grub_ to see all of them

 - _info grub_ or _info grub2_

 - Recipe 2.4

**2.8 Applying a Theme to Your GRUB Menu**

**Problem**

You like prettying up your GRUB menu, and you want to know if there are themes
for the GRUB menu and how to install them.

**Solution**

You are in luck, for there are many themes for GRUB. Start by using your package
manager with the **`grep`** command to search for package names. This example is for
Ubuntu Linux:

```
  $ apt search theme | grep grub
```

Using _theme | grep grub_ to filter your results will find all relevant packages, like _grub-_
_theme-breeze_, _grub2-themes-ubuntu-mate_, and _grub-breeze-theme_ . Install themes just
as you would any package.

**52** **|** **Chapter 2: Managing the GRUB Bootloader**

**Discussion**

Your new theme should be installed in _/boot/grub/themes_ . Find your new theme, for
example _/boot/grub/themes/ubuntu-mate_, and look for the _theme.txt_ file. Enter the full
path in _/etc/default/grub_, like this example for the _ubuntu-mate_ theme:

```
  GRUB_THEME=/boot/grub/themes/ubuntu-mate/theme.txt
```

Be sure to comment out any other configuration lines pertaining to appearance that
you may have, such as `GRUB_BACKGROUND=`, any custom font colors, and any other
themes. Then rebuild your GRUB configuration (Recipe 2.1). You should see a line
like “Found theme: /boot/grub/themes/ubuntu-mate/theme.txt” in your command
output.

If all goes well, reboot and you will be rewarded with a screen like Figure 2-10. If it
does not display correctly, recheck your configuration and commands.

_Figure 2-10. The Ubuntu MATE GRUB theme_

**See Also**

 - [GNOME Themes](https://oreil.ly/oLJtx)

 - [KDE Themes](https://oreil.ly/SLdkp)

 - [GNU GRUB Manual](https://oreil.ly/LeIHu)

**2.8 Applying a Theme to Your GRUB Menu** **|** **53**

**2.9 Rescuing a Nonbooting System from the**
**grub> Prompt**

**Problem**

When you start your system, it stops at a GRUB prompt, `grub>`, and does not boot.
You need to know how to boot your system and then repair your configuration.

**Solution**

When the boot process stops at the `grub>` prompt (Figure 2-11), this means it
found _/boot/grub/_ but cannot find the root filesystem.

_Figure 2-11. The GRUB command shell_

You need to find the root filesystem, the Linux kernel, and its matching _initrd_ file.
When you are in the GRUB command shell, the entire filesystem is open to you.

The first command you should run is to invoke the pager, so that you can page up
and down long output:

```
  grub> set pager=1
```

List your disks and partitions. GRUB has its own way of identifying hard disks and
partitions. It numbers disks from 0, partitions from 1, and labels all hard disks as _hd_ .
On a running Linux system, hard disks are identified as _/dev/sda_, _/dev/sdb_, and so on.

In the following example, GRUB lists two hard disks, _hd0_ and _hd1_, which are the
same as _/dev/sda_ and _/dev/sdb_ . _hd0,gpt5_ is the same as _/dev/sda5_, and _hd1,msdos1_ is
the same as _/dev/sdb1_ :

```
  grub> ls
  (hd,0) (hd0,gpt5) (hd0,gpt4) (hd0,gpt3) (hd0,gpt2) (hd0,gpt1)
  (hd1) (hd1,msdos1)
```

This output shows that _hd0_ has a _gpt_ partition table, and _hd1_ has the old-fashioned
_msdos_ partition table. It is not necessary to use the _gpt_ and _msdos_ labels when you are
listing partitions and files.

GRUB tells you the filesystem types, universally unique identifiers (UUIDs), and
other information on the partitions:

**54** **|** **Chapter 2: Managing the GRUB Bootloader**

```
  grub> ls (hd0,3)
  Partition hd0,3: filesystem type ext* - Last modification time 2021-12-29
  01:17:58 Tuesday, UUID 5c44d8b2-e34a-4464-8fa8-222363cd1aff - Partition start
  at 526336KiB   Total size 20444160KiB
```

You need to find _/boot_ . Suppose you remember that it is in the root filesystem on the
second partition; start looking there. A forward slash following the partition name
means list all files and directories on the partition:

```
  grub> ls (hd0,2)/
  bin  dev home lib64  media opt  root sbin sys usr
  boot etc lib  lost+found mnt  proc run  srv  tmp var
```

All boot files are in the _/boot_ directory:

```
  grub> ls (hd0,2)/boot
  efi/ grub/ System.map-5.3.18-lp152.57-default config-5.3.18-lp152.57-default
  initrd-5.3.18-lp152.57-default vmlinuz vmlinuz-5.3.18-lp152.57-default
  sysctl.conf-5.3.18-lp152.57-default vmlinux-5.3.18-lp152.57-default.gz
```

Everything you need to boot your system is there. Set the root filesystem partition,
kernel, and initrd image:

```
  grub> set root=(hd0,2)
  grub> linux /boot/vmlinuz-5.3.18-lp152.57-default root=/dev/sda2
  grub> initrd /boot/initrd-5.3.18-lp152.57-default
  grub> boot

```

**Tab Completion**

Just like the Bash shell, the GRUB command shell supports tab
completion. This means you can start typing _/boot/vml_, for exam‐
ple, then press the Tab key to autocomplete the line, or display a list
of possibilities.

If there are multiple _vmlinuz_ and _initrd_ files, use the two with the newest matching
version numbers. If all the commands are correct, your system will boot and you can
fix your GRUB configuration (Recipe 2.11).

**Discussion**

When _/boot_ is in its own partition, you won’t see any other directories because it is
not in the root filesystem.

_vmlinuz-5.3.18-lp152.57-default_ is the compressed Linux kernel.

_initrd-5.3.18-lp152.57-default_ is the initial ramdisk, a temporary root filesystem used
only to start up your system.

**2.9 Rescuing a Nonbooting System from the grub> Prompt** **|** **55**

Boot failures are caused by corrupted files; adding, removing, or moving hard disks;
installing or removing operating systems; or repartitioning. If you can’t get to
a GRUB prompt, see Chapter 19 to learn how to rescue your system with
SystemRescue.

You can practice using the `grub>` shell by pressing C when your GRUB menu appears.
This is safe because changes you make do not survive a reboot.

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/8SdwS)

**2.10 Rescuing a Nonbooting System from the grub**
**rescue> Prompt**

**Problem**

When you start your system, it stops at a GRUB prompt, `grub rescue>`, and does not
boot. You need to know how to boot your system and then repair your configuration.

**Solution**

The `grub rescue>` prompt (Figure 2-12) is the rescue shell, which means GRUB
could not find _/boot_ . Not to worry, you can find it from the GRUB prompt, boot your
system, and then make a permanent fix.

_Figure 2-12. The GRUB rescue shell_

List your partitions:

```
  grub rescue> ls
  (hd0) (hd0,gpt5) (hd0,gpt4) (hd0,gpt3) (hd0,gpt2) (hd0,gpt1)
  (hd1) (hd1, msdos1)
```

At this point there is no tab-completion or paging, so you have to type everything.

**56** **|** **Chapter 2: Managing the GRUB Bootloader**

GRUB tells you the filesystem types, UUIDs, and other information on the partitions:

```
  grub rescue> ls (hd0,3)
  Partition hd0,3: filesystem type ext* - Last modification time 2021-12-29
  01:17:58
  Tuesday, UUID 5c44d8b2-e34a-4464-8fa8-222363cd1aff - Partition start at
  526336KiB   Total size 20444160KiB
```

If you don’t know which partition contains _/boot_, you will have to list the files and
directories in each one until you find it. You do not have to use the _gpt_ and _msdos_
labels. A forward slash following the device name means list all files and directories:

```
  grub rescue> ls (hd0,2)/
  bin  dev home lib64  media opt  root sbin sys usr
  boot etc lib  lost+found mnt  proc run  srv  tmp var
```

Hurrah, there it is in the root filesystem. List the files in _/boot_ :

```
  grub rescue> ls (hd0,2)/boot
  efi/ grub/ System.map-5.3.18-lp152.57-default config-5.3.18-lp152.57-default
  initrd-5.3.18-lp152.57-default vmlinuz vmlinuz-5.3.18-lp152.57-default
  sysctl.conf-5.3.18-lp152.57-default vmlinux-5.3.18-lp152.57-default.gz
```

There are a few additional commands for `grub rescue>` . You have to tell it
where _/boot/grub_ is, and then load the _normal_ and _linux_ kernel modules, which are
in _/boot/grub/i386-pc_ (along with many other kernel modules that GRUB uses at
startup). _normal_ changes the boot mode from rescue to normal, and _linux_ starts the
system loader:

```
  grub rescue> set prefix=(hd0,2)/boot/grub
  grub rescue> set root=(hd0,2)
  grub rescue> insmod normal
  grub rescue> insmod linux
```

After loading _normal_ and _linux_, you have tab completion. You could also turn on pag‐
ing, _set pager=1_, to enable using the arrow keys to scroll to your previous commands.
Now tell GRUB where to find the _kernel_ and _initrd_ file:

```
  grub> linux /boot/vmlinuz-5.3.18-lp152.57-default root=/dev/sda2
  grub> initrd /boot/initrd-5.3.18-lp152.57-default
  grub> boot
```

If there are multiple _vmlinuz_ and _initrd_ files, use the two with the newest matching
version numbers. If all the commands are correct, your system will boot and you can
fix your GRUB configuration (Recipe 2.11).

**Discussion**

When _/boot_ is on its own partition, you won’t see any other directories because it is in
its own filesystem.

**2.10 Rescuing a Nonbooting System from the grub rescue> Prompt** **|** **57**

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/6REHG)

**2.11 Reinstalling Your GRUB Configuration**

**Problem**

You were able to boot your system from the GRUB prompt, and now you need to
know how to make a permanent repair.

**Solution**

Check your GRUB configuration carefully for errors. When it looks correct, rebuild
your GRUB configuration (Recipe 2.1). Then you need to reinstall GRUB. In the fol‐
lowing example, it is reinstalled to _/dev/sda_ :

```
  $ sudo grub-mkconfig -o /boot/grub/grub.cfg
  $ sudo grub-install /dev/sda

```

**Using the Correct Rebuild Command**

As discussed in Recipe 2.1 and “GRUB versus GRUB 2” on page 37,
you must check your filepaths to ensure you are using the correct
rebuild command.

Be sure to install it to the correct disk, if you have more than one, and use only the
device name (for example, _/dev/sda_ ) and not a partition (such as _/dev/sda1_ ).

**Discussion**

Be sure to have good current backups. If your rescue efforts fail, try reinstalling
GRUB from SystemRescue (Recipe 19.9).

**See Also**

 - [GNU GRUB Manual](https://oreil.ly/zkwke)

 - Chapter 19

**58** **|** **Chapter 2: Managing the GRUB Bootloader**

**<u>CHAPTER 3</u>**
#### **Starting, Stopping, Restarting, and** **Putting Linux into Sleep Modes**

In this chapter you will learn several ways to stop, start, and restart a Linux system,
and how to manage sleep modes. You will learn both the legacy commands and the
new systemd commands.

You will also learn how to set up automated startups and shutdowns. An automated
shutdown is nice to remind you to stop working, and you don’t have to remember to
shut off your computer for the night. You can set up automated wake-ups and shut‐
downs on a remote machine, so that you can access it during work hours without
leaving it running all the time. If your users are watt wasters who don’t shut off their
computers, you can configure them to shut down during off hours.

The “three-key salute,” Ctrl-Alt-Delete, is useful when you need to interrupt a startup
and reboot, or reboot when a process or application is misbehaving. In graphical
desktops you can remap the keys to a more convenient key combination.

There are a number of legacy shutdown commands that have accumulated over the
decades, with a lot of overlapping functionality: _shutdown_, _halt_, _poweroff_, and _reboot_ .
The _shutdown_ command provides the useful options of timed shutdowns, with warn‐
ings to all logged-in users. These commands are useful in scripts, in SSH sessions,
and anytime you are working from the command line.

**59**

**Root Privileges Not Always Required**

In olden times, root privileges were needed to run the shutdown
commands. This is changing, and on many modern Linux distribu‐
tions, root privileges are not needed for these commands. The
examples in this chapter are for normal, unprivileged users. If your
particular Linux requires root permissions, it will tell you.

These permissions are controlled by Polkit (formerly PolicyKit) on
modern Linux distributions. See _man 8 polkit_ to learn more.

But that’s not all, because in Linux distributions with systemd (Chapter 4), the classic
old commands are not installed on the system. Intead, their names are symlinked to
the _systemctl_ command. You can see this with the _stat_ command, like this example for
_shutdown_ :

```
  $ stat /sbin/shutdown
  File: /sbin/shutdown -> /bin/systemctl
  Size: 14       Blocks: 0     IO Block: 4096  symbolic link
  Device: 802h/2050d   Inode: 1177556   Links: 1
  Access: (0777/lrwxrwxrwx) Uid: ( 0/ root)  Gid: ( 0/ root)
```

The `File:` line displays a symbolic link to _/bin/systemctl_ . All of the legacy command
names, _/sbin/shutdown_, _/sbin/halt_, _/sbin/poweroff_, and _/sbin/reboot_, are symlinked
to _/bin/systemctl_ . The symlinks for the legacy command names are provided for back‐
ward compatibility. On Linux systems without systemd these symlinks do not exist,
and these systems use the legacy executables.

On some Linux distros these symlinks are in _/usr/sbin_ rather than _/sbin_ . When you
use the legacy command names, they behave the same way on systems with systemd
and on systems without systemd.

The power buttons on your graphical desktop are configurable; you should be able to
customize which buttons are visible and their location.

**3.1 Shutting Down with systemctl**

**Problem**

You want to use the _systemctl_ commands to shut down and reboot your system.

**Solution**

Halt the system and power off the machine:

```
  $ systemctl poweroff

```

**60** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

Another way to halt the system and power off the machine:

```
  $ systemctl shutdown
```

Reboot:

```
  $ systemctl reboot
```

Halt the system without powering off the machine:

```
  $ systemctl halt
```

**Discussion**

The _systemctl_ shutdown commands do not have the many options that the legacy
commands do, which does not matter all that much because there are a lot of redun‐
dant options in the legacy commands. There is one significant difference: _systemctl_
_shutdown_ lacks the timed shutdown options supported by the _shutdown_ command
(see Recipe 3.2).

**See Also**

 - _man 8 systemd-halt.service_

**3.2 Shutting Down, Timed Shutdowns, and Rebooting**
**with the shutdown Command**

**Problem**

You want to use timed shutdowns, for example, 10 minutes from now or at a specific
time, and warn all logged-in users. Or you want to just shut down now with no frills.

**Solution**

The _shutdown_ command works the same way, whether it is symlinked to _systemctl_ or
the legacy _shutdown_ executable.

The following examples show how to shut down immediately, shut down a certain
number of minutes from now, cancel a shut down, shutdown at a specific time, halt,
and reboot.

Shut down immediately, with no notification to other logged-in users:

```
  $ shutdown -h now

```

**3.2 Shutting Down, Timed Shutdowns, and Rebooting with the shutdown Command** **|** **61**

Shut down in 10 minutes with notifications:

```
  $ shutdown -h +10
  Shutdown scheduled for Sun 2021-05-23 11:04:43 PDT, use 'shutdown -c' to cancel.
```

Other users on the system may see this message, depending on which Linux they are
using, and if they have a terminal open:

```
  Broadcast message from duchess@client4 on pts/4 (Sun 2021-05-24 10:54:43 PDT):

  The system is going down for poweroff at Sun 2021-05-24 11:04:43 PDT!
```

Cancel the shutdown:

```
  $ shutdown -c
```

Logged-in users may see this message:

```
  Broadcast message from duchess@client4 on pts/4 (Sun 2021-05-24 10:56:00 PDT):

  The system shutdown has been cancelled
```

Create your own message:

```
  $ shutdown -h +6 "Time to stop working and go outside to play!"
```

Rather than specifying minutes to shutdown, you may set a shutdown time in 24hour hh:mm format. The following example shuts down the system at 10:15 P.M.:

```
  $ shutdown -h 22:15
```

Reboot:

```
  $ shutdown -r
```

Halt the system without powering off:

```
  $ shutdown -H
```

Running _shutdown_ with no options is equivalent to _shutdown -h +1_ .

**Discussion**

_shutdown_ sends messages only when you use the _-h_ option, except for the _-h now_
option, and when you use the _-k_ option. These are called _wall_ messages, which is
short for “write to all logged-in users.” Linux distributions vary in their support of
this feature, so other users on your particular Linux may not see these messages.

 - _--help_ displays a summary of options.

 - _-H_, _--halt_ performs a clean shutdown but does not power off the machine; you
must press and hold the power button to power off your machine.

 - _-P_, _--poweroff_ performs a clean shutdown and powers off the machine.

 - _-r_, _--reboot_ performs a clean shutdown and reboots the machine.

**62** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

 - _-k_ sends a wall message without shutting down the machine.

 - _--no-wall_ disables wall messages.

**See Also**

 - _man 8 shutdown_

 - _man 1 wall_

 - _man 8 systemd-halt.service_

**3.3 Shutting Down and Rebooting with halt, reboot,**
**and poweroff**

**Problem**

You understand the _shutdown_ command, and now you want to know what _halt_,
_reboot_, and _poweroff_ are for, and how to use them.

**Solution**

These are all pretty much the same.

_halt_ performs a clean shutdown, stopping all services and processes and unmounting
filesystems, but it does not power off the machine. After the _halt_ command is fin‐
ished, you must press and hold the machine’s power button to complete the shut‐
down.

_reboot_ performs a clean shutdown and restarts the system.

_poweroff_ performs a clean shutdown and powers off the machine:

```
  $ halt
  $ reboot
  $ poweroff
```

The _halt_ and _poweroff_ commands can reboot the system:

```
  $ halt --reboot
  $ poweroff --reboot
```

**Discussion**

If you’re thinking this all looks a little weird and redundant, you’re right. As software
ages, cruft accumulates and never goes away. Linux has been around since 1991, and

**3.3 Shutting Down and Rebooting with halt, reboot, and poweroff** **|** **63**

started out as a free clone of Unix, which was born in 1969. That is a lot of years for
the various contributors to tweak code and add their own favorite features.

_halt_ and _poweroff_ are the same commands and support the same options:

 - _--help_ displays a summary of options.

 - _--halt_ performs a clean shutdown but does not power off the machine (yes, _halt_
and _halt --halt_ do the same thing).

 - _-p_, _--poweroff_ performs a clean shutdown and powers off the machine (yes, _pow‐_
_eroff_ and _poweroff --poweroff_ do the same thing) .

 - _--reboot_ performs a clean shutdown and restarts the machine.

 - _-f_, _--force_ forces an immediate halt or poweroff. Shutdown of all running services
is skipped, all processes are killed, and all filesystems are unmounted or mounted
read-only. Run it twice to force an unclean shutdown; for example, _poweroff -f -f_,
which you should use only when normal shutdown commands fail.

 - _-w_, _--wtmp-only_ does not perform a shutdown, but only writes an entry
in _/var/log/wtmp_ .

 - _-d_, _--no-wtmp_ prevents writing a _wtmp_ entry.

**See Also**

 - _man 8 halt_

 - _man 8 poweroff_

 - _man 8 systemd-halt.service_

**3.4 Sending Your System into Sleep Modes with systemctl**

**Problem**

Your Linux system has systemd, and you want to use _systemctl_ to manage system
sleep modes.

**Solution**

_systemctl_ provides these power saving modes: _suspend_, _hibernate_, _hybrid-sleep_, and
_suspend-then-hibernate_ .

Put your system into suspend mode:

```
  $ systemctl suspend

```

**64** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

This stores your current session in RAM and puts all hardware into a suspended
state. Wake your system up by pressing any key, moving the mouse, or opening your
laptop lid.

Put your system into hibernate mode:

```
  $ systemctl hibernate
```

This stores your session on disk and powers off the machine. Wake it up by pressing
the power button, and when it resumes, which can take a minute or two, your session
will be restored where you left off.

Put your system into hybrid-sleep mode:

```
  $ systemctl hybrid-sleep
```

This suspends your system to both memory and disk, and shuts off all devices except
RAM. If your system RAM loses power, the system resumes from disk. Wake it up by
pressing the power button.

Put your system into suspend-then-hibernate mode:

```
  $ systemctl suspend-then-hibernate
```

_suspend-then-hibernate_ first goes into suspend mode, then enters hibernation after
the period of time specified by the HibernateDelaySec= setting in _/etc/systemd/_
_sleep.conf_ . Wake it up by pressing the power button.

**Discussion**

See the Discussion in Recipe 3.9 for details on the different sleep states.

Your graphical desktop should have buttons for entering power saving modes and a
graphical configuration tool for controlling events such as screen blanking, screen
locking, power button, mouse, and laptop lid actions such as entering a sleep state or
powering off.

Power management tends to work best on laptops and may not behave as expected on
your Linux distribution. Power management is affected by your UEFI, CPU capabili‐
ties, udev, Advanced Configuration and Power Interface (ACPI), kernel compilation
options, and possibly other devices and programs; so much depends on how your
particular Linux has implemented power management. Check your Linux distribu‐
tion documentation.

**See Also**

 - _man 1 systemctl_

 - _man 8 systemd-halt.service_

**3.4 Sending Your System into Sleep Modes with systemctl** **|** **65**

**3.5 Rebooting Out of Trouble with Ctrl-Alt-Delete**

**Problem**

You want a reliable method of rebooting that always works, even when you are having
problems such as crashes and runaway processes.

**Solution**

The good old “three-key salute,” Ctrl-Alt-Delete, was made for this. Press and hold
these three keys in sequence, and they will override most problems and reboot your
system. Ctrl-Alt-Delete is disabled in some Linux distributions, and you can change
this.

Ctrl-Alt-Delete is controlled by systemd in the Linux console. See Recipe 3.6 to learn
about managing Ctrl-Alt-Delete in systemd.

For systems without systemd, see the Discussion in this recipe.

Graphical environments have their own configuration tools for Ctrl-Alt-Delete, inde‐
pendent of systemd. For example, there is a keyboard configuration module in the
Xfce4 Settings Manager (Figure 3-1); in GNOME, use the Keyboard Settings module
in the GNOME Settings utility.

_Figure 3-1. Settings → Keyboard → Applications, configuring keyboard shortcuts in_
_Xubuntu_

**66** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

If you prefer a different key combination, use any keys you want. You could even use
a single key, though that risks rebooting with an accidental key press.

**Discussion**

On Linux systems that do not use systemd, Ctrl-Alt-Delete is controlled by the _/etc/_
_inittab_ file. This example, from MX Linux, shows a typical configuration:

```
  # What to do when CTRL-ALT-DEL is pressed.
  ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
```

_12345_ makes it active in runlevels 1, 2, 3, 4, and 5. _-t1_ means wait one second, _-a_
calls _/etc/shutdown.allow_, and _-r_ is reboot. Configure it to power off the system with
the _-h_ option, just like running _shutdown_ from the command line (see Recipe 3.2). To
disable Ctrl-Alt-Delete, comment out the line with the _shutdown_ command.

Note that _-t1_ and _-a_ are not present in all _shutdown_ command implementations. The
preceding example is from MX Linux. MX Linux supports both the Unix System V
initialization system (SysV init) and systemd, and you select the one you want to use
from the boot menu.

Ctrl-Alt-Delete is coded into the IBM PC BIOS/UEFI, and it should always reboot a
system before the operating system is launched, up to the moment before GRUB
launches the operating system.

Ctrl-Alt-Delete was created by IBM engineer David Bradley for the IBM PC BIOS.
Orignally it was a developer tool and not intended for users. It required two hands by
design, to make it difficult to press by accident.

Then Microsoft adopted it to bring up the Task Manager on the first press, and to
reboot on the second press. Then in Windows NT it was used to access the Windows
login screen. Supposedly this was a security measure that prevented users from being
deceived by fake login screens, which I never knew was a risk, but that was a long
time ago. There is a funny exchange about the invention and use of Ctrl-Alt-Delete
between Mr. Bradley and Bill Gates preserved in a YouTube video, which hopefully
[will stay up forever: “Control-Alt-Delete: David Bradley & Bill Gates”.](https://oreil.ly/e83k6)

**See Also**

 - _man 7 systemd.special_

**3.5 Rebooting Out of Trouble with Ctrl-Alt-Delete** **|** **67**

**3.6 Disabling, Enabling, and Configuring Ctrl-Alt-Delete in**
**the Linux Console**

**Problem**

systemd controls the behavior of Ctrl-Alt-Delete in the Linux console, and you want
to know how to manage it.

**Solution**

You can check the status, disable or enable Ctrl-Alt-Delete, or change it to power off
the system.

The Ctrl-Alt-Delete unit file is not a service, but a target, so it does not run as a dae‐
mon. If the _/etc/systemd/system/ctrl-alt-del.target_ symlink exists, Ctrl-Alt-Delete is
enabled.

The following example disables and masks _ctrl-alt-del.target_ :

```
  $ sudo systemctl disable ctrl-alt-del.target
  Removed /etc/systemd/system/ctrl-alt-del.target.

  $ sudo systemctl mask ctrl-alt-del.target
  Created symlink /etc/systemd/system/ctrl-alt-del.target → /dev/null.
```

Unmask and re-enable it:

```
  $ sudo systemctl unmask ctrl-alt-del.target
  Removed /etc/systemd/system/ctrl-alt-del.target.

  $ sudo systemctl enable ctrl-alt-del.target
  Created symlink /etc/systemd/system/ctrl-alt-del.target →
  /lib/systemd/system/reboot.target.
```

The changes take effect immediately.

Change it to power off the system by linking the _ctrl-alt-del.target_ unit to the _power‐_
_off.target_ unit. First, disable it to remove the existing symlink, then create the new
symlink:

```
  $ sudo systemctl disable ctrl-alt-del.target
  Removed /etc/systemd/system/ctrl-alt-del.target.

  $ sudo ln -s /lib/systemd/system/poweroff.target \
  /etc/systemd/system/ctrl-alt-del.target
```

Now it will power off the system instead of rebooting.

**68** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

**Discussion**

Use the _stat_ command to see symlinks:

```
  $ stat /lib/systemd/system/ctrl-alt-del.target
  File: /lib/systemd/system/ctrl-alt-del.target -> reboot.target
  Size: 13       Blocks: 0     IO Block: 4096  symbolic link
  Device: 802h/2050d   Inode: 136890   Links: 1
  Access: (0777/lrwxrwxrwx) Uid: ( 0/ root)  Gid: ( 0/ root)
```

You should not change any _/lib/systemd/system/_ links. Instead, create the new symlink
in _/etc/systemd/system/_ so that your change is not overwritten by system updates.

**See Also**

 - _man 7 systemd.special_

**3.7 Creating Scheduled Shutdowns with cron**

**Problem**

You want your machine to turn itself off at night so you can walk away and not worry
about it. Or, your users are careless watt wasters who refuse to develop the habit of
shutting their PCs down at night.

**Solution**

Use _cron_ to create scheduled shutdowns. For example, add this line to _/etc/crontab_ to
shut down every night at 10:30 P.M., with a 20-minute warning. Editing _/etc/crontab_
requires root permissions, and the following example uses the nano text editor:

```
  $ sudo nano /etc/crontab
  # m  h  dom mon dow  user  command
  10 22  *  *  *  root  /sbin/shutdown -h +20

```

Before doing this on your work computer, check your employer’s
policies. If they run updates and backups at night, then your com‐
puter may need to stay on.

This example runs only at 11 P.M. on weekdays and shuts down immediately:

```
  # m  h  dom mon dow  user  command
  00 23  *  * 1-5  root  /sbin/shutdown -h now

```

**3.7 Creating Scheduled Shutdowns with cron** **|** **69**

Another way is to use the _crontab_ command as root or with _sudo_ :

```
  $ sudo crontab -e
  # m  h   dom mon dow command
  00 23  *  *  1-5 /sbin/shutdown -h now
```

There is no name field when you run _crontab_, as there is in _/etc/crontab_ . The previous
example opens the root user’s crontab in edit mode. Edit and save, then you’re done.

Don’t try to name the file yourself. During editing it is a temporary file, which is auto‐
matically renamed by _crontab_ when you save it. It will be saved in _/var/spool/cron/_
_crontabs_ .

**Discussion**

_/etc/crontab_ has a name field, so any user can have entries in this file, but only root
can edit _/etc/crontab_ . Users who want to control their own personal crontabs should
use the _crontab_ command, as personal crontabs do not require root permissions.

The fields in _/etc/crontab_ can take a little getting used to (Table 3-1), so here are more
examples and explanations.

_Table 3-1. Table of crontab values_

**<mark>Field</mark>** **<mark>Allowed values</mark>**
minute 0-59

hour 0-23

day of month 1-31

month 1-12

day of week 0-7

The asterisk * is a wildcard for “all.”

Shut down only on weekends:

```
  # shutdown at 1:05 am Saturdays and Sundays
  00 01  * * 7,0  root /sbin/shutdown -h +5
```

There is a quirk in _cron_ that Sunday is 0 or 7. This dates back to very olden times, and
I have no idea why it persists. You’ll have to test it to see what works, so you may need
to use _6,7_ for Saturday, Sunday:

```
  00 01  * * 6,7  root /sbin/shutdown -h +5
```

It would be nice to use _sat,sun_, but you can only enter one day by name, and cannot
use names in lists. Days of the week and months are named with the first three letters:
sat, sun, jan, feb. Case does not matter.

You can use ranges: 1–4 means 1, 2, 3, and 4.

**70** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

Ranges and lists can be mixed: 1, 3, 5, 6-10.

Step values follow ranges:

 - 10–23/2 is every second hour in the range

 - */2 in the dow field means every other day

 - 2–6/2 equals 2, 4, 6

The following strings are nice shortcuts that replace the first five fields:

```
  @reboot
  @yearly
  @annually
  @monthly
  @weekly
  @daily
  @midnight
  @hourly
```

**See Also**

 - _man 8 cron_

 - _man 1 crontab_

 - _man 5 crontab_

**3.8 Scheduling Automated Startups with UEFI Wake-Ups**

**Problem**

Scheduled shutdowns are so wonderful, you want scheduled wake-ups as well.

**Solution**

You’re in luck, because Linux supports scheduled wake-ups. There are three methods
to try: Wake-on-LAN, real-time clock (RTC) wake-ups, or your computer’s UEFI
setup, if it has a scheduled wake-up feature.

UEFI wake-ups are the most reliable. Figure 3-2 shows the scheduled wake-up screen
on a Lenovo ThinkPad.

**3.8 Scheduling Automated Startups with UEFI Wake-Ups** **|** **71**

_Figure 3-2. Scheduling wake-ups in a Lenovo UEFI_

Enter your UEFI setup by pressing the appropriate F _n_ key at startup. On Dell, ASUS,
and Acer systems this is usually F2; Lenovo uses F1. This varies, however. For exam‐
ple, some systems use the Delete key, so check your machine’s documentation. Some
systems tell which key to press on their startup screens. It can be a bit tricky to press
the key at the right time, so start pressing it right after you press the power button,
just like banging on an elevator button to make it arrive faster.

If your system does not have a UEFI wake-up feature, try either Wake-on-LAN (see
Recipe 3.10, which requires a second device to send a wake-up signal), or RTC wakeups (see Recipe 3.9).

**Discussion**

Let’s discuss briefly what BIOS and UEFI mean. When you boot up your computer,
the first startup instructions come from the Basic Input Output System (BIOS), or the
Unified Extensible Firmware Interface (UEFI) firmware stored on the computer’s
motherboard. BIOS is the old legacy system that has been with us since 1980. UEFI is
its modern replacement. UEFI includes legacy BIOS support, though someday this
will be removed. Nearly all computers made after the mid-2000s have UEFI.

UEFI has considerably more features than the old BIOS, and is like a little operating
system. The UEFI setup screens control boot order, boot devices, security options,
Secure Boot, overclocking, displaying hardware health, networking, and many more
functions.

**72** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

**See Also**

 - Recipe 3.9

 - Recipe 3.10

 - Recipe 3.11

**3.9 Scheduling Automated Startups with RTC Wake-ups**

**Problem**

You want to set up scheduled wake-ups with RTC because your UEFI setup does not
have a scheduled wake-up feature, or because you just want to.

**Solution**

Use the _rtcwake_ command, which should already be present on your system from the
_util-linux_ package. _rtcwake_ stops and wakes your system. You may set it to wake up
your system after a specified interval, such as 1800 seconds from now, or at a sched‐
uled time and date.

Your system’s real-time clock (RTC) should be set to Coordinated Universal Time
(UTC).

When _rtcwake_ stops your system, it sends it into an ACPI sleep state. Look in _/sys/_
_power/state_ to see which sleep states your system supports. In the following example,
only three of the six ACPI sleep states are supported:

```
  $ cat /sys/power/state
  freeze mem disk
```

On non-systemd Linuxes, run _cat /proc/acpi/info_ .

In the above example, we have three sleep states to try. Test each one according to the
following example:

```
  $ sudo rtcwake -m freeze -s 60
```

_-m_ specifies the standby mode, and _-s_ is the number of seconds until the system starts
up again. When it is successful, you will see your system go into a sleep state, then
wake up, and you will see either a success message or an error message.

The following example does a dry run of scheduling a wake-up tomorrow at 8 A.M.:

```
  $ sudo rtcwake -n -m disk no -u -t $(date +%s -d "tomorrow 08:00")
  rtcwake: wakeup from "disk" using /dev/rtc0 at Mon Nov 23 08:00:00 2021
```

Remove _-n_ to disable the dry run and run it for real.

**3.9 Scheduling Automated Startups with RTC Wake-ups** **|** **73**

The following is a nice, simple _/etc/crontab_ example to automate shutdowns and
wake-ups. The _rtcwake_ command suspends to disk at 11 P.M. on weeknights and
wakes up 8 hours later:

```
  # m  h  dom mon dow  user  command
  00 23  *  * 1-5  root  /usr/sbin/rtcwake -m disk -s 28800
```

**Discussion**

Look in your system’s BIOS/UEFI to verify that your hardware clock is set to UTC. If
there is no button or some kind of setting to change the real-time clock to UTC,
change the time manually to the current UTC time.

The example that includes _-u -t +$(date +%s -d “tomorrow 08:00”)_ converts Unix
epoch time to human-readable values. Unix epoch time is the number of seconds
elapsed since midnight January 1, 1970 UTC. _date +%s_ reports the current Unix
epoch time. The _-t_ option passes Unix epoch time to _date_ for conversion, and _-u_
specifies that your hardware clock is set to UTC.

The _no_ option for _rtcwake_ means do not go into a sleep state, but only set the wakeup time. Remove the _no_ option to immediately go into a sleep state.

Real-time clock (RTC) wake-ups are the least reliable. Your system has to be put into
an Advanced Configuration and Power Interface (ACPI) sleep state supported by
your Linux. ACPI is the modern power management standard for managing sleep
states. It is supposed to be vendor neutral and hardware independent, but the stan‐
dard is complex and hardware vendors often support only a subset of its capabilities.
Adding to the fun, the various Linuxes implement it in different ways.

There are six ACPI sleep states, S0-S5. The Linux kernel is capable of supporting up
to four, and distributions vary in which ones and how many:

_S0_

_S1_

_S2_

_S3_

_S4_

System is running, monitor may be off, most peripherals are on.

Power-on suspended, CPU stops, power to CPU and RAM is on.

CPU is powered off, dirty cache is flushed to RAM.

Also called standby, sleep, and suspend-to-RAM. Data may not be written to
disk.

Hibernation, suspend-to-disk. Everything in RAM is written to disk and the sys‐
tem is powered down.

**74** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

_S5_

Similar to powering the system off, except there is still power to the power button
and peripherals, such as the keyboard, network interface, and USB devices.

**See Also**

 - _man 8 cron_

 - _man 8 rtcwake_

 - [Time and Date](https://timeanddate.com)

**3.10 Setting Up Remote Wake-Ups with Wake-on-LAN**
**over Wired Ethernet**

**Problem**

You want to set up remotely triggered wake-ups with Wake-on-LAN because your
UEFI setup does not have a scheduled wake-up feature, or it is too simple for your
needs, or you want the flexibility to send a wake-up signal at random times. This
recipe is for waking up a machine on the same network as the device you use to send
the wake-up signal, and your target machine must use a wired Ethernet interface.

**Solution**

Configure your PC to listen for wake-up requests, then use a second device, such as
another computer, a smartphone, or a Raspberry Pi to send the wake-up signal,
which is called the _magic packet_ . Which isn’t really magic, but merely a specialized
packet designed specifically for remote wake-ups. (Yes, I too am sad it is not real
magic.)

Start by booting into your system’s UEFI setup and look for settings for enabling
Wake-on-LAN.

An important precaution is to disable all settings that enable PXE
(preboot execution environment) booting. If PXE boot is enabled,
and you have a PXE server (a preboot execution environment
server, which is booting from a network installation server) on
your network, it is possible that your machine will wake up to PXE
boot and install a new image, overwriting the existing installation.

Then exit and finish starting up. Install the _wakeonlan_ and _ethtool_ packages.

**3.10 Setting Up Remote Wake-Ups with Wake-on-LAN over Wired Ethernet** **|** **75**

Fetch the name of your Ethernet interface, which in this example is _enp0s25_, and use
_ethtool_ to verify that it supports Wake-on-LAN. The output is abbreviated for clarity:

```
  $ ip addr show
  2: enp0s25: <BROADCAST,MULTICAST,UP,LOWER_UP> state UP 0
  link/ether 9c:ef:d5:fe:8f:20 brd ff:ff:ff:ff:ff:ff
  inet 192.168.1.97/24 brd 192.168.1.255 scope global dynamic
  [...]

  $ sudo ethtool enp0s25 | grep -i wake-on
  Supports Wake-on: pumbg
  Wake-on: g
```

Record the MAC address of your interface. In the preceding _ip_ example, the “ether”
line lists the MAC address, 9c:ef:d5:fe:8f:20. Yours will be different, as MAC addresses
are unique.

“Supports Wake-on: pumbg” is the magic phrase that verifies your interface has the
necessary support, indicated by the _g_ switch. The second line, “Wake-on: g,” tells you
that it is already enabled. If it is not, enable it:

```
  $ sudo ethtool -s enp0s25 wol g
```

If it does not stay enabled after a restart, add an entry like this to _/etc/crontab_ to run
the command after every restart:

```
  $ @reboot root /usr/bin/ethtool -s enp0s25 wol g
```

Shut down the machine, and from a second device on the same network, send the
command to wake it up, using the MAC address of your target machine’s Ethernet
interface:

```
  $ /usr/bin/wakeonlan 9c:ef:d5:fe:8f:20
```

If your target machine and second device are on the same network but in different
subnets, specify the broadcast address for your target machine:

```
  $ /usr/bin/wakeonlan -i 192.168.44.255 9c:ef:d5:fe:8f:20
```

**Discussion**

Wake-on-LAN is an Ethernet standard for remotely waking up a computer by send‐
ing it a wake-up signal over a network. _wakeonlan_ is the name of the command and
the name of the package on most Linuxes.

When your computer is shut down, it isn’t really turned off, but is in a low power
mode, and can receive and act on the magic packet wake-up signal.

_wakeonlan_ sends the magic packet over UDP port 9. The magic packet goes to the
network’s broadcast address, and every host on the network receives this packet. The
MAC address ensures that only the host with that address will wake up.

**76** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

The target machine wakes up just as if you had pressed the power button.

**See Also**

 - _man 1 wakeonlan_

 - _man 8 ethtool_

 - Recipe 3.8

 - Recipe 3.9

 - Recipe 3.11

**3.11 Setting Up Remote Wake-Ups over WiFi (WoWLAN)**

**Problem**

Your want to wake up a remote computer via its wireless interface (Wake-on-Wireless
LAN, or WoWLAN).

**Solution**

This recipe is for waking up a machine on the same network as the device you use to
send the wake-up signal.

Your machine must have an onboard wireless interface, either integrated on the
motherboard or peripheral component interconnect (PCI). It will not work with
a USB interface because there is no power to the USB bus when the machine is
shut down.

First, enter the UEFI setup of the machine you want to wake up remotely and enable
any Wake-on-LAN settings.

An important precaution is to also disable all settings that enable
PXE booting. If PXE boot is enabled and you have a PXE server on
your network, it is possible that your machine will wake up to PXE
boot and install a new image, overwriting the existing installation.

Then exit and finish starting up. Install the _iw_ command, and use it to list all of your
wireless devices:

```
  $ iw dev
  phy#0
  Interface wlxcc3fd5fe014c
  ifindex 3
  wdev 0x1

```

**3.11 Setting Up Remote Wake-Ups over WiFi (WoWLAN)** **|** **77**

```
  addr 9c:bf:25:fe:0e:7c
  ssid accesspointe
  type managed
  channel 11 (2462 MHz), width: 20 MHz, center1: 2462 MHz
  txpower 20.00 dBm
```

If there is more than one, query the one you want to use. The following example
shows a wireless interface that does not support WoWLAN:

```
  $ iw phy0 wowlan show
  command failed: Operation not supported (-95)
```

The following example is for an interface that supports WoWLAN, and it is not
enabled:

```
  $ iw phy0 wowlan show
  WoWLAN is disabled
```

Enable WoWLAN:

```
  $ sudo iw phy0 wowlan enable magic-packet
  WoWLAN is enabled:
  * wake up on magic packet
```

_iw dev_ provides the MAC address, which your second device needs to send the magic
packet:

```
  $ /usr/bin/wakeonlan 9c:bf:25:fe:0e:7c
```

Send the magic packet to a machine on the same network, but in a different subnet,
using the broadcast address of the subnet:

```
  $ /usr/bin/wakeonlan -i 192.168.44.255 9c:bf:25:fe:0e:7c
```

**Discussion**

This works well when the remote computer is a laptop, as laptops have integrated
wireless network interfaces that typically support more features. Desktop machines
usually don’t ship with integrated wireless interfaces, so you must shop carefully for a
PCI/PCIe wireless adapter that supports WoWLAN and Linux.

**See Also**

 - _man 8 iw_

 - _man 1 wakeonlan_

 - Recipe 3.8

 - Recipe 3.9

 - Recipe 3.10

**78** **|** **Chapter 3: Starting, Stopping, Restarting, and Putting Linux into Sleep Modes**

**<u>CHAPTER 4</u>**
#### **Managing Services with systemd**

Every time you start your Linux computer, its initialization system launches a batch
of processes, from a few dozen to hundreds, depending on how the system is set up.
You can see this on your startup screen (Figure 4-1; press the Escape key to hide your
graphical startup screen and see the startup messages).

_Figure 4-1. Linux startup messages_

In olden times we had the Unix System V initialization system (SysV init), BSD init,
and Linux Standard Base (LSB) init for launching processes at startup. SysV init was
the most common. Those days are fading away, and now systemd is the shiny new

**79**

init system for Linux. It has been adopted by all the major Linux distributions,
though of course there are a number of distributions that still use the legacy init
systems.

In this chapter you will learn if your Linux distribution uses systemd. You will learn
what processes, threads, services, and daemons are, and how to use systemd to man‐
age services: start, stop, enable, disable, and check status. You will become acquainted
with the _systemctl_ command, which is the systemd system and service manager.

systemd is designed to provide functionality suited to modern complex server and
desktop systems, and it does considerably more than the legacy init systems. It pro‐
vides complete service management from startup to shutdown, starting processes at
boot, on-demand after boot, and shutting down services when they are not needed. It
manages functions such as system logging, automounting filesystems, automatic ser‐
vice dependency resolution, name services, device management, network connection
management, login management, and a host of other tasks.

This sounds like a lot until you realize that processes do everything on a computer,
and all of this functionality used to be provided by a large assortment of other pro‐
grams. systemd brings it all together in an integrated software suite that should oper‐
ate the same way on all Linux systems, though as always with Linux there are some
minor exceptions, such as file locations and service names. Be aware that your partic‐
ular Linux may have some differences from the examples in this chapter.

systemd attempts to decrease boot times and parcel out system resources more effi‐
ciently by starting processes concurrently and in parallel, and starting only necessary
services, leaving other services to start after boot as needed. A service that is depen‐
dent on other services no longer has to wait to start for those services to become
available because all it needs is a waiting Unix socket to become available. Recipe 4.9
shows how to find processes that are slowing down your system startup.

systemd binaries are written in C, which provides some performance enhancement.
The legacy inits are masses of shell scripts, and any compiled language operates faster
than shell scripts.

systemd is backwards compatible with SysV init. Most Linux distributions retain the
legacy SysV configuration files and scripts, including _/etc/inittab_ and the _/etc/rc.d/_
and _/etc/init.d/_ directories. When a service does not have a systemd configuration file,
systemd looks for a SysV configuration file. systemd is also backward compatible with
Linux Standard Base (LSB) init.

systemd service files are smaller and easier to understand than SysV init files. Com‐
pare a SysV init file for sshd with its systemd service file. This is a snippet of the sshd
init file, _/etc/init.d/ssh_, from MX Linux:

**80** **|** **Chapter 4: Managing Services with systemd**

```
  #! /bin/sh

  ### BEGIN INIT INFO
  # Provides: sshd
  # Required-Start: $remote_fs $syslog
  # Required-Stop: $remote_fs $syslog
  # Default-Start: 2 3 4 5
  # Default-Stop:
  # Short-Description: OpenBSD Secure Shell server
  ### END INIT INFO

  set -e

  # /etc/init.d/ssh: start and stop the OpenBSD "secure shell(tm)" daemon

  test -x /usr/sbin/sshd || exit 0

  umask 022

  if test -f /etc/default/ssh; then
  [...]
```

This goes on for a total of 162 lines. This is a complete systemd service file from
Ubuntu 20.04, _/lib/systemd/system/ssh.service_ :

```
  [Unit]
  Description=OpenBSD Secure Shell server
  Documentation=man:sshd(8) man:sshd_config(5)
  After=network.target auditd.service
  ConditionPathExists=!/etc/ssh/sshd_not_to_be_run

  [Service]
  EnvironmentFile=-/etc/default/ssh
  ExecStartPre=/usr/sbin/sshd -t
  ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
  ExecReload=/usr/sbin/sshd -t
  ExecReload=/bin/kill -HUP $MAINPID
  KillMode=process
  Restart=on-failure
  RestartPreventExitStatus=255
  Type=notify
  RuntimeDirectory=sshd
  RuntimeDirectoryMode=0755

  [Install]
  WantedBy=multi-user.target
  Alias=sshd.service
```

Even without reading the documentation, or knowing anything about systemd, you
can understand some of what this file is supposed to do.

**Managing Services with systemd** **|** **81**

[See Rethinking PID 1 for a detailed introduction to systemd by one of its inventors](https://oreil.ly/dFz4K)
and maintainers, Lennart Poettering. Rethinking PID 1 details the rationale behind
building a new init system, its architecture, advantages, and how it uses existing
Linux kernel features in place of duplicating existing functionality.

**4.1 Learning if Your Linux Uses systemd**

**Problem**

You need to know if your Linux distribution uses systemd or something else.

**Solution**

Look for the _/run/systemd/system/_ directory. If this exists, then your init system is sys‐
temd.

**Discussion**

The _/run/systemd/_ directory may be present on your system if your distribution sup‐
ports multiple init systems. But systemd is not the active init unless you see _/run/_
_systemd/system/_ .

There are several other ways to learn which init system your system is using. Try
querying _/sbin/init_ . Originally this was the SysV executable, and now most Linux dis‐
tributions preserve the name and symlink it to the systemd executable. This example
confirms that the init is systemd:

```
  $ stat /sbin/init
  File: /sbin/init -> /lib/systemd/systemd
  [...]
```

On a system using SysV init, it has no symlink:

```
  $ stat /sbin/init
  File: /sbin/init
  [...]
```

The _/proc_ pseudofilesystem is an interface to your Linux kernel, and contains the cur‐
rent state of a running system. It is called a pseudofilesystem because it exists only in
memory and not on disk. In this example, _/proc/1/exe_ is symlinked to the systemd
executable:

```
  $ sudo stat /proc/1/exe
  File: /proc/1/exe -> /lib/systemd/systemd
  [...]

```

**82** **|** **Chapter 4: Managing Services with systemd**

On a SysV system, it links to _init_ :

```
  $ sudo stat /proc/1/exe
  File: /proc/1/exe -> /sbin/init
  [...]
```

The _/proc/1/comm_ file reports your active init system:

```
  $ cat /proc/1/comm
  systemd
```

On a SysV system, it reports _init_ :

```
  $ cat /proc/1/comm
  init
```

The command attached to process ID (PID) 1 is your init. PID 1 is the first process
launched at startup, which then starts all other processes. You can see this with the _ps_
command:

```
  $ ps -p 1
  PID TTY     TIME CMD
  1 ?    00:00:00 systemd
```

When the init is SysV, it looks like this:

```
  $ ps -p 1
  PID TTY     TIME CMD
  1 ?    00:00:00 init
```

See Recipe 4.2 for more information on PID 1.

Linux support for systemd varies. Most of the major Linux distributions have adoped
systemd, including Fedora, Red Hat, CentOS, openSUSE, SUSE Linux Enterprise,
Debian, Ubuntu, Linux Mint, Arch, Manjaro, Elementary, and Mageia Linux.

Some popular distributions that do not support systemd, or include it but not as the
default init, are Slackware, PCLinuxOS, Gentoo Linux, MX Linux, and antiX.

**See Also**

 - [Distrowatch for information on hundreds of Linux distributions](https://distrowatch.com)

 - _man 5 proc_

 - _man 1 pstree_

 - _man 1 ps_

**4.1 Learning if Your Linux Uses systemd** **|** **83**

**4.2 Understanding PID 1, the Mother of All Processes**

**Problem**

You want a better understanding of services and processes on Linux.

**Solution**

PID 1 is the mother of all processes on Linux systems. This is the first process to start,
and then it launches all other processes.

Processes are one or more running instances of a program. Every task in a Linux sys‐
tem is performed by a process. Processes can create independent copies of them‐
selves, that is, they can _fork_ . The forked copies are called _children_, and the original is
the _parent_ . Each child has its own unique PID, and its own allocation of system
resources, such as CPU and memory. _Threads_ are lightweight processes that run in
parallel and share system resources with their parents.

Some processes run in the background and do not interact with users. Linux calls
these processes _services_ or _daemons_, and their names tend to end with the letter D,
such as httpd, sshd, and systemd.

Every Linux system starts PID 1 first, which then launches all other processes. Use the
_ps_ command to list all running processes in PID order:

```
  $ ps -ef
  UID    PID PPID C STIME TTY     TIME CMD
  root     1   0 0 10:06 ?    00:00:01 /sbin/init splash
  root     2   0 0 10:06 ?    00:00:00 [kthreadd]
  root     3   2 0 10:06 ?    00:00:00 [rcu_gp]
  root     4   2 0 10:06 ?    00:00:00 [rcu_par_gp]
  [...]
```

The _pstree_ command organizes this mass of information into a tree diagram. This
example shows all processes, their child processes, PIDs, and threads, which are
enclosed in curly braces:

```
  $ pstree -p
  systemd(1)─┬─ModemManager(925)─┬─{ModemManager}(944)
  │          └─{ModemManager}(949)
  ├─NetworkManager(950)─┬─dhclient(1981)
  │           ├─{NetworkManager}(989)
  │           └─{NetworkManager}(991)
  ├─accounts-daemon(927)─┬─{accounts-daemon}(938)
  │           └─{accounts-daemon}(948)
  ├─acpid(934)
  ├─agetty(1103)
  ├─avahi-daemon(953)───avahi-daemon(970)
  [...]

```

**84** **|** **Chapter 4: Managing Services with systemd**

The full _pstree_ output is quite large. You can view a single process, identified by its
PID, and its parents, children, and threads, like the following example for the Kate
text editor:

```
  $ pstree -sp 5193
  systemd(1)───kate(5193)─┬─bash(5218)
  ├─{kate}(5195)
  ├─{kate}(5196)
  ├─{kate}(5197)
  ├─{kate}(5198)
  ├─{kate}(5199)
  [...]
```

This shows that `systemd(1)` is Kate’s parent, `bash(5218)` is Kate’s child, and all the
processes in curly braces are Kate’s threads.

**Discussion**

Processes always exist in one of several states, and these states change according to
system activity. The following _pstree_ example displays the PID, user, state, and com‐
mand fields:

```
  $ ps -eo pid,user,stat,comm
  PID USER    STAT COMMAND
  1 root    Ss  systemd
  2 root    S  kthreadd
  32 root    I<  kworker/3:0H-kb
  68 root    SN  khugepaged
  11222 duchess  Rl  konsole

```

 - _R_ is either currently running or waiting in the run queue.

 - _l_ means the process is multithreaded.

 - _S_ is interruptable sleep; the process is waiting for an event to complete.

 - _s_ is a session leader. Sessions are related processes managed as a unit.

 - _I_ is an idle kernel thread.

 - _<_ means high priority.

 - _N_ is low priority.

There are several rarely used states you can read about in _man 1 ps_ .

**See Also**

 - Recipe 4.7

 - _man 5 proc_

**4.2 Understanding PID 1, the Mother of All Processes** **|** **85**

 - _man 1 pstree_

 - _man 1 ps_

**4.3 Listing Services and Their States with systemctl**

**Problem**

You want to list all services installed on your system, and you want to know the states
of the services: whether they are running, not running, or in an error state.

**Solution**

_systemctl_, the systemd manager command, tells all. Run it with no options to see a
detailed list of all loaded units. A systemd unit is any related batch of processes
defined in a unit configuration file and managed by systemd:

```
  $ systemctl
```

This prints a giant pile of information: 177 active loaded units on my test system with
the full unit names, status, and long descriptions. Redirect the the output to a text file
for easier study:

```
  $ systemctl > /tmp/systemctl-units.txt
```

Treat yourself to more information overload by listing all units, active and inactive:

```
  $ systemctl --all
```

This results in 349 loaded units listed on my test system, including _not-found_ and
_inactive_ units. How many total unit files? The following example shows 5 out of 322:

```
  $ systemctl list-unit-files
  UNIT FILE                   STATE
  proc-sys-fs-binfmt_misc.automount       static
  -.mount                    generated
  mount                     generated
  dev-hugepages.mount              static
  home.mount                   generated
  [...]
  322 unit files listed.
```

We are interested in service files because Linux users and administrators interact
mainly with service files and rarely need to bother with any other type of unit file.
How many are installed? Let’s see:

```
  $ systemctl list-unit-files --type=service
  UNIT FILE                 STATE
  accounts-daemon.service          enabled
  acpid.service               disabled

```

**86** **|** **Chapter 4: Managing Services with systemd**

```
  alsa-state.service             static
  alsa-utils.service             masked
  anacron.service              enabled
  [...]
  212 unit files listed.
```

The preceding example displays the four most common states that a service can be in:
enabled, disabled, static, or masked.

List only enabled services:

```
  $ systemctl list-unit-files --type=service --state=enabled
  UNIT FILE                 STATE
  accounts-daemon.service          enabled
  anacron.service              enabled
  apparmor.service              enabled
  autovt@.service              enabled
  avahi-daemon.service            enabled
  [...]
  62 unit files listed.
```

List only disabled services:

```
  $ systemctl list-unit-files --type=service --state=disabled
  UNIT FILE              STATE
  acpid.service            disabled
  brltty.service            disabled
  console-getty.service        disabled
  mariadb@.service           disabled
  [...]
  12 unit files listed.
```

List only static services:

```
  $ systemctl list-unit-files --type=service --state=static
  UNIT FILE               STATE
  alsa-restore.service          static
  alsa-state.service           static
  apt-daily-upgrade.service       static
  apt-daily.service           static
  [...]
  106 unit files listed.
```

List only masked services:

```
  $ systemctl list-unit-files --type=service --state=masked
  UNIT FILE          STATE
  alsa-utils.service      masked
  bootlogd.service       masked
  bootlogs.service       masked
  checkfs.service       masked
  [...]
  36 unit files listed.

```

**4.3 Listing Services and Their States with systemctl** **|** **87**

**Discussion**

Service unit files are in _/usr/lib/systemd/system/_ or _/lib/systemd/system/_, according to
where your Linux distribution puts them. These are plain-text files you can read.

_enabled_

This shows that the service has become available and is managed by systemd.
When a service is enabled, systemd creates a symlink in _/etc/systemd/system/_
from the unit file in _/lib/systemd/system/_ . It can be started, stopped, reloaded, and
disabled by the user with the _systemctl_ command.

Enabling a service does not immediately start it, and disabling
a service does not immediately stop it (see Recipe 4.6).

_disabled_

Diabled means that there is no symlink in _/etc/systemd/system/_, and it will not
start automatically at boot. You can stop and start it manually.

_masked_

This means the service is linked to _/dev/null/_ . It is completely disabled and can‐
not be started by any means.

_static_

This means that the unit file is a dependency of other unit files, and cannot be
started or stopped by the user.

Some less-common service states you will see:

_indirect_

Indirect states belong to services that are not meant to be managed by users, but
are meant to be used by other services.

_generated_

Generated states indicate that the service has been converted from a nonnative
systemd initialization configuration file, either SysV or LSB init.

**See Also**

 - _man 1 systemctl_

**88** **|** **Chapter 4: Managing Services with systemd**

**4.4 Querying the Status of Selected Services**

**Problem**

You want to know the status of one service or a few specific services.

**Solution**

_systemctl status_ provides a nice little bundle of useful status information. The follow‐
ing example queries the CUPS service. CUPS, the Common Unix Printing System,
should be on all Linux systems:

```
  $ systemctl status cups.service
```

   - `cups.service - CUPS Scheduler`
```
  Loaded: loaded (/lib/systemd/system/cups.service; enabled; vendor preset:
  enabled)
  Active: active (running) since Sun 2021-11-22 11:01:48 PST; 4h 17min ago
```

`TriggeredBy:`   - `cups.path`

          - `cups.socket`
```
  Docs: man:cupsd(8)
  Main PID: 1403 (cupsd)
  Tasks: 2 (limit: 18760)
  Memory: 3.8M
  CGroup: /system.slice/cups.service
  ├─1403 /usr/sbin/cupsd -l
  └─1421 /usr/lib/cups/notifier/dbus dbus://

  Nov 22 11:01:48 host1 systemd[1]: Started CUPS Scheduler.
```

Query multiple services with a space-delimited list:

```
  $ systemctl status mariadb.service bluetooth.service lm-sensors.service
```

**Discussion**

There is a lot of useful information in this little bit of output (Figure 4-2).

_Figure 4-2. systemctl status output for the CUPS printer service_

**4.4 Querying the Status of Selected Services** **|** **89**

The dot next to the service name is a quick status indicator. It appears in colors on
most terminals. White is an _inactive_ or _deactivating_ state. Red is a _failed_ or _error_ state.
Green indicates an _active_, _reloading_, or _activating_ state. The rest of the information in
the output is described in the following:

_Loaded_

Verifies that the unit file has been loaded into memory, displays its full path,
the service is enabled (see the Discussion about states in Recipe 4.3), and
`vendor preset: disabled/enabled` indicates if the installation default is to start
at boot or not. When it is disabled, the vendor default is to not start at boot. This
only shows the vendor preference and does not indicate if it is currently enabled
or disabled.

_Active_

Tells you if the service is active or inactive, and how long it has been in that state.

_Process_

Reports the PIDs and their commands and daemons.

_Main PID_

This is the process number for the cgroup slice.

_Tasks_

Reports how many tasks the service has started. Tasks are PIDs.

_CGroup_

Shows which unit slice the service belongs to and its PID. The three default unit
slices are _user.slice_, _system.slice_, and _machine.slice_ .

Linux control groups (cgroups) are sets of related processes and all of their future
children. In systemd, a _slice_ is a subdivision of a cgroup, and each slice manages a
particular group of processes. Run _systemctl status_ to see a diagram of the cgroup
hierarchy.

By default, service and scope units are grouped in _/lib/systemd/system/_
_system.slice_ .

User sessions are grouped in _/lib/systemd/system/user.slice_ .

Virtual machines and containers registered with systemd are grouped in _/lib/_
_systemd/system/machine.slice_ .

The remaining lines are the most recent log entries from _journalctl_, the systemd log
manager.

**90** **|** **Chapter 4: Managing Services with systemd**

**See Also**

 - _man 1 systemctl_

 - _man 5 systemd.slice_

 - _man 1 journalctl_

 - [Kernel cgroups documentation](https://oreil.ly/FfUb3)

**4.5 Starting and Stopping Services**

**Problem**

You want to stop and start services with systemd.

**Solution**

This is a job for _systemctl_ . The following examples use the SSH service to demonstrate
service management.

Start a service:

```
  $ sudo systemctl start sshd.service
```

Stop a service:

```
  $ sudo systemctl stop sshd.service
```

Stop and then restart a service:

```
  $ sudo systemctl restart sshd.service
```

Reload the service’s configuration. For example, you made a change to _sshd_config_
and want to load the new configuration without restarting the service:

```
  $ sudo systemctl reload sshd.service
```

**Discussion**

All of these commands also work with multiple services, space-delimited, for
example:

```
  $ sudo systemctl start sshd.service mariadb.service firewalld.service
```

If you’re curious about the commands that systemd runs behind the scenes to start,
reload, or stop the individual daemons, look in their unit files. Some services have
start, reload, stop, and other instructions in their unit files, like this example for
httpd:

**4.5 Starting and Stopping Services** **|** **91**

```
  ExecStart=/usr/sbin/httpd/ $OPTIONS -DFOREGROUND
  ExecReload=/usr/sbin/httpd $OPTIONS -k graceful
  ExecStop=/bin/kill -WINCH ${MAINPID}
```

You don’t have to do anything special with this information; it is there when you want
to know how _systemctl_ is managing a particular service.

**See Also**

 - Recipe 4.6

 - _man 1 systemctl_

**4.6 Enabling and Disabling Services**

**Problem**

You want a service or services to automatically start at boot, or you want to prevent a
service from starting at boot, or to disable it completely.

**Solution**

Enabling a service configures it to automatically start at boot.

Disabling a service stops it from starting at boot, but it can be started and stopped
manually.

Masking a service disables it so that it cannot be started at all.

The following example enables the _sshd_ service:

```
  $ sudo systemctl enable sshd.service
  Created symlink /etc/systemd/system/multi-user.target.wants/sshd.service →
  /usr/lib/systemd/system/sshd.service
```

The output shows that enabling a service means creating a symlink from the service
file in _/lib/systemd/system/_ to _/etc/systemd/system/_ . This does not start the service. You
can start the service with _systemctl start_, or enable and start the service in one com‐
mand with the _--now_ option:

```
  $ sudo systemctl enable --now sshd.service
```

This command disables the _sshd_ service. It does not stop the service, so you must stop
it manually after disabling it:

```
  $ sudo systemctl disable sshd.service
  Removed /etc/systemd/system/multi-user.target.wants/sshd.service
  $ sudo systemctl stop sshd.service

```

**92** **|** **Chapter 4: Managing Services with systemd**

Or, disable and stop it with one command:

```
  $ sudo systemctl disable --now sshd.service
```

This command reenables the _mariadb_ service, which disables and then enables it. If
you have created the symlinks manually for a service, this is useful for quickly reset‐
ting them to the defaults:

```
  $ sudo systemctl reenable mariadb.service
  Removed /etc/systemd/system/multi-user.target.wants/mariadb.service.
  Removed /etc/systemd/system/mysqld.service.
  Removed /etc/systemd/system/mysql.service.
  Created symlink /etc/systemd/system/mysql.service →
  /lib/systemd/system/mariadb.service.
  Created symlink /etc/systemd/system/mysqld.service →
  /lib/systemd/system/mariadb.service.
  Created symlink /etc/systemd/system/multi-user.target.wants/mariadb.service →
  /lib/systemd/system/mariadb.service.
```

The following command disables the _bluetooth_ service completely by masking it, so
that it cannot be started at all:

```
  $ sudo systemctl mask bluetooth.service
  Created symlink /etc/systemd/system/bluetooth.service → /dev/null.
```

Unmasking the _bluetooth_ service does not enable it, so it must be started manually:

```
  $ sudo systemctl unmask bluetooth.service
  Removed /etc/systemd/system/bluetooth.service.
  $ sudo systemctl start bluetooth.service
```

**Discussion**

When you enable, disable, mask, or unmask a service, it remains in its current state
unless you use the _--now_ option. The _--now_ option works with _enable_, _disable_, and
_mask_ to immediately stop or start the service, but it does not work with _unmask_ .

See the Discussion in Recipe 4.3 to learn more about how systemd uses symlinks to
manage services.

**See Also**

 - _man 1 systemctl_

 - The Discussion in Recipe 4.3 to learn how systemd uses symlinks to manage
services

**4.6 Enabling and Disabling Services** **|** **93**

**4.7 Stopping Troublesome Processes**

**Problem**

You want to know how to stop troublesome processes. A certain service may be unre‐
sponsive or running away, spawning forks and causing your system to hang. Your
normal stop command is not working. What do you do?

**Solution**

Stopping a process is called killing the process. On Linux systems with systemd, you
should use _systemctl kill_ . On systems without systemd, use the legacy _kill_ command.

_systemctl kill_ is preferable because it stops all processes that belong to a service and
leaves no orphan processes, nor any processes that might restart the service and con‐
tinue to make trouble. First, try it with no options other than the service name, then
check the status:

```
  $ sudo systemctl kill mariadb

  $ systemctl status mariadb
```

   - `mariadb.service - MariaDB 10.1.44 database server`
```
  Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset:
  enabled)
  Active: inactive (dead) since Sun 2020-06-28 19:57:49 PDT; 6s ago
  [...]
```

The service has cleanly stopped. If this does not work, then try the nuclear option:

```
  $ sudo systemctl kill -9 mariadb
```

The legacy _kill_ command does not recognize service or command names, but rather
requires the PID of the offending process:

```
  $ sudo kill 1234
```

If this does not stop it, use the nuclear option:

```
  $ sudo kill -9 1234
```

**Discussion**

Use the _top_ command to identify runaway processes. Run it with no options, and the
processes using up the most CPU resources are listed at the top. Press the q key to
exit _top_ .

```
  $ top
  top - 20:30:13 up 4:24, 6 users, load average: 0.00, 0.03, 0.06
  Tasks: 246 total,  1 running, 170 sleeping,  0 stopped,  0 zombie
  %Cpu(s): 0.4 us, 0.2 sy, 0.0 ni, 99.4 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
  KiB Mem : 16071016 total, 7295284 free, 1911276 used, 6864456 buff/cache

```

**94** **|** **Chapter 4: Managing Services with systemd**

```
  KiB Swap: 8928604 total, 8928604 free,    0 used. 13505600 avail Mem

  PID USER    PR NI  VIRT  RES  SHR S %CPU %MEM   TIME+ COMMAND
  3504 madmax   20  0 99.844g 177588 88712 S  2.6 1.1  0:08.68 evolution
  2081 madmax   20  0 3818636 517756 177744 S  0.7 3.2  5:07.56 firefox
  1064 root    20  0 567244 148432 125572 S  0.3 0.9 12:54.75 Xorg
  2362 stash   20  0 2997732 230508 145444 S  0.3 1.4  0:40.72 Web Content
  [...]
```

_kill_ sends signals to processes, and the default signal is SIGTERM (signal terminate).
SIGTERM is gentle, allowing processes to shut down cleanly. SIGTERM is also igno‐
rable, and processes don’t have to pay attention to it. Signals can be identified by
name or number; for most folks the numbers are easier to remember, so spelling out
the default looks like this:

```
  $ sudo kill -1 1234
```

_kill -9_ is SIGKILL. SIGKILL stops processes immediately and uncleanly, and also
attempts to stop all child processes.

Killing services with _systemctl kill_ is easier than with _kill_, and more reliable. You only
need the service name, and you don’t have to hunt down PIDs. It ensures that all pro‐
cesses belonging to the service are stopped, which _kill_ cannot ensure.

There are a ton of signals that have accumulated over the years, and you can read all
about them in _man 7 signal_ . In my experience, the most relevant signals are SIG‐
TERM and SIGKILL, but don’t let that stop you from learning more about the others.

If you are uncomfortable with terminology like kill, parents, children, and orphans,
so am I. Maybe someday it will change.

**See Also**

 - _man 5 systemd.kill_

 - _man 1 systemctl_

 - _man 1 kill_

 - _man 7 signal_

**4.8 Managing Runlevels with systemd**

**Problem**

You want to reboot to different system states in a manner similar to using SysV
runlevels.

**4.8 Managing Runlevels with systemd** **|** **95**

**Solution**

systemd _targets_ are similar to SysV runlevels. These are boot profiles that start your
system with different options, such as multiuser mode with a graphical desktop, mul‐
tiuser mode with no graphical desktop, and emergency and rescue modes to use
when your current target will not boot. (See the Discussion for more information on
runlevels.)

The following command checks if the system is running and reports its state:

```
  $ systemctl is-system-running
  running
```

What is the default target?

```
  $ systemctl get-default
  graphical.target
```

Get the current runlevel:

```
  $ runlevel
  N 5
```

Reboot to rescue mode:

```
  $ sudo systemctl rescue
```

Reboot to emergency mode:

```
  $ sudo systemctl emergency
```

Reboot to the default mode:

```
  $ sudo systemctl reboot
```

Reboot to a different target without changing the default:

```
  $ sudo systemctl isolate multi-user.target
```

Set a different default runlevel:

```
  $ sudo systemctl set-default multi-user.target
```

List the runlevel target files and their symlinks on your system:

```
  $ ls -l /lib/systemd/system/runlevel*
```

List the dependencies in a runlevel target:

```
  $ systemctl list-dependencies graphical.target

```

**96** **|** **Chapter 4: Managing Services with systemd**

**Discussion**

SysV runlevels are different states that your system can boot to, for example, with a
graphical desktop, without a graphical desktop, and with emergency runlevels to use
when your default runlevel has problems and will not boot.

systemd _targets_ approximately correspond to the legacy SysV runlevels:

 - _runlevel0.target_, _poweroff.target_, halt

 - _runlevel1.target_, _rescue.target_, single-user text mode, all local filesystems moun‐
ted, root user only, no networking

 - _runlevel3.target_, _multi-user.target_, multiuser text mode (no graphical environ‐
ment)

 - _runlevel5.target_, _graphical.target_, multiuser graphical mode

 - _runlevel6.target_, _reboot.target_, reboot

_systemctl emergency_ is a special target that is more restricted than _rescue_ mode: no
services, no mount points other than the root filesystem, no networking, root user
only. It is the most minimal running system for debugging problems. You may see
options to boot into a rescue or emergency mode in your GRUB2 bootloader screen.

_systemctl is-system-running_ reports various system states:

 - _initializing_ means the system has not completed startup.

 - _starting_ means the system is in the final stages of startup.

 - _running_ is fully operational, and all processes are started.

 - _degraded_ means the system is operational, but one or more systemd units have
failed. Run _systemctl | grep failed_ to see which units failed.

 - _maintenance_ means that either the _rescue_ or _emergency_ target is active.

 - _stopping_ means that systemd is shutting down.

 - _offline_ means that systemd is not running.

 - _unknown_ means that there is a problem preventing systemd from determining
the operational state.

**See Also**

 - _man 1 systemctl_

 - _man 8 systemd-halt.service_

**4.8 Managing Runlevels with systemd** **|** **97**

**4.9 Diagnosing Slow Startups**

**Problem**

systemd promises faster startups, but your system starts up slowly, and you want to
find out why.

**Solution**

You want _systemd-analyze blame_ . Run it with no options to see a list of system pro‐
cesses and how long they took to start:

```
  $ systemd-analyze blame
  34.590s apt-daily.service
  6.782s NetworkManager-wait-online.service
  6.181s dev-sda2.device
  4.444s systemd-journal-flush.service
  3.609s udisks2.service
  2.450s snapd.service
  [...]
```

Analyze only user processes:

```
  $ systemd-analyze blame --user
  3.991s pulseaudio.service
  553ms at-spi-dbus-bus.service
  380ms evolution-calendar-factory.service
  331ms evolution-addressbook-factory.service
  280ms xfce4-notifyd.service
  [...]
```

**Discussion**

It is useful to review everything that starts at boot and perhaps find services you don’t
want starting at boot. My favorite to disable is Bluetooth because I don’t use it on my
servers or PCs, but many Linux distros enable it by default.

**See Also**

 - _man 1 systemd-analyze_

**98** **|** **Chapter 4: Managing Services with systemd**

**<u>CHAPTER 5</u>**
#### **Managing Users and Groups**

Linux has two types of users: human users and system users. Each user has a unique
identity (UID), and at least one group identification (GID). All users have one pri‐
mary group and may be members of multiple groups.

Each human user owns a home directory for their personal files. User home directo‐
ries belong in _/home_ and are named for the owner, like our example user Duchess,
who owns _/home/duchess_ . Users may belong to multiple groups, and the additional
group memberships are called _supplemental_ groups. Users in a group have all the
privileges of that group. (To learn all about privileges, see Chapter 6.) Privileges con‐
trol access to files and commands, and are fundamental to system security.

System users represent system services and processes. System users need user
accounts for controlling their privileges and do not have logins or directories
in _/home_ .

Human users are divided into two categories: the _root_ user, or the superuser, is allpowerful and can do anything on the system. All other users are called normal or
unprivileged users. Normal users are given just enough privileges to manage their
own files and run commands that allow normal users to use them. Normal users can
be given limited or complete root powers, which you will learn about in the recipes
about _su_ and _sudo_ .

You can see all the users on your system in _/etc/passwd_, and all the groups in _/etc/_
_group_ .

**99**

**Centralized User Management**

_/etc/passwd_ and _/etc/group_ are inherited from Unix and have not
changed much since they were ported to Linux in 1992. Since then,
newer tools have evolved to manage users and groups, such as cen‐
tralized databases that serve entire organizations. This chapter does
not cover centralized user management tools.

Linux comes with a number of commands for managing users and groups:

 - _useradd_ creates new users.

 - _groupadd_ creates new groups.

 - _userdel_ deletes users.

 - _groupdel_ deletes groups.

 - _usermod_ is for making changes to existing users.

 - _passwd_ creates and changes passwords.

These are part of the _Shadow Password Suite_, and _/etc/login.defs_ is its main configura‐
tion file.

_useradd_ behaves differently on different systems, according to how it is configured.
Traditionally, it lumped all new users into the same primary group, _users_ (100). This
meant that users had to be careful with permissions on their files to avoid exposing
them to other group users. Red Hat changed this with its _User Private Group_ scheme,
which creates a personal private group for each new user. Most Linux distributions
make this the default, though there are exceptions, such as openSUSE.

The Shadow Password Suite was created by Julianne Frances Haugh way back in the
1980s, back before Linux was born, to improve Unix password security and to make
user account management easier. It was ported to Linux in 1992, when Linux was
barely a year old.

Before the Shadow Password Suite, all the relevant files had to be edited individually,
there were multiple password management commands, and hashed passwords were
stored in _/etc/passwd_ and _/etc/group_ . These two files must be world readable, so stor‐
ing passwords in them, even when they’re hashed, is asking for trouble. Anyone can
copy a world-readable file, and then crack the passwords at their leisure. Relocating
the hashed passwords to the shadow files, _/etc/shadow_ and _/etc/gshadow_, which are
accessible only by root, added a strong layer of protection. The longevity of the
Shadow Password Suite is a testament to how well it was designed and coded.

Newer arrivals are _adduser_ and _addgroup_ for Debian. They are Perl script wrappers
for _useradd_ and _groupadd_ . These scripts walk you through a complete new user and
new group configuration.

**100** **|** **Chapter 5: Managing Users and Groups**

In this chapter, you will learn how to create and remove human and system users,
manage passwords, find UIDs and GIDs, set your desired defaults for creating new
users, change group memberships, customize the common files your new users need,
clean up after users that you have removed, become root, and grant limited root
powers to normal users.

**5.1 Finding a User’s UID and GID**

**Problem**

You want to list users’ UIDs and GIDs.

**Solution**

Use the _id_ command with no options to see your own UID and GIDs. In the follow‐
ing example, the user is Duchess:

```
  duchess@pc:~$ id
  uid=1000(duchess) gid=1000(duchess)
  groups=1000(duchess),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),118(lpadmin),
  126(sambashare),131(libvirt)
```

Display another user’s UID and GIDs by providing their username as an argument:

```
  duchess@pc:~$ id madmax
  uid=1001(madmax) gid=1001(madmax) groups=1001(madmax),1010(composers)
```

Display your effective ID. This is your ID when you run a command as another user.
You can see this with _sudo_ :

```
  duchess@client4:~$ sudo id -un
  root

  duchess@client4:~$ sudo -u madmax id -gn
  madmax
```

**Discussion**

There are three types of user IDs in Linux:

 - Real UID/GID

 - Effective UID/GID

 - Saved UID/GID

The _real ID_ is the UID and primary GID assigned to the user at creation. These are
what you see when you run the _id_ command, as yourself, with no options.

**5.1 Finding a User’s UID and GID** **|** **101**

The _effective ID_ is the UID used to run a process that requires different privileges
than the user who launched the process, for example, the _passwd_ command. _passwd_
requires root privileges but uses the special permission modes to allow users to
change their own passwords.

You can see this for yourself. First, take a look at the _passwd_ command’s permissions:

```
  $ ls -l /usr/bin/passwd
  -rwsr-xr-x 1 root root 68208 May 27 2020 /usr/bin/passwd
```

This shows that _passwd_ is owned by root, both UID and GID. Now type the _passwd_
command and press Enter.

Open a second terminal to find the process for _passwd_, then print its process ID,
effective ID, and real ID:

```
  $ ps -a|grep passwd
  12916 pts/1  00:00:00 passwd

  $ ps -eo pid,euser,ruser,rgroup | grep 12916
  12916 root   root   root
```

Even though an unprivileged user is running _passwd_, it runs with root permissions.
(See Recipe 6.11 for information on the special permission modes.)

The _saved ID_ is used by processes that need elevated privileges, usually root privi‐
leges. When a process needs to do work that requires fewer privileges, it can tem‐
porarily switch to a nonprivileged user ID. The effective UID is changed to the lower
privilege value, and the original effective UID is saved to the SUID, saved user ID.
When the process needs elevated privileges again, it changes to the SUID.

The _id_ command has a few options:

 - _-u_ shows the effective UID number.

 - _-g_ shows the effective GID number.

 - _-G_ shows all group IDs.

 - _-n_ prints the name rather than the number. You can use this in combination with
_-u_, _-g_, and _-G_ .

 - _-un_ shows the effective UID username.

 - _-gn_ shows the effective group name.

 - _-Gn_ shows all effective GID names.

 - _-r_ shows the real ID instead of the effective ID. You can use this in combination
with _-u_, _-g_, and _-G_ .

**102** **|** **Chapter 5: Managing Users and Groups**

**See Also**

 - Recipe 6.11

 - _man 1 id_

 - _man 1 ps_

**5.2 Creating a Human User with useradd**

**Problem**

You want to create a new user with a user private group and home directory popula‐
ted with a set of default files like _.bashrc_, _.profile_, _.bash_history_, and any other files you
want them to have.

**Solution**

The _useradd_ command is included in most Linux distributions and is configurable to
suit your requirements. The default configuration varies across the various Linux dis‐
tributions, so the quickest way to learn how your system is set up is to create a new
test user:

```
  $ sudo useradd test1
```

Now run the _id_ command, and then see if _useradd_ created a home directory. The fol‐
lowing examples are from Fedora 34:

```
  $ id test1
  uid=1011(test1) gid=1011(test1) groups=1011(test1)

  $ sudo ls -a /home/test1/
  . .. .bash_logout .bash_profile .bashrc
```

In this example, the default configuration meets all the requirements listed in the
Problem. Now you only need to set a password:

```
  $ sudo passwd test1
  Changing password for user test1.
  New password: password
  Retype new password: password
  passwd: all authentication tokens updated successfully.
```

You may elect to force the user to reset their password at first login, after creating the
user’s password:

```
  $ sudo passwd -e test1
  Expiring password for user test1.
  passwd: Success

```

**5.2 Creating a Human User with useradd** **|** **103**

Give the login to your user, and they can start using their new account. The new user
account is represented like this in _/etc/passwd_ :

```
  test1:x:1011:1011::/home/test1:/bin/bash
```

Some Linuxes, for example openSUSE, configure _useradd_ to not create the user’s
home directory by default and to put all users into the _users (100)_ group. This poten‐
tially exposes files to other users, if group permissions on the files allow it. The fol‐
lowing example creates a user private group:

```
  $ sudo useradd -mU test2
```

_-m_ creates the user’s home directory, and _-U_ creates their private group with the same
name as their username.

**Discussion**

All new user accounts are inactive until you set a password.

The first group created for a user, whether it is a user private group or a common
group for all users, is their _primary_ group. All other groups the user is assigned to are
_supplementary_ groups.

There are some additional useful options:

 - _-G_, _--groups_ is for adding the user to multiple supplemental groups in a commadelimited list. The groups must already exist:

```
  $ sudo useradd -G group1,group2,group3 test1

```

 - _-c_, _--comment_ accepts any text string. Use this for the user’s full name, or any
comment or description:

```
  $ useradd -G group1,group2,group3 -c 'Test 1,,,,' test1
```

The four commas define five fields: full name, room number, work phone, home
phone, and other. Way back in olden times this was called the GECOS data. GECOS
is short for General Electric Comprehensive Operating Supervisor, a mainframe
operating system. You may enter any text string in these fields, or nothing, though it
is useful to include the user’s full name. Study your _/etc/passwd_ file to see how other
entries use the GECOS fields.

The _useradd_ defaults are scattered across multiple configuration files; see Recipe 5.4
to learn how to change the defaults.

**104** **|** **Chapter 5: Managing Users and Groups**

**See Also**

 - _man 8 useradd_

 - _man 5 login.defs_

 - _/etc/default/useradd_

 - _/etc/skel_

 - _/etc/login/defs_

**5.3 Creating a System User with useradd**

**Problem**

You want to create a system user with the _useradd_ command.

**Solution**

The following example creates a new system user with no home directory, no login
shell, and uses the correct UID numbering range for system users:

```
  $ sudo useradd -rs /bin/false service1
```

_-r_ means create a system user with a real ID in the correct numerical range for system
users, and _-s_ specifies the login shell. _/bin/false_ is a command that does nothing and
prevents the user from logging into the system.

See the Discussion in Recipe 5.6 for information about UID and GID numbering.

**Discussion**

In olden times, most services ran as the _nobody_ user. Now it is a common practice for
services to have their own unique users, as this provides stronger security than the
_nobody_ user owning multiple services. You will rarely have to create a system user, as
services should create their own unique users when they are installed.

The _nobody_ user is always assigned UID 65534 and GID 65534.

**See Also**

 - _man 8 useradd_

 - _man 1 false_

 - The Discussion in Recipe 5.6

**5.3 Creating a System User with useradd** **|** **105**

**5.4 Changing the useradd Default Settings**

**Problem**

The default _useradd_ settings are not right for you, and you want to change them.

**Solution**

The _useradd_ configuration is spread across multiple configuration files: _/etc/default/_
_useradd_, _/etc/login.defs_, and files in the _/etc/skel_ directory.

The following values appear in _/etc/default/useradd_ . This example shows the open‐
SUSE defaults:

```
  $ useradd -D
  GROUP=100
  HOME=/home
  INACTIVE=-1
  EXPIRE=
  SHELL=/bin/bash
  SKEL=/etc/skel
  CREATE_MAIL_SPOOL=yes
```

_GROUP=100_ sets a single shared group as the default for all new users, traditionally
_100_ . The group must first exist, and _USERGROUPS_ENAB no_ must be set in _/etc/_
_login.defs_ . Then set _GROUP=_ in _/etc/default/useradd_ to the GID of the user group. If
our Duchess user is in a shared group, her _id_ output shows _uid=1000(duchess)_
_gid=100(users)_ .

Enable private user groups by setting _USERGROUPS_ENAB yes_ in _/etc/login.defs_,
then comment out _GROUP=_ in _/etc/default/useradd_ . This creates a nonshared private
group for each user. If our Duchess user has her own private group, her _id_ output
shows _uid=1000(duchess) gid=1000(duchess)_ .

_HOME=_

sets the default directory for all user home directories. The default is _/home_ .

_INACTIVE=-1_

sets the number of days after a password expires until the account is locked. A
value of 0 disables the account as soon as the password expires, and a value of –1
disables locking the account.

_EXPIRE=_

sets an expiration date on the account, in YYYY-MM-DD format. For example, if
you set it to 2021-12-31, the account will be disabled on that date. Leaving
_EXPIRE=_ empty means the account will not expire.

**106** **|** **Chapter 5: Managing Users and Groups**

_SHELL=/bin/bash_

sets the default command shell. _/bin/bash_ is the most commonly used Linux shell.
Other values are any installed shell on the user’s system, such as _/bin/zsh_
or _/usr/bin/tcsh_ . _cat /etc/shells_ lists all installed shells.

_SKEL=/etc/skel_

sets the location for the files that you want automatically distributed to new users.
Most Linuxes put them in _/etc/skel_ . These are files such as _.bash_log‐_
_out_, _.bash_profile_ or _.profile_, _.bashrc_, and any other files you want new users to
have. You may edit these files to suit your own requirements. _SKEL_ is short for
skeleton.

_CREATE_MAIL_SPOOL=yes_

is a relic of olden times, and should be set to _yes_, as there may be some legacy
processes that still need it.

The following values in _/etc/login.defs_ are relevant to user creation defaults:

 - _USERGROUPS_ENAB yes_ enables private user groups.

 - _CREATE_HOME yes_ configures _useradd_ to automatically create private user
home directories. This does not apply to system users (see Recipe 5.3).

**Discussion**

The UID numbering range is defined in _/etc/login.defs_ . Every UID must be unique, so
the user account creation commands assign UIDs from the range defined in this file.
Typically, human UIDs start at 1000, and are automatically assigned by _useradd_ . You
can override this with the _-u_ option, but you must select an unused number that fol‐
lows the configured numbering scheme (see the Discussion in Recipe 5.6).

A mandatory password change at first login is a simple precaution against the origi‐
nal password possibly falling into the wrong hands as it passes from the administrator
to the user.

**See Also**

 - _man 8 useradd_

 - _man 5 login.defs_

 - _/etc/default/useradd_

 - _/etc/skel_

 - _/etc/login/defs_

**5.4 Changing the useradd Default Settings** **|** **107**

**5.5 Customizing the Documents, Music, Video, Pictures,**
**and Downloads Directories**

**Problem**

You followed Recipe 5.2 to create a new user, now you want to customize the Docu‐
ments, Music, Video, Pictures, and Downloads directories for new users.

**Solution**

Creating these directories is not a function of _useradd_, but rather the X Desktop
Group (XDG) user directories tool. The Documents, Music, Video, etc., directories
are called the _well-known user directories_ . These directories are set up from
the _/etc/xdg/user-dirs.defaults_ configuration file, which establishes the default configu‐
ration for all users:

```
  $ less /etc/xdg/user-dirs.defaults
  # Default settings for user directories
  #
  # The values are relative pathnames from the home directory and
  # will be translated on a per-path-element basis into the users locale
  DESKTOP=Desktop
  DOWNLOAD=Downloads
  TEMPLATES=Templates
  PUBLICSHARE=Public
  DOCUMENTS=Documents
  MUSIC=Music
  PICTURES=Pictures
  VIDEOS=Videos
  # Another alternative is:
  #MUSIC=Documents/Music
  #PICTURES=Documents/Pictures
  #VIDEOS=Documents/Videos
```

These are name-value pairs. The names cannot be changed. The values are the direc‐
tories that the names are mapped to, and they are relative to users’ home directories.
For example, DOCUMENTS is mapped to _/home/username/Documents_ . The directo‐
ries are created automatically for every new user when they start their graphical desk‐
top environments for the first time. You may comment out any directories you wish
to exclude or change the directories the names are mapped to.

Users may create their own personal configurations in _~/.config/user-dirs.dirs_ . The
directories must exist before applying the changes. The following example was cre‐
ated by our example user Duchess, who does not care for the boring default values.
Note that the name-value pair syntax is different in _~/.config/user-dirs.dirs_ :

**108** **|** **Chapter 5: Managing Users and Groups**

```
  XDG_DESKTOP_DIR="$HOME/table"
  XDG_DOWNLOAD_DIR="$HOME/landing-zone"
  XDG_DOCUMENTS_DIR="$HOME/omg-paperwork"
  XDG_MUSIC_DIR="$HOME/singendance"
  XDG_PICTURES_DIR="$HOME/piccies"
```

When your changes are complete and the new directories have been created, use the
_xdg-user-dirs-update_ command to apply your changes:

```
  duchess@pc:~$ xdg-user-dirs-update --set DOWNLOAD $HOME/landing-zone
  duchess@pc:~$ xdg-user-dirs-update --set DESKTOP $HOME/table
  duchess@pc:~$ xdg-user-dirs-update --set DOCUMENTS $HOME/omg-paperwork
  duchess@pc:~$ xdg-user-dirs-update --set MUSIC $HOME/singendance
  duchess@pc:~$ xdg-user-dirs-update --set PICTURES $HOME/piccies
```

Log out, then log back in, and you will see something like Figure 5-1. XDG applies
special icons to the well-known directories.

_Figure 5-1. Custom well-known directories_

The shortcuts in the side pane will not change, and the old directories are unchanged
except they do not have the special icons. You will have to change the shortcuts and
migrate the old directory contents manually.

Restore to the defaults in _/etc/xdg/user-dirs.defaults_ with this command:

```
  $ xdg-user-dirs-update --force
```

Log out and back in to see the changes. Again, none of your directories are removed
or changed in any way, except for the special icons that mark the well-known user
directories.

**5.5 Customizing the Documents, Music, Video, Pictures, and Downloads Directories** **|** **109**

**Discussion**

When you run the _xdg-user-dirs-update --set_ command, you must use only the names
as listed in _man 5 user-dirs.default_ :

```
  DESKTOP
  DOWNLOAD
  TEMPLATES
  PUBLICSHARE
  DOCUMENTS
  MUSIC
  PICTURES
  VIDEOS
```

Only the values, which are the target directories, are configurable. Target directories
must be relative to users’ home directories. If you want to use directories outside of
your home, create symlinks. For example, Duchess owns _/users/stuff/duchess_ and
stores music files in it. The following example links this directory to _/home/duchess/_
_singendance_ :

```
  duchess@pc:~$ ln -s /users/stuff/duchess /home/duchess/singendance
```

**See Also**

 - _man 5 user-dirs.defaults_

 - _man 1 xdg-user-dirs-update_

 - _man 5 user-dirs.conf_

 - [xdg-user-dirs at freedesktop](https://oreil.ly/FFDga)

**5.6 Creating User and System Groups with groupadd**

**Problem**

You want to create groups with _groupadd_ .

**Solution**

The following example creates a new user group _musicians_ :

```
  $ sudo groupadd musicians
```

Use _groupadd_ with the _-r_ option to create a system group:

```
  $ sudo groupadd -r service1

```

**110** **|** **Chapter 5: Managing Users and Groups**

**Discussion**

System groups differ from human user groups in the UID and GID numbering
ranges assigned to them. This is configured in _/etc/login.defs_ for _groupadd_ and _user‐_
_add_, as this example from Fedora 34 shows:

```
  # Min/max values for automatic uid selection in useradd(8)
  #
  UID_MIN         1000
  UID_MAX         60000
  # System accounts
  SYS_UID_MIN        201
  SYS_UID_MAX        999
  # Extra per user uids
  SUB_UID_MIN        100000
  SUB_UID_MAX       600100000
  SUB_UID_COUNT        65536

  #
  # Min/max values for automatic gid selection in groupadd(8)
  #
  GID_MIN         1000
  GID_MAX         60000
  # System accounts
  SYS_GID_MIN        201
  SYS_GID_MAX        999
  # Extra per user group ids
  SUB_GID_MIN        100000
  SUB_GID_MAX       600100000
  SUB_GID_COUNT        65536
```

These define the number ranges available to the system administrator. All others are
reserved for and managed by the system.

GID numbering is managed automatically by _groupadd_, according to the number
ranges defined in _/etc/login.defs_ You may override this with the _-g_ option, but your
chosen GID must fall within the defined range, and must not already be used.

**See Also**

 - _man 8 groupadd_

 - _/etc/login.defs_

**5.6 Creating User and System Groups with groupadd** **|** **111**

**5.7 Adding Users to Groups with usermod**

**Problem**

You want to assign users to groups.

**Solution**

Use the _usermod_ command. The following example adds Duchess to the _musicians_
group:

```
  $ sudo usermod -aG musicians duchess
```

This example adds Duchess to multiple groups:

```
  $ sudo usermod -aG musicians,composers,stagehands duchess
```

Alternatively, you could edit _/etc/group_ and type Duchess’s name after the appropriate
group or groups. When you list multiple group members, the list must be commadelimited, with no spaces between the names.

```
  musicians:x:900:stash,madmax,duchess

```

**Be Careful to Append, Not Replace**

If you forget the _-a_ option and use _-G_ alone, all of the user’s exist‐
ing groups will be removed and replaced with the new groups. This
is especially damaging if this removes users from their _sudo_ group.

When you change group memberships for logged-in users, users must log out and
then log back in to activate the changes. There are various workarounds to activate a
new group assignment without logging out, but they all have limitations, such as
being limited to the current shell. Groups are enumerated at login, so the most relia‐
ble solution is to log out and log back in.

**Discussion**

The _-a_ option means append, and _-G_ is group or groups.

**See Also**

 - _man 8 usermod_

**112** **|** **Chapter 5: Managing Users and Groups**

**5.8 Creating Users with adduser on Ubuntu**

**Problem**

You are running Debian or a Debian-based Linux, and need to know how to create
new users with _adduser_ .

**Solution**

_adduser_ walks you through a complete new user setup, like this example for Stash Cat:

```
  $ sudo adduser stash
  Adding user 'stash' ...
  Adding new group 'stash' (1009) ...
  Adding new user 'stash' (1009) with group 'stash' ...
  Creating home directory '/home/stash' ...
  Copying files from '/etc/skel' ...
  Enter new UNIX password:
  Retype new UNIX password:
  passwd: password updated successfully
  Changing the user information for stash
  Enter the new value, or press ENTER for the default
  Full Name []: Stash Cat
  Room Number []:
  Work Phone []:
  Home Phone []:
  Other []:
  Is the information correct? [Y/n]
```

Stash looks like this in _/etc/passwd_ :

```
  stash:x:1009:1009:Stash Cat,,,:/home/stash:/bin/bash
```

**Discussion**

The _adduser_ defaults are managed in _/etc/adduser.conf_ . This provides a number of
useful defaults such as:

_DSHELL=_

sets the default login shell. _/bin/bash_ is the most commonly used Linux shell.
Other values are any installed shell on the user’s system, such as _/bin/zsh_
or _/usr/bin/tcsh_ . _cat /etc/shells_ lists all installed shells.

_USERGROUPS=yes_

creates user private groups, _no_ puts all users into the same group.

_USERS_GID=100_

is required when _USERGROUPS=no_ is set.

**5.8 Creating Users with adduser on Ubuntu** **|** **113**

_EXTRA_GROUPS=_

is your list of supplemental groups for new users, for example,
_EXTRA_GROUPS="audio video plugdev libvirt"_ .

_ADD_EXTRA_GROUPS=1_

makes the groups listed in _EXTRA_GROUPS=_ the default for new users.

_/etc/adduser.conf_ contains the following user and group numbering scheme:

```
  FIRST_SYSTEM_UID=100
  LAST_SYSTEM_UID=999

  FIRST_SYSTEM_GID=100
  LAST_SYSTEM_GID=999

  FIRST_UID=1000
  LAST_UID=59999

  FIRST_GID=1000
  LAST_GID=59999-```

Fedora Linux includes _adduser_, but it is not really _adduser_, just a symlink to _useradd_ :

```
  $ stat /usr/sbin/adduser
  File: /usr/sbin/adduser -> useradd
  Size: 7  Blocks: 0  IO Block: 4096  symbolic link
  [...]
```

**See Also**

 - _man 5 adduser.conf_

**5.9 Creating a System User with adduser on Ubuntu**

**Problem**

You want to create a system user with _adduser_ on your Ubuntu (or Debian, Mint, or
other Debian derivative) system.

**Solution**

The following example creates a new system user, _service1_, with _adduser_, without a
home directory, and with its own unique primary group:

```
  $ sudo adduser --system --no-create-home --group service
  Adding system user 'service1' (UID 124) ...
  Adding new group 'service1' (GID 135) ...
  Adding new user 'service1' (UID 124) with group 'service1' ...
  Not creating home directory '/home/service1'.

```

**114** **|** **Chapter 5: Managing Users and Groups**

This is how it looks in _/etc/passwd_ :

```
  service1:x:124:135::/home/service1:/usr/sbin/nologin
```

**Discussion**

System users do not have home directories.

Back in olden times, it was common for services to run as the _nobody_ user and group,
except Debian which uses _nobody_ and _nogroup_ . Recycling the same user for multiple
services is a security weakness. It is unlikely you will ever have to create a system user,
as the common practice now is for the package installer to create a unique user and
group when you install a new service. But now you know how, just in case you ever
need to.

_nobody_ and _nogroup_ always have a real ID of 65534.

**See Also**

 - _man 8 adduser_

**5.10 Creating User and System Groups with addgroup**

**Problem**

You want to know how to create user and system groups with Debian’s _addgroup_
command.

**Solution**

The following example creates a human user group:

```
  $ sudo addgroup composers
  Adding group 'composers' (GID 1010) ...
  Done.
```

It looks like this in _/etc/group_ :

```
  composers:x:1010:
```

This example creates a new system group:

```
  $ sudo addgroup --system service1
  Adding group 'service1' (GID 136) ...
  Done.

```

**5.10 Creating User and System Groups with addgroup** **|** **115**

**Discussion**

The difference between user and system groups is they each have different numbering
ranges for UIDs and GIDs, which are configured in _/etc/adduser.conf_ .

**See Also**

 - _man 8 addgroup_

**5.11 Checking Password File Integrity**

**Problem**

There is a lot going on in all these user files and group files, and you want to know if
there is some kind of checker to verify that these files are written correctly.

**Solution**

The _pwck_ command checks the integrity of _/etc/passwd_ and _/etc/shadow_, and _grpck_
checks _/etc/group_ and _/etc/gshadow_ . They look for correct format, valid data, valid
names, and valid GIDs (see the man pages for a complete list). When you run these
with no options, they report both warnings and errors:

```
  $ sudo pwck
  user 'news': directory '/var/spool/news' does not exist
  user 'uucp': directory '/var/spool/uucp' does not exist
  user 'www-data': directory '/var/www' does not exist
  user 'list': directory '/var/list' does not exist

  $ sudo grpck
  group mail has an entry in /etc/gshadow, but its password field in /etc/group is
  not set to 'x'
  grpck: no changes
```

Add the **`-q`** option to report only errors:

```
  $ sudo pwck -q

  $ sudo grpck -q
  group mail has an entry in /etc/gshadow, but its password field in /etc/group
  is not set to 'x'
```

This shows an error in _/etc/gshadow_ . This is not a very helpful message because it’s
not really an error. It is not a common practice to place passwords on user groups, so
reporting this an as error is needlessly confusing. The other checks are useful, such as
the correct number of fields, and a unique valid group name.

You will never edit _/etc/shadow_ or _/etc/gshadow_, but only _/etc/passwd_ and _/etc/group_ .

**116** **|** **Chapter 5: Managing Users and Groups**

**Discussion**

The following example shows an error that must be corrected. Type **`n`**, when promp‐
ted, to prevent deleting the entries. The first “delete line” example is from _/etc/passwd_,
and the second is in _/etc/shadow_ :

```
  $ sudo pwck -q
  invalid password file entry
  delete line 'fakeservice:x:996:996::/home/fakeservice'? n
  delete line 'fakeservice:!:18469::::::'? n
  pwck: no changes
```

Then correct the line in _/etc/passwd_, and that will fix both error messages. In the
example, _fakeservice:x:996:996::/home/fakeservice_ is missing the last field, and should
be _fakeservice:x:996:996::/home/fakeservice:/bin/false_ .

The “directory does not exist” warnings for _/etc/passwd_ usually refer to default system
users that are not in use. For example:

```
  user 'www-data': directory '/var/www' does not exist
```

The _www-data_ user is unused when you are not running an HTTP server, and there
is no _/var/www_ directory until you install an HTTP server.

The “no changes” message means that no changes were made to the password file.

See the man pages for a complete list of checks.

**See Also**

 - _man 8 pwck_

 - _man 8 grpck_

**5.12 Disabling a User Account**

**Problem**

You want to disable a user account without deleting it.

**Solution**

To temporarily deactivate an account, disable the user’s password with the _passwd_
command:

```
  $ sudo passwd -l stash
  passwd: password expiry information changed.

```

**5.12 Disabling a User Account** **|** **117**

Now the user cannot log in. The following example unlocks the user’s account:

```
  $ sudo passwd -u stash
  passwd: password expiry information changed.
```

This does not prevent a user from logging in via a different authentication method,
such as an SSH key. To completely disable a user account, use _usermod_ :

```
  $ sudo usermod --expiredate 1 stash
```

When the user tries to log in, they see a “Your account has expired; please contact
your system administrator” message. Restore their account:

```
  $ sudo usermod --expiredate -1 stash
```

**Discussion**

Another way to disable a user is to replace the x in the password field in _/etc/passwd_
with an asterisk (*):

```
  stash:*:1009:1009:Stash Cat,,,:/home/stash:/bin/bash
```

Reenable Stash by replacing the asterisk with _x_ .

**See Also**

 - _man 1 passwd_

**5.13 Deleting a User with userdel**

**Problem**

You need to delete a user, and possibly their home directory and its contents.

**Solution**

The following example uses the _userdel_ command to delete the user Stash from _/etc/_
_passwd_, Stash’s primary group and all group memberships, and the shadow files:

```
  $ sudo userdel stash
```

If Stash belongs to a shared primary user group (discussed in Recipe 5.4), the group
will not be deleted.

Use the _-r_ option to delete the user’s home directory and its contents, and their mail
spool:

```
  $ sudo userdel -r stash

```

**118** **|** **Chapter 5: Managing Users and Groups**

If the user owns files outside of their home directory, you will have to find and take
care of them separately (see Recipe 5.16).

**Discussion**

Read your _/etc/passwd_ and _/etc/group_ files before and after deleting a user to see the
user disappear.

It is a good practice to clean up after removing a user.

**See Also**

 - _man userdel_

**5.14 Deleting a User with deluser on Ubuntu**

**Problem**

You’re running Ubuntu (or another Debian derivative) and want to use _deluser_ to
delete a user.

**Solution**

The following example deletes the user Stash from _/etc/passwd_, Stash’s primary group
from _/etc/group_, and their corresponding shadow files:

```
  $ sudo deluser stash
  Removing user 'stash' ...
  Warning: group 'stash' has no more members.
  Done.
```

_deluser_ will not remove the primary group of an existing user, so if Stash belongs to a
shared primary group it will not be removed.

This example removes Stash’s home directory and makes a backup of all the deleted
files:

```
  $ sudo deluser --remove-all-files --backup stash
```

**Discussion**

_--backup_ creates a compressed archive of the user’s files in the current directory. Use
the _--backup-to_ option to select a different directory:

```
  $ sudo deluser --remove-all-files --backup-to /user-backups stash
```

If the user owns files outside of their home directory, you will have to hunt them
down and deal with them manually (see Recipe 5.16).

**5.14 Deleting a User with deluser on Ubuntu** **|** **119**

**See Also**

 - _man 8 deluser_

**5.15 Removing a Group with delgroup on Ubuntu**

**Problem**

You have an Ubuntu system and want to use the _delgroup_ command to delete groups.

**Solution**

The following example removes the _musicians_ group:

```
  $ sudo delgroup musicians
```

_delgroup_ will not remove the primary group of an existing user. It will remove supple‐
mental groups even when they have members. If you do not want to remove groups
that have members, use the _--only-if-empty_ option:

```
  $ sudo delgroup --only-if-empty musicians
```

**Discussion**

The default behavior of _delgroup_ is configured in _/etc/deluser.conf_ and _/etc/_
_adduser.conf_ .

**See Also**

 - _man 8 delgroup_

**5.16 Finding and Managing All Files for a User**

**Problem**

You want to delete a user, but you don’t want a bunch of orphaned files left over, and
you need to find all of them.

**Solution**

The _find_ command will locate all files on the local system by UID or GID. The follow‐
ing example searches the entire root directory for all files owned by the user’s UID:

```
  $ sudo find / -uid 1007

```

**120** **|** **Chapter 5: Managing Users and Groups**

This can take some time if there are lot of files to search. If you are certain you do not
have to search the entire filesystem, you can narrow your search to specific subdirec‐
tories, such as _/etc_, _/home_, or _/var_ :

```
  $ sudo find /etc -uid 1007
  $ sudo find /home -uid 1007
  $ sudo find /var -uid 1007
```

You may also search by GID, username, or group name:

```
  $ sudo find / -gid 1007
  $ sudo find / -name duchess
  $ sudo find / -group duchess
```

Now that you know where all the files are, what to do with them? One option is to
change their ownership to another user and let the new user deal with them:

```
  $ sudo find /backups -uid 1007 -exec chown -v 1010 {} \;
  changed ownership of '/backups/duchess/' from 1007 to 1010
  changed ownership of '/backups/duchess/bin' from 1007 to 1010
  changed ownership of '/backups/duchess/logs' from 1007 to 1010
```

You could combine _find_ and _cp_ to find and copy all the files to a different directory:

```
  $ sudo find / -uid 1007 -exec cp -v {} /orphans \;
```

Using _cp -v_ prints progress messages and copies only the files and not their parent
directories. If you wish to copy the parent directories, use the _-r_ option:

```
  $ sudo find / -uid 1007 -exec cp -rv {} /orphans \;
```

Copying leaves the original files in place. After they are safely copied, you may wish
to delete the originals. One way to do this is to run _find_ again and use _rm_ to delete the
original files:

```
  $ sudo find / -uid 1007 -exec rm -v {} \;
```

This deletes the files but not the directories. Use the _-r_ option to delete the directories
if you are certain there are no other files in those directories that you want to keep:

```
  $ sudo find / -uid 1007 -exec rm -rv {} \;
```

One more option is to use _find_ and _mv_ to move the files to a different location:

```
  $ sudo find / -uid 1007 -exec mv {} /orphans \;
```

If you see a “No such file or directory” message, usually that is because the file or
directory was moved, which you can verify by looking in the directory they were
moved to.

Find files owned by a nonexistent user or group:

```
  $ find / -nouser
  $ find / -nogroup

```

**5.16 Finding and Managing All Files for a User** **|** **121**

**Discussion**

Be careful with _mv_ and _rm_ because there is no undo. If you make a mistake, your best
hope of recovery is from backup.

Cleaning up after departed users can be a chore, because computers make it too easy
to create as many files as your storage will hold. If you find yourself thinking that _find_
is taking too long, keep in mind it will find everything while you go do something
else.

**See Also**

 - _man 1 find_

 - _man 1 mv_

 - _man 1 cp_

 - _man 1 rm_

**5.17 Using su to Be Root**

**Problem**

You need to know how to get root permissions to perform some administration
chores.

**Solution**

Use the _su_ command to change to the root user when you need to do system chores:

```
  duchess@pc:~$ su -l
  Password:
  root@pc:~#
```

If you do not know root’s password, or if there is no root password, see Recipe 5.21 to
learn how to use _sudo_ to set a root password.

When you are finished, exit root and return to your own account:

```
  root@pc:~# exit
  logout
  duchess@pc:~$
```

The _-l_ option invokes the root user’s environment, changing to root’s home directory
and loading root’s environment variables. Omit _-l_ to keep your own environment:

```
  duchess@pc:~$ su
  Password:
  root@pc:/home/duchess~#

```

**122** **|** **Chapter 5: Managing Users and Groups**

**Discussion**

You can change to any user, as long as you have their password.

Using _su_ to change to root gives you absolute power over your system, and every
command that you run is run as root. Consider using _sudo_ (see Recipe 5.18), which
provides some safety features, such as protecting root’s password and leaving an audit
trail.

**See Also**

 - _man 1 su_

**5.18 Granting Limited Root Powers with sudo**

**Problem**

You want to delegate some system administration chores to other users, and you want
to limit their root powers to what is needed for their specific tasks.

**Solution**

Use the _sudo_ command. _sudo_ is safer than _su_ because it grants limited root powers to
specific users for specific tasks, logs activity, and caches the user’s password for a limi‐
ted amount of time, with a default of 15 minutes. After 15 minutes, the user must
provide _sudo_ with their password again. The caching duration is configurable. _sudo_
protects root’s password because _sudo_ users use their own passwords.

Some Linux distributions, such as openSUSE, default to _sudo_ ask‐
ing for the root user’s password. See Recipe 5.22 to learn how to
change this.

_/etc/sudoers_ is the configuration file, and you should edit it with a special command,
_visudo_ . This opens _/etc/sudoers_ with your default text editor, and you can review and
edit the default configuration. Once again, Duchess demonstrates for us:

```
  duchess@pc:~$ sudo visudo
  [sudo] password for duchess:
  [...]
  ##Allow root to run any commands
  root  ALL=(ALL) ALL

  # Allow members of group sudo to execute any command

```

**5.18 Granting Limited Root Powers with sudo** **|** **123**

```
  %sudo  ALL=(ALL) ALL
  [...]
```

_%sudo ALL=(ALL) ALL_ means that any user you add to the _sudo_ group gets full _sudo_
powers just like root. The percent sign indicates _%sudo_ is a group from _/etc/group_,
and not a group configured in _/etc/sudoers_ .

Suppose you have a junior admin, Stash, whose job is installing and removing soft‐
ware and keeping the system updated. You could create a system group for Stash. Or
you could configure Stash for this task in _/etc/sudoers_ . The following example gives
Stash _sudo_ powers to run the listed commands. You need the username, the hostname
of the local machine, and a comma-delimited list of allowed commands:

```
  stash server1 = /bin/rpm, /usr/bin/yum, /usr/bin/dnf
```

Suppose you want to give Stash more admin chores, such as managing services. The
allowed commands list will get long, so you could create some command aliases
instead. The following example aliases the software management commands to
SOFTWARE, and the service management commands to SYSTEMD:

```
  Cmnd_Alias SOFTWARE = /bin/rpm, /usr/bin/yum, /usr/bin/dnf
  Cmnd_Alias SYSTEMD = /usr/bin/systemctl start, /usr/bin/systemctl stop,
  /usr/bin/systemctl reload, /usr/bin/systemctl restart, /usr/bin/systemctl
  status, /usr/bin/systemctl enable, /usr/bin/systemctl disable,
  /usr/bin/systemctl mask, /usr/bin/systemctl unmask
```

Now Stash’s configuration looks like this:

```
  stash server1 = SOFTWARE, SYSTEMD
```

You may create user groups in _/etc/sudoers_ (not related to system groups in _/etc/_
_group_ ), then assign them some command aliases:

```
  User_Alias JRADMIN = stash, madmax

  JRADMIN server1 = SOFTWARE, SYSTEMD
```

You may create a _Host_Alias_ to give a user _sudo_ rights on multiple machines:

```
  Host_Alias SERVERS = server1, server2, server3
```

Then bring in the JRADMINs:

```
  JRADMIN SERVERS = SOFTWARE, SYSTEMD
```

**Discussion**

When your limited _sudo_ users try to run a not-allowed command, they see this mes‐
sage: “Sorry, user _duchess_ is not allowed to execute _`/some/command`_ as root on _server2_ .”

Don’t put too much faith in limiting users to a specific set of commands. Many every‐
day applications provide a means for privilege escalation via shell escape, and your
users can gain full root powers. This example shows how it works with _awk_ :

**124** **|** **Chapter 5: Managing Users and Groups**

```
  $ sudo awk 'BEGIN {system("/bin/bash")}'
  root@client4:/home/duchess#
```

And just like that, Duchess has full root powers. The humble _less_ command also pro‐
vides a shell escape. Read a file with _less_ that is large enough to require paging:

```
  $ sudo less /etc/systctl.conf
  #
  # /etc/sysctl.conf - Configuration file for setting system variables
  # See /etc/sysctl.d/ for additional system variables.
  # See sysctl.conf (5) for information.
  /etc/sysctl.conf
```

Type **`!`** **_`sh`_**, then when the prompt changes, type **`whoami`** :

```
  duchess@client4:~$ sudo less /etc/systctl.conf
  #
  # /etc/sysctl.conf - Configuration file for setting system variables
  # See /etc/sysctl.d/ for additional system variables.
  # See sysctl.conf (5) for information.
  !'sh'
  duchess@client4:~$ sudo less /etc/sysctl.conf
  # whoami
  root
```

Type **`exit`** to return your normal shell.

In my experience, it is extremely difficult to keep track of the many applications that
can provide a shell escape. _journalctl_ records everything, should you wish to monitor
your _sudo_ users (see Recipe 20.1).

In some Linuxes, such as Fedora, the _wheel_ group is the default _sudo_ group. Check
your _/etc/sudoers_ file to see how your distribution configures this. You can also create
your own _sudo_ group, and name it whatever you want.

The _/etc/sudoers_ file controls users only on the local machine. Including other
machines, like the SERVERS alias, allows you to share a single configuration file on
multiple machines. _sudo_ ignores any items, such as hosts or users, that are not present
on the local machine.

Let’s dissect _root ALL=(ALL) ALL_ to understand what all those ALLs mean.

_root_

is in the user field, and this field holds any single user, user alias, or system group.

_ALL=_

is in the host field. ALL means any host anywhere, or you could use a host alias,
or name a single host.

_(ALL)_

is in the optional users field. _(ALL)_ means the user or users can run commands as
any other user, or you can specify certain users.

**5.18 Granting Limited Root Powers with sudo** **|** **125**

_ALL_

in is the command field. _ALL_ is unrestricted, or you can specify a list of allowed
commands.

**See Also**

 - _man 8 sudo_

 - _man 5 sudoers_

**5.19 Extending the sudo Password Timeout**

**Problem**

On most Linux distributions, _sudo_ caches passwords for a default interval of 15
minutes. Then after 15 minutes you have to enter your password again. You are tired
of having to enter your password so often when you have a lot of work to do, and
want to make the caching interval longer.

**Solution**

Change the caching interval in _/etc/sudoers_ . Open the file for editing with _visudo_ :

```
  $ sudo visudo
```

Then look for a _Defaults_ line and set your new cache interval. The following example
sets it to 60 minutes:

```
  $ Defaults timestamp_timeout=60
```

If you set it to 0, _sudo_ asks for your password every time you use it.

If you set _timestamp_timeout_ to a negative number, like _-1_, your password never
expires.

**Discussion**

The _sudo_ password caching is a useful protection against accidents, such as forgetting
you are running as root or wandering away and allowing someone else to have some
fun with your computer.

**See Also**

 - _man 8 sudo_

 - _man 5 sudoers_

**126** **|** **Chapter 5: Managing Users and Groups**

**5.20 Creating Individual sudoers Configurations**

**Problem**

You want to set some different _sudo_ configurations for your users; for example, you
want your junior admins to have a different password timeout than you. Yours is
long, and you want theirs to be short.

**Solution**

You may create individual configurations in _/etc/sudoers.d_ . The following example
creates a 30-minute password timeout for Stash:

```
  $ cd /etc/sudoers.d/
  $ sudo visudo -f stash
```

Type **`Defaults timestamp_timeout=30`**, save the file, and you’re done. You can see
the new file:

```
  $ sudo ls /etc/sudoers.d/
  README stash
```

You only need to enter configuration items that are different from the entries in _/etc/_
_sudoers_, not to replicate the whole file.

**Discussion**

This is a nice feature for managing multiple users. Instead of managing one big con‐
figuration file, break it up into smaller per-user files.

**See Also**

 - _man 8 sudo_

 - _man 5 sudoers_

**5.21 Managing the Root User’s Password**

**Problem**

Your Linux distribution set you up as system administrator during installation, with
unrestricted _sudo_ privileges, and did not create a root password. Or, your root user
had a password but you forgot it. You need to know how to give root a new password.

**5.20 Creating Individual sudoers Configurations** **|** **127**

**Solution**

When you want to run as “real” root, use _sudo_ to _su_ to root:

```
  duchess@pc:~$ sudo su -l
  [sudo] password for duchess:
  root@pc:~#
```

At this point you can use the _passwd_ command to give root a password so you can log
in as root directly, or reset a lost root password.

**Discussion**

There are times when you need a root password and not _sudo_ ; for example, when you
boot to an emergency runlevel.

**See Also**

 - _man 8 sudo_

 - _man 5 sudoers_

 - _man 1 passwd_

**5.22 Changing sudo to Not Ask for the Root Password**

**Problem**

You want your _sudo_ users to authenticate with their own passwords, but your Linux
system asks for the root user’s password, like the following example:

```
  $ sudo visudo
  [sudo] password for root:
```

**Solution**

This is the default behavior on some Linux distributions, such as openSUSE.

When you install Ubuntu Linux and make your user an administrator during instal‐
lation, Ubuntu configures your user appropriately with full _sudo_ powers, equivalent
to root but using your own password. openSUSE does not, but instead configures
your user to use the password of the target user, which is root.

To set up _sudo_ users to always be asked for their own passwords, edit _/etc/sudoers_ by
commenting out these two lines:

```
  duchess@pc:~$ sudo visudo

```

**128** **|** **Chapter 5: Managing Users and Groups**

```
  # Defaults targetpw
  # ALL  ALL=(ALL) ALL
```

In openSUSE and Fedora, create _sudo_ users with full root powers by adding them to
the _wheel_ group in _/etc/group_ . (For limited users, refer to Recipe 5.18.)

The change takes effect immediately after saving your changes and closing the file.

**Discussion**

Protecting the root user’s password is a primary reason to use _sudo_, rather than _su_ .

**See Also**

 - Recipe 5.18

**5.22 Changing sudo to Not Ask for the Root Password** **|** **129**

**<u>CHAPTER 6</u>**
#### **Managing Files and Directories**

Linux provides strong basic controls for access to files and directories with configura‐
ble privileges. Every file and directory has three levels of ownership, including user,
group, and other; and multiple levels of access, including read, write, and execute.
You can protect your personal files and control who has access to them, and the root
user can manage access to commands, scripts, shared files, and system files.

Even when you are using stronger access control tools—tools such as SELinux or
AppArmor—it is still important to get the fundamentals right.

On a Linux system, both human users and system services have user accounts. Some
system services need user accounts to control privileges, just like human users.

Every file has three types of ownership: owner, group, and other (sometimes _other_ is
expressed as _world_ ). The owner is a single user, the group owner is a single group, and
other is everyone else who has access to the file.

Every file has six permission modes—read, write, and executable—and three special
modes: the _sticky bit_, _setuid_, and _setgid_ .

File permissions control which users can create, read, edit, or delete a file, and which
users can execute a command. The special modes control who can move, delete, or
rename a file, and who can execute a command with elevated privileges.

Directory permissions control which users can edit or enter a directory and who can
read, edit, add, or remove files from a directory.

Remember the fundamental Linux security principle: use the minimum necessary
privileges to get the job done.

**131**

**Limitations of Privileges**

Anyone who can read a file can copy it.

You cannot prevent the root user, or _sudo_ users with sufficient priv‐
ileges, from accessing your files.

Permissions and ownership are functions of filesystems and can be
bypassed by reading a storage device from another Linux instance,
such as booting up a live Linux from removable media to access the
host system, or removing the hard drive and connecting it to a dif‐
ferent machine. You only need root privileges on the system that
you mount the storage device on, and do not need to know any‐
thing about the original file owners and permissions.

On a Linux system the root user, also called the superuser, reigns supreme. Root can
do almost anything, including editing and deleting other users’ files, entering any
directory, and running any command. Normal, or unprivileged, users may temporar‐
ily assume root powers with the _sudo_ or _su_ commands (see Recipes 5.17 and 5.18).

Every user has a unique identification (UID), and belongs to at least one group (see
Recipe 5.1). Every user in a group shares the permissions of that group.

To see what all of this looks like, take a look at _/etc_, which contains system configura‐
tion files:

```
  $ stat --format=%a:%A:%U:%G /etc
  755:drwxr-xr-x:root:root
```

The command output shows the directory’s _mode_, or set of permissions, in two
forms, _755:drwxr-xr-x_ . _755_ is octal notation, and _drwxr-xr-x_ is symbolic notation.
These are two different ways of expressing the same mode, which in this example is
unrestricted privileges for the directory owner, and group and other may only enter
the directory. File modes are discussed in detail in this chapter.

_root:root_ is the owner and group. Files and directories can have different owners and
groups; for example, _/etc/cups_ is owned by _root:lp_ .

In this chapter you will learn about the special modes: the _sticky bit_, _setuid_, and _setgid_ .
The setuid and setgid modes elevate user and group permissions to the same level as
the file owner. These are used only in special cases, and used very carefully because
privilege escalation is a potential security risk. The sticky bit prevents anyone but the
file owner, or anyone with root privileges, from deleting, renaming, or moving files
they do not own in a directory, such as _/tmp_ .

You will learn how to set ownership and modes, create and delete files and directo‐
ries, configure default privileges, transfer file ownership to a different user or group,
and copy, move, and rename files and directories.

**132** **|** **Chapter 6: Managing Files and Directories**

**Using sudo**

Most of the examples in this recipe use the dollar sign command
prompt, $, which indicates an unprivileged user. Depending on
your own file permissions, you may need _sudo_ for some operations.

**6.1 Creating Files and Directories**

**Problem**

You want to organize your files by placing them in directories.

**Solution**

Use the _mkdir_ command to create directories. The following example creates a new
subdirectory in the current directory:

```
  $ mkdir -v presentations
  mkdir: created directory 'presentations'
```

Create a subdirectory two levels down inside the current directory, and its parent
directories, with the _-p_ (parent) option:

```
  $ mkdir -p presentations/2020/august
  mkdir: created directory 'presentations/2020'
  mkdir: created directory 'presentations/2020/august'
```

Create a new top-level directory, which is relative to root, /. You need root privileges
to do this:

```
  $ sudo mkdir -v /charts
  mkdir: created directory '/charts'
```

You can set permissions when you create a directory:

```
  $ mkdir -m 0700 /home/duchess/dog-memes
```

Files are created by applications, such as word processors and image editors, and spe‐
cial commands like _touch_ . The _touch_ command creates a new empty file:

```
  $ touch newfile.txt
```

See Recipe 6.2 to learn how to use _touch_ to quickly create batches of files for testing.

**Discussion**

If you are having trouble visualizing file trees, and how all directories are relative to /,
try the _tree_ command. Root, /, is at the top:

```
  $ tree -L 1 /
  /
  ├── backups

```

**6.1 Creating Files and Directories** **|** **133**

```
  ├── bin
  ├── boot
  [...]
```

You have probably noticed that this is upside down. In the real world, trees branch
from the root, but the _tree_ command displays the directory tree branching down‐
ward. There is a reason for this: we read screens from the top down.

This example lists only the top-level directories under root. _-L 2_ shows second-level
directories, _-L 3_ goes to three levels, and so on.

**See Also**

 - Recipe 6.2

 - _man 1 mkdir_

 - _man 1 touch_

 - _man 1 yes_

 - _man 1 tree_

**6.2 Quickly Creating a Batch of Files for Testing**

**Problem**

You want to create batches of files to use for testing file permissions, and for any test‐
ing that needs a lot of files in a hurry.

**Solution**

Use the _touch_ command. The following example creates a single new empty file:

```
  $ touch newfile.txt
```

Create 100 new empty files:

```
  $ touch file{00..99}
```

This creates 100 new files named _file00_, _file01_, _file02_, and so on. You may give them
file extensions and name them anything:

```
  $ touch test{00..99}.doc
  $ ls
  test00.doc
  test01.doc
  test02.doc
  [...]

```

**134** **|** **Chapter 6: Managing Files and Directories**

Put the numbers first in the filename for easy ordering:

```
  $ touch {00..99}test.doc
  $ ls
  00test.doc
  01test.doc
  02test.doc
  [...]
```

A fast way to populate the files with content is to use the _yes_ command. The following
example creates a 500 MB file filled with the repeated line “This is a test file”:

```
  $ yes This is a test file | head -c 500 MB > testfile.txt
```

Create a batch of 100 files with 1 MB of content in each file:

```
  $ for x in {01..100};
  > do yes This is a test file | head -c 1MB > $x-testfile.txt;
  > done
```

The new files look like this:

```
  001-testfile.txt
  002-testfile.txt
  003-testfile.txt
  [...]
```

**Discussion**

You may customize this command in a number of ways: filenames, file sizes, number‐
ing, and the text for _yes_ .

The examples in the recipe pad the numbers in the filenames with leading zeroes so
they will order correctly. Most graphical file managers handle ordering numbered
filenames correctly, but the default for _ls_ is lexicographic order. The following exam‐
ple demonstrates this with a 1- to 3-digit numbering range:

```
  $ touch {0..150}test.doc
  $ ls -C1
  0test.doc
  100test.doc
  101test.doc
  102test.doc
  103test.doc
  104test.doc
  105test.doc
  106test.doc
  107test.doc
  108test.doc
  109test.doc
  10test.doc
  110test.doc
  111test.doc

```

**6.2 Quickly Creating a Batch of Files for Testing** **|** **135**

```
  112test.doc
  113test.doc
  114test.doc
  115test.doc
  116test.doc
  117test.doc
  118test.doc
  119test.doc
  11test.doc
  120test.doc
  121test.doc
  [...]
```

Lexicographic ordering treats the filenames as text strings instead of integers and
characters, and compares each number and letter individually, from left to right. Lex‐
icographic ordering doesn’t know that 10 is smaller than 100, only that 101 follows
100, 102 follows 101, and 10t follows 109 because letters follow numbers, so the _t_
follows the _9_ .

You can use leading zeroes to make all the numbers the same number of characters,
or list your files with _ls -v_ . This treats the numbers in filenames as integers and not
characters, so they are listed in correct numerical order.

**See Also**

 - _man 1 ls_

 - _man 1 touch_

 - _man 1 yes_

**6.3 Working with Relative and Absolute Filepaths**

**Problem**

You need to understand the difference between relative and absolute filepaths, and
how to find where you are in the filesystem.

**Solution**

Absolute filepaths always start at the root, _/_, such as _/boot_ and _/etc_ . Relative filepaths
are relative to your current directory and do not have a leading slash. Suppose you
are in your home directory and it contains the following subdirectories:

```
  madmax@client2:~$ ls --group-directories-first
  Audiobooks
  bin
  Desktop

```

**136** **|** **Chapter 6: Managing Files and Directories**

```
  Documents
  Downloads
  games
  Music
  Pictures
  Public
  Templates
  Videos
```

In this example, the absolute path to _Audiobooks_ is _/home/madmax/Audiobooks_, and
the relative path is _Audiobooks_ . Use the _cd_ command to enter this directory with
either the absolute path:

```
  $ cd /home/madmax/Audiobooks
```

Or the relative path:

```
  $ cd Audiobooks
```

The directory you are in is the current working directory, _cwd_ . Confirm your _cwd_
with the _pwd_ (print working directory) command:

```
  $ pwd
  /home/madmax
```

**Discussion**

Absolute and relative filepaths are a common source of confusion. Remember that
when the filepath begins with a slash (/), it is an absolute path. When there is no lead‐
ing slash, it is relative to your current working directory.

Some applications and commands require relative paths; for example, _rsync_ _include_
and _exclude_ lists use filepaths that are relative to the directories being copied.

**See Also**

 - _man 1 pwd_

 - Chapter 7

**6.4 Deleting Files and Directories**

**Problem**

You had fun creating a bunch of files and directories, and now you want to get rid of
them.

**6.4 Deleting Files and Directories** **|** **137**

**Solution**

Use the _rm_ (remove) command with caution, because _rm_ will happily delete every‐
thing you tell it to, so be sure you tell it the right files or directories to delete.

Delete a single file, with verbose output:

```
  $ rm -v aria.ogg
  removed 'aria.ogg'
```

Use the _-i_ flag to prompt for confirmation first:

```
  $ rm -iv intermezzo.wav
  rm: remove regular file 'intermezzo.wav'? y
  removed 'intermezzo.wav'
```

Add the _-r_ (recursive) flag to delete a directory and all of its files and subdirectories.
Combining _-r_ with _-i_ will prompt you for confirmation before each deletion:

```
  $ rm -rvi rehearsals
  rm: descend into directory 'rehearsals'? y
  rm: remove regular file 'rehearsals/brass-section'? y
  [...]
```

If you are confident you don’t need to be prompted for every deletion, omit the _-i_
option.

This example deletes only the _jan_ subdirectory:

```
  $ rm -rv rehearsals/2020/jan
```

This example deletes the _rehearsals_ directory and all of its files and subdirectories:

```
  $ rm -rv rehearsals
```

Use wildcards to match file names to delete, for example by file extension:

```
  $ rm -v *.txt
```

Or by files named with the same text strings:

```
  $ rm -v aria*
```

If _rm_ refuses to delete a file or directory, and you are certain you want to delete it, add
the _-f_ (force) option.

**Discussion**

_rm -rf /_ will erase your entire root filesystem (if you have root privileges). Some folks
think it is a funny prank to tell newbies to do this. It is not funny. It is fun to run it on
a test machine, or on a virtual machine, and observe how long the system keeps run‐
ning because processes in memory are still running, even though the filesystem is
erased from disk.

**138** **|** **Chapter 6: Managing Files and Directories**

**See Also**

 - _man 1 rm_

**6.5 Copying, Moving, and Renaming Files and Directories**

**Problem**

You have directories, and you have files. You want to move files into the directories,
change filenames, and make copies.

**Solution**

Use the _cp_ command for copying, and the _mv_ command for moving or renaming.

This example copies two files from the current working directory into the _~/songs2_
directory:

```
  $ cp -v aria.ogg solo.flac ~/songs2/
  'aria.ogg' -> '/home/duchess/songs2/aria.ogg'
  'solo.flac' -> '/home/duchess/songs2/solo.flac'

```

**The Tilde Represents Your Home Directory**

The tilde is short for your home directory, so in the example, _~/_
_songs2_ is the same as _/home/duchess/songs2/_ .

Copy a directory and all of its contents with the _-r_ (recursive) option:

```
  $ cp -rv ~/music/songs2 /shared/archives
```

The recursive example only copies the directory and its files. Use the _--parents_ option
to preserve parent directories. The following example copies _songs1_ and its contents,
and preserves the filepath _duchess/music/songs2/_ :

```
  $ cp -rv --parents duchess/music/songs2/ shows/
  duchess -> shows/duchess
  duchess/music -> shows/duchess/music
  'duchess/music/songs2' -> 'shows/duchess/music/songs2'
  'duchess/music/songs2/intro.flac' -> 'shows/duchess/music/songs2/intro.flac'
  'duchess/music/songs2/reprise.flac' -> 'shows/duchess/music/songs2/reprise.flac'
  'duchess/music/songs2/solo.flac' -> 'shows/duchess/music/songs2/solo.flac'
```

The other contents of _duchess_ and _music_ are not copied, only _songs2_ and its contents.

**6.5 Copying, Moving, and Renaming Files and Directories** **|** **139**

Use the _mv_ command to move and rename files. This example moves two files to
another directory:

```
  $ mv -v aria.ogg solo.flac ~/songs2/
  renamed 'aria.ogg' -> '/home/duchess/songs2/aria.ogg'
  renamed 'solo.flac' -> '/home/duchess/songs2/solo.flac'
```

The following example moves a directory into another directory:

```
  $ mv -v ~/songs2/ ~/music/
```

**Discussion**

Some useful _cp_ options are:

 - _-a, --archive_ preserves all the file attributes, such as mode, ownership, and time‐
stamps.

 - _-i, --interactive_ prompts before overwriting destination files.

 - _-u, --update_ overwrites an existing destination file only if the source file is newer.
This saves time when you’re recopying a batch of files, and some of the copies are
unchanged. ( _rsync_ is better for efficient file transfers by copying only changes, see
Chapter 7.)

_mv_ has some useful options:

 - _-i, --interactive_ prompts before overwriting destination files.

 - _-n, --no-clobber_ prevents overwriting destination files.

 - _-u, --update_ moves your files only when they are newer than the destination files,
or when they are moved for the first time.

**See Also**

 - _man 1 cp_

 - _man 1 mv_

**6.6 Setting File Permissions with chmod’s Octal Notation**

**Problem**

You know that the _chmod_ (change mode) command supports both octal and symbolic
notation, and you want to use octal notation to manage file permissions.

**140** **|** **Chapter 6: Managing Files and Directories**

**Solution**

The following examples show how to set different permissions on files using octal
notation. The first example grants read-write access to the owner of the _file.txt_ file,
and excludes all access for group and world:

```
  $ chmod -v 0600 file.txt
  mode of 'file.txt' changed from 0644 (rw-r--r--) to 0600
  (rw-------)
```

The file owner can read, edit, and delete the file, while other users can do nothing
with it, not even read it, though they can see it listed in a file manager.

Make a file world readable and writeable, allowing everyone to do whatever they want
to it:

```
  $ chmod 0666 file.txt
```

In the next example, _file.txt_ is changed to read-write for the file owner and read-only
for group and world:

```
  $ chmod -v 0644 file.txt
  mode of 'file.txt' changed from 0666 (rw-rw-rw-) to 0644 (rw-r--r--)
```

A common permission set is to give the owner and group the same permissions, such
as read-write, and to exclude other:

```
  $ chmod 0660 file.txt
```

Commands and scripts require the executable bit to be set. This example makes the
_backup.sh_ script executable and read-write for the owner, executable and readable for
group, and inaccessible to other:

```
  $ chmod 0750 backup.sh
```

Octal notation has four fields, but you probably will use the last three fields the most
often, and the first field rarely. The first field is reserved for the special modes (see
Recipe 6.8).

**Discussion**

Octal notation uses integers 0-7. Table 6-1 shows the relationship between owners
and permissions.

_Table 6-1. Octal fields_

**<mark>Mode</mark>** **<mark>Owner</mark>** **<mark>Group</mark>** **<mark>Other</mark>**
Read 4 4 4

Write 2 2 2

Execute 1 1 1

No permission 0 0 0

**6.6 Setting File Permissions with chmod’s Octal Notation** **|** **141**

A file or directory has one user owner, and one group owner. _Other_ is everyone else.
A directory or executable that is unrestricted to everyone is mode 0777, and an unre‐
stricted file is mode 0666.

When you’re not familiar with Linux file permissions, it might help to see them in
another view, like in Table 6-2.

_Table 6-2. Linux file permissions_

**<mark>Permission</mark>** **<mark>Description</mark>**
_7_ Read, write, execute. Directories differ from files because all directories require the executable bit set. You can
assign a directory any permissions, just like a file, but without the executable bit no one can enter the directory
(with the _cd_ command or in a file manager). Scripts and binary commands must have the executable bit set, or
they will be treated as ordinary files.

_6_ Read and write.

_5_ Read and execute. This is a common permission for commands.

_4_ Read.

_3_ Write and execute.

_2_ Write.

_1_ Execute.

_0_ No permission.

**See Also**

 - _man 1 chmod_

 - Recipe 6.8

**6.7 Setting Directory Permissions with chmod’s Octal**
**Notation**

**Problem**

You know that permissions are managed a little differently on directories, and you
want to manage them with chmod’s octal notation.

**Solution**

Directories must have the executable bit set. This might sound a little strange, but it is
necessary for entering the directory with the _cd_ command or with a file manager.

The following examples creates a shared directory:

```
  $ sudo mkdir /shared

```

**142** **|** **Chapter 6: Managing Files and Directories**

This example makes _/shared_ read-write for the owner and read-only for everyone
else:

```
  $ chmod 0755 /shared
```

The owner has unrestricted privileges to the directory. Group and world may enter
the directory and read files, but not edit or add files.

This example applies the same permissions to the existing contents of the directory,
using the _-R_ (recursive) option:

```
  $ chmod -R 0755 /shared
```

The next example restricts the directory and its existing contents to the directory
owner. Files and directories inside the directory may have different owners and per‐
missions, but are still inaccessible to group and world:

```
  $ chmod 0700 /shared
```

A common permission set is to give the owner and group the same permissions, such
as read-write-execute, and to exclude other:

```
  $ chmod 0770 /shared
```

**Discussion**

You have a lot of power with groups and directories to control file access. Set up
groups according to function, for example various teams could each have their own
exclusive shared directories. Most shops don’t need super-fine-grained control and
default to more sharing rather than less. Whatever your needs are, the old _chmod_
command is still the fundamental tool for controlling file permissions.

**See Also**

 - _man 1 chmod_

**6.8 Using the Special Modes for Special Use Cases**

**Problem**

You want to set some permissions not supported by the traditional user-group-other
set of permissions, such as allowing unprivileged users to run a command that
requires elevated permissions, protecting files in a directory shared by multiple users,
or enforcing certain file permissions in a directory.

**6.8 Using the Special Modes for Special Use Cases** **|** **143**

**Solution**

The special modes are _sticky bit_, _setuid_, and _setgid_ (see Table 6-3). The sticky bit is
applied to directories that contain files owned by multiple users, to prevent users
from moving, renaming, or deleting files they do not own:

```
  $ chmod -v 1770 /home/duchess/shared
  mode of '/home/duchess/shared changed from 0770 (rwxrwx---) to 1770 (rwxrwx--T)
```

_setuid_ is applied to executable files, to elevate any user running the command to the
same permissions as the owner:

```
  $ chmod 4750 backup-script
  mode of 'backup-script' changed from 0750 (rwxrw----) to 4770 (rwsrwx---)
```

Apply _setgid_ to a directory, so that all newly created files in the directory are assigned
to the same group as the directory’s group owner. This is a nice trick for enforcing
correct ownership in a shared directory:

```
  $ chmod 2770 /home/duchess/shared
  mode of '/home/duchess/shared' changed from 0770 (rwxrwx---) to 2770 (rwxrws---)
```

_setgid_ may also be applied to files, changing the effective group of the user to the same
group as the file owner.

**Discussion**

_setgid_ and _setuid_ have the potential to create security holes for an intruder or an
untrustworthy user. It is a best practice to use them only when you can’t think of a
safer way to accomplish what you want to do, such as using group assignments or
_sudo_ .

_setuid_ is useful for executable files.

_setgid_ is useful for directories and files.

The sticky bit is only for directories. Table 6-3 shows the relationship of permissions
to owners.

_Table 6-3. Octal fields_

**<mark>Mode</mark>** **<mark>Special modes</mark>** **<mark>Owner</mark>** **<mark>Group</mark>** **<mark>World</mark>**
Read 4 4 4

Write 2 2 2

Execute 1 1 1

setuid 4

setgid 2

Sticky bit 1

No permission 0 0 0 0

**144** **|** **Chapter 6: Managing Files and Directories**

The special mode values may be combined (see Table 6-4).

_Table 6-4. Sticky bit/setgid/setuid values_

**<mark>Option name</mark>** **<mark>Octal value</mark>**
No option set 0

Sticky bit set 1

setgid 2

Sticky bit and setgid 3

setuid 4

Sticky bit and setuid 5

setgid and setuid 6

Sticky bit, setgid, and setuid 7

A more descriptive name for the sticky bit is _restricted deletion bit_ . This bit prevents
unprivileged users from removing or renaming a file in a directory, unless they own
the file. You can see this on your _/tmp_ directory, which is world readable and writea‐
ble, and contains files owned by multiple users. Using the sticky bit prevents users
from moving, renaming, or deleting files they do not own, even if they have write
privileges on some files they do not own:

```
  $ stat --format=%a:%A:%U:%G /tmp
  1777:drwxrwxrwt:root:root
```

The sticky bit is the 1 in 1777.

_setgid_ means set group user identification, and _setuid_ is set user identification. These
are used to elevate the permissions of an unprivileged user to the same as the user or
group owner. This is how unprivileged users can use the _passwd_ command to change
their own passwords, even though only root has write permissions on _/etc/passwd_,
and everyone else has only read and execute permissions:

```
  $ stat --format=%a:%A:%U:%G /usr/bin/passwd
  4755:-rwsr-xr-x:root:root
```

In _/etc/passwd_ the 4 in 4755 is _setuid_, which means all users have root powers when
they run the command, though their powers are limited to changing their own pass‐
words.

**See Also**

 - _man 1 chmod_

**6.8 Using the Special Modes for Special Use Cases** **|** **145**

**6.9 Removing the Special Modes in Octal Notation**

**Problem**

You want to remove the special modes from a file or directory.

**Solution**

Removing a special mode is a little different from setting it because you need to use
an extra leading zero, as in the following example:

```
  $ chmod -v 00770 backup.sh
  mode of 'backup.sh' changed from 1770 (rwxrwx--T) to 0770 (rwxrwx---)
```

Or replace the leading zeroes with a leading equals sign:

```
  $ chmod -v =770 backup.sh
  mode of 'backup.sh' changed from 1770 (rwxrwx--T) to 0770 (rwxrwx---)
```

**See Also**

 - _man 1 chmod_

**6.10 Setting File Permissions with chmod’s**
**Symbolic Notation**

**Problem**

You know that the _chmod_ (change mode) command supports both octal and symbolic
notation, and you want to use symbolic notation to manage file permissions.

**Solution**

Symbolic notation is more complex than octal notation and behaves differently
according to which operator you use.

There are three operators: +, -, and =. You can change permissions for everyone with
the _a_ flag, or individually with _u_ for the file owner, _g_ for the group, and _-o_ for other,
which is everyone else:

 - _+_ adds to existing permissions.

 - _-_ subtracts from existing permissions.

 - _=_ adds new permissions, and removes any permission bits not listed.

**146** **|** **Chapter 6: Managing Files and Directories**

Suppose that _file.txt_ is owner read-write, group read, and other read, or _-rw-r--r--_ :

```
  $ stat --format=%a:%A:%U:%G file.txt
  664:-rw-r--r--:stash:stash
```

You want to change it to _-rw-rw-rw-_ . Add write permissions to group and other:

```
  $ chmod -v g+w,o+w file.txt
  mode of 'file.txt' changed from 0644 (rw-r--r--) to 0666 (rw-rw-rw-)
```

You could also use _a=rw_ .

In the next example the owner of _file.txt_ changes it from world readable and writeable
to only the file owner can edit it, and group and world can only read it:

```
  $ chmod -v g-w,o-w file.txt
  mode of 'file.txt' changed from 0666 (rw-rw-rw-) to 0644 (rw-r--r--)
```

A common permission set is to give the owner and group the same permissions, such
as read-write, and to exclude other:

```
  $ chmod -v u=rw,g=rw,o-r file.txt
  mode of 'file.txt' changed from 0644 (rw-r-r--) to 0660 (rw-rw----)
```

Commands and scripts require the executable bit to be set. This example adds the
executable bit to the existing permissions for the file owner:

```
  $ chmod -v u+x file.txt
  mode of 'file.sh' changed from 0660 (rw-rw----) to 0760 (rwxrw----)
```

The **`=`** operator is useful for overwriting existing permissions:

```
  $ chmod -v u=rw,g=rw,o=r file.txt
  mode of 'file.sh' changed from 0760 (rwxrw----) to 0664 (rw-rw-r--)
```

**Discussion**

The key to using _chmod_ ’s symbolic notation reliably is to always be explicit and to be
mindful of the existing permissions. Add and subtract from existing permissions
(except with the = operator, which overwrites), and specify _u_, _g_, _o_, or _-a_ .

_symbolic_ notation is designed to be mnemonic, _r_ for read, _w_ for write, and _x_ for exe‐
cute (Table 6-5).

_Table 6-5. Symbolic notation permissions_

**<mark>Mode</mark>** **<mark>Value</mark>**
r read

w write

x execute

**6.10 Setting File Permissions with chmod’s Symbolic Notation** **|** **147**

The notation for users and groups is also mnemonic (Table 6-6).

_Table 6-6. Symbolic notation owners_

**<mark>Owner</mark>** **<mark>Notation</mark>**
user u

group g

other 
all a

Just like octal notation, symbolic notation also supports the special modes (see Recipe
6.11).

There are 10 values in symbolic notation, and unset values (which mean no permis‐
sions) are represented by a dash, like this example for Duchess’s home directory:

```
  $ stat --format=%a:%A:%U:%G /home/duchess
  755:drwxr-xr-x:duchess:duchess
```

In _drwxr-xr-x_, the _d_ indicates that this is a directory. There is no comparable value in
octal notation.

The remaining nine values are divided into three triads, and the three values in each
triad represent read, write, and execute.

**See Also**

 - _man 1 chmod_

**6.11 Setting the Special Modes with chmod’s Symbolic**
**Notation**

**Problem**

You want to set special modes with _chmod_ ’s symbolic notation.

**Solution**

The special modes include the _sticky bit_, _setuid_, and _setgid_ . These are all set in the exe‐
cutable fields. (See the end of the Discussion in Recipe 6.10 if you are not sure what
the executable fields are.)

The sticky bit is applied to directories that contain files owned by multiple users to
prevent nonowners from moving, renaming, or deleting the files:

**148** **|** **Chapter 6: Managing Files and Directories**

```
  $ chmod o+t /shared/stickydir
  mode of '/shared/stickydir' changed from 0775 (rwxrwxr-x) to 1775 (rwxrwxr-t)
```

Apply _setgid_ to a directory to set all newly created files in the directory to the same
group as the directory. This is a nice trick for enforcing correct ownership in a shared
directory:

```
  $ chmod -v g+s /shared
  mode of '/shared' changed from 0770 (rwxrwx---) to 2770 (rwxrws---)
```

Apply _setuid_ to an executable file to allow nonroot users to run the executable:

```
  $ chmod -v u+s backup-script
  mode of 'backup-script' changed from 0755 (rwxr-xr-x) to 4755 (rwsr-xr-x)
```

_setuid_ and _setgid_ have the potential to open security holes; see the Discussion to learn
more.

**Discussion**

_setuid_ is useful for executable files.

_setgid_ is useful for directories and files.

The sticky bit is only for directories.

Table 6-7 shows the relationship between owners and modes.

_Table 6-7. All symbolic modes_

**<mark>Mode</mark>** **<mark>User</mark>** **<mark>Group</mark>** **<mark>Other</mark>**
Read r r r

Write w w w

Execute x x x

setuid s

setgid s

Sticky bit t

A more descriptive name for the sticky bit is _restricted deletion bit_ . This prevents users
from removing or renaming a file in a directory unless they own the file. You can see
this on your _/tmp_ directory, which is world readable and writeable, and contains files
for multiple users. Using the sticky bit prevents users from moving, renaming, or
deleting files they do not own:

```
  $ stat --format=%a:%A:%U:%G /tmp
  1777:drwxrwxrwt/:root:root
```

_setgid_ means set group identification, and _setuid_ is set user identification. These are
used to elevate the permissions of an unprivileged user to the same as the file owner.
This is how unprivileged users can use the _passwd_ command to change their own

**6.11 Setting the Special Modes with chmod’s Symbolic Notation** **|** **149**

passwords, even though only root has write permissions on _/etc/passwd_, and every‐
one else has only read and execute permissions:

```
  $ stat --format=%a:%A:%U:%G /usr/bin/passwd
  4755:-rwsr-xr-x:root:root
```

_rws_ in the user fields means read, write, and execute for all users, with the same per‐
missions as the file owner.

_setgid_ and _setuid_ have the potential to create security holes. It is a best practice to use
them only when you can’t devise a safer way to accomplish what you want to do, such
as using group assignments or _sudo_ .

**See Also**

 - _man 1 chmod_

**6.12 Setting Permissions in Batches with chmod**

**Problem**

You want to set permissions on more than one file at a time.

**Solution**

_chmod_ supports operating on lists of files. You can also use the _find_ command and
shell wildcards to select the files you want to change.

**You May Need sudo**

If you see “Permission denied” messages, use _sudo_ .

The following example takes a space-delimited list of files and makes them all readonly for everyone:

```
  $ chmod -v 444 file1 file2 file3
```

Set permissions for a directory and its contents, including subdirectories, with the _-R_
(recursive) flag:

```
  $ chmod -vR 755 /shared
```

You may use wildcards to select files; for example, to make all _.txt_ files in the current
directory readable and writable to the owner, and to make group and other readable:

```
  $ chmod -v 644 *.txt

```

**150** **|** **Chapter 6: Managing Files and Directories**

Use a wildcard to select all filenames that start with the same string:

```
  $ chmod -v 644 abcd*
```

This example makes all files in the current directory read-write for the owner and
group, without changing permissions on the directory:

```
  $ find . -type f -exec chmod -v 660 {} \;
```

You can change the mode of all files belonging to a particular user. You may name the
user with either their numeric ID or username. This example starts at the root of the
filesystem:

```
  $ sudo find / -user madmax -exec chmod -v 660 {} \;
  $ sudo find / -user 1007 -exec chmod -v 660 {} \;
```

**Discussion**

You need root privileges to search for files in all directories.

The dot ( _find ._ ) tells _find_ to start its search in the current directory. You can start your
search in any directory.

_-type_ limits the results to files, and not directories.

_-user_ looks for files owned by the specified user.

_-exec chmod -v 660 {} \;_ is a fabulous little incantation that takes the results of the _find_
search and runs the _chmod -v 660_ command on the results. You can use this for pretty
much any command that you want to apply to the results of a _find_ search.

**See Also**

 - _man 1 chmod_

 - _man 1 find_

**6.13 Setting File and Directory Ownership with chown**

**Problem**

You need to change ownership on a file or directory.

**Solution**

Use the _chown_ (change owner) command to change file ownership. The basic com‐
mand syntax is _chown user:group filename_ . You may change only the owner, _chown_
_user: filename_, or only the group, _chown :group filename_ .

**6.13 Setting File and Directory Ownership with chown** **|** **151**

Changing the owner requires root privileges:

```
  duchess@client1:~$ sudo chown -v madmax: song.wav
  changed ownership of 'song.wav' from duchess:duchess to madmax:duchess
```

Change the group owner:

```
  $ sudo chown -v :composers song.wav
  changed ownership of 'song.wav' from madmax:duchess to :composers
```

Change both the user and group owner:

```
  $ sudo chown stash:stash song.wav
```

**Discussion**

You need root privileges to make changes to files you do not own and to transfer file
ownership to another user. You can change group file ownership without root privi‐
leges when you belong to both the original group and the new group.

The colon is optional when you change only the owner and required when you
change the group.

**See Also**

 - _man 1 chown_

**6.14 Changing Ownership on Batches of Files with chown**

**Problem**

You want to change ownership of directories and their contents, or just the contents
of directories, a list of files, or change ownership of files from one user to another.

**Solution**

_chown_ supports operating on lists of files. You can also use the _find_ command and
shell wildcards to list the files you want to change.

To change the owner of several files at once with _chown_, use a space-delimited list:

```
  $ sudo chown -v madmax:share file1 file2 file3
```

Change files with a certain file extension in the current directory to a new group:

```
  $ sudo chown -v :share *.txt
```

Give all of a user’s files in a directory to another user, using their numeric UIDs or
usernames:

**152** **|** **Chapter 6: Managing Files and Directories**

```
  $ chown -Rv --from duchess stash /shared/compositions

  $ chown -Rv --from 1001 1005 /shared/compositions
```

Use the -find_ command to traverse the entire filesystem, or any directory and its
subdirectories, to give all of a user’s files to another user:

```
  $ sudo find / -user duchess -exec chown -v stash {} \;

  $ sudo find / -user 1001 -exec chown -v 1005 {} \;
```

**Discussion**

Transferring ownership of all of a user’s files to another user, or to a different group, is
useful for cleaning up after users who no longer have accounts on the system.

**See Also**

 - _man 1 chown_

**6.15 Setting Default Permissions with umask**

**Problem**

You want to understand why files are created with a certain set of default permissions,
and how to configure the defaults yourself.

**Solution**

The umask (user file-creation mode mask) controls this behavior. To see what yours
is, run the _umask_ command:

```
  $ umask
  0002
```

This is how it looks it in symbolic notation:

```
  $ umask -S
  u=rwx,g=rwx,o=rx
```

This sets your default permissions to 0775 for directories and 0664 for files, because
the umask “masks” the hardcoded default permissions of 0777 and 0666. Or you can
think of it as subtraction, 0777 - 0002 = 0775.

To change your umask temporarily for the duration of your current session, set it this
way:

```
  $ umask 0022

```

**6.15 Setting Default Permissions with umask** **|** **153**

Set the umask permanently by inserting the line _umask 0022_, or whatever value you
want, in your _~/.bashrc_ file.

Set the default umask for all of your users in _/etc/login.defs_ :

```
  UMASK 022
```

Table 6-8 shows some common umask values.

**Discussion**

_umask_ is a Bash shell built-in, and not an executable program stored in _/bin_, _/usr/bin_,
or any of the other _bin_ (binary) directories.

Table 6-8 lists some commonly used umask values.

_Table 6-8. Common umask values_

**<mark>umask</mark>** **<mark>Directories</mark>** **<mark>Files</mark>**
0002 0775 0664

0022 0755 0644

0007 0770 0660

0077 0700 0600

**See Also**

 - _man 1 chmod_

 - See the Shell Builtin Commands section of _man 1 bash_ to learn more about
_umask_ and other Bash built-in commands

**6.16 Creating Shortcuts (Soft and Hard Links) to Files**
**and Directories**

**Problem**

You want to create shortcuts or links to files.

**Solution**

There are two types of links in Linux: soft links and hard links. Soft links are for files
and directories. Hard links are only for files.

Use the _ln_ (link) command to create soft and hard links. The following example cre‐
ates a soft link to an external directory, _/files/userstuff_, in Mad Max’s home directory:

**154** **|** **Chapter 6: Managing Files and Directories**

```
  $ ln -s /files/userstuff stuff
```

_/files/userstuff_ is the target, and _stuff_ is the destination, or soft link name. You can
name your soft links anything you want, and move and delete them without affecting
their targets. When you open a soft link, it behaves the same way as opening the tar‐
get.

Hard links are copies of files. The default for the _ln_ command is to create hard links:

```
  $ ln /files/config1.txt myconf.txt
```

**Discussion**

Soft links are for files and directories, while hard links are only for files.

**Soft links**

Soft links are more commonly called _symlinks_, short for symbolic links.

Symlinks point to files and directories. When the target of a symlink is deleted,
renamed, or moved, the symlink is broken. If you create a new file with the same
name as the deleted file, the symlink is restored, even if the content is different.

Symlinks can cross filesystems. You can even create symlinks to files or directories
that are not permanently available, like USB storage devices or network file shares.

Symlinks are not updated when the target changes (renamed, moved, or deleted). You
need to create a new symlink and delete the old one.

You don’t manage permissions or ownership on symlinks because only the permis‐
sions on the target matter.

Symlinks look like this:

```
  $ stat stuff
  File: stuff -> /files/userstuff
  Size: 4        Blocks: 0     IO Block: 4096  symbolic link
  Device: 804h/2052d   Inode: 877581   Links: 1
  Access: (0777/lrwxrwxrwx) Uid: ( 1000/ madmax) Gid: ( 1000/ madmax)
```

_File: stuff → /files/userstuff_ shows the target that the symlink points to.

The third line identifies this as a symbolic link.

The _l_ in _Access: lrwxrwxrwx_ identifies this as a symlink.

This is what a symlink looks like in a file listing:

```
  $ ls -l
  [...]
  lrwxrwxrwx 1 madmax madmax 4 Apr 26 12:42 stuff -> /files/userstuff

```

**6.16 Creating Shortcuts (Soft and Hard Links) to Files and Directories** **|** **155**

**Hard links**

Files are uniquely identified by _inodes_, and inodes are what hard links point to, rather
than filenames. The _ls_ command shows inodes with the _-i_ option. The inode in this
example is 1353, and it is the same for the three hard links:

```
  $ ls -li
  1353 -rw-rw-r--  3 madmax madmax 11208 Apr 26 13:06 config.txt
  1353 -rw-rw-r--  3 madmax madmax 11208 Apr 26 13:06 config2.txt
  1353 -rw-rw-r--  3 madmax madmax 11208 Apr 26 13:06 config3.txt
```

This is because all three inodes point to the same block of data.

Hard links always work because they point directly to inodes. Files with multiple hard
links can be moved, renamed, and edited, and all hard links remain in sync because
they all point to the same data block.

Every file on a Linux system starts with a hard link. When you create a hard link, you
are creating a new filename for an existing data block.

Hard links cannot cross filesystems, but exist only inside a single filesystem. For
example, if you have _/_ and _/home_ on separate partitions, you cannot make hard links
in _/home_ for files in _/_ .

You can make as many hard links to a file as you like, and the disk space occupied by
the data they point to is always the same, regardless of how many hard links it has.

Contrast hard links with making file copies: every copy uses more disk space, each
copy is independent, and copies can go anywhere.

A file is not completely deleted until all hard links are deleted. You can see this with
_ls_ . The following example shows another view of our example inode with three hard
links:

```
  $ stat config3.txt
  File: config3.txt
  Size: 11208      Blocks: 24     IO Block: 4096  regular file
  Device: 804h/2052d   Inode: 1353    Links: 3
```

Compare the File, Size, and Links to a symlink. A hard link is a regular file, and note
Links: 3. This shows there are three hard links to the same data. When you delete a
file with more than one hard link, it is not deleted until you delete all of them. Locate
all related hard links with the _find_ command:

```
  $ find /etc -xdev -samefile config3.txt
  ./config
  ./config2
  ./config3
```

Symlinks are used a lot in Linux, hard links not so much. Some backup applications
use inodes for deduplication. In olden times, when filesystems were much smaller,

**156** **|** **Chapter 6: Managing Files and Directories**

running out of inodes was not uncommon. In this case hard links were preferable,
because symlinks each have their own inodes, but hard links share inodes.

You can see how many inodes a filesystem has with the _du_ command, and how many
are used:

```
  $ df -i /dev/sda4
  Filesystem    Inodes IUsed   IFree IUse% Mounted on
  /dev/sda4   384061120 389965 383671155  1% /home
```

With 1% in use, I’m not running out of inodes anytime soon.

**See Also**

 - man 1 ls

**6.17 Hiding Files and Directories**

**Problem**

You want to hide some files and directories so that nobody can see them.

**Solution**

To hide files so nobody can see them, put them on a storage device only you have
access to.

To reduce clutter in your file manager, use _dot files_ to ignore files. You already have
these. Look for a setting like “Show hidden files” in your graphical file manager, or
use the _-a_ option for _ls_ :

```
  $ ls -a
  .
  ..
  Audiobooks
  .bash_history
  .bash_logout
  .bashrc
  bin
  .bogofilter
  .cache
  Calibre-Library
  cat-memes
  .cddb
  .cert
```

Prefixing any file with a dot makes it a hidden file, though it is really not hidden, but
ignored until you want to see it. This is used mainly in users’ home directories to

**6.17 Hiding Files and Directories** **|** **157**

reduce clutter by not displaying configuration files. These are normal files you can
edit, delete, or whatever you want.

**Discussion**

Note the single and double dots at the top of the file list. The single dot represents the
current directory, and the double dot represents the parent directory. Try it with the
_cd_ command. The first example stays in the current directory, the second example
changes to the parent directory:

```
  stash@client4:~$ cd .
  stash@client4:~$

  stash@client4:~$ cd ..
  stash@client4:/home$
```

Run _cd_ with no options to return to your home directory, or _cd -_ to return to the last
directory you were in.

**See Also**

 - See the Shell Builtin Commands section of _man 1 bash_ to learn more about _cd_
and other Bash built-in commands

**158** **|** **Chapter 6: Managing Files and Directories**

**<u>CHAPTER 7</u>**
#### **Backup and Recovery with rsync and cp**

You know you need to make good backups of your computer files and to test them
periodically to see if you can restore your files. But how do you do this on Linux?
Fear not, for backups and restores on Linux are quite understandable, and your
backup files are easy to search and restore.

It is helpful to have a couple of USB sticks for practicing the commands in this chap‐
ter and a few directories full of files that you won’t mind losing, should anything go
wrong.

We will use _rsync_ and _cp_ . Both are essential Linux tools, and you can count on them
being well maintained and available.

_cp_ is the copy command included in the GNU _coreutils_ package, which is installed by
default on nearly every Linux distribution. _cp_ is for simple copying. It may be all you
need to maintain regular backups.

_rsync_ is an efficient file-transfer program, and its main purpose is keeping filesystems
in sync with each other. When you use it for making backups, it keeps your local files
in sync with your backup device. It is fast and efficient because it transfers only the
changes in files. Unlike a lot of backup software, which never want you to delete any‐
thing, it even mirrors deletions. Because of these features, rsync is the tool of choice
for updating and mirroring user home directories, websites, git repositories, and
other large complex file trees.

There are two ways to use rsync over a network: over SSH, for authenticated login
and transport, or by running it as a daemon. Using SSH requires users to have login
accounts on every machine for which they need rsync access. When rsync is run in
daemon mode, you can use its built-in authentication methods to control access
so that users do not need login accounts on the rsync server. Daemon mode is

**159**

well-suited for a LAN backup server. It is not safe to access over untrusted networks,
unless you use a VPN (see Chapter 13).

What sort of device do you store your backups on? This depends on your needs. I am
a fan of USB storage media for a single user. Suppose you have a desktop Linux PC, a
laptop, a tablet, and a smartphone. Back up your phone and tablet to your PC, then
back up the PC to a USB hard drive. Super-important files could go to an online
backup service.

For multiple users, a good solution is a central backup server. This can be any Linux
PC.

Consider longevity. You cannot count on longevity with digital storage media,
because even if the medium (hard disk, USB storage drive, CD/DVD) survives, there
is no guarantee that the tools to read it will endure. Hardware and file formats
change. Can you still read floppy disks? Remember Zip disks? How about those
archives of old Microsoft Word and Powerpoint documents? With open source file
formats you can always find a way to recover them. Good luck with proprietary for‐
mats when the vendor decides to stop supporting them.

Paper is still the long-term storage champion, and worth considering for your most
important documents and photos.

For long-term digital storage, plan to transfer your archives to new media periodi‐
cally, possibly with new commands and to new filesystem formats.

What about backing up your backup server? No problem. Setting up a remote rsync
mirror for backing up the backups is a common strategy, if your internet connection
is robust enough to handle the traffic. But before you build a massive backup infra‐
structure, think about how many levels of redundancy you really need. Offsite back‐
ups are insurance against a disaster at your site. This can be a remote backup server at
a site you control, or a friend’s site, or rented space in a datacenter. Maybe regular
drops of an external hard drive to a bank safe-deposit box would be enough for your
needs. Also think about recovery: can you get to your backups quickly?

Always remember that the purpose of backups is _recovery_ . Test your backups regu‐
larly to avoid learning the hard way that your backup method failed.

In this chapter you will learn about simple copying to USB storage devices with _cp_ .
For some users this is all they will ever need.

Most of the chapter is about using the _rsync_ command for faster and more efficient
copying. You can use _rsync_ to back up your files to local media or remote servers. You
will learn which files you should back up, how to fine-tune your file selection, main‐
tain the same file permissions and timestamps on your files, how to build an rsync
backup server for multiple users, and how to make secure remote backups.

**160** **|** **Chapter 7: Backup and Recovery with rsync and cp**

**7.1 Selecting Which Files to Back Up**

**Problem**

You’re not sure which files you should back up. Do you need to make backups of your
system files? Do you really need to back up all of your personal files? Are there files
you should not back up?

**Solution**

Any file that you would be sorry to lose is a file you need to back up. Your personal
files and system data files are the most important. Restoring system files such as com‐
mands, applications, and libraries is less important because you can always download
and reinstall these.

The following directories contain files such as configurations; data files for servers
such as web, FTP, and mail servers; log files; applications installed in nonstandard
locations; and shared directories, all of which should be backed up:

 - _/boot/grub_, if it contains any customizations such as themes, background images,
or fonts.

 - _/etc_ contains system configuration files.

 - _/home_, users’ personal files.

 - _/mnt_, temporary filesystem mountpoints. Back this up if you have mountpoints
you want to preserve.

 - _/opt_, for proprietary or other applications not installed the standard way.

 - _/root_, the root user’s personal files.

 - _/srv_, data for servers such as web, FTP, and rsync servers.

 - _/tmp_ holds temporary data that is automatically updated or deleted as needed.
Some of the data in _/tmp_ is persistent, for example user-created files and some
system services, and they should be backed up.

 - _/var_ stores many types of data such as log files, mail spools, cron jobs, and data
for system services, though most distros have migrated to using _/srv_ for system
services.

If you have any shared directories, custom commands and scripts, or any data files or
directories not listed previously, back them up.

_/proc_, _/sys_, and _/dev_ are pseudofilesystems that exist only in memory and should not
be backed up.

**7.1 Selecting Which Files to Back Up** **|** **161**

_/media_ is for mounting removable storage media and should be managed by the sys‐
tem, so there is no need to back it up. If you are manually creating mountpoints
in _/media_, they really need to be moved to _/mnt_ .

Many databases should not be backed up with simple copying because they have spe‐
cial utilities and procedures for making copies and backups, and for restoring from
backups. Use the tools made for your databases. Some examples are PostrgreSQL,
MariaDB, and MySQL.

**Restoring From Backup**

Some files should not be restored from backup; see Recipe 7.2.

Copying everything is the easy way if your backup storage is large enough. You also
have the option of fine-tuning your file selection by creating lists of files to copy or to
exclude; see Recipes 7.8 and 7.9.

**Discussion**

Storage media is so cheap now you may not have to care about conserving storage
space. If you need to be mindful of storage limitations, see the recipes in this chapter
on file selection.

**See Also**

 - [Filesystem Hierarchy Standard](https://oreil.ly/y1pJs)

**7.2 Selecting Files to Restore from Backups**

**Problem**

You are restoring files from backup, and you want to know if there are files that
should not be restored.

**Solution**

Some files should not be restored, depending on the circumstances.

Do not restore _/etc/fstab_ after reinstalling Linux (the file that configures your static
filesystem mounts). Every time you install Linux, all the filesystems get new Universal
Unique Identifiers (UUIDs), so they will not be recognized and your new installation
will fail.

**162** **|** **Chapter 7: Backup and Recovery with rsync and cp**

Be careful restoring any file in _/etc_ or the dotfiles (such as _/home/.config_
or _/home/.local_ ) in your home directory. If you are restoring from backup to a new
installation of a different release, or a different Linux distribution, there may be
incompatibilities in configuration options or file locations. Restore them one at a time
so you can quickly spot any problems.

**See Also**

 - Chapter 1

**7.3 Using the Simplest Local Backup Method**

**Problem**

You want to know the easiest, simplest way to make regular backups to a local USB
storage device.

**Solution**

The answer is to use simple copying. Get yourself a nice USB hard drive or USB stick.
Plug it in and use your file manager to copy your files. Easy peasey, no muss, no fuss,
and it is dead simple to restore your files. Or, use the _cp_ command (see Recipe 7.4).

**Discussion**

Simple copying doesn’t scale all that well, but for a few devices, like a PC, laptop, and
phone, it works fine. The important part is making regular backups, verifying that
you can restore files from your backups, and not worrying if you’re being nerdy
enough.

Back in olden times, backups were more complicated because storage was expensive,
so backup programs used a lot of tricks to save space. Now you can buy multiterabyte external USB 3.0 hard drives for less than $200.

**See Also**

 - _man 1 cp_

**7.3 Using the Simplest Local Backup Method** **|** **163**

**7.4 Automating Simple Local Backups**

**Problem**

You like using simple copying for making your backups to an external USB storage
drive, and you want to automate the process.

**Solution**

This calls for the _cp_ command and _crontab_ to schedule your backups.

You may list individual files and directories to copy with _cp_, separated by spaces:

```
  duchess@pc:~$ cp -auv Pictures/cat-desk.jpg Pictures/cat-chair.png \
  ~/cat-pics /media/duchess/2tbdisk/backups/
```

The following example copies Duchess’s entire home directory to the _backups_ direc‐
tory on an external USB drive named _2tbdisk_ :

```
  duchess@pc:~$ cp -auv ~ /media/duchess/2tbdisk/backups/
```

This creates _/media/duchess/2tbdisk/backups/duchess/_ on the backup device.

Copy the contents of a directory without copying the directory itself:

```
  duchess@pc:~$ cp -auv /home/duchess/* /media/duchess/2tbdisk/backups/
```

Create a personal cron job to run your backup every night at 10:30 P.M.:

```
  duchess@pc:~$ crontab -e
  # m h dom mon dow  command
  30 22 *  *  *  /bin/cp -au /home/duchess /media/duchess/2tbdisk/backups/
```

**Discussion**

If you want to preserve file attributes such as ownership and permissions, format
your backup drive with a Linux filesystem that supports file attributes, such as Ext4,
XFS, or Btrfs (see Chapter 11). The FAT filesystems do not preserve ownership or
permissions.

Keep an eye on how long it takes your backup to run. If it takes longer than your
scheduled backup interval, cron will start the next backup on schedule, and then you
have a mess.

The first run takes the longest because all the files are new. Subsequent backups will
go faster as only new files and files with newer timestamps will be copied.

The tilde, ~, is a shortcut for the current user’s home directory, so in this recipe it is
short for _/home/duchess_ .

**164** **|** **Chapter 7: Backup and Recovery with rsync and cp**

The asterisk in _/home/duchess/*_ means copy all the files in _/home/duchess_, but not the
directory _/home/duchess_ .

The _-a_, _-u_, and _-v_ options for _cp_ mean:

 - _-a, --archive_ recursively copies and preserves all file attributes: mode, ownership,
timestamps, and extended attributes.

 - _-u, --update_ tells _cp_ to copy only files with newer timestamps than the copies in
the backup directory, or new files that have not been backed up yet.

 - _-v, --verbose_ prints activity messages during the copy operation.

Some other useful options:

 - _-R, -r_ recursive; use this to copy directories when you do not use the _-a_ option. _-a_
preserves file attributes, _-R, -r_ does not. FAT and exFAT filesystems do not sup‐
port file attributes, so use _-R, -r_ with these.

 - _--parents_ creates missing parent directories on the destination.

 - _-x, --one-file-system_ This prevents recursing into other partitions and mounted
network filesystems. For example, if you have an NFS share mounted you may
not want to add it to your backup.

Most Linux distributions mount USB devices in _/run/media_ or _/media_ . The easy way
to find the filepath for your USB drive is to look in your file manager or use the _lsblk_
command:

```
  $ lsblk
  NAME  MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
  [...]
  sdb   8:16  0 1.8T 0 disk
  └─sdb1  8:17  0 1.5T 0 part /media/duchess/backups
```

**See Also**

 - Recipe 3.7 to learn more about using _cron_

 - _man 1 crontab_

 - _man 1 cp_

**7.4 Automating Simple Local Backups** **|** **165**

**7.5 Using rsync for Local Backups**

**Problem**

You want to make backups to a USB stick or USB hard drive, and you want some‐
thing that is faster and more efficient than simple copying. You also want simple file
restorations that you can make with standard Linux tools, without needing special
software.

**Solution**

_rsync_ is what you want. It keeps filesystems synchronized, both local and remote.
_rsync_ is fast and efficient, as it transfers only the changes in files, and you can restore
files with the _rsync_ command, the _cp_ command, your file manager, or whatever copy‐
ing tool you prefer.

The following example shows how to back up a home directory. First, name your
source directory, which is the directory you want to back up, then name the destina‐
tion directory. This example copies Duchess’s _/home_ to a USB drive named _2tbdisk_ :

```
  duchess@pc:~$ rsync -av ~ /media/duchess/2tbdisk/
  sending incremental file list
  duchess/
  duchess/Documents/
  duchess/Downloads/
  duchess/Music/
  [...]

  sent 27,708,209 bytes received 20,948 bytes 11,091,662.80 bytes/sec
  total size is 785,103,770,793 speedup is 28,313.29
```

You can specify two or more directories, in a space-delimited list, to transfer to the
destination directory:

```
  duchess@pc:~$ rsync -av ~/arias ~/overtures /media/duchess/2tbdisk/duchess/
```

Copy files from your backup device to your computer by reversing the source and
destination:

```
  duchess@pc:~$ rsync -av /media/duchess/2tbdisk/duchess/arias /home/duchess/
```

You may safely test your _rsync_ command, without copying any files, with the _--dry-_
_run_ option:

```
  duchess@pc:~$ rsync -av --dry-run \
  ~/Music/scores ~/Music/woodwinds /media/duchess/2tbdisk/duchess/
```

If any files are deleted from a source directory, _rsync_ will not delete them from the
destination directory unless you explicitly tell it to with the _delete_ option:

```
  duchess@pc:~$ rsync -av --delete /home/duchess /media/duchess/2tbdisk/

```

**166** **|** **Chapter 7: Backup and Recovery with rsync and cp**

**Discussion**

The tilde, _~_, is a shortcut for your home directory, so in the examples it means _/home/_
_duchess_ .

Command examples with line breaks use a slash, \, to indicate that the command
continues on the next line. You can copy the whole command, with the slashes, and it
should work.

If you have networked filesystems mounted on your PC, such as NFS or Samba, use
the _-x_ option to copy only from your local filesystem, and not recurse into the remote
filesystems.

Adding a trailing slash, _~/_, ( _/home/duchess/_ ) copies only the contents of the _duchess/_
directory, but not the directory itself, resulting in _/media/duchess/2tbdisk/[files]_ .
Omitting the trailing slash transfers the contents of _/home/duchess_ and the _duchess_
directory, resulting in _/media/duchess/2tbdisk/duchess/[files]_ . The trailing slash only
matters on the source directory, and it makes no difference on the destination
directory.

Don’t feel bad if you have to count on your fingers or make a lot of test runs to
remind yourself how the trailing slash behaves, because this vexes everyone. It might
help to think of the trailing slash as a little fence that prevents the source directory
from escaping.

The _-a_ and _-v_ options for _rsync_ mean:

 - _-a, --archive_ retains the mode, timestamps, permissions, and ownership, and
copies recursively. This is the same as _*-rlptgoD*_, which copies recursively, copies
symlinks, preserves permissions, preserves file modification times, preserves file
ownership, and preserves special files, such as device files.

 - _-v, --verbose_ displays activity messages.

You may wish to use some of these options:

 - _-q, --quiet_ suppresses nonerror messages.

 - _--progress_ shows information on each file as it is transferred.

 - _-A, --als_ preserves access control lists (ACLs).

 - _-X, --xattrs_ preserves extended file attributes (xattrs).

Your filenames, of course, will be different than the examples. _2tbdisk_ is a filesystem
label created by the user (see Recipe 9.4). It is an abbreviation for “2 terabyte disk.” If
you do not create a label, _udev_ creates one, for example _/media/duchess/488B-7971/_ .

**7.5 Using rsync for Local Backups** **|** **167**

You may use the normal Linux tools, such as _rsync_, your file manager, or the _cp_ com‐
mand, to restore files.

**See Also**

 - _man 1 rsync_

**7.6 Making Secure Remote File Transfers with rsync over**
**SSH**

**Problem**

You want to use _rsync_ to copy files to another computer on your local network or
over the internet, and you want encrypted transport and authentication.

**Solution**

_rsync_ uses SSH by default when you transfer files to another machine. The remote
machine must be running an SSH server, and the source machine must have an SSH
client already set up (see Chapter 12).

This example transfers files over the local network from Duchess’s PC to her laptop.
Duchess’s username on her laptop is Empress, and she is copying files from her home
directory on her PC to her home directory on her laptop:

```
  duchess@pc:~$ rsync -av ~/Music/arias empress@laptop:songs/
  duchess@laptop's password:
  building file list ... done
  arias/
  arias/o-mio-babbino-caro.ogg
  arias/deh-vieni-non-tardar.ogg
  arias/mi-chiamano-mimi.ogg
  wrote 25984 bytes read 68 bytes 7443.43 bytes/sec
  total size is 25666 speedup is 0.99
```

If the destination directory does not exist, _rsync_ will create it.

To upload files over the internet, use the fully qualified domain name of the server
you are logging in to:

```
  duchess@pc:~$ rsync -av ~/Music/woodwinds \
  empress@remote.example.com:/backups/

```

**168** **|** **Chapter 7: Backup and Recovery with rsync and cp**

The syntax for copying files from a remote host is reversed. This example copies
the _/woodwinds_ directory and its contents from the remote host to Duchess’s home
directory:

```
  duchess@pc:~$ rsync -av empress@remote.example.com:/backups/woodwinds \
  /home/duchess/Music/
```

**Discussion**

You might remember when the SSH option had to be explicit—for example, _rsync -a -_
_e ssh [options]_ . This is no longer necessary.

You may find some of these options to be useful:

 - _--partial_ preserves partially downloaded files when the network connection is
interrupted, and resumes the file transfer from where it left off when the connec‐
tion is restored.

 - _-h, --human-readable_ displays file sizes in kilobytes, megabytes, and gigabytes,
rather than bytes.

 - _--log-file=_ stores a complete record of each transfer in a text file. Put them all
together like this:

```
  duchess@pc:~$ rsync --partial --progress \
  --log-file=/home/duchess/rsynclog.txt \
  -hav ~/Music/arias empress@remote.example.com:/backups/
```

Both authentication and transport are encrypted by SSH. Users need shell accounts
on all machines they are going to transfer files to. See Chapter 12 to learn about
secure remote administration with SSH.

Consider setting up a central backup server for simplifying administration. Your
users have their own accounts with their own _/home_ directories and can manage their
own backups and restores without bothering you.

Another option for a backup server is to run _rsync_ as a service. The advantage of this
is your _rsync_ users do not need login accounts on the server. One disadvantage is it
does not support encrypted transfers. See Recipe 7.13 to learn about this.

**See Also**

 - _man 1 rsync_

 - Recipe 12.5

 - Recipe 12.7

**7.6 Making Secure Remote File Transfers with rsync over SSH** **|** **169**

**7.7 Automating rsync Transfers with cron and SSH**

**Problem**

You want to create crontabs to automatically run your secure _rsync_ transfers.

**Solution**

You need SSH set up for passwordless authentication on the destination machine (see
Recipes 12.10 and 12.11) and network access to the destination machine for the
clients.

Then use _/etc/crontab_ for transfers that require root permissions. The following
example makes a backup of _/etc_ every night at 10 P.M. to a LAN server named _server1_ :

```
  # m h dom mon dow user command
  00 22 * * * root /usr/bin/rsync -a /etc server1:/system-backups
```

Use personal crontabs for transferring your own files (see Recipe 3.7).

**Discussion**

OpenSSH is a lovely tool that provides secure network transfers for a host of tasks.
Anything that you run over a network can probably run over SSH.

**See Also**

 - Chapter 12

 - Recipe 12.10

 - Recipe 12.11

**7.8 Excluding Files from Backup**

**Problem**

So far the examples have shown how to transfer entire directories. You want to know
how to exclude files and directories from being copied.

**Solution**

For simplicity, the following examples demonstrate local transfers to a USB drive, but
they also work for remote transfers over SSH; see Recipe 7.6.

**170** **|** **Chapter 7: Backup and Recovery with rsync and cp**

When it’s just a few files, you can list them on the command line using _--exclude=_ .
This example excludes one file from _/home/duchess/Music/arias_ :

```
  duchess@pc:~$ rsync -av --exclude=lho-perduta.wav \
  ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

This is nice and easy and reliable. However, there is a gotcha: if there are multiple files
in your source directory with the same name as your excluded file, all of them will be
excluded. If you do not want the duplicates to be excluded, you need to specify which
one is to be excluded. In the following example you want to exclude only the copy in
the _arias/_ source directory:

```
  duchess@pc:~$ rsync -av --exclude=arias/lho-perduta.wav \
  ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

Exclude more than one file by enclosing them in curly braces, separated with single
quotes and commas. There must be no spaces between the equals sign and the curly
brace, and no spaces between the commas and single quotes:

```
  duchess@pc:~$ rsync -av \
  --exclude={'arias/lho-perduta.wav','non-mi-dir.wav','un-bel-di-vedremo.flac'} \
  ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

Excluding directories works the same way as excluding files, and you can mix files
and directories in your exclude list:

```
  duchess@pc:~$ rsync -av \
  --exclude={'soprano/','tenor/','non-mi-dir.wav'} \
  ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

See Recipe 7.11 to learn how to put your excludes list in a file.

**Discussion**

The root directory in an _rsync_ transfer is the top-level directory you are transferring
files from. In the examples in this recipe, that is _~/Music/arias_ . _rsync_ checks all the
files and directories in your root directory, and compares them to your exclude direc‐
tives, which _rsync_ calls _patterns_ . Patterns are checked against the files and directories
in your root directory, starting at the root and proceeding down through the direc‐
tory hierarchy. Every time a pattern is matched, it is excluded from the transfer. If the
pattern _arias/lho-perduta.wav_ is duplicated in another location, such as _2arias/lho-_
_perduta.wav_, it will also be excluded. When a pattern ends with a slash ( _/_ ), _rsync_ will
match only directories.

**See Also**

 - _man 1 rsync_

 - Recipe 7.10

**7.8 Excluding Files from Backup** **|** **171**

**7.9 Including Selected Files to Backup**

**Problem**

You want to include a selected set of files in your backup, rather than defining a list of
files to exclude.

**Solution**

When you want to back up just a few files, you can do this on the command line.
_--include=_ operates differently than _--exclude=_ because it doesn’t really mean
“include,” it means “do not exclude.” It needs two additional options, _--include=*/_ and
_--exclude='*'_, as this example of transferring a single file shows:

```
  duchess@pc:~$ rsync -av --include=*/ --include=lho-perduta.wav \
  --exclude='*' ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

You may transfer a list of files:

```
  duchess@pc:~$ rsync -av --include=*/ \
  --include={'lho-perduta.wav','non-mi-dir.wav','un-bel-di-vedremo.flac'} \
  --exclude='*' ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
```

There must be no spaces between the equals sign and the curly brace, and no spaces
between the commas and single quotes.

If there are multiple files with the same name in different locations in your source
directory, _rsync_ will transfer all of them. In this example only _/home/duchess/Music/_
_arias/sopranos/lho-perduta.wav_ is transferred because the pattern _soprano/lho-_
_perduta.wav_ is unique in _/Music/arias_ :

```
  duchess@pc:~$ rsync -av --include=*/ --include=soprano/lho-perduta.wav
  --exclude='*' ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
  Music/
  Music/arias/
  Music/arias/baritone/
  Music/arias/soprano/
  Music/arias/soprano/lho-perduta.wav
  Music/arias/tenor/
  [...]
```

That transfers only a single file, but all the subdirectories in _~/Music/arias_ are copied.
Use the _-m, --prune-empty-dirs_ option to prevent copying empty directories, like this
example:

```
  duchess@pc:~$ rsync -avm --include=*/ --include=soprano/lho-perduta.wav
  --exclude='*' ~/Music/arias /media/duchess/2tbdisk/duchess/Music/
  Music/
  Music/arias/soprano/
  Music/arias/soprano/lho-perduta.wav

```

**172** **|** **Chapter 7: Backup and Recovery with rsync and cp**

When you have more than a few files to include, store your list in a plain-text file (see
Recipes 7.10 and 7.11).

**Discussion**

_--include=*/_ tells _rsync_ to traverse your entire source directory.

_--include=[files]_ means do not exclude these files.

_--exclude='*'_ tells _rsync_ to exclude everything not included.

Remember that all filepaths are relative to your source directory and not your sys‐
tem’s root directory.

**See Also**

 - _man 1 rsync_

 - Recipe 7.10

 - Recipe 7.11

**7.10 Managing Includes with a Simple Include File**

**Problem**

Your includes are too many for a command-line incantation, and you want to main‐
tain your list in a file that _rsync_ can read. You also want this to be simple, if possible,
thanks to past experience with _rsync_ include/exclude files that never would work
right.

**Solution**

The simplest way to maintain a list, without going crazy over figuring out _rsync_ ’s
include/exclude syntax, is to create a plain list of files that you provide to the
_--files-from=_ option. You don’t have to worry about getting them in the right order, or
using _rsync_ ’s filter notation, just a plain list with whatever files and directories you
want. The only gotcha is every item in your list must be relative to your source direc‐
tory. In the following example, all list items are relative to _/home/duchess_ :

```
  # include file list
  #
  /Documents/compositions/jazz/
  /Documents/schedule.odt
  /Videos/concerts/
  .config
  .local

```

**7.10 Managing Includes with a Simple Include File** **|** **173**

```
  /Music/courses/bassoon.avi</strong>
  [...]
```

Then use the list with the _--files-from_ option:

```
  duchess@pc:~$ rsync -av ~ --files-from ~/include-list.txt \
  duchess@remote.example.com:/backups/
```

**Discussion**

This is the easiest way to maintain a list of files and directories to back up. There are
no excludes, no wildcards, no funny syntax, just a nice clean understandable list.

When you use the tilde to indicate your home directory, leave off the equals sign from
_--files-from_, like the last example in the recipe.

**See Also**

 - _man 1 rsync_

 - Recipe 7.9

 - Recipe 7.11

**7.11 Managing Includes and Excludes with an Exclude File**

**Problem**

You like the simple include file concept in Recipe 7.10, but you really want to have
both includes and excludes.

**Solution**

What you want is an _rsync_ exclude file. An exclude file provides more flexibility and
contains both includes and excludes. The following example illustrates a basic config‐
uration. Every item must start by including the source root, which in this example
is _/home/duchess_, and end with excluding the source root:

```
  # exclude file list
  #
  # include home directory
  + /duchess/
  #
  # include .config and .local, exclude all other dotfiles
  + /duchess/.config
  + /duchess/.local
  - /duchess/.*
  #
  # include jazz/, exclude all other files in Documents

```

**174** **|** **Chapter 7: Backup and Recovery with rsync and cp**

```
  + /duchess/Documents/
  + /duchess/Documents/compositions/
  + /duchess/Documents/compositions/jazz/
  - /duchess/Documents/compositions/*
  - /duchess/Documents/*
  #
  # include schedule.odt, include all .ogg files in
  # arias/, exclude all other files in Music
  + /duchess/Music/
  + /duchess/Music/schedule.odt
  + /duchess/Music/arias/*.ogg
  - /duchess/Music/arias/*
  - /duchess/Music/*
  #
  # includes courses/, exclude all other files in Videos
  + /duchess/Videos/
  + /duchess/Videos/courses/
  - /duchess/Videos/*
  #
  # exclude everything else
  - /duchess/*
```

Feed it to _rsync_ with the _exclude-from=_ option:

```
  duchess@pc:~$ rsync -av ~ \
  --exclude-from=/home/duchess/exclude-list.txt \
  /media/duchess/2tbdisk/
```

**Discussion**

The _exclude-list.txt_ example demonstrates backing up:

 - Two dotfiles, _.config_ and _.local_

 - A single subdirectory of _/Documents_, _/jazz_

 - A single file in _/Music_, _schedule.odt_, and only _.ogg_ files in _/Music/arias/_

 - A single directory in _/Videos_, _/courses_

There must be no spaces between lines, and comments (#) are useful for reminding
you of the purpose of each section, and for adding a bit of whitespace. Preface your
includes with the plus sign and the excludes with the minus sign.

All other files in _/home/duchess_ are excluded from backup. Includes must always
come first. As the example file shows, you have to be precise in defining each include/
exclude. Includes must be listed in their directory hierarchy order, with all subdirec‐
tories. For example, this will fail with all files excluded:

```
  + /duchess/Documents/compositions/
  - /duchess/*

```

**7.11 Managing Includes and Excludes with an Exclude File** **|** **175**

Try including _/Documents_ :

```
  + /duchess/Documents/
  + /duchess/Documents/compositions/
  - /duchess/*
```

Now all the subdirectories and their contents in _/Documents_ are transferred, and not
just _/compositions_ . To copy only _/compositions_ you have to exclude _/Documents_ ; it is
not enough to exclude only _/duchess_ . The following example copies only _/duchess/_
_Documents/compositions/_ and nothing else:

```
  + /duchess/Documents/
  + /duchess/Documents/compositions/
  - /duchess/Documents/*
  - /duchess/*
```

You may use wildcards to include or exclude files by type. For example, include
all _.ogg_ and _.flac_ files, exclude all _.wav_ files, and exclude all _cache_ and _temp_ directories:

```
  # include home directory
  + /duchess/
  #
  # include all ogg and flac files
  + *.ogg
  + *.flac
  #
  # exclude wav files, all cache and temp dirs
  - *.wav
  - cache*
  - temp*
```

You may have multiple source directories.

There is always just one destination directory.

**See also**

 - _man 1 rsync_

 - Recipe 7.10

**7.12 Limiting rsync’s Bandwidth Use**

**Problem**

Large file transfers can use a lot of network bandwidth and slow down everything.
You want a simple way to restrict _rsync_ ’s bandwidth use without implementing some‐
thing complex like traffic shaping.

**176** **|** **Chapter 7: Backup and Recovery with rsync and cp**

**Solution**

Use _rsync_ ’s _--bwlimit_ option. This example limits it to 512 Kbps:

```
  $ rsync --bwlimit=512 -ave ssh ~/Music/arias empress@laptop:songs/
```

**Discussion**

_--bwlimit_ only accepts values in kilobits.

**See Also**

 - _man 1 rsync_

**7.13 Building an rsyncd Backup Server**

**Problem**

You want your users to back up their own data on a central backup server, but you
don’t want to give them shell accounts on your backup server.

**Solution**

Set up a central backup server, and run _rsync_ in daemon mode. You should have
name services already set up, and the hosts on your network have access to the
backup server. Users will not need login accounts on the server because you will use
_rsync_ ’s own access controls and user authorization to control access to the _rsync_
archives.

**For LAN Use Only**

This is suitable for LAN use only, and not over untrusted networks,
because the _rsync_ daemon does not encrypt the authentication or
file transfers. For encrypted transfers you need OpenVPN (Chap‐
ter 13).

_rsync_ must be installed on all machines. _rsyncd_ runs on the backup server, and clients
will use the _rsync_ command to connect to the server.

On the backup server, edit or create _/etc/rsyncd.conf_ to create an _rsync_ module defin‐
ing the archive:

```
  # modules
  [ backup_dir1 ]
  path = /backups
  comment = "server1 public archive"

```

**7.13 Building an rsyncd Backup Server** **|** **177**

```
  list = yes
  read only = no
  use chroot = no
  uid = 0
  gid = 0
```

Create your _/backups_ directory, mode 0700, owned by root, to prevent unauthorized
access from anyone who has access to the server:

```
  $ sudo mkdir /backups/
  $ sudo chmod 0700 /backups/
```

Start _rsyncd_ on the server in daemon mode with systemd:

```
  $ sudo systemctl start rsyncd.service
```

On Debian/Ubuntu it is _rsync.service_ .

If your Linux does not have systemd, start it with the _rsync_ command:

```
  admin@server1:~$ sudo rsync --daemon
```

On the backup server, test that _rsyncd_ is listening and accepting connections:

```
  admin@server1:~$ rsync server1::
  backup_dir1   "server1 public archive"
```

Then test from another PC on your network using the server’s hostname or IP
address:

```
  duchess@pc:~$ rsync server1::
  backup_dir1   "server1 public archive"

  duchess@pc:~$ rsync 192.168.10.15::
  backup_dir1   "server1 public archive"
```

Now you know that it is ready to transfer files. Test that you can copy files to your
new _rsyncd_ server:

```
  duchess@pc:~$ rsync -av ~/drawings server1::backup_dir1
  building file list.....done
  drawings/
  drawings/aug_03
  drawings/sept_03

  wrote 1126399 bytes read 104 bytes 1522.0 bytes/sec
  total size is 1130228 speedup is 0.94
```

Now view the nice new uploaded files:

```
  duchess@pc:~$ rsync server1::backup_dir1/drawings/
  drwx------  4,096 2021/01/04 06:06:55  .
  -rw-r--r--  21,560 2021/09/17 08:53:18  aug_03
  -rw-r--r--  21,560 2021/10/14 16:42:16  sept_03

```

**178** **|** **Chapter 7: Backup and Recovery with rsync and cp**

Upload a few more files to the server, then download files to a different computer
from the _rsyncd_ server:

```
  madmax@buntu:~$ rsync -av server1::backup_dir1/drawings ~/downloads
  receiving incremental file list
  created directory /home/madmax/downloads
  drawings/
  drawings/aug_03
  drawings/sept_03

  sent 123 bytes received 11562479 bytes 1755.00 bytes/sec
  total size is 1141776 speedup is 1.00
```

Everything works. Take a break and enjoy your success.

**Discussion**

This is not a secure form of file transfer because there is no encryption, and anyone
on the network can access the files. It is suitable to use on your local network for easy
archiving and file sharing.

_rsync [hostname]::_ needs double colons when connecting to an _rsync_ server running
in daemon mode. This tells _rsync_ to look for a module name.

These are the command options in the _/etc/rsyncd.conf_ example:

_[backup_dir1]_

The module name can be anything you want.

_path =_

Defines the directory for the module to use.

_comment =_

This is a brief description to remind you who the module belongs to, or what it is
for.

_list=yes_

Permits users to see a list of files in the module. _no_ hides the module.

_read only = no_

This allows users to upload files to the server.

_use chroot = no_

Overrides the default of _use chroot = yes_ . _chroot_ is _change root_, sometimes called a
_chroot jail_ . A _chroot jail_ is a separate environment inside your filesystem that con‐
tains its own root filesystem, commands, libraries, and everything else it needs to
function. This is not a secure environment, though it is commonly thought of as
a security tool. For _rsync_, the man page describes this as useful protection from
configuration errors. The trade-off is _rsync_ is blocked from following symlinks to

**7.13 Building an rsyncd Backup Server** **|** **179**

files outside of the chroot environment, and it complicates preserving UIDs and
GIDs by name. As they say, your mileage may vary, and it may be a good option
for you. See the _use chroot_ section of _rsyncd.conf (5)_ .

Set both _uid_ and _gid_ to _root_ or _0_ . This preserves UIDs and GIDs, and manages per‐
missions correctly.

If any of your transfers fail, look at the _rsync_ error messages. They will tell you if you
made a mistake in your filepaths, misspelled something, or couldn’t connect to the
server, and give useful hints for correcting the problem.

If you are running a Linux without systemd, consult its documentation to learn how
to start and stop rsyncd.

See Recipe 7.14 to learn how to set up access controls.

**See Also**

 - _man 5 rsyncd.conf_

**7.14 Limiting Access to rsyncd Modules**

**Problem**

You don’t want an open _rsyncd_ server, and you want users to have their own protected
modules that other users cannot access.

**Solution**

_rsyncd_ comes with its own simple authentication and access controls. Create a new
file containing username/password pairs, and add _auth users_ and _secrets file_ directives
to _/etc/rsyncd.conf_ .

First create the password file. In the following example, _/etc/rsyncd-users_ sets up three
users and their passwords:

```
  # rsync-users for server1
  duchess:12345
  madmax:23456
  stash:34567
```

Set permissions to read-write for root-only:

```
  $ sudo chmod 0600 /etc/rsyncd-users

```

**180** **|** **Chapter 7: Backup and Recovery with rsync and cp**

Now create a module for one of your users in _/etc/rsyncd.conf_ . This example creates a
module for Duchess, using the _/backups/duchess_ directory on the _rsync_ server:

```
  [ duchess_backup ]
  path = /backups/duchess
  comment = Duchess's private archive
  list = yes
  read only = no
  auth users = duchess
  secrets file = /etc/rsyncd-users
  use chroot = no
  strict modes = yes
  uid = root
  gid = root

```

Create your user’s backup directory, like this example for Duchess, with mode 0700:

```
  $ sudo mkdir /backups/duchess/
  $ sudo chmod -R 0700 /backups/duchess/
```

Now try logging in:

```
  $ rsync duchess@server1::duchess_backup
  Password: 12345
  drwxr-xr-x   4,096 2020/06/29  18:24:43 .
```

Try transferring some files:

```
  $ rsync -av ~/logs duchess@server1::duchess_backup
  Password:
  sending incremental file list
  logs/
  logs/irc.log
  logs/irc_#core-standup.log
  logs/irc_#core.log
  logs/irc_#desktop.log
  logs/irc_#engineering.log
  logs/irc_#mobile.log

  sent 130,507 bytes received 305 bytes 37,374.86 bytes/sec
  total size is 129,383 speedup is 0.99
```

It worked! If the file transfer fails, check the _rsync_ log to learn why. On systemd
Linuxes, read the most recent log entries in the status output:

```
  $ systemctl status rsyncd.service
```

On other Linux distributions the rsyncd log should be in _/var/log_ .

**7.14 Limiting Access to rsyncd Modules** **|** **181**

**Discussion**

The username/password pairs are arbitrary and are not related to system user
accounts. _rsyncd_ users have no access to the host system outside of their _rsync_ shares.

For additional security, add these directives to _/etc/rsyncd.conf_ :

_hosts allow_

Use this to list hosts that are allowed to access the _rsyncd_ archives. For example,
you can limit access to hosts on a single subnet:

```
    hosts allow = *.local.net
    hosts allow = 192.168.1.
```

All hosts not allowed are denied, so you don’t need a _hosts deny_ directive.

_hosts deny_

This usually isn’t needed, if you use _hosts allow_ . It is useful for denying access to
specific hosts that cause annoyance.

The password file is in cleartext, so it must be restricted to the superuser.

**See Also**

 - _man 5 rsyncd.conf_

 - The Discussion in Recipe 7.13 to learn about the command options.

**7.15 Creating a Message of the Day for rsyncd**

**Problem**

You’re running an _rsyncd_ server, and you think it would be nice to greet users with a
cheerful message.

**Solution**

Create your message of the day (MOTD) in a plain-text file, such as _/etc/rsync-motd_ :

```
  Welcome to your local backup server! Please remember to actually back up
  your files!
```

Then configure the MOTD file location at the top of _/etc/rsyncd.conf_ :

```
  [global]
  motd file = /etc/rsync-motd

```

**182** **|** **Chapter 7: Backup and Recovery with rsync and cp**

When users connect to your server, they will see your message:

```
  $ rsync server1::backup_dir1/
  Welcome to your local backup server! Please remember to actually backup your
  files!

  drwx------     4,096 2020/06/29 18:24:43 .
  -rwxr-xr-x     6,400 2015/03/13 08:21:21 keytool
  drwx------     4,096 2020/06/17 06:07:41 WIP
  drwx------     4,096 2020/06/17 06:06:55 bin
  drwxr-xr-x     4,096 2020/06/30 09:47:42 duchess
  [...]
```

**Discussion**

A message of the day is an old Unix tradition. Use it for cheery greetings, mainte‐
nance downtime announcements, security tips, backup tips, or anything you think is
important.

**See Also**

 - _man 5 rsyncd.conf_

**7.15 Creating a Message of the Day for rsyncd** **|** **183**

**<u>CHAPTER 8</u>**
#### **Managing Disk Partitioning with parted**

All mass storage drives—SATA hard disks, solid state drives, USB drives, SD (Secure
Digital), NVMe (Non-Volatile Memory Express), and CompactFlash cards—must be
partitioned and formatted with filesystems before you can use them. They all ship
with some kind of partitioning and filesystems, which may not be what you want. As
your needs change, you will want to repartition your disks and use different filesys‐
tems. In this chapter you will learn about using _parted_ (partition editor) to manage
partitioning.

**Overview**

_parted_ only manages partitioning; see Chapter 11 to learn about filesystems. Chap‐
ter 9 covers the graphical frontend to _parted_, GParted, which manages both partition‐
ing and filesystems.

You will also learn about the modern replacement for the Master Boot Record
(MBR), which is the elderly and inadequate legacy partition table. The MBR has been
supplanted by the new Globally Unique Identifier Partition Table (GUID Partition
Table or GPT).

_parted_ shows partition information and adds, removes, and resizes partitions. _parted_
has just one gotcha: it writes your changes to disk immediately, so you must be care‐
ful. GParted does not apply changes until you click a button.

It is a common convenience to call all mass storage devices _disks_, even though many
of them are not disks anymore, but solid-state devices, like USB sticks. Why not,
when we still dial telephones, and make tape recordings and film videos with our
smartphones?

**185**

A disk partition is a logical division of a storage disk, a way of dividing the disk into
one or more independent regions. A disk must have at least one partition. The num‐
ber of partitions depends on your needs and whims. After partitioning a disk, you
must put a filesystem on each partition, and then you can use it. A single disk may
have multiple partitions, and each partition may have a different filesystem.

The disk name on Linux is always _/dev_ something, which is short for device. For
example, _/dev/sda_ for a hard disk, and _/dev/sr0_ for an optical drive. Partitions are the
disk name plus a number. If _/dev/sda_ has three partitions, they are _/dev/sda1_, _/dev/_
_sda2_, and _/dev/sda3_ .

**Partitioning Schemes**

The default partitioning scheme on some Linux distributions is to stuff the whole
installation into a single partition. This works fine, but setting up a few more parti‐
tions during installation has some advantages:

 - Giving _/boot_ its own partition makes managing multiboot systems easier because
the boot files are independent of whatever operating systems you install or
remove.

 - Put _/home_ on its own partition to isolate it from the root filesystem, so you can
replace your Linux installation without touching _/home_ . _/home_ could even be on
a separate drive.

 - _/var_ and _/tmp_ can fill up from runaway processes. Putting them on their own
partitions prevents them from interfering with the other filesystems.

 - Putting the swap file on its own partition enables suspend-to-disk.

See Chapter 1 to learn more about designing your partitioning layouts.

**Partition Tables: GPT and MBR**

The GUID Partition Table (GPT), first released in 2010, is the modern replacement
for the antique PC-DOS Master Boot Record (MBR). If your only experience is with
the MBR, prepare yourself for a treat, because the GPT is a big improvement.

The MBR was created for IBM PCs way back in the last millennium in the early
1980s, during the exciting era of 10-megabyte (MB) hard disks. The MBR goes on the
first 512 bytes of the first sector of your disk, preceding the first partition, and holds
the bootloader and partition table. The bootloader occupies 446 bytes, the partition
table uses 64 bytes, and the remaining 2 bytes store the boot signature.

64 bytes is not much room to store much of anything, so the MBR is limited to four
primary partitions. One primary partition may hold an extended partition, which can
then be divided into logical partitions. Linux supports (theoretically) an unlimited

**186** **|** **Chapter 8: Managing Disk Partitioning with parted**

number of logical partitions. Even with great thundering herds of logical partitions,
the MBR is limited to addressing a maximum disk size of 2.2 TiB, which these days is
barely enough to hold your cat memes. Why this limitation? You can do the math
yourself: the MBR is limited to 32 bits of addressing, and can address 2 <sup>32</sup> number of
blocks (we’ll discuss blocks and sectors in a moment), so the equation for disks with
512-byte blocks is 2 <sup>32</sup> x 512 = 2.199023256×10 <sup>12</sup> bytes.

**BIOS and UEFI**

The GPT is part of the UEFI (Unified Extensible Firmware Interface) specification.
UEFI replaces your computer’s Basic Input Output System, better known as the PC
BIOS, or just plain BIOS. Figure 8-1 is the old legacy BIOS, and Figure 8-2 is a
modern UEFI, all full of shiny whizbang features, just like a little operating system.

GPT has many advantages over the MBR:

 - Up to 128 partitions on Linux, numbered 1–128, and no messing with primary
and extended partitions

 - Fault-tolerance: copies of the partition table are stored in multiple locations

 - Unique IDs for disks and partitions

 - Legacy BIOS/MBR boot mode

 - Verifies its own integrity and the partition table

 - Secure Boot

_Figure 8-1. Legacy BIOS setup_

**Overview** **|** **187**

_Figure 8-2. UEFI setup_

The MBR is nearly obsolete, and you should use the GPT. In GPT, the first sector of
the disk is reserved for a protective MBR that supports GPT on a BIOS computer, so
we can use the GPT on older systems that have a BIOS instead of UEFI. The boot‐
loader and operating system must both be GPT-aware, which has been the case with
Linux for years. The only reason to use the MBR is on old computers with old operat‐
ing systems that do not support the GPT.

If you have an older system with a BIOS, you cannot upgrade it to UEFI, but must
replace the motherboard to get UEFI. Both UEFI and BIOS are integrated into the
motherboard.

**Blocks and Sectors**

Now we will talk about blocks and sectors, and how they affect the maximum sizes of
your disks, files, and partitions. _Blocks_ are the smallest storage units on a disk that a
filesystem can use. These are logical, not physical, divisions. The smallest physical
unit of storage is a _sector_ . Blocks can span multiple sectors, and a file can span multi‐
ple blocks.

When a file spans multiple blocks, there is a certain amount of waste because files
rarely match block sizes. For example, a file that is one byte larger than four blocks
uses five blocks. The fifth block holds just that one byte, and that block is exclusive to
the file. Because of this you might think that 512-byte blocks are less wasteful. But
there is more information stored in a block than just the file.

**188** **|** **Chapter 8: Managing Disk Partitioning with parted**

Every block, in addition to your file data, stores timestamps, the filename, ownership,
permissions, the block ID, and its correct order with other blocks, the inode, and
other metadata.

4096-byte blocks use one-eighth the metadata of 512-byte blocks. On a 4 TiB hard
disk, you need 8,000,000,000 512-byte blocks. With a 4096-byte block size there are
only 1,000,000,000 blocks, which represents quite a lot of metadata savings.

The sector size limits the size of storage volumes. The standard sector size for hard
disks has been 512 bytes for some years, and now 4096 bytes is the standard because
hard disks have grown so large.

The GPT provides 64-bit addressing, supporting 2 <sup>64</sup> total blocks on a single disk, so a
hard disk with 512-byte blocks can be as large as 9 zettabytes. With 4096-byte blocks,
your maximum disk size is 64 zettabytes, which I daresay is sufficient for even the
most dedicated cat meme collector. These are theoretical maximums, limited by avail‐
able hardware, operating system limits, and filesystem support for large volumes. For
example, the Ext4 filesystem maxes out at 1 EiB for a single filesystem, and a maxi‐
mum 16 TiB file size with a 4096-byte block size. XFS supports a maximum filesystem
and file size of 8 EiB minus 1 byte.

CDs and DVDs have 2048-byte sectors. Solid-state devices such as USB sticks, SD
cards, CompactFlash, and Solid State Drives (SSDs) also have sectors and blocks. The
smallest unit on an SSD is called a _page_ . Common page sizes are 2 KB, 4 KB, 8 KB,
and larger. Blocks contain 128 to 256 pages, and block size is typically 256 KB to
4 MB.

All of these enormous numbers are a bit dizzying. Table 8-1 summarizes the decimal
and binary measurements used to measure disk capacity.

_Table 8-1. Decimal and binary multiples of bytes_

**<mark>Value</mark>** **<mark>Decimal</mark>** **<mark>Value</mark>** **<mark>Binary</mark>**
1 B byte 1 B byte

1000 kB kilobyte 1024 KiB kibibyte

1000 <sup>2</sup> MB megabyte 1024 <sup>2</sup> MiB mebibyte

1000 <sup>3</sup> GB gigabyte 1024 <sup>3</sup> GiB gibibyte

1000 <sup>4</sup> TB terabyte 1024 <sup>4</sup> TiB tebibyte

1000 <sup>5</sup> PB petabyte 1024 <sup>5</sup> PiB pebibyte

1000 <sup>6</sup> EB exabyte 1024 <sup>6</sup> EiB exbibyte

1000 <sup>7</sup> ZB zettabyte 1024 <sup>7</sup> ZiB zebibyte

1000 <sup>8</sup> YB yottabyte 1024 <sup>8</sup> YiB yobibyte

**Overview** **|** **189**

The decimal values are powers of 10; for example, a kilobyte is 1000 bytes, or 10 <sup>3</sup> . The
binary values are powers of two, so a kibibyte is 2 <sup>10</sup>, 1024 bytes. Hard disk manufac‐
turers like to use the decimal format to make their drives look bigger.

Whoever came up with the weird “bibyte” naming scheme just about guaranteed that
nobody would ever want to say the names. It’s all a mishmash anyway, as people like
to use them interchangeably. At any rate, now you know the difference.

**8.1 Unmounting Your Partitions Before Using parted**

**Problem**

You know you must unmount your partition, or partitions, before you can make any
changes with _parted_, and you need to know how.

**Solution**

Unmount a partition from your graphical file manager, or use the _umount_ command.
The following example unmounts _/dev/sdc2_ :

```
  $ sudo umount /dev/sdc2
```

How do you know the correct device name? See Recipe 8.3 to learn how to list your
attached disks and partitions.

If you are creating a new partition table on a disk, you should unmount all the parti‐
tions on it.

**Changing a Running System**

It is risky to unmount filesystems attached to the active root filesys‐
tem, such as _/home_, _/var_, or _/tmp_, if they are on separate partitions.
It is safer to perform partitioning operations from another Linux
instance, such as SystemRescue (Chapter 19), or a second Linux on
the same machine (Chapter 1).

**Discussion**

Technically, you mount and unmount filesystems rather than partitions. However, I
shall not hold it against you if you say “partitions.”

**See Also**

 - _man 8 parted_

 - [Parted User’s Manual](https://oreil.ly/SNyLL)

**190** **|** **Chapter 8: Managing Disk Partitioning with parted**

**8.2 Choosing the Command Mode for parted**

**Problem**

You know you can start the _parted_ command in interactive mode, launching the _par‐_
_ted_ command shell, or run it as an ordinary command, and you want to know how to
do both.

**Solution**

Running _parted_ with no options launches the interactive _parted_ shell. You need root
privileges:

```
  $ sudo parted
  GNU Parted 3.2
  Using /dev/sda
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted)
```

When your normal command prompt changes to _(parted)_, you are in the _parted_ shell.
Type **`help`** to see a list of commands and their descriptions. There is also help for the
individual _parted_ commands, for example, _help print_ . Type _quit_ to exit parted. Most
_parted_ commands can be abbreviated to their first letter, like _h_ and _q_ .

Enter a complete command to run _parted_ as a normal command in your regular shell,
like this example that lists all of your disks:

```
  $ sudo parted /dev/sdb print devices
  /dev/sdb (2000GB)
  /dev/sda (4001GB)
  /dev/sdc (4010MB)
  /dev/sdd (15.7GB)
  /dev/sr0 (425MB)
```

The command runs and exits, and returns to your normal command prompt.

**Discussion**

Be careful in both modes, because _parted_ applies your changes immediately. Always
have good backups before doing anything with _parted_ .

**See Also**

 - _man 8 parted_

 - [Parted User’s Manual](https://oreil.ly/SNyLL)

**8.2 Choosing the Command Mode for parted** **|** **191**

**8.3 Viewing Your Existing Disks and Partitions**

**Problem**

You want to see your existing partitions, their sizes, and what filesystems are on them.

**Solution**

If you don’t know the names of the disks on your system, run _parted_ with no options:

```
  $ sudo parted
  GNU Parted 3.2
  Using /dev/sda
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted)
```

When you have not selected a device, _parted_ guesses which one you want, usually the
first one, and tells you which one it has selected (see _Using /dev/sda_ in the preceding
example).

_print devices_ lists your disk names and sizes:

```
  (parted) print devices
  /dev/sda (256GB)
  /dev/sdb (1000GB)
  /dev/sdc (4010MB)
```

Select which device you want to look at, then display its information:

```
  (parted) select /dev/sdb
  Using /dev/sdb
  (parted) print
  Model: ATA ST1000DM003-1SB1 (scsi)
  Disk /dev/sdb: 1000GB
  Sector size (logical/physical): 512B/4096B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system   Name Flags
  1   1049kB 525MB  524MB  fat16         boot, esp
  2   525MB  344GB  343GB  btrfs
  3   344GB  998GB  654GB  xfs
  4   998GB  1000GB 2148MB linux-swap(v1)    swap

  (parted)
```

Type **`quit`** to exit.

You can open the _parted_ shell to a specific disk:

```
  $ sudo parted /dev/sda
  GNU Parted 3.2

```

**192** **|** **Chapter 8: Managing Disk Partitioning with parted**

```
  Using /dev/sdb
  Welcome to GNU Parted! Type 'help' to view a list of commands.
```

Enter **`print`** with no options to see information about this disk:

```
  (parted) print
  Model: ATA SAMSUNG SSD SM87 (scsi)
  Disk /dev/sda: 256GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  [...]
```

_print all_ lists all partitions on all devices:

```
  (parted) print all
  Model: ATA SAMSUNG SSD SM87 (scsi)
  Disk /dev/sda: 256GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start  End  Size  File system Name          Flags
  1   1049kB 524MB 523MB  fat16    EFI system       legacy_boot,
  partition        msftdata

  2   524MB  659MB 134MB        Microsoft reserved   msftres
  partition
  3   659MB  253GB 253GB  ntfs     Basic data partition  msftdata

  4   253GB  256GB 2561MB ntfs                 diag

  Model: ATA ST1000DM003-1SB1 (scsi)
  Disk /dev/sdb: 1000GB
  Sector size (logical/physical): 512B/4096B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system   Name Flags
  1   1049kB 525MB  524MB  fat16         boot, esp
  2   525MB  344GB  343GB  btrfs
  3   344GB  998GB  654GB  xfs
  4   998GB  1000GB 2148MB linux-swap(v1)    swap

  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: msdos
  Disk Flags:

  Number Start  End   Size  Type   File system Flags
  1   1049kB 4010MB 4009MB primary fat32

```

**8.3 Viewing Your Existing Disks and Partitions** **|** **193**

Find any unpartitioned free space on any disk:

```
  (parted) print free
  Model: ATA ST4000DM000-1F21 (scsi)
  Disk /dev/sda: 4001GB
  Sector size (logical/physical): 512B/4096B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system   Name Flags
  17.4kB 1049kB 1031kB Free Space
  1   1049kB 500MB  499MB  ext4
  2   500MB  60.5GB 60.0GB ext4
  3   60.5GB 2061GB 2000GB xfs
  4   2061GB 2069GB 8000MB linux-swap(v1)
  2069GB 4001GB 1932GB Free Space
```

**Discussion**

Let’s take a look at what all of this output means:

 - _Model_ is the manufacturer’s name for the device.

 - _Disk_ gives the device name and size.

 - _Sector size_ gives both the logical and physical block size. A logical block size of
512B is for backward compatibility with older disk controllers and software.

 - _Partition table_ tells you the partition type, either _msdos_ or _gpt_ .

 - _Flags_ matter more to Windows than Linux. They identify the partition types, and
in some cases are necessary so Windows gets less confused. The full list is in the
_[Parted User’s Manual](https://oreil.ly/SNyLL)_ .

These are the partition flags in the examples:

 - _legacy_boot_ marks a GPT partition as bootable.

 - _msftdata_ labels GPT partitions that contain Microsoft filesystems, either NTFS or
FAT.

 - _msftres_ is a Microsoft reserved partition. This is a special partition that is
required by Microsoft on GPT partitions, for use by the operating system. On
partitions less than 16 GB in size, the MSR is 32 MB, and on larger drives it is 128
MB.

 - _diag_ is a Windows recovery partition.

 - _boot, esp_ both mark the partition as a boot partition. _boot_ is an MBR label, and
_esp_ is a GPT label.

 - _swap_ marks swap partitions.

**194** **|** **Chapter 8: Managing Disk Partitioning with parted**

**See Also**

 - _[Parted User’s Manual](https://oreil.ly/SNyLL)_

 - _man 8 parted_

**8.4 Creating GPT Partitions on a Nonbooting Disk**

**Problem**

You want to repartition a disk, removing all data and starting over with a new GUID
Partition Table (GPT). This is not a bootable disk with an operating system, but is
only for data storage.

**Solution**

First, create the new partition table, then create your partitions, then verify that all
were created correctly. Be very certain that you select the correct disk; see Recipe 8.3
to learn how to list your disks and partitions.

In the following example, there is a USB stick at _/dev/sdc_, which is used for data stor‐
age. It is not a bootable disk with an operating system on it. You must unmount your
devices before running _parted_ . The first step is to unmount it, then create a new GPT
partition table:

```
  $ sudo umount /dev/sdc
  $ sudo parted /dev/sdc
  GNU Parted 3.2
  Using /dev/sdc
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) mklabel gpt
  Warning: The existing disk label on /dev/sdc will be destroyed and all data on
  this disk will be lost. Do you want to continue?
  Yes/No? Yes
  (parted) p
  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start End Size File system Name Flags
```

Now you can create new partitions. The following example creates two partitions that
are about the same size. You must specify a name for the partition, and the start and
end locations for both partitions:

**8.4 Creating GPT Partitions on a Nonbooting Disk** **|** **195**

```
  (parted) mkpart "images" ext4 1MB 2004MB
  (parted) mkpart "audio files" xfs 2005MB 100%
```

Then check your work, and exit:

```
  (parted) print
  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system Name     Flags
  1   1049kB 2005MB 2004MB ext4     images
  2   2006MB 4009MB 2003MB xfs     audio files

  (parted) q
  Information: You may need to update /etc/fstab.
```

If your start or end points are too close to another partition, you will see an error
message. In the following example, the start of the second partition is the same as the
end of the first partition:

```
  (parted) mkpart "images" ext4 2004MB 100%
  Warning: You requested a partition from 2004MB to 4010MB (sectors
  3914062..7831551).
  The closest location we can manage is 2005MB to 4010MB (sectors
  3915776..7831518).
  Is this still acceptable to you?
  Yes/No? Yes
```

Changing it to 200 5MB fixes the error.

**Discussion**

_start_ sets the beginning of the new partition. This is always a number value. The `1MB`
value in the example means one megabyte from the beginning of the disk. You cannot
start at zero because the first 33 sectors are reserved for the EFI label, so the first par‐
tition starts at the 34th sector or higher. I start at the one megabyte mark because it is
easy to remember.

_end_ can take a size value or a percentage. In the example, the end of first partition is
200 5MB from the start of the first partition. The second partition ends at 100% of
the remaining space. Creating a new partition table wipes out all data on the disk.

You must put filesystems on your new partitions before they are usable (see
Chapter 11).

The warning “You may need to update /etc/fstab” applies only if you change parti‐
tions that are in your _/etc/fstab_ file.

The syntax for creating new GPT partitions is _mkpart name fs-type start end_ .

**196** **|** **Chapter 8: Managing Disk Partitioning with parted**

_name_ is required. This is anything you want, so you can make it a name that helps
you remember what the partition is for.

The _fs-type_ label is not required, but you should specify it so that the partition is
assigned the correct filesystem type code. Run _help mkpart_ in the _parted_ shell to see a
list of filesystem labels.

Even though you created filesystem labels, there are no filesystems on your disk. Cre‐
ating filesystems is a separate step.

The filesystem labels sometimes disappear. After you put a filesystem on the parti‐
tion, they will stay put.

The _parted_ help and documentation are a bit confusing on the differences between
creating GPT partitions and MS-DOS partitions. When you create a GPT partition,
you must create a _name_ for it. When you create an MS-DOS partition you must spec‐
ify a _part-type_, which is one of _primary_, _extended_, or _logical_ . There is a fair bit of con‐
fusion about this, and the result is admins creating GPT partition names of _primary_,
_extended_, and _logical_ . This is not correct and you should create _names_ for GPT
partitions.

At any rate, you should not create MS-DOS partition tables because they are obsolete,
except on old computers with old software that does not support GPT.

**See Also**

 - _[Parted User’s Manual](https://oreil.ly/SNyLL)_

 - _man 8 parted_

 - Chapter 11

**8.5 Creating Partitions for Installing Linux**

**Problem**

You want to install Linux on a disk and need to know how to partition it.

**Solution**

Use the partition manager in the Linux installer. You can set up your partitions before
running the installer, but using the installer’s partition manager ensures that it will be
done correctly, and you will see warnings for any errors. See Recipe 1.8 for a sug‐
gested partitioning scheme.

**8.5 Creating Partitions for Installing Linux** **|** **197**

**Discussion**

Most Linux installers provide guidance for partitioning for a new installation and also
allow manual customizations.

**See Also**

 - The introduction to this chapter for partitioning suggestions

 - Chapter 1

**8.6 Removing Partitions**

**Problem**

You want to delete some partitions.

**Solution**

Start _parted_ in interactive mode for the disk you want to make changes on, then print
the partition table:

```
  $ sudo parted /dev/sdc
  GNU Parted 3.2
  Using /dev/sdc
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) p

  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: msdos
  Disk Flags:

  Number Start  End   Size  Type   File system Flags
  1   1049kB 2005MB 2004MB primary
  2   2005MB 4010MB 2005MB primary
```

In this example, delete the second partition by typing _rm 2_ . The partition will be
immediately removed, and there will not be a confirmation. Then type _p_ to verify:

```
  (parted) rm 2
  (parted) p
  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: msdos
  Disk Flags:

```

**198** **|** **Chapter 8: Managing Disk Partitioning with parted**

```
  Number Start  End   Size  Type   File system Flags
  1   1049kB 2005MB 2004MB primary
```

**Discussion**

Be very certain you are deleting the correct partitions. It is OK to make written notes
and check many times before you start.

If you try to delete a mounted partition, _parted_ will warn you with “Warning: Parti‐
tion /dev/sdc2 is being used. Are you sure you want to continue?” You may go ahead
and delete it. Any open files will remain in memory until you reboot or close
them, which is kind of fun because you can still read and save the files to a different
partition.

**See Also**

 - _man 8 parted_

 - [Parted User’s Manual](https://oreil.ly/SNyLL)

**8.7 Recovering a Deleted Partition**

**Problem**

You deleted a partition, and now you wish you hadn’t, and you want to get it back.

**Solution**

If you accidentally deleted a new empty partition, don’t bother trying to recover it,
just create it again. If your partition had a filesystem and data on it, then your best
chance is to try immediate recovery. In the _parted_ shell, use the _rescue_ command, and
give it the partition’s start and end locations. These can be approximate:

```
  (parted) rescue 2000MB 4010MB
  searching for file systems... 40%    (time left 00:01)Information: A ext4
  primary partition was found at 2005MB -> 4010MB. Do you want to add it to the
  partition table?
  Yes/No/Cancel? Yes
```

_parted_ won’t give you any feedback, so print the partition table to see if the lost parti‐
tion came back:

```
  (parted) p
  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

```

**8.7 Recovering a Deleted Partition** **|** **199**

```
  Number Start  End   Size  File system Name  Flags
  1   1049kB 2005MB 2004MB xfs     images
  2   2005MB 4010MB 2005MB ext4
```

And there it is. With a little luck all of your files are intact.

**Discussion**

The longer you wait to try to restore a partition, the more likely it will not be restora‐
ble because it may be unintentionally overwritten. If you need to delay rescue opera‐
tions until a later time, put it away in a safe place, if possible.

As always, your best practice is to always maintain good backups.

**See Also**

 - _[Parted User’s Manual](https://oreil.ly/SNyLL)_

 - _man 8 parted_

**8.8 Increasing Partition Size**

**Problem**

You want to increase the size of an existing partition, which has a filesystem on it.

**Solution**

The following example increases the size of a partition with a filesystem on it. There
are two steps: first resize the partition, then resize the filesystem to match. Every file‐
system has its own set of tools, and you must use the correct tool for increasing the
size. In this recipe, we will resize the Ext4, XFS, Btrfs, and FAT16/32 partitions.

Ext4, XFS, and Btrfs can all be enlarged online or offline. FAT16/32 can be resized
only offline and must be unmounted first.

There must be free space at the end of the partition you want to increase. Open the
_parted_ shell to your selected disk, and look for free space:

```
  $ sudo parted /dev/sdc
  GNU Parted 3.2
  Using /dev/sdc
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) print free
  Model: General USB Flash Disk (scsi)
  Disk /dev/sdc: 4010MB
  Sector size (logical/physical): 512B/512B

```

**200** **|** **Chapter 8: Managing Disk Partitioning with parted**

```
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system Name  Flags
  [...]
  1024MB 2005MB 981MB  Free Space
  2   2005MB 3500MB 1495MB ext4     audio
  3500MB 4010MB 510MB  Free Space
```

This shows 981 MB of free space preceding Partition 2, and 510 MB of free space fol‐
lowing. You can only change the end point of a partition, so the following examples
expand Partition 2 to use all of the 510 MB of free space at the end.

First, expand the partition to its new end point:

```
  (parted) resizepart 2 4010MB
```

You will not see a success message, but if you make a mistake, you will see an error
message. Type **`p`** to see the partition table and verify that _resizepart_ did what you want.

Now you must expand the filesystem to fit the new partition size with the appropriate
command for the filesystem. Table 8-2 shows the commands to use for each filesys‐
tem, expanding them to fill their partitions.

_Table 8-2. Commands to increase filesystem sizes_

**<mark>Filesystem</mark>** **<mark>Resize command</mark>**
Ext4 sudo resize2fs /dev/sd _c2_

XFS sudo xfs_growfs -d /dev/sd _c2_

Btrfs sudo btrfs filesystem resize max /dev/sd _c2_

FAT16/32 sudo fatresize -i /dev/sd _c2_

Remember that FAT16/32 must be unmounted first.

Print the partition table in _parted_ to check your work.

**Discussion**

The examples in this chapter and in Recipe 8.9 are small, using a 4 GB USB stick.
This is great for testing, but in real life you will likely be using larger disks. The com‐
mands are the same, except for partition sizes.

As always, you should have current backups before you start.

You could resize a filesystem to be smaller than the partition, but that doesn’t make
sense. Check out Chapter 11 to learn all about creating and managing filesystems.

**8.8 Increasing Partition Size** **|** **201**

If you are wondering “Where is my favorite filesystem?” I chose Ext4, Btrfs, XFS, and
FAT16/32 because those are the most commonly used Linux filesystems, and they are
all well maintained.

**See Also**

 - Chapter 11

 - _man 8 resize2fs_

 - _man 8 parted_

 - _man 8 xfs_growfs_

 - _man 8 btrfs_

 - _man 8 fsck.vfat_

**8.9 Shrinking a Partition**

**Problem**

You have a partition with a filesystem on it, and you want to shrink it.

**Solution**

XFS filesystems cannot be reduced in size, only increased. You can shrink Ext4, Btrfs,
and FAT16/32. Ext4 and FAT16/32 must be unmounted before shrinking them. Btrfs
can be shrunken online, but it is safer to unmount it first.

Make sure that the used portion of the filesystem you want to shrink is smaller than
the size you want to shrink it to. Use the _du_ command to see how much space your
files occupy:

```
  $ du -sh /media/duchess/shrinkme
  922.6M  /media/duchess/shrinkme
```

You should allow about 40% extra room for metadata, wasted block space, and for
just in case, so in this example the new size should not be smaller than 1.4 GB. If you
need room to add more files, then account for that as well.

Shrinking partitions is a little more complicated than expanding them. There are
more steps, and the filesystems must be shrunk offline. If the partition is on an exter‐
nal storage device, such as a USB stick, unmount it and then shrink it. If it is a parti‐
tion that belongs to your running system, then you must run _parted_ from a bootable
rescue disk, or a second Linux on a multiboot system, so that you can unmount the
filesystem you want to shrink.

**202** **|** **Chapter 8: Managing Disk Partitioning with parted**

After your selected filesystem is unmounted, follow these steps:

 - Run a filesystem check

 - Shrink the filesystem

 - Shrink the partition

Run the following command to check the health of an Ext4 filesystem:

```
  $ sudo e2fsck -f /dev/sdc2
```

Check a Btrfs filesystem:

```
  $ sudo btrfs check /dev/sdc2
```

Check a FAT16/32 filesystem:

```
  $ sudo fsck.vfat -v /dev/sdc2
```

When everything checks out, shrink your filesystem. The examples in Table 8-3
shrink the filesystems to 2000 MB.

_Table 8-3. Commands to decrease filesystem sizes_

**<mark>Filesystem</mark>** **<mark>Resize command</mark>**
Ext4 sudo resize2fs /dev/sd _c2_ 2g

Btrfs sudo btrfs filesystem resize 2g /dev/sd _c2_

FAT16/32 sudo fatresize -s 2G /dev/sd _c2_

Now you can shrink your partition to match the filesystem size. Open the _parted_ shell
to your device and then run the _resize_ command. Specify the partition number and
the end point:

```
  (parted) resizepart 1 2000MB
  Warning: Shrinking a partition can cause data loss, are you sure you want to
  continue?
  Yes/No? y
```

Check your work by printing the partition table in _parted_ .

**Discussion**

Storage media is large and cheap. In the olden days, fiddling with partitions was nec‐
essary for cramming the most files onto a disk. Now we have the luxury of customiz‐
ing their sizes for our convenience.

**8.9 Shrinking a Partition** **|** **203**

**See Also**

 - Chapter 11

 - _man 8 resize2fs_

 - _man 8 parted_

 - _man 8 btrfs_

 - _man 8 fsck.vfat_

**204** **|** **Chapter 8: Managing Disk Partitioning with parted**

**<u>CHAPTER 9</u>**
#### **Managing Partitions and Filesystems** **with GParted**

GParted, the GNOME Partition Manager, is one of my favorite tools on Linux. GPar‐
ted is a nice graphical front-end to the _parted_ partition manager command and all of
the filesystem management commands. You can create, delete, move, copy, and resize
partitions and filesystems, and create new partition tables with just a few clicks. Other
features are data rescue and managing labels and UUIDs.

Labels on partitions and filesystems are useful for identifying partitions and filesys‐
tems in a friendly way, and to give filesystems short, easy names. Without a label, a
filesystem is identified by its long UUID. For example, when you plug in a USB stick
without filesystem labels, it appears as something like _/media/username/1d742b2d-_
_a621-4454-b4d3-469216a6f01e_ . Give it a nice short label like _mystuff_, and then it
mounts as _/media/username/mystuff_ .

After an operation in GParted is complete, the status window offers you the option to
save a logfile of what it did. Save this information and study it because it shows you
the commands it used.

**Changing Your Running System**

For some operations, such as copying, checking and repair, and set‐
ting labels and UUIDs, it is required to unmount the filesystems
first. You cannot unmount the filesystems that are required for
your running system. In this case, use a bootable SystemRescue
CD/USB (Chapter 19). If you are running a multiboot system with
more than one Linux distribution installed, boot to a different
Linux and run GParted from there (see Chapter 1).

**205**

GParted requires root privileges. When you launch GParted, a dialog for entering
your sudo or root password will open (Figure 9-1).

_Figure 9-1. The application launcher asks for a password_

It is common to call all storage media _disks_, even solid-state media like SSDs, USB
drives, SD (Secure Digital), NVMe (Non-Volatile Memory Express), and Compact‐
Flash. GParted manages any of these disks physically attached to your system, inter‐
nal and external.

If you are not familiar with the basics of partitioning and managing filesystems, the
introduction to Chapter 8 provides a detailed overview.

**Be Careful!**

Before you try any of the recipes in this chapter, have current back‐
ups and be very certain that you are operating on the correct disks
and partitions.

Creating a new partition table wipes out your entire disk.

Deleting or otherwise damaging a partition loses all the data on
that partition. It is possible to recover it, but not guaranteed.

USB sticks are great for practice and testing.

**206** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

**9.1 Viewing Partitions, Filesystems, and Free Space**

**Problem**

You want to see all the partitions, filesystems, and free space on all attached disks.

**Solution**

Launch GParted, and use the drop-down menu on the upper right to see all attached
disks (Figure 9-2). Click View → Device Information to open the panel on the left to
see disk information, such as the model, serial number, size, and partition table type.

_Figure 9-2. Viewing disks on GParted_

You will see a lot of information: device names, mountpoints, filesystems, labels, par‐
tition type and sizes, used and total space, and free space. Right-click on any partition
to open the operations menu, and click the Information button at the bottom of the
menu to see more information on that partition (Figure 9-3).

**9.1 Viewing Partitions, Filesystems, and Free Space** **|** **207**

_Figure 9-3. Viewing partition information on GParted_

**Discussion**

GParted does not apply changes until you click the green checkmark in the top tool‐
bar, so it is safe to poke around and explore. If you accidentally click a command,
click the little curvy yellow arrow next to the checkmark to undo.

When you open the right-click operations menu, some commands are grayed out,
because they can be used only on unmounted filesystems. Click the Unmount com‐
mand, and then these commands will become available. Note that any filesystems that
are necessary for your running system cannot be unmounted; in this case, use a Sys‐
temRescue CD/USB (Chapter 19).

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

**208** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

**9.2 Creating a New Partition Table**

**Problem**

You want to reformat a disk with a new GPT partition table. Your existing partition
table is MS-DOS, and you want to replace it with GPT, or it is a used disk with old
installations on it, and you want to start over with a clean disk.

**Solution**

First, be very sure which disk you want to create the new partition table on, because
this will erase all data on the disk. This is one operation that GParted applies immedi‐
ately, after just one warning, and there is no Undo, so be careful.

Select your disk in the top-right dropdown menu, then click Device → Create Parti‐
tion Table (Figure 9-4).

_Figure 9-4. Creating a new partition table_

Select the GPT partition table type and click Apply (Figure 9-5) .

It doesn’t take very long, and then you will have a new, clean, empty disk, all ready to
partition and format with new filesystems.

**9.2 Creating a New Partition Table** **|** **209**

_Figure 9-5. Select the partition table type_

**Discussion**

Always create a GPT partition table, unless you have a reason to use something else.
GParted supports several partition table types, including MS-DOS, BSD, Amiga, and
AIX. GPT and MS-DOS are the most commonly used on the x86 platform. GPT is
for modern large hard disks and is easier to manage and more resilient than the old
MS-DOS partition table. See the introduction to Chapter 8 for detailed information
on partition tables.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Chapter 8

**9.3 Deleting a Partition**

**Problem**

You need to delete one or more partitions.

**Solution**

Select the partition you want to delete, and right-click to open the operations menu.
If it has a mounted filesystem on it, you must first unmount it, which you can do by
clicking Unmount in the menu. Then click Delete, click the green checkmark, and it
is gone (Figure 9-6).

**210** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

_Figure 9-6. Deleting a partition_

You will see a status message when the delete has finished.

**Discussion**

Deleting the partition deletes everything inside the partition, so if you have a filesys‐
tem and data on the partition, be very sure you want to delete it.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Recipe 8.6

**9.4 Creating a New Partition**

**Problem**

You want to create new partitions.

**9.4 Creating a New Partition** **|** **211**

**Solution**

All you need is empty space on a disk. The following example creates a new 400 GB
partition and formats it with an Ext4 filesystem (Figure 9-7).

_Figure 9-7. Creating a new partition_

Click Partition → New in the top menu. This opens a new window, where you enter
your partition size, select your filesystem, and create partition and filesystem labels.
Use either the slider or the New Size (MiB) field to set your filesystem size. The values
in the New Size field are in mibibytes, so 400,000 is 400 GiB. Then click Add, then the
green checkmark.

When finished, see Chapter 6 to learn how to set correct ownership and permissions
on your new filesystem.

**Discussion**

With a GPT partition table, you will always create only primary filesystems. The
other two options, logical partition and extended partition, are only for MS-DOS par‐
tition tables. If you’re not sure which one your disk is using, click View → Device
Information. This opens a pane on the left with information about your disk, includ‐
ing the partition table type.

In the filesystem selector you also have the option to create an empty partition
without a filesystem. This is way down at the bottom, Unformatted. Next to Unfor‐
matted is Clear, which deletes an existing filesystem and preserves the partition.

GParted combines creating a partition and putting a filesystem on it into a single, fast
operation. This is faster than using _parted_, which only creates partitions and rquires
you to create your filesystem separately.

**212** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Chapter 8

 - Chapter 11

**9.5 Deleting a Filesystem Without Deleting the Partition**

**Problem**

You want to remove a filesystem without deleting its underlying partition because
you want to format the partition with a different filesystem, or the existing filesystem
is corrupt and you need to reformat it and then copy your files back into it
(Figure 9-8).

_Figure 9-8. Deleting a filesystem without deleting the partition_

**9.5 Deleting a Filesystem Without Deleting the Partition** **|** **213**

**Solution**

The filesystem must first be unmounted. Right-click on the partition to open the
operations menu, then click Unmount. When that is completed, click Format To.
Scroll to the bottom of the list and click Cleared. This deletes the filesystem without
deleting the partition.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

**9.6 Recovering a Deleted Partition**

**Problem**

You deleted a partition, and now you wish you hadn’t, and you want to get it back.

**Solution**

If you accidentally deleted a new empty partition, don’t bother trying to recover it,
just create it again. If your partition had a filesystem and data on it, then your best
chance is to try an immediate recovery. Click Delete → Attempt Data Rescue.

This could take a long time, and there is no guarantee of success. _parted_ seems to do
this faster; see Recipe 8.7.

**Discussion**

It is usually faster to create a new partition and filesystem, and then replace your files
from backup. But it does not hurt to try recovery first.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Recipe 8.7

**214** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

**9.7 Resizing Partitions**

**Problem**

You want to make a partition larger or smaller.

**Solution**

With GParted, this takes just a few clicks. When a partition is resized, the filesystem
on it must also be resized. GParted does this in a single operation.

To enlarge a partition, there must be free space at the end of it. Ext4, Btrfs, and XFS
can be enlarged online. FAT16/32 must be unmounted first.

**Always Have Backups!**

Remember, always have current backups!

Figure 9-9 shows a FAT32 filesystem with plenty of free space to grow into.

_Figure 9-9. Selecting a partition to resize_

Right-click on the selected partition to open the menu, then click Resize/Move. This
opens a dialog where you set the new size, either by dragging the slider or by typing
the value, in mibibytes, in the New Size field (Figure 9-10).

Click Resize/Move, then click the green checkmark. Enlarging a partition takes just a
minute or two, and you will see a status message when it is finished.

Use the same procedure for shrinking a partition, except this does not require any
free space at the end. Your new partition size should be at least 10% larger than the

**9.7 Resizing Partitions** **|** **215**

space used by your files. Even if you do not plan to add any new files to this filesys‐
tem, you must leave a certain amount of unused capacity, because if the filesystem fills
up completely, you may not be able to access it. Shrinking a partition takes longer
than enlarging it.

_Figure 9-10. Configuring the new partition size_

**Discussion**

The Ext4 filesystem reserves a small amount of space for the root user. If the filesys‐
tem fills up, then root can still access the filesystem and remove files. FAT16/32, Btrfs,
and XFS do not have reserved blocks.

Ext4 and Btrfs can be shrunk online. XFS can only be enlarged, it cannot be shrunk. It
is safer to unmount them before resizing.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Recipe 8.8

 - Recipe 8.9

**9.8 Moving a Partition**

**Problem**

You have a bit of free space between partitions, for example, between _/dev/sda1_
and _/dev/sda2_ . You want to move _/dev/sda2_ into the free space so there is no gap

**216** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

between them. Or, you wish to enlarge _/dev/sda1_, but there is no free space following
it, so you have to move _/dev/sda2_ to make room.

**Solution**

Right-click the partition you want to move to open the operations menu, then click
Resize/Move (Figure 9-11).

_Figure 9-11. Selecting a partition_

In the Resize/Move dialog, you can drag the slider to the left, or enter 0 in the Free
Space Preceding (MiB) field. Then click Resize/Move (Figure 9-12).

_Figure 9-12. Moving a partition_

This will take some time, as much as several hours, depending on how much data is
on the partition.

**9.8 Moving a Partition** **|** **217**

**Discussion**

Moving a partition is more complicated than resizing a partition. When you resize a
partition, you are moving only its endpoint, but moving a partition requires also
changing its starting point, which, to the operating system, is a big change. GParted
usually manages this reliably, but it is risky, so always have good backups.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Chapter 19

**9.9 Copying a Partition**

**Problem**

You want to make a clone of a partition, or several partitions, as backups or to move
data to a new hard disk.

**Solution**

Use GParted’s Copy command. For example, you want to copy _/dev/sdb2_ to a USB
hard drive attached to your system. Copy it to free space equal to or larger than the
partition you are copying.

Right-click on the partition you want to copy (Figure 9-13). Unmount it if it is moun‐
ted, then click Copy.

_Figure 9-13. Copying a partition_

Change to the disk you want to copy it to and click Paste. This opens the configura‐
tion dialog, with options to increase the size and change the location of the new parti‐
tion (Figure 9-14). When you are satisfied with the settings, click Paste.

**218** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

The final step is to click the green checkmark to start the copy. If you change your
mind, click Undo. The copy operation will take a little time, depending on how much
data needs to be copied.

_Figure 9-14. Settings for the new partition_

**Discussion**

The copied partition must go into a new partition of equal or greater size. Copying a
partition into free space saves the hassle of creating the destination partition.

Copying partitions, in my experience, has limited usefulness. The partition and file‐
system UUIDs remain the same, so you cannot use the copied partition on the same
system as the original without changing the UUIDs. (Which you can do in GParted
in the right-click operations menu.) If you change UUIDs for filesystems listed
in _/etc/fstab_, their entries must be updated. I think it is better, in most cases, to create
new partitions and filesystems, and then copy your files into them.

**See Also**

 - [GNOME Partition Editor](https://gparted.org)

 - Chapter 11

 - Recipe 11.6

 - Chapter 19

**9.9 Copying a Partition** **|** **219**

**9.10 Managing Filesystems with GParted**

**Problem**

You want a nice graphical tool for creating new filesystems.

**Solution**

Use GParted, which manages partitions and filesystems. Find the partition you want
to format with a new filesystem, right-click, and select the filesystem you want to use
(see Figure 9-15).

_Figure 9-15. GParted displays filesystem types_

Click the green checkmark in the toolbar to create the new filesystem. Creating a new
filesystem destroys everything on the existing filesystem, so be sure you are in the
right place.

**Discussion**

GParted is one of the best graphical applications in any category. It is a well-organized
frontend to a number of command-line tools for managing partitions and filesys‐
tems, and it makes complicated tasks simple and fast.

GParted shows the filesystem types on mounted and unmounted volumes, displaying
one disk at a time (see Figure 9-16). Click the drop-down menu on the top right to
view other disks.

**220** **|** **Chapter 9: Managing Partitions and Filesystems with GParted**

_Figure 9-16. GParted displays filesystem types_

**9.10 Managing Filesystems with GParted** **|** **221**

**<u>CHAPTER 10</u>**
#### **Getting Detailed Information About** **Your Computer Hardware**

Linux comes with several good utilities for getting detailed information on the hard‐
ware components in your computer. You can sit down at a machine and in minutes
have an inventory of its components and their specifications, without opening the
case.

These utilities are useful for providing detailed information for technical support,
finding the correct drivers for a device, and finding out if it is supported in Linux at
all. You can’t count on manufacturers to provide timely accurate information about
their own products. For example, they will often change their chipsets without chang‐
ing model numbers, which may turn a device that worked fine on Linux into a device
that does not work on Linux. Fortunately, in these modern times Linux support is
much less of a hassle than it used to be.

Ideally, you will also have your computer documentation, or at least the motherboard
manual. Motherboard manuals are usually full of photos, diagrams, and useful infor‐
mation, and you should be able to find them online.

In this chapter you will learn about the _lshw_ (list hardware), _lspci_ (list PCI), _hwinfo_
(hardware information), _lsusb_ (list USB), _lscpu_ (list CPU), and _lsblk_ (list block devi‐
ces) commands.

_lshw_ and _hwinfo_ provide the most complete information.

_lshw_ reports memory configuration, firmware versions, mainboard configuration,
CPU version and speed, cache configuration, bus speed, hardware paths, attached
devices, partitions, and filesystems.

**223**

_hwinfo_ reports computer monitor information, RAID arrays, memory configuration,
CPU information, firmware, mainboard configuration, caches, bus speeds, attached
devices, partitions, and filesystems.

_lsusb_ probes USB buses and the devices attached to them.

_lspci_ probes PCI buses and the devices attached to them.

_lsblk_ lists physical drives, partitions, and filesystems.

_lscpu_ lists information about your CPU.

**10.1 Collecting Hardware Information with lshw**

**Problem**

You want an inventory of the hardware on your system and details about each item.

**Solution**

Try the _lshw_ (Hardware Lister) command with no options, and store the output in a
text file:

```
  $ sudo lshw | tee hardware.txt
  duchess
  description: Laptop
  product: Latitude E7240 (05CA)
  vendor: Dell Inc.
  version: 00
  serial: 456ABC1
  width: 64 bits
  [...]
```

You’ll get several hundred lines of output that include firmware, drivers, capabilities,
serial numbers, version numbers, and bus information. _lshw_ will not probe any device
attached via a wireless network interface, such as a wireless printer, or a smartphone
attached via Bluetooth, but it will report wireless and Bluetooth interfaces.

You may prefer a summary in a hardware path tree view:

```
  $ sudo lshw -short
  H/W path     Device      Class     Description
  ============================================================
  system     To Be Filled By O.E.M.
  /0                bus      H97M Pro4
  /0/0               memory     64KiB BIOS
  /0/b               memory     16GiB System Memory
  /0/b/0              memory     DIMM [empty]
  /0/b/1              memory     8GiB DIMM DDR3 Synchronous
  1333
  MHz (0.8 ns)

```

**224** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

```
  [...]
  /0/100/14/0/5           bus      USB3.0 Hub
  /0/100/14/0/5/1          generic    SAMSUNG_Android
  /0/100/14/0/5/2          printer    MFC-J5945DW
  /0/100/14/0/5/4 wlx9cefd5fe8f20 network    802.11 n WLAN
  /0/100/14/0/b           input     USB Optical Mouse
  /0/100/14/0/c           input     QuickFire Rapid keyboard
  [...]
```

Or try the summary bus view, rather than the hardware path view:

```
  $ sudo lshw -businfo
  Bus info     Device      Class     Description
  =============================================================
  [...]
  cpu@0               processor   Intel(R) Core(TM) i7-4770K
  CPU
  @ 3.50GHz
  usb@3:5.4     wlx9cefd5fe8f20 network    802.11 n WLAN
  usb@3:b              input     USB Optical Mouse
  usb@3:c              input     QuickFire Rapid keyboard
  pci@0000:00:19.0 enp0s25     network    Ethernet Connection (2) I218-V
  pci@0000:00:1a.0          bus      9 Series Chipset Family USB
  scsi@0:0.0.0   /dev/sda     disk      4TB ST4000DM000-1F21
  scsi@0:0.0.0,1  /dev/sda1    volume     476MiB EXT4 volume
  [...]
```

_lshw_ has a graphical interface, which you open with _sudo lshw -X_ . This is often a sepa‐
rate package, for example, _lshw-gtk_ on Ubuntu and _lshw-gui_ on openSUSE and
Fedora.

**Discussion**

_lshw_ [packs a lot of information into its output. Visit Hardware Lister (lshw) to learn](https://oreil.ly/XRGx1)
what everything means.

_lshw_ does not detect FireWire interfaces or computer monitors.

The example says “system To Be Filled By O.E.M.” because it is a homebrew machine.
A branded computer, such as Lenovo or Dell, should have the brand name and
model.

The _H/W path_ column contains hardware paths, which are analogous to filepaths. /0
is _/system/bus_, which means computer and motherboard. Then all the following
entries are in a tree view, similar to a file tree. As you can see in the example
output, /0/0 is _/system/bus/BIOS memory_, /0/b is the first populated RAM slot,
and /0/b/1 is the second populated RAM slot. These paths correspond to physical
connections on your motherboard and are commonly called _slots_, even though most
of them are soldered to the motherboard and do not have physical slots that you can
plug expansion cards into.

**10.1 Collecting Hardware Information with lshw** **|** **225**

**See Also**

 - [Hardware Lister (lshw)](https://oreil.ly/axiyL)

 - _man 1 lshw_

**10.2 Filtering lshw Output**

**Problem**

_lshw_ sure does dump a lot of information, and you want to limit the output to what
you want to see.

**Solution**

Run _sudo lshw -short_ or _sudo lshw -businfo_ to see a list of device classes, then name
one or more device classes that you want to see:

```
  $ sudo lshw -short -class bus -class cpu
```

Omit the _-short_ option to see detailed information.

Format the long output as HTML, XML, or JSON, and store it in a file so you can use
your favorite scripting hacks to parse the output:

```
  $ sudo lshw -html -class bus -class cpu | tee lshw.html
  $ sudo lshw -xml -class printer -class display -class input | tee lshw.xml
  $ sudo lshw -json -class storage | tee lshw.json
```

Remove sensitive information with the _-sanitize_ option, such as IP addresses and
serial numbers, to make it safer to share with technical support:

```
  $ sudo lshw -json -sanitize -class bus -class cpu | tee lshw.json
```

**Discussion**

The _tee_ command displays output on the screen and stores it in a text file.

**See Also**

 - [Hardware Lister (lshw)](https://oreil.ly/qCioO)

 - _man 1 lshw_

**226** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

**10.3 Detecting Hardware, Including Displays and RAID**
**Devices, with hwinfo**

**Problem**

You want to get information on your computer monitor and RAID devices, as well as
other devices on your system.

**Solution**

The _hwinfo_ command provides a detailed hardware inventory, including monitors
and RAID devices on your system. The following example probes your monitor:

```
  $ hwinfo --monitor
  [...]
  Hardware Class: monitor
  Model: "VIEWSONIC VX2450 SERIES"
  Vendor: VSC "VIEWSONIC"
  Device: eisa 0xe226 "VX2450 SERIES"
  [...]
```

The complete output is quite a bit longer than this example, and it includes all sup‐
ported screen resolutions, date of manufacture, synchronization ranges, type of mon‐
itor, and refresh frequencies.

Another nice feature is detecting RAID devices. It does not detect them by default, so
use the _--listmd_ option:

```
  $ hwinfo --listmd
```

If it returns nothing, there are no RAID devices on your system. If there are, it prints
a lot of information.

Create a summary of your hardware:

```
  $ hwinfo --short
  keyboard:
  /dev/input/event4  CM Storm QuickFire Rapid keyboard
  mouse:
  /dev/input/event5  CM Storm QuickFire Rapid keyboard
  /dev/input/mice   Logitech Optical Wheel Mouse
  printer:
  Brother Industries MFC-J5945DW
  monitor:
  VIEWSONIC VX2450 SERIES
  graphics card:
  Intel Xeon E3-1200 v3/4th Gen Core Processor Integrated
  [...]

```

**10.3 Detecting Hardware, Including Displays and RAID Devices, with hwinfo** **|** **227**

Get detailed information on one or more hardware components:

```
  $ hwinfo --mouse --network --cdrom
```

Consult _man 8 hwinfo_ for a list of device names, or run _hwinfo --help_ :

```
  $ hwinfo --help
  Usage: hwinfo [OPTIONS]
  Probe for hardware.
  Options:
  --<HARDWARE_ITEM>
  This option can be given more than once. Probe for a particular
  HARDWARE_ITEM. Available hardware items are:
  all, arch, bios, block, bluetooth, braille, bridge, camera,
  cdrom, chipcard, cpu, disk, dsl, dvb, fingerprint, floppy,
  framebuffer, gfxcard, hub, ide, isapnp, isdn, joystick, keyboard,
  memory, mmc-ctrl, modem, monitor, mouse, netcard, network, partition,
  pci, pcmcia, pcmcia-ctrl, pppoe, printer, redasd,
  reallyall, scanner, scsi, smp, sound, storage-ctrl, sys, tape,
  tv, uml, usb, usb-ctrl, vbe, wlan, xen, zip
  [...]
```

**Discussion**

_hwinfo_ prints useful and complete information. For example, for network interfaces it
shows their _/sys_ paths, drivers, link status, and MAC addresses. CD-ROM output
includes the model name, revision number, drivers, device files, drive speed, a fea‐
tures list, and whether there is a disk in the drive. _hwinfo_ often tells you more than
the manufacturer’s product information.

**See Also**

 - _man 8 hwinfo_

 - [hwinfo on GitHub](https://oreil.ly/BsDAT)

**10.4 Detecting PCI Hardware with lspci**

**Problem**

You want to list devices attached to the PCI bus on your computer with vendor and
version information.

**Solution**

Run the _lspci_ (list PCI) command. The following example prints a summary list of all
PCI devices:

**228** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

```
  $ lspci
  00:00.0 Host bridge: Intel Corporation 4th Gen Core Processor DRAM Controller
  (rev 06)
  00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen
  Core Processor Integrated Graphics Controller (rev 06)
  00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor
  HD Audio Controller (rev 06)
  [...]
```

Increase verbosity to see more details:

```
  $ lspci -v
  $ lspci -vv
  $ lspci -vvv
```

When you see “access denied” messages, try _sudo lspci_ to see what you’re missing.

**Discussion**

_lspci_ reads information from the PCI bus, which includes onboard components on
your motherboard as well as expansion cards plugged into PCI slots.

_lspci_ displays additional information from its own database of hardware IDs, such as
vendors, devices, and classes and subclasses. This information is stored in a text file
in various locations, depending on your Linux distribution. Ubuntu puts it in _/usr/_
_share/misc/pci.ids_, Fedora uses _/usr/share/hwdata/pci.ids_, and openSUSE uses _/usr/_
_share/pci.ids_ . The man page for your Linux should tell you where it is, or search for
the _pci.ids_ file ( _locate pci.ids_ ).

The _lspci_ maintainers welcome submissions of updated information; read your _pci.ids_
file for instructions. Run the _sudo update-pciids_ command periodically to update your
PCI IDs database.

PCI is short for Peripheral Component Interconnect. PCI is a local hardware bus; that
is, a means for the various hardware devices in your computer to communicate with
the Linux kernel. _lspci_ primarily detects controllers, buses, and some individual devi‐
ces, including:

 - SATA controllers

 - Audio controllers and devices

 - Video controllers and devices

 - Ethernet controllers

 - USB controllers

 - Communication controllers

 - Ethernet controllers

 - RAID controllers

**10.4 Detecting PCI Hardware with lspci** **|** **229**

 - Integrated SD/MMC card readers

 - PCI FireWire controllers

There have been several PCI protocols over the years. The current standard is PCIe,
PCI Express, introduced in 2003. It is backward compatible with all legacy PCI proto‐
cols, and it replaces PCI, PCI-X, and AGP. Remember AGP, the Accelerated Graphics
Port protocol? AGP video cards were faster than PCI video cards because AGP pro‐
vided a dedicated link for video processing.

PCIe is substantially different from the earlier protocols because, just like AGP, each
device gets it own dedicated link. The older protocols used a shared parallel bus,
which was considerably slower.

**See Also**

 - _man 8 lspci_

 - _man 8 update-pciids_

**10.5 Understanding lspci Output**

**Problem**

Most of the output of _lspci_ makes sense because it is device specifications. But you
want to know what the numbers at the beginning of each device line are for, like this
example:

```
  $ lspci
  [...]
  00:1f.2 SATA controller: Intel Corporation 9 Series Chipset Family SATA
  Controller [AHCI Mode]
  [...]
```

**Solution**

_00:1f.2_ is the device’s BDF number, _bus:device.function_ . Bus number 00, device num‐
ber 1f, and function number 2. A function number of 2 means the device has two
functions, and each one gets its own PCI address.

Use the tree view to see the relationship between the PCI bus and the devices:

```
  $ lspci -tvv
  -[0000:00]-+-00.0 Intel Corporation 4th Gen Core Processor DRAM Controller
  +-02.0 Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor
  Integrated Graphics Controller
  +-03.0 Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD
  Audio Controller

```

**230** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

```
  +-14.0 Intel Corporation 9 Series Chipset Family USB xHCI Controller
  +-16.0 Intel Corporation 9 Series Chipset Family ME Interface #1
  +-19.0 Intel Corporation Ethernet Connection (2) I218-V
  +-1a.0 Intel Corporation 9 Series Chipset Family USB EHCI
  Controller #2
  +-1b.0 Intel Corporation 9 Series Chipset Family HD Audio Controller
  +-1c.0-[01]-  +-1c.3-[02-03]----00.0-[03]-  +-1d.0 Intel Corporation 9 Series Chipset Family USB EHCI
  Controller #1
  +-1f.0 Intel Corporation H97 Chipset LPC Controller
  +-1f.2 Intel Corporation 9 Series Chipset Family SATA Controller
  [AHCI Mode]
  \-1f.3 Intel Corporation 9 Series Chipset Family SMBus Controller
```

PCs almost always have a single PCI bus, which is always 00.

**Discussion**

The zeroes enclosed in brackets at the root of the tree, [0000:00], identify the _domain_
and _bus_ . The first four zeroes are the domain number, and the two zeroes after the
colon are the bus number. The domain is the host bridge. The PCI host bridge con‐
nects the PCI controller to the CPU. _Domain_ is a Linux-specific term, and it is more
commonly called the _segment group_ . You can also see this with the _-D_ option:

```
  $ lspci -D
  0000:00:00.0 Host bridge: Intel Corporation 4th Gen Core Processor DRAM
  Controller (rev 06)
  0000:00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen
  Core Processor Integrated Graphics Controller (rev 06)
  0000:00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core
  Processor HD Audio Controller
  [...]
```

You will see multiple host bridges on servers with multiple physical CPUs, and some‐
times multiple buses on a single domain.

**See Also**

 - _man 8 lspci_

**10.6 Filtering lspci Output**

**Problem**

_lspci_ outputs a lot of information, and you want to filter it to see just what you want
to see.

**10.6 Filtering lspci Output** **|** **231**

**Solution**

Use the _awk_ command to cut out the clutter. The following example finds only entries
pertaining to USB:

```
  $ lspci -v | awk '/USB/,/^$/'
  00:14.0 USB controller: Intel Corporation 9 Series Chipset Family USB xHCI
  Controller (prog-if 30 [XHCI])
  Subsystem: ASRock Incorporation 9 Series Chipset Family USB xHCI
  Controller
  Flags: bus master, medium devsel, latency 0, IRQ 26
  Memory at efc20000 (64-bit, non-prefetchable) [size=64K]
  Capabilities: <access denied>
  Kernel driver in use: xhci_hcd

  00:1a.0 USB controller: Intel Corporation 9 Series Chipset Family USB EHCI
  Controller #2 (prog-if 20 [EHCI])
  Subsystem: ASRock Incorporation 9 Series Chipset Family USB EHCI
  Controller
  Flags: bus master, medium devsel, latency 0, IRQ 16
  Memory at efc3b000 (32-bit, non-prefetchable) [size=1K]
  Capabilities: <access denied>
  Kernel driver in use: ehci-pci
```

You must use the classes (Audio, Ethernet, USB, etc.) as they appear in the output
from _lspci_, and pay attention to case, because using _awk_ to run a case-insensitive
search is complicated. This example shows the audio controller and device:

```
  $ lspci -v | awk '/Audio/,/^$/'
  00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor
  HD Audio Controller (rev 06)
  Subsystem: ASRock Incorporation Xeon E3-1200 v3/4th Gen Core Processor
  HD Audio Controller
  Flags: bus master, fast devsel, latency 0, IRQ 31
  Memory at efc34000 (64-bit, non-prefetchable) [size=16K]
  Capabilities: <access denied>
  Kernel driver in use: snd_hda_intel
  Kernel modules: snd_hda_intel

  00:1b.0 Audio device: Intel Corporation 9 Series Chipset Family HD Audio
  Controller
  Subsystem: ASRock Incorporation 9 Series Chipset Family HD Audio
  Controller
  Flags: bus master, fast devsel, latency 0, IRQ 32
  Memory at efc30000 (64-bit, non-prefetchable) [size=16K]
  Capabilities: <access denied>
  Kernel driver in use: snd_hda_intel
  Kernel modules: snd_hda_intel
```

Adjust the verbosity level as needed.

**232** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

You may also select items by vendor, device, or class number. Find these numbers
with the _-nn_ option. In this example, `0300` (enclosed in square braces) is the class
number, `8086` is the vendor number, and `0412` is the device number:

```
  $ lspci -nn
  [....]
  00:02.0 VGA compatible controller [0300]: Intel Corporation
  Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics Controller
  [8086:0412] (rev 06)
  [...]
```

The following examples filter by class, vendor, and device, respectively:

```
  $ lspci -d ::0604
  00:1c.0 PCI bridge: Intel Corporation 9 Series Chipset Family PCI Express Root
  Port 1 (rev d0)
  00:1c.3 PCI bridge: Intel Corporation 82801 PCI Bridge (rev d0)
  02:00.0 PCI bridge: ASMedia Technology Inc. ASM1083/1085 PCIe to PCI Bridge (rev
  03)

  $ lspci -d 8086::
  00:00.0 Host bridge: Intel Corporation 4th Gen Core Processor DRAM Controller
  (rev 06)
  00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen
  Core Processor Integrated Graphics Controller (rev 06)
  00:03.0 Audio device: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor
  HD Audio Controller (rev 06)
  [...]

  $ lspci -d :0412:
  00:02.0 VGA compatible controller: Intel Corporation Xeon E3-1200 v3/4th Gen
  Core Processor Integrated Graphics Controller (rev 06)
```

[Another way to find these numbers is to look them up at the PCI ID Repository.](https://oreil.ly/f2EKi)

**Discussion**

_awk_ is a marvelous power tool for extracting specific text strings from command out‐
put or documents. The caret, _^_, is a regular expression anchor that matches the start
of a string, and _$_ matches the end, so in this example, _/^$/_ looks for the line breaks,
the empty spaces at the beginning and end of the text blocks. This is a great trick for
extracting text blocks from sources that have spaces between sections.

**See Also**

 - _man 1 grep_

 - _man 8 lspci_

 - [the PCI ID Repository](https://oreil.ly/f2EKi)

**10.6 Filtering lspci Output** **|** **233**

**10.7 Using lspci to Identify Kernel Modules**

**Problem**

You want to know which kernel modules your PCI devices are using, and which ones
are available on your system.

**Solution**

Use the _-k_ option. The following example queries only the Ethernet controller:

```
  $ lspci -kd ::0200
  00:19.0 Ethernet controller: Intel Corporation Ethernet Connection (2) I218-V
  Subsystem: ASRock Incorporation Ethernet Connection (2) I218-V
  Kernel driver in use: e1000e
  Kernel modules: e1000e
```

You may also use _awk_, like this example for your graphics controller:

```
  $ lspci -vmmk| awk '/VGA/,/^$/'
  Class: VGA compatible controller
  Vendor: Intel Corporation
  Device: Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics Controller
  SVendor:    ASRock Incorporation
  SDevice:    Xeon E3-1200 v3/4th Gen Core Processor Integrated Graphics
  Controller
  Rev:  06
  Driver: i915
  Module: i915
```

**Discussion**

The _-k_ option shows the kernel modules in use, and all of the available kernel mod‐
ules for each device. Usually the in-use and available entries are the same, but some‐
times there are multiple modules available.

When you use _awk_ remember to add some verbosity, or you may not see the informa‐
tion you want. See the Discussion in Recipe 10.6 to learn about the _awk_ options.

**See Also**

 - _man 1 awk_

 - _man 8 lspci_

**234** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

**10.8 Using lsusb to List USB Devices**

**Problem**

You want a quick, easy tool for listing USB devices on your system.

**Solution**

_lsusb_ lists USB buses and connected USB devices, including mice, keyboards, USB
sticks, printers, smartphones, and other connected peripherals. The following two
examples show two different views of the same devices.

Run _lsusb_ with no options to see a summary of USB devices on your system. In the
next example, three external USB devices are connected: a keyboard, mouse, and
wireless network interface:

```
  $ lsusb
  [...]
  Bus 003 Device 011: ID 148f:5372 Ralink Technology, Corp. RT5372 Wireless Adapter
  Bus 003 Device 002: ID 0bda:5401 Realtek Semiconductor Corp. RTL 8153 USB 3.0
  hub with gigabit ethernet
  Bus 003 Device 006: ID 046d:c018 Logitech, Inc. Optical Wheel Mouse
  Bus 003 Device 005: ID 2516:0004 Cooler Master Co., Ltd. Storm QuickFire Rapid
  Mechanical Keyboard
  [...]
```

This example shows the same thing, with more details in a USB bus hierarchy format,
including kernel drivers, device codes and vendor numbers, and port numbers:

```
  $ lsusb -tv
  [...]
  /: Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/14p, 480M
  ID 1d6b:0002 Linux Foundation 2.0 root hub
  |__ Port 3: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M
  ID 0bda:5401 Realtek Semiconductor Corp. RTL 8153 USB 3.0 hub with
  gigabit ethernet
  |__ Port 7: Dev 11, If 0, Class=Vendor Specific Class, Driver=rt2800usb, 480M
  ID 148f:5372 Ralink Technology, Corp. RT5372 Wireless Adapter
  |__ Port 11: Dev 5, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
  ID 2516:0004 Cooler Master Co., Ltd. Storm QuickFire Rapid Mechanical
  Keyboard
  |__ Port 12: Dev 6, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
  ID 046d:c018 Logitech, Inc. Optical Wheel Mouse
  [...]
```

The following examples show what it looks like when you plug in an external USB
hub with a Bluetooth interface and a Samsung smartphone attached to the hub:

```
  $ lsusb
  [...]
  Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

```

**10.8 Using lsusb to List USB Devices** **|** **235**

```
  Bus 003 Device 012: ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy series,
  misc. (MTP mode)
  Bus 003 Device 013: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle
  (HCI mode)
  Bus 003 Device 002: ID 0bda:5401 Realtek Semiconductor Corp. RTL 8153 USB 3.0
  hub with gigabit ethernet
  [...]

  $ lsusb -tv
  [...]
  /: Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/14p, 480M
  ID 1d6b:0002 Linux Foundation 2.0 root hub
  |__ Port 3: Dev 2, If 0, Class=Hub, Driver=hub/4p, 480M
  ID 0bda:5401 Realtek Semiconductor Corp. RTL 8153 USB 3.0 hub with
  gigabit ethernet
  |__ Port 4: Dev 12, If 0, Class=Imaging, Driver=, 480M
  ID 04e8:6860 Samsung Electronics Co., Ltd Galaxy series, misc. (MTP
  mode)
  |__ Port 2: Dev 13, If 0, Class=Wireless, Driver=btusb, 12M
  ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
  |__ Port 2: Dev 13, If 1, Class=Wireless, Driver=btusb, 12M
  ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
  [...]
```

**Discussion**

The bus and port numbers are always the same. The dev number changes every time
you plug in a device.

The ID numbers, for example, `0a12:0001`, are the vendor and device codes. Manufac‐
turers must apply to _[https://usb.org](https://usb.org)_ for new codes. You can find the list of current
[USB IDs at linux-usb.org and to contribute updated information.](https://oreil.ly/bHLo6)

The class codes are also managed by _[https://usb.org](https://usb.org)_ ; see [USB class codes. I find it](https://oreil.ly/vNCgT)
interesting that Dev 57, which is a Samsung Android phone, is classed as an imaging
device. However, it makes sense because most Linux distributions use the Media
Transfer Protocol (MTP) to transfer files from an Android phone.

The examples in this section are from a PC that has both USB 2.0 and USB 3.1 ports.
The _lsusb_ output shows the negotiated speeds the devices are using, so when you see
something like `usbhid, 1.5M`, instead of `480M` or `5000M`, that is all right because that is
a keyboard, which does not need the full speed of the USB link. You should see higher
speeds for storage devices, such as USB sticks and external hard drives.

**236** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

**See Also**

 - _man 8 lsusb_

 - _[https://usb.org](https://usb.org)_

 - _[https://oreil.ly/js1oj](https://oreil.ly/js1oj)_

**10.9 Listing Partitions and Hard Disks with lsblk**

**Problem**

You need a quick way to list all of your attached storage drives, and their partitions.

**Solution**

Use the _lsblk_ (list block devices) command. Run it with no options to generate a list of
all block devices on your computer:

```
  $ lsblk
  NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
  sda   8:0  0  3.7T 0 disk
  ├─sda1  8:1  0  476M 0 part /boot
  ├─sda2  8:2  0 55.9G 0 part /
  ├─sda3  8:3  0  1.8T 0 part /home
  └─sda4  8:4  0  7.5G 0 part [SWAP]
  sdb   8:16  0  1.8T 0 disk
  ├─sdb1  8:17  0  102M 0 part
  ├─sdb2  8:18  0  6.5G 0 part
  ├─sdb3  8:19  0  1.1G 0 part [SWAP]
  └─sdb4  8:20  0  1.8T 0 part
  sdc   8:32  0  3.7T 0 disk
  ├─sdc1  8:33  0  128M 0 part
  ├─sdc2  8:34  0 439.7G 0 part
  └─sdc3  8:35  0  3.2T 0 part
  sdd   8:48  1  3.8G 0 disk
  └─sdd1  8:49  1  3.8G 0 part
  sr0   11:0  1 159.3M 0 rom
```

Show the filesystem labels and UUIDs on the selected device:

```
  $ lsblk -f /dev/sdc
  NAME  FSTYPE LABEL         UUID        MOUNTPOINT
  sdc
  ├─sdc1
  ├─sdc2 ntfs  Seagate Backup Plus  2E203F82203F5057
  └─sdc3 ext4  backup        0451d428-9716-4cdd /media/max/backup

```

**10.9 Listing Partitions and Hard Disks with lsblk** **|** **237**

List only SCSI devices and their types:

```
  $ lsblk -S
  NAME HCTL    TYPE VENDOR  MODEL       REV TRAN
  sda 0:0:0:0  disk ATA   ST4000DM000-1F21 CC54 sata
  sdb 2:0:0:0  disk ATA   SAMSUNG HD204UI 0001 sata
  sdc 6:0:0:0  disk Seagate BUP SL      0304 usb
  sr0 4:0:0:0  rom ATAPI  iHAS424  B   GL1B sata
```

**Discussion**

_sda_ and _sdb_ are SATA hard disks, and _sdc_ is a USB flash drive. On Linux, mass storage
devices such as SATA hard disks and flash media use the SCSI driver. _sr0_, _rom_, and
_ATAPI_ all identify a CD/DVD player.

Defining the term _block devices_ without starting arguments is rather difficult because
it’s a programming term that does not translate well to a concise userland concept. In
my experience it is most useful to think of block devices as mass storage devices and
the partitions on storage devices.

`MAJ:MIN` are the major and minor numbers. The major number identifies the cate‐
gory, for example, 8 is for _sd_ devices, and the minor number labels each device in
sequence. (Run **`lsblk -l`** to see this in a tree structure.)

`RM` tells if it a removable drive or not, with 1 indicating a removable drive.

`SIZE` is the size of the block device.

`RO = 0` means the device is not read-only, and 1 is read-only. _sr0_, the CD/DVD drive,
is a read-write drive, but _lsblk_ cannot tell you if the disk in _sr0_ is writeable.

`TYPE` identifies the disk type.

`MOUNTPOINT` shows the paths, if the device is mounted.

**See Also**

 - _man 8 lsblk_

**10.10 Getting CPU Information**

**Problem**

You want to know what CPU or CPUs are on your system, and their specifications.

**238** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

**Solution**

Run the _lscpu_ (list CPU) command with no options:

```
  $ lscpu
  Architecture:    x86_64
  CPU op-mode(s):   32-bit, 64-bit
  Byte Order:     Little Endian
  CPU(s):       8
  On-line CPU(s) list: 0-7
  Thread(s) per core: 2
  Core(s) per socket: 4
  Socket(s):      1
  Vendor ID:      GenuineIntel
  CPU family:     6
  Model:        60
  Model name:     Intel(R) Core(TM) i7-4770K CPU @ 3.50GHz
  [...]
  L1d cache:      128 KiB
  L1i cache:      128 KiB
  L2 cache:      1 MiB
  L3 cache:      8 MiB
  [...]
```

This spits out a large amount of information; you will also see a large number of flags,
which list capabilities, and L cache information.

**Discussion**

There are three types of CPU caches: L1, L2, and L3. These are small memory caches
on the CPU. They are very fast, many times faster than system RAM, and store the
data that the CPU is most likely to need for its next operations. L1 is the fastest and
most expensive, so it is usually the smallest. L2 is the next fastest and less expensive,
and is usually larger than L1. L3 is the slowest and least expensive, and usually the
largest.

The CPU in the preceding example has four caches. Use the _-C_ option to see more
detailed cache information:

```
  $ lscpu -C
  NAME ONE-SIZE ALL-SIZE WAYS TYPE    LEVEL
  L1d    32K   128K  8 Data      1
  L1i    32K   128K  8 Instruction   1
  L2    256K    1M  8 Unified     2
  L3     8M    8M  16 Unified     3
```

This shows four caches, shared among the four physical CPU cores. L1i caches store
CPU instructions, and L1d caches store data. L2 and L3 store data.

**10.10 Getting CPU Information** **|** **239**

The number of CPU cores can be a little confusing. `CPU(s): 8` does not mean 8 phys‐
ical cores in this example; instead, that is how many cores the Linux kernel sees. The
following lines tell the full story:

```
  Thread(s) per core: 2
  Core(s) per socket: 4
  Socket(s):      1
```

This is a single processor with four physical cores and two threads per core, for a total
of eight logical CPUs.

**See Also**

 - _man 1 lscpu_

**10.11 Identifying Your Hardware Architecture**

**Problem**

You’re not sure what the hardware architecture is on a machine; you think it is either
x86-64 or ARM, and you need to know which it is.

**Solution**

Use the _uname_ command. This example is on an x86-64 machine:

```
  $ uname -m
  x86_64
```

The following list contains some of the more common results you might see:

 - arm

 - aarch64

 - armv7* (arm7 and below are 32-bit)

 - armv8* (arm8 and up is 64-bit)

 - ia64

 - ppc

 - ppc64

 - s390x

 - sparc

 - sparc64

 - i386

**240** **|** **Chapter 10: Getting Detailed Information About Your Computer Hardware**

 - i686

 - x86_64

If the machine is not running Linux, try booting it with a SystemRescue USB stick,
and then run _uname -m_ .

You can install Linux on a Chromebook. Chromebooks use both Intel and ARM pro‐
cessors. One way to see what yours has is to open the web browser to _chrome://system_ .
This shows all the system information, probably more than you want.

A friendlier tool is [Cog System Info Viewer, which displays hardware and network](https://oreil.ly/Yeirk)
information on Chromebooks.

**Discussion**

Linux supports more hardware architectures than any other operating system, from
tiny embedded systems and systems on a chip (SoCs), to mainframes and supercom‐
puters and everything in between. Whatever obscure computing hardware you might
have, chances are that some flavor of Linux will run on it.

**See Also**

 - _man 1 uname_

**10.11 Identifying Your Hardware Architecture** **|** **241**

**<u>CHAPTER 11</u>**
#### **Creating and Managing Filesystems**

Linux supports a lot of filesystems, more than any other operating system. Filesys‐
tems are essential to computing and do an astounding amount of work. A computer
filesystem stores, organizes, and protects our data, and is under continual stress from
being constantly in use. As Linux users we are fortunate to have many first-rate file‐
systems to choose from.

In this chapter you will learn about the command-line tools for creating and manag‐
ing the following general-purpose filesystems, which are fully supported on Linux
and well maintained:

 - Ext4, the Extended Filesystem

 - XFS, the X File System; the X stands only for X

 - Btrfs, the b-tree filesystem, pronounced Butter FS

 - FAT16/32, File Allocation Table 16- and 32-bit

 - exFAT, Extended FAT, Microsoft’s newest 64-bit filesytem

Not included in this chapter are Microsoft’s NTFS or Apple’s HFS/HFS+/APFS. Linux
has good support for Microsoft’s NTFS, both read and write. To try it, look for _ntfs-3g_
(NTFS third generation) packages.

Support for Apple’s HFS/HFS+/APFS is unreliable. To give it a test drive, look for
packages with _hfs_ or _apfs_ in the names, and make sure the description specifies they
are for Apple filesystems.

There are many special-purpose filesystems, such as UBIFS and JFFS2 for Compact‐
Flash devices; the compressed filesystem SquashFS, HDFS, CephFS, and GlusterFS
for distributed computing; NFS for network file sharing; and many more. These

**243**

could easily fill a large book by themselves and are not included here. They are freely
available to try out and learn.

**Filesystem Overview**

Before you can use any storage device, such as a hard disk, USB flash drive, or SD
card, it must be partitioned and formatted with a filesystem. Every filesystem must
have its own disk partition. A partition can cover an entire disk, or a disk can be divi‐
ded into multiple partitions. Each partition is like an independent disk, and each par‐
tition can have a different filesystem.

A filesystem must be mounted, or attached, to the running filesystem before it is
accessible. A filesystem needs a _mountpoint_, which is a directory created for that file‐
system. This directory can be anywhere, though the traditional locations are _/mnt_
and _/media_ .

You may mount only one filesystem per mountpoint. If you mount a second filesys‐
tem, it overwrites the first filesystem.

A filesystem can be set up to mount automatically at system startup, dynamically
when you attach removable media, manually from the command line, or by clicking a
button on your desktop or in your file manager. Most Linux distributions take good
care of handling removable media. Plug in your USB device or optical disk, and
Linux takes care of setting up the mountpoint and automounting it, or setting it up
for you to mount it with the click of a button (Figure 11-1).

_Figure 11-1. Removable media buttons on Xfce desktop_

Ext4, XFS, Btrfs, and exFAT are _64-bit_ filesystems. This means they support a 64-bit
block addressing space, which enables much larger file and filesystem sizes than 32and 16-bit filesystems. 64-bit computing has been around at least since the 1970s on

**244** **|** **Chapter 11: Creating and Managing Filesystems**

supercomputers, then later on high-end business machines like IBM Power and Sun
Microsystems UltraSPARC.

My first Windows 3.1/DOS PC, back in the mid-1990s, was a 16-bit system. Windows
95 boasted of being the first 32-bit consumer operating system. The first 64-bit file‐
systems for x86 PCs started appearing in Linux around 2001. See [Ext4 High Level](https://oreil.ly/kufyJ)
[Design in the Linux kernel documentation to see nice tables that lay this all out for us,](https://oreil.ly/kufyJ)
comparing 32- and 64-bit filesystems.

64-bit filesystems are backward compatible with 32-bit applications. After all these
years it is unlikely you will run into 32-bit apps, though if you do they will run on
your modern Linux, provided that it supplies the necessary packages to set up a 32bit environment.

Ext4 and XFS are _journaling_ filesystems, and Btrfs is a _copy-on-write_ (CoW) filesys‐
tem. Journaling and CoW keep your filesystems in consistent states even after a
power failure or system crash. Filesystems are complex and busy, and an interruption
affects more than just the files you are working on. Interruptions result in large num‐
bers of files with incompleted tasks, and in the olden days this meant possibly losing
your whole filesystem.

_Ext4_ is the most widely used filesystem on Linux and is the default on the majority of
Linux distributions. It’s not exciting. It’s well tested, well supported, and does its job
without drama. The Ext4 journal records changes until they are written to disk, pro‐
viding protection from data loss in the event of an interruption. Ext4 filesystems can
be resized, both larger and smaller.

_XFS_ was originally a high-performance Unix 64-bit filesystem, ported to Linux in
2001. XFS is a fast, efficient, reliable journaling filesystem suitable for systems from
small personal machines and to multidisk datacenter setups. XFS can be resized
larger, but not smaller.

_Btrfs_ is an advanced copy-on-write (CoW) filesystem that includes a batch of features
not present in the other filesystems in this chapter, including snapshots; RAID 0, 1,
and 10; and subvolumes. Subvolumes are wonderfully flexible, as they enable creating
multiple filesystem roots on a single partition. CoW is a cool way of creating snap‐
shots in a space-efficient way, where each snapshot contains only the changes from
the previous snapshot. When you run into problems, you can roll back to an older
known good snapshot. Btrfs resizes smaller and larger.

_FAT16/32_ are the elderly Microsoft 16- and 32-bit filesystems. FAT32 is the most uni‐
versal filesystem, supported by Microsoft Windows, Apple’s macOS, Linux, Unix, and
DOS operating systems. Use FAT32 for easiest file sharing on portable media. It has
one limitation that is a showstopper for some uses, and that is a maximum file size of
4 GB (on media with 4K blocks).

**Filesystem Overview** **|** **245**

_exFAT_ is the newest Microsoft 64-bit filesystem, a nice upgrade from FAT32. exFAT is
a fast, lightweight filesystem for USB sticks and SD media, and supports much larger
file and volume sizes than FAT32. Wikipedia cites a 16 EiB maximum file size and
128 PiB maximum volume size. It does not have a journal or CoW.

exFAT is troublesome for Linux users because it is a patented proprietary filesystem,
which was not available to Linux as a native filesystem until 2020. You need to worry
about Linux compatibility only if you want to read and copy USB flash drives or
SDXC cards formatted with exFAT to your Linux computer. For example, you want to
use exFAT-formatted SDXC cards with your digital camera, or audio recording
device.

To use exFAT with Linux you have two options. One is to use the _exfatprogs_, or _exfat-_
_fuse_ and _exfat-utils_ packages, which are available on most distributions. exFAT FUSE
was developed and is maintained outside of the US, making it immune to US patent
laws. exFAT FUSE takes advantage of Filesystem in Userspace (FUSE), which enables
unprivileged users to run filesystems in userspace. It is not as efficient as a filesystem
properly integrated into the kernel, but it works, and you can read and write exFAT
files. Some hardy souls try to use exFAT FUSE in shared partitions to share files with
Windows and macOS. In theory this should work, though there are sometimes
glitches related to how well a particular Windows or macOS release implements
exFAT.

The other option is to wait a little while for native support. Microsoft released exFAT
in 2006 and licensed it primarily to companies that make embedded systems and
embedded media. But times change. Microsoft has become an open source contribu‐
tor, and a member of the [Open Invention Network (OIN). Microsoft released the](https://oreil.ly/AJepb)
exFAT specification in 2019. Releasing the specification sidestepped licensing hassles
with the existing exFAT code, and Linux kernel developers wasted no time writing
new code. Native support for exFAT with this shiny new code is in Linux kernel 5.7.
This should find its way into your favorite distro soon; run _uname -r_ to see your ker‐
nel version.

**11.1 Listing Supported Filesystems**

**Problem**

You need to know what filesystems are installed on your Linux system.

**Solution**

Read _/proc/filesystems_ to see a list of installed filesystems:

```
  $ cat /proc/filesystems
  nodev  sysfs

```

**246** **|** **Chapter 11: Creating and Managing Filesystems**

```
  nodev  tmpfs
  nodev  bdev
  nodev  proc
  nodev  cgroup
  nodev  cgroup2
  nodev  cpuset
  nodev  devtmpfs
  nodev  debugfs
  nodev  tracefs
  nodev  securityfs
  nodev  sockfs
  nodev  bpf
  nodev  pipefs
  nodev  ramfs
  nodev  hugetlbfs
  nodev  devpts
  ext3
  ext2
  ext4
  nodev  autofs
  nodev  mqueue
  nodev  pstore
  btrfs
  vfat
  xfs
  fuseblk
  nodev  fuse
  nodev  fusectl
  jfs
  nilfs2
```

**Discussion**

See all those _nodev_ entries? Those are all virtual filesystems that exist only in memory
and are not attached to a physical device like _/dev/sda1_ . Systemd manages all of these
virtual filesystems.

The other filesystems, Ext4, XFS, and so on, are the filesystems we use on our storage
devices to store, organize, and protect our data.

**See Also**

 - [“sysfs, the filesystem for exporting kernel objects” is written for developers, but it](https://oreil.ly/QCMN7)
has useful information for Linux users and admins.

**11.1 Listing Supported Filesystems** **|** **247**

**11.2 Identifying Your Existing Filesystems**

**Problem**

You do not know what filesystems are already on your system, or on a removable
storage disk, and you need to know how to list them.

**Solution**

Use the _lsblk_ command. You can list just the device names and filesystems with the
_NAME_ and _FSTYPE_ options:

```
  $ lsblk -o NAME,FSTYPE
  NAME  FSTYPE
  sda
  ├─sda1 vfat
  ├─sda2 btrfs
  ├─sda3 xfs
  └─sda4 swap
  sdb
  ├─sdb1 ext2
  ├─sdb2 ext4
  ├─sdb3 swap
  └─sdb4 LVM2_member
  sdc
  └─sdc1 vfat
  sr0
```

Query a single disk:

```
  $ lsblk -o NAME,FSTYPE /dev/sdb
  ├─sdb1 ext2
  ├─sdb2 ext4
  ├─sdb3 swap
  └─sdb4 LVM2_member
```

Or a single partition:

```
  $ lsblk -o NAME,FSTYPE /dev/sda1
  NAME FSTYPE
  sda1 vfat
```

This is my favorite _lsblk_ incantation. It shows all device names, filesystem types, file‐
system sizes, percentage used, labels, and mountpoints:

```
  $ lsblk -o NAME,FSTYPE,LABEL,FSSIZE,FSUSE%,MOUNTPOINT
  NAME  FSTYPE  LABEL   FSSIZE FSUSE% MOUNTPOINT
  loop0 squashfs      646.5M  100% /run/archiso/sfs/airootfs
  sda
  ├─sda1
  └─sda2 ntfs
  sdb

```

**248** **|** **Chapter 11: Creating and Managing Filesystems**

```
  ├─sdb1 vfat   BOOT
  ├─sdb2 btrfs  root
  ├─sdb3 xfs   home
  └─sdb4 swap
  sdc  iso9660 RESCUE800
  └─sdc1 iso9660 RESCUE800  708M  100% /run/archiso/bootmnt
  sr0
```

**Discussion**

Run _lsblk --help_ to see a list of columns. There is quite a bit of useful information,
such as PATH, LABEL, UUID, HOTPLUG, MODEL, SERIAL, and SIZE.

On some distros you may need root permissions to see the filesystem types, UUIDs,
and labels.

_lsblk_ always prints _vfat_ for both FAT16 and FAT32 filesystems. Use GParted or _parted_
to see whether a filesystem is FAT16 or FAT32.

_vfat_ is Virtual FAT, the kernel’s filesystem driver for FAT16 and FAT32.

**See Also**

 - [Linux Kernel SCSI Interfaces Guide](https://oreil.ly/beFOx)

 - [Major and minor numbers for block and character devices](https://oreil.ly/NW2S7)

 - _man 8 lsblk_

 - _man 8 parted_

 - Chapter 8

 - Chapter 9

**11.3 Resizing Filesystems**

**Problem**

You want to enlarge or reduce the size of your filesystem.

**Solution**

Every filesystem has its own commands for resizing. See Recipes 8.8, 8.9, and 9.7 to
learn about resizing filesystems.

**11.3 Resizing Filesystems** **|** **249**

**Discussion**

The filesystem’s partition must also be resized to match. GParted does this in a single
operation (see Recipe 9.7).

Recipes 8.8 and 8.9 use _parted_ and filesystem utilities to resize a filesystem and its
partition in two steps.

**See Also**

 - Recipe 8.8

 - Recipe 8.9

 - Recipe 9.7

 - _man 8 resize2fs_

 - _man 8 parted_

 - _man 8 xfs_growfs_

 - _man 8 btrfs_

 - _man 8 fsck.vfat_

**11.4 Deleting Filesystems**

**Problem**

You need to delete a filesystem and its underlying partition.

**Solution**

To delete the filesystem and its partition, use _parted_ . In this example, _/dev/sdb1_ is
deleted. Verify which partition and filesystem you are going to delete, then make sure
the filesystem is unmounted. In the example, the mountpoint is _/media/duchess/stuff_ :

```
  $ lsblk -f
  sda
  ├─sdb1 ext4  /media/duchess/stuff
  [...]
  $ umount /media/duchess/stuff
```

Then use _parted_ to delete the partition:

```
  $ sudo parted /dev/sdb
  GNU Parted 3.2
  Using /dev/sdb
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) print

```

**250** **|** **Chapter 11: Creating and Managing Filesystems**

```
  Model: ATA SAMSUNG HD204UI (scsi)
  Disk /dev/sdb: 2000GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system Name Flags
  1   1049kB 1656GB 1656GB ext4     stor-1
  1   1656GB 2656GB 1000GB ext4     stor-2
  (parted) rm 1
```

If you prefer a graphical tool, use GParted (Chapter 9).

**Discussion**

Yes, the command is _umount_, not _unmount_ . _umount_ dates from the ancient Unix era,
when identifiers had a limit of six characters.

Deleting all the files in a partition does not delete the filesystem. The filesystem struc‐
ture remains in place.

**See Also**

 - _man 1 dd_

**11.5 Using a New Filesystem**

**Problem**

You just created a nice new filesystem, and you need to mount it.

**Solution**

After creating your new filesystem, you must create a mountpoint, and optionally
configure automatic mounting. As discussed in the introduction to this chapter, a
new filesystem must be mounted, or attached, to the running filesystem to be usable.

Ext4, XFS, and Btrfs all have access controls. If you want the files on these filesystems
available to anyone other than the root user, you must adjust ownership and permis‐
sions. FAT16/32 and exFAT do not have access controls and are wide open to anyone.

Start by mounting your new filesystem. Create a mountpoint, which is a directory,
and then mount the filesystem, like this example for Mad Max:

```
  $ sudo mkdir -p /mnt/madmax/newfs
  $ sudo mount /dev/sdb1 /mnt/madmax/newfs

```

**11.5 Using a New Filesystem** **|** **251**

The following example sets the ownership of the new filesystem to Mad Max, readwrite-execute, with read-only permissions for group and world:

```
  $ sudo chown -R madmax:madmax /mnt/madmax/newfs
  $ sudo chmod -R 0755 /mnt/madmax/newfs
```

Now Mad Max can access the new filesystem. This mount only lasts until the next
system restart; see Recipe 11.6 to learn how to configure automatic filesystem
mounts.

**Only One Filesystem per Mountpoint**

Every filesystem needs its own unique mountpoint; you cannot put
multiple filesystems on a single mountpoint.

**Discussion**

See Chapter 6 for detailed recipes on managing ownership and permissions.

The traditional directories that contain mountpoints are _/mnt_ and _/media_ . _/mnt_ is tra‐
ditionally for static mounts (configured in _/etc/fstab_ ), and _/media_ is for automounting
removable media. You may create your mountpoints wherever you want. The advan‐
tage of using the traditional directories is having your mountpoints in a limited num‐
ber of predictable locations.

A shared directory with mountpoints for multiple users could look like this, with a
directory for each user:

```
  $ tree /shared
  /shared
  ├── duchess
  ├── madmax
  └── stash
```

Then every filesystem needs its own mountpoint in the user subdirectories. For
example, Mad Max has two filesystems mounted at _madmax1_ and _madmax2_ :

```
  $ tree -L 2 /mnt
  /mnt
  ├── duchess
  ├── madmax
  │  ├── madmax1
  │  └── madmax2
  └── stash
```

The mountpoints can have any names you want. For example, Mad Max’s mount‐
points could be _fs1_ and _fs2_, or _fred_ and _ethel_, or _max1_ and _max2_, whatever helps you
remember what they are.

**252** **|** **Chapter 11: Creating and Managing Filesystems**

Use the _stat_ command to see the permissions on a filesystem, like this example for
Mad Max’s new filesystem:

```
  $ stat /shared/madmax/madmax1
  [...]
  Access: (0755/drwxr-xr-x) Uid: ( 0/ madmax) Gid: ( 0/ madmax)
```

List all filesystem mounts with _mount_ :

```
  $ mount
  sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
  proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
  udev on /dev type devtmpfs
  [...]
```

Use the _mountpoint_ command to learn if a directory is a mountpoint:

```
  $ mountpoint madmax1/
  madmax1/ is a mountpoint
```

**See Also**

 - _man 1 chown_

 - _man 1 chmod_

 - _man 1 stat_

**11.6 Creating Automatic Filesystem Mounts**

**Problem**

You have added a new filesystem, and you want it to automatically mount at system
startup.

**Solution**

This is what your _/etc/fstab_ file is for. The following example is added to the exist‐
ing _/etc/fstab_ file to create a static mount for the filesystem in Recipe 11.5, and it will
be automatically mounted at startup:

```
  #<file system>  <mount point>    <type>  <options>    <dump> <pass>
  LABEL=xfs-ehd   /mnt/madmax/newfs  xfs   defaults,user  0    2
```

Use the _findmnt_ command to test your new configuration:

```
  $ sudo findmnt --verbose --verify
  /
  [ ] target exists
  [ ] UUID=102a6fce-8985-4896-a5f9-e5980cb21fdb translated to /dev/sda2
  [ ] source /dev/sda2 exists

```

**11.6 Creating Automatic Filesystem Mounts** **|** **253**

```
  [ ] FS type is btrfs
  [W] recommended root FS passno is 1 (current is 0)
  /mnt/madmax/newfs
  [ ] target exists
  [ ] LABEL=xfs-ehd translated to /dev/sdb1
  [ ] source /dev/sdb1 exists
  [ ] FS type is xfs
  [...]
  0 parse errors, 0 errors, 1 warning
```

The warning “recommended root FS passno is 1 (current is 0)” is not significant. If
that is the only warning, and there are no errors, reboot to test, or run the following
command to mount your new _/etc/fstab_ entry:

```
  $ sudo mount -a
```

**Discussion**

This is what the six _fstab_ columns are for:

_device_

The UUID or filesystem LABEL. Don’t use _/dev_ names because they are not
unique, and sometimes they change. Run _lsblk -o UUID,LABEL_ to list UUIDs
and filesystem labels to use in the _device:_ column.

_mountpoint_

The directory you created for the filesystem.

_type_

The filesystem type, for example, _xfs_, _ext4_, or _btrfs_ . You may use _auto_ for the file‐
system type, and the kernel will automatically detect the filesystem type.

_options_

Your mount options in a comma-delimited list (see below for a list).

_dump_

If you’re using the _dump_ command for backups, this tells _dump_ the backup inter‐
val, in days. So, 1 means every day, 2 means every other day, 3 is every third day,
and so on. Most likely you are not using _dump_ and should enter 0.

_pass_

This tells the filesystem checker which filesystem to check first at bootup, if it
ever needs to. Make your root filesystem 1, any other Linux filesystems 2, and
non-Linux filesystems 0.

The following _options_ define permissions:

_defaults_

The default options are _rw_, _suid_, _dev_, _exec_, _auto_, _nouser_, and _async_ . The _defaults_
values are overridden by appending additional options, for example _defaults,user_

**254** **|** **Chapter 11: Creating and Managing Filesystems**

gives the user permission to mount and unmount the filesystem. You may
append as many options as you like, or omit _defaults_ and list only the options you
want.

_rw_

Read/write.

_ro_

Read-only.

_suid_

Allow setuid and setgid bits to operate.

_dev_

Interpret block and character devices.

_exec_

Allow binaries to run.

_auto_

Indicates which filesystems should start at boot.

_nouser_

Nonroot users cannot mount or unmount the filesystem.

_async_

Asynchronous I/O, which is standard for Linux.

_user_

Nonroot users can mount and unmount the device, if they mounted it.

_users_

Any user can mount and unmount the device.

_noauto_

Do not automatically mount at boot.

_ro_

Mount the filesystem read-only.

_noatime_

Do not update the “time accessed” file attribute. _noatime_ was used in times past
to speed up performance. If you are on a modern computer, it probably won’t
make much difference.

_gid_

Limit access to a group (from _/etc/group_ ); for example, _gid=group1_ .

**11.6 Creating Automatic Filesystem Mounts** **|** **255**

**See Also**

 - _man 8 mount_

 - _man 5 fstab_

 - [systemd](https://systemd.io)

**11.7 Creating Ext4 Filesystems**

**Problem**

You want to create a new Ext4 filesystem on an internal or external storage disk.

**Solution**

Start with a partition of the size you want for your filesystem. Then use the _mkfs.ext4_
command to create the new Ext4 filesystem.

The following example overwrites an existing XFS filesystem with a new Ext4 filesys‐
tem. When you overwrite an existing filesystem, it must first be unmounted. In this
example, the filesystem on _/dev/sdb1_ is mounted at _/media/duchess/stuff_, which you
can see with the _df_ command:

```
  $ df -Th /media/duchess/stuff/
  Filesystem   Type Size Used Avail Use% Mounted on
  /dev/sdb1   xfs  952M 7.9M 944M  1% /media/duchess/stuff
```

You may need root permissions to unmount:

```
  $ sudo umount /media/duchess/stuff
```

Create the new Ext4 filesystem:

```
  $ sudo mkfs.ext4 -L 'mylabel' /dev/sdb1
  mke2fs 1.44.1 (24-Mar-2018)
  /dev/sdb1 contains a XFS file system labelled 'stuff'
  created on Sun Sep 20 19:37:43 2020
  Proceed anyway? (y,N) y
  Creating filesystem with 466432 4k blocks and 116640 inodes
  Filesystem UUID: 99da2e5d-f96a-4fb6-990d-599cf56247a2
  Superblock backups stored on blocks:
  32768, 98304, 163840, 229376, 294912

  Allocating group tables: done
  Writing inode tables: done
  Creating journal (8192 blocks): done
  Writing superblocks and filesystem accounting information: done

```

**256** **|** **Chapter 11: Creating and Managing Filesystems**

You could also create a new partition and put your new filesystem on it; see the exam‐
ples for creating new partitions in Recipes 8.4 and 9.4.

**Discussion**

Overwriting a filesystem destroys all the data on it.

The _-L_ option is for creating a volume label. This can be anything you want, up to 16
characters (FAT32 is limited to 11 characters). It is not required, though filesystem
labels are useful, and for some operations, such as in _/etc/fstab_, can be used in place of
the long UUID.

The _-n_ option does a dry run, so you see what will happen without actually creating
the new filesystem.

_mke2fs_ has numerous options, but you will likely use just a few of them: device name,
volume label, dry-run, and creating an external journal. Its defaults are set in _/etc/_
_mke2fs.conf_, and I suggest not changing them without thorough study of the available
settings.

**See Also**

 - _man 8 mke2fs_

 - Recipe 8.4

 - Recipe 11.5

**11.8 Configuring the Ext4 Journal Mode**

**Problem**

You know that the default journal mode for ext4 is _data=ordered_, which does not
journal data, but only metadata. It is a good balance of safety and speed, but you want
to set it to _data=journal_, which is the safest.

**Solution**

Use the _tune2fs_ command. First check your existing journal mode with _dmesg_ . The
filesystem must be mounted:

```
  $ dmesg | grep sdb1
  [25023.525279] EXT4-fs (sdb1): mounted filesystem with ordered data mode.

```

**11.8 Configuring the Ext4 Journal Mode** **|** **257**

That confirms _/dev/sdb1_ is formatted as Ext4 and has the default _data=ordered_ jour‐
nal mode. Now change it to _data=journal_ mode:

```
  $ sudo tune2fs -o journal_data /dev/sdb1
  tune2fs 1.44.1 (24-Mar-2018)
```

Unmount and remount, and check again with _dmesg_ :

```
  $ dmesg | grep sdb1
  [25023.525279] EXT4-fs (sdb1): mounted filesystem with ordered data mode.
```

If you see multiple lines with conflicting information, like this:

```
  [ 206.076123] EXT4-fs (sdb1): mounted filesystem with journalled data mode.
  [ 206.076433] EXT4-fs (sdb1): mounted filesystem with ordered data mode.
```

Reboot, and then you should see only the “mounted filesystem with journalled data
mode” line.

**Discussion**

The journal mode command options are named differently, depending on what doc‐
umentation you are reading. In _man 8 tune2fs_, the following options are listed:

 - journal_data

 - journal_data_ordered

 - journal_data_writeback

In the kernel documentation, and a whole lot of how-tos, these are the options:

 - data=journal

 - data=ordered

 - data=writeback

The _data=_ options are meant to be passed to the kernel at boot either in your boot‐
loader configuration, or in _/etc/fstab_ . I favor using _tune2fs_ because it is fast and easy,
and works on all Ext4 filesystems regardless of their mount configurations.

These are the journal modes in order of data safety:

_data=journal_

Provides the most protection for your data. All data and metadata are first writ‐
ten to the journal, and then written to the filesystem. In the event of a failure, this
gives you the best chance of recovering your data. This is also the most resource
intensive, as your changes are written twice.

**258** **|** **Chapter 11: Creating and Managing Filesystems**

_data=ordered_

This does not write your data to the journal. Data is first written to the filesystem,
and then metadata is written to the journal. The metadata is logically grouped in
order and held in a single transaction. When the metadata is written to disk, its
associated data blocks are written first.

_data=writeback_

This is the fastest and the least safe. Data is first written to the filesystem, and
then metadata is written to the journal. Data ordering is not preserved. I don’t
think the small performance gain is worth the extra risk.

**See Also**

 - _man 8 tune2fs_

 - [Kernel documentation for the Ext4 filesystem](https://oreil.ly/Y4ajq)

**11.9 Finding Which Journal Your Ext4 Filesystem Is**
**Attached To**

**Problem**

You have several Ext4 filesystems, some with internal journals and some with external
journals, and you want to know which journals they are using.

**Solution**

Meet a new command, _dumpe2fs_ . This is a part of the _e2fsprogs_ suite of ext2/3/4 utilit‐
ies. Query your Ext4 filesystem:

```
  $ sudo dumpe2fs -h /dev/sda1 | grep -i uuid
  dumpe2fs 1.43.8 (1-Jan-2018)
  Filesystem UUID:     8593f3b7-4b7b-4da7-bf4a-cc6b0551cff8
  Journal UUID:       f8e42703-94eb-49af-a94c-966e5b40e756
```

The _Journal UUID_ belongs to the journal. Run _lsblk_ to verify details:

```
  $ lsblk -f | grep f8e42703-94eb-49af-a94c-966e5b40e756
  └─sdb5 ext4  journal1 f8e42703-94eb-49af-a94c-966e5b40e756
```

And there it is. An Ext4 filesystem using an internal journal looks like this, without
the Journal UUID line:

```
  $ sudo dumpe2fs -h /dev/sda2 | grep UUID
  dumpe2fs 1.44.1 (24-Mar-2018)
  Filesystem UUID:     64bfb5a8-0ef6-418a-bb44-6c389514ecfc

```

**11.9 Finding Which Journal Your Ext4 Filesystem Is Attached To** **|** **259**

**Discussion**

There is always a way to find out where things are in Linux. The _dumpe2fs_ command
shows a lot of useful information about your Ext4 filesystems, including UUIDs, file‐
system creation time, block count, free blocks, journal size, and much more.

**See Also**

 - _man 8 dumpe2fs_

**11.10 Improving Performance with an External Journal**
**for Ext4**

**Problem**

You have heard that placing the Ext4 journal on a different disk than the filesystem
improves performance, and you want to do this.

**Solution**

An external journal improves performance when your journal mode is _data=journal_ .
(See the Discussion for more information on journal modes.) You may create a new
Ext4 filesystem and external journal, or convert an existing filesystem to use an exter‐
nal journal.

The two disks must be on the same machine and have similar read and write speeds.
If the journal disk is slower than the filesystem disk, you will not see much, if any, of a
performance gain. You could use two similar solid-state disks (SSDs), two similar
hard disk drives (HDDs), or use a small SSD for the journal and a large HDD for the
filesystem, because SSDs are much faster than HDDs.

Locating the Ext4 journal on a separate disk takes several steps. In the following
example, we will create two new partitions, one for the journal and one for the new
Ext4 filesystem. Then create the journal, then the filesystem, and attach it to the
journal.

The first partition is for the journal on _/dev/sdb5_, 200 GB in size, and the second par‐
tition is for the Ext4 filesystem on _/dev/sda1_, 500 GB:

```
  $ sudo parted
  (parted) select /dev/sdb
  Using /dev/sdb
  (parted) mkpart "journal1" ext4 1600GB 1800GB
  (parted) select /dev/sda

```

**260** **|** **Chapter 11: Creating and Managing Filesystems**

```
  Using /dev/sda
  (parted) mkpart "ext4fs" ext4 1MB 500GB
```

The external journal and the filesystem must have the same block size, which is speci‐
fied in the following example with _-b 4096_ . If you don’t know the block size, find
it with _tune2fs_ . The following commands are run in the Bash shell, and not in the
_parted_ shell:

```
  $ sudo tune2fs -l /dev/sda1 | grep -i 'block size'
  Block size:        4096
```

Now create the journal, which can take a few minutes, and then the new filesystem:

```
  $ sudo mke2fs -b 4096 -O journal_dev /dev/sdb5
  mke2fs 1.43.8 (1-Jan-2018)
  /dev/sdb2 contains a ext4 file system labelled 'ext4'
  created on Mon Jan 4 18:25:30 2021
  Proceed anyway? (y,N) y
  Creating filesystem with 48747520 4k blocks and 0 inodes
  Filesystem UUID: f8e42703-94eb-49af-a94c-966e5b40e756
  Superblock backups stored on blocks:
  Zeroing journal device:

  $ sudo mkfs.ext4 -b 4096 -J device=/dev/sdb5 /dev/sda1
  mke2fs 1.43.8 (1-Jan-2018)
  Creating filesystem with 35253504 4k blocks and 8814592 inodes
  Filesystem UUID: 8593f3b7-4b7b-4da7-bf4a-cc6b0551cff8
  Superblock backups stored on blocks:
  32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
  4096000, 7962624, 11239424, 20480000, 23887872

  Allocating group tables: done
  Writing inode tables: done
  Adding journal to device /dev/sdb2: done
  Writing superblocks and filesystem accounting information: done
```

You’re finished and can use your new filesystem.

You can attach an external journal to an existing filesystem with the _tune2fs_ com‐
mand. First clear the journal on the existing filesystem, then link the filesystem to the
external journal:

```
  $ sudo tune2fs -O ^has_journal /dev/sda1
  $ sudo tune2fs -b 4096 -J device=/dev/sdb5 /dev/sda1
```

**Discussion**

The Ext4 journal provides extra protection for your data, in the event of a disk or sys‐
tem failure, by tracking changes that are not yet written to disk. Even if it loses your
most recent changes, it protects the filesystem from being corrupted, so you lose just
a little bit instead of the whole works.

**11.10 Improving Performance with an External Journal for Ext4** **|** **261**

Moving the journal to a separate disk on the same machine provides a noticeable per‐
formance boost when the journal mode is _data=journal_ . Ext4 has three journaling
modes: _journal_, _ordered_, and _writeback_ . The default is _ordered_ . See Recipe 11.8 to
learn about these modes and how to select the one you want to use.

The caret, _^_, disables a feature. In the example in the recipe, it clears the existing
internal journal.

Ext4 journals cannot be shared, and can be used by only one filesystem.

**See Also**

 - _man 8 mke2fs_

 - _man 8 tune2fs_

 - Chapter 8

 - Chapter 9

**11.11 Freeing Space from Reserved Blocks on Ext4**
**Filesystems**

**Problem**

Most Linux distributions reserve 5% of Ext4 filesystems for the root user and system
services. On large modern hard disks that is a lot of space, and you want to free some
of that space.

**Solution**

Use the _tune2fs_ command to adjust the size of the free space on an Ext4 filesystem.
You may configure it by percentage, like this example that reduces it to 1%:

```
  $ sudo tune2fs -m 1 /dev/sda1
  tune2fs 1.44.1 (24-Mar-2018)
  Setting reserved blocks percentage to 1% (820474 blocks)
```

That is still about 3 gigabytes, with 4K blocks (820,474 x 4,096 = 3,360,661,504 bytes).
Find your block size:

```
  $ sudo tune2fs -l /dev/sda1 | grep -i 'block size'
  Block size:        4096
```

You can set a fractional percentage:

```
  $ sudo tune2fs -m .25 /dev/sda1
  tune2fs 1.44.1 (24-Mar-2018)
  Setting reserved blocks percentage to 0.25% (205118 blocks)

```

**262** **|** **Chapter 11: Creating and Managing Filesystems**

That is roughly 800 MB. Or, specify a number of blocks:

```
  $ sudo tune2fs -r 250000 /dev/sda1
  tune2fs 1.44.1 (24-Mar-2018)
  Setting reserved blocks count to 250000
```

250,000 4K blocks is about a gigabyte. Check your work:

```
  $ sudo tune2fs -l /dev/sda1 | grep -i 'reserved block'
  Reserved block count:   250000
```

**Discussion**

If you run out of disk space, you can still log in as root and free up space, which you
could not do if that 5% was not held in reserve. However, that 5% is a holdover from
the days of megabyte hard disks. Hard disks are so large now, you don’t need all that
reserved space. For example, 5% of a 1 TB disk is about 50 GB. Only a few hundred
megabytes of reserved space is necessary. I set mine to a gigabyte. It’s easy to remem‐
ber and provides more than enough room.

Use the _dumpe2fs_ command to check out the reserved blocks settings in your Ext4
filesystem:

```
  $ sudo dumpe2fs -h /dev/sda1
  [...]
  Block count:       82047488
  Reserved block count:   250000
  [...]
```

**See Also**

 - _man 8 dumpe2fs_

 - _man 8 tune2fs_

**11.12 Creating a New XFS Filesystem**

**Problem**

You like XFS, and want to create a new XFS filesystem.

**Solution**

You need the _xfsprogs_ package installed on your system and a partition for the new
filesystem. Then create your new XFS filesystem with _mkfs.xfs_ . The following exam‐
ple, on Ubuntu, demonstrates all these steps. The example new partition is _/dev/sda1_,
and the new filesystem gets an _xfstest_ label:

**11.12 Creating a New XFS Filesystem** **|** **263**

```
  $ sudo apt install xfsprogs
  $ sudo parted /dev/sda mkpart testxfs xfs 1MB 500GB
  $ sudo mkfs.xfs -L xfstest /dev/sda1
  meta-data=/dev/sdb5       isize=512  agcount=4, agsize=640000 blks
  =            sectsz=512  attr=2, projid32bit=1
  =            crc=1    finobt=1, sparse=0, rmapbt=0,
  reflink=0
  data   =            bsize=4096  blocks=2560000, imaxpct=25
  =            sunit=0   swidth=0 blks
  naming  =version 2       bsize=4096  ascii-ci=0 ftype=1
  log   =internal log      bsize=4096  blocks=2560, version=2
  =            sectsz=512  sunit=0 blks, lazy-count=1
  realtime =none          extsz=4096  blocks=0, rtextents=0
```

Check your work with _lsblk_ :

```
  $ lsblk -f | grep -w sda1
  ├─sda1 xfs  xfstest bb5dddb3-af74-4bed-9d2a-e79589278e84
```

Mount your new filesystem, adjust ownership and permissions, and it’s ready to use.
The following example mounts it on _/mnt/xfstest_, sets ownership to Duchess, readwrite for Duchess and read only for everyone else:

```
  $ sudo mkdir /mnt/xfstest
  $ sudo mount /dev/sda1 /mnt/xfstest
  $ sudo chown -R duchess:duchess /mnt/xfstest
  $ sudo chmod -R -755 /mnt/xfstest
```

**Discussion**

The command output from creating a new XFS filesystem contains a few helpful
items, like the block size, number of blocks, and sector size.

**See Also**

 - _man 8 mkfs.xfs_

**11.13 Resizing an XFS Filesystem**

**Problem**

You want to resize an XFS filesystem.

**Solution**

You can only increase the size of an XFS filesystem. If you need it to be smaller, you
must copy your data to a safe location, create a smaller partition, format it as XFS,
then restore your data.

**264** **|** **Chapter 11: Creating and Managing Filesystems**

Increasing the size is less work. You need free space at the end of the partition that
your XFS filesystem is on. In the following examples, the new endpoint for the parti‐
tion is 2700 GB, and the filesystem is mounted at _/media/duchess/xfs_ .

Launch _parted_ . Print the partition information to verify the correct partition and
endpoint, increase the partition size, then quit _parted_ :

```
  $ sudo parted /dev/sdb
  GNU Parted 3.3
  Using /dev/sdb
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) p free
  Model: ATA SAMSUNG HD204UI (scsi)
  Disk /dev/sdb: 4000GB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system Name  Flags
  17.4kB 1049kB 1031kB Free Space
  1   1049kB 1656GB 1656GB xfs     files
  2   1656GB 1759GB 103GB  xfs     files2
  1759GB 4000GB 242GB  Free Space

  (parted) resizepart 2
  (parted) Warning: Partition /dev/sdb2 is being used. Are you sure you want to
  continue?
  Yes/No? Yes
  End? [1759GB]? 1900GB
  (parted) q
```

Now, expand the filesystem to match the new partition size:

```
  $ sudo xfs_growfs /media/duchess/xfs
```

You’re done! Enjoy your new larger filesystem.

**Discussion**

You also have the option to unmount the filesystem and resize it offline. This is a little
safer.

Using GParted to resize a filesystem is fast and easy; see Recipe 9.7.

**See Also**

 - Recipe 8.8

 - Recipe 9.7

**11.13 Resizing an XFS Filesystem** **|** **265**

**11.14 Creating an exFAT Filesystem**

**Problem**

Your digital camera flash drive is formatted with the exFAT filesystem, or you have
other flash storage devices that use exFAT, and you want to read, write, and edit the
files from these devices on your Linux system.

**Solution**

There are two possible solutions: one is to use the exFAT implementation that runs
on Filesystem in Userspace (FUSE). The other solution is to use the native implemen‐
tation that runs in the Linux kernel, rather than userspace. In this recipe we will use
exFAT FUSE because at the time this was written the native implementation had not
yet made it into most distribution releases. Look for kernel version 5.7, and check
your distribution release notes and news. (Run the _uname -r_ command to see your
kernel version.)

The exFAT package names vary. _exfat-fuse_ and _exfat-utils_ are the older packages.
_exfatprogs_ is the newest implementation, replacing both _exfat-fuse_ and _exfat-utils_ .
Whatever you have, go ahead and install it.

The command to create a new exFAT filesystem is the same for both. The following
example formats _/dev/sdc1_ as exFAT:

```
  $ sudo mkfs.exfat /dev/sdc1
  mkexfatfs 1.2.8
  Creating... done.
  Flushing... done.
  File system created successfully.
```

exFAT is designed to be simple, so there are not a lot of options. You can give it a
label:

```
  $ sudo exfatlabel /dev/sdc2 exfatfs
```

Verify your changes with _lsblk_ :

```
  $ lsblk -f
  NAME  FSTYPE LABEL  UUID
  sdc
  ├─sdc1
  ├─sdc2 exfat exfatfs 8178-51D4
  └─sdc3

```

**266** **|** **Chapter 11: Creating and Managing Filesystems**

**Discussion**

You do not need a special exFAT partition to read exFAT files on other devices, but
only exFAT installed on your Linux system.

If you prefer a graphical partitioning tool, GParted does not support exFAT, due to
legal concerns. GNOME Disks, called Disks in most GNOME implementations, does
support exFAT. You do not have to install GNOME to get Disks; look for the _gnome-_
_disk-utility_ package.

Microsoft released the exFAT specification in 2019. Samsung wrote _exfatprogs_ and
released it in early 2020. By the time you read this, the latest releases of Fedora,
Ubuntu, and openSUSE Tumbleweed should have native exFAT support.

**See Also**

 - _man 8 exfat_

 - _man 8 exfatlabel_

**11.15 Creating FAT16 and FAT32 Filesystems**

**Problem**

You need to know how to create FAT16 and FAT32 filesystems.

**Solution**

You need the _dosfstools_ package, which is installed by default on most Linuxes. The
following examples demonstrate creating a new 500 MB partition with _parted_, then
formatting the partition with FAT32.

Create the new partition, and note how to change the measurement units to MB, and
how to use _mkpart_ interactively:

```
  $ sudo parted /dev/sdb
  GNU Parted 3.2
  Using /dev/sdb
  Welcome to GNU Parted! Type 'help' to view a list of commands.
  (parted) print
  Model: ATA SAMSUNG HD204UI (scsi)
  Disk /dev/sdb: 2000399MB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start  End   Size  File system Name  Flags
  1    0.00GB  1656GB 1656GB xfs     files

```

**11.15 Creating FAT16 and FAT32 Filesystems** **|** **267**

```
  (parted) unit mb
  mkpart
  Partition name? []?
  File system type? [ext2]? fat32
  Start? 1656331MB
  End? 1656831MB
  (parted) print
  Model: ATA SAMSUNG HD204UI (scsi)
  Disk /dev/sdb: 2000399MB
  Sector size (logical/physical): 512B/512B
  Partition Table: gpt
  Disk Flags:

  Number Start   End    Size    File system Name Flags
  1   1.05MB   1656331MB 1656330MB xfs     bup
  2   1656331MB 1656831MB 500MB   fat32

  (parted) q
```

The _partition_ name is optional; in the example it is left empty. Now create a nice new
FAT32 filesystem:

```
  $ sudo mkfs.fat -F 32 -n fat32test /dev/sdb2
  mkfs.fat 4.1 (2017-01-24)
  mkfs.fat: warning - lowercase labels might not work properly with DOS or Windows
```

Verify with _lsblk_ :

```
  $ lsblk -f /dev/sdb
  NAME  FSTYPE LABEL    UUID             FSAVAIL FSUSE% MOUNTPOINT
  sdb
  ├─sdb1 xfs  xfstest   1d742b2d-a621-4454-b4d3-469216a6f01e
  └─sdb2 vfat  fat32test  AB39-1808
```

**Discussion**

If you want a FAT16 filesystem, use _-F 16_ .

FAT16 files and filesystems max out at 4 GB.

FAT32 supports a maximum file size of 4 GB, and a maximum partition size of 16 TB,
using 4 KB sectors and 64 KB clusters.

**See Also**

 - Chapter 8

 - Chapter 9

 - _man 8 mkfs.fat_

**268** **|** **Chapter 11: Creating and Managing Filesystems**

**11.16 Creating a Btrfs Filesystem**

**Problem**

Btrfs sounds cool, and you want to try it out.

**Solution**

It is cool, and it is also complex. SUSE Linux Enterprise Server (SLES) and openSUSE
are the best Linux distributions to try Btrfs on. SLES and openSUSE are the biggest
Btrfs supporters and developers, and they created the excellent Snapper tool for man‐
aging Btrfs snapshots. They also provide the most thorough documentation. The
default partitioning on an openSUSE/SLES sets up Btrfs subvolumes and automatic
snapshots.

Start by downloading the latest openSUSE Tumbleweed. Launch the installer, and
when you get to the Suggested Partitioning screen, take a look at the installer’s first
proposal (Figure 11-2).

_Figure 11-2. openSUSE first partitioning proposal_

Click Guided Setup to modify this proposal. Skip past the “Enable logical volume
management (LVM) / Enable disk encryption” screen, and stop at the Filesystem
Options screen. Select “Propose Separate Home Partition,” and format it as Btrfs.

**11.16 Creating a Btrfs Filesystem** **|** **269**

Check both boxes for “Propose Separate Swap Partition,” then click Next
(Figure 11-3).

_Figure 11-3. Create a home partition_

This returns you to the Suggested Partitioning screen. If you wish to adjust partition
sizes, click Expert Partitioner → Start with Current Proposal (Figure 11-4). Otherwise
click Next and continue with the installation.

_Figure 11-4. Custom partitioning, using current proposal_

**270** **|** **Chapter 11: Creating and Managing Filesystems**

When you are finished, you will have a ready-to-use Btrfs Linux system, already set
up with good defaults.

**Discussion**

Setting up Btrfs manually is a bit of a chore, though as you learn about it you might
want to try setting it up manually. I like to learn new things by starting with a work‐
ing implementation. It is not possible, at least for me, to provide a useful Btrfs how-to
in a few recipes. Btrfs is so flexible and so capable, it needs its own book. Which it
has, thanks to the good SUSE people. Consult the Startup Guide for installation, and
[the “System Recovery and Snapshot Management with Snapper” section in the open‐](https://oreil.ly/1Vi9L)
[SUSE documentation. Snapper + Btrfs is a great combination for Btrfs management](https://oreil.ly/1Vi9L)
and fast failure recovery.

**See Also**

 - [The openSUSE Startup and Reference Guides](https://oreil.ly/1Vi9L)

 - [The Deployment and Administration guides in the SLES Product Manuals](https://oreil.ly/fX5G9)

**11.16 Creating a Btrfs Filesystem** **|** **271**

**<u>CHAPTER 12</u>**
#### **Secure Remote Access with OpenSSH**

OpenSSH is the tool of choice for secure remote administration. It encrypts authenti‐
cation and all traffic during a session, and guarantees the integrity of the data transfer.
If something happens to alter your packets, SSH will tell you. In this chapter you will
learn how to set up SSH access to remote hosts, manage your SSH encryption keys,
configure logins to multiple remote hosts, customize your Bash prompt to show
when it is an SSH session, and more good things.

OpenSSH supports a large number of strong encryption algorithms. All of them are
unencumbered by patents because the OpenSSH team has gone to great lengths to
ensure that no patented or otherwise encumbered code is inside OpenSSH. Recipe
12.16 shows how to print lists of all supported algorithms.

OpenSSH is a suite of remote transfer utilities:

 - _sshd_, the OpenSSH server daemon.

 - _ssh_, short for secure shell, though it doesn’t really include a shell, but provides a
secure channel to the command shell on the remote system.

 - _scp_, secure copy, for encrypted file transfer.

 - _sftp_, Secure File Transfer Protocol, provides file access.

 - _ssh-copy-id_, a nice little program for installing your public key to a remote SSH
server’s _authorized_keys_ file.

 - _ssh-keyscan_, finds and collects public host keys on a network, saving you the
trouble of hunting them down manually.

 - _ssh-keygen_, generates and manages authentication keys.

 - _ssh-add_, adds your identities to the authentication agent, _ssh-agent_ .

**273**

In this chapter you will learn about _ssh_, _sshd_, _ssh-copy-id_, _ssh-keygen_, and two useful
related utilities: _sshfs_ and _ssh-agent_ .

_sshfs_ mounts remote filesystems on your local PC, while _ssh-agent_ remembers the
passphrases on your private SSH keys over multiple SSH logins for automatic authen‐
tication. _ssh-agent_ binds to a single login session, so logging out or opening another
terminal means starting over. A better utility for automated operations is Keychain,
which is a frontend to _ssh-agent_ . Keychain reuses _ssh-agent_ until you restart your
machine, so you only have to enter your passphrases at startup (see Recipe 12.10).

OpenSSH supports different types of authentication:

_Password authentication_

Uses your Linux login and password to authenticate. This is the simplest and the
most flexible, because you can log in from any machine. You must be careful to
not open an SSH session from an untrustworthy computer, like in a library or
internet cafe. If it is infected with a keylogger, it will capture your credentials.

_Public key authentication_

Authenticates with your personal SSH public keys, not your system login. This is
a bit more work to set up because you need to create and distribute your public
keys, and you can log in only from machines that hold your private key. Some
commercial services require customers to use some form of public key authenti‐
cation.

_Passphrase-less authentication_

Public key authentication without a passphrase. This is useful for automated
services, like scripts and cron jobs. Anyone who succeeds in thieving the private
key can easily masquerade as you, so you need to be very protective of a
passphrase-less private key.

An alternative to using keys without passphrases is Keychain, which remembers your
private keys for you (see Recipe 12.10).

There are two different uses for authentication keys: host keys, which authenticate
computers, and public keys, which authenticate users. SSH keys come in pairs, private
and public. Transmissions are encrypted with the public key and decrypted with the
private key, a brilliantly simple scheme. You can safely distribute your public keys as
much as you want, while you must protect your private key and not let anyone else
have it.

Server and client are defined by the direction of the transaction. The server has the
SSH daemon running and listening for connection requests, and the client is anyone
logging in to this machine via SSH.

**274** **|** **Chapter 12: Secure Remote Access with OpenSSH**

**12.1 Installing OpenSSH Server**

**Problem**

You want to install an OpenSSH server.

**Solution**

Most Linux distributions install the OpenSSH client by default, but not always the
server. The different Linux distributions package OpenSSH in different ways, so use
your package manager to list the packages for your Linux (see the Appendix). Install
the server, then check if it has started:

```
  $ systemctl status sshd
```

   - `sshd.service - OpenSSH Daemon`
```
  Loaded: loaded (/usr/lib/systemd/system/sshd.service; disabled; vendor preset
  Active: inactive (dead)
  [...]
```

This shows that the server is not running and is not enabled. On most Linuxes,
OpenSSH is not configured to start automatically after installation. This is good
because you need to configure your server correctly before opening it up to receive
connection requests. If it is running before you have examined the server configura‐
tion, stop it, or block its listening port(s) with your firewall.

The next steps are to set up host encryption keys and configure your server. See
Recipes 12.2 and 12.3.

**Discussion**

Remember, server and client are not only about hardware, but are defined by the
direction of the transaction. The server has the SSH daemon running and listening
for connection requests, and the client is anyone logging in to the server via SSH. Any
Linux PC can be a server, client, or both.

**See Also**

 - Chapter 14

 - [OpenSSH](https://openssh.com)

 - sshd (8)

 - The Appendix

**12.1 Installing OpenSSH Server** **|** **275**

**12.2 Generating New Host Keys**

**Problem**

Your Linux distribution does not automatically create host keys at installation, or you
want to replace your existing host keys, or when you clone an installation or a virtual
machine your clones need their own unique host keys.

**Solution**

Use the _ssh-keygen_ command. There are four different types of keys: RSA, DSA,
ECDSA, and ED25519. First, delete the old keys, if they exist:

```
  $ sudo rm /etc/ssh/ssh_host*
```

Create all of the new keys at once with the following command:

```
  $ sudo ssh-keygen -A
  ssh-keygen: generating new host keys: RSA DSA ECDSA ED25519
```

**Discussion**

If you ever get bored and need something to do, try researching “Which SSH key for‐
mats should I use?” The arguments are endless. The short answer is use RSA,
ECDSA, and ED25519, and avoid DSA. Delete your DSA host key and keep the rest.

RSA is the oldest. It is strong and provides the most compatibility.

ECDSA and ED25519 are newer, very strong, and computationally less expensive.

Some older SSH clients do not support ECDSA and ED25519. Hopefully you are not
using such ancient clients, because ECDSA and ED25519 were released with
OpenSSH 6.5 in 2014. It is extremely important to keep security services updated and
to not allow unsafe old clients.

**See Also**

 - [OpenSSH](https://openssh.com)

 - ssh-keygen (1)

**12.3 Configuring Your OpenSSH Server**

**Problem**

You want to configure your OpenSSH server as securely as possible and test it safely.

**276** **|** **Chapter 12: Secure Remote Access with OpenSSH**

**Solution**

First, verify that your server’s private host keys are owned by root, read-only:

```
  $ ls -l /etc/ssh/
  -r-------- 1 root root  227 Jun 4 11:30 ssh_host_ecdsa_key
  -r-------- 1 root root  399 Jun 4 11:30 ssh_host_ed25519_key
  -r-------- 1 root root  1679 Jun 4 11:30 ssh_host_rsa_key
```

That is how they are supposed to look. Then check your public keys, which are
owned by root, read-write for root, and read-only for everyone else:

```
  $ ls -l /etc/ssh/
  -rw-r--r-- 1 root root  174 Jun 4 11:30 ssh_host_ecdsa_key.pub
  -rw-r--r-- 1 root root   94 Jun 4 11:30 ssh_host_ed25519_key.pub
  -rw-r--r-- 1 root root  394 Jun 4 11:30 ssh_host_rsa_key.pub
```

These are correct.

Now take a look at _/etc/ssh/sshd_config_ . When you change this file, reload _sshd_ to load
your changes:

```
  $ sudo systemctl reload sshd.server
```

Uncomment the options you want to use or change.

Configure _sshd_ to check if the file modes and ownership of the user’s files and home
directory are correct before accepting their login:

```
  StrictModes yes
```

If file permissions are not correct, this setting will not allow them to log in.

If your machine has more than one IP address, define which address, or addresses, it
listens on:

```
  ListenAddress 192.168.10.15
  ListenAddress 1 92.168.10.16
```

You may assign nonstandard ports for _sshd_ to listen on. Use only ports above 1024,
and check _/etc/services_ to find unused ports, then add your new ports to _/etc/services_ :

```
  sshd 2022
  sshd 2023
```

Then add them to _/etc/ssh/sshd_config_ :

```
  Port 2022
  Port 2023
```

You can restrict access to only the specified groups (create these groups in _/etc/group_ ):

```
  AllowGroups webadmins backupadmins
```

Or deny access with _DenyGroups_ .

**12.3 Configuring Your OpenSSH Server** **|** **277**

Do not allow root logins. It is safer to log in as an unprivileged user, and then use
_sudo_ after login:

```
  PermitRootLogin no
```

An alternative is to allow root logins only with public key authentication:

```
  PermitRootLogin prohibit-password
```

You can disable password logins for all users, and allow only public key authentica‐
tion (see Recipe 12.7):

```
  PasswordAuthentication no
```

You can deny specified users, either by username, or user at hostname or IP address:

```
  DenyUsers duchess madmax stash@example.com cagney@192.168.10.25
```

Or allow access with _AllowUsers_ . You may use both, and _DenyUsers_ is always pro‐
cessed first.

Limit the length of time the server waits for a user to log in and complete the connec‐
tion. The default is 120 seconds:

```
  LoginGraceTime 90
```

You can limit the number of failed connection attempts. The default is 6:

```
  MaxAuthTries 4
```

**Discussion**

Any port scanner will find your open ports, and attackers will attempt brute force
password cracking. Attackers still target the default SSH port 22 the most. Changing
the port won’t reduce this risk very much, but it should reduce the number of entries
in your log files. When you use alternate port numbers, first look in _/etc/services_ to
find unused ports, and then record the ports you use in this file.

Public key authentication is very strong and cannot be brute-forced like password
logins (see Recipe 12.7). The trade-off is less convenience, as you can log in only from
machines that have your private key.

**See Also**

 - [OpenSSH](https://openssh.com)

 - _man 5 sshd_config_

 - Recipe 12.5

 - Recipe 12.7

**278** **|** **Chapter 12: Secure Remote Access with OpenSSH**

**12.4 Checking Configuration Syntax**

**Problem**

Everyone makes mistakes, and you want a syntax checker for _/etc/ssh/sshd_config_ .

**Solution**

And you shall have one. After making your changes, run this command:

```
  $ sudo sshd -t
```

If there are no syntax errors, it exits silently. If it find mistakes, it tells you:

```
  $ sudo sshd -t
  /etc/ssh/sshd_config: line 9: Bad configuration option: Porotocol
  /etc/ssh/sshd_config: terminating, 1 bad configuration options
```

You can do this while the SSH daemon is running, so you can correct your mistakes
before issuing a reload or restart command.

**Discussion**

The _-t_ stands for _test_ . It does not affect the SSH daemon, it only checks _/etc/ssh/_
_sshd_config_ for syntax errors, so you can use it anytime.

**See Also**

 - _man 5 sshd_config_

 - [OpenSSH](https://openssh.com)

**12.5 Setting Up Password Authentication**

**Problem**

You want to set up your OpenSSH client to log in to a remote host using the simplest
method that it supports.

**Solution**

Password authentication is the simplest way to set up remote SSH access. You need:

 - OpenSSH server installed and properly configured on the machine you want to
log in to (Recipe 12.3)

 - The SSH daemon running on the remote machine, and port 22, or whatever port
_sshd_ uses, not blocked by firewalls

**12.4 Checking Configuration Syntax** **|** **279**

 - The SSH client installed on your client machine

 - Your own user account on the remote machine

 - Host keys on the server (see Recipe 12.2)

The public host key must be distributed to the clients. The easy way is to log in from
the client, and let OpenSSH transfer the key:

```
  duchess@pc:~$ ssh duchess@server1
  The authenticity of host ' server1 (192.168.43.74) ' can't be established.
  ECDSA key fingerprint is SHA256:8iIg9wwFIzLgwiiQ62WNLF5oOS3SL/aTw6gFrtVJTx8.
  Are you sure you want to continue connecting (yes/no)? *yes*
  Warning: Permanently added ' server1,192.168.43.74 ' (ECDSA) to the list of
  known hosts.
  Password: password
  Last login: Wed Jul 8 19:22:39 2021 from 192.168.43.183
  Have a lot of fun...
```

Now Duchess can work on _server1_ just as if she were sitting at _server1_ ’s keyboard. All
traffic and authentication are encrypted.

The host key exchange happens only once, the first time you log in. You should never
be asked again unless the key is replaced with a new key, or you delete it from your
personal _~/.ssh/known_hosts_ file.

**Discussion**

_server1_ ’s public host key is stored in the _~/.ssh/known_hosts_ file on the client PC. This
file can contain any number of host keys.

It is unsafe to log in as root over SSH; it is better to log in as an ordinary user, then _su_
or _sudo_ after login. You can log in as any user that has an account on the remote
machine, if you know their password:

```
  duchess@pc:~$ ssh madmax@server1
```

When you have the same username on both machines, you don’t need to specify the
user, and can log in like this:

```
  duchess@pc:~$ ssh server1
```

I make it a habit to always specify the username as cheap insurance against mistakes.

Don’t get too worked up over _client_ and _server_ . These are not about hardware. The
server is whatever machine you are logging in to, and the client is wherever you are
logging in from. _sshd_ does not need to be running on the client.

There is a risk that the host key transmission could be intercepted and a forged key
substituted, which would allow an attacker access to your systems. You can verify the
public key fingerprint before typing **`yes`** . Use an old-fashioned method like writing it
down and comparing, or a newfangled method like taking a photo of the host key

**280** **|** **Chapter 12: Secure Remote Access with OpenSSH**

with your phone for comparison, or using your phone as an actual phone and calling
someone who has access to the remote machine to read the fingerprint to you.

See Recipe 12.6 to learn how to retrieve a key fingerprint.

**See Also**

 - Recipe 12.6

 - [OpenSSH](https://openssh.com)

 - _man 1 ssh_

 - _man 1 ssh-keygen_

 - _man 8 sshd_

**12.6 Retrieving a Key Fingerprint**

**Problem**

You need the fingerprint of a host key so you can verify for the client that the key is
legitimate.

**Solution**

Use the _ssh-keygen_ command on the server with the host key you want to query:

```
  duchess@server1:~$ ssh-keygen -lf /etc/ssh/ssh_host_rsa_key
  4096 SHA256:32Pja4+F2+MTdla9cs4ucecThswRQp6a4xZ+5sC+Bf0 backup server1 (RSA)
```

**Discussion**

This is where old-fashioned methods of communication, like telephone and sneaker‐
net, come in handy. Don’t use email, unless you already have encrypted email with its
own separate encryption and authentication, because unencrypted email is easy to
intercept and read.

**See Also**

 - [OpenSSH](https://openssh.com)

 - _man 1 ssh-keygen_

**12.6 Retrieving a Key Fingerprint** **|** **281**

**12.7 Using Public Key Authentication**

**Problem**

You want to use public key authentication because it is stronger than password
authentication, and because it does not use your Linux password. You want the
option of using a single public key to access multiple systems, or creating a unique
public key for each remote machine.

**Solution**

Yes, Linux user, you can have it all. You may create as many SSH keys as you want and
use them however you wish. This is my favorite incantation for creating a new RSA
key pair. Of course you will create your own comment and key name. (See the Dis‐
cussion to learn if you need to set a passphrase on your private key.)

```
  duchess@pc:~/.ssh $ ssh-keygen -C " backup server2 " -f id-server2 -t rsa -b 4096
  Generating public/private rsa key pair.
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  Your identification has been saved in id-server2 .
  Your public key has been saved in id-server2.pub .
  The key fingerprint is:
  SHA256:32Pja4+F2+MTdla9cs4ucecThswRQp6a4xZ+5sC+Bf0 backup server2
  The key's randomart image is:
  +---[RSA 4096]----+
  |     ..   |
  |     ....  |
  |      o. . .|
  |     + . o|
  |    S* .o o o|
  |    +.+..Bo*+|
  |     *.+*EX=o|
  |    o *o.Oo+.|
  |     o.o=+*+.|
  +----[SHA256]-----+
```

The next step is to copy your nice new key to a remote machine, which in this case is
the local backup server _server1_ . You must already have SSH access to the remote
machine, for example, via host key authentication, then use the _ssh-copy-id_ command
to transfer your public key to the server:

```
  duchess@pc:~/.ssh $ ssh-copy-id -i id-server1 duchess@server1
  /usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: " .ssh/id-server1 "
  /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter
  out any that are already installed
  /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are
  prompted now it is to install the new keys

  Number of key(s) added: 1

```

**282** **|** **Chapter 12: Secure Remote Access with OpenSSH**

```
  Now try logging into the machine, with:  "ssh ' duchess@server1 '"
  and check to make sure that only the key(s) you wanted were added.
```

Try logging in:

```
  duchess@pc:~/.ssh $ ssh -i id-server1 duchess@server1
  Enter passphrase for key ' id-server1 ':
  Last login: Sat Jul 11 11:09:53 2021 from 192.168.43.234
  Have a lot of fun...
  duchess@server1:~$
```

You may use this new key to access multiple remote hosts, or create a unique key for
each remote host. Using the same key for multiple machines is easy to use, but a pain
to change on multiple hosts. If a unique key is compromised or lost, you only need to
replace it once.

**Discussion**

Always use a passphrase on SSH keys created for human users, because anyone who
gains access to your private keys can masquerade as you if there is no passphrase.

_ssh-copy-id_ is a lovely little utility that ensures your public keys are copied into the
correct location, which is _~/.ssh/authorized_keys_ on the remote host, in the correct
format and with the correct permissions. It also ensures your private key will not be
copied by mistake.

Options are as follows:

 - _-C_ is for adding a comment to your key, which can help you remember what the
key is for.

 - _-f_ is the key name, which can be anything you want. Be mindful of your current
working directory; if you are not in _~/.ssh_, include the path.

 - _-t_ is the key type: _rsa_, _ecdsa_, or _ed25519_ .

 - _-b_ is the bit strength, and only _rsa_ takes this option. The default is 2048, and 4096
is the maximum. More bits equals more processing overhead, but it is doubtful
you would notice any difference using 4096 bits except on old feeble hardware or
on very busy servers.

 - _-i_ tells your SSH client which key you want to use. When you have more than one
key, you must use this. When you have multiple public keys, you may see a “Too
many authentication failures” error message if you do not specify one key,
because SSH tries all of them when one is not specified.

**12.7 Using Public Key Authentication** **|** **283**

**See Also**

 - [OpenSSH](https://openssh.com)

 - _man 1 ssh_

 - _man 1 ssh-keygen_

**12.8 Managing Multiple Public Keys**

**Problem**

You want to use different keys for different servers. How do you manage keys with
different names?

**Solution**

When you create a new key pair, use the _-f_ option of the _ssh-keygen_ command to give
keys unique names:

```
  duchess@pc:~/.ssh $ ssh-keygen -t rsa -f id-server2
```

Then, use the _-i_ option to specify the key you want to use when you log in to the
remote host:

```
  duchess@pc:~/.ssh $ ssh -i id-server2 duchess@server2
```

To manage multiple public keys more easily, create a new file, _~/.ssh.config_ . This file
configures the logins for your various remote hosts, so you log in with _ssh foo_ instead
of a long command string. The following example configures a simpler login for
Duchess to access _server2_ :

```
  Host server2
  HostName server2
  User duchess
  IdentityFile ~/.ssh/id-server2
  IdentitiesOnly yes
```

Now Duchess logs in like this, using the _Host_ value:

```
  $ ssh server2
```

Keep adding to this file for your other public key logins, like this:

```
  Host server3
  HostName server3
  User duchess
  IdentityFile ~/.ssh/id-server3
  IdentitiesOnly yes

  Host server3
  HostName server3

```

**284** **|** **Chapter 12: Secure Remote Access with OpenSSH**

```
  User madmax
  IdentityFile ~/.ssh/id-server3
  IdentitiesOnly yes
```

**Discussion**

In the preceding solution snippet:

 - The _Host_ line defines the start of each configuration. This is the label you use to
login, and it can be anything you want.

 - _HostName_ is the remote machine’s hostname, fully qualified domain name, or IP
address.

 - _User_ is your user on the remote machine.

 - _IdentityFile_ is the full path to your public key.

 - _IdentitiesOnly yes_ tells _ssh_ to use the settings in _~/.ssh/config_, or passed on the
command line, and not other providers, if there are any.

The default SSH port number is 22. When you need to connect to a nonstandard
port, for example 2022, specify it with _Port_ :

```
  Port 2022
```

You may call your keys anything you want. I like to use descriptive names so I know
what machines they belong to.

Remember to always put a passphrase on your personal private keys.

**See Also**

 - [OpenSSH](https://openssh.com)

 - _man 1 ssh_config_

 - _man 1 ssh_

**12.9 Changing a Passphrase**

**Problem**

You want to change the passphrase on one of your private keys.

**Solution**

Use the _-p_ option with the _ssh-keygen_ command:

```
  $ ssh-keygen -p -f ~/.ssh/ id-server2
  Enter old passphrase:

```

**12.9 Changing a Passphrase** **|** **285**

```
  Key has comment ' backup server2 '
  Enter new passphrase (empty for no passphrase ):
  Enter same passphrase again: passphrase
  Your identification has been saved with the new passphrase.
```

**Discussion**

Passphrases are not recoverable. If you lose a passphrase, your only option is to create
a new key with a new passphrase.

**See Also**

 - [OpenSSH](https://openssh.com)

 - _man 1 ssh__

 - _man 1 ssh-keygen_

**12.10 Automatic Passphrase Management with Keychain**

**Problem**

You want something to remember your private key passphrases for you, and use them
as needed.

**Solution**

The Keychain utility was made for this. Install the _keychain_ package, then copy the
lines in the following example into your _.bashrc_ file.

In the following example, you want access to _server1_, _server2_, and _server3_ without
entering your passphrases every time you log in. Copy these lines, except using your
own key names:

```
  keychain ~/.ssh/ id-server1 ~/.ssh/ id-server2 \
  ~/.ssh/ id-server3 . ~/.keychain/$HOSTNAME-sh
```

Keychain keeps your private keys available until you shut down, so you must enter
your passphrases every time you start up your system.

When you boot to a graphical environment, you may not be prompted to enter your
passphrases. Try opening a terminal, and if you still don’t see a Keychain prompt for
your passphrases, you must enter a Linux console. Press Ctrl-Alt-F2 and log in. After
logging in, you should see something like this:

```
  * keychain 2.8.5 ~ http://www.funtoo.org
  * Found existing ssh-agent: 2016
  * Adding 3 ssh key(s): /home/duchess/.ssh/id-server1

```

**286** **|** **Chapter 12: Secure Remote Access with OpenSSH**

```
  /home/duchess/.ssh/id-server2 /home/duchess/.ssh/id-server3
  Enter passphrase for /home/duchess/.ssh/id-server1 :
  Enter passphrase for /home/duchess/.ssh/id-server2 :
  Enter passphrase for /home/duchess/.ssh/id-server3 :
  * ssh-add: Identities added: /home/duchess/.ssh/id-server1
  /home/duchess/.ssh/id-server2 /home/duchess/.ssh/id-server3
```

**Discussion**

The leading dot in _. ~/.keychain/$HOSTNAME-sh_ is short for _source_, meaning use the
named file.

_$HOSTNAME_ tells Keychain to look in the user’s environment variables to fetch their
hostname. You can see this for yourself:

```
  $ echo $HOSTNAME
  pc
```

Keychain is a manager for both _ssh-agent_ and _gpg-agent_, caching your SSH and GPG
passphrases for as long as your computer is powered on. You can log out and log back
in, and will have to reenter your passphrases only after a restart.

A good alternative is _gnome-keyring_, which runs in graphical environments. This pro‐
vides a graphical interface for viewing and managing SSH and GPG keys, and it also
includes a password manager. This appears as “Passwords and Keys” on most sys‐
tems. Its has two disadvantage: it’s not suitable to use on headless systems, and it does
not make passphrases available to cron (see Recipe 12.11.)

**See Also**

 - [Funtoo Keychain](https://oreil.ly/rljaf)

**12.11 Using Keychain to Make Passphrases Available**
**to Cron**

**Problem**

You need to use cron to automate tasks, such as running rsync backups to a remote
host. But no matter what you try, you get nothing for your troubles but failed backups
with authentication errors.

**12.11 Using Keychain to Make Passphrases Available to Cron** **|** **287**

**Solution**

To configure Keychain to manage your private keys for cron jobs, create a script for
cron to use. The following example is for an rsync backup, and the script is named
_duchess-backup-server1_ :

```
  #!/bin/bash
  source $HOME/.keychain/${HOSTNAME}-sh
  /usr/bin/rsync -ae "ssh -i /home/duchess/.ssh/id-server3" /home/duchess/ \
  duchess@server1:/backups/
```

Make this script executable with _chmod_ :

```
  $ chmod +x duchess-backup-server1
```

This example adds a line to your crontab to run the script every night at 10:15 P.M.:

```
  15 22 * * * /home/duchess/duchess-backup-server1
```

**Discussion**

In the example script, the line starting with _/usr/bin/rsync_ must be all on a single line.

Cron runs in its own special limited environment and needs Keychain to provide the
required keys and environment variables.

**See Also**

 - _man 1 crontab_

 - [Funtoo Keychain](https://oreil.ly/rljaf)

**12.12 Tunneling an X Session Securely over SSH**

**Problem**

You want to run graphical applications from the remote host. You know that the X
Window System has built-in networking abilities, but it sends all traffic in cleartext,
which is insecure, and you want to do this safely.

**Solution**

Tunneling X over SSH requires no additional software. First, use these commands to
see if your client machine is running the X11 or Wayland protocol. The following
examples show both results:

```
  $ echo $XDG_SESSION_TYPE
  x11
  $ echo $XDG_SESSION_TYPE

```

**288** **|** **Chapter 12: Secure Remote Access with OpenSSH**

```
  wayland
  $ loginctl show-session "$XDG_SESSION_ID" -p Type
  Type=x11
  $ loginctl show-session "$XDG_SESSION_ID" -p Type
  Type=wayland
```

_loginctl_ is part of systemd.

If you are running Wayland, you cannot tunnel it over SSH because it does not have
networking support.

If your system is using X11, configure X11 forwarding in _/etc/ssh/sshd_config_ on the
remote machine:

```
  X11Forwarding yes
```

The following example tunnels X over SSH, using the _-Y_ option:

```
  duchess@pc:~$ ssh -Yi id-server1 duchess@server1
  Last login: Thu Jul 9 09:26:09 2021 from 192.168.43.80
  Have a lot of fun..
  duchess@server1:~$
```

Now you can run graphical applications, though only one at a time, like the game in
Figure 12-1:

```
  duchess@server1:~$ kmahjongg

```

_Figure 12-1. Playing KMahjongg on the remote server_

**12.12 Tunneling an X Session Securely over SSH** **|** **289**

**Discussion**

The X server runs with the offset specified in _/etc/ssh/sshd.conf_, _X11DisplayOffset 10_ .
This avoids colliding with existing X sessions. Your regular local X session is :0.0, so
your first remote X session is :10.0. You can see this with your own eyes. Run the fol‐
lowing commands on your local machine. The first one is at your local command
prompt:

```
  duchess@pc:~$ echo $DISPLAY
  :0.0
```

The second example is at your SSH command prompt:

```
  duchess@server1:~ssh $ echo $DISPLAY
  localhost:10.0
```

The remote system only needs to be powered on. You don’t need any local users to be
logged in, and you don’t even need X to be running. X needs to be running only on
the client PC.

**See Also**

 - _man 1 sshd_

 - _man 1 ssh_config_

**12.13 Opening an SSH Session and Running a Command**
**in One Line**

**Problem**

You have a single command to run on the remote machine, and you think it would be
nice to run it without logging in and running the command, and then logging out.
After all, is it not true that laziness is a virtue for system administrators?

**Solution**

OpenSSH can do this. This example shows how to restart Postfix:

```
  $ ssh mailadmin@server2.example.com sudo systemctl restart postfix
```

You’ll be asked for a _sudo_ password, but you will still save one whole step.

This shows how to open a quick game of GNOME Sudoku, which requires the X
Window System:

```
  $ ssh -Y duchess@laptop /usr/games/gnome-sudoku

```

**290** **|** **Chapter 12: Secure Remote Access with OpenSSH**

**Discussion**

Another way to do this is with public key authentication for the root user, so you
don’t have to invoke _sudo_ (Recipe 12.7).

**See Also**

 - _man 1 ssh_

**12.14 Mounting Entire Remote Filesystems with sshfs**

**Problem**

OpenSSH is fast and efficient, and even tunneling X applications over OpenSSH isn’t
too laggy. But you want a faster way to edit a number of remote files without running
a graphical file manager over SSH.

**Solution**

_sshfs_ is the tool for you. _sshfs_ is for mounting an entire remote filesystem, and then
accessing it just like a local filesystem, without the hassles of setting up an NFS or
Samba server.

Install the _sshfs_ package, which should also install FUSE, the Filesystem in Userspace.
You need a local directory that you have write permissions for as your mountpoint:

```
  duchess@pc:~$ mkdir sshfs
```

Then mount your chosen remote directory in your local _sshfs_ directory. This example
mounts the home directory for _duchess@server2_ in the _sshfs_ directory at _duchess@pc_ :

```
  duchess@pc:~$ sshfs duchess@server2: sshfs/
```

The remote filesystem is just as accessible as your local filesystems:

```
  duchess@pc:~$ ls sshfs
  Desktop
  Documents
  Downloads
  [...]
```

Access these files from the command line or with your graphical file manager, just
like your local files.

Your command prompt will not change to the remote prompt.

When you’re finished, unmount the remote filesystem:

```
  duchess@pc:~$ fusermount -u sshfs/

```

**12.14 Mounting Entire Remote Filesystems with sshfs** **|** **291**

That mounts Duchess’s entire home directory. Specify a subdirectory instead:

```
  duchess@pc:~$ sshfs duchess@server2:/home/duchess/arias sshfs/
```

You cannot use the tilde, ~, as a shortcut for _/home/user_ because _sshfs_ does not sup‐
port it.

If your network connection is not reliable, tell _sshfs_ to automatically reconnect after
an interruption:

```
  duchess@pc:~$ sshfs duchess@server2:/home/duchess/arias sshfs/ -o reconnect
```

**Discussion**

Users who are new to _sshfs_ always ask these questions: why not just run X over SSH,
or why not just use NFS? The answers are: it is faster than running X over SSH, it is
easier to set up than NFS, and you may use NFS, Samba, or whatever your heart
desires.

**See Also**

 - _man 1 sshfs_

**12.15 Customizing the Bash Prompt for SSH**

**Problem**

Sure, you know that the prompt changes to display the remote hostname when you’re
logged in via SSH. But it’s just a plain prompt, and it’s easy to make mistakes, so you
want a customized, colorful prompt to indicate when you have an active SSH login.

**Solution**

Customize the Bash prompt on the remote machines. This example turns the prompt
purple and adds “ssh” to it.

Copy these lines into the _.bashrc_ file for the remote account you want to log in to:

```
  if [ -n "$SSH_CLIENT" ]; then text=" ssh"
  fi
  export PS1='\[\e[0;36m\]\u@\h:\w${text}$\[\e[0m\] '
```

When you log in to this machine, the prompt will look like what’s shown in
Figure 12-2.

**292** **|** **Chapter 12: Secure Remote Access with OpenSSH**

_Figure 12-2. A customized SSH prompt_

Only the prompt is purple, and all the other text will be your normal shell colors.

**Discussion**

Customizing the Bash prompt is practically a book topic in itself. The example in this
recipe can be edited to suit your preferences. You don’t have to use the term “ssh” or
name the variable “text”; these can be anything you like. You could say “super duper
encrypted session” and name your variable “sekkret-squirl” if you want.

_[\e[0;31m\]_ is the code block that determines the text color. All you have to do is
change the numbers to change the colors.

_[\e[0m\]_ turns off the custom colors, so that your commands and command output
will return to the normal shell colors. Here are the color codes:

- Black 0;30

- Blue 0;34

- Green 0;32

- Cyan 0;36

- Red 0;31

- Purple 0;35

- Brown 0;33

- Light Gray 0;37

- Dark Gray 1;30

- Light Blue 1;34

- Light Green 1;32

- Light Cyan 1;36

- Light Red 1;31

- Light Purple 1;35

- Yellow 1;33

- White 1;37

This customization works by checking for the presence of the _SSH_CLIENT_ environ‐
ment variable, which is present only when there is an active SSH connection. You can
see this for yourself on the remote host:

```
  $ echo $SSH_CLIENT
  192.168.43.234 51414 22
```

Then Bash knows to use the custom SSH prompt instead of the default prompt.
When you run this command on a machine without any active SSH sessions, it
returns an empty line.

**12.15 Customizing the Bash Prompt for SSH** **|** **293**

**See Also**

 - _man 1 bash_

 - [Bash Prompt HOWTO, Chapter 6](https://oreil.ly/QXWmT)

**12.16 Listing Supported Encryption Algorithms**

**Problem**

You have compliance rules to follow and need to know what encryption algorithms
OpenSSH supports.

**Solution**

OpenSSH includes a command to query and list all supported algorithms, _ssh -Q_
_<query_option>_ . List them with the _help_ option:

```
  $ ssh -Q help
  cipher
  cipher-auth
  compression
  kex
  kex-gss
  key
  key-cert
  key-plain
  key-sig
  mac
  protocol-version
  sig
```

The following example lists the _sig_ signature algorithms:

```
  $ ssh -Q sig
  ssh-ed25519
  sk-ssh-ed25519@openssh.com
  ssh-rsa
  rsa-sha2-256
  rsa-sha2-512
  ssh-dss
  ecdsa-sha2-nistp256
  ecdsa-sha2-nistp384
  ecdsa-sha2-nistp521
  sk-ecdsa-sha2-nistp256@openssh.com

```

**294** **|** **Chapter 12: Secure Remote Access with OpenSSH**

**Discussion**

The following list briefly describes each option:

 - _cipher_ lists supported symmetric ciphers.

 - _cipher-auth_ lists supported symmetric ciphers that also support authenticated
encryption.

 - _compression_ lists supported compression types.

 - _mac_ lists supported message integrity codes. These protect your message’s data
integrity and its authenticity.

 - _kex_ lists key exchange algorithms.

 - _kex-gss_ lists GSSAPI (Generic Security Service Application Program Interface)
key exchange algorithms.

 - _key_ lists key types.

 - _key-cert_ lists certificate key types.

 - _key-plain_ lists noncertificate key types.

 - _key-sig_ lists all key types and signature algorithms.

 - _protocol-version_ lists supported SSH protocol versions, which is only version 2 at
the time of writing.

 - _sig_ lists supported signature algorithms.

**See Also**

 - [OpenSSH](https://openssh.com)

 - _Serious Cryptography_ by Jean-Philippe Aumasson (No Starch Press)

**12.16 Listing Supported Encryption Algorithms** **|** **295**

**<u>CHAPTER 13</u>**
#### **Secure Remote Access with OpenVPN**

Open Virtual Private Network (OpenVPN) creates a TLS/SSL encrypted connection
between two different networks at separate physical locations, like a branch office
linked to a main office, or a remote worker logging in to the company network from
home. This connection is called an encrypted _tunnel_, a secure transport protecting
your connection from the big bad internet. OpenVPN is dependent on OpenSSL, so
having OpenSSL knowledge is helpful.

If you are already familiar with OpenVPN, you can probably skip
ahead to Recipes 13.5, 13.6, and 13.7 to review creating your
encryption certificates and client and server configuration. If you
are new to VPNs, try each recipe in sequence. Take your time;
VPNs are complicated and finicky. Do a lot of testing before
deploying to production systems.

**OpenVPN Overview**

A VPN is a secure extension of your network that makes all the same services avail‐
able to remote workers that local users have, so the remote users’ experience is the
same as for users physically present at your location. They can access your local web
servers, email, file shares, chat servers, video conferencing apps, internal wikis, every‐
thing that you have walled off from the outside world and is available only to users
inside your network. A VPN is not like SSH, which connects individual computers. A
VPN links etworks and individual hosts to networks.

In this chapter you will learn how to set up an OpenVPN server, configure clients,
and create and manage a proper public key infrastructure (PKI) for authentication
and encryption. Your server will authenticate and protect all manner of clients: Linux,
macOS, Windows PCs, Android, and iOS devices.

**297**

OpenVPN is an open source project, with both free downloads and commercial
options. The free-of-cost server and client is the _openvpn_ package, which is available
[on all Linux distros and downloads at OpenVPN Community Downloads. Commer‐](https://oreil.ly/vwEAs)
cial options include OpenVPN Access Server, which is a premises server with addi‐
tional management tools and cloud options. Hosted personal plans require installing
only the client and provide access to a global network of OpenVPN servers.

A true VPN is strong because it trusts no one and requires authenticated endpoints,
where server and client authenticate to each other. Most commercial TLS/SSL VPNs
do not do this, but instead trust all clients, like shopping sites do. This is more flexible
and allows users to log in from anywhere, using any device. It is convenient not to
have to install and configure client software and copy encryption keys. But for your
internal network that is shortsighted—the last thing you need is users logging in from
random PCs or smartphones infected with keyloggers and spyware, and then given a
warm welcome into your LAN.

**Certificate Authority**

A certificate authority (CA) is the most important part of running an OpenVPN
server. A CA issues digital certificates and certifies ownership of public keys. Click
the little padlock in a web browser to see the public certificate for a website, and
which CA signed it. A CA is a trusted authority, and that is why so many sites use
commercial CAs. Self-signed certificates, like the ones we are creating in this chapter,
are fine to use inside your organization. Customer-facing sites should use commercial
CAs. Using a CA saves you from the hassle of keeping copies of client certificates on
your OpenVPN server; all the server needs to know is that the client certificate is
authenticated by your CA.

**SSL Versus TLS**

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are cryptographic
protocols. TLS evolved from SSL. All versions of SSL are deprecated, as are TLS 1.0
and TLS 1.1. Use TLS 1.2 or 1.3, and disable all the others (Recipe 13.10). Older ver‐
sions are deprecated because of security flaws, so don’t let anyone talk you into sup‐
porting deprecated versions.

**TUN/TAP**

The _TUN_ and _TAP_ devices are virtual network interfaces. These are built into the
Linux kernel, and you should not have to do anything to make them available. The
_TUN_ device is for routed networks, and the _TAP_ device is for bridged networks. Your
server and client configuration files specify which one to use.

**298** **|** **Chapter 13: Secure Remote Access with OpenVPN**

**Good Security Takes Work**

Good security requires ongoing study and maintenance. This chap‐
ter aims to show you how to set up a strong VPN that is reasonably
user-friendly. There are many additional methods for making your
VPN even stronger, such as client certificates with short lifetimes,
additional authentications, hardware devices, SELinux, chroot jails,
short password timeouts, and many more. If you require superhigh security, please consult expert professionals.

**13.1 Installing OpenVPN, Server and Client**

**Problem**

You need to know how to install openVPN.

**Solution**

[The OpenVPN website supplies both the community open source OpenVPN and the](https://openvpn.net)
commercial OpenVPN Access Server. The community OpenVPN is free of cost and
open source. This chapter covers the community OpenVPN.

On Linux, install the _openvpn_ package. (As always, verify the package name on your
particular Linux.) Get the most current version you can, from 2.4.5 and up. This pro‐
vides both server and client. Source tarballs and Windows installers are available
[from OpenVPN Community Downloads.](https://oreil.ly/vwEAs)

[For your clients, you could try the free OpenVPN Access Clients, which are available](https://oreil.ly/vQugl)
for Linux, macOS, Android, iOS, and Windows. These are designed for the commer‐
cial OpenVPN Access Server and also work with the community OpenVPN server.

You can also find the community OpenVPN client for Android in the Google Play
Store.

See Recipe 13.9 to learn how to use the _.ovpn_ inline file format for easier client
configuration.

**Discussion**

On Linux, OpenVPN must be installed on your OpenVPN server and on all clients.
The OpenVPN package provides both client and server functionality.

Ubuntu, Fedora, and openSUSE include additional packages that provide integration
with NetworkManager, which makes managing, connecting, and disconnecting to
VPNs nice and easy.

**13.1 Installing OpenVPN, Server and Client** **|** **299**

_NetworkManager-openvpn_ (Fedora, openSUSE) and _network-manager-openvpn_
(Ubuntu) integrate OpenVPN with Network Manager. If you are using the GNOME
environment (such as GNOME, Xfce, Cinnamon, or Mate), you also need
_NetworkManager-openvpn-gnome_ (openSUSE, Fedora), or _network-manager-openvpn_
(Ubuntu).

OpenVPN Access Server is a free download, and you may connect up to two clients at
the same time without purchasing a license. It comes with additional features, such as
a web administration interface and automatic configurations with the free OpenVPN
Access Client. If you start with the community OpenVPN and then decide to migrate
to OpenVPN Access Server, everything you learned for the community OpenVPN
server applies to Access Server as well.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.2 Setting Up a Simple Connection Test**

**Problem**

You want to run the simplest OpenVPN connection test to get an idea of how it
works and to verify connectivity.

**Solution**

The following simple test creates an unencrypted tunnel between two Linux comput‐
ers that are on the same network. OpenVPN must be installed on both of them. First
verify that the OpenVPN daemon is not running on either host, and if it is, stop it:

```
  $ systemctl status openvpn@.openvpn1.service
```

   - `openvpn.service - OpenVPN service`
```
  Loaded: loaded (/lib/systemd/system/openvpn.service; enabled; vendor prese>
  Active: active (exited) since Sun 2021-01-10 13:43:18 PST; 33min ago
  [...]
  $ sudo systemctl stop openvpn@.openvpn1.service

```

**Use a Different Subnet for Your VPN**

Use a different subnet for your OpenVPN tunnel; for example,
_host1_ and _host2_ are on 192.168.43.0/24, so the example uses the
10.0.0.0/24 private address space for the VPN tunnel.

**300** **|** **Chapter 13: Secure Remote Access with OpenVPN**

In the following example, the two computers are named _host1_ and _host2_ . The first
example creates a VPN tunnel from _host1_ to _host2_ :

```
  [madmax@host1 ~]$ sudo openvpn --remote host2 --dev tun0 --ifconfig 10.0.0.1 \
  10.0.0.2
  Sat Jan 9 14:40:34 2021 disabling NCP mode (--ncp-disable) because not in P2MP
  client or server mode
  Sat Jan 9 14:40:34 2021 OpenVPN 2.4.8 x86_64-redhat-linux-gnu [SSL (OpenSSL)]
  [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Jan 29 2020
  Sat Jan 9 14:40:34 2021 library versions: OpenSSL 1.1.1d FIPS 10 Sep 2019,
  LZO 2.10
  Sat Jan 9 14:40:34 2021 ******* WARNING *******: All encryption and
  authentication features disabled -- All data will be tunnelled as clear text
  and will not be protected against man-in-the-middle changes. PLEASE DO
  RECONSIDER THIS CONFIGURATION!
  Sat Jan 9 14:40:34 2021 TUN/TAP device tun0 opened
  Sat Jan 9 14:40:34 2021 /sbin/ip link set dev tun0 up mtu 1500
  Sat Jan 9 14:40:34 2021 /sbin/ip addr add dev tun0 local 10.0.0.1 peer 10.0.0.2
  Sat Jan 9 14:40:34 2021 TCP/UDP: Preserving recently used remote address:
  [AF_INET]192.168.122.239:1194
  Sat Jan 9 14:40:34 2021 UDP link local (bound): [AF_INET][undef]:1194
  Sat Jan 9 14:40:34 2021 UDP link remote: [AF_INET]192.168.122.239:1194
```

This example creates a link from _host2_ to _host1_ :

```
  [stash@host2 ~]$ sudo openvpn --remote host1 --dev tun0 --ifconfig 10.0.0.2 \
  10.0.0.1
  Sat Jan 9 14:50:53 2021 disabling NCP mode (--ncp-disable) because not in P2MP
  client or server mode
  Sat Jan 9 14:50:53 2021 OpenVPN 2.4.7 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO]
  [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Sep 5 2019
  Sat Jan 9 14:50:53 2021 library versions: OpenSSL 1.1.1f 31 Mar 2020, LZO 2.10
  Sat Jan 9 14:50:53 2021 ******* WARNING *******: All encryption and
  authentication features disabled -- All data will be tunnelled as clear text
  and will not be protected against man-in-the-middle changes. PLEASE DO
  RECONSIDER THIS CONFIGURATION!
  Sat Jan 9 14:50:53 2021 TUN/TAP device tun0 opened
  Sat Jan 9 14:50:53 2021 /sbin/ip link set dev tun0 up mtu 1500
  Sat Jan 9 14:50:53 2021 /sbin/ip addr add dev tun0 local 10.0.0.2 peer 10.0.0.1
  Sat Jan 9 14:50:53 2021 TCP/UDP: Preserving recently used remote address:
  [AF_INET]192.168.122.52:1194
  Sat Jan 9 14:50:53 2021 UDP link local (bound): [AF_INET][undef]:1194
  Sat Jan 9 14:50:53 2021 UDP link remote: [AF_INET]192.168.122.52:1194
  Sat Jan 9 14:51:03 2021 Peer Connection Initiated with
  [AF_INET]192.168.122.52:1194
  Sat Jan 9 14:51:04 2021 WARNING: this configuration may cache passwords in
  memory -- use the auth-nocache option to prevent this
  Sat Jan 9 14:51:04 2021 Initialization Sequence Completed
```

You have a successful connection when both hosts show the “Initialization Sequence
Completed” message. Test your connections by pinging through the _tun0_ interface on
both hosts:

**13.2 Setting Up a Simple Connection Test** **|** **301**

```
  [madmax@host1 ~]$ ping -I tun0 10.0.0.2
  PING 10.0.0.2 (10.0.0.2) from 10.0.0.1 tun0: 56(84) bytes of data.
  64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=0.515 ms
  64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.436 ms

  [stash@host2 ~]$ ping -I tun0 10.0.0.1
  PING 10.0.0.1 (10.0.0.1) from 10.0.0.2 tun0: 56(84) bytes of data.
  64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=0.592 ms
  64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=0.534 ms
```

Press Ctrl-C on each host to stop ping, and again to close the tunnels.

**Discussion**

This simple test illustrates how OpenVPN works. It creates a virtual network inter‐
face, _tun0_ on both hosts, then routes network traffic through this interface. This sim‐
ple test does not create an encrypted connection, as you can see from the “*******
WARNING *******: All encryption and authentication features disabled” message in
your command output.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - [systemd.unit](https://oreil.ly/2AAEe)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.3 Setting Up Easy Encryption with Static Keys**

**Problem**

You want an easy way to create and manage encryption for OpenVPN.

**Solution**

The easiest method is to use shared static keys. Shared static keys are useful for test‐
ing, but they are not adequate for production systems. (See the Discussion to learn
about their shortcomings.) In this recipe you will learn how to create and share static
keys, and how to create simple server and client configuration files.

**302** **|** **Chapter 13: Secure Remote Access with OpenVPN**

Follow these steps:

1. Create and distribute a shared static key between two hosts.

2. Create server and client configuration files.

3. Start OpenVPN on both hosts, referencing their configuration files.

In the following examples, the OpenVPN server is on _server1_, the client is _client1_, and
the new key is _myvpn.key_ . You may name your keys whatever you want.

Create a new directory on the OpenVPN server to store keys, then create a new static
key:

```
  $ sudo mkdir /etc/openvpn/keys
  $ sudo openvpn --genkey --secret myvpn.key
```

Copy the key to the client machine:

```
  $ scp myvpn.key client1:/etc/openvpn/keys/
  Password:
  myvpn.key             100% 636  142.7KB/s  00:00
```

Create the server configuration file. The example is _/etc/openvpn/server1.conf_, and
you can call yours anything you like. Use a different subnet for your OpenVPN tun‐
nel; for example, _server1_ and _client1_ are on 192.168.43.0/24, so the example uses the
10.0.0.0/24 private address space for the VPN tunnel. The server’s _tun_ address is
10.0.0.1:

```
  # server1.conf
  dev tun
  ifconfig 10.0.0.1 10.0.0.2
  secret /etc/openvpn/keys/myvpn.key
  local 192.168.43.184
```

_local_ is the LAN IP address of the server.

Create the client configuration file on the client machine. The client’s _tun_ address is
10.0.0.2:

```
  # client1.conf
  dev tun
  ifconfig 10.0.0.2 10.0.0.1
  secret /etc/openvpn/keys/myvpn.key
  remote 192.168.43.184
```

Make sure the OpenVPN daemon is not running on the server or client:

```
  $ sudo systemctl stop openvpn
```

Start OpenVPN on the server and client:

```
  [server1 ~] $ sudo openvpn /etc/openvpn/server1.conf

  [client1 ~] $ sudo openvpn /etc/openvpn/client1.conf

```

**13.3 Setting Up Easy Encryption with Static Keys** **|** **303**

When you see “Initialization Sequence Completed” on both hosts, you have estab‐
lished a connection. Ping each host over the _tun_ virtual network interface:

```
  [server1 ~] $ ping -I tun0 10.0.0.1
  [client1 ~] $ ping -I tun0 10.0.0.2
```

Press Ctrl-C on both hosts to close the connection.

**Discussion**

If you see “WARNING: INSECURE cipher with block size less than 128 bit (64 bit).
This allows attacks like SWEET32. Mitigate by using a cipher with a larger block size
(e.g. AES-256-CBC)” in your command output, correct it with the following entry in
both the server and client configuration files:

```
  cipher AES-256-CBC
```

The biggest problem with using static keys is that you lose perfect forward secrecy
because your static key never changes. If an attacker found a way to sniff and capture
your network traffic, and then captured and cracked your encryption key, the
attacker could then decrypt everything they capture, past and future. OpenVPN’s PKI
uses a complex process that generates session keys, which are not persistent but
change regularly. So, at best, a successful attacker can decrypt one session’s worth of
traffic at a time, and then has to start over.

Another drawback is you need a different key for each client, and a copy of each cli‐
ent key on the server. Managing multiple clients is less work and more secure with a
proper PKI.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - [systemd.unit](https://oreil.ly/2AAEe)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.4 Installing EasyRSA to Manage Your PKI**

**Problem**

You are going to use EasyRSA to create and manage your public key infrastructure
(PKI), and you want to install and set it up correctly.

**304** **|** **Chapter 13: Secure Remote Access with OpenVPN**

**Solution**

Your PKI can be anywhere, it does not have to be on the OpenVPN server. You will
create server and client certificates on the PKI, then copy them to their respective
hosts.

You can install the _easy-rsa_ [package or fetch the freshest release from EasyRSA Relea‐](https://oreil.ly/LtAKu)
[ses on GitHub.](https://oreil.ly/LtAKu)

Fedora and Ubuntu stuff all the EasyRSA files into _/usr/share/_ . This is not a good
working directory, and it is overwritten by system updates. Create a new directory
that you control and does not need root permissions, like our fine example user
Duchess who creates _/home/duchess/mypki_ :

```
  ~$ mkdir mypki
```

On Fedora and Ubuntu Linux, copy the _/usr/share/easy-rsa_ directory to your new
directory:

```
  ~$ sudo cp -r /usr/share/easy-rsa mypki
```

This creates _mypki/easyrsa_ . Check your permissions; you should be the owner and
group owner of everything in your directory.

openSUSE does a proper installation with configuration files in _/etc/easy-rsa_, the _easy‐_
_rsa_ command in _/usr/bin_, and the documentation and license files in _/usr/share/_ . You
don’t have to move anything or worry about permissions.

**Discussion**

You should not need root permissions to create and manage your PKI. You may put it
wherever you want, and it should be separate from your OpenVPN configuration,
either in a separate directory or on a separate machine. The good OpenVPN people
recommend putting it on a well-protected machine that is not exposed to the
internet.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - [systemd.unit](https://oreil.ly/2AAEe)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.4 Installing EasyRSA to Manage Your PKI** **|** **305**

**13.5 Creating a PKI**

**Problem**

You installed EasyRSA (Recipe 13.4), and now you want to know how to set up a
proper public key infrastructure (PKI).

**Solution**

A proper PKI is essential to running an OpenVPN server safely. In this recipe we will
use EasyRSA to create a PKI, which simplifies the process considerably over using the
_openssl_ command. Creating a PKI involves these steps:

1. Create your own Certificate Authority (CA) certificate to sign server and client
certificates. This should be in a separate directory from your OpenVPN server
configuration, or on a separate machine.

2. Create and sign an OpenVPN server certificate.

3. Create and sign client certificates.

4. Copy the server certificates and the client certificates to _/etc/openvpn/keys_ on
their respective machines. (You may create a different directory than _keys_ .)

In the following examples, all the commands are run from the _/home/duchess/mypki/_
directory.

Change to your PKI directory and run the command to initiate a new PKI:

```
  ~$ cd mypki
  ~/mypki $ easyrsa init-pki

  init-pki complete; you may now create a CA or requests.
  Your newly created PKI dir is: /home/duchess/mypki/pki
```

This creates an empty structure for your new PKI. Next, build your new CA. The CA
creates and signs server and client certificates. Protect it with a strong passphrase, and
create the Common Name you want for your new CA:

```
  ~/mypki $ easyrsa build-ca
  [...]
  Enter New CA Key Passphrase: passphrase
  Re-Enter New CA Key Passphrase: passphrase
  [...]
  Common Name (eg: your user, host, or server name) [Easy-RSA CA]: vpnserver1
  [...]
  CA creation complete and you may now import and sign cert requests.
  Your new CA certificate file for publishing is at:
  /home/duchess/mypki/pki/ca.crt

```

**306** **|** **Chapter 13: Secure Remote Access with OpenVPN**

If you see a “RAND_load_file:Cannot open file:crypto/rand/rand‐
file.c:98:Filename=/mypki/pki/.rnd” message, ignore it, as it is
meaningless. You can make it go away by finding _openssl-_
_easyrsa.cnf_ and commenting out the _RANDFILE_ line at the begin‐
ning.

Generate a keypair and certificate signing request for your OpenVPN server. It is cus‐
tomary to not put a passphrase on the server’s private key. You may protect yours
with a passphrase if you wish by omitting the _nopass_ option. A passphrase provides
strong protection, but it means entering the passphrase every time you restart your
server:

```
  ~/mypki $ easyrsa gen-req vpnserver1 nopass

  Using SSL: openssl OpenSSL 1.1.1d 10 Sep 2019
  Generating a RSA private key
  .............................+++++
  ................................................................++++++
  writing new private key to '/home/duchess/mypki/pki/private/vpnserver1.key.NYjr5y
  c9kj'
  [...]
  Common Name (eg: your user, host, or server name) [ vpnserver1 ]:

  Keypair and certificate request completed. Your files are:
  req: /home/duchess/mypki/pki/reqs/vpnserver1.req
  key: /home/duchess/mypki/pki/private/vpnserver1.key
```

Generate a keypair and certificate signing request for a client. Client private keys
should have passwords, especially on mobile clients:

```
  ~/mypki $ easyrsa gen-req vpnclient1

  Using SSL: openssl OpenSSL 1.1.1d 10 Sep 2019
  Generating a RSA private key
  ................+++++
  ....................................................................+++++
  writing new private key to '/home/duchess/mypki/pki/private/vpnclient1.key.bicpOc
  EC5S'
  Enter PEM pass phrase: passphrase
  Verifying - Enter PEM pass phrase: passphrase
  [...]
  Common Name (eg: your user, host, or server name) [ vpnclient1 ]:

  Keypair and certificate request completed. Your files are:
  req: /home/duchess/mypki/pki/reqs/vpnclient1.req
  key: /home/duchess/mypki/pki/private/vpnclient1.key
```

Sign the requests, using their Common Names. Use only their names; if you enter
their paths it will cause an error:

```
  ~/mypki $ easyrsa sign-req server vpnserver1
  Using SSL: openssl OpenSSL 1.1.1d 10 Sep 2019

```

**13.5 Creating a PKI** **|** **307**

```
  You are about to sign the following certificate.
  Please check over the details shown below for accuracy. Note that this request
  has not been cryptographically verified. Please be sure it came from a trusted
  source or that you have verified the request checksum with the sender.

  Request subject, to be signed as a server certificate for 1080 days:

  subject=
  commonName        = vpnserver1

  Type the word 'yes' to continue, or any other input to abort.
  Confirm request details: yes
  Using configuration from /home/duchess/mypki/pki/safessl-easyrsa.cnf
  Enter pass phrase for /home/duchess/mypki/pki/private/ca.key:
  Check that the request matches the signature
  Signature ok
  The Subject's Distinguished Name is as follows
  commonName      :ASN.1 12:'vpnserver1'
  Certificate is to be certified until Jan 27 20:09:12 2024 GMT (1080 days)

  Write out database with 1 new entries
  Data Base Updated

  Certificate created at: /home/duchess/mypki/pki/issued/vpnserver1.crt

  mypki $ easyrsa sign-req client vpnclient1
  [...]
  Certificate created at: /home/duchess/mypki/pki/issued/vpnclient1.crt
```

Generate the Diffie-Hellman parameters for the server; this takes a minute or two.
This command must be run on your OpenVPN server:

```
  $ easyrsa gen-dh
  Using SSL: openssl OpenSSL 1.1.1d 10 Sep 2019
  Generating DH parameters, 2048 bit long safe prime, generator 2
  This is going to take a long time
  ...........................................+...........
  ..........+............................................
  [...]
  DH parameters of size 2048 created at /home/duchess/mypki/pki/dh.pem
```

Create a Hash-based Message Authentication Code (HMAC) key, also on your server:

```
  $ openvpn --genkey --secret ta.key
```

Copy _vpnclient1.key_, _vpnclient1.crt_, _ca.crt_, and _ta.key_ to _/etc/openvpn/keys_ on _client1_ .

Copy _vpnserver1.key_, _vpnserver1.crt_, _ca.crt_, _dh.pem_, and _ta.key_ to _/etc/openvpn/keys_
on _server1_ .

You may delete all of the _*.req_ files after you have signed the certificate signing
requests.

**308** **|** **Chapter 13: Secure Remote Access with OpenVPN**

Table 13-1 should help you remember which files go where.

_Table 13-1. Server and client key location_

**<mark>Name</mark>** **<mark>Location</mark>** **<mark>Public</mark>** **<mark>Private</mark>**
ca.crt server & clients X

ca.key PKI machine X

ta.key server & clients X

dh.pem server X

server.crt server X

server.key server X

client1.crt client1 X

client1.key client1 X

client2.crt client2 X

client2.key client2 X

**Discussion**

What’s this Diffie-Hellman stuff? It is the encryption mechanism that allows two
hosts to create and share a secret key. Once the OpenVPN client and server authenti‐
cate to each other, additional send and receive keys are generated to encrypt the
session.

HMAC calculates a message authentication code. HMAC verifies the integrity and
authenticity of a message.

_easyrsa init-pki_ creates a new PKI, and you may also run it to cleanly remove and
rebuild an existing PKI.

You may set up your PKI anywhere, and the good OpenVPN people recommend
putting it on a machine that is not exposed to the internet and is well-protected from
anyone who should not be messing with your PKI. If your CA is compromised, it is
easy for an attacker to infiltrate your network. Obviously, you must have a secure
method of distributing these files: USB stick, the _scp_ command, an encrypted tarball
downloaded from a secure server or emailed to your users.

Take a look in your PKI directory to see how all these items are organized.

```
  ~/mypki $ ls */*
  pki/ca.crt        pki/index.txt      pki/index.txt.old
  pki/serial        pki/dh.pem        pki/index.txt.attr
  pki/openssl-easyrsa.cnf pki/serial.old      pki/extensions.temp
  pki/index.txt.attr.old  pki/safessl-easyrsa.cnf pki/ta.key

  pki/certs_by_serial:
  4954C26DB44106B20F1B9DA17CE515E5.pem DA68CBE53E30923C9BCC3B9F1C5C9011.pem

```

**13.5 Creating a PKI** **|** **309**

```
  pki/issued:
  vpnclient1.crt vpnserver1.crt

  pki/private:
  ca.key vpnclient1.key vpnserver1.key

  pki/renewed:
  certs_by_serial private_by_serial reqs_by_serial

  pki/reqs:
  vpnclient1.req vpnserver1.req

  pki/revoked:
  certs_by_serial private_by_serial reqs_by_serial
```

Signing requests have a _.req_ file extension, public keys _.crt_, and private keys _.key_ . Keys
always come in pairs, public and private.

**Public Keys Encrypt, Private Keys Decrypt**

Public keys encrypt, private keys decrypt. Private keys must be pro‐
tected and never shared. Public keys are meant to be shared.

Click on any signed certificate in your file manager to see something like Figure 13-1.
This provides a wealth of information: the CA that signed it, expiration date, serial
number, fingerprint, signature, and lots more.

_Figure 13-1. Viewing a signed certificate_

**310** **|** **Chapter 13: Secure Remote Access with OpenVPN**

Or use the _openssl_ command to read it:

```
  $ openssl x509 -noout -text -in vpnserver1.crt
```

A certificate is a request signed by a CA, and it contains the public key and the CA’s
digital signature. A request contains a public key and the digital signature from the
corresponding private key. You can see all of this by comparing them.

EasyRSA was originally part of OpenVPN and then spun off as a separate project. If
you are used to managing PKIs with OpenSSL, you will appreciate how EasyRSA has
streamlined the process.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.6 Customizing EasyRSA Default Options**

**Problem**

The default settings for EasyRSA are not what you want, and you want to know how
to change them.

**Solution**

Look for your _vars.example_ file, which is part of EasyRSA. Save a copy of this file as
_vars_ in your PKI directory, which in the examples in this chapter is _/home/duchess/_
_mypki/pki/_ . The _vars_ file defines your default settings for creating and signing certifi‐
cates.

This file is well commented. Make your edits below the `# DO YOUR EDITS BELOW`
`THIS POINT` line. Everything prefaced with _set_var_ is editable. Uncomment every‐
thing you change.

For example, the default configuration uses just the Common Name, and not a full
_org_ configuration. The following example creates a traditional _org_ configuration:

```
  set_var EASYRSA_DN   "org"

  set_var EASYRSA_REQ_COUNTRY  " US "
  set_var EASYRSA_REQ_PROVINCE  " Oregon "
  set_var EASYRSA_REQ_CITY    " Walla Walla "

```

**13.6 Customizing EasyRSA Default Options** **|** **311**

```
  set_var EASYRSA_REQ_ORG    " MyCo "
  set_var EASYRSA_REQ_EMAIL   " me@example.com "
  set_var EASYRSA_REQ_OU     " MyOU "
```

When you use the _org_ configuration, remember to enter your Common Name when
you run _easyrsa build-ca_, or you will be stuck with the default _Easy-RSA CA_ :

```
  Common Name (eg: your user, host, or server name) [Easy-RSA CA]: myCN
```

**Discussion**

Use _cn_ or _org_ according to your own policies and preferences; it makes no difference
to your server operations.

See Recipe 13.10 to learn how to harden your server.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.7 Creating and Testing Server and**
**Client Configurations**

**Problem**

Now that you have a nice stout PKI, you want to know how to configure your
OpenVPN server and clients.

**Solution**

In this recipe we will set up a simple test instance between two hosts on the same sub‐
net, _server1_ and _client1_ . This is a good simple way to test your server configuration
without having to hassle with routing and getting past your internet gateway.

The following example is a simple OpenVPN server configuration. Note that you can
store your server keys anywhere on the server, as long you reference them correctly in
your configuration file:

```
  # vpnserver1.conf
  port 1194
  proto udp
  dev tun
  user nobody
  group nobody

```

**312** **|** **Chapter 13: Secure Remote Access with OpenVPN**

```
  ca /etc/openvpn/keys/ca.crt
  cert /etc/openvpn/keys/ vpnserver1.crt
  key /etc/openvpn/keys/ vpnserver1.key
  dh /etc/openvpn/keys/dh.pem
  tls-auth /etc/openvpn/keys/ta.key 0

  server 10.10.0.0 255.255.255.0
  ifconfig-pool-persist ipp.txt
  keepalive 10 120
  persist-key
  persist-tun
  tls-server
  remote-cert-tls client

  status openvpn-status.log
  verb 4
  mute 20
  explicit-exit-notify 1
```

An example client configuration:

```
  # vpnclient1.conf
  client
  dev tun
  proto udp
  remote server1 1194

  persist-key
  persist-tun
  resolv-retry infinite
  nobind

  user nobody
  group nobody
  tls-client
  remote-cert-tls server
  verb 4

  ca /etc/openvpn/keys/ca.crt
  cert /etc/openvpn/keys/ vpnclient1.crt
  key /etc/openvpn/keys/ vpnclient1.key
  tls-auth /etc/openvpn/keys/ta.key 1
```

Stop your OpenVPN server if it is running:

```
  $ sudo systemctl stop openvpn@.openvpn1.service
```

Start OpenVPN on both hosts with the _openvpn_ command:

```
  $ sudo openvpn /etc/openvpn/vpnserver1.conf
  Tue Feb 16 16:50:49 2021 us=265445 Current Parameter Settings:
  Tue Feb 16 16:50:49 2021 us=265481  config = '/etc/openvpn/vpnserver1.conf'

```

**13.7 Creating and Testing Server and Client Configurations** **|** **313**

```
  [...]
  Tue Feb 16 16:50:49 2021 us=270212 Initialization Sequence Completed

  $ sudo openvpn /etc/openvpn/vpnclient1.conf
  Tue Feb 16 16:56:22 2021 OpenVPN 2.4.3 x86_64-suse-linux-gnu [SSL (OpenSSL)]
  [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Jun 20 2017
  Tue Feb 16 16:56:22 2021 library versions: OpenSSL 1.1.1d 10 Sep 2019, LZO 2.10
  Enter Private Key Password: *******
  [...]
  Tue Feb 16 16:56:26 2021 Initialization Sequence Completed
```

And there you have it, both configurations are correct and you have a successful con‐
nection. Press Ctrl-C on both hosts to stop.

**Discussion**

OpenVPN installs with a batch of example configurations in _/usr/share/doc/openvpn/_ .
These are abundantly commented and are excellent references. There are dozens of
options, but in real life you will use just a few of them. In the examples in this recipe,
there are a few items of note.

`port 1194` is the default port, and `proto udp` is preferred over `proto tcp` . UDP is
more secure, providing some protection from port scanning and denial-of-service
attacks, and provides higher throughput and lower latency. TCP is useful when a
remote user uses public networks with restrictive firewalls, such as hotels and coffee
shops.

_tls-auth /etc/openvpn/keys/ta.key_ must always have the 0 value on the server, and 1 on
the clients. _tls-auth_ enforces TLS-only connections.

_verb 4_ is the logging level. 1 is the lowest, 9 is the most verbose. Keep it at 4–6 until
you are confident everything is set up correctly. When you start OpenVPN from the
command line, you will see a lot of messages.

There are a lot of stale how-tos that recommend the _comp_lzo_ option to enable com‐
pression. Don’t bother, as it does not provide much benefit. Most traffic is not com‐
pressible since it is either already compressed or is encrypted and cannot be com‐
pressed. There is at least one vulnerability enabled by compression, VORACLE.

**See Also**

 - The example configuration files in your installation

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**314** **|** **Chapter 13: Secure Remote Access with OpenVPN**

**13.8 Controlling OpenVPN with systemctl**

**Problem**

You want to manage the OpenVPN daemon like any other daemon, with _systemctl_,
but you don’t see an OpenVPN unit file. Or, you see an odd-looking unit file like
_openvpn-server@.service_, and when you try to start it, it throws error messages.

**Solution**

The ampersand, @, creates a _parameterized_ unit file. This means you can easily create
multiple unit files for the same service by calling different configuration files. For
example, suppose your server configuration file is _/etc/openvpn/austin.conf_ . Your unit
file is _openvpn@austin.service_, created with _systemctl_ :

```
  $ sudo systemctl enable openvpn@austin
  Created symlink /etc/systemd/system/multi-user.target.wants/openvpn@austin.service
  → /usr/lib/systemd/system/openvpn@.service.
  Created symlink /etc/systemd/system/openvpn.target.wants/openvpn@austin.service
  → /usr/lib/systemd/system/openvpn@.service.
```

Note that you do not type the file extension of your OpenVPN _.conf_ file. Now you can
control your OpenVPN daemon with _systemctl_, just like any other service.

**Discussion**

This is a rather ingenious method that gives you the flexibility to create multiple con‐
figurations without having to write multiple unit files. You can “parameterize” any
systemd unit file.

You can have multiple tunnels running at the same time on the same machine. Each
configuration requires a different _tun_ device, for example _tun0_, _tun1_, _tun2_, a different
subnet for each tunnel, and a different UDP port. Control all of these tunnels with
different configuration files and their corresponding parameterized unit files.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - [systemd.unit](https://oreil.ly/2AAEe)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.8 Controlling OpenVPN with systemctl** **|** **315**

**13.9 Distributing Client Configurations More Easily**
**with .ovpn Files**

**Problem**

Setting up clients is a fair bit of work, and you want to know if there is a faster way,
one that your users can do themselves without a lot of help.

**Solution**

Bundle your client configurations and keys into single files with the _.ovpn_ extension.
All clients, Linux, Windows, macOS, iOS, and Android, can import these.

First create the users’ certificates, then follow this template to create their _.ovpn_ files.
This example builds on the example in Recipe 13.7. Instead of linking to all their cer‐
tificates, copy them into this file. All certificates are in plain text, so all you do is copy
the BEGIN/END portions into the _.ovpn_ file:

```
  # vpnclient1.ovpn
  client
  dev tun
  proto udp
  remote server2 1194

  persist-key
  persist-tun
  resolv-retry infinite
  nobind

  user nobody
  group nobody
  tls-client
  remote-cert-tls server
  verb 4

  # ca.crt
  <ca>
  -----BEGIN CERTIFICATE----  MIIDSDCCAjCgAwIBAgIUD2UxdEwgvhhr0zq5fAxIDIueB2EwDQYJKoZIhvcNAQEL
  BQAwFTETMBEGA1UEAwwKdnBuc2VydmVyMTAeFw0yMTAyMjExODU1MjNaFw0zMTAy
  MTkxODU1MjNaMBUxEzARBgNVBAMMCnZwbnNlcnZlcjEwggEiMA0GCSqGSIb3DQEB
  AQUAA4IBDwAwggEKAoIBAQDpQJo+Izt8v0zriSWwrChc1tnVj3E3h3XuyEHub7hj
  y4bMu2PqKByFNr+iikEF3u0d6HrCRSDKt1BcLzL3TsTJ/hJBHAlTyqEgVce1knjL
  2g9NnDbekRtJSJCxS9j+RWtP43Xdg5edb5hTCZqdNFHD8oNuSMGFBbHN4oi9eDXl
  rvyVHJe+UkI1Ow6mW0+ln/IoKNFPovz+l+ds3fJ5+UHe2TaQPQc7tGZ33j7wfJQd
  es8baFdK+lnmGdUOrW9BQE6ReMSezkz6dKdIZdy7jEs6xoflOzyWlgydmnkAvLnx
  MBQDgDUbc5MuooVMAWa4yhtz0B9ZmdJDb8jzHDpTPqdRAgMBAAGjgY8wgYwwHQYD
  VR0OBBYEFF8KPhl1xxV0110JiBs5iUEPoJ1IMFAGA1UdIwRJMEeAFF8KPhl1xxV0
  110JiBs5iUEPoJ1IoRmkFzAVMRMwEQYDVQQDDAp2cG5zZXJ2ZXIxghQPZTF0TCC+

```

**316** **|** **Chapter 13: Secure Remote Access with OpenVPN**

```
GGvTOrl8DEgMi54HYTAMBgNVHRMEBTADAQH/MAsGA1UdDwQEAwIBBjANBgkqhkiG
9w0BAQsFAAOCAQEAMnRLz3CBApSrjfUKsWYioNGQGvh77Smh/1hPGIu4eEldQSmZ
Aj7qclEaORdBxmqrVtA3Z9cX1L0xFrg14nLyddmuWHG3ZChc5ZMpYtD2YpOH265B
FFjDp96vK13dpixWKrVpvakLCCA4EvnC8CEjbm0oNFiCgSwKAoJFCcUzwC33swsU
B2w5/iT6CZKuKhSmET1IDpG8krGC/Ib2GNAS0szMI94P0ajZgVznMcXOJ7gUg4rM
sEB8OzM6GBEZTqbAa9uVMZnOZvZA5jGIbBuelUo0bqGdAyx2B68zzuL//qvsHsvw
kZCyKIaXH0NBV7vexMKWcwFLLBzWizFQbbFpFA==
-----END CERTIFICATE----</ca>

# vpnclient1.cert
<cert>
-----BEGIN CERTIFICATE----MIIDVjCCAj6gAwIBAgIQLhO4FTrqN5WZiQETULAwnzANBgkqhkiG9w0BAQsFADAV
MRMwEQYDVQQDDAp2cG5zZXJ2ZXIxMB4XDTIxMDIyMTE4NTYzM1oXDTI0MDIwNjE4
NTYzM1owFTETMBEGA1UEAwwKdnBuY2xpZW50MTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBALUFYXwk6JW/hRtoMs0Ug5jMcWXsjMUsCz8L8CeXNOs3wQrf
YBWF1TYCLPd2/vwXsvbqCE85IZwjsJ5mEx9YgQ5M1teDkLZqBn8y7VIyDAAU8RsN
NcrnpeMDV0LgZIBeUrHi4ZTooaw4FdJ5BBYRHR1APVaaHDWx59ohJuBDpriWhvWk
lWX0rpSJltXriIOCzky/yEwfw6ah5jWaTgfe41fXq8j3lx2IbgIL7I4//jhC6JYz
N7huTdT2uB2MUbYX0XWBffMG8wcBZtMI2XryZmPvFYWP7N5nZZsBXkLz/UngAu3k
jkYJOnJy/hdOFLN/yXj7VFydmivUSeekdjjxyAECAwEAAaOBoTCBnjAJBgNVHRME
AjAAMB0GA1UdDgQWBBSnLIQoTPLyECbJHfgYBHvQpcmfgzBQBgNVHSMESTBHgBRf
Cj4ZdccVdNddCYgbOYlBD6CdSKEZpBcwFTETMBEGA1UEAwwKdnBuc2VydmVyMYIU
D2UxdEwgvhhr0zq5fAxIDIueB2EwEwYDVR0lBAwwCgYIKwYBBQUHAwIwCwYDVR0P
BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQBaBpYZXVYUzOcXOVSaijmOZAIVBTeJ
meQz9xBQjqDXaRvypWlQ1gQtO8WnK9ruafc1g/h7LtvqtiALnGiJ0NbshkH8C1KE
yen46UCau5B/Xi0gA7FoPildvYdKSn/jI6KySCsplubjnJK9H/6DjAcEuqFLcsaY
5vpKQGP9Vl7H7hEVs4f1aory1T4Ma/bdXEOqgzHmIARLmxYeJm90sUT/n7e7VXfy
fILZ+8D1fMxCbeQRBkg1e8wJfgEbMRY9aGGt1qAs9gkm9RPelGB18v4iCbyebv3X
4hVHmfjcixdbWiABC7yq/gisooQ0robW/92dgemcwO0awHZX+opNBgwr
-----END CERTIFICATE----</cert>

# vpnclient1.key
<key>
-----BEGIN ENCRYPTED PRIVATE KEY----MIIFHDBOBgkqhkiG9w0BBQ0wQTApBgkqhkiG9w0BBQwwHAQInjFvz5a4mY8CAggA
MAwGCCqGSIb3DQIJBQAwFAYIKoZIhvcNAwcECNsxQXxvMpN0BIIEyEZdgFwPnGup
vyhywXR6l6ihvHK2GRczIgH0mFIiwQDgDjZj2YsEnvSA/P3MHplkU/bgv9DJ5j2T
C5wPDmGN4yG1boHx9BQKbXqxGwdz/UcHwmNKur9qnSFrSVEvMDwvum+rmzWuKykf
gkKKBCT1JZ2DWKtjjDNYG9qhBn3S2zYVq311dDuLbBcruvo1UL031sDDYWTpVuuf
zZc0ozng0Nzb35bNkG6Ib+LYLzJi4stxzw0DTFl52lKv++R6xhmqb81IJE3vBs4H
DOutkYfifO1eGqEKksPQRl8n03UVkOtB5pH8VdQeLqEBBaq3qeIfU6FkH9XrPR/E
8VOg9BNpbyuUW7bQu0MzuJ8Ofkjy9K+HHdwFtGPyOatkeaXT/qcKVMvzWcbr8bPc
VncavzXdzo0Sb8FigsKYU1lNjgo00Phd3m0AOfptrweK6ucBds5SmqNrUFXiQ2JA
Ms3LUw4CXBBgvdu5TsA2xLGysip0RPKLyTnUPGnXxbBaaHMv8Jz3XRCrWgZbtAE3
XhE9fKw+ZMEP+2jpC/1mjN/N9VuJfYZEhgA84wzYMu6pt3zPkWZqR6yGTDFEDhvh
OAZYEpqrhe++nxDpuQlpCCl4IndSg9L9oX1ydrvPNHGbRVztd3+r9wr4Ub3fJ1g/
9ckCdanohEymKbjw34HEMmdx+fn5k2T9bLnl8fsYtcESkg04ChON3yOnZFKl6chT
BQ9X2Qmeg7FoawWiUY5o+7OHNKL7QpRt4jXPbXNuXFK9EYvuRzUqubLhL5DdmjuO
Se1vvZg7fT4C8qjYsoCa18idA00EN3ePFFf9AssHCoVW92GiUTTKG+qURCjtNtG6

```

**13.9 Distributing Client Configurations More Easily with .ovpn Files** **|** **317**

```
  dnPvxiSf98OBkkjeX3ni0cKdfMGoQTSdEy5GexvfRMF5HJrGO+CWXmqSBsuIlPUe
  quqCsPmpaT2Ws/0UU9cKe4qaKjTL7CghtFmUEhH7t6Cd41Ki9gKi33j3541l9w7l
  J1bgca4rRUCecp2BPF3IjJc/RnTvHkbUK4mDX9s8xJhYf9WE6JYsk3NBSNNIj/9G
  FMJlo71x8H3OAdFzRN5bjV797HByZ+YidZIgGAx2dSko3PQPy7RSxdmzFbxfUvzj
  9jcYEu+V9unbtDK2qZ9I+LqXGE+EXjPBui40IWp8XIYNlSLn2qgroH079lXhXKBY
  +DzcBzyT7GTX2QeYE+yqqPRIFWHnbnsnD6dMnAa46h+Si+f5sq33rfRsF7UpK4gV
  IhzFkncCM47/Taqi0OY04Q40LuSCDjmjFL+VzZOsAtWGRNYNzIgniThEehElJwfI
  ErzClcVptjhtCer8BPuO7YaMIHk1hKecHFqw3RrimWzroL1iu9Q29m2oM+bVc6mD
  we6r+t8JbaAFxoHBK4i6M0rcdJPICxDTIOjPC3Fg/MeqiCi7F0DFZvXwPGRD+0Of
  MBnsDplEUjK06jbE5BjGQ7n7P+dwDxyp/aVO4CfX7ZOco6h9r3b6nqlzPVNE9erw
  kS7WwT/TWraw/sfIO9sNSgle7PoRh2s/w/oGVhC6ymlMdXe+mhMzHFnGEbBRh2Rd
  kd/EdYNubHg0k9+RLTwbgwZ+176cIJyOpqaoJGv0bsKM8X26Pk/fkyF6xgdQYQOx
  8i9Whea8OjUOQAcgc7gUyA==
  -----END ENCRYPTED PRIVATE KEY----  </key>

  # ta.key
  <tls-auth>
  -----BEGIN OpenVPN Static key V1----  4eb35b44d1d8a82cfa51af394d4f58f3
  69bf8fe8c0a0a032f38b0ee104889628
  8a5dc89486736b39d64ad3c6831bf9ba
  9f3f96c3307d322a5bf055b9bc3bfa74
  929faf361c14de97445f5927794264bb
  e3f71c925f2236cfb0109ecfd6406cef
  857dfb39783a09ecd56d3cf09ebbc853
  0f43b1c787f0db99dbecabcd2090cfbb
  54c86d8102a5430fd6a7f37ab5ce8ed9
  f6bec8984bde4267f78913ff702dd396
  a205b6be9e7ab41cf1ebad3953c27c7c
  f3b435345e02aede049ef7c9f1c2704f
  2ed91110ccb19d0d3bd46a00f54c73e2
  07b31160cdc54c3f5a7989bb999ac5f3
  89c6de7e79fc93399924a8d298eab462
  231234e690c319d5cbd832788f0dbcfb
  -----END OpenVPN Static key V1----  </tls-auth>
```

Now you have only one file to distribute to your clients. (See Recipe 13.1 to learn
what to install for Linux, macOS, Windows, iOS, and Android clients.)

The easy way to import a new _.ovpn_ file in Linux is using NetworkManager. Open
“VPN Connections” → “Add a VPN connection.” This opens “Choose a VPN Con‐
nection Type.” Select “Import a Saved VPN Connection,” click Create, and find
your _.ovpn_ file in the file selector. Review the settings on the General and VPN tabs.

On the General tab, make sure that “All users may connect to this network” is not
checked. This is a simple but important security measure that requires every user to
have their own individual OpenVPN configuration.

**318** **|** **Chapter 13: Secure Remote Access with OpenVPN**

On the VPN tab, note that NetworkManager converts the inline certificates to _.pem_
files (Figure 13-2). This is normal and not a mistake. You can compare these to the
originals; click on the little file folder icon to the right to see where the converted files
are stored.

_Figure 13-2. Importing the .ovpn client configuration file into NetworkManager_

For all other clients, the procedure is similar. Follow their instructions, and if all goes
well, your clients will be up and running in a couple of minutes.

The NetworkManager import function also works with client configuration files that
are not inline, like in Recipe 13.7. In this case the certificates are not converted, and
they retain their original filenames.

An inline file may have the _.conf_ extension if you have only Linux clients.

**13.9 Distributing Client Configurations More Easily with .ovpn Files** **|** **319**

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.10 Hardening Your OpenVPN Server**

**Problem**

You want to know some options for making your OpenVPN more secure.

**Solution**

The OpenVPN default settings are pretty good, but they’re designed for broader com‐
patibility. There are some changes you can make that will make your server stronger.

The following examples go in both server and client configuration files. These
options maximize the effectiveness of TLS. All SSL and TLS protocols older than TLS
1.2 are deprecated and should not be allowed. Accept only TLS 1.2 or higher:

```
  tls-version-min 1.2
  tls-version-max 1.3 or-highest
```

Use a stronger data channel cipher, and enforce its use by disabling cipher negotia‐
tion:

```
  AES-128-GCM
  ncp-disable
```

There are many changes in TLS 1.3, so you need two different configurations for TLS
1.2 and 1.3. These are all stronger and more efficient encryption ciphers:

```
  # TLS 1.3
  tls-ciphersuites TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256
  # TLS 1.2
  tls-cipher TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256:TLS-ECDHE-RSA  WITH-CHACHA20-POLY1305-SHA256:TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256:
  TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256
```

Use Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) in place of our old DiffieHellman static keys. You do not have to create a _ta.key_, as you do in Recipe 13.5:

```
  dh none
  ecdh-curve secp384r1
  # use tls-server on the server, tls-client on the client
  tls-server

```

**320** **|** **Chapter 13: Secure Remote Access with OpenVPN**

Add the _float_ option, in the server configuration only, to allow clients to roam on dif‐
ferent networks without losing connection, as long they pass all other authentication
tests.

The _opt-verify_ option, in the server configuration only, checks for compatibility
between server and client settings, and disconnects clients that do not match. _opt-_
_verify_ checks _dev-type, link-mtu, tun-mtu, proto, ifconfig, comp-lzo, fragment, keydir,_
_cipher, auth, keysize, secret, no-replay, no-iv, tls-auth, key-method, tls-server_, and
_tls-client_ .

See the Discussion for complete example configurations.

**Discussion**

Put these enhancements all together in the server configuration:

```
  # vpnserver1.conf
  port 1194
  proto udp
  dev tun
  user nobody
  group nobody

  ca /etc/openvpn/keys/ca.crt
  cert /etc/openvpn/keys/ vpnserver1.crt
  key /etc/openvpn/keys/ vpnserver1.key

  server 10.10.0.0 255.255.255.0
  ifconfig-pool-persist ipp.txt
  keepalive 10 120
  persist-key
  persist-tun
  tls-server

  remote-cert-tls client
  verify-client-cert require
  tls-cert-profile preferred
  tls-version-min 1.2
  tls-version-max 1.3 or-highest

  float
  opt-verify
  AES-128-GCM
  ncp-disable
  dh none
  ecdh-curve secp384r1

  # TLS 1.3
  tls-ciphersuites TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256
  # TLS 1.2
  tls-cipher TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256:TLS-ECDHE-RSA
```

**13.10 Hardening Your OpenVPN Server** **|** **321**

```
  WITH-CHACHA20-POLY1305-SHA256:TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256:
  TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256

  status openvpn-status.log
  verb 4
  mute 20
  explicit-exit-notify 1
```

An example client configuration, using the inline file format (Recipe 13.9):

```
  # vpnclient1.conf
  client
  dev tun
  proto udp
  remote server1 1194

  persist-key
  persist-tun
  resolv-retry infinite
  nobind

  user nobody
  group nobody
  tls-client
  remote-cert-tls server
  verb 4

  # Using inline keys
  # ca.crt
  <ca>
  [...]
  </ca>

  # client.crt
  <cert>
  [...]
  </cert>

  # client.key
  <key>
  [...]
  </key>

  tls-version-min 1.2
  tls-version-max 1.3 or-highest
  AES-128-GCM
  ncp-disable
  dh none
  ecdh-curve secp384r1

  # TLS 1.3 encryption settings
  tls-ciphersuites TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256
  # TLS 1.2 encryption settings

```

**322** **|** **Chapter 13: Secure Remote Access with OpenVPN**

```
  tls-cipher TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256:TLS-ECDHE-RSA-WITH  CHACHA20-POLY1305-SHA256:TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256:TLS-ECDHE-RSA  WITH-AES-128-GCM-SHA256

  status openvpn-status.log
  verb 4
  mute 20
  explicit-exit-notify 1
```

These options strengthen the authentication between client and server, and enforce
using TLS 1.2 and higher. If you’re wondering how to know which ciphers and
ciphersuites to use, I asked some experts. You can lock down your setup even tighter.
For example, disallowing users from saving passwords, adding more restrictions to
client-server authentication, using SELinux, or using a chroot. These are advanced
topics not covered here.

**See Also**

 - [EasyRSA](https://oreil.ly/eKbsg)

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

 - [OpenSSL Cookbook](https://oreil.ly/Ctm0X)

**13.11 Configuring Networking**

**Problem**

Your OpenVPN server is running, all of your connection tests work as expected, and
now you need to know how to set up your networking so that remote clients can find
your server and traffic gets routed appropriately.

**Solution**

There is no one-size-fits-all solution. Configuring your networking has to take into
account how your LAN is set up, whether you are connecting individual clients or
linking networks, IPv4, IPv6, how your internet gateway is set up, and lots more.
Consult Jan Just Keijser’s excellent _[OpenVPN Cookbook](https://learning.oreilly.com/library/view/openvpn-cookbook-/9781786463128/)_, 2nd Edition (O’Reilly), to
find the answers you need. This book covers TUN versus TAP, Windows clients, PAM
and LDAP, IPv6, routing, and site-to-site configurations.

**13.11 Configuring Networking** **|** **323**

**Discussion**

Networking is the most challenging part of running any server, especially an impor‐
tant security server. It pays to study this and take pains to get it right. The OpenVPN
documentation has a lot of good information on networking as well.

**See Also**

 - [OpenVPN documentation](https://oreil.ly/Ah124)

 - _man 8 openvpn_

**324** **|** **Chapter 13: Secure Remote Access with OpenVPN**

**<u>CHAPTER 14</u>**
#### **Building a Linux Firewall with firewalld**

This chapter covers the basics of using firewalld to build host firewalls. Individual
hosts have different requirements. For example, a server has to allow different types
of incoming connection requests, and a PC running no services does not have to
accept any connection requests. A laptop that is used to access multiple networks
needs dynamic firewall management.

**firewalld Overview**

firewalld, like all firewalls, has a very long list of capabilities. We will mainly learn
about using firewalld _zones_ to control traffic entering our systems. A zone is a con‐
tainer for a level of trust; for example, some zones allow all manner of incoming con‐
nection requests, and some are very restrictive. Each network interface on a system
may be assigned only one zone, and one zone may be assigned to multiple interfaces.

**Networking Knowledge Required**

The most important networking concepts to understand are ports,
services, TCP, UDP, port forwarding, masquerade, routing, and IP
addressing. You will understand how to configure your firewall
when you understand these. If you need some coaching on com‐
puter networking, try _Networking Fundamentals_ by Gordon Davies
(Packt Publishing), or _Networking All-in-One For Dummies_, 7th
Edition by Doug Lowe (For Dummies). If you have an [O’Reilly](https://oreil.ly/mEsNB)
[Learning Platform subscription, you will find a wealth of great](https://oreil.ly/mEsNB)
information.

**325**

The traditional Linux firewall is built with the _netfilter_ packet-filtering framework in
the Linux kernel, which filters incoming and outgoing network traffic, and _iptables_,
which is the software used to create and manage tables of rules to filter your traffic.

Times change, and iptables is being replaced by newer rules managers, such as _ufw_
(Uncomplicated Firewall), _nftables_ (Netfilter tables), and _firewalld_ (firewall daemon).
firewalld, like iptables and nftables, uses tables of rules to manage traffic filtering. It
provides both a command-line interface and a nice graphical interface, _firewall-_
_config_ . firewalld is a frontend to both iptables and nftables. nftables is a significant
improvement over iptables and is intended to be the default backend for firewalld,
but in some Linux distributions iptables is still the default. Set your preferred back‐
end in _/etc/firewalld/firewalld.conf_ with the _FirewallBackend_ option (Recipe 14.4).

firewalld comes with predefined sets of rules, called _zones_, for different use cases,
such as a machine running no services, a machine running services, and different
zones for different network interfaces on the same machine. You can edit these zones
to suit your own requirements.

firewalld zones manage _services_, which are configurations for common services such
as ssh, imaps, and rsync. Most of the predefined services include only the standard
port assignments. You may edit these as you need and create your own custom zones.

firewalld is integrated with NetworkManager, so you don’t have to worry about man‐
aging dynamic connections, like when you tote your laptop all over and connect to
different networks.

**The NetworkManager Service**

NetworkManager has been an important part of Linux since 2004.
NetworkManager replaced a hodgepodge of cumbersome network
client tools and manages all of your network interfaces and net‐
work connections. If you’re not familiar with NetworkManager, see
[GNOME NetworkManager.](https://oreil.ly/hkqaq)

If you are running public servers on a commercial hosting service, your firewall setup
depends on what your service provider supports. Protecting public servers, such as
web servers and online storefronts, whether they are remotely hosted or in your own
datacenter, requires a great deal of skill and care that is beyond the scope of this book.
Do please get in-depth study and training, or hire experts.

**How Firewalls Work**

Once upon a time, Ubuntu Linux did not ship with a firewall, because the default
installation had no public services, and therefore no listening network ports. The rea‐
soning was that with no listening ports there were no points of attack. Fortunately,

**326** **|** **Chapter 14: Building a Linux Firewall with firewalld**

this decision was reversed in later releases, because users make changes, even the
most experts users make mistakes, and attackers are always discovering new vulnera‐
bilities. Security is a multilayered process.

Let’s look at how firewalls work. The basic principle is deny all, allow only as needed.

A network service, such as an SSH server, needs to open a network port to enable
remote users to log in. You are allowing other people into your system. The default
port for _sshd_ is TCP port 22. You can see all the listening ports on your system with
the _netstat_ command. This snippet shows what the SSH port looks like:

```
  $ sudo netstat -untap | sed '2p;/ssh/!d'
  Proto Recv-Q Send-Q Local Address Foreign Address State  PID/Program name
  tcp    0   0 0.0.0.0:22   0.0.0.0:*    LISTEN 1296/sshd: /usr/sbi
  tcp6    0   0 :::22     :::*       LISTEN 1296/sshd: /usr/sbi
```

This example shows that there is not an active connection because the Foreign
Address fields are all zeroes and the State is LISTEN. _sshd_ is listening for incoming
IPv4 and IPv6 connections on all network interfaces and all IP addresses on TCP port
22. The combination of IP address and port number is an address that tells the Linux
kernel where to send SSH packets.

This example shows an active SSH connection, with the ESTABLISHED State. It lists
the local address and port that the remote machine is connected to, and the foreign
address and port of the remote machine (the Recv-Q and Send-Q columns have been
removed for clarity):

```
  $ sudo netstat -untap | sed '2p;/ssh/!d'
  Proto Local Address   Foreign Address   State    PID/Program name
  tcp  0.0.0.0:22    0.0.0.0:*      LISTEN   1296/sshd: /usr/sbi
  tcp  192.168.1.97:22  192.168.1.91:56142  ESTABLISHED 13784/sshd: duchess
  tcp6  :::22       :::*         LISTEN   1296/sshd: /usr/sbi
```

There are several ways to control which TCP/IP packets can access a particular IP
address and port. Most servers have configuration options to listen only on particular
network interfaces or IP addresses, and to accept requests from specific addresses and
address ranges. A firewall adds additional controls, and it is a best practice to use
both.

**Network Ports and Numbering**

There are 65,536 possible network ports on a Linux system, numbered 0-65535, and
many of them are reserved for specific services. 0 is reserved and not used. You can
see all of these in the _/etc/services_ [file, which is on every Linux. See the IANA Service](https://oreil.ly/CF0bF)
[Name and Transport Protocol Port Number Registry for the complete official list.](https://oreil.ly/CF0bF)

**firewalld Overview** **|** **327**

This is how the port numbering ranges are organized:

 - 0-1023 are called the _well-known ports_ . These are system ports for common serv‐
ices, such as FTPS (secure file sharing), SSH (secure remote login), NTP (Net‐
work Time Protocol), POP3 (email), HTTPS (encrypted web server), and so on.

 - 1024-49151 are the _registered ports_, which are for additional services.

 - 49152-65535 are the _ephemeral ports_, also called private ports and dynamic ports.
These are used by your system to complete connections with remote services. For
example, when you are web surfing, it looks like this in _netstat_ (the Recv-Q and
Send-Q columns have been removed for clarity):

```
  $ sudo netstat -untap
  Proto Local Address     Foreign Address  State    PID/Program name
  [...]
  tcp  192.168.43.234:50586 72.21.91.66:443  ESTABLISHED 2798/firefox
  tcp  192.168.43.234:38262 52.36.174.147:443 ESTABLISHED 6481/chrome
  tcp  192.168.43.234:53232 99.86.33.45:443  ESTABLISHED 2798/firefox
  [...]
```

This illustrates a response to an outgoing request from your computer. When you
visit a website you initiate the connection request, and the remote web server sends
responses to ephemeral network ports on your system. The first connection on the
list is connected to the example local computer at IP address 192.168.43.234, port
50586. The Foreign Address is the remote server’s IP address and port. The state
ESTABLISHED means it is connected to another machine. When the session is fin‐
ished, after closing the web browser, port 50586 is released and ready to be used
again.

Ephemeral ports are not listening ports for services. Connections to ephemeral ports
are temporary, and are created only as replies to an outgoing connection request from
your computer, such as visiting a website. A firewall can block ephemeral ports, but
then you have no access to hosts or sites outside of your computer.

**14.1 Querying Which Firewall Is Running**

**Problem**

You need to know which firewall your Linux system is using.

**Solution**

Start with the documentation for your particular Linux distribution, as most Linuxes
install with a firewall. The three most common are _iptables_ (Internet Protocol tables),
_ufw_ (Uncomplicated Firewall), and _nftables_ (Netfilter tables). All three manage filter
rules on the netfilter framework, which is part of the Linux kernel.

**328** **|** **Chapter 14: Building a Linux Firewall with firewalld**

Then see what systemd says. This example shows that nftables is running:

```
  $ systemctl status nftables.service
```

     - `nftables.service - Netfilter Tables`
```
  Loaded: loaded (/usr/lib/systemd/system/nftables.service; disabled; vendor>
  Active: active (exited) since Sat 2020-10-17 13:15:05 PDT; 4s ago
  Docs: man:nft(8)
  Process: 3276 ExecStart=/sbin/nft -f /etc/sysconfig/nftables.conf (code=exi>
  Main PID: 3276 (code=exited, status=0/SUCCESS)
  [...]
```

This shows firewalld is running:

```
  $ systemctl status firewalld.service
```

   - `firewalld.service - firewalld - dynamic firewall daemon`
```
  Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor>
  Active: active (running) since Sat 2020-10-17 12:36:20 PDT; 37min ago
  Docs: man:firewalld(1)
  Main PID: 775 (firewalld)
  Tasks: 2 (limit: 4665)
  Memory: 40.9M
  [...]
```

This example checks for ufw and shows that it is installed but inactive:

```
  $ systemctl status ufw.service
```

   - `ufw.service - Uncomplicated firewall`
```
  Loaded: loaded (/lib/systemd/system/ufw.service; disabled; vendor preset:
  enabled)
  Active: inactive (dead)
  Docs: man:ufw(8)
```

If any of them are not installed, you will see a message to that effect.

You could remove ufw and nftables, or mask them so that they cannot be started:

```
  $ sudo systemctl stop ufw.service
  $ sudo systemctl mask ufw.service

  $ sudo systemctl stop nftables.service
  $ sudo systemctl mask nftables.service
```

**Discussion**

It is best to run only one firewall, unless you enjoy untangling conflicting firewall
rules.

**See Also**

 - Chapter 4

 - _[https://firewalld.org](https://firewalld.org)_

**14.1 Querying Which Firewall Is Running** **|** **329**

**14.2 Installing firewalld**

**Problem**

You need to install firewalld on your Linux system.

**Solution**

If firewalld is not on your system, install the _firewalld_ package, and install _firewall-_
_config_ to get the nice graphical interface.

**Discussion**

So far, the major Linux distributions, thankfully, all use the same package names, _fire‐_
_walld_ and _firewall-config_ .

firewalld may or may not start automatically after installation, depending on your
Linux distribution. It must be running to create and test rules.

If possible, disable your machine’s network connection until you have completed your
initial firewalld configuration. Disconnect from your network by clicking the Net‐
workManager applet, which is installed by default on most Linux distributions
(Figure 14-1).

_Figure 14-1. Disconnect from the network with NetworkManager_

Or use the _nmcli_ command. The following example finds and disconnects a WiFi
connection. Use the CONNECTION name in your command:

```
  $ nmcli device status
  DEVICE TYPE STATE    CONNECTION
  wlan0  wifi connected  ACCESS_POINTE

```

**330** **|** **Chapter 14: Building a Linux Firewall with firewalld**

```
  $ nmcli connection down ACCESS_POINTE
  Connection 'ACCESS_POINTE' successfully deactivated
  (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/4)
```

Restore the connection:

```
  $ nmcli connection up ACCESS_POINTE
  Connection successfully activated
  (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/7)
```

Manage firewalld the usual way with systemd. Here are the commands:

 - _systemctl status firewalld.service_

 - _sudo systemctl enable firewalld.service_

 - _sudo systemctl start firewalld.service_

 - _sudo systemctl stop firewalld.service_

 - _sudo systemctl restart firewalld.service_

**See Also**

 - Chapter 4

 - _[https://firewalld.org](https://firewalld.org)_

 - The Appendix

**14.3 Finding Your firewalld Version**

**Problem**

You need the version number of your installed firewalld.

**Solution**

Query the installed package with your package manager, or use _firewall-cmd_ :

```
  $ sudo firewall-cmd --version
  0.9.3
```

**Discussion**

firewalld must be running for the _firewall-cmd_ command to work. If it is not running
you will see a “FirewallD is not running” message.

**14.3 Finding Your firewalld Version** **|** **331**

**See Also**

 - _[https://firewalld.org](https://firewalld.org)_

**14.4 Configuring iptables or nftables as the firewalld**
**Backend**

**Problem**

You want to choose your own firewalld backend, either iptables or nftables.

**Solution**

Edit _/etc/firewalld/firewalld.conf_ with your preference:

```
  FirewallBackend=nftables
```

Or:

```
  FirewallBackend=iptables
```

Then restart firewalld.

**Discussion**

You may need to install your preferred backend.

Even if you don’t care which one your system uses, you should use nftables because
that is what the firewalld developers are actively working on.

**See Also**

 - “firewalld Overview” on page 325

 - [The nftables backend blog post by the firewalld developers has detailed informa‐](https://oreil.ly/xO5eS)
tion about the two backends and future development.

**14.5 Listing All Zones and All Services Managed by**
**Each Zone**

**Problem**

You want to see all the available zones in your firewalld configuration and the services
that each zone manages.

**332** **|** **Chapter 14: Building a Linux Firewall with firewalld**

**Solution**

List the default zone:

```
  $ firewall-cmd --get-default-zone
  public
```

List all zones:

```
  $ firewall-cmd --get-zones
  block dmz drop external home internal public trusted work
```

List all active zones, the zones currently in use:

```
  $ firewall-cmd --get-active-zones
  internal
  interfaces: eth1
  work
  interfaces: wlan0
```

List the configuration of a zone:

```
  $ sudo firewall-cmd --zone=public --list-all
  public
  target: default
  icmp-block-inversion: no
  interfaces:
  sources:
  services: dhcpv6-client ipp ipp-client mdns ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

List the configurations of all zones:

```
  $ sudo firewall-cmd --list-all-zones
  [...]
```

**Discussion**

firewalld zones define levels of trust for network connections. Each zone contains the
zone description and other items as shown in the preceding example for the _public_
zone. Zone files are in XML format, and must have the _.xml_ file extension. Look
in _/usr/lib/firewalld/zones_ to see their source files.

**14.5 Listing All Zones and All Services Managed by Each Zone** **|** **333**

The following list defines zone options:

 - _target:_ defines the default action for packets that do not match any rules. It takes
one of four values: _default_, _ACCEPT_, _DROP_, or _REJECT_ . For example, when con‐
nection requests for dhcpv6-client, ipp, ipp-client, mdns, or ssh packets arrive in
the example _public_ zone, they are accepted. Any packets that do not match the
allowed services are rejected by the _default_ target, and it sends reject messages.

 - _ACCEPT_ accepts all packets that are not explicitly blocked by rules.

 - _DROP_ silently drops all packets not explicitly allowed.

 - _REJECT_ is similar to _DROP_, except that it also sends reject messages.

 - _icmp-block-inversion_ inverts your ICMP requests settings. Any requests that are
blocked are changed to unblocked, and unblocked requests are inverted to
blocked. It is usually set to _no_ .

 - _interfaces:_ defines the network interface or interfaces that this zone is applied to.
Each interface may be bound to only one zone, and you may use the same zone
on multiple interfaces.

 - _source:_ takes IP and MAC addresses, and IP address ranges. For example, you can
accept only packets from your local network, from specific hosts, or block hosts
or networks.

 - _services:_ is the list of services managed by this zone.

 - _ports:_ list port numbers managed by this zone.

 - _protocols:_ list additional TCP protocols managed by this zone, as shown in _/etc/_
_protocols_ .

 - _masquerade:_ is either _yes_ or _no_ . Masquerading is for sharing an IPv4 internet
connection. Set it to _no_ on all hosts except routers.

 - _forward-ports:_ is for forwarding packets that come in on one port to another
port.

 - _source-ports:_ is for listing source ports.

 - _icmp-blocks:_ is for listing ICMP types to block.

 - _rich rules_ are custom rules that you write.

**See Also**

 - _[https://firewalld.org](https://firewalld.org)_

 - _man 5 firewalld.zone_

 - _man 1 firewall-cmd_

**334** **|** **Chapter 14: Building a Linux Firewall with firewalld**

**14.6 Listing and Querying Services**

**Problem**

You want to see a list of services that firewalld supports.

**Solution**

Use the _firewall-cmd_ command:

```
  $ sudo firewall-cmd --get-services
  RH-Satellite-6 amanda-client amanda-k5-client amqp amqps apcupsd audit bacula
  bacula-client bb bgp bitcoin bitcoin-rpc bitcoin-testnet bitcoin-testnet-rpc
  bittorrent-lsd ceph ceph-mon cfengine cockpit condor-collector ctdb dhcp dhcpv6
  [...]
```

That is rather a big glob. Convert it to nice tidy single column:

```
  $ sudo firewall-cmd --get-services| xargs -n1
  RH-Satellite-6
  amanda-client
  amanda-k5-client
  amqp
  amqps
  apcupsd
  [...]
```

Create more columns with _xargs -n2_, _xargs -n3_, and so on.

firewalld services can be more than simple port addressing. For example, the
_bittorrent-lsd_ service includes two destination IP addresses:

```
  $ sudo firewall-cmd --info-service bittorrent-lsd
  bittorrent-lsd
  ports: 6771/udp
  protocols:
  source-ports:
  modules:
  destination: ipv4:239.192.152.143 ipv6:ff15::efc0:988f
  includes:
  helpers:
```

The _ceph-mon_ service opens two listening ports:

```
  $ sudo firewall-cmd --info-service ceph-mon
  ceph-mon
  ports: 3300/tcp 6789/tcp
  [...]
```

You may edit any of the predefined services to meet your requirements.

**14.6 Listing and Querying Services** **|** **335**

**Discussion**

When you’re adding services to a zone, use their names exactly as they appear in the
list. You can create your own custom service; see “Add a Service” in the [firewalld](https://oreil.ly/kvMYY)
[documentation.](https://oreil.ly/kvMYY)

**See Also**

 - _[https://firewalld.org](https://firewalld.org)_

 - [“Add a Service” in the firewalld documentation](https://oreil.ly/kvMYY)

**14.7 Selecting and Setting Zones**

**Problem**

You want to know how to select and set the right zone.

**Solution**

The firewalld zone you select depends on which services your machine is running. If
your machine is not running any network services and needs only a network connec‐
tion, use the _drop_ or the _block_ zone. The _drop_ zone is the most restrictive, dropping all
incoming connections requests, and allowing replies only to connections initiated
from the computer. _block_ is like _drop_, except it sends rejection messages.

The other zones are configured differently on the different Linux distros, so you need
to see how they are configured on your system, like this example for the _work_ zone:

```
  $ sudo firewall-cmd --zone=work --list-all
  work
  target: default
  icmp-block-inversion: no
  interfaces:
  sources:
  services: dhcpv6-client ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

You must bind a zone to a network interface. The following example assigns the _work_
zone to eth0, then verifies it:

```
  $ sudo firewall-cmd --zone=work --permanent --change-interface=eth0
  success

```

**336** **|** **Chapter 14: Building a Linux Firewall with firewalld**

```
  $ sudo firewall-cmd --zone=work --list-interfaces
  eth0
```

If you prefer to test changes before making them permanent, omit the _--permanent_
option. This creates a _runtime_ configuration, and the change is immediately applied.
Runtime changes are lost when firewalld is restarted and when you run _firewall-cmd_
_--reload_ . Convert runtime changes to permanent:

```
  $ sudo firewall-cmd --runtime-to-permanent
```

It is not necessary to reload the firewalld configuration when you bind a zone to a
network interface or restart firewalld.

**Discussion**

How do you know which zone to select? These are the predefined zones that come
with firewalld on Ubuntu 20.04, in order from most restrictive to least restrictive.
Zones may be configured a little differently on your Linux; see Recipe 14.5 to learn
how view your zone configurations.

The following list describes the default zones:

_drop_

All unsolicited incoming network packets are dropped, and there is no reply.
Only incoming packets that are replies to connections initiated from your com‐
puter are allowed. This is the strongest protection when you are connected to an
untrusted network and don’t need to allow access for incoming SSH connections,
shared files, or any other external connection requests.

_block_

Any incoming network connections are rejected with an _icmp-host-prohibited_
message for IPv4, and _icmp6-adm-prohibited_ for IPv6. Only network connections
initiated from your system are allowed.

_public_

Incoming dhcpv6-client, ipp, ipp-client, mdns, and ssh connections are accepted,
all others are blocked.

_external_

This is for a simple internet gateway, combining a firewall and simple routing.
Only incoming SSH connections are accepted, and IPv4 masqerading is enabled
for sharing an internet connection.

_dmz_

For computers in your demilitarized zone that are publicly accessible. Only
incoming SSH connections are accepted. (A DMZ is a separate network segment
on your network for internet-facing servers.)

**14.7 Selecting and Setting Zones** **|** **337**

_work_

Only incoming ssh and dhcpv6-client connections are accepted.

_home_

Only incoming ssh, mdns samba-client, and dhcpv6-client connection requests
are accepted.

_internal_

Only incoming ssh, mdns, samba-client, and dhcpv6-client connection requests
are accepted.

_trusted_

All network connection requests are accepted.

You may customize any of these zones or create new zones; see Recipe 14.9.

**See Also**

 - Recipe 14.9

 - _[https://firewalld.org](https://firewalld.org)_

**14.8 Changing the Default firewalld Zone**

**Problem**

You don’t like your default firewalld zone and want to change it.

**Solution**

Verify your current default:

```
  $ firewall-cmd --get-default-zone
  internal
```

Suppose you want _drop_ as your default, because it is the most restrictive. Set the new
default with the _firewall-cmd_ command:

```
  $ sudo firewall-cmd --set-default-zone drop
  success
```

It is not necessary to reload the firewalld configuration or restart firewalld when you
use this command.

**Discussion**

You may assign zones with NetworkManager (Recipe 14.11). NetworkManager
assigns the default zone to all connections that you do not explicitly assign a zone to.

**338** **|** **Chapter 14: Building a Linux Firewall with firewalld**

**See Also**

 - The Discussion in Recipe 14.7 to learn about firewalld zones

 - Recipe 14.11

 - _[https://firewalld.org](https://firewalld.org)_

**14.9 Customizing firewalld Zones**

**Problem**

None of the default zones meet your needs, and you want to modify the predefined
zones.

**Solution**

Suppose you like the _internal_ zone, but the default configuration isn’t quite what you
want. The current configuration allows _ssh_, _mdns_, _samba-client_, and _dhcpv6-client_ :

```
  $ firewall-cmd --zone=internal --list-all
  internal
  target: default
  icmp-block-inversion: no
  interfaces:
  sources:
  services: ssh mdns samba-client dhcpv6-client
  [...]
```

The following example shows how to remove _samba-client_ because you don’t use
Samba:

```
  $ sudo firewall-cmd --remove-service=samba-client --zone=internal
  success
```

You are running a small local 389 Directory server, so you need to add the LDAPS
service:

```
  $ sudo firewall-cmd --zone=internal --add-service=ldaps
  success
```

These are temporary changes that will not survive a reboot or configuration reload.
However, they are immediately applied so that you can test them. Test your changes,
and if everything works as expected, make the changes permanent:

```
  $ sudo firewall-cmd --runtime-to-permanent
  success

```

**14.9 Customizing firewalld Zones** **|** **339**

To discard the changes, do not use _--runtime-to-permanent_ . Instead, use _--reload_ to
discard the runtime changes and revert to your original configuration:

```
  $ sudo firewall-cmd --reload
  success
```

**Discussion**

_--reload_ does not interrupt any active connections.

_--complete-reload_ reloads firewalld completely, including reloading kernel modules,
and terminates active connections. This is a good option when your runtime changes
are so messed up you want to start over.

**See Also**

 - The Discussion in Recipe 14.7 to learn about firewalld zones

 - _[https://firewalld.org](https://firewalld.org)_

 - Chapter 4

**14.10 Creating a New Zone**

**Problem**

You want to create a new custom zone.

**Solution**

Create an XML containing your zone configuration, then reload firewalld and it is
ready to use.

The following example creates a zone for local name services, with DNS and DHCP
servers on the same machine, and SSH access. The example file is named _/etc/fire‐_
_walld/zones/names.xml_ :

```
  <?xml version="1.0" encoding="utf-8"?>
  <zone>
  <short>Name Services</short>
  <description>
  DNS and DHCP servers for the local network, IPv4 only.
  </description>
  <service name="dns"/>
  <service name="dhcp"/>
  <service name="ssh"/>
  </zone>

```

**340** **|** **Chapter 14: Building a Linux Firewall with firewalld**

Run the _sudo firewall-cmd --get-zones_ command, and your new zone will not be lis‐
ted. Add the _--permanent_ option to see any new zones that are not yet read by fire‐
walld, and now the new “names” zone appears. Zone names are the filenames without
the _.xml_ extension:

```
  $ sudo firewall-cmd --permanent --get-zones
  block dmz drop external home internal names public trusted work
```

Reload firewalld:

```
  $ sudo firewall-cmd --reload
  success
```

Now firewalld can read it, and you can see it with the other zones:

```
  $ sudo firewall-cmd --get-zones
  block dmz drop external home internal names public trusted work
```

And list its configuration:

```
  $ sudo firewall-cmd --zone=names --list-all
  names
  target: default
  icmp-block-inversion: no
  interfaces:
  sources:
  services: dhcp dns ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

Your new zone is ready to use, and you can modify it just like any other zone.

**Discussion**

See _man 5 firewalld.zone_ to learn about configuration options and see the source files
for the predefined zones in _/usr/lib/firewalld/zones/_ to use as examples. The only files
that go in _/etc/firewalld/zones/_ are user custom files.

Remove a zone by deleting its _.xml_ file, and then reload firewalld.

**See Also**

 - _man 5 firewalld.zone_

 - _[https://firewalld.org](https://firewalld.org)_

 - Recipe 14.9

**14.10 Creating a New Zone** **|** **341**

**14.11 Integrating NetworkManager and firewalld**

**Problem**

You travel between multiple networks, such as multiple work locations, coffee shops,
hotels, and coworking locations. You need to know how to set up NetworkManager
to keep up with these changes and always ensure that new connections are assigned
to the correct firewall zone.

**Solution**

NetworkManager includes firewalld integration. When you connect to a new net‐
work, NetworkManager assigns it to your default firewalld zone.

You may assign a nondefault zone to a particular connection with NetworkManager.
If you have the NetworkManager applet in your panel, click it to bring up the Edit
Connections dialog (Figure 14-2).

_Figure 14-2. Editing network connections in NetworkManager_

Or, run the _nm-connection-editor_ command to open the editor. Click Edit Connec‐
tions, click the connection you want to edit, and click the gear icon to open the editor.
This opens the editing dialog (Figure 14-3).

**342** **|** **Chapter 14: Building a Linux Firewall with firewalld**

_Figure 14-3. Changing the firewall zone_

Go to the General tab and use the Firewall Zone drop-down menu to select the zone
you want for that connection. Save your change and you’re finished.

**See Also**

 - The Discussion in Recipe 14.7 to learn about firewalld zones

 - Recipe 14.9

 - [NetworkManager Reference Manual](https://oreil.ly/pvrwj)

**14.12 Allowing or Blocking Specific Ports**

**Problem**

You are using nonstandard ports, for example, port 2022 for your SSH server. You
want to block port 22 and allow port 2022.

**Solution**

Any port that is not specifically allowed is denied for all firewalld zones, except the
_trusted_ zone, which allows everything. If you were using the default SSH service,
which uses TCP port 22, first remove port 22 from the relevant zone, then add port

**14.12 Allowing or Blocking Specific Ports** **|** **343**

2022, then reload firewalld. In this example the nonstandard port is assigned to the
_work_ zone:

```
  $ sudo firewall-cmd --zone=work --remove-port=22/tcp
  success
  $ sudo firewall-cmd --zone=work --add-port=2022/tcp
  success
```

Verify by listing the zone configuration:

```
  $ sudo firewall-cmd --list-all --zone=work
  work
  target: default
  icmp-block-inversion: no
  interfaces:
  sources:
  services: ssh
  ports:2022/tcp
  [...]
```

When you are satisfied, make your changes permanent:

```
  $ sudo firewall-cmd --runtime-to-permanent
```

**Discussion**

If you see a message like “Warning: NOT_ENABLED: 22:tcp” when you try to
remove that port, that means it was not enabled for that zone, and you can go ahead
and add your new port.

When you use a nonstandard port, clients connecting to the service must specify that
port number. For example, for SSH:

```
  $ ssh -p 2022 server1
```

How do you know what ports to use? Every service has its own default ports, which
you will find in the service’s documentation, and in the _/etc/services_ file. You may use
nonstandard ports, and they must be unused ports between 1024 and 49151. Record
your changes in _/etc/services_ . You also need to set your nonstandard ports in the con‐
figuration for your server. See Recipe 12.3 for an example.

**See Also**

 - _[https://firewalld.org](https://firewalld.org)_

 - Recipe 12.3

**344** **|** **Chapter 14: Building a Linux Firewall with firewalld**

**14.13 Blocking IP Addresses with Rich Rules**

**Problem**

You want to block certain IP addresses.

**Solution**

Create a _rich rule_, which defines the address to be blocked, and the target, which in
the example is _reject_ . The following example blocks a single address, and is added to
the internal zone:

```
  $ sudo firewall-cmd --zone=internal \
  --add-rich-rule='rule family="ipv4" source address=192.168.1.91 reject'
  success
```

Test it by pinging from the blocked host. The blocked host should see the “Destina‐
tion Port Unreachable” message.

If you do not want to keep the rule, run _sudo firewall-cmd --reload_ to delete it.

To make it permanent, use the _--runtime-to-permanent_ option:

```
  $ sudo firewall-cmd --runtime-to-permanent
```

List the rich rules in a zone:

```
  $ sudo firewall-cmd --zone=internal --list-rich-rules
  rule family='ipv4' source address='192.168.1.91' reject
```

To delete a permanent rich rule, use the _--remove-rich-rule_ option:

```
  $ sudo firewall-cmd --zone=internal \
  --remove-rich-rule="rule family='ipv4' \
  source address='192.168.1.91' reject"
  success
```

You don’t have to completely block the offending host, but you can apply blocks to
specific services. The following example blocks the source address only for the SSH
service:

```
  $ sudo firewall-cmd --zone=internal --add-rich-rule='rule family="ipv4" \
  source address=192.168.1.91 service name="ssh" protocol=tcp reject'
  success
```

**Discussion**

You may create multiple rich rules in a zone, though be careful to avoid conflicts.

Once upon a time, a person I had the dubious pleasure of working with thought it
was funny to practice penetration testing on his coworkers. Our team ran a number

**14.13 Blocking IP Addresses with Rich Rules** **|** **345**

of test servers on our workstations and made them available to the team. Our wan‐
nabe pen-tester was so annoying, we all blocked him at our firewalls.

**See Also**

 - The Discussion in Recipe 14.7 to learn about firewalld zones and options

 - _[https://firewalld.org](https://firewalld.org)_

 - _man 5 firewalld.richlanguage_

**14.14 Changing a Zone Default Target**

**Problem**

You want to change the default target for a zone.

**Solution**

List the current target:

```
  $ sudo firewall-cmd --zone=internal --list-all
  internal
  target: ACCEPT
  [...]
```

Change it from _ACCEPT_ to _REJECT_, then reload and verify:

```
  $ sudo firewall-cmd --permanent --zone=internal --set-target=REJECT
  success

  $ sudo firewall-cmd --reload

  $ firewall-cmd --zone=names --list-all
  names
  target: %%REJECT%%
  [...]
```

**Discussion**

The zone target defines the default action for packets that do not match any rules. It
takes one of four values: _default_, _ACCEPT_, _DROP_, or _REJECT_ .

**See Also**

 - _[https://firewalld.org](https://firewalld.org)_

 - The Discussion in Recipe 14.5 to learn about firewalld zones

 - Recipe 14.11

**346** **|** **Chapter 14: Building a Linux Firewall with firewalld**

**<u>CHAPTER 15</u>**
#### **Printing on Linux**

Linux relies on CUPS, the Common Unix Printing System, to manage printers. In
this chapter you will learn how to install and manage printers, and how to share them
over your network. You will learn about the _driverless_ future of Linux printing, in
which printers will be available to client devices without having to install drivers.

**Overview**

The key to happy printing on Linux is to select good-quality printers and multifunc‐
tion devices (printer, scanner, copier, fax) that are well supported on Linux. Which,
thankfully, is a lot easier than in olden times. When you select a well supported
device, the drivers are included in CUPS, and you do not have to hassle with hunting
down and downloading manufacturer drivers.

The next-best option is buying machines that have manufacturer-supplied Linux
drivers. This is not my favorite option, as the drivers are often old and not main‐
tained, and you must manually install them. This is more common with multifunc‐
tion devices (MFDs). For one example, the Brother MFC-J5945DW is my personal
machine, and it does not have native CUPS drivers, though it does support driverless
printing. It was a good deal and inks are cheap, though in hindsight I really should
have bought a machine with native Linux support. Native support is more reliable
because once a device is supported in CUPS it is always supported, and you won’t be
at the mercy of manufacturers who don’t maintain their drivers or who discontinue
their driver downloads.

The least favorable option is to buy without doing your homework and hope it works.
In this case you might be able to use macOS drivers (PPD files) for printers not sup‐
ported in Linux, though it can take some work if the Macintosh PPD has macOCspecific entries, such as calling macOS executables, libraries, or filters. These must be

**347**

[replaced with the equivalents for Linux, if they exist. See cupsFilter for some useful](https://oreil.ly/w3Oqd)
information if you want to try this.

If you want a shared device, the least troublesome approach is to get one that has net‐
working built in, and that has built-in controls for copying, setting up networking,
viewing ink levels, cleaning print heads, and other setup and maintenance tasks.
These are easier and more pleasant to use than devices that require setup and control
from a computer.

**Finding Supported Printers and Scanners**

Hewlett-Packard (HP) printers and multifunction devices have excellent Linux sup‐
port via the _hplip_, _hplip-hpijs_, _hplip-sane_, and _hplip-scan-utils_ packages. Of course
every Linux is special and has different package names, such as _hpijs-ppds_, _hplip-data_,
_printer-driver-hpcups_, _hplip-common_, and _libsane-hpaio_ . Searching for _hplip_ should
find them.

Not all HP printers and MFDs are supported in Linux; see the link below for HP’s
Linux support database.

Brother has good machines, decent customer support, and good prices on inks. They
have both machines with native Linux support and some that require the Brother
drivers.

Canon, Epson, Honeywell, Fujitsu, IBM, Lexmark, Kodak, Tektronix, Samsung,
Sharp, Xerox, Toshiba, and many other brands have some level of Linux support. It
can be difficult to learn which models are supported. Some vendors tell you in their
product specs. There are several websites to check, though they are usually not com‐
plete nor up-to-date, but they’re good places to start:

 - [Supported HP printers](https://oreil.ly/y9z4J)

 - [OpenPrinting.org printer listings](https://oreil.ly/7JbPH)

 - [H-node printers and MFDs](https://oreil.ly/Hwy0w)

 - [ThinkPenguin store](https://oreil.ly/54H5F)

 - [Ubuntu page for supported printers](https://oreil.ly/03SV3)

 - [IPP Everywhere Printers](https://oreil.ly/l7pFz)

**CUPS Printer Drivers**

Linux printer drivers are provided by CUPS, the Common Unix Printing System.
CUPS has been the standard printing subsystem for Linux since around 2000. Apple
started using CUPS around 2002, then hired CUPS creator Michael Sweet and bought
the source code in 2007. Sweet left Apple in 2019, and Apple’s involvement stalled—

**348** **|** **Chapter 15: Printing on Linux**

see [apple/cups on GitHub. Mr. Sweet has not been idle; rather, he has been hard at](https://oreil.ly/HgUX8)
[work on the OpenPrinting.org’s CUPS fork at OpenPrinting/cups on GitHub.](https://oreil.ly/uP0CJ)

There is a lot more to CUPS than writing code. Michael Sweet, Till Kamppeter, and
others invested a lot of work into getting manufacturers on board and developing
common printing standards and APIs. The centers of CUPS and printing standards
[development are The Printer Working Group and OpenPrinting.](https://oreil.ly/yEMad)

Printer drivers in CUPS consist of one or more filters specific to a printer, which are
packaged in PPD (PostScript Printer Description) files. All printers in CUPS, even
non-PostScript printers, need a PPD. The PPDs contain descriptions about the print‐
ers, printer commands, and filters.

Filters translate print jobs to formats the printer can understand, such as PDF, HPPCL, raster, and image files, and they pass in commands for operations such as page
selection, paper size, colors, contrast, and media type. PPDs are plain-text files, and
the PPDs for all supported printers are in _/usr/share/cups/model/_ . Installed printers
have PPDs in _/etc/cups/ppd/_ .

**PPDs Are Doomed**

CUPS has relied on PPDs from its inception, and they have worked well. However,
there is new approach in development called _driverless_ printing. Instead of using
static PPD files, the printer advertises its capabilities and does not require driver
installation on client machines. The idea is to make connecting to a new printer as
easy as connecting to a new network with NetworkManager, which automatically
finds available networks and does not require you to install drivers or to manually
configure every new network. This is especially advantageous for mobile devices like
phones and tablets, which have limited storage space and limited screen size for has‐
sling with driver installation.

Driverless was introduced in CUPS 2.2.0. You should have at least CUPS 2.2.4
(released in June 2017) for reliable performance. You can learn more at the following
resources:

 - [Printer Applications: A New Way to Print in Linux](https://oreil.ly/clNC3)

 - [CUPS Driverless Printing](https://oreil.ly/yaj5q)

**Overview** **|** **349**

**15.1 Using the CUPS Web Interface**

**Problem**

You need to find the CUPS administration tool.

**Solution**

Open the CUPS web interface in your web browser at _[http://localhost:631/](http://localhost:631/)_
(Figure 15-1).

_Figure 15-1. The CUPS web control panel_

**Discussion**

There are numerous graphical tools for managing printers, such as _system-config-_
_printer_ and the YaST printer module in openSUSE. The CUPS web administration
page provides the most complete management options and is the same on all Linux
distributions.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.2 Installing a Locally Attached Printer**

**Problem**

You need to install a new printer which is connected to your PC. You have wisely
chosen a printer with native CUPS support.

**350** **|** **Chapter 15: Printing on Linux**

**Solution**

Use the CUPS web control panel. Your printer should be connected and powered on.
The following examples are on a Linux Mint system.

Go to the Administration tab and click Add Printer. It will ask you for your login
(Figure 15-2). (If your login does not work, and only the root login succeeds, see
Recipe 15.7 to learn how to configure CUPS to accept nonroot logins.) Check “Save
debugging information for troubleshooting,” and check “Share printers connected to
this system” to share printers directly attached to your computer. This only enables
sharing, and then you must enable sharing on each printer you want to share.

_Figure 15-2. Adding a printer_

On the next screen, CUPS discovers and lists your printer in the Local Printers sec‐
tion (Figure 15-3). Select your printer and click Continue.

Now you should see a screen like Figure 15-4, with Name, Description, and Location
fields. The Name and Description fields are automatically filled, and you may change
these to whatever you want. The Name field appears in the printer dialogs when you
print a document.

**15.2 Installing a Locally Attached Printer** **|** **351**

_Figure 15-3. CUPS finds your local printer_

_Figure 15-4. Specifying the name, description, and location_

Select your printer driver. CUPS displays a giant list for you to choose from. Find the
driver for your printer model. In Figure 15-5 the drivers come from the _epson-inkjet-_
_printer-escpr_ package ( _printer-driver-escpr_ on Ubuntu), for Seiko Epson color ink jet
printers.

**352** **|** **Chapter 15: Printing on Linux**

_Figure 15-5. Select the printer driver_

The final configuration screen is for setting default options, such as paper type, paper
size, color or black and white, print quality, and other options according to what your
printer and printer driver support. When you are finished, click Set Default Options
(Figure 15-6).

_Figure 15-6. Set default printer options_

**15.2 Installing a Locally Attached Printer** **|** **353**

When you are finished, you see the Printers page, listing all of your installed printers
(Figure 15-7).

_Figure 15-7. All installed printers_

Click on your new printer, and print a test page from the Maintenance drop-down
menu. When it prints correctly, you are done.

**Discussion**

In Figure 15-2 you see two buttons, Add Printer and Find New Printers. These are
pretty much the same thing, with the discovered printer listings organized differently.

You will probably have more than one printer driver to choose from; for example, it is
common to see both CUPS+Gutenprint and Foomatic drivers for the same printer.
Gutenprint used to be the better choice for color printers; try both to see which you
prefer. CUPS+Gutenprint Simplified drivers contain fewer features and options than
the full versions.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.3 Giving Printers Useful Names**

**Problem**

When you open the printer dialog in a document, you have several printers to choose
from, including some that look similar, and you aren’t sure which one to use.

**Solution**

When you install a printer, enter a descriptive name in the Name field (Figure 15-8).
You have to do this at installation because you cannot change the name after
installation.

**354** **|** **Chapter 15: Printing on Linux**

_Figure 15-8. Use the printer name to identify your printers_

**Discussion**

When you first install a printer using the CUPS web control panel, there are Descrip‐
tion and Location fields that you can use, and these show up in the CUPS web control
panel. But many apps that you print from do not read these fields and only read the
Name field. Some exceptions are the Evolution mail client and the Firefox and Chro‐
mium web browsers, which display the name, location, and status.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.4 Installing a Network Printer**

**Problem**

There is a shared network printer on your network, and you want to install it on your
computer.

**Solution**

The procedure is the same as installing a locally attached USB printer (Recipe 15.2),
except you select a discovered network printer. The printer must be powered on and

**15.4 Installing a Network Printer** **|** **355**

on the same network segment as your computer. You will see it listed under Discov‐
ered Network Printers (Figure 15-9).

_Figure 15-9. Installing a shared network printer_

You need TCP port 631 open in the firewalls on all clients.

**Discussion**

What if CUPS does not discover your printer? See Recipe 15.11 for some trouble‐
shooting help. If CUPS does not see your printer, you cannot install it.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**356** **|** **Chapter 15: Printing on Linux**

**15.5 Using Driverless Printing**

**Problem**

Your printer is not supported in CUPS, and you want to try the driverless printing
option. Or, you want to connect your Android or iOS devices to your printer.

**Solution**

You may have already seen driverless options in the CUPS printer driver selector. The
following example is for my Brother MFC-J5945DW, which does not have native
CUPS support.

Go to Administration → Add Printer in the CUPS web control panel. CUPS sees my
Brother machine in Discovered Network Printers (Figure 15-10). There is a _driverless_
option, and that is the correct one to choose.

_Figure 15-10. CUPS sees my unsupported network printer_

Continue the installation, and select the correct driver, which in Figure 15-11 is the
“Brother MFC-J5945DW, driverless, cups-filters 1.25.0 (en).”

Print a test page, and if it looks right, the installation is completed.

**15.5 Using Driverless Printing** **|** **357**

_Figure 15-11. Select the driverless printer driver_

**Discussion**

Strictly speaking, this isn’t driverless, because CUPS creates PPD files in _/etc/cups/ppd_
for your “driverless” printer. However, you don’t have to maintain directories full of
OpenPrinting.org and Gutenprint PPDs.

Your printer must support driverless printing, which means it must support the Mop‐
ria, AirPrint, IPP Everywhere, or WiFi Direct Print standard. These are all similar:
the printer advertises itself, its network address, and basic functionality via the Avahi
daemon. Avahi provides service discovery on your local network, using the mDNS/
DNS-SD protocol suite. (Apple calls this service Bonjour and Zeroconf.)

Driverless printing in CUPS works great for Android and iOS devices. You only need
to install a printer app. If your printer is driverless enabled, and especially if it is Mop‐
ria certified, then your mobile devices will have no trouble finding it. Mopria certifi‐
cation means your printer supports wireless printing sent from mobile devices. If

**358** **|** **Chapter 15: Printing on Linux**

your printer documentation does not tell you if it is Mopria certified, run the follow‐
ing command, which shows that the printer is Mopria certified:

```
  $ avahi-browse -rt _ipp._tcp
  [...]
  txt = ["mopria-certified=1.3"
  [...]
```

**See Also**

 - [Debian Wiki, Driverless Printing](https://oreil.ly/d2Qw8)

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.6 Sharing Nonnetworked Printers**

**Problem**

You want to share a printer that does not have built-in networking.

**Solution**

CUPS shares printers that do not have networking, but are connected to a PC on your
network. First, you must have your name services working so that all your LAN hosts
can ping each other.

Make sure that printer sharing is enabled on the Administration screen by checking
“Share printers connected to this system.” Then enable sharing on the printer you
want to share (Figure 15-12).

_Figure 15-12. Enable printer sharing_

**15.6 Sharing Nonnetworked Printers** **|** **359**

CUPS will advertise the printer to your network. Any Linux client on your network
who wants to use this printer must install it the same way as installing a network or
locally attached printer; start at Administration → Add Printer, then go through the
normal installation process.

You may also share with Windows and macOS clients. macOS has native support for
discovery via DNS-SD/mDNS and IPP. DNS-SD/mDNS is provided by Avahi on
Linux and is called Bonjour on the Macintosh. Use the Macintosh control panel to
find and install shared CUPS printers.

Windows 10 natively supports DNS-SD/mDNS. Older Windows releases support
sharing via the Internet Printing Protocol (IPP). Use the Windows printer control
panel to find and install shared CUPS printers.

**Discussion**

In olden times, before network-enabled printers were common and inexpensive,
admins used dedicated printer servers. These were old PCs, old laptops, small singleboard computers, or commercial printer server devices. You can still buy small
printer server gadgets, and they cost a lot less than in the old days.

Nowadays most printers have networking built in and are simpler to manage.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.7 Correcting the “Forbidden” Error Message**

**Problem**

When you try to perform any administrative task in the CUPS web control panel, for
example, adding a new printer, your login fails and there is a “Add Printer Error
Unable to add printer: Forbidden” message.

**Solution**

On some Linux distributions, such as openSUSE, the default configuration allows
only the root user to do CUPS administration tasks. Edit _/etc/cups/cups-files.conf_ to
allow nonroot users to do CUPS administration tasks. Look for these lines:

```
  # Administrator user group, used to match @SYSTEM in cupsd.conf policy rules...
  # This cannot contain the Group value for security reasons...
  SystemGroup root

```

**360** **|** **Chapter 15: Printing on Linux**

This is why only the root login works. You can add your own private user group, like
our example user Duchess, whose private group is _duchess_ :

```
  SystemGroup root duchess
```

After saving changes to _/etc/cups/cups-files.conf_, restart the CUPS service:

```
  $ sudo systemctl restart cups.service
```

Now Duchess can do CUPS administration tasks.

Another approach is to use a system group created for this purpose. On Ubuntu
Linux distributions, this is the _lpadmin_ group, and Fedora uses the _sys_ and _wheel_
groups. You may create your own group for CUPS administration, like the following
example that creates a _cupsadmin_ group, and adds the user Mad Max to this group:

```
  $ sudo groupadd -r cupsadmin
  $ sudo usermod -aG cupsadmin madmax
```

Mad Max must log out, then log back in to activate the new group membership. Add
the _cupsadmin_ group to _SystemGroup_ in _/etc/cups/cups-files.conf_ :

```
  SystemGroup root duchess cupsadmin
```

Restart CUPS, and Mad Max can go to work.

**Discussion**

There should also be a section like this in _/etc/cups/cups-files.conf_ :

```
  # Default user and group for filters/backends/helper programs; this cannot be
  # any user or group that resolves to ID 0 for security reasons...
  #User lp
  #Group lp
```

None of the groups listed for _SystemGroup_ can match _Group_ . If you try to use _lp_, as in
the preceding example, CUPS will not start, and you will see error messages
in _/var/log/cups/error_log_ or the syslog, depending how yours is configured in _/etc/_
_cups/cups-files.conf_ .

If your Linux uses SysV init instead of systemctl, restart it with this command:

```
  $ sudo /etc/init.d/cups restart
```

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

 - Chapter 4

**15.7 Correcting the “Forbidden” Error Message** **|** **361**

**15.8 Installing Printer Drivers**

**Problem**

You need to know if installing CUPS also installs a complete set of printer drivers, or
if there are more that you might want that are not included with CUPS.

**Solution**

Most Linuxes install a subset of all available printing options. Every Linux distribu‐
tion varies in which printer drivers are available, which ones are included in a default
installation, and which specific names are used for packages, especially between
Ubuntu and everyone else.

The following list comprises a basic set of CUPS packages and printer drivers:

 - _cups_ (server and client)

 - _cups-filters_ (OpenPrinting CUPS filters and backends)

 - _gutenprint_ (Gutenprint printer drivers)

 - _foomatic_ (Foomatic printer drivers)

 - OpenPrinting.org PPDs; for example, OpenSUSE provides:

 - _OpenPrintingPPDs_

 - _OpenPrintingPPDs-ghostscript_ (interpreter of printer drivers written in the

PostScript language)

 - _OpenPrintingPPDs-hpijs_ (HP printers)

 - _OpenPrintingPPDs-postscript_

 - _cups-client_ (command-line utilities for setting up and managing printers)

OpenPrinting.org includes Foomatic. Fedora and Ubuntu ship _foomatic_ packages,
while OpenSUSE includes _OpenPrinting_ packages. The names change, but the func‐
tionality is the same.

These packages may provide everything you need. The following are additional
printer packages you might find useful:

 - _gimp-gutenprint_ (provides a more featureful printer dialog for GIMP, the GNU
Image Manipulation Program)

 - _bluez-cups_ (connect Bluetooth printers)

 - _cups-airprint_ (share printers with iOS devices)

 - _ptouch-driver_ (Brother P-touch label printers)

**362** **|** **Chapter 15: Printing on Linux**

 - _rasterview_ (view Apple raster images such as GIF, JPEG, and PNG, see
[MSweet.org/rasterview](https://oreil.ly/zZZAp)

 - _c2esp_ (some Kodak all-in-one printers)

Ubuntu packages the largest assortment of printer drivers. Many, but not all, of the
package names start with _printer-driver_ :

 - _openprinting-ppds_ (OpenPrinting printer support, PostScript PPD files)

 - _printer-driver-all_ (printer drivers metapackage)

 - _printer-driver-brlaser_ (some Brother laser printers)

 - _printer-driver-c2050_ (Lexmark 2050 Color Jetprinter)

 - _printer-driver-foo2zjs_ (ZjStream-based printers)

 - _printer-driver-c2esp_ (Kodak ESP AiO color inkjet series)

 - _printer-driver-cjet_ (Canon LBP laser printers)

 - _printer-driver-cups-pdf_ (PDF writing via CUPS)

 - _printer-driver-dymo_ (DYMO label printers)

 - _printer-driver-escpr_ (Epson Inkjets that use ESC/P-R)

 - _printer-driver-foo2zjs_ (ZjStream-based printers)

 - _printer-driver-fujixerox_ (Fuji Xerox printers)

 - _printer-driver-gutenprint_ (printer drivers for CUPS)

 - _printer-driver-hpcups_ (HP Linux Printing and Imaging, CUPS Raster driver
(hpcups))

 - _printer-driver-hpijs_ (HP Linux Printing and Imaging, printer driver (hpijs))

 - _printer-driver-indexbraille_ (CUPS printing to Index Braille printers)

 - _printer-driver-m2300w_ (Minolta magicolor 2300W/2400W color laser printers)

 - _printer-driver-min12xxw_ (KonicaMinolta PagePro 1[234]xxW)

 - _printer-driver-oki_ (OKI Data printers)

 - _printer-driver-pnm2ppa_ (HP-GDI printers)

 - _printer-driver-postscript-hp_ (HP Printers PostScript Descriptions)

 - _printer-driver-ptouch_ (printer driver for Brother P-touch label printers)

 - _printer-driver-pxljr_ (HP Color LaserJet 35xx/36xx)

 - _printer-driver-sag-gdi_ (Ricoh Aficio SP 1000s/SP 1100s)

 - _printer-driver-splix_ (Samsung and Xerox SPL2 and SPLc la)

**15.8 Installing Printer Drivers** **|** **363**

**Discussion**

If you don’t see your printer listed in the driver selector in the CUPS web interface,
try searching for the brand name of your printer in your package manager. This may
all seem rather messy, but setting up printers is untidy on all computing platforms
(not just on Linux).

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

 - [Ghostscript documentation](https://oreil.ly/CHZpP)

 - [OpenPrinting](https://oreil.ly/jpYIW)

 - [The Printer Working Group](https://oreil.ly/Q5BUh)

**15.9 Modifying an Installed Printer**

**Problem**

You want to change the configuration of a printer that is already installed. For exam‐
ple, you want to share it.

**Solution**

Open the printer in the CUPS web control panel, then click Administration → Mod‐
ify Printer. This is similar to installing a new printer, except it displays the printer’s
current settings. Figure 15-13 enables sharing the printer. (Note that sharing must
first be enabled on the Administration → Advanced page.)

_Figure 15-13. Modifying an installed printer_

**364** **|** **Chapter 15: Printing on Linux**

**Discussion**

You can change everything except the printer name.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.10 Saving Documents by Printing to a PDF File**

**Problem**

You want to save a web page, or any document, to a PDF file instead of sending it to a
printer.

**Solution**

Look at the File → Print dialog in any application, and you will see an option to print
to a PDF file (Figure 15-14).

_Figure 15-14. Printing to a PDF file_

You have all the usual options, such as filename and location, margins, print quality,
color or monochrome, and page orientation. The printer dialogs look different in dif‐
ferent apps; for example, the Firefox web browser printer dialog includes a document
preview. In other apps the preview is usually a separate button.

**15.10 Saving Documents by Printing to a PDF File** **|** **365**

**Discussion**

Print to file is great for saving web confirmation forms and receipts, and creating
PDFs from any type of documents.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**15.11 Troubleshooting**

**Problem**

Printing doesn’t work! How do you fix it?

**Solution**

These are the most common issues with printers on Linux:

 - For shared printers, make sure that your networking is set up correctly and your
firewall allows TCP port 631. If you have more than one network, verify that the
printer is on the same network as your computer.

 - For USB-connected printers, try a different USB port or a different cable.

 - Verify you are using the correct printer drivers, or try driverless.

 - The CUPS daemon is managed by systemd. Try restarting the daemon:
```
    $ sudo systemctl restart cups.service
```

Or reboot, and also power-cycle your printer.

 - Check your log files on the CUPS web administration page; you can view both
the error log and the access log. Turn the logging level up to Debug to get the
most information. (Click Edit Configuration File, then set _LogLevel debug_ .)

**Discussion**

The most important factor is using printers with good Linux support. This prevents
most problems.

**See Also**

 - [CUPS documentation](https://oreil.ly/OlCzV)

**366** **|** **Chapter 15: Printing on Linux**

**<u>CHAPTER 16</u>**
#### **Managing Local Name Services with** **Dnsmasq and the hosts File**

[Dnsmasq is an excellent server for LAN name services, both Domain Name System](https://oreil.ly/MUa4U)
(DNS) and Dynamic Host Discovery Protocol (DHCP). Dnsmasq also provides
BOOTP, PXE, and TFTP, which are for network booting and installing operating sys‐
tems from a network server. Dnsmasq supports IPv4 and IPv6, provides local DNS
caching, and acts as a stub resolver.

This chapter covers setting up local DNS and DHCP using Dnsmasq and the _/etc/_
_hosts_ file together. _/etc/hosts_ is the very old way of setting up DNS, mapping host‐
names to IP addresses in a static file. _/etc/hosts_ by itself is sufficient for very small net‐
works.

Dnsmasq is designed for LAN name services. It is lightweight and simple to config‐
ure, especially in comparison to BIND, the dominant DNS server, which is heavy‐
weight and has a rather steep learning curve.

Dnsmasq and _/etc/hosts_ work great together. Dnsmasq reads the entries in _/etc/hosts_
into DNS.

The DHCP server in Dnsmasq automatically integrates with DNS. All you need for
Dnsmasq to create DNS entries for your DHCP clients is to configure your DHCP
clients to send their hostnames to the DHCP server, which is the default in most
Linux distributions.

There are four types of DNS servers: recursive resolvers, root name servers, top-level
domain (TLD) name servers, and authoritative name servers.

Recursive resolvers answer DNS requests. A stub resolver, like Dnsmasq and
systemd-resolved, forwards any requests it cannot answer from its cache to an
upstream resolver. When you visit a website a recursive resolver finds the site’s DNS

**367**

information by querying the other three types of DNS servers. Recursive resolvers
cache this information to make it available more quickly. Your ISP’s name servers,
and services like [OpenDNS,](https://oreil.ly/oCRsV) [Cloudflare, and](https://oreil.ly/9Fgqc) [Google Public DNS are all recursive](https://oreil.ly/lc9ep)
resolvers.

There are 13 types of root name servers, spread all over the planet, and there are cur‐
rently several hundred root name servers. A root server accepts a query from a recur‐
sive resolver, then the root server directs the request to the appropriate TLD server
according to the top-level domain: .com, .net, .org, .me, .biz, .int, .biz, .gov, .edu, and
[so on. The Internet Corporation for Assigned Names and Numbers—ICANN—over‐](https://icann.org)
sees all of these servers and domains.

Authoritative name servers are the source records for a domain and are controlled by
the owner of the domain. Dnsmasq can serve as your authoritative name server,
though I recommend using BIND. See the Authoritative Configuration section of
_man 8 dnsmasq_ to learn more.

**Too Many Name Service Utilities**

Linux distributions are still transitioning to NetworkManager and
_systemd-resolved_ from the legacy _resolvconf_, which has long been
the default DNS resolver on Linux systems. This presents a bit of a
tangle for Linux users, with continual changes and the various dis‐
tros making the transition at different rates. Pay close attention to
the documentation, forums, and release notes for your particular
Linux.

It should be possible to use Dnsmasq as the DNS backend for Net‐
workManager, because NetworkManager has a plug-in for this. But
on some Linux distributions, this does not yet work correctly
(Recipe 16.5).

You don’t need systemd-resolved running on your Dnsmasq server
because it will contend with Dnsmasq for control of the system’s
stub DNS resolver.

By the time you read this, all of this may be different, but for now
the recipes aim to be reliable rather than cutting edge.

**16.1 Simple Name Resolution with /etc/hosts**

**Problem**

You want a simple, fast way to set up name resolution without having to run a DNS
server.

**368** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

**Solution**

This is what the _/etc/hosts_ file is made for. Your LAN computers must have static IP
addresses. The following is an example for three computers:

```
  127.0.0.1 localhost
  ::1 localhost ip6-localhost ip6-loopback
  192.168.43.81 host1
  192.168.43.82 host2
  192.168.43.83 host3
```

Copy these entries to all three hosts, then try pinging each other by hostnames, like
this example for pinging _host2_ from _host3_ :

```
  host3:~$ ping -c2 host2
  PING host2 (192.168.43.82) 56(84) bytes of data.
  64 bytes from host2 (192.168.43.82): icmp_seq=1 ttl=64 time=3.00 ms
  64 bytes from host2 (192.168.43.82): icmp_seq=2 ttl=64 time=3.81 ms

  --- host2 ping statistics --  2 packets transmitted, 2 received, 0% packet loss, time 1001ms
  rtt min/avg/max/mdev = 3.001/3.403/3.806/0.402 ms
```

_/etc/hosts_ also manages domain names, so you can give your LAN a cool domain. In
the following examples, that is _sqr3l.nut_ . First enter the IP address, then the fully
qualified domain name (FQDN), then the hostname:

```
  127.0.0.1 localhost
  ::1 localhost ip6-localhost ip6-loopback
  192.168.43.81 host1.sqr3l.nut host1
  192.168.43.82 host2.sqr3l.nut host2
  192.168.43.83 host3.sqr3l.nut host3
```

Now your hosts can connect to each other with their hostnames, like _host1_, or their
FQDNs, like _host1.sqr3l.nut_ .

**Shared and Individual Hosts Entries**

You can have both shared and private entries in _/etc/hosts_ . Any‐
thing you want shared must be copied to all the relevant hosts.
Anything else in your hosts file that is not copied to other hosts will
work only for you. See Recipe 16.2 to learn more.

**Discussion**

_127.0.0.1 localhost_ and _::1 localhost ip6-localhost ip6-loopback_ are required. Yours
might look a little different, but however they are written, do not delete them. They
are assigned to the loopback device, a special virtual network interface that your
Linux system uses to communicate with itself.

**16.1 Simple Name Resolution with /etc/hosts** **|** **369**

You can ping them and use them to connect to local servers. For example, when you
use the CUPS web administration page, you are using the loopback device. Enter
_127.0.0.1:631_ or _localhost:631_ to open it (Figure 16-1).

_Figure 16-1. Opening a local web page with the loopback device_

The virtual network interface for the loopback device is _lo_ . Use the _ip_ command to
see it:

```
  $ ip addr show dev lo
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group
  default qlen 1000
  link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
  inet 127.0.0.1/8 scope host lo
  valid_lft forever preferred_lft forever
  inet6 ::1/128 scope host
  valid_lft forever preferred_lft forever
```

Your system does not need a physical network interface for the loopback device
to work.

Use the _hostname_ command to confirm that your configuration is correct. Check the
hostname of your computer:

```
  $ hostname
  host1
```

Check the FQDN:

```
  $ hostname -f
  host1.sqr3l.nut
```

Check the domain name:

```
  $ hostname -d
  sqr3l.nut
```

_/etc/hosts_ does not scale well, but for small networks it may be all you ever need for
your local DNS.

**370** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

**See Also**

 - _man 5 hosts_

 - _man 8 ping_

 - Recipe 16.2

**16.2 Using /etc/hosts for Testing and Blocking**
**Annoyances**

**Problem**

You are working on development servers, and you want to manage their DNS
without hassles. Or, you want a simple way to block annoying sites.

**Solution**

Suppose the name of a dev server you are working on is _dev.stashcat.com_ . Make an
entry for it your _/etc/hosts_ file:

```
  192.168.10.15 dev.stashcat.com
```

You don’t have to bother your network admin or mess with your DNS server, but can
create and remove entries in _/etc/hosts_ as you need.

Another fun trick is to map annoying websites to bogus IP addresses:

```
  12.34.56.78 badsite.com
  12.34.56.78 www.badsite.com
```

This makes the site unreachable from your computer. Most how-tos use the loopback
address, 127.0.0.1, and it works, but I prefer to keep the annoying sites separate. You
can use the same fake IP address for multiple annoying sites.

If your web browser still reaches the site after adding it to _/etc/hosts_, clear your
browser cache and try again.

**Discussion**

When you run a LAN Dnsmasq server, keep in mind that all entries in _/etc/hosts_ on
the Dnsmasq server will be applied to all Dnsmasq clients, so don’t put your name
server on your development computer.

**16.2 Using /etc/hosts for Testing and Blocking Annoyances** **|** **371**

Linux has a number of DNS managers, and _/etc/hosts_ is read first. The order is set in
the _/etc/nsswitch.conf_ file on the _hosts_ line. The following example is from Ubuntu
20.04:

```
  hosts: files mdns4_minimal [NOTFOUND=return] dns mymachines
```

_files_ is _/etc/hosts_ .

_mdns4_minimal_ uses the Avahi autodiscovery service to locate network services.

_[NOTFOUND=return]_ means that if _mdns4_minimal_ is working but the requested
host is not found, the DNS lookup should stop and return an error. If the
_mdns4_minimal_ service is not found, continue the lookup.

_dns_ uses any available DNS server.

_mymachines_ refers to the _systemd-machined_ service, which tracks local virtual
machines and containers.

You should put _files dns_ first on your Dnsmasq server.

**See Also**

 - _man 5 hosts_

 - _man 5 nsswitch.conf_

 - _man 8 systemd-machined.service_

**16.3 Finding All DNS and DHCP Servers on Your Network**

**Problem**

You want to know if there are any DNS and DHCP servers on your LAN, other than
your Dnsmasq server.

**Solution**

Probe your LAN with _nmap_ . The following example searches the local network for all
open TCP ports and finds an open TCP port 53, which is used by DNS. This is indi‐
cated by “53/tcp open domain”:

```
  $ sudo nmap --open 192.168.1.0/24
  Starting Nmap 7.70 ( https://nmap.org ) at 2021-05-23 13:25 PDT
  [...]
  Nmap scan report for dns-server.sqr3l.nut (192.168.1.10)
  Host is up (0.12s latency).
  Not shown: 998 filtered ports
  Some closed ports may be reported as filtered due to --defeat-rst-ratelimit

```

**372** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

```
  PORT  STATE SERVICE
  22/tcp open ssh
  53/tcp open domain
  [...]

  Nmap done: 256 IP addresses (3 hosts up) scanned in 81.38 seconds
```

By default, _nmap_ only looks for TCP ports. DNS servers listen to TCP and UDP 53,
and DHCP listens on UDP 67. The following example looks only for ports UDP 53
and 67:

```
  $ sudo nmap -sU -p 53,67 192.168.1.0/24
  Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-27 18:05 PDT

  Nmap scan report for dns-server.sqr3l.nut (192.168.1.10)
  Host is up (0.085s latency).

  PORT  STATE     SERVICE
  53/udp open     domain
  67/udp open|filtered dhcps

  Nmap done: 256 IP addresses (3 hosts up) scanned in 13.85 seconds
```

_nmap_ found one DNS/DHCP server, on dns-server.sqr3l.nut.

The following command searches for all open TCP and UDP ports on the network:

```
  $ sudo nmap -sU -sT 192.168.1.0/24
```

This takes several minutes to complete, and then you have a list of the active services
on all up hosts in your network, including any services running on nonstandard
ports.

**Discussion**

Be very careful with port scanning, and use it only on networks that you have permis‐
sion for. Port scanning other networks is often treated as a hostile act, like you are
probing for vulnerabilities to exploit.

Multiple name servers can cause conflicts, and in any case it is good to know if your
users are running any servers.

On most Linux systems, the package to install is _nmap_ .

**See also**

 - _man 1 nmap_

**16.3 Finding All DNS and DHCP Servers on Your Network** **|** **373**

**16.4 Installing Dnsmasq**

**Problem**

You want to install Dnsmasq and take care of any prerequisites.

**Solution**

Install the _dnsmasq_ package. In this recipe the Dnsmasq server is named _dns-server_ .
You will use both Dnsmasq and the _/etc/hosts_ file to configure your DNS server.

After installation, stop Dnsmasq if it is running:

```
  $ systemctl status dnsmasq.service
```

   - `dnsmasq.service - dnsmasq - A lightweight DHCP and caching DNS server`
```
  Loaded: loaded (/lib/systemd/system/dnsmasq.service; enabled; vendor
  preset: enabled)
  Active: active (running) since Mon 2021-05-24 05:49:36 PDT; 6h ago
  [...]
  $ sudo systemctl stop dnsmasq.service
```

Give your Dnsmasq server a static IP address, if it does not already have one. Do this
with NetworkManager’s graphical control panel ( _nm-connection-editor_ ), or with the
_nmcli_ command.

The following example uses _nmcli_ to find your active connections:

```
  $ nmcli connection show --active
  NAME    UUID           TYPE   DEVICE
  1local   3e348c97-4c5f-4bbf-967e wifi    wlan1
  1wired   0460d735-e14d-3c3f-92c0 ethernet  eth1
```

Then assign the static IP address you want your DNS server to use, using the NAME
to identify the correct connection:

```
  $ nmcli con mod " 1wired " \
  ipv4.addresses " 192.168.1.30/24 " \
  ipv4.gateway " 192.168.1.1 " \
  ipv4.method "manual"
```

Then restart NetworkManager:

```
  $ sudo systemctl restart NetworkManager.service
```

Next, check if your Linux is running _systemd-resolved.service_ :

```
  $ systemctl status systemd-resolved.service
```

If it is, see Recipe 16.5 before configuring Dnsmasq, and also to learn how to config‐
ure NetworkManager on your Dnsmasq server.

**374** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

**Discussion**

systemd is implemented differently amongst the various Linuxes. For example, open‐
SUSE Leap 15.2 does not use the _systemd-resolved.service_, so you should not have to
make any systemd changes to enable Dnsmasq to control your LAN DNS. Fedora 33
and up, and Ubuntu 17.04 and up, run _systemd-resolved.service_, and it should be dis‐
abled on your Dnsmasq server.

**See Also**

 - Recipe 16.5

 - [Dnsmasq](https://oreil.ly/vvfHg)

**16.5 Making systemd-resolved and NetworkManager Play**
**Nice with Dnsmasq**

**Problem**

_systemd-resolved_ and NetworkManager are conflicting with Dnsmasq, and you want
them out of the way.

**Solution**

Check if the _systemd-resolved.service_ is running:

```
  $ systemctl status systemd-resolved.service

```

   - `systemd-resolved.service - Network Name Resolution`
```
  Loaded: loaded (/usr/lib/systemd/system/systemd-resolved.service; enabled;
  vendor preset: enabled)
  Active: active (running) since Sat 2021-05-22 12:57:34 PDT; 1min 21s ago
  [...]
```

That shows that it is running. _systemd-resolved.service_ is fine for providing a stub
DNS resolver for client machines, but not DNS servers. Disable it:

```
  $ sudo systemctl stop systemd-resolved.service
  $ sudo systemctl disable systemd-resolved.service
```

Then look at _/etc/resolv.conf_, which should be a symlink:

```
  $ ls -l /etc/resolv.conf
  lrwxrwxrwx 1 root root 39 May 21 20:38 /etc/resolv.conf ->
  ../run/systemd/resolve/stub-resolv.conf

```

**16.5 Making systemd-resolved and NetworkManager Play Nice with Dnsmasq** **|** **375**

When it is a symlink, it is managed by _systemd-resolved.service_ . To remove control
from _systemd-resolved.service_, delete the symlink and create a plain-text file with the
same name:

```
  $ sudo rm /etc/resolv.conf
  $ sudo touch /etc/resolv.conf
```

Now that _/etc/resolv.conf_ is a file and not a symlink, it is managed by NetworkMan‐
ager. Open your NetworkManager configuration file and look for the _[main]_ section,
then add or change the _dns=_ value to _none_ :

```
  $ sudo nano /etc/NetworkManager/NetworkManager.conf

  [main]
  dns=none
```

Enter your Dnsmasq server’s IPv4 and IPv6 localhost addresses in _/etc/resolv.conf_ and
your local domain, if you have one:

```
  search sqr3l.nut
  nameserver 127.0.0.1
  nameserver ::1
```

Then reboot and configure your new Dnsmasq installation.

**Discussion**

NetworkManager and _systemd-resolved_ are wonderful on client machines. On your
Dnsmasq server, you must have control of _/etc/resolv.conf_, and Dnsmasq should be
the only stub resolver.

**See Also**

 - _man 8 systemd-resolved.service_

 - _man 8 networkmanager_

**16.6 Configuring Dnsmasq for LAN DNS**

**Problem**

You want to set up Dnmasq as your LAN DNS server.

**Solution**

Any hosts that you enter in _/etc/hosts_ need static IP addresses, and Dnsmasq will
automatically enter them into DNS. At a minimum, enter your Dnsmasq server. The

**376** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

following example includes the Dnsmasq server, a backup server, and an internal web
server:

```
  127.0.0.1 localhost
  ::1 localhost ip6-localhost ip6-loopback
  192.168.43.81 dns-server
  192.168.43.82 backups
  192.168.43.83 https

```

**Configure Static Hosts from DHCP**

See Recipe 16.12 to learn how to manage static IP address assign‐
ments from DHCP, instead of _/etc/hosts_ .

Now it is time to configure Dnsmasq. Rename the default configuration file so you
can start with a new empty file, and use the original as a reference:

```
  $ sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf-old
  $ sudo nano /etc/dnsmasq.conf
```

Copy the following configuration, replacing the second _listen-address_ with your own
server’s IP address, and use your own domain name. The upstream name servers are
OpenDNS, and you may use whatever upstream name servers you wish. Dnsmasq
looks for _/etc/resolv.conf_ by default, but it doesn’t hurt to be explicit:

```
  # global options
  resolv-file=/etc/resolv.conf
  domain-needed
  bogus-priv
  expand-hosts
  domain= sqr3l.nut
  local=/ sqr3l.nut /
  listen-address=127.0.0.1
  listen-address= 192.168.43.81

  # upstream name servers
  server= 208.67.222.222
  server= 208.67.220.220
```

Run Dnsmasq’s syntax checker:

```
  $ dnsmasq --test
  dnsmasq: syntax check OK.
```

The syntax checker won’t find configuration errors, but only typos. Start up
Dnsmasq, and if there are errors it will not start. The following example shows a suc‐
cessful start:

```
  $ sudo systemctl start dnsmasq.service
  $ systemctl status dnsmasq.service
```

   - `dnsmasq.service - dnsmasq - A lightweight DHCP and caching DNS server`

**16.6 Configuring Dnsmasq for LAN DNS** **|** **377**

```
  Loaded: loaded (/lib/systemd/system/dnsmasq.service; enabled; vendor preset:
  enabled)
  Active: active (running) since Mon 2021-05-24 17:13:48 PDT; 1min 0s ago
  Process: 11023 ExecStartPre=/usr/sbin/dnsmasq --test (code=exited,
  status=0/SUCCESS)
  Process: 11024 ExecStart=/etc/init.d/dnsmasq systemd-exec (code=exited,
  status=0/SUCCESS)
  Process: 11033 ExecStartPost=/etc/init.d/dnsmasq systemd-start-resolvconf
  (code=exited, status=0/SUCCESS)
  Main PID: 11032 (dnsmasq)
  Tasks: 1 (limit: 18759)
  Memory: 2.5M
  CGroup: /system.slice/dnsmasq.service
  └─11032 /usr/sbin/dnsmasq -x /run/dnsmasq/dnsmasq.pid -u dnsmasq -7
  /etc/dnsmasq.d,.dpkg-dist,.dpkg-old,.dpkg-new --local->

  May 24 17:13:48 dns-server systemd[1]: Starting dnsmasq - A lightweight DHCP and
  caching DNS server...
  May 24 17:13:48 dns-server dnsmasq[11023]: dnsmasq: syntax check OK.
  May 24 17:13:48 dns-server systemd[1]: Started dnsmasq - A lightweight DHCP and
  caching DNS server.
```

Run some tests on your Dnsmasq server with _nslookup_ using your server’s hostname
and FQDN:

```
  $ nslookup dns-server
  Server:     127.0.0.1
  Address:    127.0.0.1#53

  Name:  dns-server
  Address: 192.168.43.81

  $ nslookup dns-server.sqr3l.nut
  Server:     127.0.0.1
  Address:    127.0.0.1#53

  Name:  dns-server.sqr3l.nut
  Address: 192.168.43.81

  $ nslookup 192.168.43.81
  18.43.168.192 .in-addr.arpa    name = host1.sqr3l.nut.
```

Use the _ss_ command to verify the listening ports. In the following example, the
Recv-Q, Send-Q, and Peer Address:Port columns have been removed for clarity:

```
  $ sudo ss -lp "sport = :domain"
  Netid State  Local Address:Port  Process
  udp  UNCONN   127.0.0.1:domain  users:(("dnsmasq",pid=1531,fd=8))
  udp  UNCONN  192.168.1.10 :domain  users:(("dnsmasq",pid=1531,fd=6))
  tcp  LISTEN   127.0.0.1:domain  users:(("dnsmasq",pid=1531,fd=9))
  tcp  LISTEN  192.168.1.10 :domain  users:(("dnsmasq",pid=1531,fd=7))

```

**378** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

You should see your server address, localhost address, and only _dnsmasq_ in the Pro‐
cess column. Add the _-r_ option to see hostnames instead of IP addresses.

When all of these commands succeed, your configuration is correct.

**Discussion**

If Dnsmasq fails to start, run _journalctl -ru dnsmasq_ to see why. (If your Dnsmasq
logs are sent somewhere else, then look there; see Recipe 16.14.)

_nslookup_ is in the _bindutils_ package.

_ss_, socket statistics, is in the _iproute2_ package.

If your _nslookup_ commands fail, try restarting networking, and then restarting
Dnsmasq. If they still fail, reboot. If this doesn’t fix it, recheck all your configurations.

_domain-needed_ prevents Dnsmasq from forwarding queries for your plain hostnames
to upstream nameservers. If the name is not known from _/etc/hosts_ or DHCP, then a
“not found” answer is returned. This keeps requests for your LAN addresses from
leaking out into the world and possibly being answered incorrectly if your LAN
domain is the same as a public domain name.

_bogus-priv_ blocks bogus private reverse lookups. All reverse lookups for private IP
ranges which are not found in _/etc/hosts_ or the DHCP leases file are answered with
“no such domain” rather than being forwarded upstream.

_expand-hosts_ automatically adds your private domain name to the plain hostnames
in _/etc/hosts_ .

_domain=_ is your local domain name.

_local=/[domain]/_ tells Dnsmasq to resolve queries for the local domain directly, and
not forward them upstream.

**See Also**

 - _man 5 hosts_

 - [Dnsmasq](https://oreil.ly/vvfHg)

**16.7 Configuring firewalld to Allow DNS and DHCP**

**Problem**

You need to open your Dnsmasq server’s firewall to allow your LAN clients access
to it.

**16.7 Configuring firewalld to Allow DNS and DHCP** **|** **379**

**Solution**

Open TCP and UDP ports 53 for DNS, and UDP 67 for DHCP. If you are running
_firewalld_, use this command:

```
  $ sudo firewall-cmd --permanent --add-service=\{dns,dhcp\}
```

**Discussion**

One of the first things to check, when you have connectivity problems, is firewall
settings.

**See Also**

 - Chapter 14

**16.8 Testing Your Dnsmasq Server from a Client Machine**

**Problem**

You want to test your nice new Dnsmasq DNS server from a client computer.

**Solution**

Use the _dig_ command from any host on your network to query any website, via the IP
address for your Dnsmasq server:

```
  $ dig @ 192.168.1.10 oreilly.com

  ; <<>> DiG 9.16.6 <<>> @ 192.168.1.10 oreilly.com
  ; (1 server found)
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29387
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; udp: 4096
  ;; QUESTION SECTION:
  ;oreilly.com.          IN   A

  ;; ANSWER SECTION:
  oreilly.com.      240   IN   A    199.27.145.65
  oreilly.com.      240   IN   A    199.27.145.64

  ;; Query time: 108 msec
  ;; SERVER: 192.168.1.10 #53( 192.168.1.10 )

```

**380** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

```
  ;; WHEN: Mon May 24 17:49:32 PDT 2021
  ;; MSG SIZE rcvd: 72
```

That is a successful test, confirmed by “status: NOERROR” and the SERVER line
showing the IP address of your Dnsmasq server.

**Discussion**

You can also test using your server’s hostname and fully qualified domain name
(FQDN):

```
  $ dig @ dns-server oreilly.com
  $ dig @ dns-server.sqr3l.nut oreilly.com
```

**See Also**

 - _man 1 dig_

**16.9 Managing DHCP with Dnsmasq**

**Problem**

Your DNS is working, and now you want to set up DHCP.

**Solution**

No problem. Add these lines to your _/etc/dnsmasq.conf_ file to define a single pool of
addresses, substituting your own desired addressing:

```
  # DHCP range
  dhcp-range= 192.168.1.25,192.168.1.75,12h
  dhcp-lease-max= 25
```

Restart Dnsmasq:

```
  $ sudo systemctl restart dnsmasq.service
```

Try getting an address on a LAN computer. First, make sure it is configured to get its
IP address via DHCP:

```
  $ nmcli con show --active
  NAME  UUID           TYPE   DEVICE
  1net   de7c00e7-8e4d-45e6-acaf ethernet eth0

  $ nmcli con show 1net | grep ipv..method
  ipv4.method:      auto
  ipv6.method:      auto

```

**16.9 Managing DHCP with Dnsmasq** **|** **381**

_auto_ confirms it is a DHCP client. (If it says _manual_ then it is not.) Bring the interface
down, then back up again:

```
  $ sudo nmcli con down 1net
  Connection '1net' successfully deactivated (D-Bus active path: /org/freedesktop/
  NetworkManager/ActiveConnection/11

  $ sudo nmcli con up 1net
  Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkMan
  ager/ActiveConnection/15)
```

Check your Dnsmasq server logs:

```
  $ journalctl -ru dnsmasq
  -- Logs begin at Sun 2021-02-28 14:35:01 PST, end at Mon 2021-05-31 17:36:04
  PDT. -  May 31 17:34:56 dns-server dnsmasq-dhcp[8080]: DHCPACK(eth0) 192.168.1.45
  9c:ef:d5:fe:01:7c client2
  May 31 17:34:56 dns-server dnsmasq-dhcp[8080]: DHCPREQUEST(eth0) 192.168.1.45
  9c:ef:d5:fe:01:7c
```

That shows a successful IP address assignment from _dns-server_ to _client2_ .

**Discussion**

You can use the NetworkManager panel applet instead of _nmcli_, or run the _nm-_
_connection-editor_ command to open NetworkManager’s graphical configurator, then
disconnect and connect with a mouse click (Figure 16-2).

Most Linux distributions use NetworkManager to control client DHCP. If yours does
not, it probably uses _dhclient_ . Look for a _dhclient.conf_ configuration file, if this exists,
then request a new lease with the _dhclient_ command:

```
  $ sudo dhclient -v
  Internet Systems Consortium DHCP Client 4.3.6-P1
  Copyright 2004-2018 Internet Systems Consortium.
  All rights reserved.
  For info, please visit https://www.isc.org/software/dhcp/

  Listening on LPF/ eth0/9c:ef:d5:fe:01:7c
  Sending on  LPF/ eth0/9c:ef:d5:fe:01:7c
  Sending on  Socket/fallback
  DHCPREQUEST on eth0 to 255.255.255.255 port 67 (xid=0xec8923)
  DHCPACK from 192.168.1.10 (xid=0xec8923)
  bound to 192.168.1.27 -- renewal in 1415 seconds.
```

You can send, over DHCP, some of the information your client machines need to
access network services. See Recipe 16.10 to learn more.

**382** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

_Figure 16-2. Managing network connections with nm-connection-editor_

_dhcp-range=192.168.1.25,192.168.10.75,24h_ defines a range of 50 available address
leases, with a lease time of 24 hours. This range must not include your Dnsmasq
server, nor any hosts with static IP addresses. Define the lease time in seconds,
minutes, or hours. The default is one hour, and the minimum is two minutes. If you
want leases that never expire, don’t specify a lease time.

_dhcp-lease-max=25_ defines how many leases can be active at one time. You can have a
large address pool available, and then limit the number of active leases.

**See Also**

 - Recipe 16.10

 - [Dnsmasq](https://oreil.ly/vvfHg)

 - _man 8 dhclient_

**16.10 Advertising Important Services over DHCP**

**Problem**

You want to advertise various servers to your LAN clients over DHCP.

**16.10 Advertising Important Services over DHCP** **|** **383**

**Solution**

Some services, like the default route to your internet gateway, DNS server, and NTP
server, can be advertised to your LAN clients so that they automatically use them. The
following examples show how to configure _/etc/dnsmasq.conf_ to advertise some
services.

Set the default router:

```
  dhcp-option=3, 192.168.1.1
```

Advertise your DNS server:

```
  dhcp-option=6, 192.168.1.10
```

This example points the way to your local NTP server:

```
  dhcp-option=42, 192.168.1.11
```

How do you know which numbers to use? Use this command to list all of them:

```
  $ dnsmasq --help dhcp
  Known DHCP options:
  1 netmask
  2 time-offset
  3 router
  6 dns-server
  7 log-server
  9 lpr-server
  [...]
```

**Discussion**

_dnsmasq --help dhcp_ displays the known DHCPv4 configuration options. See the Dis‐
cussion in Recipe 16.11 for more information on the DHCPv4 configuration options.

**See Also**

 - [Dnsmasq](https://oreil.ly/vvfHg)

**16.11 Creating DHCP Zones for Subnets**

**Problem**

You have two subnets, and you want to configure Dnsmasq to apply different options
to them, such as different default routers and servers.

**384** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

**Solution**

Define your zones with whatever names you want to give them, like _zone1_ and _zone2_,
and set their address ranges:

```
  dhcp-range= zone1,192.168.50.20,192.168.50.120
  dhcp-range= zone2,192.168.60.20,192.168.60.50,24h
```

The two zones have different routers:

```
  dhcp-option= zone1,3,192.168.50.1
  dhcp-option= zone2,3,192.168.60.2
```

They use the same DNS server:

```
  dhcp-option= zone1,6,192.168.1.10
  dhcp-option= zone2,6,192.168.1.10
```

_zone2_ gets an NTP server:

```
  dhcp-option= zone2,42,192.168.60.15
```

**Discussion**

Only a few of the DHCP options are useful. They are very old, and some are mysteri‐
ous, for example:

option default-url string;

The format and meaning of this option is not described in any standards document,
but is claimed to be in use by Apple Computer. It is not known what clients may rea‐
sonably do if supplied with this option. Use at your own risk.

—man 5 DHCP options

Client support is inconsistent for many of them. The only ones I use are NTP, routers,
and DNS servers.

**See Also**

 - _man 5 dhcp_

 - [Dnsmasq](https://oreil.ly/vvfHg)

**16.12 Assigning Static IP Addresses from DHCP**

**Problem**

You want to centralize IP addressing as much as possible, including assigning static IP
addresses.

**16.12 Assigning Static IP Addresses from DHCP** **|** **385**

**Solution**

Use the _dhcp-host_ option in _/etc/dnsmasq.conf_ . Identify the client machine by its host‐
name, and assign an unused address from your LAN’s address block. (It is not neces‐
sary to use the DHCP address range you defined with the __dhcp-range=_ - option
in _/etc/dnsmasq.conf_ for static addresses.) The following example assigns an address
to _server2_ in the 192.168.3.0/24 network:

```
  dhcp-host= server2,192.168.3.45
```

Restart Dnsmasq, then the next time _server2_ requests an address it will receive the
address specified by the _dhcp-host=_ option.

Use multiple _dhcp-host=_ lines to configure multiple clients, one per line.

You may use the client’s MAC address in place of the hostname.

**Discussion**

In general, centralizing administration chores saves time and headaches.

**See Also**

 - [Dnsmasq](https://oreil.ly/vvfHg)

**16.13 Configuring DHCP Clients for Automatic DNS Entries**

**Problem**

You want your DHCP clients to be entered into DNS automatically by Dnsmasq.

**Solution**

The only thing the clients have to do is send their hostnames to Dnsmasq’s DHCP
server, which is the default in most Linuxes.

Suppose a DHCP client on the local _sqr3l.nut_ domain has the host name _client4_ . _cli‐_
_ent4_ starts up, and receives its IP address and other network information from
Dnsmasq. Dnsmasq receives _client4_ ’s hostname and enters it into DNS. Now other
hosts on the network can access _client4_ and _client4.sqr3l.nut_ .

There must not be any duplicate entries for _client4_ in _/etc/hosts_ .

There are three different ways to check your DHCP client configuration: in
_dhclient.conf_, NetworkManager’s graphical configuration tool ( _nm-connection-editor_ ),
and with the _nmcli_ command.

**386** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

First check _dhclient_, which has been the default DHCP client on Linux for years. On
most Linux systems its configuration file is _/etc/dhcp/dhclient.conf_ . Look for this line,
which automatically finds the system’s hostname and sends it to the DHCP server:

```
  send host-name = gethostname();
```

Or a line like this, specifying the system’s hostname:

```
  send host-name = myhostname
```

If there is no _dhclient.conf_ file, then NetworkManager is your DHCP client manager.
You can check this in your graphical _nm-connection-editor_ (Figure 16-3).

_Figure 16-3. NetworkManager sends client hostname to DHCP server_

When the connection method is “Automatic (DHCP),” NetworkManager sends the
hostname to the DHCP server. “Automatic (addresses only)” does not send the host‐
name to the DHCP server, but only provides DNS to the client.

You may also use the _nmcli_ command. First, find your active network connection:

```
  $ nmcli connection show --active
  NAME  UUID                 TYPE   DEVICE
  wifi1  3e348c97-4c5f-4bbf-967e-7624f3e1e4f0  wifi    wlan1
```

Then verify that it sends the hostname to your DHCP server. The following example
confirms that it does:

```
  $ nmcli connection show wifi1 | grep send-hostname
  ipv4.dhcp-send-hostname:        yes
  ipv6.dhcp-send-hostname:        yes
```

If it says _no_, run the following commands to set it to _yes_ . After that, reload the
configuration:

```
  $ sudo nmcli con mod wifi1 ipv4.dhcp-send-hostname yes
  $ sudo nmcli con mod wifi1 ipv6.dhcp-send-hostname yes
  $ sudo nmcli con reload

```

**16.13 Configuring DHCP Clients for Automatic DNS Entries** **|** **387**

**Discussion**

If you prefer a graphical tool to manage NetworkManager, it’s best to use Network‐
Manager’s graphical configuration utility, _nm-connection-editor_, rather than a differ‐
ent graphical tool, such as the network module in the GNOME control panel. The
_nm-connection-editor_ offers the most complete configuration options, and it is the
same on all Linux distros.

**See Also**

 - _man 1 nmcli_

 - _man 1 nmcli-examples_

 - _man 5 nm-settings_

**16.14 Managing Dnsmasq Logging**

**Problem**

Dnsmasq has the option to send its messages to a file of your choice using the legacy
_syslog_ daemon, rather than to _journalctl_, and you want to know which is the best
option.

**Solution**

It does not matter which one you use: the same information is logged either way. The
default behavior is to log to the systemd journal.

It can be convenient to isolate Dnsmasq logs in their own directory, such as _/var/log/_
_dnsmasq/dnsmasq.log_ . Use the _log-facility=_ option in _/etc/dnsmasq.conf_ to specify the
log file you want to use, then restart Dnsmasq. The file must already exist or
Dnsmasq will not start.

Your logfile will grow very large unless you set up log rotation. The following exam‐
ple configuration, _/etc/logrotate.d/dnsmasq_, sets up a simple weekly rotation:

```
  /var/log/dnsmasq/dnsmasq.log {
  missingok
  compress
  notifempty
  rotate 4
  weekly
  create
  }

```

**388** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

Test it with the _logrotate_ command:

```
  $ sudo /etc/logrotate.conf --debug
  [...]
  rotating pattern: /var/log/dnsmasq/dnssmasq.log weekly (4 rotations)
  empty log files are not rotated, old logs are removed
  switching euid to 0 and egid to 4
  considering log /var/log/dnsmasq/dnssmasq.log
  Creating new state
  Now: 2021-06-01 13:08
  Last rotated at 2021-06-01 13:00
  log does not need rotating (log has been already rotated)
  switching euid to 0 and egid to 0
  [...]
```

This shows no errors and it is working correctly.

**Discussion**

systemd supports both _journalctl_ and the _syslog_ daemon. They will probably exist
together for a long time, so you can set up logging in whatever way you prefer.

**See Also**

 - _man 8 rsyslog_

 - [Dnsmasq](https://oreil.ly/vvfHg)

 - _man 1 journalctl_

 - Chapter 20

**16.15 Configuring Wildcard Domains**

**Problem**

You want to create a wildcard domain in Dnsmasq, so that requests for the domain’s
subdomains resolve without manually adding the subdomains to your DNS.

**Solution**

Use the _address_ option in _/etc/dnsmasq.conf_ to create the top-level domain (TLD):

```
  address=/ wildcard.net/192.168.1.35
```

Restart Dnsmasq, then run _nslookup_ to test:

```
  $ sudo systemctl restart dnsmasq.service
  $ nslookup foo.wildcard.net
  Server:     127.0.0.1

```

**16.15 Configuring Wildcard Domains** **|** **389**

```
  Address:    127.0.0.1#53

  Name:  foo.wildcard.net
  Address: 192.168.1.35
```

_foo.wildcard.net_ resolves, showing that it works.

**Discussion**

Use DNS wildcards carefully. Wildcards are useful when you’re doing development
work on complex services such as Kubernetes. Make sure to use address ranges that
are different from the ranges on your LAN’s name server, and are available only to
LAN clients.

**See Also**

 - [Dnsmasq](https://oreil.ly/vvfHg)

**390** **|** **Chapter 16: Managing Local Name Services with Dnsmasq and the hosts File**

**<u>CHAPTER 17</u>**
#### **Keeping Time with ntpd, chrony,** **and timesyncd**

Keeping accurate time on your computer, and on all hosts on your network, is easy
and automatic with NTP, the Network Time Protocol. NTP is implemented on Linux
with _ntpd_, the NTP daemon, _chrony_, the modern replacement for _ntpd_, and systemd’s
_timesyncd_ . That is right, friends, there are three (at least), count them, three ways to
automatically manage time on your Linux computer.

_ntpd_ and _chrony_ can also function as LAN time servers, while _timesyncd_ is a simpler
lightweight client with no server functions. _ntpd_ and _chrony_ are full NTP implemen‐
tations, while _timesyncd_ uses SNTP, the Simple Network Time Protocol.

Most Linux distributions provide a default configuration that points to time servers
that they maintain. These servers have names like _2.fedora.pool.ntp.org_ and
_0.ubuntu.pool.ntp.org_ . You don’t have to do anything, except be sure to not disable this
during installation. In this chapter you will learn how to check your current settings,
how to change them, and how to set up a LAN time server.

There is a worldwide network of time servers that are free for everyone to use, and
they are organized into _strata_, starting at stratum 0. Stratum 0 is the source for all
timekeeping, a network of atomic clocks, radio receivers tuned to atomic clocks, and
GPS receivers using signals broadcast by GPS satellites.

Next in line is stratum 1, where the primary time servers reside. The primary time
servers in stratum 1 are directly connected to the sources in stratum 0.

Stratum 2 contains thousands of public servers, and they sync with stratum 1. It is
good etiquette to connect to stratum 2 servers to prevent the stratum 1 servers from
being overwhelmed and to not use the stratum 1 servers without a good reason.

**391**

The hierarchy continues on down the line, for example there are stratum 4, 5, and 6
public servers, and private LAN servers that sync with them. It’s not really that
orderly; you can designate your private LAN NTP server as stratum 10, and it doesn’t
have to connect to stratum 9 servers, but any server it can reach. You don’t have to
worry about selecting the correct servers because you will use _pool_ servers, which are
clusters of NTP servers, rather than individual servers.

When you dig into timekeeping on computers, it becomes confusing and overwhelm‐
[ing, or perhaps fascinating, depending on how nerdy you want to get. Visit the NTP](https://ntppool.org)
[Pool Project and NTP: The Network Time Protocol to learn the nerdy stuff and how](https://ntppool.org)
to run your own public time server.

There are at least two timekeepers on your Linux system. One is the hardware clock
on your motherboard, which is also called the real-time clock (RTC). The other is
system time, managed by your Linux kernel. The RTC always has power, even when
your machine is turned off, from a battery or capacitor on the motherboard. When
your Linux computer starts up, your selected NTP client gets its time from the RTC.
Then, after the network is available, it corrects the time according to its upstream
time server.

Your RTC time is set in your BIOS/UEFI, and with some of the commands you will
learn about in this chapter. It should always be set to UTC, Coordinated Universal
Time, and then the Linux kernel calculates the time for your time zone from the
UTC. UTC is similar to Greenwich Mean Time (GMT), though they are not the
same. UTC is a time standard and GMT is a time zone. Neither UTC nor GMT
change for daylight saving time (DST).

[Time zone data comes from IETF.org Timezones. This is a moving target as countries](https://oreil.ly/gUnet)
change their DST dates, opt out of DST, and opt back in. Most Linuxes store this
information in _/usr/share/zoneinfo/_ . The Internet Engineering Task Force (IETF)
tracks these changes and makes their databases freely available.

**17.1 Finding Which NTP Client Is on Your Linux System**

**Problem**

You read the chapter introduction, and now you know that time synchronization on
Linux is managed by _ntpd_, _chrony_, or _timesyncd_, and you need to know which one
your Linux system uses.

**Solution**

Use the _ps_ command to see if any of the three time synchronization daemons, _ntpd_,
_chronyd_, or _timesyncd_ are running on your system:

**392** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

```
  $ ps ax|grep -w ntp
  $ ps ax|grep -w chrony
  $ ps ax|grep -w timesyncd
```

If any of these are running, skip ahead to the relevant recipes in this chapter to learn
how to manage your time daemon.

If none of these are running, see if your system is using _timedatectl_, which is part of
systemd:

```
  $ timedatectl status
  Local time: Sun 2020-10-04 10:59:48 PDT
  Universal time: Sun 2020-10-04 17:59:48 UTC
  RTC time: Sun 2020-10-04 17:59:48
  Time zone: America/Los_Angeles (PDT, -0700)
  System clock synchronized: no
  systemd-timesyncd.service active: no
  RTC in local TZ: no
```

This output shows that _timedatectl_ is running without any time daemons, indicated
by _systemd-timesyncd.service active: no_ . Double-check by querying the status of
_systemd-timesyncd_ :

```
  $ systemctl status systemd-timesyncd
```

   - `systemd-timesyncd.service - Network Time Synchronization`
```
  Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; disabled;
  vendor preset: enabled)
  Active: inactive (dead)
  Docs: man:systemd-timesyncd.service(8)
```

This shows that _systemd-timesyncd_ is not running, which means there is no time syn‐
chronization on your system, and it is getting its time from your system’s real-time
clock (RTC). In this case you need to set up _ntpd_, _chrony_, or _timesyncd_ .

**Discussion**

Some Linux distributions do not use systemd; see Recipe 4.1 to learn how to know if
your Linux has it. If you are running a Linux system without systemd, your NTP
choices are _ntpd_ or _chrony_ .

If you find both _ntpd_ and _chrony_ running on the same system, get rid of _ntpd_, as
_chrony_ is newer, faster, and more reliable. Having both will create conflicts.

The output of _timedatectl_ has a lot of useful information. The example shows that the
RTC is correctly set to the Coordinated Universal Time (UTC) protocol, and that the
system time zone is Pacific Daylight Time, PDT. _systemd-timesyncd.service_ is not run‐
ning, and the system has not been synchronized.

**17.1 Finding Which NTP Client Is on Your Linux System** **|** **393**

**See Also**

 - [timedatectl: Control the system time and date](https://oreil.ly/QddJ7)

 - _man 1 ps_

**17.2 Using timesyncd for Simple Time Synchronization**

**Problem**

You want to know how to set up the simplest NTP client to keep the correct time on
your computer.

**Solution**

Enable synchronization with a public NTP server using the _systemd-timesyncd_ dae‐
mon, which requires systemd. Check the status of _systemd-timesyncd_ :

```
  $ systemctl status systemd-timesyncd
```

   - `systemd-timesyncd.service - Network Time Synchronization`
```
  Loaded: loaded (/usr/lib/systemd/system/systemd-timesyncd.service;
  disabled; vendor preset: enabled)
  Active: inactive (dead)
  Docs: man:systemd-timesyncd.service(8)
```

Enable it with _timedatectl_, and verify that _systemd-timesyncd_ started:

```
  $ timedatectl set-ntp true
  $ systemctl status systemd-timesyncd
```

   - `systemd-timesyncd.service - Network Time Synchronization`
```
  Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; enabled;
  vendor preset: enabled)
  Active: active (running) since Sun 2020-10-04 18:17:51 PDT; 16min ago
  Docs: man:systemd-timesyncd.service(8)
  Main PID: 3990 (systemd-timesyn)
  Status: "Synchronized to time server 91.189.89.198:123 (ntp.ubuntu.com)."
  Tasks: 2 (limit: 4915)
  CGroup: /system.slice/systemd-timesyncd.service
  └─3990 /lib/systemd/systemd-timesyncd

  Oct 04 18:17:51 pc systemd[1]: Starting Network Time Synchronization...
  Oct 04 18:17:51 pc systemd[1]: Started Network Time Synchronization.
  Oct 04 18:33:01 pc systemd-timesyncd[3990]: Synchronized to time server
  91.189.89.198:123 (ntp.ubuntu.com).
```

If _systemd-timesyncd_ did not start, start it:

```
  $ sudo systemctl start systemd-timesyncd

```

**394** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

Now see what _timedatectl_ reports:

```
  $ timedatectl status
  Local time: Sun 2020-10-04 18:35:56 PDT
  Universal time: Mon 2020-10-05 01:35:56 UTC
  RTC time: Mon 2020-10-05 01:35:56
  Time zone: America/Los_Angeles (PDT, -0700)
  System clock synchronized: yes
  systemd-timesyncd.service active: yes
  RTC in local TZ: no
```

Everything looks correct. Your system is synchronized, all the times are correct, and
the _systemd-timesyncd.service_ is active.

It is a good practice to configure multiple public time servers for redundancy.
Edit _/etc/systemd/timesyncd.conf_ to add more NTP servers by uncommenting the `NTP`
line and entering a space-delimited list of public server pools:

```
  [Time]
  NTP=0.north-america.pool.ntp.org 1.north-america.pool.ntp.org
  2.north-america.pool.ntp.org
  #FallbackNTP=ntp.ubuntu.com
  #RootDistanceMaxSec=5
  #PollIntervalMinSec=32
  #PollIntervalMaxSec=2048
```

**Discussion**

In your original _/etc/systemd/timesyncd.conf_ file, the commented options document
the default configuration.

The pool servers are highly reliable because they are multiple servers in a single pool,
rather than individual servers. For best peformance use the pool servers for your
[region, either the continental pools or the country pools, which you will find by click‐](https://oreil.ly/iEipo)
ing on the continental pool links.

Your Linux distribution may configure multiple server pools of their own, such as:

```
  0.opensuse.pool.ntp.org 1.opensuse.pool.ntp.org 2.opensuse.pool.ntp.org
```

This is good, and you don’t need to change it, but a more diverse configuration is
usually more reliable.

**See Also**

 - Chapter 4

 - [NTP Pool Project](https://ntppool.org)

 - _man 5 timesyncd.conf_

**17.2 Using timesyncd for Simple Time Synchronization** **|** **395**

**17.3 Setting Time Manually with timedatectl**

**Problem**

You want to set your system and RTC time manually.

**Solution**

Use _timedatectl_ . It sets the date, system time, and RTC time with a single command:

```
  $ timedatectl set-time "2020-10-04 19:30:00"
  Failed to set time: Automatic time synchronization is enabled
```

You cannot do this when _systemd-timesyncd_ is running, so you must stop it:

```
  $ sudo systemctl stop systemd-timesyncd
```

Then enter your new settings in the format shown in the example, YYYY-MM-DD
HH:MM:SS, and verify that it worked:

```
  $ timedatectl set-ntp false
  $ timedatectl set-time "2020-10-04 19:30:00"
  $ timedatectl status
  Local time: Sun 2020-10-04 19:30:06 PDT
  Universal time: Mon 2020-10-05 02:30:06 UTC
  RTC time: Mon 2020-10-05 02:30:06
  Time zone: America/Los_Angeles (PDT, -0700)
  System clock synchronized: no
  systemd-timesyncd.service active: no
  RTC in local TZ: no
```

If you restart _systemd-timesyncd_, it will override your manual settings.

**Discussion**

_timedatectl_ has a small set of commands. If you are used to the _date_ command for
setting the time, and other time and date operations, _timedatectl_ may seem light‐
weight. It is simple by design, and you still have _date_ and its numerous options for
complex tasks.

**See Also**

 - _man 5 timesyncd.conf_

**396** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

**17.4 Using chrony for Your NTP Client**

**Problem**

Your want a fully featured NTP client/server, and you want to know how to set up
_chrony_ as your NTP client.

**Solution**

First, check if _ntpd_ is installed. If it is, remove it. If you have _systemd-timesyncd_,
disable it:

```
  $ sudo systemctl disable systemd-timesyncd
  $ sudo systemctl stop systemd-timesyncd
```

Then install _chrony_ . The package name on most Linuxes is _chrony_ . After installation
use the _chronyc_ command to check its status:

```
  $ chronyc activity
  200 OK
  8 sources online
  0 sources offline
  0 sources doing burst (return to online)
  0 sources doing burst (return to offline)
  0 sources with unknown address
```

Success! It is already working, as _8 sources online_ tells you. (If it did not start, see the
Discussion.) Find your _chrony.conf_, either _/etc/chrony.conf_ (Fedora) or _/etc/chrony/_
_chrony.conf_ (Ubuntu), and take a look at the settings. There is not much you need to
change, if anything, to use it as a client. Check the NTP server list, where you will see
either _server_ options or _pool_ . The following example on an Ubuntu system includes
the default Ubuntu NTP server pools and a local LAN server:

```
  pool 0.ubuntu.pool.ntp.org iburst
  pool 1.ubuntu.pool.ntp.org iburst
  pool 1.ubuntu.pool.ntp.org iburst
  server ntp.domain.lan iburst prefer
```

You could replace some of the Ubuntu server pools with some public server pools to
improve reliability with a more diverse set of pools:

```
  pool 0.ubuntu.pool.ntp.org iburst
  pool 1.ubuntu.pool.ntp.org iburst
  pool 0.north-america.pool.ntp.org iburst
  pool 1.north-america.pool.ntp.org iburst
  server ntp.domain.lan iburst prefer
```

Restart _chronyd_ after changing the configuration file.

**17.4 Using chrony for Your NTP Client** **|** **397**

**Discussion**

_iburst_ means synchronize quickly after network interruptions, and _prefer_ means
always use this server, unless it is not available.

That really is all you need to do for a client setup. _chrony_ is a full NTP implementa‐
tion and has many options; see _man 5 chrony.conf_ for a complete description.

Manage _chronyd_ just like any other service using the following commands:

 - _systemctl status chrony_

 - _sudo systemctl stop chrony_

 - _sudo systemctl start chrony_

 - _sudo systemctl restart chrony_

Chrony has several advantages over _ntpd_ . The main advantages as a client are better
handling of interrupted network connections and faster resyncing when the connec‐
tion is restored.

**See Also**

 - [chrony](https://oreil.ly/1S41c)

 - _man 5 chrony.conf_

 - _man 1 chronyc_

**17.5 Using chrony as a LAN Time Server**

**Problem**

You want to set up _chrony_ as your LAN time server.

**Solution**

Just like in Recipe 17.4, disable _systemd-timesyncd_ and remove _ntpd_ if it is on your
system. Then install the _chrony_ package.

Find the configuration file, either _/etc/chrony.conf_ (Fedora, openSUSE) or _/etc/chrony/_
_chrony.conf_ (Ubuntu). The following example is a basic configuration:

```
  pool 0.north-america.pool.ntp.org iburst
  pool 1.north-america.pool.ntp.org iburst
  pool 2.north-america.pool.ntp.org iburst

  local stratum 10

```

**398** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

```
  allow 192.168.0.0/16
  allow 2001:db8::/56

  driftfile /var/lib/chrony/chrony.drift
  maxupdateskew 100.0
  rtcsync
  logdir /var/log/chrony
  log measurements statistics tracking
  leapsectz right/UTC
  makestep 1 3
```

Then your clients need your server’s name added to their _chrony.conf_ files:

```
  server ntp.domain.lan iburst prefer
```

The _prefer_ option means to always use this server as long as it is available. One of the
reasons to keep a local time server is to put less of a load on the public time servers.
With the _prefer_ option you can configure some public servers as backups, in case your
local server becomes unavailable, and not worry about burdening them, like this:

```
  server ntp.domain.lan iburst prefer
  pool 1.north-america.pool.ntp.org iburst
  pool 2.north-america.pool.ntp.org iburst
```

**Discussion**

_local stratum 10_ configures _chrony_ to continue acting as your local NTP server even
when your internet connection is interrupted, and _stratum 10_ puts your server safely
down the strata hierarchy, so that it is lower than any external NTP servers you are
using. Allowed values are 1–15. (Do please use a number other than 10, in case this
recipe makes _stratum 10_ wildly popular.)

The _allow_ options define the networks that are allowed to use your NTP server.

_rtcsync_ tells _chrony_ to keep your RTC synchronized with system time.

_log_ enables logging and defines the events you want logged.

You may look up the other options in _man 5 chrony.conf_, or in your default
_chrony.conf_, which is usually well commented.

**See Also**

 - [chrony](https://oreil.ly/1S41c)

 - _man 5 chrony.conf_

 - _man 1 chronyc_

**17.5 Using chrony as a LAN Time Server** **|** **399**

**17.6 Viewing chrony Statistics**

**Problem**

You want to call up some real-time _chrony_ activity and statistics, such as upstream
NTP servers, offsets, skew, which server you are currently synced with, and other
information.

**Solution**

Use the _chronyc_ command. The _tracking_ subcommand shows how much correction
has been applied, the RTC time, skew, and other information:

```
  $ chronyc tracking
  Reference ID  : A29FC87B (time.cloudflare.com)
  Stratum     : 4
  Ref time (UTC) : Tue Oct 06 02:20:23 2020
  System time   : 0.002051390 seconds fast of NTP time
  Last offset   : +0.002320110 seconds
  RMS offset   : 0.017948814 seconds
  Frequency    : 28.890 ppm fast
  Residual freq  : +0.252 ppm
  Skew      : 1.250 ppm
  Root delay   : 0.069674924 seconds
  Root dispersion : 0.003726898 seconds
  Update interval : 838.2 seconds
  Leap status   : Normal
```

List your current source servers:

```
  $ chronyc sources
  chronyc sources
  210 Number of sources = 19
  MS Name/IP address     Stratum Poll Reach LastRx Last sample
  ===============================================================================
  ^- golem.canonical.com      2  9   0  37m  +55ms[ +58ms] +/- 209ms
  ^- alphyn.canonical.com     2  9   0  34m  +23ms[ +25ms] +/- 158ms
  ^- pugot.canonical.com      2  9   0  44m  +92ms[ +80ms] +/- 229ms
  ^- chilipepper.canonical.com   2  9  11  31  +48ms[ +48ms] +/- 181ms
  [...]
```

List your current source servers, with descriptions:

```
  $ chronyc sources -v
  210 Number of sources = 19

  .-- Source mode '^' = server, '=' = peer, '#' = local clock.
  / .- Source state '*' = current synced, '+' = combined, '-' = not combined,
  | /  '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
  ||                         .- xxxx [ yyyy ] +/- zzzz
  ||   Reachability register (octal) -.      | xxxx = adjusted offset,
  ||   Log2(Polling interval) --.   |     | yyyy = measured offset,

```

**400** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

```
  ||                \   |     | zzzz = estimated error.
  ||                 |  |      \
  MS Name/IP address     Stratum Poll Reach LastRx Last sample
  ===============================================================================
  ^- golem.canonical.com      2  9   0  46m  +67ms[ +58ms] +/- 209ms
  ^- alphyn.canonical.com     2  9   0  44m  +35ms[ +25ms] +/- 158ms
  ^* pugot.canonical.com      2  9   1  54m  +104ms[ +80ms] +/- 229ms
  ^- chilipepper.canonical.com   2  9  11  587  +60ms[ +48ms] +/- 181ms
  ^- ntp.wdc1.us.leaseweb.net   2  7   4  327  +26ms[ +15ms] +/- 198ms
  ^- 216.126.233.109        2  9   1  459  +106ms[ +95ms] +/- 171ms
  ^- 157.245.170.163        3  9   1  476 +1191us[ -10ms] +/- 145ms
```

The asterisk shows which server your system is currently synchronizing with.

**Discussion**

_chrony_ adjusts for network delays and latency, intermittent connections, and sleep
and hibernate modes on client machines. The _chrony_ clock never stops, and it keeps
your network synchronized even when external name servers are unavailable.

**See Also**

 - _man 1 chronyc_

 - [chrony.tuxfamily.org](https://oreil.ly/1S41c)

**17.7 Using ntpd for Your NTP Client**

**Problem**

Yes, you know all about _chrony_ and _timesyncd_, and how good they are, but you still
want to use _ntpd_ as your NTP client.

**Solution**

No problem, because _ntpd_ is actively maintained and does the job just fine. First,
make sure that _ntpd_ is the only NTP client on your system (see Recipe 17.1). On most
Linux distributions, look for the _ntp_ package to install.

On most Linux distributions _ntpd_ comes with a useful configuration, and starts after
installation. Check with the _ps_ command:

```
  $ ps ax | grep -w ntpd
  3754 ?    Ssl  0:00 /usr/sbin/ntpd -u ntp:ntp -g
```

If it does not start automatically, start it:

```
  $ systemctl start ntpd

```

**17.7 Using ntpd for Your NTP Client** **|** **401**

While _ntpd_ is running, take a look at your configuration file, usually _/etc/ntp.conf_ . The
default configuration for your Linux distribution should work fine for you without
changes. If your network has its own LAN server, the following configuration sets the
local server as the primary and one Fedora Linux server pool as a fallback:

```
  server ntp.domain.lan iburst prefer
  pool 2.fedora.pool.ntp.org iburst
```

You may keep the default configuration, which works fine for most situations. It is
common for Linux distributions to maintain their own NTP server pools and provide
these in the default configuration. If you wish to replace these, or add some external
[public servers, see continental pools for a list of the continental NTP server pools, or](https://oreil.ly/W70Ba)
use your country pools, which you will find by clicking on the continental pool links.

When you change _/etc/ntp.conf_, restart _ntpd_ :

```
  $ systemctl restart ntpd

  $ sudo /etc/init.d/ntp restart
```

Check that it is working with _ntpq_ . The asterisk shows that the machine is syncing
with the LAN NTP server:

```
  $ ntpq -p

  remote      refid   st t when poll reach  delay  offset jitter
  ==============================================================================
  2.fedora.pool.n .POOL.     16 p  -  64  0  0.000  +0.000  0.000
  * ntp.domain.lan . 172.16.16.3   2 u  34 256 203  80.324 -49.772 54.508
  +138.68.46.177 ( 80.153.195.191  2 u  92 256 123  90.932 -15.534 39.947
  +vps6.ctyme.com 216.218.254.202 2 u 453 256  46  69.927 -29.296 84.811
  +ec2-3-217-79-24 132.163.97.6   2 u 426 256 202 165.888 -51.442 93.224
```

**Discussion**

_iburst_ tells _ntpd_ to synchronize quickly at system startup.

_prefer_ means use this server, and use the others only when it becomes unavailable.

**See Also**

 - _man 5 ntp.conf_

 - _man 8 ntpd_

 - _man 8 ntpq_

 - [NTP Documentation](https://oreil.ly/lpDgk)

**402** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

**17.8 Using ntpd for Your NTP Server**

**Problem**

You want to know how to run an _ntpd_ server for your LAN.

**Solution**

Using _ntpd_ for your LAN time server is similar to using it as an NTP client. The con‐
figuration is almost the same, with the addition of some access controls. The follow‐
ing example is a complete _/etc/ntp.conf_ configuration:

```
  driftfile /var/lib/ntp/drift

  restrict default nomodify notrap nopeer noquery
  restrict -6 default nomodify notrap nopeer noquery
  restrict 127.0.0.1
  restrict ::1

  pool 0.north-america.pool.ntp.org
  pool 1.north-america.pool.ntp.org
  pool 2.north-america.pool.ntp.org

  leapfile /usr/share/zoneinfo/leap-seconds.list

  statistics clockstats loopstats peerstats
  filegen loopstats file loopstats type day enable
  filegen peerstats file peerstats type day enable
  filegen clockstats file clockstats type day enable
  statsdir /var/log/ntpstats/
```

**Discussion**

The driftfile is where _ntpd_ tracks the time drift caused by fluctuations in the oscillat‐
ing frequency of the quartz crystal on your motherboard. You have the following
options:

 - _restrict default_ denies all, permits only what is explicitly allowed, and sets
defaults.

 - _nomodify_ does not allow other time servers to make any changes on your system.
Queries are allowed.

 - _notrap_ disables remote logging.

 - _nopeer_ does not allow peering. Peer servers synchronize with each other, so the
only servers allowed to supply time service are specified by the _server_ or _pool_
directives.

**17.8 Using ntpd for Your NTP Server** **|** **403**

 - _noquery_ disallows remote queries and remote logging.

 - _restrict 127.0.0.1_ and _restrict ::1_ mean trust localhost.

The _statistics_ section logs your selected statistics into _/var/log/ntpstats/_ . This is not
necessary, but it could be interesting for tracking which upstream NTP servers have
the best performance.

**See Also**

 - _man 5 ntp.conf_

 - _man 8 ntpd_

 - _man 8 ntpq_

 - [NTP Documentation](https://oreil.ly/lpDgk)

**17.9 Managing Time Zones with timedatectl**

**Problem**

You want to list all time zones, see your current time zone, and change time zones.

**Solution**

Use _timedatectl_ . View your current time zone:

```
  $ timedatectl | grep -i "time zone"
  Time zone: America/Los_Angeles (PDT, -0700)
```

List all time zones:

```
  $ timedatectl list-timezones
  Africa/Abidjan
  Africa/Accra
  Africa/Addis_Ababa
  Africa/Algiers
  [...]
```

The list is over 400 lines long. Use the _grep_ command when you know what you are
looking for. The list names major cities, for example, Berlin:

```
  $ timedatectl list-timezones | grep -i berlin
  Europe/Berlin
```

Set this as your time zone:

```
  $ sudo timedatectl set-timezone Europe/Berlin
```

The change takes effect immediately. Run _timedatectl_ again to verify.

**404** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

**Discussion**

When you work with people in different time zones, use UTC to coordinate meeting
[times. There are several online time zone converters, such as Time Zone Converter.](https://oreil.ly/NyLj7)

You must use the region/city form, as displayed by _timedatectl list-timezones_, to set
your time zone. This is defined by the ISO 8601 standard, which defines an unambig‐
uous standard for expressing time zones, time, and dates. The standard uses a
“descending notation,” which is the largest values to the smallest values, in sequence.
For example, for time zones the order is continent/country/city. The US habit of writ‐
ing the date as year-day-month does not conform to this standard. Year-month-day is
the standard, with a 4-digit year, YYYY-MM-DD. Time is HH:MM:SS, in the 24-hour
clock format.

The officially published ISO 8601 standard costs money, but a bit of web searching
should find the information for free.

**See Also**

 - _man 1 timedatectl_

**17.10 Managing Time Zones Without timedatectl**

**Problem**

Your Linux system does not have systemd, and you need to know what commands to
use to manage time zones.

**Solution**

Use the _date_ command to see your current time zone:

```
  $ date
  Wed Oct 7 08:32:40 PDT 2020
```

Or see what _/etc/localtime_ is linked to:

```
  $ ls -l /etc/localtime
  lrwxrwxrwx 1 root root 41 Oct 7 08:06 /etc/localtime ->
  ../usr/share/zoneinfo/America/Los_Angeles
```

The _/usr/share/zoneinfo_ directory contains all time zones:

```
  $ ls /usr/share/zoneinfo
  total 324
  drwxr-xr-x 2 root root 4096 May 21 23:02 Africa
  drwxr-xr-x 6 root root 20480 May 21 23:02 America
  drwxr-xr-x 2 root root 4096 May 21 23:02 Antarctica

```

**17.10 Managing Time Zones Without timedatectl** **|** **405**

```
  drwxr-xr-x 2 root root 4096 May 21 23:02 Arctic
  [...]
```

Look in the subdirectories to find a city close to yours, for example, Madrid:

```
  $ ls /usr/share/zoneinfo/Europe
  [...]
  -rw-r--r-- 1 root root 2637 May 7 17:01 Madrid
  -rw-r--r-- 1 root root 2629 May 7 17:01 Malta
  lrwxrwxrwx 1 root root  8 May 7 17:01 Mariehamn
  -rw-r--r-- 1 root root 1370 May 7 17:01 Minsk
  [...]
```

Change your time zone by changing the link to _/etc/localtime_ :

```
  $ sudo ln -sf /usr/share/zoneinfo/Europe/Madrid/etc/localtime
```

The change takes effect immediately.

**Discussion**

This cool command lists all time zones alphabetically:

```
  $ php -r 'print_r(timezone_identifiers_list());'
  Array
  (
  [0] => Africa/Abidjan
  [1] => Africa/Accra
  [2] => Africa/Addis_Ababa
  [3] => Africa/Algiers
  [4] => Africa/Asmara
  [...]
```

The _php_ command is in the _php-cli_ package.

Your graphical desktop should have a nice graphical utility for managing time, date,
and time zones. If a clock is displayed on your desktop, try right-clicking it to bring
up a properties or settings panel.

**See Also**

 - _man 1 date_

 - _man 1 ln_

**406** **|** **Chapter 17: Keeping Time with ntpd, chrony, and timesyncd**

**<u>CHAPTER 18</u>**
#### **Building an Internet Firewall/Router** **on Raspberry Pi**

The Raspberry Pi (RPi) makes a great internet firewall/router for small networks, and
it does not cost a lot of money. You can use any Raspberry Pi, but I recommend the
Raspberry Pi 4B because it is more powerful than the older Pis and is the first Pi with
a dedicated gigabit Ethernet port.

**Overview**

In this chapter you will learn how to install Raspberry Pi OS, connect your Pi to a
computer monitor or TV, use the Raspberry Pi OS recovery mode, run your Pi head‐
less, add a second Ethernet port, share an internet connection, and use the Pi for LAN
name services.

The examples in this chapter are all on a Raspberry Pi 4 Model B,
using the Raspberry Pi OS. Raspberry Pi OS used to be called
Raspbian. Underneath it is Debian Linux, so if you are accustomed
to Debian, Ubuntu, Mint, or any other Debian variant, it’s the same
Linux.

**Pros and Cons of a Raspberry Pi Firewall/Router**

The Raspberry Pi is a general-purpose computer, not a specialized firewall/router. It
has WiFi, Ethernet, and Bluetooth, and it runs Linux. In comparison, a common
choice for small networks is the small combination firewall/router/wireless access
point/ Ethernet switch, like the Linksys AC1900 or the TP-Link Archer AX20. These
have WiFi, gigabit Ethernet, multiple antennas, and support for “smart” services like
Alexa and smartphone administration apps.

**407**

The drawback to these devices is their inflexibility, especially limited storage and
operating system support. If you want to replace the vendor software, you must use
specialized router distributions like OpenWRT, DD-WRT, pfSense, or OPNsense,
which are all excellent, but it is not easy, and you have to find supported devices.

These are some of the advantages Raspberry Pi has over the all-in-one boxes:

 - Flexibility, just like any general-purpose Linux computer

 - More memory and storage

 - Connects to a computer monitor or TV, keyboard, and mouse

 - Runs a number of Linux distributions, so you can use your existing knowledge
and not have to learn some weird new interface or command set

 - Runs a number of *bsd operating systems, Windows 10, Android, Chromium,
and others

 - Tethers to a mobile hotspot

 - 64-bit support

You can run the Raspberry Pi with a graphical desktop, with no graphical desktop,
and headless via SSH, just like any Linux system.

Downsides of Raspberry Pi:

 - Cannot function as an Ethernet switch, like the all-in-one devices

 - WiFi is not as strong as all-in-one devices

 - Raspberry Pi models 3 and older have poor Ethernet performance because the
Ethernet port shares the USB bus; RPi 4 cures this with a dedicated gigabit Ether‐
net port

There are a number of customized Linux operating systems for Raspberry Pi. The
official operating system is Raspberry Pi OS, which is based on Debian Linux. SUSE,
Ubuntu, Fedora, Arch Linux ARM, and MX Linux have Raspberry Pi variants. There
are also specialized media server and gaming distros. In this chapter we’ll stick with
Raspberry Pi OS because it is optimized for the Pi, and you get a full graphical desk‐
top with decent performance even on the older RPi models. Raspberry Pi OS is just
like any other Linux, so anything you can do on a big Linux machine you can do on
Raspberry Pi.

**408** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

**Hardware Architecture**

The RPi is powered by a Broadcom system-on-a-chip (SoC). The CPU, GPU, and I/O
are all on a single chip. This is especially impressive on the Raspberry Pi 4 Model B,
which supports running two screens at the same time. It handles high-definition
movies without a hiccup.

The Broadcom SoC is an ARM chip, rather than the x86_64 architecture that domi‐
nates the PC market. ARM processors are less complex, using a reduced instruction
set (RISC). x86_64 processors are CISC, complex instruction set computers. x86_64
processors work a lot harder, are considerably more complex, and consume more
power.

**Rasberry Pi Banquet of Products**

Every Raspberry Pi model ever made is still available, including updated releases of
the Raspberry Pi 1, models A and B. The A models are the lower-cost versions of
every release, and the B models cost a little more for more features.

You have many other Pis to choose from, such as:

 - Raspberry Pi Zero, the smallest Pi for $5

 - Raspberry Pi Zero W includes WiFi, $10

 - Raspberry Pi 400 Personal Computer Kit, a complete system integrated into a
compact keyboard (all you need to add is a display), $100

RPi prices have been stable since the first RPi was released, though of course this
could change.

There is a giant thundering herd of accessories: cases, touchscreens, heat sinks, fans,
breakout boards, hats (expansion boards), all manner of cables and adapters, motors,
cameras, audio boards, little wireless keyboards with touchpads, gaming emulators,
RGB matrices, powered USB hubs, real-time clocks, tiny displays…it is one of the
best playgrounds ever.

**History and Purpose**

The Raspberry Pi is a real phenomenon. The original intent of its creator, Eben
Upton, was to produce a small and inexpensive computer to encourage young stu‐
dents to study computing, especially students who could not afford to buy a PC. The
first Raspberry Pi, Version 1 Model B, cost about $35. Add a keyboard and mouse,
connect to a TV or monitor, and for less than a tenth the price of a PC you had a
working Linux computer with audio, video, Ethernet, and USB. The open hardware
design, combined with open source software, encourages hacking and learning.

**Overview** **|** **409**

The Broadcom chipsets that power the Pi are not open. This has
been a point of contention since the first Pi was released. The sche‐
matics are open, available on [RaspberryPi.org, and the operating](https://raspberrypi.org)
system and BIOS are open source. In my moderately humble opin‐
ion, a completely open source platform is preferable and would be
great, and having something that works and is available now is bet‐
ter than not having something that works and is available now.

The first Raspberry Pi was an immediate success, selling over 500,000 units in the
first 6 months after its release in February 2012. Since then around 30 million Rasp‐
berry Pis have been sold. The current version, Version 4 Model B, is a significant
upgrade, the most powerful model yet, featuring:

 - 2 USB 2 ports

 - 2 USB 3 ports

 - 2 micro HDMI ports, supporting 2 4K displays

 - 1 dedicated gigabit Ethernet port

 - Supports RAM from 2 GB–8 GB

 - Broadcom BCM2711, 1.5 GHz Quad-core Cortex-A72 (ARM v8) 64-bit SoC

 - 2.4 GHz and 5.0 GHz IEEE 802.11ac WiFi

 - Bluetooth

 - 40-pin GPIO header

Compared to modern Intel and AMD CPUs, these specs are far from bragworthy, but
it’s enough horsepower to run a Linux graphical desktop, play music, movies, surf the
web, write documents…it is quite capable for its size and price.

The Raspberry Pi is developed and produced by the Raspberry Pi Foundation, a reg‐
istered nonprofit charity. The foundation supports numerous education projects for
teachers and students; visit _[https://raspberrypi.org](https://raspberrypi.org)_ for current educational materials
and information.

**18.1 Starting and Shutting Down Raspberry Pi**

**Problem**

You don’t see a power switch on your Raspberry Pi (RPi), and you want to turn it on
and off.

**410** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

**Solution**

Power it up by plugging in the power connector. Shut it down from the menu in your
operating system, then unplug it.

**Discussion**

When you shut down your RPi, you have to disconnect and then reconnect the power
to start it up again.

It wouldn’t surprise me if there is a power switch out there somewhere made for the
RPi, though I have not seen one. One alternative is to plug it into a switched power
strip.

**See Also**

 - _[https://raspberrypi.org](https://raspberrypi.org)_

**18.2 Finding Hardware and How-Tos**

**Problem**

You bought a Raspberry Pi 4 Model B, and you want to know what other hardware
devices you need in order to use it.

**Solution**

Presumably you already have a computer monitor or TV, mouse, and keyboard. You
also need:

 - Raspberry Pi power supply

 - HDMI-to-micro-HDMI cable

 - Micro SD card of at least 16 GB

 - Cooling fan, or heat sinks on the CPU, RAM module, and USB controller

 - Case

 - Micro SD card reader

Start by installing Raspberry Pi OS to your micro SD card on another computer.
While that is running, assemble your hardware. When everything is ready, connect
the power and watch your new system boot up. (See Recipes 18.4 and 18.5 to learn
how to install Raspberry Pi OS.)

**18.2 Finding Hardware and How-Tos** **|** **411**

To learn all about RPi, there are numerous sources of schematics, specifications, howtos, and clever ideas. The “See Also” section of this recipe lists a nice selection to get
you started.

**Discussion**

If your display does not have an HDMI port, see Recipe 18.6.

You may use any micro SD card at least 16 GB in size. High-speed cards make a
noticeable performance improvement. 16 GB is pretty small, and you can use as large
a card as you like.

The RPi 4B has three RAM options, 2 GB, 4 GB, and 8 GB. It is not upgradable, so
whatever you buy is what you will have. 2 GB is more than enough for an internet
gateway, and using your Pi as a lightweight Linux desktop. More memory is good for
multimedia processing, compiling code, games, and other memory-intensive tasks.

The RPi 4B is quite a bit more powerful than older Pis, and it runs hotter than older
versions. See Recipe 18.3 to learn how to keep it cool.

With 4 USB ports, the RPi 4B has a lot of flexibility. You can use standard USB key‐
boards and mice, a keyboard with a trackpad, and USB-to-PS/2 adapters for older
keyboards and mice. You can attach a USB hard drive for more storage or backups,
and any other USB devices just like on a big computer. The 40-pin GPIO header sup‐
ports attaching nearly any expansion board.

There are many nice kits that bundle everything you need to get started. My favorite
[store is Adafruit.com, and you can find many more listed on](https://adafruit.com) _[https://raspberrypi.org](https://raspberrypi.org)_ .

**See Also**

These sites publish excellent Raspberry Pi tutorials:

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

 - [Adafruit](https://oreil.ly/5qwn5)

 - [MagPi](https://oreil.ly/EuMY7)

 - [Hackspace](https://oreil.ly/5KY5B)

 - [Maker Pro](https://oreil.ly/NQcB0)

 - [Makezine](https://oreil.ly/foZqS)

**412** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

**18.3 Cooling the Raspberry Pi**

**Problem**

Your Raspberry Pi feels hot to the touch, and you want to install some kind of cooling
for it.

**Solution**

Install a cooling fan in the case, or heat sinks on the CPU, RAM module, and USB
controller. Install a fan and heat sinks on the Raspberry Pi 4, which runs hotter than
older Pis.

Use the built-in _vcgencmd_ command to measure CPU temperatures before and after
installing cooling devices, and before and after running computationally intensive
tasks such as compiling code or playing videos. The following example is a fanless
board at idle with the case lid removed, and then after five minutes of playing a movie
at 1080p:

```
  $ vcgencmd measure_temp
  temp=48.3'C

  $ vcgencmd measure_temp
  temp=61.9'C
```

This example shows the effect of a cooling fan when playing the same movie:

```
  $ vcgencmd measure_temp
  temp=52.1'C
```

The temperature should not go over 70°C. 40°C to 60°C is a good operating range.

**See Also**

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

 - [Adafruit](https://oreil.ly/5qwn5)

 - [MagPi](https://oreil.ly/EuMY7)

**18.4 Installing Raspberry Pi OS with Imager and dd**

**Problem**

You have your hardware, and you want to install the operating system.

**18.3 Cooling the Raspberry Pi** **|** **413**

**Solution**

You will create a bootable micro SD card on another computer, then load the SD card
into your Raspberry Pi and start it up.

There are four ways to get a bootable SD card:

 - Use the Raspberry Pi Imager (currently only for _.deb_ systems such as Debian,
Ubuntu, or Mint)

 - Use the NOOBS installer (Recipe 18.5)

 - Copy your installation image to your micro SD card with the _dd_ command

 - Buy a micro SD card with the installer already loaded

I favor NOOBs because it works on all Linuxes, and it creates a rescue boot mode.

To install the Raspberry Pi Imager from the _.deb_ package, download it from _[https://](https://raspberrypi.org)_
_[raspberrypi.org](https://raspberrypi.org)_ . Then install the package:

```
  $ sudo dpkg -i imager_1.5_amd64.deb
```

Alternatively, Ubuntu users can install the Raspberry Pi Imager with _apt_ :

```
  $ sudo apt install rpi-imager
```

Plug your SD card into your computer. Locate it with _lsblk -p_ (see Recipe 10.9).

Start the Raspberry Pi Imager from your system menu, and enjoy its cheery raspberry
logo. Click Operating System to select the operating system you want to install, and
the Imager will download it and copy it to your SD card. If you have already down‐
loaded an image, scroll down the selection menu to Use Custom to select your down‐
loaded image. You will see a screen like Figure 18-1.

_Figure 18-1. Creating a bootable micro SD card with Raspberry Pi Imager_

**414** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

Click SD Card to select the device, and then click Write to install the operating
system.

If you don’t have an Ubuntu system, download your chosen operating system image
from _[https://raspberrypi.org](https://raspberrypi.org)_ and use the _dd_ command to copy it to your SD card.
The following example unzips and copies _2021-03-24-raspios-buster-armhf.zip_ to the
SD card:

```
  $ sudo unzip -p 2021-03-24-raspios-buster-armhf.zip | \
  sudo dd of=/dev/ foo bs=4M conv=fsync status=progress
```

When the SD card is ready, insert it in your Raspberry Pi and power it on. When it
boots up, you will complete a short setup, and then it is ready to use.

The default user is _pi_ . Look in _/home/pi/Bookshelf_ for a PDF copy of _The Official Rasp‐_
_berry Pi Beginner’s Guide_ by Gareth Halfacree (Raspberry Pi Press).

**Discussion**

You do not have to format your SD card before copying with _dd_ .

The imager creates two partitions: a 256 MB FAT32 _/boot_ partition, and an Ext4 _rootfs_
partition just big enough to hold the filesystem. On my test system that is 3.4 GB, and
the rest of the card is unallocated space.

When you boot up your new system for the first time, the root filesystem is expanded
to fill all the unallocated space. You may shrink the root filesystem and create more
partitions with GParted (Chapter 9) or _parted_ (Chapter 8).

**See Also**

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

**18.5 Installing Raspberry Pi with NOOBS**

**Problem**

You want to use NOOBS to install Raspberry Pi.

**Solution**

NOOBS (New Out Of the Box Software) is an older installer. It works on all Linux
distributions and creates a recovery boot mode, which Raspberry Pi Imager does
not do.

**18.5 Installing Raspberry Pi with NOOBS** **|** **415**

Download NOOBS on another computer, unzip the download archive, copy all of its
files to a micro SD card, then load the SD card into your Raspberry Pi and start it up.

Download NOOBS from _[https://raspberrypi.org](https://raspberrypi.org)_ . There are two versions: NOOBS and
NOOBS Lite. NOOBS includes Raspberry Pi OS, and a network installer for other
operating systems. NOOBS Lite includes only the network installer.

Unpack NOOBS after downloading:

```
  $ unzip NOOBS_lite_v3_5.zip
```

Plug your SD card into your computer. Locate it with _lsblk -p_ (see Recipe 10.9).

Format your micro SD card as a single FAT32 partition.

Copy all the NOOBS files to your SD card, then use it to boot your Raspberry Pi.
First you will see a cool rainbow colored screen, then NOOBS boots to the installa‐
tion menu (Figure 18-2). Set up networking to use the network installer or to get
updates after installation. Select your operating system, then go find something to do
until it is finished.

_Figure 18-2. NOOBS installation screen_

**416** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

After installation is complete, you will go through a brief setup process, and then
your Raspberry Pi is ready to use.

The default user is _pi_ . Look in _/home/pi/Bookshelf_ for a PDF copy of _The Official Rasp‐_
_berry Pi Beginner’s Guide_ by Gareth Halfacree (Raspberry Pi Press).

**Discussion**

NOOBS is a simple unzip and copy, so it works on any computer.

Copying the NOOBS files to your SD card can take a long time. Usually it is faster to
copy the ZIP file to the SD card, then unzip it on the card. You can delete the ZIP file
after installation.

**See Also**

 - Chapter 9

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

**18.6 Connecting to a Video Display Without HDMI**

**Problem**

You have a TV or computer monitor that does not have HDMI ports, and you want
to connect your Raspberry Pi to it.

**Solution**

There are four ways to connect a screen to the RPi 4B. You can use:

 - Small screens made for the Raspberry Pi

 - DVI-to-HDMI adapter

 - VGA-to-HDMI adapter

 - RCA composite video (use cables made for Raspberry Pi)

There is quite a variety of screens made for the RPi: touchscreens, LED, LCD, OLED,
eInk—you name it, there is probably an RPi version. Follow the installation instruc‐
tions that come with the screen.

The DVI-to-HDMI and VGA-to-HDMI adapters connect to your screen, and then
your HDMI-to-micro-HDMI cable connects to the adapter. When you connect to a
single HDMI display on the RPi 4B, plug into the HDMI 0 port, which is the one
closest to the power port.

**18.6 Connecting to a Video Display Without HDMI** **|** **417**

Composite video requires some extra steps on the RPi 4B because it is disabled by
default. The easy way is to find an HDMI screen to use when you boot your Pi for the
first time and complete your installation. After your installation is complete, open the
configuration tool to enable composite video:

```
  $ sudo raspi-config
```

Arrow-key down to 6 Advanced Options, then select A8 HDMI/Composite. Select V2
Enable Composite. Exit _raspi-config_, shut down your Pi, connect your Pi to your
composite video screen, then start it up again. It should default to your composite
video screen.

**Discussion**

Older flat-panel screens usually have VGA and composite video connectors, so you
could use either composite video or a VGA-to-HDMI adapter. Technically, HDMI
delivers a higher-quality image than composite video, but most people cannot tell the
difference.

Figure 18-3 shows a Rocketfish DVI-to-HDMI adapter, a composite cable bundle, a
Rasberry Pi 4B in a CanaKit case with the top removed, and a micro SD card.

_Figure 18-3. Raspberry Pi 4B with accessories_

**418** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

The RCA composite audio/video cable set, the one with the yellow, red, and white
connectors, plugs into the nifty little 3.5 mm TRRS port on the RPi. You need one
made for the RPi because there is no standard for how the TRRS plug is ordered. You
might find some that don’t work as they are supposed to, which is yellow for video,
and red and white for audio. Avoid composite cables made for camcorders and MP3
players, which have their own weird ordering that puts the ground ring in the wrong
place. The TRRS (tip-ring-ring-sleeve) plug should be configured like this:

```
  Tip     Ring 1    Ring 2  Sleeve
  Left audio  Right audio  Ground  Video
```

There are several options for tweaking your composite video settings in _/boot/_
_config.txt_ . If you plan to use composite video, use the NOOBS installer. Then if you
need to correct its settings, you can boot to recovery mode (Recipe 18.7) and have
access to _/boot/config.txt_ .

_sdtv_mode=_ sets the TV standard. _sdtv_mode=0_ is the default for North America.
Most of the world uses PAL; see Table 18-1 for the settings.

_Table 18-1. sdtv_mode settings_

**<mark>value</mark>** **<mark>mode</mark>**
0 Normal NTSC (default)

1 Japanese version of NTSC

2 Normal PAL

3 Brazilian version of PAL

16 Progressive scan NTSC

18 Progressive scan PAL

_sdtv_aspect=_ command defines the aspect ratio (Table 18-2).

_Table 18-2. sdtv_aspect screen ratio settings_

**<mark>value</mark>** **<mark>ratio</mark>**
1 4:3 (default)

2 14:9

3 16:9

**See Also**

 - [Video options in config.txt](https://oreil.ly/yp7Mu)

**18.6 Connecting to a Video Display Without HDMI** **|** **419**

**18.7 Booting into Recovery Mode**

**Problem**

You want to know how to boot into recovery mode in case you ever have problems.

**Solution**

You must have installed your operating system with NOOBS because that is the only
installer that sets up a recovery mode. Power on your Pi and watch your startup
screen. A screen with the Raspberry Pi logo and a “For recovery mode, hold Shift”
message appears briefly. Press and hold the shift key until the recovery screen appears
(Figure 18-2; the recovery screen is the same as the NOOBS installation screen).

The recovery screen is a nice graphical utility for performing some basic operations.
You can connect to the internet, browse the online help, edit the _/boot/cinfig.txt_, or
blow away your installation and install something else.

**Discussion**

The recovery screen is the same as the NOOBS installation screen. You have this
recovery option only when you install Raspberry Pi with NOOBS, though by the time
you read this it could be different.

**See Also**

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

**18.8 Adding a Second Ethernet Interface**

**Problem**

You want to use your Raspberry Pi as an internet firewall/router, but it has only one
Ethernet port, and you really want two Ethernet ports.

**Solution**

There are two ways to get a second Ethernet port: with a USB-to-Ethernet adapter or
by installing an Ethernet port that connects to the GPIO pins.

USB-to-Ethernet is easy; just plug it in.

**420** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

A wired Ethernet port is a little more work. You need an Ethernet adapter powered by
an ENC28J60 Ethernet controller module (Figure 18-4).

_Figure 18-4. ENC28J60 Ethernet adapter_

The HanRun HR911105A adapter in the photo needs seven female-to-female jumper
wires to connect to the GPIO pins. You can buy multicolor bundles that supply an
assortment of wires for cheap.

Before connecting the wires, generate your own handy pinout diagram by running
the _pinout_ command on your Raspberry Pi (Figure 18-5).

Figure 18-6 shows the diagram from RaspberryPi.org numbers and labels the GPIO
pinouts.

**18.8 Adding a Second Ethernet Interface** **|** **421**

_Figure 18-5. Pinout diagram generated by pinout command_

**422** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

_Figure 18-6. Pinout diagram from RaspberryPi.org_

Edit _/boot/config.txt_ to enable the new Ethernet port and load the drivers:

```
  dtparam=spi=on
  dtoverlay=enc28j60
```

Keep a copy of the pinout diagram available and power off your Raspberry Pi. Con‐
nect the jumper wires in the following locations on your RPi and ENC28J60 module:

```
  RPi      ENC28J60
  ---------------------------  +3V3     VCC
  GPIO10    SI
  GPIO9     SO
  GPIO11    SCK
  GND      GND

  GPIO25    INT
  CE0#/GPIO8  CS
```

Note the orientation of the GPIO pins: pin #1 is on the same end of the RPi board as
the SD card slot. Start with 3V3 pin 17, then all of your wires are in the same area,
and the other 3V3 pin is free for a case fan.

When all of the wires are in place, power up your RPi. Run _ifconfig_ to see your new
Ethernet interface. It should be _eth1_ :

```
  $ ip link show dev eth1
  2: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel
  state DOWN mode DEFAULT group default qlen 1000
  link/ether d0:50:99:82:e7:2b brd ff:ff:ff:ff:ff:ff

```

**18.8 Adding a Second Ethernet Interface** **|** **423**

There it is, all ready to be configured.

**Discussion**

The ENC28J60 Ethernet controller supports only 10 MBps. If your internet speeds
are no better 10 MBps, then this is fine. On the Raspberry Pi 4 you will get as much as
900 MBps with a USB 3.0 Ethernet adapter.

Older Raspberry Pis have slower Ethernet because it runs over the USB 2.0 bus. The
RPi 4B is the first Pi to have a dedicated Ethernet bus.

Keep an eye on new product releases for dual gigabit Ethernet options, as there are
likely to be some soon.

The _pinout_ command is provided by the _python3-gpiozero_ package. This is installed
by default in the Raspberry Pi OS desktop image, but not on Raspberry Pi OS Lite.
Install it with _apt install python3-gpiozero_ .

**See Also**

 - [GPIO diagram](https://oreil.ly/0pgXZ)

 - [Technical information and datasheet for ENC28J60 controller](https://oreil.ly/HjlAM)

**18.9 Setting Up an Internet Connection Sharing Firewall**
**with firewalld**

**Problem**

You want to configure a simple firewall on your Raspberry Pi that shares your inter‐
net connection and keeps the bad bits out.

**Solution**

We will use _firewalld_ to filter incoming packets, allowing only responses to traffic that
originated from inside the LAN and disallowing external connection requests.

Your internet gateway setup looks something like Figure 18-7.

_Figure 18-7. Raspberry Pi firewall/router_

**424** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

The big bad internet comes in through whatever device connects you to your ISP,
which connects to your Raspberry Pi, which filters and routes traffic to your LAN
through an Ethernet switch.

You need two network interfaces on your RPi, one that connects from your internet
box to the RPi, and a second interface to connect your RPi to your LAN. In this
recipe we will use two Ethernet interfaces.

Install _firewalld_, and optionally _firewall-config_ and _firewall-applet_ . _firewall-config_ pro‐
vides a graphical configuration tool, and _firewall-applet_ sits in the panel and provides
quick access to some commands, such as the panic button and lockdown:

```
  $ sudo apt install firewalld firewall-config firewall-applet
```

Find your default router/gateway:

```
  $ ip r show
  default via 192.168.1.1 dev eth0 proto dhcp src 192.168.1.43 metric 303 mtu 1500
  192.168.1.0/24 dev eth0 proto dhcp scope link src 192.168.1.43 metric 303 mtu
  1500cat
```

_default via 192.168.1.1_ is your default gateway.

Make _eth1_ the external interface by connecting it to your internet box. _eth0_ is your
internal interface, connected to your LAN switch. The two interfaces should be on
different subnets. _eth1_ should be on the same subnet as your internet box. Suppose
the LAN interface of your internet box is 192.168.1.1, then _eth1_ could be 192.168.1.2.

_eth0_ is on your LAN subnet, for example, 192.168.2.1.

Configure the two interfaces in _/etc/dhcpcd.conf_ :

```
  # external interface
  interface eth1
  static ip_address=192.168.1.2/24
  static routers=192.168.1.1

  # internal interface
  interface eth0
  static ip_address=192.168.2.1/24
  static routers=192.168.1.1
```

Reboot to apply the changes.

The next step is to set up _firewalld_ . The two interfaces must be in two different fire‐
wall zones. _eth1_ goes in the _external_ zone, and _eth0_ goes in the _internal_ zone, then
verify your changes:

```
  $ sudo firewall-cmd --zone=external --change-interface=eth1
  success
  pi@raspberrypi:~ $ sudo firewall-cmd --zone=internal --change-interface=eth0
  success
  pi@raspberrypi:~ $ sudo firewall-cmd --get-active-zones

```

**18.9 Setting Up an Internet Connection Sharing Firewall with firewalld** **|** **425**

```
  external
  interfaces: eth1
  internal
  interfaces: eth0
```

List the configuration for each zone:

```
  $ sudo firewall-cmd --zone=external --list-all
  external (active)
  target: default
  icmp-block-inversion: no
  interfaces: eth1
  sources:
  services: ssh
  ports:
  protocols:
  masquerade: yes
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:

  $ sudo firewall-cmd --zone=internal --list-all
  internal (active)
  target: default
  icmp-block-inversion: no
  interfaces: eth0 wlan0
  sources:
  services: dhcpv6-client mdns samba-client ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
```

Note that _ssh_ access is the default for the external zone. You may add or remove any
services that you wish. You must leave _masquerade_ enabled because this is what ena‐
bles internet access.

Make your changes permanent:

```
  $ sudo firewall-cmd --runtime-to-permanent
  success
```

IPv4 forwarding is also enabled by default in the _external_ zone, which you can verify
by reading _/proc_ . IPv4 forwarding enables routing; otherwise, all the packets entering
your RPi would not be routed to other hosts on your network.

```
  $ cat /proc/sys/net/ipv4/ip_forward
  1
```

1 means it is enabled, 0 is not enabled.

**426** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

**Discussion**

IPv4 masquerading is network address translation, or NAT. NAT was created to
extend the limited pool of IPv4 addresses (which is officially exhausted). NAT allows
us to freely use the private IPv4 address spaces on our internal networks without hav‐
ing to purchase public IPv4 addresses. Your internet provider gives you at least one
public IPv4 address. Your private addresses are translated to appear as your one pub‐
lic IPv4 address; otherwise, your internal hosts would have no internet access.

You can add and remove services from your zones; see Chapter 14.

**See Also**

 - Chapter 14

 - [Debian Bug report logs - #914694](https://oreil.ly/SuHLL)

**18.10 Running Your Raspberry Pi Headless**

**Problem**

You are using your Raspberry Pi as an internet firewall/router, LAN router, or some
kind of lightweight LAN server, and you want to reduce the load by running it
without a graphical desktop.

**Solution**

Follow these steps:

1. Set up SSH access on your RPi (Chapter 12).

2. Run _raspi-config_ to disable the graphical desktop.

3. Reboot.

4. Launch _sudo raspi-config_, then navigate to 1 System Options → S5 Boot / Auto
Login (see Figure 18-8).

5. Set the next boot to console, not GUI, then reboot.

As long as you can open an SSH session to your RPi, you will be able to access it
without a screen.

You can launch your graphical environment from the text console by typing the
**`startx`** command.

**18.10 Running Your Raspberry Pi Headless** **|** **427**

_Figure 18-8. Set the next boot to console, not GUI_

**Discussion**

_rpi-config_ uses the _ncurses_ interface. _ncurses_ is a console interface that looks like a
simple GUI.

When you run the Raspberry Pi headless, it needs only power and network connec‐
tions, because you control it over an SSH session from another computer.

**See Also**

 - Chapter 12

 - [The Raspberry Pi Foundation](https://oreil.ly/Ji4j2)

**18.11 Building a DNS/DHCP Server with Raspberry Pi**

**Problem**

Your internet box does not offer much in the way of administration features, and you
want control of your local name services, DNS and DHCP.

**Solution**

Disable the name services on your internet box, and set up a second Raspberry Pi to
provide your LAN name services with Dnsmasq (Chapter 16). Use DHCP to supply

**428** **|** **Chapter 18: Building an Internet Firewall/Router on Raspberry Pi**

all services and addresses to your LAN hosts, including static addresses, except for
your internet gateway, which should be independent of any internal services.

**Discussion**

You could install your name server on your internet firewall/gateway, but it is not a
good security practice to put internal services on a host that is directly connected to
the internet. Your Raspberry Pi DNS/DHCP server needs only a single network inter‐
face, like any other LAN server.

**See Also**

 - Chapter 16

**18.11 Building a DNS/DHCP Server with Raspberry Pi** **|** **429**

**<u>CHAPTER 19</u>**
#### **System Rescue and Recovery** **with SystemRescue**

A SystemRescue DVD or USB drive is an essential tool, and you may use it to rescue
nonbooting Linux and Windows systems. In this chapter you will learn how to create
SystemRescue boot media, how to find your way around SystemRescue, customize
boot options, repair GRUB, retrieve files from a failing disk, reset Linux and Win‐
dows passwords, and convert SystemRescue from a read-only filesystem to a readwrite filesystem with a data partition.

Any live Linux can serve as a rescue Linux. The advantage of SystemRescue is its
small size, and it is tailored for rescue operations.

The root SystemRescue filesystem is read-only, so any changes you make are lost
when you shut it down. You will learn how to set it up to preserve your changes, such
as configurations, appearance, and adding software.

SystemRescue was originally based on Gentoo Linux, and since version 6.0 it is built
from Arch Linux. Arch Linux is known for being a reliable and efficient Linux distri‐
bution, and has first-rate documentation. Visit _[https://archlinux.org](https://archlinux.org)_ for documenta‐
tion and forums.

I prefer USB devices for SystemRescue, both thumb drives and USB hard disks.
They’re fast and have as much capacity as you need for copying files.

**431**

**19.1 Creating Your SystemRescue Bootable Device**

**Problem**

You want to make a SystemRescue DVD or USB drive.

**Solution**

Download the latest SystemRescue _.iso_ from _[https://system-rescue.org](https://system-rescue.org)_ .

The most reliable way to create a bootable SystemRescue USB stick is with the _dd_
command (see Recipe 1.6). See Recipes 1.4 and 1.5 for instructions on creating a
bootable DVD. Chapter 1 also describes how to boot to your new medium and how
to disable Secure Boot. SystemRescue does not include signing keys, so you must dis‐
able Secure Boot.

When you boot from a USB stick, plug it in to a USB port on your computer, not a
USB hub, because it will not be recognized on a hub.

**Discussion**

Remember to reenable Secure Boot when you are finished using SystemRescue.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - Chapter 1

**19.2 Getting Started with SystemRescue**

**Problem**

You have booted up SystemRescue, and it stops at a plain console prompt, and you
need to know what to do.

**Solution**

SystemRescue gives you instructions on the initial login screen (Figure 19-1). You are
automatically logged in as root, and there is no root password.

You can either work from the console or type **`startx`** to launch the Xfce4 desktop
environment (Figure 19-2).

**432** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

_Figure 19-1. The SystemRescue login screen_

_Figure 19-2. The SystemRescue Xfce4 desktop environment_

Explore the applications menu, adjust the appearance of Xfce, connect to networks
with NetworkManager, and shut it down or reboot just like any Linux system.

**19.2 Getting Started with SystemRescue** **|** **433**

**Discussion**

The one thing you cannot do with the stock SystemRescue image is make persistent
changes in its own configuration. Any changes you make will not survive a restart
because SystemRescue runs from a compressed read-only SquashFS filesystem. How‐
ever, you can set it up to preserve your changes; see Recipe 19.14.

SquashFS is the basis of many live Linux distributions, such as Ubuntu, Debian, Mint,
Fedora, and Arch. It is also used by the open source router firmware projects DDWRT and OpenWRT. SquashFS is lightweight and fast.

I like working from Xfce4 because it provides a lightweight graphical environment
and applications, and an X terminal for command-line operations.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - _[https://xfce.org](https://xfce.org)_

**19.3 Understanding SystemRescue’s Two Boot Screens**

**Problem**

While testing SystemRescue, you noticed there are two different boot screens, and
you want to know what they are for.

**Solution**

There are two different boot screens according to how you boot SystemRescue. You’ll
see one boot screen with legacy BIOS boot (Figure 19-3) and a different screen with
UEFI boot (Figure 19-4).

When the UEFI setup on my Dell system is configured to allow booting legacy devi‐
ces, the one-time boot menu (press F12 at startup) shows all possible boot options
(Figure 19-5). SystemRescue supports UEFI, so it is not necessary to enable legacy
boot. (Remember that Secure Boot must be disabled for SystemRescue to boot.)

Your system’s BIOS/UEFI may not look like mine, as they all vary.

**434** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

_Figure 19-3. The SystemRescue legacy BIOS boot screen_

_Figure 19-4. The SystemRescue UEFI boot screen_

**19.3 Understanding SystemRescue’s Two Boot Screens** **|** **435**

_Figure 19-5. Dell one-time boot menu shows all possible boot options_

The main difference between the two boot screens is the SystemRescue UEFI boot
screen has the “Start EFI Shell” and “EFI Firmware Setup” options, which are not
applicable to a legacy BIOS boot.

The legacy BIOS boot screen does not have the two EFI options, but it includes
Memtest86+ for testing system memory.

See Recipe 19.4 to learn what the different SystemRescue boot options are for.

**Discussion**

You can configure removable media as the default boot device. Then you don’t have
to hassle with entering your BIOS/UEFI to enable a different boot device or waiting
for the right moment to call up your one-time boot menu; just insert your removable
boot media when you need it.

If you are running an older system with no UEFI, you won’t have to choose or hassle
with Secure Boot.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - Chapter 1

 - Recipe 19.4

**436** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

**19.4 Understanding SystemRescue’s Boot Options**

**Problem**

You want to know what all those SystemRescue boot options are for (Recipe 19.3).

**Solution**

The boot menu options are shortcuts for the most commonly used boot options, sav‐
ing you the trouble of opening the editing form and typing them. In most cases you
will use the first boot option, “Boot SystemRescue Using Default Options.”

The second option, “Boot SystemRescue and copy to RAM (copytoram),” speeds up
performance by loading SystemRescue completely into memory. This is especially
useful when you run SystemRescue from a DVD. It uses about 2 GB of RAM.

The third option, “Boot SystemRescue and verify integrity of the medium (check‐
sum),” tests itself for corruption. Use this to verify that your SystemRescue is healthy.

The fourth option, “Boot SystemRescue using basic display drivers (nomodeset),”
uses lower-resolution basic video drivers. Use this if your video does not look right
because SystemRescue does not have the right graphics drivers.

The fifth option, “Boot a Linux operating system installed on the disk (findroot),” is a
good way to test if the bootloader is the problem on a nonbooting Linux installation.
It will find a bootable partition, and if there is more than one it lists all of them, and
you select which one you want to use.

The sixth option, “Stop during the root process before mounting the root filesystem,”
is a repair mode in case SystemRescue will not boot. I think it’s easier to keep some
extra SystemRescue drives on hand than to try to repair a broken SystemRescue.

The UEFI boot screen has two additional options: “Start EFI Shell,” and “EFI Firm‐
ware Setup.” “Start EFI Shell” gives you access to the numerous EFI utilities, and “EFI
Firmware Setup” takes you to your system’s UEFI setup.

Then Reboot and Power off.

The BIOS boot screen has two additional options: “Boot existing OS” and “Run
Memtest86+.” “Boot existing OS” helps diagnose bootloader problems by bypassing
the system’s bootloader, and “Memtest86+” tests system memory.

Both screens include “Reboot” and “Power off,” for rebooting or shutting down Sys‐
temRescue instead of starting it up.

**19.4 Understanding SystemRescue’s Boot Options** **|** **437**

**Discussion**

I don’t see much value in using the EFI shell because it supports advanced operations
[far beyond what you need for rescuing a nonbooting system. See Intel’s Basic Instruc‐](https://oreil.ly/dktzy)
[tions for Using the Extensible Firmware Interface to learn all about it.](https://oreil.ly/dktzy)

All of these menu options are shortcuts for some of SystemRescue’s boot options,
which are documented on _[https://system-rescue.org](https://system-rescue.org)_ . You may append boot options to
any of the SystemRescue boot menu items, which you will see in several of the recipes
in this chapter.

You can do these tasks after you start SystemRescue, or pass in boot options. In the
legacy BIOS screen, select your boot entry, then press the Tab key, which opens an
edit field. Enter **`rootpass=`** **_`yourpassword`_** **`nofirewall`**, then press Enter to resume
startup.

In the UEFI boot screen, press the E key to pass in your own boot options.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

**19.5 Identifying Filesystems**

**Problem**

You need to know how to identify the filesystems on your hard disks, so you are cer‐
tain which ones to use in your rescue operations.

**Solution**

Use the good old _lsblk_ command:

```
  # lsblk -f
  NAME  FSTYPE  FSVER LABEL   UUID        SAVAIL FSUSE% MOUNTPOINT
  loop0 squashfs 4.0                   0  100% /run/archiso/sf
  s/airootfs
  sda
  ├─sda1
  └─sda2 ntfs           5E363
  sdb
  ├─sdb1 vfat   FAT16 BOOT   5E2F-1E75
  ├─sdb2 btrfs     root   02bfdc9a-b8bb-45ac-95a8
  ├─sdb3 xfs      home   cc8acf0b-529e-473c-b484
  └─sdb4 swap   1        7a5519ae-efe6-45e6-b147
  sdc  iso9660    RESCUE800 2021-03-06-08-53-50-00

```

**438** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

```
  └─sdc1 iso9660    RESCUE800 2021-03-06-08-53-50-00  0  100% /run/archiso/
  bootmnt
```

**Discussion**

Using filesystem labels makes finding the correct filesystems a lot easier. You may also
use labels in place of UUIDs, for example, in _/etc/fstab_ . See Recipe 9.4 and Chapter 11
for information on managing filesystem labels.

_lsblk_ does not need root privileges and displays information about your block devices
in almost any way you want to see it.

**See Also**

 - Recipe 9.4

 - Recipe 11.2

 - Chapter 11

**19.6 Resetting a Linux Root Password**

**Problem**

You forgot your Linux root password and need to reset it.

**Solution**

Boot SystemRescue, then mount the correct root filesystem. In the following exam‐
ples, the root filesystem is on _/dev/sdb2_ . Create a mountpoint in _/mnt_, then mount
your filesystem:

```
  # mkdir /mnt/ sdb2
  # mount /dev/ sdb2 /mnt/ sdb2
```

Change from the SystemRescue root filesystem to your mounted filesystem:

```
  # chroot /mnt/sdb2/ /bin/bash
  :/ #
```

Reset the root password:

```
  :/ # passwd root
  New password:
  Retype new password:
  passwd: password updated successfully
  :/ #

```

**19.6 Resetting a Linux Root Password** **|** **439**

Type **`exit`** to return to the SystemRescue root filesystem.

Reboot, log in, and try your new password.

**Discussion**

You cannot recover a forgotten password, but only create a new one.

This works for any user’s password.

By changing to the host system’s root filesystem you can run some commands, but
not all of them because it is not a complete filesystem. It is missing all the pseudofilesystems that exist only in memory, such as _sysfs_ and _proc_ . See Recipe 19.9 to learn
how to set up a more complete _chroot_ environment.

Once upon a time you could reset a root password by deleting the password hash
in _/etc/shadow_ . That was then, and now the _pam_ subsystem is more complex and con‐
trols authorization. If you’re curious, study the SystemRescue _pam_ configuration to
see how it is set up to allow an empty root password.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - Chapter 5

 - _man 7 pam_

**19.7 Enabling SSH in SystemRescue**

**Problem**

You want SSH access to SystemRescue.

**Solution**

SSH is enabled by default, and so is the firewall. Disable the firewall to allow incom‐
ing SSH sessions.

After launching SystemRescue, disable the firewall with _systemctl_ :

```
  [root@systemrescue ~]# systemctl stop iptables.service

```

**440** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

By default, root has no password on SystemRescue. You must create one to enable an
SSH session:

```
  [root@systemrescue ~]# passwd root
  New password:
  Retype new password:
  passwd: password updated successfully
```

Now you can log in to SystemRescue from another computer:

```
  $ ssh root@ 192.168.10.101
  ssh root@192.168.1.91
  The authenticity of host '192.168.1.91 (192.168.1.91)' can't be established.
  ECDSA key fingerprint is SHA256:LlUCEngz5NHg98xv.
  Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
  Warning: Permanently added '192.168.1.91' (ECDSA) to the list of known hosts.
  root@192.168.1.91's password:
  [root@sysrescue ~]#
```

**Discussion**

Every time you boot SystemRescue, it is like a brand-new system with a different SSH
host key. If you reboot SystemRescue, then open a second SSH system from the same
computer to SystemRescue, you will see this warning:

```
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @  WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!   @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
```

This goes on for a few more lines, and it tells you the remedy:

```
  Offending ECDSA key in /home/duchess/.ssh/known_hosts:12
  remove with:
  ssh-keygen -f "/home/duchess/.ssh/known_hosts" -R "192.168.10.101"
```

Do what is says, then you can SSH in to SystemRescue.

You may disable the firewall from the boot menu. Press the Tab key (legacy boot) or
the E key (UEFI boot) to add the _nofirewall_ boot option (see the boot parameters line
at the bottom of the screen, Figure 19-6).

**19.7 Enabling SSH in SystemRescue** **|** **441**

_Figure 19-6. Disabling the firewall at boot_

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - Recipe 19.4

 - Chapter 12

**19.8 Copying Files over the Network with scp and sshfs**

**Problem**

You have SystemRescue up and running on the system you are rescuing and want to
rescue files by copying them over the network.

**Solution**

No problem, do this just like on any Linux. First, enable SSH (Recipe 19.7). Then use
_scp_ or _sshfs_ to move the files you want to save. All of the commands in this recipe are
run from SystemRescue.

Find the filesystem you want to copy files from with _lsblk_ . If you don’t remember
which partition you want, mount each one to see the files until you find the right one:

**442** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

```
  # lsblk -f
  NAME  FSTYPE  FSVER LABEL   UUID        SAVAIL FSUSE% MOUNTPOINT
  loop0 squashfs 4.0                   0  100% /run/archiso/sf
  s/airootfs
  sda
  ├─sda1
  └─sda2 ntfs           5E363E30363E0993
  sdb
  ├─sdb1 vfat   FAT16 BOOT   5E2F-1E75
  ├─sdb2 btrfs     root   02bfdc9a-b8bb-45ac-95a8
  ├─sdb3 xfs      home   cc8acf0b-529e-473c-b484
  └─sdb4 swap   1        7a5519ae-efe6-45e6-b147
  sdc  iso9660    RESCUE800 2021-03-06-08-53-50-00
  └─sdc1 iso9660    RESCUE800 2021-03-06-08-53-50-00  0  100% /run/archiso/b
  ootmnt
  sr0
```

The following example mounts the partition containing _/home_ on the system being
rescued in _/mnt_ on SystemRescue, lists the files in the mountpoint, then copies the
whole _/home_ directory to Duchess’s PC with _scp_ :

```
  # mkdir /mnt/ sdb3
  # mount /dev/ sdb3 /mnt/ sda3
  # ls /mnt/ sdb3
  bin  dev home lib64    media opt  root sbin sys usr
  boot etc lib  lost+found mnt  proc run  srv  tmp var
  # scp -r /mnt/sdb3/home/ duchess@pc:
```

The result is _/home/duchess/home_ .

**Always Create a Subdirectory in /mnt**

Never mount any filesystems in _/mnt_ ; it will freeze SystemRescue.
Always create subdirectories for your mountpoints.

You may copy a space-delimited list of files and mix files and directories. This exam‐
ple copies them to the _rescue_ directory on _duchess@pc_ . The remote directory must
already exist:

```
  # cd /mnt/sdb3/home/
  # scp -r file1.txt directory1 file2.txt duchess@pc:rescue/
```

_sshfs_ is convenient because it mounts a remote filesystem so that it appears as a local
filesystem, and you can copy files just as though they were local. Create a mountpoint
on SystemRescue, then mount a remote directory on it, which must already exist. You
will copy files from SystemRescue to the remote system:

```
  # mkdir /mnt/ remote
  # sshfs duchess@pc:rescue/ /mnt/ remote /

```

**19.8 Copying Files over the Network with scp and sshfs** **|** **443**

```
  # ls /mnt/ remote
  rescue
```

Now you can use the _cp_ command on SystemRescue, or use a graphical file manager
to copy files (Figure 19-7).

_Figure 19-7. Copy files on SystemRescue with a graphical file manager_

When you are finished, run **`fusermount -u`** **_`remote`_** to cleanly unmount the _sshfs_ file‐
system.

**Discussion**

If you have disabled SSH password authentication on the system you are copying the
files to, reenable it temporarily by commenting out _PermitRootLogin no_ in _/etc/ssh/_
_sshd_config_ .

The syntax for connecting to the remote directory is relative to the user account you
are logging into. _duchess@pc:_ is the same as _duchess@pc:/home/duchess_ . _duchess@pc:/_

**444** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

accesses the root filesystem. When you need to edit system configuration files, use
_duchess@pc:/etc_ ; for bootfiles, use _duchess@pc:/boot_, and so on.

You can create the remote directory from SystemRescue with _ssh_ :

```
  # ssh duchess@pc
  duchess@pc's password:
  duchess@pc:~$ mkdir remote
```

**See Also**

 - Recipe 6.5

 - Chapter 12

**19.9 Repairing GRUB from SystemRescue**

**Problem**

Your GRUB bootloader is broken, and your system does not boot.

**Solution**

Boot up SystemRescue, create a _chroot_ environment, and reinstall GRUB.

After starting up SystemRescue, create a _chroot_ environment for the root filesystem
on the host:

```
  # mkdir /mnt/linux
  # mount /dev/ sda2 /mnt/linux
  # mount -o bind /proc /mnt/linux/proc
  # mount -o bind /dev /mnt/linux/dev
  # mount -o bind /sys /mnt/linux/dev
```

Enter the _chroot_ environment:

```
  # chroot /mnt/linux /bin/bash
  :/ #
```

If _/boot_ is on its own partition, mount it:

```
  :/ # mount /dev/sda1 /boot/
```

Now reinstall GRUB:

```
  :/ # grub-install /dev/sda
```

When this is completed, type **`exit`** to leave the _chroot_ environment, then unmount all
the filesystems. Reboot your system, and GRUB should work.

**19.9 Repairing GRUB from SystemRescue** **|** **445**

**Discussion**

Be very careful when creating a _chroot_ environment, and make sure you are using the
correct partitions and filesystems. _chroot_, change root, is a great utility for changing
to a different root filesystem without rebooting.

You must unmount all _chroot_ filesystems so that they unmount cleanly. It should be
all right to simply reboot, but it is cheap insurance to manually unmount them first.

**See Also**

 - _man 1 chroot_

**19.10 Resetting a Windows Password**

**Problem**

You lost your Windows password, and you don’t want to jump through the usual
Windows hoops to reset it.

**Solution**

No worries, for SystemRescue will have you back in action in a jiffy. Boot up System‐
Rescue on your Windows machine, then mount your Windows system directory:

```
  # mkdir /mnt/windows
  # mount /dev/ sda2
```

Navigate to the _/mnt/windows/Windows/System32/config_ directory, then use the
_chntpw_ (change NT password) command to list users:

```
  # cd /mnt/windows/Windows/System32/config
  # chntpw -l SAM
  chntpw version 1.00 140201, (c) Petter N Hagen
  Hive <SAM> name (from header): <\SystemRoot\System32\Config\SAM>
  ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
  File size 65536 [10000] bytes, containing 7 pages (+ 1 headerpage)
  Used for data: 318/31864 blocks/bytes, unused: 29/12968 blocks/bytes.

  | RID -|---------- Username ------------| Admin? |- Lock? --|
  | 01f4 | Administrator         | ADMIN |     |
  | 03e9 | duchess            | ADMIN |     |
  | 01f7 | DefaultAccount         |    | dis/lock |
  | 01f5 | Guest             |    | dis/lock |
  | 01f8 | WDAGUtilityAccount       |    | dis/lock |

```

**446** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

Examine the information on the user you want to change:

```
  # chntpw -u Administrator SAM
  chntpw version 1.00 140201, (c) Petter N Hagen
  Hive <SAM> name (from header): <\SystemRoot\System32\Config\SAM>
  ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
  File size 65536 [10000] bytes, containing 9 pages (+ 1 headerpage)
  Used for data: 321/33816 blocks/bytes, unused: 34/27336 blocks/bytes.

  ================= USER EDIT ====================

  RID   : 0500 [01f4]
  Username: Administrator
  fullname:
  comment : Built-in account for administering the computer/domain
  homedir :

  00000220 = Administrators (which has 2 members)

  Account bits: 0x0210 =
  [ ] Disabled    | [ ] Homedir req.  | [ ] Passwd not req. |
  [ ] Temp. duplicate | [X] Normal account | [ ] NMS account   |
  [ ] Domain trust ac | [ ] Wks trust act. | [ ] Srv trust act  |
  [X] Pwd don't expir | [ ] Auto lockout  | [ ] (unknown 0x08) |
  [ ] (unknown 0x10) | [ ] (unknown 0x20) | [ ] (unknown 0x40) |

  Failed login count: 0, while max tries is: 0
  Total login count: 5

  - - - - User Edit Menu:
  1 - Clear (blank) user password
  2 - Unlock and enable user account [probably locked now]
  3 - Promote user (make user an administrator)
  4 - Add user to a group
  5 - Remove user from a group
  q - Quit editing user, back to user select
  Select: [q] ^
```

Enter **`1`** to remove the existing password:

```
  Select: [q] ^ 1
  Password cleared!
  [...]
```

Press **`q`** to quit, and **`y`** to “write hive files,” which saves your changes.

Now the Administrator, or whatever user you selected, must log in and set a new
password.

**19.10 Resetting a Windows Password** **|** **447**

**Discussion**

You cannot create a new password or recover the old one with _chntpw_, but only delete
it. Then you log in without a password and create a new password, or, if your user is
present, let them do it.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

 - _man 8 chntpw_

**19.11 Rescuing a Failing Hard Disk with GNU ddrescue**

**Problem**

You suspect that your hard disk is dying, and you want to copy your data from it
before it expires.

**Solution**

You want the excellent GNU _ddrescue_ utility. _ddrescue_ tries to copy all the good blocks
first, saving as much data as possible, and skips over the bad blocks, tracking their
locations in a log file. You may make multiple passes to try to capture more data.

The disk you are trying to rescue must be unmounted. You need another disk, also
unmounted, such as a USB storage device or an internal hard disk, to copy the res‐
cued data to. Your target partition must already exist and be at least 50% larger than
the partition you are trying to rescue.

The following example copies _/dev/sdb1_ to _/dev/sdc1_ :

```
  # ddrescue -f -n /dev/sdb1 /dev/sdc1 ddlogfile
  GNU ddrescue 1.25
  Press Ctrl-C to interrupt
  ipos:  100177 MB, non-trimmed: 0 B  current rate:  207 MB/s
  opos:  100177 MB, non-scraped: 0 B  average rate: 83686 kB/s
  non-tried:  47868 MB, bad-sector: 0 B,   error rate:   0 B/s
  rescued:  100177 MB,  bad areas: 0,     run time:  23m 56s
  pct rescued:  66.77%, read errors: 0,  remaining time:   6m 4s
  time since last successful read:     0s
  Copying non-tried blocks... Pass 1 (forwards)
```

This will take some time. When it is finished the last line will say “Finished.”

This example does one pass, copying the most easily read blocks as quickly as possi‐
ble. This is a good tactic on a drive with a lot of errors because _ddrescue_ won’t spend a

**448** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

lot of time trying to recover the most damaged blocks. After making this first pass,
run it three more times to try to recover more data:

```
  # ddrescue -d -f -r3 /dev/sdb1 /dev/sdc1 ddlogfile
```

When it is finished, run a filesystem check on the recovery disk, which should remain
unmounted. This example checks and automatically repairs Ext4 filesystems:

```
  # e2fsck -vfp /dev/sdc1
```

_-f_ forces a check, in case _e2fsck_ thinks the filesystem is clean. _-p_ is short for preen, or
repair, and _-v_ is verbose. If it finds a problem that requires your intervention, it prints
a description of the problem and exits.

_e2fsck -vf [device]_ launches an interactive check and repair.

_fsck.vfat -vfp [device]_ is for FAT16/32.

_xfs_repair [device]_ is for XFS filesystems.

If your recovered filesystem passes the filesystem checks, go ahead and copy your files
to their final location. If there are still problems, mount it read-only:

```
  # mkdir /mnt/sdc1-copy
  # mount -o ro /dev/sdc1 /mnt/sdc1-copy
```

Then copy as many files as you can to another disk.

**Discussion**

Make sure you have GNU _ddrescue_, by Antonio Diaz Diaz, and not _dd-rescue_ by Kurt
Garloff. _dd-rescue_ is a great tool, but it is more complicated to use.

_ddrescue_ copies at the block level, so it doesn’t matter what the filesystem is that you
are trying to rescue. _ddrescue_ will make an exact copy regardless of what filesystems
your Linux supports.

If _ddrescue_ runs out of space, it will fail at the very end, so be sure your recovery drive
has a generous amount of room.

You can use _ddrescue_ on USB sticks, CompactFlash, and SD cards.

**See Also**

 - [GNU ddrescue](https://oreil.ly/mMxQf)

 - _man 8 fsck (e2fsprogs)_

**19.11 Rescuing a Failing Hard Disk with GNU ddrescue** **|** **449**

**19.12 Managing Partitions and Filesystems from**
**SystemRescue**

**Problem**

You want to partition your hard disk or make changes to filesystem, and you need to
do it from an external Linux system.

**Solution**

Use SystemRescue. SystemRescue includes both GParted and _parted_ . You don’t have
to mount any filesystems, and SystemRescue will operate directly on the block devices
on your host system. Use _lsblk_ to see your host block devices:

```
  [root@systemrescue ~]# lsblk -p -o NAME,FSTYPE,LABEL
  NAME     FSTYPE   LABEL
  /dev/loop/0  squashfs
  /dev/sr0
  /dev/sr1   iso9660  RESCUE800
  /dev/sda
  ├─/dev/sda1  vfat
  ├─/dev/sda2  xfs    osuse15-2
  ├─/dev/sda3  xfs    home
  ├─/dev/sda4  xfs
  └─/dev/sda5  swap
  /dev/sdb
  └─/dev/sdb1  xfs    backups
  /dev/sr0
```

Follow the recipes in Chapters 8, 9, and 11 for managing partitions and filesystems.

**See Also**

 - Chapter 8

 - Chapter 9

 - Chapter 11

**450** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

**19.13 Creating a Data Partition on Your SystemRescue**
**USB Drive**

**Problem**

SystemRescue on USB drives is working well for you, but you want to know how to
partition your device with the SystemRescue root filesystem on the first partition and
a writable filesystem on the second partition. Then you will need only a single device
for copying files.

**Solution**

You can do this in just a few steps.

The stock SystemRescue image cannot boot from a partition. It uses less than a giga‐
byte of space, so any USB stick will have a lot of wasted space. The trick to making
SystemRescue bootable from a partition is to make your SystemRescue ISO capable
of booting from a partition, add a Master Boot Record (MBR), then install the boot
code, _mbr.bin_ .

You need _isohybrid_ and _mbr.bin_, which are provided by _syslinux_ . This is provided by
the _syslinux_ package on Fedora and openSUSE, and by _syslinux-utils_ and _install-mbr_
on Ubuntu.

In the following examples, replace _/dev/sdc_ with your own device.

First, make the SystemRescue image bootable from a partition:

```
  $ isohybrid --partok systemrescuecd-8.01-amd64.iso
```

Create an _msdos_ partition table on your USB drive. Use GParted (Recipe 9.2) or
_parted_ :

```
  $ sudo parted /dev/ sdc
  (parted) mklabel msdos
```

Create two partitions on your USB drive. Set the filesystem type on Partition 1 as
FAT32, and set the _boot_ flag. The following example creates an approximately 2 GB
boot partition:

```
  (parted) mkpart "sysrec" fat32 1MB 2000MB
  (parted) set 1 boot
```

Add a second partition for data storage, using any filesystem type you want. The fol‐
lowing example creates a 2 GB partition, then quits _parted_ :

```
  (parted) mkpart "data" xfs 2001MB 4000MB
  (parted) q

```

**19.13 Creating a Data Partition on Your SystemRescue USB Drive** **|** **451**

Create your filesystems. Partition 1 is FAT32, with the label _SYSRESCUE_ ; Partition 2
is XFS, labeled _data_ :

```
  $ sudo mkfs.fat -F 32 -n SYSRESCUE /dev/sdc1
  $ sudo mkfs.xfs -L data /dev/sdc2
```

Install SystemRescue to the first partition:

```
  $ sudo dd status=progress if= systemrescuecd-8.01-amd64.iso of=/dev/ sdc1
```

On Ubuntu, install the MBR to the USB drive:

```
  $ sudo install-mbr /dev/ sdc
```

On other Linuxes, use _dd_ :

```
  $ sudo if= /usr/share/syslinux/mbr.bin of=/dev/ sdc
```

_mbr.bin_ may be in a different directory, depending which Linux you are using.

Boot up your SystemRescue drive, and it should start up normally.

**Discussion**

Your filesystems do not need labels; they are a convenience to help you remember
what they are for.

You may use any filesystem on the first partition. FAT32 is universal, so you can boot
SystemRescue on Linux, macOS, and Windows. For copying files from macOS and
Windows, format your data partition as FAT32 or exFAT.

You will have to mount your second partition manually, then you can use it however
you want. It is convenient for copying files from the host system, and the coolest
thing about having this writable partition is you can use it as a backing store for stor‐
ing changes you make to SystemRescue, such as configuration changes and installing
software. See Recipe 19.14 to learn all about it.

**See Also**

 - Chapter 8

 - Chapter 11

 - _[https://system-rescue.org](https://system-rescue.org)_

 - _man 1 isohybrid_

 - _man 1 dd_

**452** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

**19.14 Preserving Changes in SystemRescue**

**Problem**

SystemRescue is working well for you, but you wish you could preserve some changes
and not have to start over every time you start SystemRescue.

**Solution**

See Recipe 19.13 to learn how to create a writable partition on your SystemRescue
USB drive. Give this partition a filesystem label, such as _data_ . Once this is set up, boot
up SystemRescue, select your boot menu choice, press the Tab key, and append
**`cow_label=`** **_`data`_** to your boot selection (Figure 19-8).

_Figure 19-8. Appending boot options_

SystemRescue mounts both of your partitions in _/run/archiso/_ :

```
  # lsblk -p
  lsblk
  NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
  [...]
  sdc   8:32  1  3.7G 0 disk
  ├─sdc1  8:33  1   2G 0 part /run/archiso/bootmnt
  └─sdc2  8:34  1  152G 0 part /run/archiso/cowspace

```

**19.14 Preserving Changes in SystemRescue** **|** **453**

All changes you make to SystemRescue are stored in _/run/archiso/cowspace/persis‐_
_tent_RESCUE800_, and the root filesystem remains the same. _RESCUE800_ is different
for each SystemRescue release, according to the release number.

You can configure SystemRescue just like any Linux: enable and disable services, set a
root password, change appearance, install new software, change network configura‐
tions, or write new documents.

**Discussion**

Large USB drives are inexpensive, and needing only a single rescue device is conve‐
nient. You can use either USB thumb drives or USB hard drives.

**See Also**

 - _[https://system-rescue.org](https://system-rescue.org)_

**454** **|** **Chapter 19: System Rescue and Recovery with SystemRescue**

**<u>CHAPTER 20</u>**
#### **Troubleshooting a Linux PC**

Linux includes numerous utilities to help diagnose and fix problems, enough to fill
several thick books. In this chapter, the focus is on using system logs to find out what
went wrong, building a central systemd logging server, monitoring hardware health,
finding and stopping troublesome processes, getting the best performance from hard‐
ware, and tips and tricks for diagnosing hardware issues.

**Overview**

Get to know your system logs well, and you will find the causes of problems. If learn‐
ing the cause does not point you to a solution, you have the information you need to
ask for help, whether it’s product documentation, distribution documentation, paid
support, or community support.

Get well-acquainted with the documentation for your Linux distributions, especially
changelogs and release notes, and the documentation for the servers and applications
that you use. Ubuntu, Fedora, and openSUSE all excel at maintaining their documen‐
tation and detailed release notes. Also get acquainted with the forums, wikis, and
chats for your distro, servers, and applications. For every issue you encounter, it is
likely many other users have dealt with the same issue.

**Prevention**

Most errors are caused by software. Even consumer-grade hardware is pretty robust,
and it fails most often from abuse and age. The most common hardware failures are
components with moving parts:

 - SATA and SCSI disk drives

 - CPU coolers

**455**

 - Power supplies

 - Case fans

 - CD/DVD drives

There are simple measures you can take to extend the life of your hardware. Over‐
heating and unreliable electricity are electronics killers. Good cooling is essential for
keeping your computers healthy. Good cooling comes from well-designed cases that
provide proper airflow, heat sinks and CPU coolers, and case fans oriented so that air
is pulled in and pushed out correctly. This can get a little noisy, and you can buy
cases, power supplies, and fans that run quietly. Vacuum out your computer insides
periodically with a nonstatic vacuum, and clean case filters. If you prefer using com‐
pressed air to blow the dust out, be careful with fans. If you spin them too fast you
can damage their bearings.

A power conditioner provides continuous protection from voltage sags and spikes,
and from radio and electromagnetic interference. Surge protectors cost less, but only
provide protection from surges. Voltage sags are just as damaging as spikes. A power
conditioner more than pays for itself in longer life and stable operation.

**Patience**

Patience is your best friend when debugging problems. It’s best to take it slowly and
systematically:

 - Review instructions and make sure you did not miss any steps or make a mistake.

 - Is an update available? Many times this is the solution.

 - Copy error messages and log file entries, and use them in web searches and trou‐
ble tickets.

 - What are the last things that happened before the error occurred? What are the
exact steps that created the error? Is it reproducible?

 - Are the last things that happened reversible? If the answer is yes, undo them one
at a time and test. Making multiple changes at once means you may not discover
what caused the error.

 - As a last resort, reboot. Really! This works a surprising number of times to
resolve the issue, though you may not learn what the problem was.

Some graphical applications, such as the wonderful digiKam photo manager and edi‐
tor, emit all manner of details when you start them from a terminal, as this snippet
shows after digiKam failed to start:

```
  $ digikam
  Object::connect: No such signal org::freedesktop::UPower::DeviceAdded(QString)
  Object::connect: No such signal org::freedesktop::UPower::DeviceRemoved(QString)

```

**456** **|** **Chapter 20: Troubleshooting a Linux PC**

```
  digikam: symbol lookup error: digikam: undefined symbol:
  _ZNK11KExiv2Iface14AltLangStrEdit8textEditEv
```

I have no idea what this means, but someone does, so I can reference this in a web
search, or ask for help in the digiKam forums.

When you ask for help, remember patience and courtesy. When you are asked for
additional information, provide exactly what you are asked for. When you resolve
your issue, share your solution and thank the people who helped you.

**20.1 Finding Useful Information in Logfiles**

**Problem**

Weird stuff is happening, and you need to know where to start figuring it out.

**Solution**

Log everything, and then read your logfiles. _/var/log_ contains log files, and the _dmesg_
and _journalctl_ commands display log messages. systemd manages all logs with _jour‐_
_nald_, so you will see a lot of duplication with _dmesg_ and _/var/log_ .

_dmesg_ reads the kernel ring buffer, which is a special memory location for recording
kernel activity. Look in _dmesg_ to see everything that happened at startup; hardware
activity after startup, such as attaching and removing USB devices; and network
interface activity. The kernel ring buffer is a fixed size, so new entries overwrite the
oldest entries. Nothing is lost because the kernel logs are stored in _/var/log/messages_, _/_
_var/log/dmesg_, and _journalctl_ .

Read _dmesg_ like this:

```
  $ dmesg | less
  [  0.000000] microcode: microcode updated early to revision 0x28,
  date = 2019-11-12
  [  0.000000] Linux version 5.8.0-45-generic (buildd@lcy01-amd64-024) (gcc
  (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, GNU ld (GNU Binutils for Ubuntu) 2.34)
  #51~20.04.1-Ubuntu SMP Tue Feb 23 13:46:31 UTC 2021
  (Ubuntu 5.8.0-45.51~20.04.1-generic 5.8.18)
  [...]
```

When you are looking for something specific, use _grep_, like when you are having
trouble with a storage drive:

```
  $ dmesg | grep -w sd
  [11236.888910] sd 7:0:0:0: [sdd] Attached SCSI removable disk
  [11245.095341] FAT-fs (sdd1): Volume was not properly unmounted. Some data may
  be corrupt. Please run fsck.

```

**20.1 Finding Useful Information in Logfiles** **|** **457**

**Finding Whole Words with grep**

When you want to find a word with _grep_ use the _-w_ switch. For
example, when you grep for _ping_ you will get results like piping,
escaping, sleeping. _-w_ returns only whole word matches.

Run _dmesg -T_ to see human-readable timestamps:

```
  $ dmesg -T | less
  [Tue Mar 23 15:25:17 2021] PCI: CLS 64 bytes, default 64
  [Tue Mar 23 15:25:17 2021] Trying to unpack rootfs image as initramfs...
  [Tue Mar 23 15:25:17 2021] Freeing initrd memory: 56008K
  [...]
```

The default is the seconds and nanoseconds since startup. Run _dmesg --follow_ to
monitor new events as they occur, such as plugging and unplugging USB devices.
Press Ctrl-C to stop.

Look for certain logging levels, such as errors and warnings:

```
  $ dmesg -l err,warn
```

Run _dmesg -h_ to see commands and options.

_/var/log_ is the legacy location for log files, and you will still find logs there, depending
on how your Linux distribution manages them. _/var/log_ is easy to search because
most of the files are in plain text. When you’re not sure where to start looking, _grep_
the whole directory.

For example, suppose you thought you installed _graphicsmagick_, but can’t find it. Take
a quick look in _/var/log_, and there it is, a record of its installation:

```
  $ sudo grep -ir graphicsmagick /var/log
  apt/history.log:Install: libgraphicsmagick-q16-3:amd64 (1.4+really1.3.35-1,
  automatic), graphicsmagick:amd64 (1.4+really1.3.35-1)
  [...]
  /var/log/dpkg.log:2021-03-11 17:00:57 install libgraphicsmagick-q16-3:amd64
  1.4+really1.3.35-1
  [...]
```

Systemd stuffs all logging into _journalctl_, so you can use it exclusively and not bother
with _dmesg_ and _/var/log_ :

```
  $ journalctl
```

Invoke it with _sudo_ to see if that adds any more information. Usually it doesn’t.

_journalctl_ defaults to displaying oldest entries first. Press the spacebar or PageUp/
Down keys to navigate a screen at a time, or use the arrow keys to scroll one line at a
time. Ctrl-End goes all the way to the newest, and Ctrl-Home goes back to the oldest.
Press the Q key to exit.

**458** **|** **Chapter 20: Troubleshooting a Linux PC**

See newest entries first:

```
  $ journalctl -r
```

It does not wrap long lines by default, so you have to use arrow keys to read long
lines. Make it wrap by piping its output to _less_ :

```
  $ journalctl -r | less
```

See the most recent entries, with explanation messages, if there are any. This shows an
example of an explanation message:

```
  $ journalctl -ex | less

  -- The unit grub-initrd-fallback.service has successfully entered the 'dead'
  state.
  Mar 27 10:14:29 client4 systemd[1]: Finished GRUB failed boot detection.
  -- Subject: A start job for unit grub-initrd-fallback.service has finished
  successfully
  -- Defined-By: systemd
```

Search for specific services, such as MariaDB:

```
  $ sudo journalctl -u mariadb.service
  Mar 19 16:07:27 client4 /etc/mysql/debian-start[7927]: Looking for 'mysql' as:
  /usr/bin/mysql
  Mar 19 16:07:27 client4 /etc/mysql/debian-start[7927]: Looking for 'mysqlcheck'
  as: /usr/bin/mysqlcheck
  [...]
```

Select date ranges, which you can define in several ways:

```
  $ journalctl -u mariadb.service -S today
  $ journalctl -u ssh.service -S '1 week ago'
  $ journalctl -u libvirtd.service -S '2021-03-05'
  $ journalctl -u httpd.service -S '2021-03-05' -u '2021-03-09'
  $ journalctl -u nginx.service -S '2 hours ago'
```

When you do not specify times, the default is 00:00:00, midnight. Specify times in
HH:MM:SS format:

```
  $ journalctl -u httpd.service -S '2021-03-05 13:15:00' -U now
```

Look at activity from an hour ago until 5 minutes ago and show the unit filenames:

```
  $ journalctl -S '1h ago' -U '5 min ago' -o with-unit
```

_journalctl_ sorts logs by system boot. Look at HTTP server activity since the most
recent boot, and limit the number of lines displayed to the most recent 50:

```
  $ journalctl -b -n 50 -u httpd.service
```

See what happened three boots ago:

```
  $ journalctl -b -2 -u httpd.service

```

**20.1 Finding Useful Information in Logfiles** **|** **459**

List all recorded boot sessions, with timestamps:

```
  $ journalctl --list-boots
```

You can filter for specific severity levels. When you specify a single level, in this
example, _crit_, it shows all messages from _crit_ up to the most severe level, _emerg_ :

```
  $ journalctl -b -1 -p "crit" -u nginx.service
```

Define your own range, for example from _crit_ to _warning_ :

```
  $ journalctl -b -3 -p "crit".."warning"
```

Follow new events as they are logged, starting from the 10 most recent entries:

```
  $ journalctl -n 10 -u mariadb.service -f
```

Ctrl-C stops it.

And, of course, use good old _grep_ to find things, like usernames, or any search term
you wish:

```
  $ journalctl -b -1 | grep madmax
```

**Discussion**

Severity levels are the standard syslog levels, from 0 to 7, with 0 being the most
severe, and 7 the least severe:

```
  emerg   (0)
  alert   (1)
  crit    (2)
  err    (3)
  warning  (4)
  notice   (5)
  info    (6)
  debug   (7)
```

_journalctl_ provides dozens of ways to filter and parse your output, and you can learn
even more in _man 1 journalctl_ .

**See Also**

 - _man 3 syslog_

 - _man 1 journalctl_

 - _man 1 dmesg_

 - _[https://systemd.io](https://systemd.io)_

**460** **|** **Chapter 20: Troubleshooting a Linux PC**

**20.2 Configuring journald**

**Problem**

You’re not sure what the default configuration is for _journald_, and you need to know
how to see the current configuration and how to change it.

**Solution**

_journald_ is configured in _/etc/systemd/journald.conf_ . Some default options are com‐
mented out, and all compile-time defaults are documented in _man 5 journald.conf_ .
We will take a look at the most commonly used options.

_Storage=auto_ means different things on different distros. Ubuntu and Fedora
use _/run/log/journal/_ for volatile storage, and persistent storage is in _/var/log/journal_ .
See the locations of log files, used space, and free space with _systemctl_ :

```
  $ systemctl status systemd-journald.service s
```

   - `systemd-journald.service - Journal Service`
```
  Loaded: loaded (/usr/lib/systemd/system/systemd-journald.service; static;
  vendor preset: disabled)
  Active: active (running)
  [...]
  Mar 27 15:04:40 server2 systemd-journald[508]: Runtime journal (/run/log/journal/
  1181e27c52294e97a8ca5c5af5c92e20) is 8.0M, max 2.3G, 2.3G free.
  Mar 27 15:04:55 server2 systemd-journald[508]: Time spent on flushing to /var is
  381.408ms for 1176 entries.
  Mar 27 15:04:55 server2 systemd-journald[508]: System journal (/var/log/journal/
  1181e27c52294e97a8ca5c5af5c92e20) is 16.0M, max 4.0G, 3.9G free.
```

openSUSE puts volatile storage in _/run/log/journal/_ and persistent storage in _/var/log/_
_messages_ . If you prefer to use _/var/log/journal_, create it and change the group owner
to _systemd-journal_ :

```
  $ sudo mkdir /var/log/journal
  $ sudo chgrp /var/log/journal/ systemd-journal
```

You don’t have to change anything else, and the storage is changed after reboot. Other
options are _volatile_, _persistent_, and _none_ .

_volatile_ stores logs only in memory, in _/run/log/journal/_ .

_persistent_ stores logs on disk and uses _/run/log/journal/_ when the disk is not available,
such as early in system startup.

_none_ disables all local logging, and you have the option to send log messages to a cen‐
tral logging server.

**20.2 Configuring journald** **|** **461**

_SystemMaxUse=_ controls the size of log storage on disk, and _RuntimeMaxUse=_ con‐
trols the size of volatile storage. The default is 10% of available space in the filesystem,
to a maximum of 4 GB.

_SystemKeepFree=_ and _RuntimeKeepFree=_ control how much disk space is left free for
other uses. The defaults are 15% and 4 GB. You may change these by specifying num‐
bers of bytes, or use K, M, G, T, P, and E; for example, 25 G (gigabytes).

_MaxRetentionSec=_ controls how long files are retained. The default is 0, which disa‐
bles it, and files are retained according to other settings, such as available disk space.
You may configure a time value, using `year`, `month`, `week`, `day`, `h`, or `m`, for example,
`6 month` .

**Discussion**

_journald_ automatically handles log rotation. Active files are rotated into archived files,
and archived files are deleted according to your configuration.

**See Also**

 - _man 5 journald.conf_

**20.3 Building a Logging Server with systemd**

**Problem**

You want to set up a central logging server so that logs are preserved when systems go
down, and for centralized management.

**Solution**

systemd provides a remote logging daemon, _journald_ . Client machines send their log
messages to the _journald_ server. The prerequisites are as follows:

 - A machine to host the log files

 - Network access to the logging server for clients

 - The _systemd-journal-remote_ package installed on the log server and on all clients

 - Your public key infrastructure (PKI) already in place (Recipe 13.5), with keys and
certificates distributed to servers and clients

**462** **|** **Chapter 20: Troubleshooting a Linux PC**

After installing _systemd-journal-remote_, edit _/etc/systemd/journal-remote.conf_ on the
server. I like to store encryption keys and certificates in _/etc/pki/journald/_ :

```
  [Remote]
  Seal=false
  SplitMode=host
  ServerKeyFile=/etc/pki/journald/ log-server.key
  ServerCertificateFile=/etc/pki/journald/ log-server.crt
  TrustedCertificateFile=/etc/pki/journald/ ca.crt
```

Set permissions for the server key and certificates:

```
  $ sudo chmod -R 0755 /etc/pki/journald
  $ sudo chmod 0440 /etc/pki/journald/ log-server.key
```

Change the group owner of the server private key to _systemd-journal-remote_ :

```
  $ sudo chgrp systemd-journal-remote /etc/pki/journald/ log  server.key
```

Enable and start the _systemd-journal-remote_ service, starting _systemd-journal-_
_remote.socket_ first:

```
  $ sudo systemctl enable --now systemd-journal-remote.socket
  $ sudo systemctl enable --now systemd-journal-remote.service
```

Check the status of both to make sure they started correctly. Open the necessary ports
in the server firewall:

```
  $ sudo firewall-cmd --zone= internal --add-port=19532/tcp
  $ sudo firewall-cmd --zone= internal --add-port=80/tcp
  $ sudo firewall-cmd --runtime-to-permanent
  $ sudo firewall-cmd --reload
```

On every client, create a new user, _systemd-journal-upload_ . This is the user that the
_systemd-journal-upload_ process uses to transfer log messages to the central server:

```
  $ sudo useradd -r -d /run/systemd -M -s /usr/sbin/nologin -U \
  systemd-journal-upload
```

Set permissions for the client key and certificates:

```
  $ sudo chmod -R 0755 /etc/pki/journald
  $ sudo chmod 0440 /etc/pki/journald/ client.key
```

Edit _/etc/systemd/journal-upload.conf_ with the URL and TCP port to your log server,
and the locations of the client key and certificates:

```
  [Upload]
  URL=https:// logserver.example.com:19532
  ServerKeyFile=/etc/pki/journald/ client1.key
  ServerCertificateFile=/etc/pki/journald/ client1.crt
  TrustedCertificateFile=/etc/pki/journald/ ca.crt

```

**20.3 Building a Logging Server with systemd** **|** **463**

Restart the _systemd-journal-upload.service_ :

```
  $ sudo systemctl restart systemd-journal-upload.service
```

If it restarts successfully, without errors, run the following steps to test that the client
is sending log entries to the server. Check the log directory on the server:

```
  $ sudo ls -la /var/log/journal/remote/
  total 7204
  drwxr-xr-x 2 systemd-journal-remote systemd-journal-remote 6 Mar 26 16:41 .
  drwxr-sr-x+ 4 root          systemd-journal    60 Mar 26 16:41 ..
  rw-r----- 1 systemd-journal-remote systemd-journal-remote 8388608 Mar 26 1
  10:46 'remote-CN=client1.example.com'
```

Looking good so far. Now, send the server a message from the client:

```
  $ sudo logger -p syslog.debug "Hello, I am client1! Do you hear me?"
```

Run your favorite _journalctl_ incantation on the server to call up the most recent
entries. If you see the client message, you know you set it all up correctly:

```
  Mar 27 18:30:11 client1 madmax[15228]: Hello, I am client1! Do you hear me?
```

**Discussion**

A central logging server preserves client logs and centralizes logging storage for easier
maintenance and analysis. Every client has their own directory on the server.

_Seal=false_ disables cryptographic signing of journal entries. To try it out, refer to the
_--setup-keys_ option in _man 1 journalctl_ . I could not find a definitive answer if it pro‐
vides a meaningful benefit, but it doesn’t hurt to learn about it.

_SplitMode=host_ stores each client log in their own file. Set it to _false_ to dump every‐
thing into a single file.

_ServerKeyFile=_, _ServerCertificateFile=_, and _TrustedCertificateFile=_ are where your
encryption keys and certificates are stored.

**See Also**

 - _man 5 journal-remote.conf_

 - _man 5 journald.conf_

 - _man 1 journalctl_

**464** **|** **Chapter 20: Troubleshooting a Linux PC**

**20.4 Monitoring Temperatures, Fans, and Voltages**
**with lm-sensors**

**Problem**

Your want to measure temperatures inside your computer case, fan speeds, and
voltages.

**Solution**

Use _lm-sensors_ to continually monitor CPU, hard disk, and case temperatures. This is
supplied by the _sensors_ package on openSUSE, _lm_sensors_ on Fedora, and _lm-sensors_
on Ubuntu.

After installing _lm-sensors_, run the _sensors-detect_ command to calibrate _lm-sensors_ to
your hardware:

```
  $ sudo sensors-detect
  # sensors-detect version 3.6.0
  # Board: ASRock H97M Pro4
  # Kernel: 5.8.0-45-generic x86_64
  # Processor: Intel(R) Core(TM) i7-4770K CPU @ 3.50GHz (6/60/3)

  This program will help you determine which kernel modules you need
  to load to use lm_sensors most effectively. It is generally safe
  and recommended to accept the default answers to all questions,
  unless you know what you're doing.

  Some south bridges, CPUs or memory controllers contain embedded sensors.
  Do you want to scan for them? This is totally safe. (YES/no):
  [...]
```

Press Enter to accept all of the defaults. When it is finished you will see something
like this:

```
  To load everything that is needed, add this to /etc/modules:
  #----cut here---  # Chip drivers
  coretemp
  nct6775
  #----cut here---  If you have some drivers built into your kernel, the list above will
  contain too many modules. Skip the appropriate ones!

  Do you want to add these lines automatically to /etc/modules? (yes/NO) yes
  Successful!
```

The modules will be loaded after a restart, or you can load them immediately:

```
  $ sudo systemctl restart systemd-modules-load.service

```

**20.4 Monitoring Temperatures, Fans, and Voltages with lm-sensors** **|** **465**

Now run the _sensors_ command and see what you get:

```
  $ sensors
  coretemp-isa-0000
  Adapter: ISA adapter
  Package id 0: +42.0°C (high = +86.0°C, crit = +96.0°C)
  Core 0:    +34.0°C (high = +86.0°C, crit = +96.0°C)
  Core 1:    +35.0°C (high = +86.0°C, crit = +96.0°C)
  Core 2:    +32.0°C (high = +86.0°C, crit = +96.0°C)
  Core 3:    +31.0°C (high = +86.0°C, crit = +96.0°C)

  nouveau-pci-0300
  Adapter: PCI adapter
  GPU core:   +1.01 V (min = +0.70 V, max = +1.20 V)
  fan1:    2850 RPM
  temp1:    +51.0°C (high = +95.0°C, hyst = +3.0°C)
  (crit = +105.0°C, hyst = +5.0°C)
  (emerg = +135.0°C, hyst = +5.0°C)

  dell_smm-virtual-0
  Adapter: Virtual device
  Processor Fan: 1070 RPM
  Other Fan:    0 RPM
  Other Fan:   603 RPM
  CPU:      +41.0°C
  SODIMM:     +25.0°C
  SODIMM:     +35.0°C
  SODIMM:     +34.0°C
```

This shows information for CPU cores, a graphics adapter, fans, and memory mod‐
ules. You see the current temperatures, and the high, critical, and emergency temper‐
ature ranges. CPUs have built-in self-preservation and shut down when they get
too hot.

Use the _watch_ command to see updated status every two seconds, with any differ‐
ences highlighted:

```
  $ watch -d sensors
```

Set a different update interval, like 10 seconds:

```
  $ watch -d -n 10 sensors
  Every 10.0s: sensors
  [...]
```

Press Ctrl-C to stop.

**Discussion**

_lm_sensors_ is not magic, it reads only devices that have temperature sensors and that
also have Linux drivers. Most temperature sensors are not very precise, so don’t
worry about small fluctuations.

**466** **|** **Chapter 20: Troubleshooting a Linux PC**

Monitoring temperatures, voltages, and fan speeds can give you early warning of
trouble. It is cheaper to replace a fan than to rebuild a cooked computer. Voltage
drops could indicate a failing power supply or a bad connection.

Before you modify the _/etc/modules_ file, check your kernel configuration to see if the
modules suggested by _sensors-detect_ are already loaded, or are statically compiled.
Your kernel configuration file is in the _/boot_ directory, named _config-kernel-version_,
like _config-5.8.0-45-generic_ . For example, search for the _nct6775_ module:

```
  $ grep -i nct6775 config-5.8.0-45-generic
  CONFIG_SENSORS_NCT6775=m
```

The _m_ means it is a loadable kernel module. Check if it is already loaded:

```
  $ lsmod | grep nct6775
```

If this returns nothing, go ahead and add it to _/etc/modules_ . If it were statically com‐
piled, it would look like this in _config-*_ :

```
  CONFIG_SENSORS_NCT6775=y
```

The _y_ means it is built-in to the kernel, so do not add it to _/etc/modules_ .

**See Also**

 - _man 1 watch_

 - _man 1 sensors_

 - _man 8 lsmod_

 - _[https://kernel.org](https://kernel.org)_

**20.5 Adding a Graphical Interface to lm-sensors**

**Problem**

You want a configurable graphical display for _lm-sensors_ that updates automatically.

**Solution**

You have several good choices. Graphical frontends to _lm-sensors_ also support other
monitors, such as _smartmontools_ and _hddtemp_ . Psensor provides a large display, col‐
ored graphs, and simple configuration to rename labels and show just what you want
to see (Figure 20-1).

Psensor supports alarms. Enable alarms individually, like for the CPU cores and fans,
by clicking on each monitor to bring up a Preferences menu (Figure 20-2).

**20.5 Adding a Graphical Interface to lm-sensors** **|** **467**

_Figure 20-1. Psensor tracks multiple hardware monitors_

_Figure 20-2. Enabling alarms and alarm thresholds_

You need to write a simple script to set up an alarm, like the following example:

```
  #!/bin/bash
  # toohot.sh, plays a mad klavichord riff when a sensor monitor
  # exceeds its upper limit

  play /home/madmax/Music/klavichord-4.wav
```

Install _sox_ to get the _play_ command. Make your script executable:

```
  $ chmod +x toohot.sh
```

Test it:

```
  $ play toohot.sh

```

**468** **|** **Chapter 20: Troubleshooting a Linux PC**

When it works to your satisfaction, configure Psensor to use it. Open Psensor → Pref‐
erences → Sensors (Figure 20-3).

_Figure 20-3. Setting up an alarm_

A simple way to test it in Psensors is to set some of your maximum temperatures too
low.

Many desktop environments, such as Xfce4, GNOME, and KDE, have nice little task‐
bar plug-ins, such as what’s shown in Figure 20-4 for Xfce4.

_Figure 20-4. Xfce taskbar plug-in for lm-sensors_

All of them have _sensor_ in their package names, except _gnome-shell-extension-freon_ .

**Discussion**

You can write your script to automatically shut the system down when an alarm is
triggered, like this simple example:

```
  #!/bin/bash
  echo "Help, too hot, I am shutting down right now!" && shutdown -h now
```

**See Also**

 - _man 1 play_

 - _man 1 sensors_

 - [Psensor](https://oreil.ly/IcRok)

**20.5 Adding a Graphical Interface to lm-sensors** **|** **469**

**20.6 Monitoring Hard Disk Health with smartmontools**

**Problem**

You need to know when a hard disk is faulty or, preferably, when it is becoming faulty,
so you can replace it before you lose data.

**Solution**

Most hard disks and solid-state drives come with S.M.A.R.T. (Self-Monitoring Analy‐
sis and Reporting Technology) built in. S.M.A.R.T. tracks and records certain perfor‐
mance attributes, which you can monitor to (hopefully) predict immiment failures.
Linux users have _smartmontools_ to read this information and give warnings.

_smartmontools_ is provided by the _smartmontools_ package. It should install and start a
systemd service automatically, which you can check with _systemctl_ :

```
  $ systemctl status smartd.service
```

Use the _smartctl_ command to see if your disk has S.M.A.R.T. support. Look for the
_SMART_ support lines:

```
  $ sudo smartctl -i /dev/ sda
  smartctl 7.1 2019-12-30 r5022 [x86_64-linux-5.8.0-45-generic] (local build)
  Copyright (C) 2002-19, Bruce Allen, Christian Franke, www.smartmontools.org

  === START OF INFORMATION SECTION ===
  Model Family:   Seagate Desktop HDD.15
  Device Model:   ST4000DM000-1F2168
  [...]
  SMART support is: Available - device has SMART capability.
  SMART support is: Enabled
```

Enable and disable _smartctl_ for each disk you want to monitor:

```
  $ sudo smartctl -s on /dev/ sda
  $ sudo smartctl -s off /dev/ sda
```

Use the _-x_ flag for a complete data dump:

```
  $ sudo smartctl -x /dev/ sda
```

Run the short health check:

```
  $ sudo smartctl -H /dev/ sda
  smartctl 7.1 2019-12-30 r5022 [x86_64-linux-5.8.0-45-generic] (local build)
  Copyright (C) 2002-19, Bruce Allen, Christian Franke, www.smartmontools.org

  === START OF READ SMART DATA SECTION ===
  SMART overall-health self-assessment test result: PASSED
```

Use the _-Hc_ flags to see the complete report.

**470** **|** **Chapter 20: Troubleshooting a Linux PC**

Check the log file:

```
  $ sudo smartctl -l error /dev/ sda
  smartctl 7.0 2019-05-21 r4917 [x86_64-linux-5.3.18-lp152.66-preempt] (SUSE RPM)
  Copyright (C) 2002-18, Bruce Allen, Christian Franke, www.smartmontools.org

  === START OF READ SMART DATA SECTION ===
  SMART Error Log Version: 1
  No Errors Logged
```

There is a short self-test and a long self-test. They tell you how long each test will take
when you start them:

```
  $ sudo smartctl -t long /dev/ sda
  [...]
  === START OF OFFLINE IMMEDIATE AND SELF-TEST SECTION ===
  Sending command: "Execute SMART Extended self-test routine immediately in
  off-line mode".
  Drive command "Execute SMART Extended self-test routine immediately in off-line
  mode" successful.
  Testing has begun.
  Please wait 109 minutes for test to complete.
  Test will complete after Thu Mar 25 17:06:33 2021

  Use smartctl -X to abort test.
```

It will not notify you when it is finished, and you can check the log file at any time:

```
  $ sudo smartctl -l selftest /dev/ sda

  [sudo] password for carla:
  [...]
  === START OF READ SMART DATA SECTION ===
  SMART Self-test log structure revision number 1
  Num Test_Description  Status         Remaining LifeTime(hours)
  # 1 Extended offline  Self-test routine in progress 70%   7961
  # 2 Short offline    Completed without error    00%   7960
  # 3 Short offline    Completed without error    00%   7952
  [...]
```

Remember to update the hard drive database periodically:

```
  $ sudo update-smart-drivedb
  /usr/share/smartmontools/drivedb.h updated from branches/RELEASE_7_0_DRIVEDB
```

**Discussion**

S.M.A.R.T. is about 60% reliable. It could be better, but the S.M.A.R.T. standard leaves
a lot of room for interpretation, and every drive manufacturer implements it differ‐
ently. Manufacturer documentation is scarce, and the best resources I have found are
Wikipedia and _[https://smartmontools.org](https://smartmontools.org)_ . As always, your best insurance is regular
backups.

**20.6 Monitoring Hard Disk Health with smartmontools** **|** **471**

Even so, it’s free, it’s easy to use, and often useful. Pay attention to the _Pre-fail_
attributes (as in the following snippet), and review the introduction to this chapter on
how to get better performance and reliability from your systems.

Run _sudo smartctl -a /dev/sda_ to dump all the S.M.A.R.T. data. The section that tends
to cause alarm is this one:

```
  SMART Attributes Data Structure revision number: 10
  Vendor Specific SMART Attributes with Thresholds:
  ID# ATTRIBUTE_NAME     FLAG   VALUE WORST THRESH TYPE   UPDATED
  1 Raw_Read_Error_Rate   0x000f  119  099  006  Pre-fail Always
  3 Spin_Up_Time      0x0003  092  091  000  Pre-fail Always
  4 Start_Stop_Count    0x0032  099  099  020  Old_age  Always
  5 Reallocated_Sector_Ct  0x0033  100  100  010  Pre-fail Always
  7 Seek_Error_Rate     0x000f  059  057  030  Pre-fail Always
  9 Power_On_Hours     0x0032  089  089  000  Old_age  Always
  10 Spin_Retry_Count    0x0013  100  100  097  Pre-fail Always
  12 Power_Cycle_Count    0x0032  099  099  020  Old_age  Always
  183 Runtime_Bad_Block    0x0032  100  100  000  Old_age  Always
  184 End-to-End_Error    0x0032  100  100  099  Old_age  Always
  187 Reported_Uncorrect   0x0032  100  100  000  Old_age  Always
  188 Command_Timeout     0x0032  100  099  000  Old_age  Always
  189 High_Fly_Writes     0x003a  100  100  000  Old_age  Always
  190 Airflow_Temperature_Cel 0x0022  072  059  045  Old_age  Always
  191 G-Sense_Error_Rate   0x0032  100  100  000  Old_age  Always
  192 Power-Off_Retract_Count 0x0032  100  100  000  Old_age  Always
  193 Load_Cycle_Count    0x0032  096  096  000  Old_age  Always
  194 Temperature_Celsius   0x0022  028  041  000  Old_age  Always
  197 Current_Pending_Sector 0x0012  100  100  000  Old_age  Always
  198 Offline_Uncorrectable  0x0010  100  100  000  Old_age  Offline
  199 UDMA_CRC_Error_Count  0x003e  200  200  000  Old_age  Always
  240 Head_Flying_Hours    0x0000  100  253  000  Old_age  Offline
  241 Total_LBAs_Written   0x0000  100  253  000  Old_age  Offline
  242 Total_LBAs_Read     0x0000  100  253  000  Old_age  Offline
```

The `TYPE` column tells the type of the attributes, either `Pre-fail` or `Old_age` . When
you see all those `Pre-fail` and `Old_age` labels, it doesn’t mean your disk is doomed,
that is just the type of attribute on that row.

`Pre-fail` is a critical attribute, one that may indicate imminent failure, and it is
always included in health assessments.

`Old_age` is a noncritical attribute; it is not included in disk health reports.

`ID#` and `ATTRIBUTE_NAME` identify each attribute. These vary by manufacturer.

`FLAG` is the attribute handling flag, and has no relevance to disk health.

The `VALUE` column displays the current values for the attributes. These range from
0-255, except for 0, 254, and 255. 253 means “unused,” like when you have a new

**472** **|** **Chapter 20: Troubleshooting a Linux PC**

drive. `VALUE` is a scale from good to bad, with higher numbers being good and lower
numbers bad, except the temperature attributes, which are temperatures in Celsius.

`WORST` is the lowest value recorded for that attribute.

`THRESH` is the lowest threshold for each attribute, and when a `Pre-fail` attribute falls
below `THRESH`, then disk failure may be imminent.

`UPDATED` is supposed to indicate when the attributes have been updated. Always is
both online and offline, and Offline supposedly means only when offline tests are
run. Usually this is inaccurate, and not all that helpful in any case.

If an attribute enters a failed state, the time it failed is recorded in _WHEN_FAILED_ .

_RAW_VALUE_ is particular to each manufacturer. Ignore it.

**See Also**

 - _man 8 smartctl_

 - _man 8 smartd_

 - _man 8 update-smart-drivedb_

 - _man 5 smartd.conf_

**20.7 Configuring smartmontools to Send Email Reports**

**Problem**

You want email notifications of any problems emailed to you by _smartd_ .

**Solution**

First, check if you already have system mail set up and working by sending a test mes‐
sage to another user on the system, such as root:

```
  $ echo "Hello, this is my message" | mail -s "Message subject" root@localhost

  [root@localhost ~]# mail
  "/var/mail/root": 1 message 1 unread
  >U "/var/mail/root": 1 message 1 new
  >N  1 stash  Mon Mar 29 15:26 13/429  Message subject
  ?
```

Press 1 to read the message, and q to quit. This shows that system mail is already set
up. If it is not, install _mailx_ and _postfix_ . _mailx_ is a mail user agent (MUA), which is a
mail client like Evolution, Thunderbird, KMail, Mutt, and so on. _postfix_ is a mail

**20.7 Configuring smartmontools to Send Email Reports** **|** **473**

transfer agent (MTA). You need both. After installation, check if they are running
with _systemctl_ :

```
  $ systemctl status smartd.service
  $ systemctl status postfix.service
```

If they are not, enable and start them. Then try your test message again.

```
  $ sudo systemctl enable --now smartd.service
  $ sudo systemctl enable --now postfix.service
```

_smartd_ is configured in _/etc/smartd.conf_ or _/etc/smartmontools/smartd.conf_ . The
default is to scan for all possible devices and email error reports to the root user. It is
better to configure which devices you want monitored. Every Linux has its own spe‐
cial configuration. The following should work on all of them, and of course you must
specify your own disks and email address:

```
  DEFAULT -a -o on -S on -s (S/../.././02|L/../../5/01):
  /dev/ sda
  /dev/ sdb
  /dev/ sdc
  DEFAULT -H -m root -M test
```

Save your configuration changes and reload _smartd.service_ :

```
  $ sudo systemctl reload smartd.service
```

**Discussion**

The default behavior in _smartd.conf_ is to scan for all available drives. It is more effi‐
cient to specify the drives you want to monitor.

The _-a_ flag is the same as all of these combined:

 - _-H_, check the S.M.A.R.T. health status

 - _-f_, report Usage Attributes ( _VALUE_ and _WORST_ ) failures

 - _-t_, report changes in Prefailure and Usage Attributes

 - _-l_, report increases in ATA errors

 - _-l selftest_, report increases in Self-Test Log errors

 - _-l selfteststs_, report changes of Self-Test execution status

 - _-C 197_, report nonzero values of the current pending sector count

 - _-U 198_, report nonzero values of the offline pending sector count

That covers all the important stuff, and of course you may tweak it to report whatever
attributes you like.

**474** **|** **Chapter 20: Troubleshooting a Linux PC**

_-M test_ sends the specified user (in the preceding example, _-m root@localhost_ ) a test
message at every startup. You can remove this when you are confident it is working
the way you want.

There are several packages that provide the _mail_ binary: _mailutils_, _mailx_, _bsd-mailx_,
and _s-nail_, to name a few. For a simple local mailer for system daemons to use, any of
them will do the job, and the _mail_ binary takes the same options on all of them.

You don’t have to use _postfix_, but can use any MTA that you prefer, such as Exim or
Sendmail.

**See Also**

 - _man 8 smartd_

 - _man 5 smartdconf_

**20.8 Diagnosing a Sluggish System with top**

**Problem**

Your system usually runs well, but now everything is bogging down and taking for‐
ever. Applications are taking a long time to start or shut down, or are slow to respond
to user input. You need to find out the cause, and then fix it.

**Solution**

Fire up the _top_ command to see which processes are using excessive system resources.
CPU and memory hogs make your nice powerful system feel ancient:

```
  $ top
  Tasks: 284 total,  1 running, 283 sleeping,  0 stopped,  0 zombie
  %Cpu(s): 6.4 us, 4.8 sy, 0.0 ni, 88.9 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
  MiB Mem : 15691.4 total,  6758.9 free,  4913.0 used,  4019.6 buff/cache
  MiB Swap: 15258.0 total, 15258.0 free,   0.0 used. 10016.5 avail Mem

  PID USER   PR NI  VIRT  RES  SHR S  %CPU %MEM  TIME+ COMMAND
  1299 duchess   9 0 2803912 22296 17904 S 80.5  0.1 172:25 Web Content
  1685 duchess   20 0 3756840 543124 241296 S  7.6  3.4  27:53 firefox
  15926 libvirt+  20 0 5151504  2.3g 25024 S  1.7 15.3  1:39 qemu
  [...]
```

_top_ runs until you stop it, refreshing every few seconds and displaying processes in
order from the most to least active. Press the q key to exit.

**20.8 Diagnosing a Sluggish System with top** **|** **475**

This shows a wealth of information. The relevant bit is that `Web Content` is using
80.5% share of CPU time. Poorly constructed websites are a common cause of bring‐
ing your system to a halt. The fast way to correct this is to kill the offending process.

Process IDs are in the left column. Press the k key to open the kill dialog. If the
default PID to kill is correct, press the Enter key. Press Enter to accept the default _15/_
_sigterm_ to terminate the process:

```
  PID to signal/kill [default pid = 1299]
  Send pid 1299 signal [15/sigterm]
```

If that does not kill the process, use the nuclear option, _9_, which is _sigkill_ :

```
  PID to signal/kill [default pid = 1299]
  Send pid 1299 signal [15/sigterm] 9
```

If you do not have sufficient permissions to kill the process, start _top_ with _sudo_ . Or,
run _sudo kill <pid>_ in another terminal.

**Discussion**

Killing a process is not always the best solution. If the process is controlled by sys‐
temd, systemd may immediately restart it, or other processes may be dependent on it,
and then you risk making a mess. If possible, shut it down with _systemctl stop <service_
_name>_ . If the offending process is not controlled by systemd, then go ahead and
kill it.

The default PID to kill is always the one at the top, the one using the most system
resources. If that is not the one you want to stop, you can enter a different PID.

What is this _sigterm_ stuff, you ask? _Signals_ are inherited from Unix, and are very
crufty, with numerous variations added over the years that you can learn all about in
_man 2 signal_, such as _SIGHUP_, _SIGINT_, _SIGQUIT_, and a host of others.

The two that are most pertinent to users and system administrators are _SIGKILL_ and
_SIGTERM_ . Always try _SIGTERM_ first, because it stops a process gracefully, ensuring
that any child processes are handed off to _INIT_ and not orphaned, and parent
processes are informed. The one downside to _SIGTERM_ is the process can elect to
ignore it.

Use _SIGKILL_ only when _SIGTERM_ is ineffective. _SIGKILL_ cannot be ignored, and it
also kills child processes, which may affect other processes. A process can be left in
limbo as a zombie process because the parent is not informed. Zombie processes are
no big deal by themselves, they just sit there not doing anything. You can see if you
have any in the header of _top_, on the right side of the Tasks line. The following exam‐
ple shows two zombies:

```
  Tasks: 249 total, 1 running, 248 sleeping, 0 stopped, 2 zombie

```

**476** **|** **Chapter 20: Troubleshooting a Linux PC**

You don’t need to do anything as the parent application should automatically clean
them up. If it doesn’t, it’s not a big deal, unless it generates a horde of zombies. That
tells you there is a problem with the application. You can’t kill zombies because they
are already dead. They use a miniscule bit of system resources, but if you want to try
getting rid of them, try sending them a _SIGCHLD_ :

```
  $ sudo kill -s SIGCHLD 1299
```

If the same process keeps using excessive system resources, review the configuration
file or settings of its program to see if there are errors, or if you can tune it to be more
efficient. Check your logfiles (Recipe 20.1) for clues.

**See Also**

 - _man 1 top_

 - _man 1 kill_

**20.9 Viewing Selected Processes in top**

**Problem**

You want to track just one or a small number of processes.

**Solution**

Start _top_ with a comma-delimited list of the processes you want to track:

```
  $ top -p 4548, 8685, 9348
  top - 10:57:39 up 44 min, 2 users, load average: 0.10, 0.11, 0.21
  Tasks:  3 total,  0 running,  3 sleeping,  0 stopped,  0 zombie
  %Cpu(s): 0.2 us, 0.2 sy, 0.0 ni, 99.6 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st
  MiB Mem : 15691.4 total, 12989.5 free,  1467.4 used,  1234.4 buff/cache
  MiB Swap: 15258.0 total, 15258.0 free,   0.0 used. 13601.1 avail Mem

  PID USER   PR NI  VIRT  RES  SHR S %CPU %MEM   TIME+ COMMAND
  2907 mysql   20  0 1775688 78584 18396 S  0.0  0.5  0:00.22 mysqld
  927 root   20  0 1569764 39072 29320 S  0.0  0.2  0:00.16 libvirtd
  822 root   20  0  11040  6384  4732 S  0.0  0.0  0:00.02 smartd
```

Now you can keep an eye on what you want to see, without having to wade through
the remaining hordes of processes. Press the equals sign key (=) to return to the com‐
plete process list.

**20.9 Viewing Selected Processes in top** **|** **477**

**See Also**

 - _man 1 top_

 - _man 1 kill_

**20.10 Escaping from a Frozen Graphical Desktop**

**Problem**

There you were, working happily, when your graphical desktop froze. The cursor
moves, but very slowly, or it does not move at all.

**Solution**

This is one of my favorite Linux features: dropping to the console from a graphical
session. Press Ctrl-Alt-F2, and you should find yourself at the plain-text console that
lies underneath your graphical session (Figure 20-5).

_Figure 20-5. The Linux console_

Log in, and now you can run some troubleshooting commands. Start with _top_ to find
the wayward process clogging your system and kill it, check log files, run other diag‐
nostics, whatever you need to do. Once you have resolved the problem, press Alt-F7
to return to your graphical desktop. The worse case is you will have to shut down or
reboot, which is better than a forced shutdown from pressing the power button.

The various Linuxes map these key combinations in different ways. Alt-F7 is tradi‐
tional for the graphical session. Fedora uses Alt-F1. It hurts nothing to try them all.

**Discussion**

Another option is to open an SSH session from another computer and try to unfreeze
your graphical desktop.

To me this is the best of all worlds, having both the console and graphical environ‐
ment available at the same time.

**478** **|** **Chapter 20: Troubleshooting a Linux PC**

A forced shutdown isn’t necessarily a disaster as it used to be, especially when you are
using a journaling filesystem such as Ext4, XFS, or Btrfs.

The standard configuration is seven consoles, F1 through F7. Each one is an inde‐
pendent login session.

Use Ctrl-Alt-F _n_ to leave a graphical session and enter the console, and when you are
in the console, use Alt-F _n_ .

**20.11 Troubleshooting Hardware**

**Problem**

You think you have failing hardware and need to know how to test it.

**Solution**

When you suspect a hardware problem, first try the recipes in this chapter about
hardware monitoring. Some system UEFI firmwares include hardware health
monitors.

If the monitors do not point you in a clear direction, shut down the machine, open
the case, clean out the dust, clean the filters if there are any, then remove and reseat
everything that can be unplugged and reconnected: power cables, SATA cables,
graphics adapters and other PCI expansion cards, memory modules, and fan connec‐
tors. Carefully reconnect everything, and pay special attention to reseating your
memory modules correctly.

**How to Not Kill Your Hardware, or Yourself**

Be careful! Ground yourself by touching something else to dis‐
charge static electricity. Wear an anti-static wrist strap, and place
your components on an anti-static mat. Unplug your machine, and
NEVER touch anything inside the case while it is plugged in.

Test the power supply with a multimeter, if you know how to do this, or try a differ‐
ent power supply. Testing with a multimeter is fairly easy, and there are plenty of
how-tos. If you have spare parts, swapping out a suspect component and trying a dif‐
ferent one can pinpoint faulty hardware.

After you are finished and everything is back together, see if the problem is corrected.
In my computer adventures a number of problems were solved by reseating the
memory modules or moving them to different slots. Note that on most motherboards
you must install RAM pairs in certain slots. Some issues related to RAM are data
corruption, incomplete boots, and odd behaviors like when you press the power

**20.11 Troubleshooting Hardware** **|** **479**

switch to start up your system, it fluctuates like the power supply is faulty, and does
not start.

Make certain that your case fans are oriented the right way. Air must be pulled into
the case, usually from the front and sides, and then evacuated out the back.

There are quite a few hardware testers in Linux-land. Some vendors provide their
own hardware and system testers; for example, Lenovo ThinkPads come with com‐
prehensive testers that test every component on your system.

[GtkStressTesting is a good utility for stress testing CPU, memory, and other compo‐](https://oreil.ly/7gEST)
nents, and it extracts detailed motherboard information. Follow the instructions in
the Setup Guide to install it on your system. It includes monitors similar to
_lm-sensors_ .

One feature it does not have is I/O monitoring, which you need to spot performance
bottlenecks. For this, use _iotop_, which monitors disk performance in a _top_ -like
interface.

**Discussion**

It can be difficult to determine whether a problem is software or hardware. Be sys‐
tematic and thorough, as hurrying takes longer. Use the available help for your Linux
distribution, as there are always issues particular to each distro. Always read the
release notes.

**See Also**

 - _man 8 iotop_

 - [GtkStressTesting](https://oreil.ly/7gEST)

 - The documentation for your hardware components

 - Your Linux distribution’s documentation, forums, wikis, and release notes

 - Chapter 10

 - Recipe 20.6

**480** **|** **Chapter 20: Troubleshooting a Linux PC**

**<u>CHAPTER 21</u>**
#### **Troubleshooting Networks**

Figuring out networking problems is just like any troubleshooting. Know your net‐
work, know how to use basic tools well, and be patient and systematic.

In this chapter we learn how to use _ping_, FPing, Nmap, _httping_, _arping_, and _mtr_ to test
connectivity, map networks, find rogue services, test website performance, find dupli‐
cate IP addresses, and find routing bottlenecks.

**Diagnostic Hardware**

If you find yourself stuck with mysterious unlabeled Ethernet and phone cabling, get
yourself an Ethernet/telephone cable test and tone tracker. There are many that cost
under $100. These come in two pieces: one emitter and one receiver. This goes fast
with two people, one at each end of a cable. When you find both ends of a cable, label
it and move on. You can do it alone, but it is faster with two people.

Multimeters are useful for a lot of jobs, such as finding shorts and opens, testing for
continuity and attenuation, determining whether a wire is terminated correctly,
testing electric outlets, and testing computer power supplies and motherboards.
[Adafruit is a great site to find excellent tutorials on using a multimeter and learning](https://adafruit.com)
electronics.

Keep a few spare parts, if you can. Sometimes it is faster to swap out a network inter‐
face, cable, or switch to find a defective piece of hardware.

**481**

**21.1 Testing Connectivity with ping**

**Problem**

Some services or hosts on your network are not accessible or have intermittent fail‐
ures. You want to figure out if it is a hardware problem, a problem with name serv‐
ices, routing, or something else.

**Solution**

When you are debugging network problems, start close, and systematically work
from closer to farther. This means physical distance and how many routers there are
to cross. Start within your local LAN segment. Then proceed to your next LAN seg‐
ment, if you have more than one, crossing a single router. Then to the next one two
routers away, and so on.

Start with good old _ping_ to test connectivity. First, ping _localhost_ :

```
  $ ping localhost
  PING localhost (127.0.0.1) 56(84) bytes of data.
  64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.065 ms
  64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.035 ms
```

Stop _ping_ by pressing Ctrl-C. Pinging _localhost_ first confirms that your network inter‐
face is up and operating. If you see “connect: Network is unreachable,” there is a prob‐
lem with your network interface. Keep some spare USB network interfaces on hand
to quickly learn if you have a defective interface.

Once you have your network interface sorted, ping your hostname to test name reso‐
lution, and tell _ping_ to stop after three pings:

```
  $ ping -c 3 client4
  PING client4 (192.168.1.97) 56(84) bytes of data.
  64 bytes from client4 (192.168.1.97): icmp_seq=1 ttl=64 time=0.087 ms
  64 bytes from client4 (192.168.1.97): icmp_seq=2 ttl=64 time=0.059 ms
  64 bytes from client4 (192.168.1.97): icmp_seq=3 ttl=64 time=0.061 ms

  --- client4 ping statistics --  3 packets transmitted, 3 received, 0% packet loss, time 2046ms
  rtt min/avg/max/mdev = 0.059/0.069/0.087/0.012 ms
```

If it returns the correct IP address, your name resolution is set up correctly. If it
returns a localhost address, like 127.0.1.1, or “Name or service not known,” some‐
thing is haywire with your DNS configuration.

When your local DNS is fixed, ping one of your network hosts by hostname. If _ping_
fails with “Destination Host Unreachable” try pinging its IP address. If that succeeds,
check your DNS. If that fails with the same message, your hostname and address are
incorrect, or the host is down.

**482** **|** **Chapter 21: Troubleshooting Networks**

If you cannot reach any external IP addresses, your network interface is probably
healthy and the problem is upstream: your Ethernet cable, wireless access point,
or switch. “Network is unreachable” means your machine is not connected to the
network.

When you’re hunting down the source of intermittent outages, set _ping_ to run for a
length of time, like 500 pings, spaced 2 seconds apart, so you don’t overwhelm the
host or your network, and output the results to a text file. The following example
appends added information to the file, so you can stop and restart:

```
  $ ping -c 500 -i 2 server2 >> server2-ping.txt
```

Or, use _tee_ to see the output and record it in a file:

```
  $ ping -c 500 -i 2 server2 | tee server2-ping.txt
```

On a multihomed host, use _ping -i interface-name_ to specify which interface to use.

**Discussion**

Don’t block _echo-request_, _echo-reply_, _time-exceeded_, or _destination-unreachable_ ping
messages. Some admins block all ping messages at their firewalls, and this is a mis‐
take because many network functions require at least these four ping messages to
operate correctly.

The _ping_ command actually pings if you use the _-a_ (audible) switch, though you will
probably have to do a bit of setup to make it work. In olden times we had PC speakers
built into computer cases, connected directly to the motherboard, and the kernel
module that activated the case speaker automatically loaded at boot. You are probably
familiar with the low-fi annoyings beeps emitted from this speaker, and perhaps you
even ran some hacks to make it play music.

Now, in these here modern times, case speakers are mostly gone, and laptops mostly
do not have a motherboard beep anymore. But most PC motherboards still support
them, and the modern beep speaker is a little thing (Figure 21-1). You will probably
have to buy one.

_Figure 21-1. Beep speaker for computer motherboard_

**21.1 Testing Connectivity with ping** **|** **483**

Once you have your beep speaker, load the _pcspkr_ kernel module, then confirm it is
loaded:

```
  $ sudo modprobe pcspkr
  $ lsmod|grep pcspkr
  pcspkr         16384 0
```

Now try it out. Drop to a plain console with Ctrl-Alt-F2, or fire up an X terminal, and
use the _echo_ command to play the ASCII bell character. All examples are the same
thing, different representations of the ASCII character code 7:

```
  $ echo -e "\a"
  $ tput bel
  $ echo -e '\007'
```

Or press Ctrl-G.

If you hear nothing in your graphical terminal, check its settings to enable sounds.
_xfce4-terminal_ and _gnome-terminal_ both play the ASCII bell. _Konsole_ supports using
your choice of sound files for notifications, but it does not support the beep speaker.

**See Also**

 - _man 8 ping_

 - [IANA list of ICMP parameters](https://oreil.ly/pWYWE)

**21.2 Profiling Your Network with fping and nmap**

**Problem**

You want to generate a list of all hosts and IP addresses on your network and probe
for MAC addresses and open ports.

**Solution**

Use _fping_ and _nmap_ to probe your LAN, and record the results.

_fping_ pings all the addresses in a range in sequence. This example pings a subnet
once, reports which hosts are alive, queries DNS for the hostnames, and prints a
summary:

```
  $ fping -c1 -gAds 192.168.1.0/24 2>1 | egrep -v "ICMP|xmt" >> fping.txt
  client1.net (192.168.1.15)   : [0], 84 bytes, 3.12 ms (3.12 avg, 0% loss)
  server2.net (192.168.1.91)   : [0], 84 bytes, 5.34 ms (5.34 avg, 0% loss)
  client4.net (192.168.1.97)   : [0], 84 bytes, 0.03 ms (0.03 avg, 0% loss)

  254 targets
  3 alive

```

**484** **|** **Chapter 21: Troubleshooting Networks**

```
  251 unreachable
  0 unknown addresses

  251 timeouts (waiting for response)

  0.03 ms (min round trip time)
  2.83 ms (avg round trip time)
  5.34 ms (max round trip time)
  3.575 sec (elapsed real time)
```

To see the unfiltered output, omit the _2>1 | egrep -v “ICMP|xmt”_ part. Any offline
machines will not be found, so you could run this at different times to try to capture
everything. _>> fping.txt_ appends the new results for each run.

This _nmap_ example performs a similar task, with less verbose output:

```
  $ sudo nmap -sn 192.168.1.0/24 > nmap.txt
  Starting Nmap 7.70 ( https://nmap.org ) at 2021-03-31 18:30 PDT
  Nmap scan report for client1.net (192.168.1.15)
  Host is up (0.0052s latency).
  MAC Address: 44:A5:6E:D7:8F:B9 (Unknown)
  Nmap scan report for BRW7440BBC7CA75.net (192.168.1.39)
  Host is up (1.0s latency).
  MAC Address: 74:40:BB:C7:CA:75 (Unknown)
  Nmap scan report for client4.net (192.168.1.97)
  Host is up (0.47s latency).
  MAC Address: 9C:EF:D5:FE:8F:20 (Panda Wireless)
  Nmap scan report for server2.net (192.168.1.91)
  Host is up.
  Nmap done: 256 IP addresses (6 hosts up) scanned in 15.19 seconds
```

That is a rather indigestible lump, so insert a newline before each host and store the
output in a new file:

```
  $ awk '/Nmap/{print ""}1' nmap.txt > nmap2.txt
```

Now you have nice groupings:

```
  Nmap scan report for client1.net (192.168.1.15)
  Host is up (0.0052s latency).
  MAC Address: 44:A5:6E:D7:8F:B9 (Unknown)

  Nmap scan report for BRW7440BBC7CA75.net (192.168.1.39)
  Host is up (1.0s latency).
  MAC Address: 74:40:BB:C7:CA:75 (Unknown)

  Nmap scan report for client4.net (192.168.1.97)
  Host is up (0.47s latency).
  MAC Address: 9C:EF:D5:FE:8F:20 (Panda Wireless)

  Nmap scan report for server2.net (192.168.1.91)
  Host is up.

  Nmap done: 256 IP addresses (6 hosts up) scanned in 15.19 seconds

```

**21.2 Profiling Your Network with fping and nmap** **|** **485**

Probe the hosts on your network for open ports:

```
  $ sudo nmap -sS  192.168.1.*
  Starting Nmap 7.70 ( https://nmap.org ) at 2021-03-31 19:36 PDT
  Nmap scan report for client2.net (192.168.1.15)
  Host is up (0.027s latency).
  Not shown: 997 closed ports
  PORT   STATE  SERVICE
  53/tcp  open   domain
  80/tcp  open   http
  MAC Address: 44:A5:6E:D7:8F:B9 (Unknown)

  Nmap scan report for 192.168.1.39
  Host is up (0.074s latency).
  Not shown: 994 closed ports
  PORT   STATE SERVICE
  25/tcp  open smtp
  80/tcp  open http
  443/tcp open https
  515/tcp open printer
  631/tcp open ipp
  9100/tcp open jetdirect
  MAC Address: 74:40:BB:C7:CA:75 (Unknown)
  [...]
```

client2.net is running a DNS and web server. You can run the same probe from out‐
side your firewall to see if they are visible outside of your network.

The second entry is interesting because it is a network printer running a whole mob
of services. The printer documentation says they all have a purpose. The printer sup‐
ports remote administration through a web control panel, so they could be disabled,
if necessary.

Collect a list of hosts and their IP addresses:

```
  $ nmap -sn 192.168.43.0/24 | grep 'Nmap scan report for' |cut -d' ' -f5,6
  server2 (192.168.43.15)
  dns-server (192.168.43.74)
  client4 (192.168.43.14)
```

**Discussion**

_nmap_ has numerous options for probing networks. Do not probe other people’s net‐
works without permission because it could be seen as a hostile act, probing for vul‐
nerabilities.

Running a port scan takes some time, but it is a good idea to do this regularly to see
what is happening on your network. It is basic security to run only necessary services
and to disable everything else.

**486** **|** **Chapter 21: Troubleshooting Networks**

**See Also**

 - _man 1 nmap_

 - _[https://nmap.org](https://nmap.org)_

 - _man 8 fping_

 - _[https://fping.org](https://fping.org)_

**21.3 Finding Duplicate IP Addresses with arping**

**Problem**

You want to search your network for duplicate IP addresses.

**Solution**

This example searches your network for 192.168.1.91 and sends four pings:

```
  $ sudo arping -I wlan2 -c 4 192.168.1.91
  ARPING 192.168.1.91
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=0 time=49.463 msec
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=1 time=458.306 msec
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=2 time=73.938 msec
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=3 time=504.482 msec

  --- 192.168.1.91 statistics --  4 packets transmitted, 4 packets received,  0% unanswered (0 extra)
  rtt min/avg/max/std-dev = 49.463/271.547/504.482/210.659 ms
```

All of the MAC addresses are the same, so it found no duplicates. This is an example
of _arping_ finding duplicate IP addresses:

```
  $ sudo arping -I wlan2 -c 4 192.168.1.91
  ARPING 192.168.1.91
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=0 time=49.463 msec
  42 bytes from 2F:EF:D5:FE:8F:20 (192.168.1.91): index=1 time=458.306 msec
  42 bytes from 9c:ef:d5:fe:01:7c (192.168.1.91): index=2 time=73.938 msec
  42 bytes from 2F:EF:D5:FE:8F:20 (192.168.1.91): index=3 time=504.482 msec
  [...]

  --- 192.168.1.91 statistics --  4 packets transmitted, 4 packets received,  0% unanswered (0 extra)
  rtt min/avg/max/std-dev = 49.463/271.547/504.482/210.659 ms
```

Use _nmap_ to identify the two machines with the same IP address:

```
  $ nmap -sn 192.168.43.0/24 | grep 'Nmap scan report for' |cut -d' ' -f5,6

```

**21.3 Finding Duplicate IP Addresses with arping** **|** **487**

**Discussion**

_arp_ is the Address Resolution Protocol, matching IP addresses to MAC addresses.

An advantage of using DHCP to dynamically assign IP addresses is less risk of creat‐
ing duplicates than setting static IP addresses manually. You can assign static
addresses with DHCP; see Chapter 16.

_arping_ is useful to see if a host is up when _ping_ does not find it. Some folks like to
block _ping_, which is not a good thing to do because it is essential to network function‐
ality. _arping_ cannot be blocked without disabling the ability for network hosts to com‐
municate with each other. _arp_, the Address Resolution Protocol, maintains a table of
MAC addresses. When a network host sends a packet to another host, _arp_ matches
the IP address to the MAC address, and then the packet can be delivered.

You can see what it looks like when _arp_ probes your network to update its address
table, with a packet sniffer like _tcpdump_ :

```
  $ sudo tcpdump -pi eth1 arp
  listening on eth1, link-type EN1000MB (Ethernet), capture size 262144 bytes
  21:19:36.921293 ARP, Request who-has client4.net tell m1login.net, length 28
  21:19:36.921309 ARP, Reply client4.net is-at 9c:ef:d5:fe:8f:20
```

**See Also**

 - Chapter 16

 - _man 8 arping_

**21.4 Testing HTTP Throughput and Latency with httping**

**Problem**

You want to test a website that you host to see if it loads in a reasonable length of
time.

**Solution**

_httping_ measures HTTP server throughput and latency. Its simplest invocation tests
latency:

```
  $ httping -c4 -l -g www.oreilly.com
  PING www.oreilly.com:443 (/):
  connected to 184.86.29.153:443 (453 bytes), seq=0 time=292.25 ms
  connected to 184.86.29.153:443 (453 bytes), seq=1 time=726.35 ms
  connected to 184.86.29.153:443 (452 bytes), seq=2 time=629.11 ms
  connected to 184.86.29.153:443 (453 bytes), seq=3 time=529.95 ms
  --- https://www.oreilly.com/ ping statistics --
```

**488** **|** **Chapter 21: Troubleshooting Networks**

```
  4 connects, 4 ok, 0.00% failed, time 6179ms
  round-trip min/avg/max = 292.2/544.4/726.3 ms
```

This doesn’t tell you how long it takes pages to load, only how long it takes the server,
in milliseconds, to respond to a HEAD request, which fetches only the page headers
without the content. A GET ( _-G_ ) request fetches the whole page:

```
  $ httping -c4 -l -Gg www.oreilly.com
  PING www.oreilly.com:443 (/):
  connected to 104.112.183.230:443 (453 bytes), seq=0 time=2125.72 ms
  connected to 104.112.183.230:443 (453 bytes), seq=1 time=701.94 ms
  connected to 104.112.183.230:443 (453 bytes), seq=2 time=470.66 ms
  connected to 104.112.183.230:443 (453 bytes), seq=3 time=433.11 ms
  --- https://www.oreilly.com/ ping statistics --  4 connects, 4 ok, 0.00% failed, time 7733ms
  round-trip min/avg/max = 433.1/932.9/2125.7 ms
```

Add the _-r_ switch to minimize DNS latency by resolving the hostname just once:

```
  $ httping -c4 -l -rGg www.oreilly.com
  PING www.oreilly.com:443 (/):
  connected to 23.10.2.218:443 (452 bytes), seq=0 time=961.29 ms
  connected to 23.10.2.218:443 (452 bytes), seq=1 time=1091.16 ms
  connected to 23.10.2.218:443 (452 bytes), seq=2 time=925.46 ms
  connected to 23.10.2.218:443 (452 bytes), seq=3 time=913.26 ms
  --- https://www.oreilly.com/ ping statistics --  4 connects, 4 ok, 0.00% failed, time 7894ms
  round-trip min/avg/max = 913.3/972.8/1091.2 ms
```

If minimizing DNS latency makes a large difference, then you need to take a look at
your nameservers.

Test an alternate port, such as 8080, by appending it to the URL:

```
  $ httping -c4 -l -rGg www.oreilly.com:8080
```

Use the _-s_ switch to display return codes, such as 200 OK, which indicates a successful
page load:

```
  $ httping -c4 -l -srGg www.oreilly.com
  PING www.oreilly.com:443 (/):
  connected to 23.10.2.218:443 (452 bytes), seq=0 time=920.88 ms 200 OK
  connected to 23.10.2.218:443 (452 bytes), seq=1 time=857.60 ms 200 OK
  connected to 23.10.2.218:443 (452 bytes), seq=2 time=1246.69 ms 200 OK
  connected to 23.10.2.218:443 (452 bytes), seq=3 time=1134.91 ms 200 OK
  --- https://www.oreilly.com/ ping statistics --  4 connects, 4 ok, 0.00% failed, time 8249ms
  round-trip min/avg/max = 857.6/1040.0/1246.7 ms

```

**21.4 Testing HTTP Throughput and Latency with httping** **|** **489**

**Discussion**

Run multiple tests at different times of day to gather data that is representative of
what your users are experiencing.

_httping_ is not a super-sophisticated tester that digs deeply into your site to identify
bottlenecks. It is a quick, simple tool to give you an idea of your overall site perfor‐
mance, and to tell you if you need to dig deeper to diagnose performance problems.

**See Also**

 - [HTTP return codes](https://oreil.ly/pMvFV)

 - _man 1 httping_

 - [httping](https://oreil.ly/2ts3n)

**21.5 Using mtr to Find Troublesome Routers**

**Problem**

There is a site you are trying to access, and it is very slow or unreachable.

**Solution**

Use _mtr_ (My Traceroute) to see where your packets are going astray. This works bet‐
ter on networks that you control, because the internet is vast and routes change, but
when you are having trouble reaching a site it will provide useful information.

Let’s see what wandering path takes us to _carlaschroder.com_ :

```
  $ mtr -wo LSRABW carlaschroder.com
  Start: 2021-03-31T09:54:17-0700
  HOST: client4                Loss%  Snt  Rcv  Avg Best Wrst
  1.|-- m1login.net              0.0%  10  10 55.5  1.2 199.6
  2.|-- 172.26.96.169             0.0%  10  10 92.3 29.0 243.6
  3.|-- 172.18.84.60              0.0%  10  10 84.5 29.3 220.3
  4.|-- 12.249.2.25              0.0%  10  10 80.7 36.4 215.5
  5.|-- 12.122.146.97             0.0%  10  10 65.6 34.8 156.6
  6.|-- 12.122.111.33             0.0%  10  10 49.3 35.5 97.6
  7.|-- cr2.st6wa.ip.att.net          0.0%  10  10 46.7 35.9 64.0
  8.|-- 12.122.111.109             0.0%  10  10 57.9 31.4 215.4
  9.|-- 12.122.111.81             0.0%  10  10 72.3 27.6 231.4
  10.|-- 12.249.133.242             0.0%  10  10 101.2 31.7 263.1
  11.|-- ae6.cbs01.wb01.sea02.networklayer.com 0.0%  10  10 93.7 31.6 202.7
  12.|-- fc.11.6132.ip4.static.sl-reverse.com  0.0%  10  10 106.0 86.1 171.2
  13.|-- ae1.cbs02.eq01.dal03.networklayer.com 60.0%  10   4 102.0 86.5 115.8
  14.|-- ae0.dar01.dal13.networklayer.com    0.0%  10  10 103.7 80.3 230.8
  15.|-- 85.76.30a9.ip4.static.sl-reverse.com  0.0%  10  10 114.8 82.8 305.7

```

**490** **|** **Chapter 21: Troubleshooting Networks**

```
  16.|-- a1.76.30a9.ip4.static.sl-reverse.com  0.0%  10  10 122.7 83.7 278.4
  17.|-- hs17.name.tools            0.0%  10  10 145.9 74.9 277.2
```

m1login.net is my network’s internet gateway router. After that it is all the wild inter‐
net. Hop 13 could be a chokepoint, with 60% packet loss. Hop 13 could be part of a
load-balancing cluster; note that hop 11 and hop 14 have the same domain name. If it
is part of a cluster then the packet loss is not significant.

Ping the last hop, hs17.name.tools. The following example looks like everything is
working fine:

```
  $ ping -c 3 hs17.name.tools
  PING hs17.name.tools (169.61.1.230) 56(84) bytes of data.
  64 bytes from hs17.name.tools (169.61.1.230): icmp_seq=1 ttl=46 time=319 ms
  64 bytes from hs17.name.tools (169.61.1.230): icmp_seq=2 ttl=46 time=168 ms
  64 bytes from hs17.name.tools (169.61.1.230): icmp_seq=3 ttl=46 time=166 ms
  [...]
```

If _mtr_ reveals a problem, use _whois_ to look up the domain owner and their contact
information:

```
  $ whois -H networklayer.com
```

_whois_ also works for IP addresses. The _-H_ switch disables the annoying legalese.

Capture _mtr_ output in a file, with the date and time at the end of each entry:

```
  $ mtr -r -c25 oreilly.com >> mtr.txt && date >> mtr.txt
```

Collect data over time by creating a cron job (Recipe 3.7) to run the preceding _mtr_
once per hour, and let it run for a day or two. Don’t forget to turn it off.

**Discussion**

_mtr -wo LSRABW_ limits the number of columns to make the example fit better on
this page. _mtr -w_ is wide format for reports.

Save your records in case you need to report a problem; the _whois_ examples show
how to find who to contact.

_mtr_ generates a lot of traffic, so take care to not run it too frequently.

**See Also**

 - _man 8 mtr_

**21.5 Using mtr to Find Troublesome Routers** **|** **491**

**<u>APPENDIX</u>**
#### **Software Management Cheatsheets**

Software on Linux comes in _packages_ . These packages contain all the files that belong
to a particular application, such as a web browser, word processor, and games. Linux
systems use shared libraries, which are shared by multiple applications. Most pack‐
ages on Linux are not self-contained, but depend on shared files.

The graphical software manager on most Linux distributions is GNOME-Software,
also called Software (Figure A-1). Software is well organized, with categories and
good search capabilities.

_Figure A-1. GNOME-Software_

**493**

**Package Management Commands**

Every Linux distribution uses three types of software management commands:

 - A package manager, which manages only single packages. Fedora and openSUSE
use the _rpm_ package manager, Ubuntu uses _dpkg_ .

 - A dependency-resolving package manager. Fedora uses _dnf_, openSUSE uses
_zypper_, and Ubuntu has _apt_ . Dependency-resolving package managers ensure
that any dependencies for a particular package are automatically resolved. For
example, the gedit text editor has a long list of dependencies, as this example for
_apt_ illustrates:
```
    $  apt depends gedit
    gedit
    Depends: gedit-common (<< 3.37)
    Depends: gedit-common (>= 3.36)
    Depends: gir1.2-glib-2.0
    Depends: gir1.2-gtk-3.0 (>= 3.21.3)
    Depends: gir1.2-gtksource-4
    Depends: gir1.2-pango-1.0
    Depends: gir1.2-peas-1.0
    Depends: gsettings-desktop-schemas
    Depends: iso-codes
    [...]
```

Managing dependencies manually is difficult; dependency-resolving package
managers make life many times easier for Linux users.

 - Commands to manage groups of related packages, such as a graphical desktop,
sound and video, or server stacks. openSUSE calls these _patterns_ . Fedora calls
them package groups. Ubuntu calls them _tasks_ . The following example shows
some openSUSE patterns:

```
  $ zypper search --type pattern
  S | Name         | Summary            | Type
  ---+----------------------+--------------------------------+-  [...]
  | mail_server     | Mail and News Server      | pattern
  | mate         | MATE Desktop Environment    | pattern
  i+ | multimedia      | Multimedia           | pattern
  | network_admin    | Network Administration     | pattern
  | non_oss       | Misc. Proprietary Packages   | pattern
  | office        | Office Software        | pattern
  | print_server     | Print Server          | pattern
  [...]

```

**494** **|** **Appendix: Software Management Cheatsheets**

Software packages are distributed from _repositories_, public servers that we download
packages from. You can browse them online:

 - [Fedora Repositories](https://oreil.ly/nLDaM)

 - [openSUSE Repositories](https://oreil.ly/H8clz)

 - [Ubuntu Packages Search](https://oreil.ly/BZw5d)

Every Linux distribution has official repositories, and then there is a whole world of
third-party repositories. This appendix covers the basic commands for managing
software and repository management on your Linux system.

**Managing Software on Ubuntu**

In this book, Ubuntu Linux stands in for a whole family of Debian-based distribu‐
tions. Debian was first, then came hundreds of derivatives. The major Debian off‐
spring use the same package management system, and the commands in this appen‐
dix should work the same way on all of them.

The three software management commands in this appendix are _dpkg_, _apt_, and
_tasksel_ .

**Using add-apt to Install and Remove Repositories**

When you add a software repository, you need the code name of your Ubuntu
release. Get it with the following command:

```
  $ lsb_release -sc
  focal
```

You need the exact URL of the repository, which should be provided by the reposi‐
tory maintainers:

```
  $ sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ focal \
  universe multiverse"
```

Remove a repository:

```
  $ sudo add-apt-repository -r "deb http://us.archive.ubuntu.com/ubuntu/ focal \
  universe multiverse"
```

When you install or remove a repository, update your package cache:

```
  $ sudo apt update
```

Run this command regularly to download repository updates, then install the
updates:

```
  $ sudo apt upgrade

```

**Software Management Cheatsheets** **|** **495**

**Using dpkg to Install, Remove, and Inspect Packages**

Remember from “Package Management Commands” on page 494 that _dpkg_ only
operates on single packages and does not resolve dependencies.

Install a package:

```
  $ sudo dpkg -i packagename
```

Remove a package (does not remove configuration files):

```
  $ sudo dpkg -r packagename
```

Remove a package and its configuration files:

```
  $ sudo dpkg --purge packagename
```

List the contents of a package:

```
  $ dpkg -L packagename
```

List all installed packages:

```
  $ dpkg-query --listdpkg
```

**Using apt to Search, Inspect, Install, and Remove Packages**

_apt_ is a dependency-resolving package manager, your everyday software manager
command.

Search for a package:

```
  $ apt search packagename
```

Limit the search to package names that include your search term:

```
  $ apt search packagename --names-only
```

Get detailed information on a package:

```
  $ apt show packagename
```

Install a package:

```
  $ sudo apt install packagename
```

Remove a package (does not remove configuration files):

```
  $ sudo apt remove packagename
```

Remove a package and its configuration files:

```
  $ sudo apt remove purge packagename

```

**496** **|** **Appendix: Software Management Cheatsheets**

**Using tasksel**

_tasksel_ manages _tasks_, which are package groups.

List available tasks:

```
  $ tasksel --list-tasks
```

Install a task:

```
  $ sudo tasksel install task
```

Remove a task:

```
  $ sudo tasksel remove task
```

**Managing Software on Fedora**

In this book, Fedora Linux represents a family of distributions based on Red Hat
Linux. Red Hat, CentOS, Scientific Linux, Oracle Linux, and many others use the
same package management system, and these commands should work on all of them.

The two software management commands in this chapter are _rpm_ and _dnf_ .

**Using dnf to Manage Repositories**

List all installed repositories, enabled and disabled:

```
  $ dnf repolist --all
```

List enabled repositories:

```
  $ dnf repolist --enabled
```

Show detailed information on enabled repositories:

```
  $ dnf repolist --enabled
```

Add a repository:

```
  $ sudo dnf config-manager --add-repo /etc/yum.repos.d/fedora_extras.repo
```

Enable the repository:

```
  $ sudo dnf config-manager --set-enabled fedora-extras
```

Disable the repository:

```
  $ sudo dnf config-manager --set-disabled fedora-extras
```

**Using dnf to Manage Software**

Search for a package:

```
  $ dnf search packagename

```

**Software Management Cheatsheets** **|** **497**

Install a package:

```
  $ sudo dnf install packagename
```

Remove a package:

```
  $ sudo dnf remove packagename
```

Get information about a package:

```
  $ dnf info packagename
```

Install updates:

```
  $ sudo dnf upgrade
```

Get a list of package groups:

```
  $ dnf grouplist
```

Install a package group:

```
  $ sudo dnf groupinstall "package-group"
```

Remove a package group:

```
  $ sudo dnf groupremove "package-group"

```

**Using rpm to Install and Remove Packages**

Install a package:

```
  $ sudo rpm -i package
```

Upgrade a package:

```
  $ sudo rpm -U package
```

Remove a package:

```
  $ sudo rpm -e package

```

**Using rpm to Get Information About Packages**

List all files in an installed _rpm_ :

```
  $ rpm -ql package
```

Get complete information about an installed package:

```
  $ rpm -qi package
```

See the changelog for a package:

```
  $ rpm -q --changes package

```

**498** **|** **Appendix: Software Management Cheatsheets**

**Managing Software on openSUSE**

openSUSE uses the RPM package format, like Fedora, but has a different
dependency-resolving package manager, _zypper_ .

**Using zypper to Manage Repositories**

List all installed repositories:

```
  $ zypper repos
```

List installed repositories and show their URLs:

```
  $ zypper repos -d
```

Enable a repository:

```
  $ sudo zypper modifyrepo -e repo
```

Disable a repository:

```
  $ sudo zypper modifyrepo -d repo
```

Add a new repository:

```
  $ sudo zypper adderepo -name " MyNewRepoName" \
  http://download.opensuse.org/distribution/leap/15.3/repo/oss/
```

Remove a repository:

```
  $ sudo zypper removerepo MyNewRepoName
```

Download repository updates:

```
  $ sudo zypper refresh
```

**Using zypper to Manage Software**

Update the system (run _sudo zypper refresh_ first):

```
  $ sudo zypper update
```

Search for a package (inexact search):

```
  $ zypper search packagename
```

Search for a package (exact search):

```
  $ zypper search -x packagename
```

Install a package:

```
  $ sudo zypper install packagename
```

Remove a package:

```
  $ sudo zypper remove packagename

```

**Software Management Cheatsheets** **|** **499**

List all software patterns:

```
  $ sudo zypper -t patterns
```

Install a pattern:

```
  $ sudo zypper -t pattern pattern-name

```

**500** **|** **Appendix: Software Management Cheatsheets**

#### **Index**

**Symbols**
/ (root), partition for, 21
/ (slash), in copying directories, 167
/boot, partition for, 21, 186
/boot/grub/, 43, 161
/dev

backups, 161
mountpoints in, 252
subdirectories in, 443
/opt, backups, 161
/proc, 82-83, 161
/proc/filesystems, 246
/root, backups, 161
/srv, backups, 161
/sys, 161
/tmp

backups, 161
partition for, 21, 186
/usr/share/zoneinfo, 405
/var

/mnt

backups, 161
disk names, 186
/etc

backups, 161
directory permissions, 132
restoring, 163
/etc/default/grub

options, 44-48
purpose of, 43
/etc/fstab, 162, 253-255
/etc/group, 99
/etc/grub.d/, 43
/etc/hosts file

on Dnsmasq servers, 371
name resolution with, 368-370
purpose of, 367
testing/blocking sites, 371-372
/etc/inittab, 67
/etc/localtime, 405
/etc/passwd, 99
/home

backups, 161
partition for, 21, 186
/var/log, 458
@ (at sign), parameterized unit files, 315
~ (tilde), for /home directory, 139, 167

**A**
absolute filepaths, 136-137
ACPI (Advanced Configuration and Power

Interface), 74
add-apt command, 495
addgroup command, 100, 115-116
Address Resolution Protocol (ARP), 488
adduser command, 100

human users, creating, 113-114
system users, creating, 114-115
advertising services over DHCP, 383-384
AGP (Accelerated Graphics Port), 230
aliasing commands, 124

backups, 161
partition for, 21, 186
purpose of, 99
tilde (~) shortcut, 139, 167
/media

backups, 162
mountpoints in, 252

**501**

allowing ports, 343-344
apt command, 496
Arch Linux, 431
ARP (Address Resolution Protocol), 488
arping command, 487-488
at sign (@), parameterized unit files, 315
attached journals (Ext4), finding, 259-260
authentication

devices for, 160
importance of, 1
with rsync command

OpenSSH

customizing Bash prompt, 292-293
encryption algorithms, 273, 294-295
host key generation, 276
key fingerprints, 281
multiple public keys, 284-285
open session and run command, 290
passphrase changes, 285-286
password authentication, 279-281
private key management with Keychain,

176
Bash prompt, customizing, 292-293
batch ownership, changing, 152-153
batch permissions, 150-151
batches of files, creating, 134-136
beep speakers, 483-484
binding zones (firewalld) to network interfaces,

automatic, 170
bandwidth limitations, 176
excluding files, 170-171, 174-176
including files, 172-174
local backups, 166-168
securing with SSH, 168-169
with rsyncd servers

access control, 180-182
building server, 177-180
MOTD files, 182-183
selecting files, 161-162
bandwidth limitations with rsync command,

286-288
public key authentication, 282-283
purpose of, 273
server configuration, 276-278
server installation, 275
sshfs command, 291-292
syntax checking, 279
tunneling X sessions, 288-290
types of, 274
on rsyncd servers, 180-182
of sudo command, 128-129
authoritative name servers, 368
automated shutdowns (see scheduled shut‐

336
BIOS/UEFI setup

downs)
automated startups (see scheduled startups)
automatic backups

entering, 4-6
GPT versus MBR, 187-188
scheduled startups, 71-72
Secure Boot, disabling, 3
steps in startup, 38
SystemRescue boot screens, 434-438
block devices, 12, 238
block zone (firewalld), 337
blocking

IP addresses, 345-346
ports, 343-344
sites with /etc/hosts file, 371-372
blocks, 188-190
boot screen

with rsync command, 170
with cp command, 164-165
automatic DHCP DNS entries, 386-388
automatic filesystem mounts, 253-255
awk command

filtering lspci output, 232-233
identifying kernel modules, 234

**B**
backgrounds for boot screen, customizing,

background, changing, 48-49
customizing, 38
displaying, 38, 40-41
font colors, changing, 49-52
grub rescue> prompt, 56-57
grub> prompt, 54-56
SystemRescue, 434-438
themes, 52-53
bootable CD/DVD (see DVD installation

48-49
backups

with cp command

automatic, 164-165
manual, 163

media)
booting

**502** **|** **Index**

from installation media, 2-3
to older kernels, 41-42
PXE booting, 75
Raspberry Pi into recovery mode, 420
steps in, 37-38
bootloaders, 37

chown command, 151-153
Chromebooks, displaying hardware informa‐

advantages, 398
determining usage, 392-393
as NTP client, 397-398
as NTP server, 398-399
purpose of, 391
viewing statistics, 400-401
chronyc command, 397, 400-401
chroot environments, creating, 445-446
chroot jail, 179
clients

tion, 241
chrony

(see also GRUB)
bootstrapping (see booting)
Bradley, David, 67
Broadcom SoC (system-on-a-chip), 409
Btrfs filesystems, 245, 269-271
bytes

decimal versus binary values, 190
in disk capacity, 188-190

**C**
CA (certificate authority), 298, 306
canceling timed shutdowns, 62
cd command, 137, 158
CD installation media (see DVD installation

NTP

chrony configuration, 397-398
determining, 392-393
ntpd configuration, 401-402
timesyncd configuration, 394-395
OpenSSH, 275
OpenVPN

media)
centralized user management, 100
certificate authority (CA), 298, 306
certificates, 311
changing

default EasyRSA options, 311-312
default firewalld zones, 338
default target for zones, 346
default useradd settings, 106-107
file ownership, 151-153
passphrases, 285-286
printer configuration, 364-365
running system, 205
sudo password timeout, 126
SystemRescue, preserving changes, 453-454
character devices, 12
child processes, 84
chmod command

configuring and testing, 312-314
distributing configurations, 316-319
installing, 299-300
testing Dnsmasq from, 380-381
Cog System Info Viewer, 241
colors

for boot screen fonts, changing, 49-52
transparency, 51
command modes (parted), selecting, 191
commands, aliasing, 124
Common Unix Printing System (see CUPS)
composite video on Raspberry Pi, 417-419
configuration files (GRUB)

explained, 43-44
rebuilding, 40
reinstalling, 58
writing, 44-48
configuring

batch permissions, 150-151
octal notation

chrony

for directory permissions, 142-143
for file permissions, 140-142
special modes

removing, 146
setting, 143-145, 148-150
symbolic notation for file permissions,

as NTP client, 397-398
as NTP server, 398-399
DHCP, 381-383
Dnsmasq for LAN DNS, 376-379
firewalld

backend, 332
for DNS and DHCP, 379
journal mode (Ext4), 257-259
journald, 461-462

146-148
chntpw command, 446-448
choosing (see selecting)

**Index** **|** **503**

logging in Dnsmasq, 388-389
networking, 323-324
ntpd

local printers

as NTP client, 401-402
as NTP server, 403-404
OpenSSH servers, 276-278

syntax checking, 279
OpenVPN, 312-314
smartmontools for email, 473-475
timesyncd, 394-395
wildcard domains in Dnsmasq, 389
connectivity testing

18-21, 186, 197
customizing

installing, 350-354
sharing, 359-360
naming printers, 354-355
network printers, installing, 355
printer configuration, changing, 364-365
printer drivers, 348

installing, 362-364
web interface for, 350
custom packages in Linux installs, 23-28
custom partitioning, installing Linux with,

in OpenVPN, 300-302
with ping, 482-484
cooling

hardware, 456
Raspberry Pi, 413
Coordinated Universal Time (see UTC)
copying

background, 48-49
font colors, 49-52
themes, 52-53
EasyRSA, 311-312
firewalld zones, 339-340
well-known user directories, 108-110
cwd (current working directory), 137

Bash prompt, 292-293
boot screen, 38

as backup method

automatic copying, 164-165
manual copying, 163
files, 139-140

from failing hard disk, 448-449
over network, 442-445
partitions, 218-219
user files, 121
CoW (copy-on-write) filesystems, 245
cp command, 121, 139-140

automatic backups, 164-165
manual backups, 163
purpose of, 159
CPU information, listing, 238-240
cron

passphrase management with Keychain, 287
scheduled shutdowns, 69-71
crontab command

**D**
daemons, 84
database backups, 162
date command, 405
dd command, 13-14, 413-415
dd-rescue command, 449
ddrescue command, 448-449
debugging (see troubleshooting)
default boot entry, setting, 45
default EasyRSA options, changing, 311-312
default firewalld zones

changing, 338
targets, changing, 346
default permissions, 153-154
default useradd settings, changing, 106-107
deleting

automatic backups, 164-165, 170
scheduled shutdowns, 69-71
Ctrl-Alt-Delete

configuration

in /etc/inittab file, 67
in graphical environments, 66
with systemd, 68-69
purpose of, 59
rebooting with, 66-67
CUPS (Common Unix Printing System), 347

files/directories, 137-138
filesystems

with Gparted, 210-211
with parted command, 198-199, 250-251
recovering deleted, 199, 214
user files, 121

with parted command, 250-251
while preserving partition, 213-214
groups with delgroup command, 120
partitions

driverless printing, 349, 357-359
"Forbidden" error message, 360-361

**504** **|** **Index**

users

with deluser command, 119
with userdel command, 118-119
delgroup command, 120
deluser command, 119
dependency-resolving package managers, 494
desktop environments, installing multiple, 28
dhclient command, 382
DHCP (Domain Name Configuration Proto‐

disconnecting from network, 330
disks

195-197
partitions (see partitions)
terminology, 185, 206
displaying

blocks and sectors, 188-190
displaying existing, 192-194, 207-208
naming, 186
nonbootable, creating GPT partitions on,

col)
advertising services, 383-384
automatic DNS entries, 386-388
configuring, 381-383
configuring firewalld for, 379
finding servers, 372-373
with Raspberry Pi, 428-429
static IP addresses, 385
subnet zones, 384-385
Diffie-Hellman, 309
dig command, 380-381
directories

backups (see backups)
copying/moving, 139-140
creating, 133-134
deleting, 137-138
filepaths, absolute/relative, 136-137
hiding, 157-158
ownership, changing, 151-153
permissions

boot screen, 38, 40-41
chrony statistics, 400-401
existing partitions/disks, 192-194
log files, 457-460
partitions, 207-208
processes, 477
startup messages, 79
UID/GID, 101-102
distro-hopping, 2
DistroWatch, 3, 7
dmesg command, 257, 457-458
dmz zone (firewalld), 337
dnf command, 497
DNS (Domain Name System)

in /etc, 132
default, 153-154
octal notation, 142-143
purpose of, 131
special modes, 143-145
renaming, 139-140
soft links, 154-157
well-known user, customizing, 108-110
disabled services

automatic entries for DHCP clients, 386-388
configuring Dnsmasq for, 376-379
configuring firewalld for, 379
finding servers, 372-373
with Raspberry Pi, 428-429
server types, 367-368
Dnsmasq

advertising services, 383-384
automatic DNS entries, 386-388
configuring, 381-383
static IP addresses, 385
subnet zones, 384-385
installing, 374-375
logging, 388-389
purpose of, 367-368
systemd-resolved and NetworkManager

/etc/hosts on, 371
configuring for LAN DNS, 376-379
DHCP

explained, 88
listing, 87
disabling

Ctrl-Alt-Delete, 68
firewalls, 440-441
repositories

with dnf command, 497
with zypper command, 499
Secure Boot, 3, 432
services, 92-93
user accounts, 117-118

conflicts, 375-376
testing from client machine, 380-381
wildcard domains, 389
documentation, purpose of, 455
Documents directory, customizing, 108-110
Domain Name System (see DNS)

**Index** **|** **505**

dot files, 157

restoring, 163
downloading Linux, 3, 6
Downloads directory, customizing, 108-110
dpkg command, 496
driverless printing, 349, 357-359
drivers for printers, 348

PKI creation, 306-311
with static keys, 302-304
ephemeral ports, 328
Ethernet ports, adding to Raspberry Pi, 420-424
Ethernet/telephone cable test and tone trackers,

481
excluding files from backups, 170-171, 174-176
exFAT filesystems, 246

installing, 362-364
drop zone (firewalld), 337
drop-in files, 43
du command, 157, 202
dual-booting

Linux/macOS, 2
Linux/Windows, 1, 31-33
dumpe2fs command, 259-260

creating, 266-267
exFAT FUSE utility, 246, 266
existing filesystems, listing, 248-249, 438-439
existing partitions/disks, displaying, 192-194,

207-208
Ext4 filesystems, 245

reserved space settings, 263
duplicate IP addresses, finding, 487-488
DVD installation media, creating

with K3b, 9-11
for SystemRescue, 432
with wodim, 12
Dynamic Host Configuration Protocol (see

creating, 256-257
external journals, 260-262
freeing reserved space, 262-263
journal mode, configuring, 257-259
journals, finding attached, 259-260
extended partitions, 212
extending sudo password timeout, 126
external journals (Ext4), 260-262
external zone (firewalld), 337

DHCP)
dynamic ports, 328

**E**
EasyRSA

customizing, 311, 312
installing, 304-305
PKI, creating, 306-311
easyrsa init-pki command, 309
effective IDs, 102
email reports, configuring smartmontools for,

**F**
FAT16 filesystems, 245

creating, 267-268
Virtual FAT, 249
FAT32 filesystems, 245

custom package installation, 26-28
rebuilding GRUB configuration files, 40
software management commands, 497-498
sudo authentication, 129
filepaths, absolute/relative, 136-137
files

creating, 267-268
Virtual FAT, 249
Fedora Linux

473-475
enabled services

explained, 88
listing, 87
enabling

Ctrl-Alt-Delete, 68
repositories

with dnf command, 497
with zypper command, 499
services, 92-93
SSH in SystemRescue, 440-441
encryption

backups (see backups)
blocks and sectors, 188-190
copying

with cp command, 139
with cp command, 140
from failing hard disk, 448-449
over network, 442-445
creating, 133-134

in OpenSSH, 273, 294-295
in OpenVPN

EasyRSA customization, 311-312
EasyRSA installation, 304-305

in batches, 134-136
deleting, 137-138
excluding from backups, 170-171, 174-176

**506** **|** **Index**

hiding, 157-158
including in backups, 172-174
ownership

resizing, 200-202, 249
shrinking, 202-203
64-bit, 244
XFS

changing, 151-153
types of, 131
permissions

in batches, 150-151
default, 153-154
octal notation, 140-142
purpose of, 131
special modes, 131, 143-145
symbolic notation, 146-148
types of, 131
printing to PDF, 365-366
renaming, 139-140
selecting

creating, 263
resizing, 264-265
filtering

lshw command output, 226
lspci command output, 231-233
filters for printing, 349
find command, 120-122

batch ownership, 152-153
batch permissions, 150-151
hard links, 156
finding

for backups, 161-162
for restores, 162-163
soft/hard links, 154-157
user files, finding/managing, 120-122
filesystems

Btrfs, creating, 269-271
CoW (copy-on-write), 245
creating with GParted, 220-220
deleting

with parted command, 250-251
while preserving partition, 213-214
exFAT, creating, 266-267
Ext4

configuring journal mode, 257-259
creating, 256-257
external journals, 260-262
finding attached journals, 259-260
freeing reserved space, 262-263
FAT16, creating, 267-268
FAT32, creating, 267-268
journaling, 245
labels, 205
Linux support for, 243
listing

attached journals (Ext4), 259-260
DNS and DHCP servers, 372-373
duplicate IP addresses, 487-488
supported printers, 348
user files, 120-122
findmnt command, 253
firewall-applet interface, 425
firewall-cmd command, 331, 335
firewall-config interface, 326, 425
firewalld

configuring for DNS and DHCP, 379
installing, 330-331
internet sharing with Raspberry Pi, 424-427
IP addresses, blocking, 345-346
iptables/nftables, configuring as backend,

332
NetworkManager integration, 342-343
overview, 325-326
ports, allowing/blocking, 343-344
services, listing, 335-336
version, determining, 331
zones

existing, 248-249, 438-439
supported, 246-247
managing in SystemRescue, 450
mounting, 251-253, 443

automatically, 253-255
mountpoints, 244
operational overview, 244-246
primary, 212
remote, mounting with sshfs, 291-292

changing default, 338
changing default target, 346
creating, 340-341
customizing, 339-340
listing, 332-334
predefined, 337-338
purpose of, 325-326
removing, 341
selecting/setting, 336-338
firewalls

determining active, 328-329
disabling, 440-441

**Index** **|** **507**

firewalld (see firewalld)
operational overview, 326-327
on Raspberry Pi, 424-427
font colors for boot screen, changing, 49-52
"Forbidden" error message in CUPS, 360-361
forked processes, 84
fping command, 484
free space, displaying, 207-208
freeing reserved space in Ext4 filesystems,

262-263
frozen graphical environments, troubleshoot‐

ing, 478-479
FUSE (Filesystem in Userspace), 246, 266

for software management, 493
SystemRescue, 432
troubleshooting, 478-479
Greenwich Mean Time (GMT), 392
grep command, 457-458
grounding, 479
group identification (see GID)
groupadd command, 100, 110-111
groupdel command, 100
groups

with groupadd command, 110-111
with addgroup command, 115-116
deleting, 120
numbering range, 111
password files, checking integrity, 116-117
permissions, 132
primary, 104
privileges, purpose of, 99
sudo, 124-125
supplemental, 99, 104
grpck command, 116-117
GRUB (GRand Unified Bootloader), 37

assigning users, 112
commands for, 100
creating

**G**
Gates, Bill, 67
GECOS data, 104
generated services, 88
GID (group identification)

displaying, 101-102
numbering range, 111
GMT (Greenwich Mean Time), 392
GNOME Disks, 267
GNOME-Software, 493
GParted (GNOME Partition Manager)

boot screen

filesystems

creating, 220-220
deleting while preserving partition,

background, 48-49
customizing, 38
displaying, 38, 40-41
font colors, 49-52
grub rescue> prompt, 56-57
grub> prompt, 54-56
themes, 52-53
booting, steps in, 37-38
configuration files

213-214
GPT partition table, creating, 209-210
partitions

copying, 218-219
creating, 211-212
deleting, 210-211
displaying, 207-208
moving, 216-218
recovering deleted, 214
resizing, 215-216
privileges, 206
purpose of, 205
GPT (GUID Partition Table), 186-188

creating new, 209-210
creating partitions on nonbootable disks,

explained, 43-44
rebuilding, 40
reinstalling, 58
writing, 44-48
legacy GRUB versus GRUB 2, 37
repairing from SystemRescue, 445-446
tab completion, 55
grub rescue> prompt, 56-57
grub> prompt, 54-56
GtkStressTesting, 480
GUID Partition Table (see GPT)

195-197
primary filesystems, 212
graphical environments

Ctrl-Alt-Delete configuration, 66
CUPS web interface, 350
for lm-sensors, 467-469

**H**
halt command, 59, 61

**508** **|** **Index**

options, 63-64
halting with shutdown command, 62
hard disks

listing, 237-238
monitoring, 470-473
rescuing, 448-449
hard links, 154-157
hardening OpenVPN servers, 320-323
hardware

listing hardware information, 227-228
purpose of, 224
hybrid-sleep mode, 65

diagnostic hardware for network compo‐

**I**
id command, 101-102
ifconfig command, 423
Imager, installing Raspberry Pi, 413-415
including files in backups, 172-174
indirect services, 88
init systems

nents, 481
identifying architecture, 240-241
listing

with hwinfo command, 227-228
with lsblk command, 237-238
with lscpu command, 238-240
with lshw command, 224-225
with lspci command, 228-230
with lsusb command, 235-236
preventing problems, 455-456

determining availability, 82-83
legacy, 79, 80-81
runlevel management, 95-97
systemd (see systemd)
inodes, 156-157
installation media

booting from, 2-3
creating

hard disk monitoring, 470-473
temperature monitoring, 465-467
testing, 479-480
hardware architectures

Linux, 4
Raspberry Pi, 409
hardware requirements for Raspberry Pi,

with dd, 13-14
with K3b, 9-11
for SystemRescue, 432
with UNetbootin, 7-9
with wodim, 12
ISO format, 4
installing

411-412
Hash-based Message Authentication Code

Dnsmasq, 374-375
EasyRSA, 304-305
firewalld, 330-331
Linux, 1-2

(HMAC), 309
HDMI connections, Raspberry Pi video

without, 417-419
headless Raspberry Pi, 427-428
hibernate mode, 65
hiding files/directories, 157-158
history of Raspberry Pi, 409-410
HMAC (Hash-based Message Authentication

basic installation, 15-18
custom package selection, 23-28
with custom partitioning, 18-21, 186,

Code), 309
home zone (firewalld), 338
host keys

fingerprint retrieval, 281
generating, 276
password authentication, 279-281
purpose of, 274
hostname command, 370
HTTP throughput and latency testing, 488-490
httping command, 488-490
human users (see users)
hwinfo command

197
in multiboot setup, 29-30
multiple desktop environments, 28
preserving partitions, 22-22
in Windows dual-boot setup, 31-33
local printers, 350-354
network printers, 355
OpenSSH server, 275
OpenVPN, 299-300
package groups, 498
packages

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
with zypper command, 499

**Index** **|** **509**

printer drivers, 362-364
Raspberry Pi OS, 413-417
repositories

with add-apt command, 495
with dnf command, 497
with zypper command, 499
tasks, 497
themes, 52
integrity of password files, checking, 116-117
internal zone (firewalld), 338
internet-sharing firewall on Raspberry Pi,

lexicographic ordering, 135-136
links to files/directories, 154-157
Linux

booting (see booting)
cost of, 2
downloading, 3, 6
dual-booting

basic installation, 15-18
custom package selection, 23-28
with custom partitioning, 18-21, 186,

424-427
iotop, 480
IP addresses

with macOS, 2
with Windows, 1, 31-33
hardware architectures, 4
installing, 1-2

blocking, 345-346
finding duplicate, 487-488
ip command, 370
iptables, 326, 328

configuring as firewalld backend, 332
IPv4 masquerading, 427
ISO format, 4
ISO images, mounting, 35-36
iw command, 77-78

**J**
journal mode (Ext4), configuring, 257-259
journalctl command, 458-460
journald

197
in multiboot setup, 29-30
multiple desktop environments, 28
preserving partitions, 22-22
in Windows dual-boot setup, 31-33
ISO images, mounting, 35-36
multibooting, 1, 29-30
recommendations for newbies, 3
size of distribution, 2
startup messages, displaying, 79
supported filesystems, 243
listing

existing, 248-249, 438-439
supported, 246-247
firewalld services, 335-336
firewalld zones, 332-334
hardware

filesystems

configuring, 461-462
logging server creation, 462-464
journaling filesystems, 245
journals (Ext4)

external, 260-262
finding attached, 259-260

**K**
K3b, 9-11
kernel modules for PCI devices, identifying,

234
key fingerprints, retrieving, 281
Keychain, 274, 286-288
kill command, 94-95
killing processes, 94-95, 475-477

**L**
L1/L2/L3 CPU caches, 239
labels for partitions/filesystems, 205
latency, testing, 488-490

**510** **|** **Index**

with hwinfo command, 227-228
with lsblk command, 237-238
with lscpu command, 238-240
with lshw command, 224-225
with lspci command, 228-230
with lsusb command, 235-236
package groups, 498
packages

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
repositories

with dnf command, 497
with zypper command, 499
services, 86-88
tasks, 497

live Linuxes, 1
lm-sensors

graphical display for, 467-469
temperature monitoring, 465-467
ln command, 154-157
local printers

listing, 87
masking services, 92-93
MBR (Master Boot Record), 186-188
memory, CPU caches, 239
message of the day (MOTD) files on rsyncd

servers, 182-183
mkdir command, 133
mkfs.exfat command, 266
mkfs.ext4 command, 256-257
mkfs.xfs command, 263
mkpart command, 267-268
modes (see permissions)
monitoring

installing, 350-354
sharing, 359-360
logging

in Dnsmasq, 388-389
journald configuration, 461-462
logging server creation, 462-464
purpose of, 455
severity levels for, 460
viewing log files, 457-460
logical partitions, 212
logrotate command, 389
loop devices, 35
loopback devices, 369-370
ls command, 135-136, 156
lsblk command, 13, 165

hard disks, 470-473
temperature, 465-467
monitors, collecting hardware information,

227-228
MOTD (message of the day) files on rsyncd

listing existing filesystems, 248-249, 438-439
listing hardware information, 237-238
purpose of, 224
lscpu command

servers, 182-183
mount command, 253
mounting

291-292
mountpoint command, 253
mountpoints, 244

filesystems, 251-253, 443

automatically, 253-255
ISO images, 35-36
remote filesystems with sshfs command,

listing CPU information, 238-240
purpose of, 224
lshw command

filtering output, 226
listing hardware information, 224-225
purpose of, 223
lspci command

explanation of output, 230-231
filtering output, 231-233
identifying kernel modules, 234
listing hardware information, 228-230
purpose of, 224
lsusb command

creating, 251-253
moving

listing hardware information, 235-236
purpose of, 224

files/directories, 139-140
partitions, 216-218
user files, 121
MS-DOS partition tables, 212
mtr command, 490-491
multibooting, 1, 29-30
multimeters, 481
multiple desktop environments, installing, 28
multiple Ethernet ports, adding to Raspberry

Pi, 420-424
multiple public keys in OpenSSH, 284-285
Music directory, customizing, 108-110
mv command, 121, 139-140

**M**
macOS, dual-booting, 2
magic packets, 75
mailx, 473
manual backups with cp command, 163
manual time settings, 396
masked services

explained, 88

**N**
name resolution, 367

(see also Dnsmasq)
with /etc/hosts file, 368-370
DHCP

**Index** **|** **511**

advertising services, 383-384
automatic DNS entries, 386-388
configuring, 381-383
configuring firewalld for, 379
finding servers, 372-373
static IP addresses, 385
subnet zones, 384-385
DNS

configuring as firewalld backend, 332
nm-connection-editor, 388
nmap command, 372-373, 484-486
nmcli command, 330, 374, 381, 387
nobody users, 105, 115
nonbootable disks, creating GPT partitions on,

configuring Dnsmasq for, 376-379
configuring firewalld for, 379
finding servers, 372-373
server types, 367-368
Linux utilities for, 368
with Raspberry Pi, 428-429
naming

195-197
nonbooting system, troubleshooting

grub rescue> prompt, 56-57
grub> prompt, 54-56
nonnetworked printers, sharing, 359-360
NOOBS

booting into recovery mode, 420
installing Raspberry Pi, 415-417
nslookup command, 378, 389
NTP (Network Time Protocol)

disks, 186
printers, 354-355
NAT (network address translation), 427
ncurses interface, 428
netfilter, 326
netstat command, 327
network address translation (NAT), 427
network printers, installing, 355
Network Time Protocol (see NTP)
networking

chrony configuration, 398-399
ntpd configuration, 403-404
ntpd

clients

chrony configuration, 397-398
determining, 392-393
ntpd configuration, 401-402
timesyncd configuration, 394-395
purpose of, 391
servers

configuring, 323-324
copying files over, 442-445
disconnecting, 330
OpenVPN (see OpenVPN)
ports, numbering, 327-328
resources for information, 325
troubleshooting

connectivity tests, 482-484
diagnostic hardware, 481
duplicate IP addresses, 487-488
HTTP throughput and latency testing,

chrony advantages over, 398
determining usage, 392-393
as NTP client, 401-402
as NTP server, 403-404
purpose of, 391
ntpq command, 402

for directory permissions, 142-143
for file permissions, 140-142
special modes

**O**
octal notation, 132

488-490
packet tracing, 490-491
port scanning, 484-486
NetworkManager, 326

configuring DHCP, 382-383
Dnsmasq conflicts, 375-376
firewalld integration, 342-343
firewalld zones, assigning, 338
importing .ovpn files, 318-319
name resolution, 368
nm-connection-editor, 388
OpenVPN installation, 300
nftables, 326, 328

removing, 146
setting, 143-145
OEM product key (Windows), recovering, 34
older kernels, booting to, 41-42
Open Virtual Private Network (see OpenVPN)
OpenSSH

authentication types, 274
Bash prompt, customizing, 292-293
clients, 275
enabling in SystemRescue, 440-441
encryption algorithms, 273, 294-295

**512** **|** **Index**

host keys, generating, 276
key fingerprints, 281
open session and run command, 290
password authentication, 279-281
public key authentication, 282-283

**P**
package groups, 494, 498
package managers, 494
packages, 493

multiple public keys, 284-285
passphrase changes, 285-286
private key management with Keychain,

custom selection during install, 23-28
installing

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
with zypper command, 499
listing

286-288
purpose of, 273
remote filesystems, mounting with sshfs,

291-292
rsync backups, 168-169
server configuration, 276-278
server installation, 275
syntax checking, 279
tunneling X sessions, 288-290
utilities in, 273-274
openssl command, 311
openSUSE

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
management commands

creating Btrfs filesystem, 269-271
custom package installation, 23-28
rebuilding GRUB configuration files, 40
software management commands, 499-499
sudo authentication, 129
OpenVPN

in Fedora, 497-498
in openSUSE, 499-499
terminology, 494-495
in Ubuntu, 495-497
removing

client configurations, distributing, 316-319
configuring and testing, 312-314
connectivity testing, 300-302
encryption

with apt command, 496
with dnf command, 497
with zypper command, 499
upgrading with rpm command, 498
packet tracing, 490-491
parameterized unit files, 315
parent processes, 84
parted command

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
with zypper command, 499
searching

EasyRSA customization, 311-312
EasyRSA installation, 304-305
PKI creation, 306-311
with static keys, 302-304
installing, 299-300
managing with systemctl, 315
networking, configuring, 323-324
overview, 297-298
server hardening, 320-323
openvpn command, 313
operating systems for Raspberry Pi, 408

command modes, 191
filesystems

installing, 413-417
optical disks (see DVD installation media)
.ovpn files, 316-319
ownership

creating FAT16/FAT32, 267-268
deleting, 250-251
resizing XFS, 265
partitions

creating on nonbootable disks, 195-197
deleting, 198-199
displaying existing, 192-194
recovering deleted, 199
resizing, 200-202
shrinking, 202-203
purpose of, 185

changing, 151-153
types of, 131

**Index** **|** **513**

partition tables, 186-188

patience, importance of, 456-457
patterns, 171, 494
PCI devices

creating, 209-210
MS-DOS, 212
partitions

blocks and sectors, 188-190
copying, 218-219
creating, 211-212

with Linux install, 18-21, 186, 197
in SystemRescue, 451-452
deleting

collecting hardware information, 228-230
kernel modules, 234
PCIe (PCI Express), 230
PDF, printing files to, 365-366
performance of external journals (Ext4),

with Gparted, 210-211
with parted command, 198-199, 250-251
displaying existing, 192-194, 207-208
filesystems and, 244
GPT, creating on nonbootable disks,

260-262
permissions

for directories

in /etc, 132
default, 153-154
octal notation, 142-143
purpose of, 131
special modes, 143-145
for files

195-197
labels, 205
listing, 237-238
managing in SystemRescue, 450
moving, 216-218
preserving

in Linux installs, 22-22
while deleting filesystem, 213-214
purpose of, 186
in Raspberry Pi, 415
recovering deleted, 199, 214
resizing, 200-202, 215-216, 249
shrinking, 30, 202-203, 215-216
unmounting, 190
passphrase-less authentication in OpenSSH,

in batches, 150-151
default, 153-154
octal notation, 140-142
purpose of, 131
special modes, 131, 143-145
symbolic notation, 146-148
types of, 131
of groups, 132
php command, 406
Pi (see Raspberry Pi)
Picture directory, customizing, 108-110
PID (process ID) 1, 83
ping command, 482-484
pinout command, 421, 424
PKI (public key infrastructure)

274
passphrases

changing, 285-286
managing with Keychain, 286-288
passwd command, 100

creating, 306-311
EasyRSA

disabling accounts, 117-118
privileges, 102
password authentication in OpenSSH, 274,

customizing, 311-312
installing, 304-305
Poettering, Lennart, 82
pool servers, 392, 395
port scanning, 372-373, 484-486
ports

279-281
passwords

checking file integrity, 116-117
extending sudo timeout, 126
for new users, 103
root

allowing/blocking, 343-344
numbering, 327-328
sshd, 327
postfix, 473
PostScript Printer Description (PPD) files, 349
power conditioners, 456
power management

managing, 127
resetting, 439-440
Shadow Password Suite, 100
for sudo command, 128-129
Windows, resetting, 446-448

ACPI sleep states, 74
sleep modes, 64-65

**514** **|** **Index**

poweroff command, 59, 60

options, 63-64
symlink with Ctrl-Alt-Delete, 68
PPD (PostScript Printer Description) files, 349
pre-installed Linux, 2
preserving

Psensor, 467-469
pstree command, 84-85
public key authentication in OpenSSH, 274,

282-283
multiple public keys, 284-285
passphrase changes, 285-286
private key management with Keychain,

partitions

in Linux installs, 22-22
while deleting filesystem, 213-214
SystemRescue changes, 453-454
preventing hardware problems, 455-456

286-288
public key infrastructure (see PKI)
public keys, 274, 310
public zone (firewalld), 337
pwck command, 116-117
pwd command, 137
PXE booting, 75

hard disk monitoring, 470-473
temperature monitoring, 465-467
primary filesystems, 212
primary groups, 104
printers

configuration, changing, 364-365
CUPS web interface, 350
driverless printing, 349, 357-359
drivers, 348

**R**
RAID devices, collecting hardware informa‐

advantages/disadvantages, 407-408
booting into recovery mode, 420
cooling, 413
hardware architecture, 409
hardware requirements, 411-412
history and purpose, 409-410
internet-sharing firewall on, 424-427
multiple Ethernet ports, 420-424
name resolution with, 428-429
operating systems, 408

tion, 227-228
Raspberry Pi

installing, 362-364
local

installing, 350-354
sharing, 359-360
naming, 354-355
network, installing, 355
selecting, 347-348
supported, finding, 348
printing

files to PDF, 365-366
troubleshooting, 360-361, 366
private keys, 310

passphrases

changing, 285-286
managing with Keychain, 286-288
purpose of, 274
private ports, 328
privileges, 132

installing, 413-417
products available, 409
running headless, 427-428
startup/shutdown, 410-411
tutorials, 412
video connections, 417-419
raspi-config, 427-428
real IDs, 101
real-time clock (see RTC)
reboot command, 59, 61

(see also permissions)
for GParted, 206
limitations, 132
for passwd command, 102
purpose of, 99
root (see root privileges)
processes

options, 63-64
rebooting

explained, 84-85
killing, 94-95, 475-477
viewing, 477
ps command, 83, 84, 392-393, 401

with Ctrl-Alt-Delete, 66-67
to different system states, 95-97
with halt command, 63
with poweroff command, 63
with reboot command, 63
with shutdown command, 62
rebuilding GRUB configuration files, 40
recovering

**Index** **|** **515**

deleted partitions, 199, 214
with SystemRescue (see SystemRescue)
Windows OEM product key, 34
recovery mode, booting Raspberry Pi, 420
recursive resolvers, 367
registered ports, 328
reinstalling GRUB configuration files, 58
relative filepaths, 136-137
remote access (see OpenSSH; OpenVPN)
remote filesystems, mounting with sshfs com‐

reset vector, 38
resetting

filesystems, 200-202, 249
partitions, 200-202, 215-216, 249
XFS filesystems, 264-265
resolvconf, 368
resolving Dnsmasq conflicts, 375-376
restoring files, what to restore, 162-163
restricted deletion bit, 145, 149
rich rules, 345-346
rm command, 121, 137-138
root name servers, 368
root password

root password, 439-440
Windows password, 446-448
resize command, 203
resizing

mand, 291-292
remote startups

with Wake-on-LAN, 75-77
with WoWLAN, 77-78
removing

firewalld zones, 341
package groups, 498
packages

with apt command, 496
with dnf command, 498
with dpkg command, 496
with rpm command, 498
with zypper command, 499
repositories

managing, 127
resetting, 439-440
root privileges

for shutdown commands, 60
via shell escape, 124
root users, 99

with add-apt command, 495
with zypper command, 499
special modes, 146
renaming files/directories, 139-140
repositories, 495

abilities of, 132
changing sudo authentication, 128-129
changing sudo password timeout, 126
individual sudo configurations, 127
limiting powers with sudo, 123-126
switching to, 122-123
routers, packet tracing, 490-491
RPi (see Raspberry Pi)
rpm command, 498
rsync command

disabling

with dnf command, 497
with zypper command, 499
enabling

with dnf command, 497
with zypper command, 499
installing

with add-apt command, 495
with dnf command, 497
with zypper command, 499
listing

automatic backups, 170
bandwidth limitations, 176
excluding files, 170-171, 174-176
including files, 172-174
local backups, 166-168
purpose of, 159
secure backups with SSH, 168-169
rsyncd servers

with dnf command, 497
with zypper command, 499
removing

with add-apt command, 495
with zypper command, 499
rescue command, 199
rescuing hard disks, 448-449
reserved space in Ext4 filesystems, freeing,

access control, 180-182
building, 177-180
MOTD files, 182-183
RTC (real-time clock), 392

manual settings, 396
scheduled startups with, 73-75
rtcwake command, 73-75
runlevels (SysV), 95-97

262-263

**516** **|** **Index**

running system, changing, 205

**S**
S.M.A.R.T. (Self-Monitoring Analysis and

listing, 335-336
killing, 94-95
listing, 86-88
masking/unmasking, 92-93
querying status, 89-90
starting/stopping, 91-92
states, 87-88
system users (see system users)
setgid mode, 132

enabling/disabling, 92-93
in firewalld, 326

Reporting Technology), 470-473
saved IDs, 102
scheduled shutdowns

with cron, 69-71
purpose of, 59
scheduled startups

with BIOS/UEFI setup, 71-72
purpose of, 59
with rtcwake command, 73-75
scp command, 273, 442-445
searching packages

octal notation, 143-145
symbolic notation, 148-150
setuid mode, 132

with apt command, 496
with dnf command, 497
with zypper command, 499
sectors, 188-190
Secure Boot, disabling, 3, 432
secure remote access (see OpenSSH;

octal notation, 143-145
symbolic notation, 148-150
severity levels for system logs, 460
sftp command, 273
Shadow Password Suite, 100
shared libraries, 493
sharing local printers, 359-360
shell escape, 124
shortcuts to files/directories, 154-157
shrinking

OpenVPN)
Secure Sockets Layer (SSL), 298
selecting

command modes (parted), 191
files

filesystems, 202-203
partitions, 30, 202-203, 215-216
shutdown command, 59, 61

for backups, 161-162
for restores, 162-163
firewalld zones, 336-338
printers, 347-348
sensors command, 466
sensors-detect command, 465
servers

options, 61-63
shutdown commands

Ctrl-Alt-Delete as, 68
halt command options, 63-64
legacy commands

logging, creating, 462-464
OpenSSH

purpose of, 59
symlinks for, 60
poweroff command options, 63-64
reboot command options, 63-64
root privileges, 60
scheduled shutdowns

configuring, 276-278
installing, 275
OpenVPN

configuring and testing, 312-314
hardening, 320-323
installing, 299-300
networking, configuring, 323-324
rsyncd

with cron, 69-71
purpose of, 59
shutdown command options, 61-63
systemctl, 60-61
SIGCHILD, 477
SIGKILL, 95, 476
signals, 476-477
SIGTERM, 95, 476
64-bit filesystems, 244
slash (/), in copying directories, 167
sleep modes, 64-65, 74

access control, 180-182
building, 177-180
MOTD files, 182-183
time (see time servers)
services, 84

advertising over DHCP, 383-384

**Index** **|** **517**

slots, 225
slow startups, troubleshooting, 98
sluggish systems, troubleshooting, 475-477
smartctl command, 470-471
smartd, configuring for email, 473-475
smartmontools

startup messages, displaying, 79
startx command, 432
stat command, 69, 253
static IP addresses, assigning via DHCP, 385
static keys, 302-304
static services

explained, 88
listing, 87
statistics for chrony, displaying, 400-401
sticky bits, 132

configuring for email, 473-475
hard disk monitoring, 470-473
soft links, 154-157
Software (graphical environment), 493
software management commands

in Fedora, 497-498
in openSUSE, 499-499
terminology, 494-495
in Ubuntu, 495-497
special modes

octal notation

removing, 146
setting, 143-145
symbolic notation, setting, 148-150
types of, 131, 132
SquashFS, 434
ss command, 378
SSH (see OpenSSH)
ssh command, 273, 294-295
ssh-add command, 273
ssh-agent command, 274
ssh-copy-id command, 273, 282-283
ssh-keygen command, 273, 276

octal notation, 143-145
symbolic notation, 148-150
stopping

Raspberry Pi, 410-411
services, 91-92
su command, 122-123
subnet zones (DHCP), 384-385
sudo command

authentication on individual passwords,

multiple public keys, 284
passphrase changes, 285-286
ssh-keyscan command, 273
sshd, 273

ports, 327
sshfs command, 274, 291-292, 442-445
SSL (Secure Sockets Layer), 298
starting

128-129
extending timeout, 126
individual configurations, 127
limiting powers with, 123-126
root password management, 127
superusers (see root users)
supplemental groups, 99, 104
supported filesystems, listing, 246-247
supported printers, finding, 348
suspend mode, 64
suspend-then-hibernate mode, 65
swap files, partition for, 21, 186
switching to root user, 122-123
symbolic notation, 132

for file permissions, 146-148
special modes, setting, 148-150
symlinks, 154-157

for Ctrl-Alt-Delete, 68
for shutdown commands, 60
syntax checking OpenSSH configuration, 279
system groups

Raspberry Pi, 410-411
services, 91-92
slow startups, troubleshooting, 98
SystemRescue, 432-434
startup commands

creating

remote startups

with Wake-on-LAN, 75-77
with WoWLAN, 77-78
scheduled startups

with BIOS/UEFI setup, 71-72
purpose of, 59
with rtcwake command, 73-75

with addgroup command, 115-116
with groupadd command, 110-111
numbering range, 111
system logs (see logging)
system states, rebooting to, 95-97
system users

with adduser command, 114-115

creating

**518** **|** **Index**

with useradd command, 105
purpose of, 99
systemctl command

SysV init, 79, 80

determining availability, 82-83
runlevels, 95-97

disabling firewall, 440
firewalld management, 331
OpenVPN management, 315
services

enabling/disabling, 92-93
killing, 94-95
listing, 86-88
masking/unmasking, 92-93
querying status, 89-90
starting/stopping, 91-92
shutdown with, 60-61
sleep modes, 64-65
symlinks to, 60
targets (runlevels), 95-97
systemd

**T**
tab completion in GRUB, 55
TAP devices, 298
targets (firewalld zones), changing default, 346
targets (systemd), 95-97
tasks, 494

installing, 497
listing, 497
tasksel command, 497
tee command, 226
temperature, monitoring, 465-467
testing

Ctrl-Alt-Delete configuration, 68-69
determining availability, 82-83
Dnsmasq installation, 375
journalctl, 458-460
journald

configuring, 461-462
logging server creation, 462-464
legacy init systems comparison, 80-81
purpose of, 80
shutdown commands, 60
slow startups, troubleshooting, 98
systemctl command (see systemctl com‐

connectivity testing in OpenVPN, 300-302
Dnsmasq from client machine, 380-381
hardware, 479-480
HTTP throughput and latency, 488-490
OpenVPN, 312-314
sites with /etc/hosts file, 371-372
themes for boot screen, 52-53
threads, 84
throughput, testing, 488-490
tilde (~), for /home directory, 139, 167
time servers

chrony configuration, 398-399
ntpd configuration, 403-404
strata, 391-392
time synchronization

mand)
targets, 95-97
timedatectl, 393-396, 404-405
systemd-analyze blame command, 98
systemd-resolved, 368, 375-376
SystemRescue

chrony

boot screens, 434-438
bootable device, creating, 432
files, copying over network, 442-445
filesystems/partitions

as NTP client, 397-398
as NTP server, 398-399
viewing statistics, 400-401
manual settings with timedatectl, 396
NTP clients, determining, 392-393
ntpd

creating data partition, 451-452
managing, 450
GRUB, repairing, 445-446
preserving changes, 453-454
purpose of, 431
root password, resetting, 439-440
SSH, enabling, 440-441
starting, 432-434
Windows password, resetting, 446-448

as NTP client, 401-402
as NTP server, 403-404
overview, 391-392
time zone management, 404-406
timesyncd, configuring, 394-395
time zones, 392, 404-406
timed shutdowns

canceling, 62
with shutdown command, 62
timedatectl, 393-396, 404-405
timesyncd

**Index** **|** **519**

configuring, 394-395
determining usage, 392-393
purpose of, 391
TLD (top-level domain) name servers, 368
TLS (Transport Layer Security), 298
top command, 94

killing processes, 475-477
viewing processes, 477
top-level domain (TLD) name servers, 368
touch command, 133-136
transparency of colors, 51
Transport Layer Security (TLS), 298
tree command, 133
troubleshooting

configuring journal mode, 257-259
finding block size, 261
freeing reserved space, 262-263
tunneling

with OpenVPN, 297
X sessions over SSH, 288-290
tutorials for Raspberry Pi, 412

**U**
Ubuntu software management commands,

Dnsmasq conflicts, 375-376
documentation, purpose of, 455
frozen graphical environments, 478-479
GRUB, repairing from SystemRescue,

495-497
(see also Linux)
UEFI (see BIOS/UEFI setup)
ufw (Uncomplicated Firewall), 326, 328
UID (unique identity)

displaying, 101-102
numbering range, 107, 111
umask command, 153-154
umount command, 190, 251
uname command, 240-241
UNetbootin, 7-9
unique identity (see UID)
unit files, parameterized, 315
unmasking services, 92-93
unmounting partitions, 190
upgrading packages with rpm command, 498
USB devices, listing, 235-236
USB stick installation media, creating

445-446
hardware

hard disk monitoring, 470-473
preventing problems, 455-456
temperature monitoring, 465-467
testing, 479-480
logging

journald configuration, 461-462
logging server creation, 462-464
purpose of, 455
severity levels for, 460
viewing log files, 457-460
networks

connectivity tests, 482-484
diagnostic hardware, 481
duplicate IP addresses, 487-488
HTTP throughput and latency testing,

data partition for SystemRescue, 451-452
with dd, 13-14
for SystemRescue, 432
with UNetbootin, 7-9
useradd command, 100

default settings, changing, 106-107
human users, creating, 103-104
system users, creating, 105
userdel command, 100, 118-119
usermod command, 100

488-490
packet tracing, 490-491
port scanning, 484-486
nonbooting system

grub rescue> prompt, 56-57
grub> prompt, 54-56
patience, importance of, 456-457
printing, 360-361, 366
processes, killing, 94-95
slow startups, 98
sluggish systems, 475-477
trusted zone (firewalld), 338
TUN devices, 298
tune2fs command

assigning users to groups, 112
disabling accounts, 118
users

with deluser command, 119

assigning to groups, 112
centralized management, 100
commands for, 100
creating

with adduser command, 113-114
with useradd command, 103-104
deleting

**520** **|** **Index**

with userdel command, 118-119
disabling accounts, 117-118
files, finding/managing, 120-122
groups (see groups)
nobody, 105, 115
password files, checking integrity, 116-117
privileges, purpose of, 99
root, 99

abilities of, 132
changing sudo authentication, 128-129
changing sudo password timeout, 126
individual sudo configurations, 127
limiting powers with sudo, 123-126
password management, 127
switching to, 122-123
system users

creating with adduser command,

114-115
creating with useradd, 105
purpose of, 99
types of, 99
UID/GID, displaying, 101-102
well-known user directories, customizing,

wall messages, 62
watch command, 466
website performance testing, 488-490
well-known ports, 328
well-known user directories, customizing,

**X**
X sessions, tunneling over SSH, 288-290
XFS filesystems, 245

creating, 263
resizing, 264-265

**Y**
yes command, 135

**Z**
zombie processes, 476-477
zones (firewalld)

changing default, 338
changing default target, 346
creating, 340-341
customizing, 339-340
listing, 332-334
predefined, 337-338
purpose of, 325-326
removing, 341
selecting/setting, 336-338
zypper command, 499-499

**Index** **|** **521**

108-110
whois command, 491
wildcard domains in Dnsmasq, 389
Windows

creating with adduser command,

dual-booting, 1, 31-33
OEM product key, recovering, 34
resetting password, 446-448
in virtual machines, 33
Windows Subsystem for Linux 2 (WSL 2), 33
wodim command, 12
work zone (firewalld), 338
WoWLAN (Wake-on-Wireless LAN), remote

startups with, 77-78
writing GRUB configuration files, 44-48
WSL 2 (Windows Subsystem for Linux 2), 33

108-110
UTC (Coordinated Universal Time), 74, 392,

405

**V**
vcgencmd command, 413
Ventoy, 9
video connections for Raspberry Pi, 417-419
Video directory, customizing, 108-110
viewing (see displaying)
Virtual FAT (vfat), 249
virtual machines, Windows in, 33
visudo command, 123
VPNs (virtual private networks), 297-298

(see also OpenVPN)

**W**
Wake-on-LAN, remote startups with, 75-77
Wake-on-Wireless LAN (WoWLAN), remote

startups with, 77-78
wakeonlan command, 75-77
wakeups (see startup commands)

**<u>About the Author</u>**

**Carla Schroder** is a serial career changer who first laid hands on a PC in the
mid-1990s and was instantly hooked. Since then she has worked as a system and net‐
work administrator running mixed Linux/Microsoft/Apple networks, tech journalist,
and technical writer. Carla has written over 1,000 Linux how-tos for various publica‐
tions and currently writes and maintains the product manuals for a Linux enterprise
software company. She is the author of the _Linux Cookbook_ (O’Reilly), _Linux Net‐_
_working Cookbook_ (O’Reilly), and _The Book of Audacity_ (No Starch Press). Her fans
love her skill at translating nerd to end user, and answering all those “How do I do
this?” questions.

**<u>Colophon</u>**

The animal on the cover of _Linux Cookbook_ is a hazel grouse ( _Tetrastes bonasia_ ).
Sometimes referred to as the hazel hen, this sedentary bird is one of the smaller mem‐
bers of the grouse species and can be found across much of eastern Europe and
northern Asia in dense woodlands.

The patterned plumage of these game birds is more grey in its underparts and more
brown on its wings and back. Male hazel grouses have crests on the top of their heads
and white-bordered black throats, while female hazel grouses have shorter crests and
brown throats. They are ground-feeding birds and eat mainly plant foods as well as
insects during the breeding season. Female hazel grouses incubate their eggs and care
for their chicks on their own.

The current conservation status of the hazel grouse is “Least Concern.” Many of the
animals on O’Reilly covers are endangered; all of them are important to the world.

The cover illustration is by Karen Montgomery, based on a black and white engraving
from _Meyers Kleines Lexicon_ . The cover fonts are Gilroy Semibold and Guardian
Sans. The text font is Adobe Minion Pro; the heading font is Adobe Myriad Con‐
densed; and the code font is Dalton Maag’s Ubuntu Mono.
