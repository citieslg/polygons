import PySimpleGUI as sg
kef = 20

RED_POLYGON = '''(9.49 6.65) (9.49 4.975) (12.845 4.975) (12.845 -5.65) (10.11 -5.65) (10.11 -5.665) (6.065 -5.665) (6.065 -3.26) (2.385 -3.26) (2.385 1.075) (4.79 1.075) (4.79 6.65)'''


list_of_square = ['polygon_1', 'polygon_2']

layout = [
			[sg.Combo(list_of_square)],
			[sg.Text('Left    '), sg.Spin([-2,-1,0,1,2] , initial_value=1, size=(5,1), key='left')
			,sg.Text(' '*70)
			,sg.Text('Bottom'), sg.Spin([-2,-1,0,1,2], initial_value=1, size=(5,1), key='bottom')],
			[sg.Text('Right  '), sg.Spin([-2,-1,0,1,2], initial_value=1, size=(5,1), key='right')
			,sg.Text(' '*70)
			,sg.Text('Top     '), sg.Spin([-2,-1,0,1,2], initial_value=1, size=(5,1),key='top')],
			[sg.Text('Width '), sg.Spin([-2,-1,0,1,2], initial_value=1, size=(5,1), key='width')
			,sg.Text(' '*70)
			,sg.Text('Height '), sg.Spin([-2,-1,0,1,2], initial_value=1, size=(5,1),key='height')],
			[sg.Graph(key='g', canvas_size=(640,480), graph_bottom_left=(-20, -480/2), graph_top_right=(640/2-20, 480/2))]
]
def draw_red_polygon(points):
	points = points.split(') (')
	points[0] = points[0].strip('(')
	points[-1] = points[-1].strip(')')
	correct_points = []
	for item in points:
		x,y = item.split(' ')
		x,y = round(float(x)*kef, 3),round(float(y)*kef,3)
		correct_points.append((x,y))


	last_line = correct_points[-1],correct_points[0]
	lines = list(zip(correct_points[0:-1], correct_points[1:]))
	lines.append(last_line)

	return [graph.DrawLine((line[0]), (line[1]), color='red', width=1) for line in lines]


def draw_rectangles(_topleft=(1.5*kef, 2.3*kef), _bottomright=(8.5*kef, -1.2*kef)):
	return graph.DrawRectangle(top_left=_topleft, bottom_right=_bottomright, line_color='yellow')



window = sg.Window('Polygon_games').Layout(layout)
# 1 way : vs code -> breakpoint, step by step
# 2 way : import pdb; pdb.set_trace();


import math
graph = window.FindElement('g')
index=0
while True:
	index+=1
	

	button, values = window.Read(timeout=50)
	if button is None or button == 'Exit': break


	graph.DrawRectangle((-20, -480/2), (640/2-20, 480/2), fill_color='black')
	# line = 0,0  ,  50, math.sin(index/10)*50
	# graph.DrawLine(line[:2], line[2:], color='red', width=3)
	line = 0,0  ,  150,150
	x_line = -20,0  ,  640/2-20, 0
	y_line = 0, -480/2  ,  0, 480/2
	graph.DrawLine(x_line[:2], x_line[2:], color='white', width=1)
	graph.DrawLine(y_line[:2], y_line[2:], color='white', width=1)
	graph.DrawCircle((0, 100), 5, fill_color='green')
	draw_red_polygon(RED_POLYGON)
	draw_rectangles()
	# p1,p2,p3 = int(values['p1']), int(values['p2']), int(values['p3'])


window.Close()



