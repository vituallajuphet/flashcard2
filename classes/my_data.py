class MyData:

	def __init__(self):
		self.data = [
			{
				"folder_name":"test",
				"cards": [
					{"title":"test2", "content":"the conetent1"},
					{"title":"test3", "content":"the conetent2"},
				]
			},
			{
				"folder_name":"tess2",
				"cards": [
					{"title":"zilong", "content":"Who is the greatest hero?"},
					{"title":"test2", "content":"the conetent1"},
					{"title":"test3", "content":"the conetent2"},
					{"title":"test4", "content":"the conetent4"},
					{"title":"test5", "content":"the conetent5"},
				]
			}
		]
	
	def get_data(self):
		return self.data

	def set_data(self, dta):
		self.data = dta