class MyData:

	def __init__(self):
		self.data = [
			[
				{"title":"zilong", "content":"Who is the greatest hero?"},
				{"title":"test2", "content":"the conetent1"},
				{"title":"test3", "content":"the conetent2"},
			],
			[
				{"title":"test", "content":"the conetent3"},

			]
		]
	
	def get_data(self):
		return self.data

	def set_data(self, dta):
		self.data = dta