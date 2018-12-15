# This is just a simple application to reverse some text
# that gets returned from user-provided input.
# It was only written to support the ls, pwd and who commands.
# Valid 'reverse' commands will print the results from the above
# commands to screen, but in reverse so I can practice my python :)

import os

# start a listener and keep it open
while True:

	# receive input from the user
	recv = input('-> ')

	# quit the listener
	if recv == 'quit':
		quit()

	# store the contents of ls in a list called ls
	# the other variables are set so that manipulated
	# list data gets passed in and manipulated
	ls = list(os.listdir())
	new_ls = []
	new_ls_items = ''
	rev_ls = ''

	# loop through the contents of ls and append them
	# into a new list so they can be 'cleanly' reversed
	for item in ls:
		new_ls.append(item)

		# each item now needs to be created as its own list item
		for i in new_ls:
			new_ls_items = list(i)

		# reverse the items in the new list
		new_ls_items.reverse()

		# add the reversed items to the new variable for output later
		for j in new_ls_items:
			rev_ls += j

	# grab the username of the currently logged in user and create a list
	# then reverse the list
	who = list(os.getlogin())
	who.reverse()
	rev_who = ''

	# loop through the reversed list and add the items to new var for output later
	for item in who:
		rev_who += item

	# get the current working directory and created a list
	# then reverse the items in the new list
	pwd = list(os.getcwd())
	pwd.reverse()
	rev_pwd = ''

	# loop through the reversed list and add the items to new var for output later
	for item in pwd:
		rev_pwd += item

	# the following are the commands that our 'shell' will listen for
	# the appropriate new reversed list will be displayed as output
	# for verification and testing, the actual system commands are
	# available and will display their output to the user as well
	if recv == 'revpwd':
		print(rev_pwd)
	elif recv == 'revwho':
		print(rev_who)
	elif recv == 'revls':
		print(rev_ls)
	elif recv == 'pwd':
		print(os.getcwd())
	elif recv == 'who':
		print(os.getlogin())
	elif recv == 'ls':
		print(', '.join(os.listdir()))
	else:
		print(f'Command not found: \'{recv}\'')