import smtplib
def spamBot():      #The phone number and carrier address: ###-###-###@carriersomething.com
    carrierNum = "516-857-0049@txt.att.net"
    gmailUser = "beytwicebeytwice@gmail.com"
    gmailPass = "beytwice"
    
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(gmailUser, gmailPass)
    
#    header = "To:",carrierNum,'\n', "From:",gmailUser,'\n'
#    print(header)
#    msg = header + "\n Body \n\n"
    
    msg = "HI STEPH."
    
    smtp_server.sendmail(gmailUser,carrierNum,msg)
    print(msg)
    print("Done.")
    smtp_server.close()
    
spamBot()