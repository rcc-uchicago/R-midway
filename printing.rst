h1. Printing

Printers are configured through the CUPS printer server *print.rcc.uchicago.edu*

Printers are named with the building and room number and printer model.

* ed126-phaser3250dn or xerox-phaser-3250.rcc.uchicago.edu

* reg216-phaser3250dn or reg216-phaser3250dn.uchicago.edu

* The Toshiba 4555C is the printer we use for large quantities of color announcements, and for scanning. It costs us per page printed, so please continue to use your office black and white printer for most of your printing needs. (*Note:* according to Kim, this info is out of date, and it no longer costs us per page printed.)

h2. Toshiba 4555C in TAAC

Instructions for Mac OS

(1) Download the driver, open it and install it. The driver is attached at the bottom of this page. Alternatively, the "e-Bridge Current Drivers" for Mac OSX 10.6 and later (Duplex, Color) from this webpage seems to work as well: http://business.toshiba.com/usa/support/downloads.jsp?SELCTD_MODEL=e-STUDIO5560C&AXN=SELCTD&site=usa

(2) Open Launchpad -> System Preferences -> Printer & Scanners

(3) Click "+" bottom at the left-bottom corner of the printers list

(4) Select "IP" on the top-bar

(5) Input / Select:

Address: copier.rcc.uchicago.edu
Protocol: LPD
Use: "Select Software" -> "TOSHIBA ColorMFP-X4"

Click Add.

(6) All the way clicking "Yes" until Done.

------ Below are old notes when it was at EDEL ------

* The website link to download the drivers is http://business.toshiba.com/support/index.jsp
** you may need to call IT Services to install the print driver
* The sales contact for the machine is 
John Cosich 
Proven Business Systems
708.407.2905
Jrcosich@simplyproven.com

* The training contact for the machine is 
Mary Sweet 
Proven Business Systems 
708.407.2924
msweet@simplyproven.com

* IP address: 128.135.112.19
** if you type that address in the omnibox you will be taken to admin control of the machine's address book, where emails/users can be added or deleted
* The code to access the printer is 60309
* From the print screen, select 'invalid' from the drop-down menu if you cannot find your job otherwise
* Can print from a USB
* Anything colored green on the machine's internal parts can be touched, all else, don't mess with it. 
* Toner replacement and machine repair are covered through Simply Proven for the duration of our lease. 
** Call the main number ((708) 614-1770) or go to their website (www.simplyproven.com) to replace toner or request service call. 
** Provide them with the ID # A4906 (located on a sticker on the machine)
** Always have one of every toner color on stock, if you use the last, send for a replacement immediately.

* For a complete user guide, check the top drawer of the Admin Assistant desk, or download it from Toshiba America using the model number.

------ End of old notes ------

h2. ED 126 

Modify the print queue name as necessary:

!macosprinter.png!

Alternatively, you can run these commands in a terminal to connect to the print server:
<pre>
echo BrowseProtocols cups | sudo tee -a /etc/cups/cupsd.conf
echo BrowsePoll print.rcc.uchicago.edu | sudo tee -a /etc/cups/cupsd.conf
sudo launchctl stop org.cups.cupsd && sudo launchctl start org.cups.cupsd
</pre>

h2. Reg 216 

If you're using Mac OS and want to do printing through the network (XEROX Phaser 3250), here are the steps,

> 1. Click the following link and download the driver
> 
> http://www.support.xerox.com/support/phaser-3250/file-download/enus.html?operatingSystem=macosx109&fileLanguage=en&contentId=123816&from=downloads&viewArchived=false
> 
> 2. Open and install the driver.
> 
> 3. In your DockBar, click "Lanchpad", then click "System Preferences"
> 
> 4. Choose "Printers and Scanners"
> 
> 5. Click the "+" on left-bottom corner, Open an "Add" window.
> 
> 6. Choose "IP" page, and put IP Address: 10.120.17.86, select protocol to be "HP Jetdirect - Socket".
> 
> 7. Now it's an important step, in the "Use" textbox, choose "Select Software". In the menu, choose "Xerox Phaser 3250D". Then click "OK".
> 
> 8. Now it's finished!

In Ubuntu:

> 1. Open System Settings -> Printing -> Add Printer
>
> 2. Select Network Printer -> Find Network Printer. In the text box enter the IP address 10.120.17.86. Keep the default port (9100) and connection (AppSocket/HP JetDirect). 
>
> 3. The automatically selected driver doesn't work right. In the "Printer Properties" dialog, click on the "Change..." button next to "Make and Model" to select a different driver. Select "Generic", "Postscript", "Generic Postscript Printer Foomatic".
