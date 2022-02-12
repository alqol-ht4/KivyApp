"""
Յու բալիկներ։ Արամ ձաձյան պարապ ա ու իրա ստրուկտուրայի տարբերակն ա մշակել
եթե տենամ դժվարանում եք, ցույց կտամ։ Բայց մեկա մինչև վերջ գրել եմ տալու, նոր կասեմ ձեզ սրա մասին ։-)
"""


from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from models import get_lessons
from functools import partial
from random import choice

Window.size = (320, 600)

class ReciveFromDatabase:

	lessons_for_test_callback = {}
	
	lessons = get_lessons()
	items = []
	sources = []

	for tmp in lessons:
		items.append(tmp)
		sources.append(lessons[tmp])

	for i in range(len(items)):
		lessons_for_test_callback[sources[i]] = items[i]




class FirstLevelCallBacks:

	def item_callback(self, instance):
			
		print(ReciveFromDatabase().lessons_for_test_callback)

		source = ReciveFromDatabase().lessons_for_test_callback[instance.text]

		self.root.ids.lessons_screens_manager.current = 'lesson_decription_screen'

		self.root.ids.lesson_description_widget.add_widget(LessonDescriptionWidget(source = source, description = instance.text))




	def lesson_callback(self, instance, lesson_sources, lesson_items):

		self.root.ids.lessons_screens_manager.current = 'lessons_more_screen'
		
		for i in range(len(lesson_items)):
			self.root.ids.lessons_more_widget.add_widget(LessonDrawer(source = lesson_sources[i], description = lesson_items[i], method = self.item_callback))



	def test_callback(self, instance, lesson_sources, lesson_items):
		print(instance)
		print(lesson_sources)
		print(lesson_items)
		self.root.ids.test_screens_manager.current = 'tests_more_screen'
		for i in range(len(lesson_items)):
			self.root.ids.tests_more_widget.add_widget(TestDrawer(source = lesson_sources[i]))
			


class LessonDescriptionWidget(GridLayout):
	
		source = StringProperty()
		description = StringProperty()


class LessonDrawer(MDBoxLayout):

	source = StringProperty()
	description = StringProperty()
	method = ObjectProperty()


class LessonsHomeWidget(MDBoxLayout):
	pass


class LessonsMoreWidget(GridLayout):
	pass


class TestsHomeWidget(MDBoxLayout):
    pass

class TestsMoreWidget(MDBoxLayout):
    pass

class TestDrawer(MDBoxLayout):
    source = StringProperty()

class RootWidget(ScreenManager):
	pass


class MainApp(MDApp, FirstLevelCallBacks):

	window = Window.size[1]
 
	def lessons_back_button(self, instance):
		self.root.ids.lessons_more_widget.clear_widgets()
		self.root.ids.lessons_screens_manager.current = 'lessons_home_screen'


	def on_start(self):


		items = ReciveFromDatabase().sources
		sources = ReciveFromDatabase().items


		# Ստեղ լցնում ենք կնոպկեքը, խոսքը համ դասերի մասին ա, համ թեստերի և այլն


		lesson_1_button = Button(text = f'Lesson ')
		lesson_1_button.bind(on_press = partial(self.lesson_callback, lesson_sources =  sources, lesson_items = items))
		self.root.ids.lessons_home_widget.add_widget(lesson_1_button)
  

		test_1_button = Button(text = f'Test')
		test_1_button.bind(on_press = partial(self.test_callback,  lesson_sources =  sources, lesson_items = items))
		self.root.ids.tests_home_widget.add_widget(test_1_button)



	def build(self):
		pass



if __name__ == '__main__':
	MainApp().run()