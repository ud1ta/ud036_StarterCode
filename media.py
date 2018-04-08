class Movie():
	"""Movie class to create your favorite movies, including its movie title, box art URL, and the movie trailer YouTube link
	
	Arguments:
		movie_title (str): Movie title
		movie_poster (str): Movie poster URL
		movie_trailer (str): Movie official trailer URL
	
	Attributes:
		title: A string that stores the movie title
		poster_image_url: A string that stores the URL of the movie poster
		trailer_youtube_url: A string that stores the URL of the movie trailer
	
	"""
	
	def __init__(self, movie_title, movie_poster, movie_trailer):
		self.title = movie_title
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
		
