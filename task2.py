from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, 
    QLabel, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QHBoxLayout, 
    QVBoxLayout, QFormLayout)
 
import json
 
app = QApplication([])

#==========================================#
'''Notes in json'''
notes = {
    "Welcome!" : {
        "text" : "This is the best note taking app in the world!",
        "tags" : ["good", "instructions"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)
#==========================================#
 
'''Application interface'''
# Application window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)
 
# Application window widgets
# List widget: List of notes
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')

# Buttons under the list of notes 
button_note_create = QPushButton('Create note') 
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')
 
# Creates a field to insert tags
field_tag = QLineEdit('') # Creates a blank field
field_tag.setPlaceholderText('Enter tag...') # Text prompt inside the field
field_text = QTextEdit() # Field for entering text

# Buttons for all the tags
button_add = QPushButton('Add to note')
button_del = QPushButton('Untag from note')
button_search = QPushButton('Search notes by tag')

# List widget: List of tags
list_tags = QListWidget()
list_tags_label = QLabel('List of tags')
 
# Arranging widgets by layout
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

#==========================================#

'''Application functionality'''
def show_note():
    # Get the text from the note with the title highlighted and display it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])
 
'''Run the application'''
# Connecting event processing
# When clicked, show the note
list_notes.itemClicked.connect(show_note)

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

#==========================================#

# Run the application
notes_win.show()
app.exec_()
