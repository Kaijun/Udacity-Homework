import webapp2
import cgi
import re

signup_form="""

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(fillusr)s">
          </td>
          <td class="error">
	%(errorusr)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(fillpsw)s">
          </td>
          <td class="error">
          %(errorpsw)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(fillpswv)s">
          </td>
          <td class="error">
	%(errorpswv)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(fillemail)s">
          </td>
          <td class="error">
	%(erroremail)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

class Signup(webapp2.RequestHandler):

	def valid_username(self, username):
		USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
		return USER_RE.match(username)

	def valid_password(self, password):
		PSW_RE = re.compile(r"^.{3,20}$")
		return PSW_RE.match(password)

	def valid_email(self, email):
		EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
		return EMAIL_RE.match(email)		

	def write_form(self, fu="", eu="", fp="", ep="", fpv="", epv="", fe="", ee=""):
		self.response.out.write(signup_form % {"fillusr": fu, 
							"errorusr": eu, 
							"fillpsw": fp, 
							"errorpsw": ep, 
							"fillpswv": fpv, 
							"errorpswv": epv, 
							"fillemail": fe, 
							"erroremail": ee})         #Dictionary Format!!!!!!!!!!!!!!!


	def get(self):
		self.write_form()

	def post(self):

		error1 = "That's not a valid username."
		error2 = "That wasn't a valid password."
		error3 = "Your passwords didn't match."
		error4 = "That's not a valid email."
		
		er1 = er2 = er3 = er4 = ""

		get_username = self.request.get('username')
		get_password = self.request.get('password')
		get_verify = self.request.get('verify')
		get_email = self.request.get('email')

		if self.valid_username(get_username) is not None and  self.valid_password(get_password) is not None and self.valid_email(get_email) is not None and get_password == get_verify:
			self.redirect("/welcome?username=%s" % get_username)
		else:
			pass
		if self.valid_username(get_username) is not None and  self.valid_password(get_password) is not None and get_email == "" and get_password == get_verify:
			self.redirect("/welcome?username=%s" % get_username)                
																		#Redirection!!!!!!!!!!! URL+name!!!!
		else:
			pass	

		if self.valid_username(get_username)  is None:
			er1 = error1
		else:
			pass
		if self.valid_password(get_password) is None:				
			er2 = error2
		else:
			pass
		if self.valid_password(get_password) is not None and get_password != get_verify:
			er3 = error3			
		else:
			pass
		if  get_email != "" and self.valid_email(get_email) is None:
			er4 = error4
		else:
			pass

			self.write_form(get_username, er1, "", er2, "", er3, get_email, er4)

class WelcomHandler(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('username')				#Get the username in URL!
		self.response.out.write("Welcome, %s" % name)

		

		



		# if  self.valid_username(get_username) is None:
		# 	self.write_form('error_usr', error1)

		# self.response.out.write(signup_form)