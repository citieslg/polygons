class Point2d(object):
	def __init__(self, x=0, y=0):
		try:
			float(x), float(y)

			self.x = float(x)
			self.y = float(y)
		except ValueError:
			print(f'{x} or {y} Not numbers enter numbers')

	def __str__(self):
		try:
			return f'x = {self.x} and  y = {self.y}'
		except AttributeError:
			return f'AttributeError with x or y'

	def __len__(self):
		return len([self.x, self.y])

	def get_values(self):
		return (self.x, self.y)



class Line2d(object):
	def __init__(self, first_point, second_point):
		
		if type(first_point) is Point2d and\
		 type(second_point) is Point2d:

			self.first_point = first_point
			self.second_point = second_point

		elif (type(first_point) and type(second_point)) is list or\
		 tuple:
			self.first_point = Point2d(*first_point)
			self.second_point = Point2d(*second_point)


	def __str__(self):
		return f'Line first_point = ({self.first_point}),\
		 second point = ({self.second_point})'

	def lenth_line(self):
		if self.first_point.x == self.second_point.x:
			return float(abs(self.first_point.y - self.second_point.y))
		elif self.first_point.y == self.second_point.y:
			return float(abs(self.first_point.x - self.second_point.x))
		else:
			print('The line shoud be parallel to coordinats x or y')




	def is_line_parallel_to_coordinat(object):
		if object.first_point.x == object.second_point.x or object.first_point.y == object.second_point.y:
			return True
		else:
			return False




	def is_right_angle_to(self, ather_line):
		if type(ather_line) is Line2d:

			if ather_line.is_line_parallel_to_coordinat() and self.is_line_parallel_to_coordinat():
				if (self.first_point.get_values() == \
					(ather_line.first_point.get_values() or ather_line.second_point.get_values())) or \
				(self.second_point.get_values == \
					(ather_line.first_point.get_values() or ather_line.second_point.get_values())):

					return True
				else:
					return False

		else:
			print('Not correct argument ather_line')







p1 = Point2d(0,1)
p2 = Point2d(0,1)



# print(len(p1))

l1 = Line2d((0,1),(2,1))
l2 = Line2d(p1,p2)

print(l1.is_right_angle_to(l2))
# print(l1.is_line_parallel_to_coordinat())