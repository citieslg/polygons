# 1. object Polygon
# 2. correct_crosing_polygon(same_lines, midle point in poligon_buttom)
# 3. gate
# 4. compair gate size
from collections import namedtuple
import numpy as np


Point = namedtuple('Point', 'x y')
Line = namedtuple('Line','first_point second_point')

SIZE_OF_FIELD = Point(480, 640)
P2 = [(0,0),(0,2),(1,2),(1,1),(2,1),(2,0)]
P1 = [(0,0),(0,1),(1,1),(1,0)]




def convert_to_point_obj(point):
	x, y = point
	return Point(x, y)



def convert_to_line_obj(line_coordinate):
	x1,y1 = line_coordinate[0]
	x2,y2 = line_coordinate[1]
	return Line(first_point =Point(x1,y1), second_point= Point(x2,y2))





def check_polygon_points(polygons_points, X=True, Y=True):
	points = [convert_to_point_obj(point) for point in polygons_points]

	for index, point in enumerate(points):
		print(index, point)
		if index == len(points) - 1:
			if (point.x == points[0].x or point.y == points[0].y):
				print(f'last {point} has same coordinats with first {points[0]}')
				return True
			else:
				print(f'last {point} doesnt have same coordinats with first {points[0]}')
				return False

		elif point.x == points[index+1].x and point.y != points[index+1].y and X:
			X = False
			Y = True
			print(f'x of {point} with index = {index} same with x of {points[index + 1]} with index = {index+1} X = {X} Y = {Y}')
		elif point.y == points[index+1].y and point.x != points[index+1].x and Y:
			X = True
			Y = False
			print(f'y of {point} with index = {index} same with y of {points[index + 1]} with index = {index+1} X = {X} Y = {Y}')
		else:
			print(f'{point} with index = {index} doesnt have correct same coordinats with {points[index + 1]} index = {index + 1}')
			return False
# check_polygon_points(P2)





def intersection_lines(line, list_of_checked_lines):
	for some_line in list_of_checked_lines:
		print(line)
		print(some_line)

		if line.first_point.x == line.second_point.x:
			X = True
			Y = False
		else:
			X = False
			Y = True
		print(X, Y)
		if (line.first_point.x in range(some_line.first_point.x, some_line.second_point.x + 1) and some_line.first_point.y in range(line.first_point.y, line.second_point.y + 1)) and X:
			print(f'{line}  has intersection with {some_line}')
			return True
		if (line.first_point.y in range(some_line.first_point.y, some_line.second_point.y + 1) and some_line.first_point.x in range(line.first_point.x, line.second_point.x + 1)) and Y:
			print(f'{line}  has intersection with {some_line}')
			return True
		else:
			print(' No intersection')

	return False
	


def check_intersection_in_polygon(polygons_points, X=True, Y=True):
	points = [convert_to_point_obj(point) for point in polygons_points]



	last_line = points[-1],points[0]
	lines_list = list(zip(points[:-1],points[1:]))
	lines_list.append(last_line)

	lines =np.array([convert_to_line_obj(line) for line in lines_list])

	for index in range(len(lines)):

		mask = np.array([False if item < 3 or item%2 == 0 or (index== 0 and item == len(lines[index:])-1) else True for item in range(len(lines[index:]))])

		if mask.any():
			print(mask)
			line = convert_to_line_obj(lines[index])
			lines_for_checking = [convert_to_line_obj(some_line) for some_line in lines[index:][mask]]

			if intersection_lines(line,lines_for_checking) == False:
				print(f'{line} has no intersection with {lines_for_checking}')
			else:
				print('Not correct coordinats of polygon')
				return False

	return True

# check_intersection_in_polygon(P2)

def size_of_polygon():# return False если габариты полигона не входят в систему координат, return min and max coordinat for the polygon
	pass


def polygon(polygons_point, start_coordinats=(0,0)):
	if check_polygon_points(polygons_point) and check_intersection_in_polygon(polygons_point):
		# if size_of_polygon(polygons_point, start_coordinats):
		# дописать возврат координат полигона если он входит в систему координат или его максимальные и минимальные координаты в системе координат
			return True
	else:
		return False

# print(polygon(P2))


def intersection_of_polygons_lines(top_lines, bottom_lines, point=False):
	# if point = True funcktion return only coordinats of intersection between two lines
	all_pairs = []
	for t_line in top_lines:
		t_lines_pairs = {'top_line': t_line, 'intersections':[]}
		# {line: t_line, intersections: b_line,b_line}

		if t_line.first_point.x == t_line.second_point.x:
			t_const = t_line.first_point.x
			t_max = max(t_line.first_point.y, t_line.second_point.y)
			t_min = min(t_line.first_point.y, t_line.second_point.y)
			X = True
			Y = False
		else:
			t_const = t_line.first_point.y
			t_max = max(t_line.first_point.x, t_line.second_point.x)
			t_min = min(t_line.first_point.x, t_line.second_point.x)
			X = False
			Y = True


		for b_line in bottom_line:

			if b_line.first_point.x == b_line.second_point.x:
				b_max = max(b_line.first_point.y, b_line.second_point.y)
				b_min = min(b_line.first_point.y, b_line.second_point.y)
				b_const = b_line.first_point.x
			else:
				b_max = max(b_line.first_point.x, b_line.second_point.x)
				b_min = min(b_line.first_point.x, b_line.second_point.x)
				b_const = b_line.first_point.y

			if t_const in range(b_min, b_max+1) and b_const in range(t_min, t_max+1):
				t_lines_pairs['intersections'].append(b_line)

				if point:
					if X:
						return t_const, b_const
					if Y:
						return b_const, t_const


		all_pairs.append(t_lines_pairs)

	return all_pairs

check_vectior_intersection(max_x=, max_y=)

def midle_point(first_point, second_point):

	if first_point.x==second_point.x:
		midle_x = first_point.x
		midle_y = (first_point.y + second_point.y) / 2
		check_vectior_intersection()
	else:
		midle_x = (first_point.x + second_point.x) / 2
		midle_y = first_point.y
		check_vectior_intersection()

	return Point(midle_x, midle_y)




def correct_intersected_lines(list_of_dicts_with_intersected_lines):
	for index, item in enumerate(list_of_dicts_with_intersected_lines):
		one_line = list_of_dicts_with_intersected_lines['top_line']
		intersected_lines = list_of_dicts_with_intersected_lines['intersections']

		if index == len(list_of_dicts_with_intersected_lines)-1:
			break
		if len(intersected_lines) >= 2:

			for ather_item in list_of_dicts_with_intersected_lines[index+1:]:

				ather_line = ather_item['top_line']
				ather_intersected_lines = ather_item['intersections']

				if len(ather_intersected_lines) >= 2:

					same_lines = [line for line in ather_intersected_lines if line in intersected_lines]

					if len(res) >= 2:
						print('One line has more then two same intersected lines with ather line')

						for ind in range(0,len(res)):
							if ind == len(res)-1:
								break
							else:
								first_intersection_one_line, second_intersected_one_line 	 = list(map(lambda x: intersection_of_polygons_lines(one_line,x,point=True),[same_line[ind], same_line[ind+1]]))
								first_intersection_ather_line, second_intersected_ather_line = list(map(lambda x: intersection_of_polygons_lines(ather_line,x,point=True),[same_line[ind], same_line[ind+1]]))














def gates(bottom_polygon, top_polygon): # return gate for top polygon

	if top_polygon.line[0].first_point.x == top_polygon.line[0].second_point.x:
		top_vertical_lines      = [top_polygon[index_line] for index_line in range(0, len(top_polygon),2)]
		top_horizontal_lines    = [top_polygon[index_line] for index_line in range(1, len(top_polygon),2)]
	else:
		top_horizontal_lines    = [top_polygon[index_line] for index_line in range(0, len(top_polygon),2)]
		top_vertical_lines      = [top_polygon[index_line] for index_line in range(1, len(top_polygon),2)]

	if bottom_polygon.line[0].first_point.x == bottom_polygon.line[0].second_point.x:
		bottom_vertical_lines   = [bottom_polygon[index_line] for index_line in range(0, len(bottom_polygon),2)]
		bottom_horizontal_lines = [bottom_polygon[index_line] for index_line in range(1, len(bottom_polygon),2)]
	else:
		bottom_horizontal_lines = [bottom_polygon[index_line] for index_line in range(0, len(bottom_polygon),2)]
		bottom_vertical_lines   = [bottom_polygon[index_line] for index_line in range(1, len(bottom_polygon),2)]

	intersection_of_top_vertical_lines   = intersection_of_polygons_lines(top_lines=top_vertical_lines, bottom_lines=bottom_horizontal_lines)
	intersection_of_top_horizontal_lines = intersection_of_polygons_lines(top_lines=top_horizontal_lines, bottom_lines=bottom_vertical_lines)



def draw(list_of_pairs_of_polygons):
	for pair in list_of_pairs_of_polygons:
		bottom_polygon = polygon(pair[0])
		top_polygon = polygon(pair[1])
		gets = gates(bottom_polygon, top_polygon)


from PIL import Image, ImageDraw


def draw_polygon(list_of_points, layer):
	points = polygon(list_of_points)


	image = Image.new('RGB', (100,100), (255,255,255))
	pol_draw = ImageDraw.Draw(image)
	pol_draw.polygon(polygon_points, outline='red')

	image.show()
	image.save('wqwq.bmp')
	del image
	del pol_draw