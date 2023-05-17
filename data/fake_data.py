
all_likes = 0


def increment_likes():
	global all_likes
	all_likes = all_likes + 1
	print(all_likes)


def reduce_likes():
	global all_likes
	all_likes = all_likes - 1
	print(all_likes)


if __name__ == '__main__':
	increment_likes()
	reduce_likes()




