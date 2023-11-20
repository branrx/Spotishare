#	Converts file stream to list object
def to_list_single(file):
	temp_list = list()
	temp_str = ''

	for f in file:
		if(f!='\n' and f!=' '):
			temp_str += f
			temp_list.append(temp_str.replace('\n', ''))
			temp_str = ''

	return temp_list

