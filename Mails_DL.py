from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from smtplib import SMTP

def send_mail_dl():
  strFrom = 'jessguzman044@gmail.com'
  strTo = 'chuchoska305t@hotmail.com'

  msgRoot = MIMEMultipart('related')
  msgRoot['Subject'] = 'Alguien encontro a tu perro'
  msgRoot['From'] = strFrom
  msgRoot['To'] = strTo
  msgRoot.preamble = 'This is a multi-part message in MIME format.'

  msgAlternative = MIMEMultipart('alternative')
  msgRoot.attach(msgAlternative)

  msgText = MIMEText('This is the alternative plain text message.')
  msgAlternative.attach(msgText)
  ###############################
  features = "perro fuerte con una cicatriz en la oreja"
  name = "Lazi"

  message = menssage_mail(name, features)
  ###############
  msgText = MIMEText(message, "html", _charset="utf-8")
  msgAlternative.attach(msgText)

  fp = open('jess.jpg', 'rb')
  msgImage = MIMEImage(fp.read())
  fp.close()

  msgImage.add_header('Content-ID', '<image1>')
  msgRoot.attach(msgImage)

  smtp = SMTP('smtp.gmail.com', 587)
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()
  smtp.login(strFrom, '') #PASSWD
  smtp.sendmail(strFrom, strTo, msgRoot.as_string())
  smtp.quit()


def menssage_mail(nombre, caracteristicas):
  name = nombre
  features = caracteristicas
  message = """\
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Dog Location</title>

</head>

<body style="margin:0;padding:0;">

<table width="100%" align="center" bgcolor="#959595" cellpadding="0" cellspacing="0" style="text-align:center;font-family:Arial, Helvetica, sans-serif;color:#000000; font-size:12px;">
<tbody>
<tr>
<td>

	<table width="600" cellpadding="0" cellspacing="0" align="center" style="font-size:12px;"><tbody>
	<tr><td height="28" align="center" style="color:#FFFFFF;">&nbsp;&nbsp;Dog location | <a href="[web_version]" style="color:#3CF; text-decoration:none;" target="_blank">Go to home</a></td>
    </tr>
	</tbody></table>

</td>
</tr>
<tr>
<td>
<table cellpadding="0" cellspacing="0" width="600" bgcolor="#FFFFFF" align="center" style="font-family:Arial, Helvetica, sans-serif; font-size:12px;">
<tr><td bgcolor="#33cc99" height="75" align="center" style="color:#FFFFFF; text-align:center;"><a href="#" target="_blank" style="border:none;"></a>
</td></tr>
<tr><td height="5" bgcolor="#25aa7e"></td></tr>
<tr><td><img src="cid:image1" style="display:block;" border="0"/></td></tr>
<tr><td height="155" align="center" style="font-family:Arial, Helvetica, sans-serif; text-align:center;">
<p style="color:#000000; font-size:22px;">Parece que alguien localizo a <h1>{name}</h1> </p>
<p style="color:#878787; font-size:16px;"> <h4>{features}</h4>  </p>
</td></tr>
<tr><td>
<table cellpadding="0" cellspacing="0" width="600">
<tr><td width="25"></td>
<td width="550">

</td>
<td width="25"></td></tr>
</table>
</td></tr>
<tr><td height="30"></td></tr>
</table>
<table cellpadding="0" cellspacing="0" width="600" bgcolor="#eaeaea" align="center" style="font-family:Arial, Helvetica, sans-serif;">
<tr><td height="10"></td></tr>
<tr><td height="80" align="center" style="text-align:center; font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#878787;">&iquest;Es tu mejor amigo?</td></tr>
<tr><td>
<table cellpadding="0" cellspacing="0" width="600" bgcolor="#eaeaea" align="center" style="font-family:Arial, Helvetica, sans-serif;">
<tr>
<td width="145"></td>
<td width="310" height="42" bgcolor="#33cc99" align="center" style="background-color:#33cc99; text-align:center; border-bottom:3px solid #25aa7e;">
<a href="#" target="_blank" style="font-size:19px; color:#FFFFFF; text-decoration:none;"> Si, es mi perro</a>
</td>
<td width="145"></td>
</tr>
</table>
</td></tr>
<tr><td height="50">&nbsp;</td></tr>
</table>
</td>
</tr>
<tr><td>
<table cellpadding="0" cellspacing="0" width="600" bgcolor="#676767" align="center">
<tr>
<td height="80" width="30"></td>
<td height="80" width="465" align="left" style="font-family:Arial, Helvetica, sans-serif; color:#FFFFFF; font-size:12px; text-align:left;">
<strong style="font-size:14px;">SAXSA DL</strong><br />
SAXSA Dog Location<br />
5500112233
</td>
<td width="30"><a href="#" target="_blank" style="border:none;"><img src="images/facebook.gif" border="0" /></a></td>
<td width="15"></td>
<td width="30"><a href="#" target="_blank" style="border:none;"><img src="images/twitter.gif" border="0" /></a></td>
<td height="80" width="30"></td>
</tr>
</table>
</td></tr>
</tbody>
</table>

</body>
</html>

  """.format(**locals())
  return message

