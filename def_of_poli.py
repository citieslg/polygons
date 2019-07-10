# 1. проверка валидности - возвращает координат
# 	- проверка пересечения отрезков
# 	- высчитывать макс длинну и макс ширину фигуры, что бы можно было ее разместить на картинке
# 2. отрисовывает  полигон по координатам 
# 3. проверяет пересечение фигур - возвращает размер Гейта!!!
# 4. Делает десктоп
# 	- который обновляет картинку!!! после нажатия клавиши пуск

a = [(30,0),(30,20),(20,20),(20,40),(40,40),(40,30),(60,30),(60,50),(80,50),(80,20),(60,20),(60,0)]




def valid_coordinats_points(list_of_points, next_x=True, next_y=True):
	for index, point in enumerate(list_of_points):

		if index == len(list_of_points)-1:

			if point[0] == list_of_points[0][0] or point[1] == list_of_points[0][1]:
				print('last_point is valid')
				return True
			else:
				print('last point is not valid')
				return False


		elif point[0] == list_of_points[index+1][0] and next_x:
			print('x valid')
			print(point,'-',list_of_points[index+1])
			next_x = False
			next_y = True
		elif point[1] == list_of_points[index+1][1] and next_y:
			print('y valid')
			print(point,'-',list_of_points[index+1])
			next_x = True
			next_y = False
		else:
			print(f'Not walid point {point}, index = {index} with next point {list_of_points[index+1]}')
			return False



def polygons_lines(coordinats_of_points):
	sections = [(point, coordinats_of_points[(len(coordinats_of_points) - (2*len(coordinats_of_points)-num))+1]) \
	for num, point in enumerate(coordinats_of_points)]
	return sections



def valid_crossing_lines(list_of_lines):
	for num, line in enumerate(list_of_lines):

		if line[0][0] == line[1][0]: # compair X first and second points of the line

			line_const_value = line[0][0] # X is const
			index_next_line_range = 0 # index of X of ather line which can intersect the line
			index_next_line_const = 1 # Y of ather line const
			line_index_range = 1 # index of Y the line for checking intersection with ather line

		if line[0][1] == line[1][1]:

			line_const_value = line[0][1]
			index_next_line_range = 1
			index_next_line_const = 0
			line_index_range = 0

		for index in range(num+3,len(list_of_lines),2): # index of ather line in list_of_lines

			if num == 0 and index == len(list_of_lines)-1: # dont check first line with last
				continue
			print(line, list_of_lines[index])
			next_line = list_of_lines[index]

			# переделать мин макс
			if line_const_value in range(next_line[0][index_next_line_range], next_line[1][index_next_line_range]+1)\
			 and next_line[0][index_next_line_const] in range(line[0][line_index_range], line[1][line_index_range]+1):

				print(f'Line {line} with index {num} intersects with line {next_line} with index {index}')
				return False
			else:
				print(f'Line {line} with index {num} does not intersect with line {next_line} with index {index}')
	return True



def polygon(list_of_points):
	if valid_coordinats_points(list_of_points=list_of_points, next_x=True, next_y=True):
		polygons_sections = polygons_lines(list_of_points)
		if valid_crossing_lines(polygons_sections):
			return list_of_points



def lendfill_of_polygon(list_of_points, start_coordinats):
	'''use when you have to know that figure in visible area of some field'''
	x_max = max([point[0] for point in a]) + start_coordinats[0]
	x_min = min([point[0] for point in a]) + start_coordinats[0]
	y_max = max([point[1] for point in a]) + start_coordinats[1]
	y_min = min([point[1] for point in a]) + start_coordinats[1]
	print(f'lenth is {x_max - x_min} and height is {y_max-y_min}')

	return(x_max, x_min, y_max, y_min)


def points_of_polygon_with_coordinats(points, start_coordintas, size_of_field):

	x_max, x_min, y_max, y_min = lendfill_of_polygon(points, start_coordinats)
	if points[0][0] - x_min >= 0 and\
	 point[0][0] + x_max <= size_of_field[0] and\
	 points[0][1] - y_min >= 0 and\
	 points[0][1] + y_max <= size_of_field[1]:
		points_with_coordinats = [(point[0]+start_coordinats[0], point[1]+start_coordinats[1]) for point in points]
		return points_with_coordinats
	else:
		print('Polygon out of field')
		return False



p1 = [((2,1),(2,5)), ((2,5),(3,5)), ((3,5),(3,1)), ((3,1),(2,1))]
p2 = [((1,2),(1,4)), ((1,4),(5,4)), ((5,4),(5,2)), ((5,2),(1,2))]


def gates(list_indexes_intersections_lines, lines_polygon_one, lines_polygon_two):
	# определить точные условия для поиска
	for index_of_item, item_in_indexes_list in enumerate(list_indexes_intersections_lines):

		line_one = lines_polygon_one[item_in_indexes_list[0]] # line from polygon_one
		crossed_lines_the_line = item_in_indexes_list[1]


		for index_of_ather_item in range(index_of_item+1, len(list_indexes_intersections_lines)):

			ather_line = lines_polygon_one[index_of_ather_item[0]] # line from polygon_two
			crossed_lines_ather_line = list_indexes_intersections_lines[index_of_ather_item][1]
			results = [for line in crossed_lines_ather_line if line in crossed_lines_the_line]
			if len(results) >= 2:
				if line_one[0][0] == line_one[1][0]:
					const_line_one = line_one[0][0]
				else:
					const_line_one = line_one[0][1]

				if ather_line[0][0] == ather_line[1][0]:
					const_ather_line = ather_line[0][0]
				else:
					const_ather_line = ather_line[0][1]

				size_of_gate = max(const_line_one, const_ather_line) - min(const_line_one, const_ather_line)


			# а если линий будет больше ????
			# если линия будет оставаться в фигуре????







def intersections_polygons(lines_polygon_one, lines_polygon_two):
	if lines_polygon_one[0][0][0] == lines_polygon_one[0][1][0]:
		print('in line one x is same')
		one_same_x = True
		line_one_const = [0,1]
	else:
		one_same_x = False
		line_one_const = [1,0]

	if lines_polygon_two[0][0][0] == lines_polygon_two[0][1][0]:
		print('in line two x is same')
		two_same_x = True
	else:
		two_same_x = False

	if one_same_x == two_same_x:
		first_index = [1,0]
	else:
		first_index = [0,1]

	
	all_correct_intersections = []
	for index, one_line in enumerate(lines_polygon_one):
		
		intersections = []
		for index_in_line_two in range(first_index[0],len(lines_polygon_two),2):
			print(one_line, ' with ',lines_polygon_two[index_in_line_two])
			two_line = lines_polygon_two[index_in_line_two]
			two_line_min = min(two_line[0][line_one_const[0]], two_line[1][line_one_const[0]])
			two_line_max = max(two_line[0][line_one_const[0]], two_line[1][line_one_const[0]])
			one_line_min = min(one_line[0][line_one_const[1]], one_line[1][line_one_const[1]])
			one_line_max = max(one_line[0][line_one_const[1]], one_line[1][line_one_const[1]])

			if one_line[0][line_one_const[0]] in range(two_line_min, two_line_max + 1) and\
			 two_line[0][line_one_const[1]] in range(one_line_min, one_line_max + 1):
				print(one_line, ' intersection with ',lines_polygon_two[index_in_line_two], '\n'*2)
				intersections.append(index_in_line_two)
			print('intersections', intersections)
		if len(intersections) >= 2:
			more_then_two_intersections = (index,intersections)
			all_correct_intersections.append(more_then_two_intersections)
			print('Coorsect_line with more then two intersections or equal ', all_correct_intersections)

			
		first_index = first_index[::-1]
		line_one_const = line_one_const[::-1]
	print(all_correct_intersections)



# intersections_polygons(p1,p2)




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



# lendfill_of_polygon(a)