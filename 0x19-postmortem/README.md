Issue Summary:
   * Start time: 21/02/23 11:00 AM (CMT+3), End time: 21/02/23 5:00 PM (CMT+3).
   * MySql Database (MAMP) for a locally hosted wordpress website I was developing was returning an error in the phpmyadmin page with the message server (Mysql) not responding.
   * Root cause: Multiple mysql servers were running in the same port number.

Timeline:
   * 21/02/23 1:00 PM (GMT+3) - The issue was detected by me while restarting apache when developing a locally hosted wordpress website.
   * 21/02/23 1:05 PM (GMT+3) - I restarted Apache and mySQL database but error code still appeared 
   * 21/02/23 1:05 PM (GMT+3) I had to restart apache2 using ‘service apache2 restart’. The page was back up like normal.

Root cause and resolution:
   * Two databases both in XAMPP and MAMP where using same port number 81
   * The issue was resolved by changing port number and restarting Mysql in MAMP.

Corrective and preventative measures:
   * Always shut down one Apache server (MAMP, XAMPP etc) server when working with the other incase they are sharing port number.

