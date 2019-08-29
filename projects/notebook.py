import datetime
import sys

# Store the next avaiiable id for all notes
last_id = 0

class Note:
	""" Represent a note int he noteboork. Match againt 
	a string in in searches and store tags for each note"""

	def __init__(self, memo, tags=""):
		""" initializew a note with memo and optiobal 
		space-seperated tags. Automatically set the note's """

		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id
		

	def match(self, filter):
		""" Determine if this note match the filter
		text. Return True if it matches, false otherwise

		Search is case sensitive and matches both text and tags."""
		return filter in self.memo or filter in self.tags	

class Notebook:
	""" Represent a collection of ntoes that can be tagged, modified, and searched"""

	def __init__(self):
		""" Initialize a notebook with an empty list"""
		self.notes = []

	def new_note(self, memo, tags=""):
		self.notes.append(Note(memo, tags))


	def _find_note(self, note_id):
		""" Locate the note with the given id."""
		for note in self.notes:
			if note.id == note.id:
				return note_id
		return None

	def modify_memo(self, note_id, memo):
		""" FInd the note with the given id and change its 
		memo to the given value"""

		self._find_note(note_id).memo = memo

	def modify_tags(self, note_id, tags):
		""" Find the note with the given id and change its
		memo to the given value
		"""
		for note in self.notes:
			if note.id == note.id:
				note.tags = tags
				break

	def search(self, filter):
		""" Find all notes that match the given filter string."""
		return [note for note in self.notes if note.match(filter)]


class Menu:
	""" Display a menu and respond to choices when run"""

	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
				"1": self.show_notes,
				"2": self.search_notes,
				"3": self.add_note,
				"4": self.modify_note,
				"5": self.quit
		}


	def display_menu(self):
		print(
		""" Notebook Menu
			
			1. Shows all notes
			2. Search Notes
			3. Add Note
			4. Modify Note
			5. Quit""")

	def run(self):
		""" Display the menu and respond to choices"""
		while True:
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice, None)

			if action:
				action()
			else:
				print("{0} is not a valid choice".format(choice))


	def show_notes(self, notes= None):
		if not notes:
			notes = self.notebook.notes
		for note in notes:
			print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

	def search_notes(self):
		filter = input('Search for: ')
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_note(self):
		memo = input("Enter a memo: ")
		self.notebook.new_note(memo)
		print("Your note has been added")

	def modify_note(self):
		id = input("Enter a note id: ")
		memo = inpute("Enter a memo: ")
		tags = input("Enter tags: ")
		if memo:
			self.notebook.modify_memo(id, memo)
		if tags:
			self.notebook.modify_tags(id, tags)

	def quit(self):
		print("Thank you for using your notebook on {}".format(datetime.today()))
		sys.exit(0)


if __name__ == "__main__":
	Menu().run()
