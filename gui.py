import PySimpleGUI as sg

# RED_POLYGON = '''(9.49 6.65) (9.49 4.975) (12.845 4.975) (12.845 -5.65) (10.11 -5.65) (10.11 -5.665) (6.065 -5.665) (6.065 -3.26) (2.385 -3.26) (2.385 1.075) (4.79 1.075) (4.79 6.65)'''
FIELD = (640,480)


list_of_square = ['active draw mod']

layout = [
			[sg.Combo(list_of_square)],
			[sg.Text('Left    '), sg.Spin(list(range(-20,620,5)) , initial_value=0, size=(5,1), key='left')
			,sg.Text(' '*70)
			,sg.Text('Bottom'), sg.Spin(list(range(-240,235,5)), initial_value=0, size=(5,1), key='bottom')],
			[sg.Text('Right  '), sg.Spin(list(range(-15,620,5)), initial_value=0, size=(5,1), key='right')
			,sg.Text(' '*70)
			,sg.Text('Top     '), sg.Spin(list(range(-20,620,5)), initial_value=0, size=(5,1),key='top')],
			[sg.Text('Width '), sg.Spin(list(range(0,640,5)), initial_value=0, size=(5,1), key='width')
			,sg.Text(' '*70)
			,sg.Text('Height '), sg.Spin(list(range(0,480,5)), initial_value=0, size=(5,1),key='height')],
			[sg.Graph( FIELD, (-20,-240),(620,240),key='g')]
]

	



window = sg.Window('Polygon_games').Layout(layout)
graph  = window.FindElement('g')
left   = window.FindElement('left')
right  = window.FindElement('right')
top    = window.FindElement('top')
bottom = window.FindElement('bottom')
width  = window.FindElement('width')
height = window.FindElement('height')

def background():
	graph.DrawRectangle((-20,-240),(620,240), fill_color='black', line_color='black')
	graph.DrawLine((-20,0),(620,0), color='white', width=.3)
	graph.DrawLine((0,-240),(0,240), color='white', width=.3)

def rectangle(bottom_left, top_right):
	graph.DrawRectangle(bottom_left, top_right, fill_color='yellow', line_color='yellow')
	return (bottom_left[0],top_right[0], top_right[1],bottom_left[1],top_right[0]-bottom_left[0], top_right[1]-bottom_left[1])




	return [_left, _right, _top, _bottom, _width, _height]

def compair_values(saved_values, values):
	if saved_values[0] != int(values[0]):

		_left   = values[0]
		_width  = saved_values[4]
		_right  = _width + _left
		_top    = saved_values[2]
		_bottom = saved_values[3]
		_height = saved_values[5]


	elif saved_values[1] != values[1]:

		_right  = values[1]
		_width  = saved_values[4]
		_left   = _right - _width
		_top    = saved_values[2]
		_bottom = saved_values[3]
		_height = saved_values[5]


	elif saved_values[2] != values[2]:
		_left   = saved_values[0]
		_right  = saved_values[1]
		_top    = values[2]
		_height = saved_values[5]
		_bottom = _top - _height
		_width  = saved_values[4]


	elif saved_values[3] != values[3]:
		_left   = saved_values[0]
		_right  = saved_values[1]
		_bottom = values[3]
		_height = _values[5]
		_top    = _bottom + _height
		_width  = _values[4]


	elif saved_values[4] != values[4]:

		_width  = values[4]
		_left   = saved_values[0]
		_right  = _left + _width
		_top    = saved_values[2]
		_bottom = saved_values[3]
		_height = saved_values[5]


	elif saved_values[5] != values[5]:

		_height = values[5]
		_left   = saved_values[0]
		_right  = saved_values[1]
		_bottom = saved_values[3]
		_top    = _bottom + _height
		_width  = saved_values[4]


	else:
		
		_left   = saved_values[0]
		_right  = saved_values[1]
		_top    = saved_values[2]
		_bottom = saved_values[3]
		_width  = saved_values[4]
		_height = saved_values[5]

	left.Update(value=_left)
	right.Update(value=_right)
	top.Update(value=_top)
	bottom.Update(value=_bottom)
	width.Update(value=_width)
	height.Update(value=_height)

	bottom_left = (_left, _bottom)
	top_right = (_right, _top)

	return bottom_left, top_right



saved_values = rectangle((0,0),(150,100))

while True:

	

	button, values = window.Read(timeout=50)
	if button is None or button == 'Exit': break
	background()
	_values = [int(values['left']), int(values['right']), int(values['top']), int(values['bottom']), int(values['width']), int(values['height'])]

	b_l, t_r = compair_values(saved_values=saved_values, values=_values)
	saved_values = rectangle(bottom_left=b_l,top_right=t_r)


window.Close()


