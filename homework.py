import webapp2
import cgi
from rot13 import *
from User_Signup import *

main_html="""

<center>
<div id="div1" style="height:1000px;width:1000px">
<br><br>
<div align="left"><font size=5><b>My Homeworks of CS253 on Udacity</b></font></div>
<br><br>
<table align="left" border="0">
<tr>
  <td>  Unit 1: </td>
  <td><S>Google App Engine</S> (quite simple)</td>
</tr>
<tr>
  <td>  Unit 2: </td>
  <td><a href="/rot13">Rot13</a></td>
</tr>
<tr>
  <td></td>
  <td><a href="/signup">User_Signup</a></td>

</tr>
</table>
</div>
</center>

"""
class main_html_class(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(main_html)



app = webapp2.WSGIApplication([ ('/', main_html_class), 
					('/rot13', Rot13),
					('/signup',Signup),
					('/welcome',WelcomHandler)],
                              debug=True)					

                              #It's the  Redirect!
