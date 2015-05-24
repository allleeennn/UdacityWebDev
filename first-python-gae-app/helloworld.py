import webapp2
import cgi

form = """
<form method="post">
	What is your birthday?
	<br>
	<label> Month
		<input name="month" value="%(month)s">
	</label>
	<label> Day
		<input name="day" value="%(day)s">
	</label>
	<label> Year
		<input name="year" value="%(year)s">
	</label>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type="submit">
</form>
"""
def valid_dates(month, day, year):
	if month.isdigit() and day.isdigit() and year.isdigit():
		
		month = int(month)
		day = int(day)
		year = int(year)
		
		if month >= 1 and month <= 12:
			if day >= 1 and day <= 31:
				if year >= 1900 and year <= 2020:
					return True
		return False

def escape_html(text):
	return cgi.escape(text, quote = True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):

    	user_input = (
    			self.request.get('month'),
    			self.request.get('day'),
    			self.request.get('year'))
    		

    	if not valid_dates(user_input[0], user_input[1], user_input[2]):
    		self.write_form("That doesn't look valid to me friend",user_input)
    	else:
    		self.redirect("/thanks")

    def write_form(self, error="", user_input=("","","")):
		self.response.out.write(form % {"error": error, 
										"month": escape_html(user_input[0]),
										"day": escape_html(user_input[1]),
										"year": escape_html(user_input[2])})


class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/thanks',ThanksHandler)
], debug=True)
