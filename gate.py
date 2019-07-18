
from collections import namedtuple
import numpy as np
from PIL import Image, ImageDraw


Point = namedtuple('Point', 'x y')
Line = namedtuple('Line','first_point second_point')

FIELD = (640, 480)
MIN_GATE_SIZE = 10
MAX_GATE_SIZE = 1000
PB1 = [(100,350),(100,200),(75,200),(75,150),(100,150),(100,50),(150,50),(150,200),(200,200),(200,125),(250,125),(250,300),(225,300),(225,250),(175,250), (175,350)]
PT1 = [(150,325),(150,265),(275,265),(275,100),(175,100),(175,125),(50,125),(50,75),(300,75),(300,325)]




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
		# print(index, point)
		if index == len(points) - 1:
			if (point.x == points[0].x or point.y == points[0].y):
				# print(f'last {point} has same coordinats with first {points[0]}')
				return True
			else:
				print(f'last {point} doesnt have same coordinats with first {points[0]}')
				return False

		elif point.x == points[index+1].x and point.y != points[index+1].y and X:
			X = False
			Y = True
			# print(f'x of {point} with index = {index} same with x of {points[index + 1]} with index = {index+1} X = {X} Y = {Y}')
		elif point.y == points[index+1].y and point.x != points[index+1].x and Y:
			X = True
			Y = False
			# print(f'y of {point} with index = {index} same with y of {points[index + 1]} with index = {index+1} X = {X} Y = {Y}')
		else:
			print(f'{point} with index = {index} doesnt have correct same coordinats with {points[index + 1]} index = {index + 1}')
			return False
# check_polygon_points(P2)





def intersection_lines(line, list_of_checked_lines):
	for some_line in list_of_checked_lines:

		if line.first_point.x == line.second_point.x:
			X = True
			Y = False
		else:
			X = False
			Y = True
		print(X, Y)
		if (line.first_point.x in range(some_line.first_point.x, some_line.second_point.x + 1) and \
			some_line.first_point.y in range(line.first_point.y, line.second_point.y + 1)) and X:
			print(f'{line}  has intersection with {some_line}')
			return True
		if (line.first_point.y in range(some_line.first_point.y, some_line.second_point.y + 1) and \
			some_line.first_point.x in range(line.first_point.x, line.second_point.x + 1)) and Y:
			print(f'{line}  has intersection with {some_line}')
			return True
		else:
			print(' No intersection')

	return False
	


def check_intersection_in_polygon(polygons_points, return_lines=False):
	points = [convert_to_point_obj(point) for point in polygons_points]

	last_line = points[-1],points[0]
	lines_list = list(zip(points[:-1],points[1:]))
	lines_list.append(last_line)
	if return_lines:
		return [convert_to_line_obj(item) for item in lines_list]

	lines =np.array([convert_to_line_obj(line) for line in lines_list])

	for index in range(len(lines)):

		mask = np.array([False if item < 3 or item%2 == 0 or (index== 0 and item == len(lines[index:])-1) else True \
			for item in range(len(lines[index:]))])

		if mask.any():
			# print(mask)
			line = convert_to_line_obj(lines[index])
			lines_for_checking = [convert_to_line_obj(some_line) for some_line in lines[index:][mask]]

			if intersection_lines(line,lines_for_checking) == False:
				print(f'{line} has no intersection with {lines_for_checking}')
			else:
				# print('Not correct coordinats of polygon')
				return False

	return True

# check_intersection_in_polygon(P2)

def size_of_polygon():# return False если габариты полигона не входят в систему координат, return min and max coordinat for the polygon
	pass


def polygon(polygons_points, start_coordinats=(0,0)):
	if check_polygon_points(polygons_points) and check_intersection_in_polygon(polygons_points):
		# if size_of_polygon(polygons_point, start_coordinats):
		# дописать возврат координат полигона если он входит в систему координат или его максимальные и минимальные координаты в системе координат

			return check_intersection_in_polygon(polygons_points=polygons_points, return_lines=True)
	else:
		return False

# print(polygon(P2))








def intersection_of_polygons_lines(top_lines, bottom_lines, point=False):
	# return dict with all intersectiond for every top lines with every bottom lines
	# if point = True funcktion return only coordinats of intersection between two lines
	all_pairs = []
	for t_line in top_lines:
		# print('T_LINE', t_line)
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

		for b_line in bottom_lines:
			# print('BOOTTOM_LINES ', bottom_lines)
			# print('B_LINE ',b_line)

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

					else:
						return False

		all_pairs.append(t_lines_pairs)
	return all_pairs





def correct_intersected_lines(list_of_dicts_with_intersected_lines):
	# return pairs of point with same intersections(line)
	res = []

	for index, item in enumerate(list_of_dicts_with_intersected_lines):
		one_line = item['top_line']
		intersected_lines = item['intersections']

		if index == len(list_of_dicts_with_intersected_lines)-1:
			break
		if len(intersected_lines) >= 2:

			for ather_item in list_of_dicts_with_intersected_lines[index+1:]:

				ather_line = ather_item['top_line']
				ather_intersected_lines = ather_item['intersections']

				if len(ather_intersected_lines) >= 2:

					same_lines = [line for line in ather_intersected_lines if line in intersected_lines]

					if len(same_lines) >= 2:

						for ind in range(0,len(same_lines)):
							if ind == len(same_lines)-1:
								break
							else:
								first_intersection_for_one_line, second_intersection_for_one_line 	 = \
								list(map(lambda x: intersection_of_polygons_lines([one_line],[x],point=True),[(same_lines[ind]), (same_lines[ind+1])]))
								first_intersection_for_ather_line, second_intersection_for_ather_line = \
								list(map(lambda x: intersection_of_polygons_lines([ather_line],[x],point=True),[same_lines[ind], same_lines[ind+1]]))

								correct_one_line = Line(convert_to_point_obj(point=first_intersection_for_one_line), convert_to_point_obj(point=second_intersection_for_one_line))
								correct_ather_line = Line(convert_to_point_obj(point=first_intersection_for_ather_line), convert_to_point_obj(point=second_intersection_for_ather_line))

								res.append((correct_one_line, correct_ather_line))
	return res




def check_vectior_intersection(point, oposits_lines_bt_poly, max_x=FIELD[0], max_y=FIELD[1], vertical=False, horizont=False):

	if vertical:
		vectopr_to_top 	 = Line(Point(point.x, point.y),Point(point.x, max_y))
		vectopr_to_bottom  = Line(Point(point.x, point.y),Point(point.x, 0))
		res = list(map(lambda x: intersection_of_polygons_lines(top_lines=[x], bottom_lines=oposits_lines_bt_poly, point=False), [vectopr_to_top, vectopr_to_bottom]))


	if horizont:
		vector_to_left  = Line(Point(point.x, point.y),Point(0, point.y))
		vector_to_right = Line(Point(point.x, point.y),Point(max_x, point.y))
		res = list(map(intersection_of_polygons_lines(top_lines=[x], bottom_lines=oposits_lines_bt_poly, point=False), [vectopr_to_left, vectopr_to_right]))
		
	return not all(item==None for item in res)

	# if all(item==None for item in res):
	# 	return False
	# else:
	# 	return True





def midle_point(line, oposits_lines_bt_poly):
	first_point,second_point = line
	if line.first_point.x==line.second_point.x: # verticall parallels lines
		point = Point(line.first_point.x, ((line.first_point.y + line.second_point.y) / 2))
		res_of_check = check_vectior_intersection(point=point, oposits_lines_bt_poly=oposits_lines_bt_poly, horizont=True)

	else: # horizontal parallel lines
		point = Point(((line.first_point.x + line.second_point.x) / 2), line.first_point.y)
		res_of_check = check_vectior_intersection(point=point, oposits_lines_bt_poly=oposits_lines_bt_poly, vertical=True)

	if res_of_check == True:
		return point
	else:
		return False




def find_gets(list_with_pairs_of_lines, oposits_lines_bt_poly):
	gates = []
	for pair_of_parallels_lines in list_with_pairs_of_lines:
		gate = list(map(lambda x: midle_point(line=x, oposits_lines_bt_poly=oposits_lines_bt_poly),pair_of_parallels_lines))
		if False in gate:
			continue
		else:
			gates.append(gate)
	return gates
		




def gates(bottom_polygon, top_polygon): # return gate for top polygon

	if top_polygon[0].first_point.x == top_polygon[0].second_point.x:
		top_vertical_lines      = [top_polygon[index_line] for index_line in range(0, len(top_polygon),2)]
		top_horizontal_lines    = [top_polygon[index_line] for index_line in range(1, len(top_polygon),2)]
	else:
		top_horizontal_lines    = [top_polygon[index_line] for index_line in range(0, len(top_polygon),2)]
		top_vertical_lines      = [top_polygon[index_line] for index_line in range(1, len(top_polygon),2)]

	if bottom_polygon[0].first_point.x == bottom_polygon[0].second_point.x:
		bottom_vertical_lines   = [bottom_polygon[index_line] for index_line in range(0, len(bottom_polygon),2)]
		bottom_horizontal_lines = [bottom_polygon[index_line] for index_line in range(1, len(bottom_polygon),2)]
	else:
		bottom_horizontal_lines = [bottom_polygon[index_line] for index_line in range(0, len(bottom_polygon),2)]
		bottom_vertical_lines   = [bottom_polygon[index_line] for index_line in range(1, len(bottom_polygon),2)]

	# next get list of dicts of lines with same intersections {'top_line':line of top polygon, 'intersections': list of bottom poligons lines}
	intersection_of_top_vertical_lines   = \
	intersection_of_polygons_lines(top_lines=top_vertical_lines, bottom_lines=bottom_horizontal_lines)
	intersection_of_top_horizontal_lines = \
	intersection_of_polygons_lines(top_lines=top_horizontal_lines, bottom_lines=bottom_vertical_lines)



	# # get list with pair of parallels lines
	parallels_vertical    = \
	correct_intersected_lines(list_of_dicts_with_intersected_lines = intersection_of_top_vertical_lines)
	parallels_horizontal = \
	correct_intersected_lines(list_of_dicts_with_intersected_lines = intersection_of_top_horizontal_lines)

	vertical_gates   = find_gets(parallels_horizontal, oposits_lines_bt_poly=bottom_horizontal_lines)
	horizontal_gates = find_gets(parallels_vertical, oposits_lines_bt_poly=bottom_vertical_lines)
	return vertical_gates + horizontal_gates















def draw(list_of_pairs_of_polygons):
	for pair in list_of_pairs_of_polygons:
		bottom_polygon = polygon(pair[0])
		top_polygon = polygon(pair[1])
		gatess = gates(bottom_polygon=bottom_polygon, top_polygon=top_polygon)
		if bottom_polygon and top_polygon:
			image = Image.new('RGB', (FIELD), (255,255,255))
			pic_draw = ImageDraw.Draw(image)
			if bottom_polygon:
				pic_draw.polygon(pair[0], outline='blue')
			if bottom_polygon:
				pic_draw.polygon(pair[1], outline='green')
			if gatess:
				for gate in gatess:
					gate_size = np.array(gate)
					gate_size = abs(gate_size[0,0]-gate_size[1,0] + gate_size[0,1]-gate_size[1,1])
					if MIN_GATE_SIZE <= gate_size <= MAX_GATE_SIZE:
						pic_draw.line((gate[0].x,gate[0].y,gate[1].x, gate[1].y), fill=128, width=3)

			image.show()

draw([(PB1,PT1)])



