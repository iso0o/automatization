import kivy
import paho.mqtt.client as mqtt
import threading

kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("igor", "3221")
mqtt_client.connect("192.168.43.17", 1883)

def mqtt_loop():
    mqtt_client.loop_forever()

mqtt_client.username_pw_set("igor", "3221")
mqtt_client.connect("192.168.43.17", 1883)

mqtt_thread = threading.Thread(target=mqtt_loop)
mqtt_thread.start()

Window.clearcolor = (1, 1, 1, 1)  # установка белого фона
Window.size = (1080, 2340)



class KettleScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(KettleScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для чайника
        kettle_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(kettle_layout)

        # добавляем  гиф-изображение чайника
        kettle_image = AsyncImage(source="kettle.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        kettle_layout.add_widget(kettle_image)

        kettle_label = Label(text="Вы выбрали чайник", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        kettle_layout.add_widget(kettle_label)

        # добавление кнопки "Назад"
        main_kitchen_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_kitchen_button.bind(on_press=self.go_to_kitchen)
        self.add_widget(main_kitchen_button)

    def go_to_kitchen(self, *args):
        # создание экземпляра класса Kitchen и отображение его на экране
        kitchen = Kitchen()
        self.clear_widgets()
        self.add_widget(kitchen)

class BurnerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(BurnerScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для конфорки
        burner_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(burner_layout)

        # добавляем  гиф-изображение конфорки
        burner_image = AsyncImage(source="burner.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        burner_layout.add_widget(burner_image)

        burner_label = Label(text="Вы выбрали конфорку", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        burner_layout.add_widget(burner_label)

        # добавление кнопки "Назад"
        main_kitchen_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_kitchen_button.bind(on_press=self.go_to_kitchen)
        self.add_widget(main_kitchen_button)

    def go_to_kitchen(self, *args):
        # создание экземпляра класса Kitchen и отображение его на экране
        kitchen = Kitchen()
        self.clear_widgets()
        self.add_widget(kitchen)

class FridgeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(FridgeScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для холодильника
        fridge_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(fridge_layout)

        # добавляем  гиф-изображение холодильника
        fridge_image = AsyncImage(source="fridge.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        fridge_layout.add_widget(fridge_image)

        fridge_label = Label(text="Вы выбрали холодильник", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        fridge_layout.add_widget(fridge_label)

        # добавление кнопки "Назад"
        main_kitchen_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_kitchen_button.bind(on_press=self.go_to_kitchen)
        self.add_widget(main_kitchen_button)

    def go_to_kitchen(self, *args):
        # создание экземпляра класса Kitchen и отображение его на экране
        kitchen = Kitchen()
        self.clear_widgets()
        self.add_widget(kitchen)

class DoorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(DoorScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для гаражной двери
        door_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(door_layout)

        # добавляем  гиф-изображение гаражной двери
        door_image = AsyncImage(source="door.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        door_layout.add_widget(door_image)

        door_label = Label(text="Вы выбрали гаражную дверь", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        door_layout.add_widget(door_label)

        # добавление кнопки "Назад"
        main_garage_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_garage_button.bind(on_press=self.go_to_garage)
        self.add_widget(main_garage_button)

    def go_to_garage(self, *args):
        # создание экземпляра класса Garage и отображение его на экране
        garage = Garage()
        self.clear_widgets()
        self.add_widget(garage)

class ColumnScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ColumnScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для колонки
        column_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(column_layout)

        # добавляем  гиф-изображение колонки
        column_image = AsyncImage(source="column.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        column_layout.add_widget(column_image)

        column_label = Label(text="Вы выбрали колонку", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        column_layout.add_widget(column_label)

        # добавление кнопки "Назад"
        main_garage_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_garage_button.bind(on_press=self.go_to_garage)
        self.add_widget(main_garage_button)

    def go_to_garage(self, *args):
        # создание экземпляра класса Garage и отображение его на экране
        garage = Garage()
        self.clear_widgets()
        self.add_widget(garage)

class LightScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LightScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для света
        light_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(light_layout)

        # добавляем  гиф-изображение света
        light_image = AsyncImage(source="light.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        light_layout.add_widget(light_image)

        light_label = Label(text="Вы выбрали свет", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        light_layout.add_widget(light_label)

        # добавление кнопки "Назад"
        main_bedroom_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_bedroom_button.bind(on_press=self.go_to_bedroom)
        self.add_widget(main_bedroom_button)

    def go_to_bedroom(self, *args):
        # создание экземпляра класса Bedroom и отображение его на экране
        bedroom = Bedroom()
        self.clear_widgets()
        self.add_widget(bedroom)

class HumidifierScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HumidifierScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для увлажнителя воздуха
        humidifier_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(humidifier_layout)

        # добавляем  гиф-изображение увлажнителя воздуха
        humidifier_image = AsyncImage(source="humidifier.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        humidifier_layout.add_widget(humidifier_image)

        humidifier_label = Label(text="Вы выбрали увлажнитель воздуха", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        humidifier_layout.add_widget(humidifier_label)

        # добавление кнопки "Назад"
        main_bedroom_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_bedroom_button.bind(on_press=self.go_to_bedroom)
        self.add_widget(main_bedroom_button)

    def go_to_bedroom(self, *args):
        # создание экземпляра класса Bedroom и отображение его на экране
        bedroom = Bedroom()
        self.clear_widgets()
        self.add_widget(bedroom)

class TempcontrScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(TempcontrScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для датчика температуры воды
        tempcontr_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(tempcontr_layout)

        # добавляем  гиф-изображение датчика температуры воды
        tempcontr_image = AsyncImage(source="tempcontr.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        tempcontr_layout.add_widget(tempcontr_image)

        tempcontr_label = Label(text="Вы выбрали терморегулятор", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        tempcontr_layout.add_widget(tempcontr_label)

        # добавление кнопки "Назад"
        main_bathroom_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_bathroom_button.bind(on_press=self.go_to_bathroom)
        self.add_widget(main_bathroom_button)

    def go_to_bathroom(self, *args):
        # создание экземпляра класса Bathroom и отображение его на экране
        bathroom = Bathroom()
        self.clear_widgets()
        self.add_widget(bathroom)

class WashingScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(WashingScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для стиральной машины
        washing_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(washing_layout)

        # добавляем  гиф-изображение стиральной машины
        washing_image = AsyncImage(source="washing.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        washing_layout.add_widget(washing_image)

        washing_label = Label(text="Вы выбрали стиральную машину", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        washing_layout.add_widget(washing_label)

        # добавление кнопки "Назад"
        main_bathroom_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_bathroom_button.bind(on_press=self.go_to_bathroom)
        self.add_widget(main_bathroom_button)

    def go_to_bathroom(self, *args):
        # создание экземпляра класса Bathroom и отображение его на экране
        bathroom = Bathroom()
        self.clear_widgets()
        self.add_widget(bathroom)

class TvScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(TvScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для телевизора
        tv_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(tv_layout)

        # добавляем  гиф-изображение телевизора
        tv_image = AsyncImage(source="tv.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        tv_layout.add_widget(tv_image)

        tv_label = Label(text="Вы выбрали телевизор", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        tv_layout.add_widget(tv_label)

        # добавление кнопки "Назад"
        main_living_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_living_button.bind(on_press=self.go_to_living)
        self.add_widget(main_living_button)

    def go_to_living(self, *args):
        # создание экземпляра класса Living Room и отображение его на экране
        living = Living()
        self.clear_widgets()
        self.add_widget(living)

class KondScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(KondScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для кондиционера
        kond_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(kond_layout)

        # добавляем  гиф-изображение кондиционера
        kond_image = AsyncImage(source="kond.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        kond_layout.add_widget(kond_image)

        kond_label = Label(text="Вы выбрали кондиционер", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        kond_layout.add_widget(kond_label)

        # добавление кнопки "Назад"
        main_living_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_living_button.bind(on_press=self.go_to_living)
        self.add_widget(main_living_button)

    def go_to_living(self, *args):
        # создание экземпляра класса Living Room и отображение его на экране
        living = Living()
        self.clear_widgets()
        self.add_widget(living)

class AirfreshScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(AirfreshScreen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для освежителя воздуха
        airfresh_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(airfresh_layout)

        # добавляем  гиф-изображение освежителя воздуха
        airfresh_image = AsyncImage(source="airfresh.gif", size_hint=(None, None), anim_delay= 1/5 , size=(100, 100),pos_hint={'center_x': 0.5})
        airfresh_layout.add_widget(airfresh_image)

        airfresh_label = Label(text="Вы выбрали освежитель воздуха", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        airfresh_layout.add_widget(airfresh_label)

        # добавление кнопки "Назад"
        main_living_button = Button(text="Назад", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_living_button.bind(on_press=self.go_to_living)
        self.add_widget(main_living_button)

    def go_to_living(self, *args):
        # создание экземпляра класса Living Room и отображение его на экране
        living = Living()
        self.clear_widgets()
        self.add_widget(living)

class Kitchen(BoxLayout):
    def __init__(self, **kwargs):
        super(Kitchen, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        kitchen_label = Label(text="Кухня", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'x': 0, 'y': 1})
        self.add_widget(kitchen_label)

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для чайника
        kettle_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(kettle_layout)

        # добавляем изображение чайника
        kettle_image = Image(source="kettle.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        kettle_layout.add_widget(kettle_image)

        # добавляем надпись "чайник"
        kettle_label = Label(text="Чайник", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        kettle_layout.add_widget(kettle_label)

        # добавляем кнопки для чайника
        kettle_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                      pos_hint={'center_x': 0.5})
        kettle_layout.add_widget(kettle_buttons_layout)

        kettle_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                              color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        kettle_on_button.bind(on_press=self.turn_on_kettle)
        kettle_buttons_layout.add_widget(kettle_on_button)

        # добавляем контейнер для конфорки
        burner_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(burner_layout)

        # добавляем изображение конфорки
        burner_image = Image(source="burner.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        burner_layout.add_widget(burner_image)

        # добавляем надпись "Конфорка"
        burner_label = Label(text="Конфорка", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                           size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        burner_layout.add_widget(burner_label)

        # добавляем кнопки для конфорки
        burner_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5})
        burner_layout.add_widget(burner_buttons_layout)

        burner_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        burner_on_button.bind(on_press=self.turn_on_burner)
        burner_buttons_layout.add_widget(burner_on_button)

        # добавляем контейнер для холодильника
        fridge_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(fridge_layout)

        # добавляем изображение холодильника
        fridge_image = Image(source="fridge.png", size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5})
        fridge_layout.add_widget(fridge_image)

        # добавляем надпись "Холодильник"
        fridge_label = Label(text="Холодильник", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                               size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        fridge_layout.add_widget(fridge_label)

        # добавляем кнопки для холодильника
        fridge_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                            pos_hint={'center_x': 0.5})
        fridge_layout.add_widget(fridge_buttons_layout)

        fridge_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                    color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        fridge_on_button.bind(on_press=self.turn_on_fridge)
        fridge_buttons_layout.add_widget(fridge_on_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_kettle(self, instance):
        kettle = KettleScreen()
        self.clear_widgets()
        self.add_widget(kettle)

    def turn_on_burner(self, instance):
        burner = BurnerScreen()
        self.clear_widgets()
        self.add_widget(burner)

    def turn_on_fridge(self, instance):
        fridge = FridgeScreen()
        self.clear_widgets()
        self.add_widget(fridge)

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)

class Garage(BoxLayout):
    def __init__(self, **kwargs):
        super(Garage, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        garage_label = Label(text="Гараж", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'x': 0, 'y': 1})
        self.add_widget(garage_label)

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для гаражной двери
        door_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(door_layout)

        # добавляем изображение гаражной двери
        door_image = Image(source="door.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        door_layout.add_widget(door_image)

        # добавляем надпись "гаражная дверь"
        door_label = Label(text="Гаражная дверь", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        door_layout.add_widget(door_label)

        # добавляем кнопки для гаражной двери
        door_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                      pos_hint={'center_x': 0.5})
        door_layout.add_widget(door_buttons_layout)

        door_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                              color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        door_on_button.bind(on_press=self.turn_on_door)
        door_buttons_layout.add_widget(door_on_button)

        # добавляем контейнер для колонки
        column_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(column_layout)

        # добавляем изображение колонки
        column_image = Image(source="column.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        column_layout.add_widget(column_image)

        # добавляем надпись "Колонка"
        column_label = Label(text="Колонка", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                           size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        column_layout.add_widget(column_label)

        # добавляем кнопки для колонки
        column_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5})
        column_layout.add_widget(column_buttons_layout)

        column_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        column_on_button.bind(on_press=self.turn_on_column)
        column_buttons_layout.add_widget(column_on_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_door(self, instance):
        door = DoorScreen()
        self.clear_widgets()
        self.add_widget(door)

    def turn_on_column(self, instance):
        column = ColumnScreen()
        self.clear_widgets()
        self.add_widget(column)

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)

class Bedroom(BoxLayout):
    def __init__(self, **kwargs):
        super(Bedroom, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        bedroom_label = Label(text="Спальня", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'x': 0, 'y': 1})
        self.add_widget(bedroom_label)

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для света
        light_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(light_layout)

        # добавляем изображение света
        light_image = Image(source="light.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        light_layout.add_widget(light_image)

        # добавляем надпись "Свет"
        light_label = Label(text="Свет", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        light_layout.add_widget(light_label)

        # добавляем кнопки для света
        light_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                      pos_hint={'center_x': 0.5})
        light_layout.add_widget(light_buttons_layout)

        light_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                              color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        light_on_button.bind(on_press=self.turn_on_light)
        light_buttons_layout.add_widget(light_on_button)

        # добавляем контейнер для увлажнителя воздуха
        humidifier_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(humidifier_layout)

        # добавляем изображение увлажнителя воздуха
        humidifier_image = Image(source="humidifier.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        humidifier_layout.add_widget(humidifier_image)

        # добавляем надпись "Увлажнитель воздуха"
        humidifier_label = Label(text="Увлажнитель воздуха", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                           size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        humidifier_layout.add_widget(humidifier_label)

        # добавляем кнопки для увлажнителя воздуха
        humidifier_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5})
        humidifier_layout.add_widget(humidifier_buttons_layout)

        humidifier_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        humidifier_on_button.bind(on_press=self.turn_on_humidifier)
        humidifier_buttons_layout.add_widget(humidifier_on_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_light(self, instance):
        light = LightScreen()
        self.clear_widgets()
        self.add_widget(light)

    def turn_on_humidifier(self, instance):
        humidifier = HumidifierScreen()
        self.clear_widgets()
        self.add_widget(humidifier)

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)

class Bathroom(BoxLayout):
    def __init__(self, **kwargs):
        super(Bathroom, self).__init__(**kwargs)
        self.orientation = "vertical"  # задаем ориентацию элементов

        bathroom_label = Label(text="Санузел", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'x': 0, 'y': 1})
        self.add_widget(bathroom_label)

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для датчика температуры воды
        tempcontr_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(tempcontr_layout)

        # добавляем изображение датчика температуры воды
        tempcontr_image = Image(source="tempcontr.jpg", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        tempcontr_layout.add_widget(tempcontr_image)

        # добавляем надпись "Датчика температуры воды"
        tempcontr_label = Label(text="Терморегулятор", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'center_x': 0.5})
        tempcontr_layout.add_widget(tempcontr_label)

        # добавляем кнопки для датчика температуры воды
        tempcontr_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                      pos_hint={'center_x': 0.5})
        tempcontr_layout.add_widget(tempcontr_buttons_layout)

        tempcontr_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                              color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        tempcontr_on_button.bind(on_press=self.turn_on_tempcontr)
        tempcontr_buttons_layout.add_widget(tempcontr_on_button)

        # добавляем контейнер для стиральной машины
        washing_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(washing_layout)

        # добавляем изображение стиральной машины
        washing_image = Image(source="washing.png", size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.5})
        washing_layout.add_widget(washing_image)

        # добавляем надпись "стиральная машина"
        washing_label = Label(text="Стиральная машина", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                           size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        washing_layout.add_widget(washing_label)

        # добавляем кнопки для стиральной машины
        washing_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5})
        washing_layout.add_widget(washing_buttons_layout)

        washing_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        washing_on_button.bind(on_press=self.turn_on_washing)
        washing_buttons_layout.add_widget(washing_on_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100), pos_hint={'x': 0, 'y': 0.1})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_tempcontr(self, instance):
        tempcontr = TempcontrScreen()
        self.clear_widgets()
        self.add_widget(tempcontr)

    def turn_on_washing(self, instance):
        washing = WashingScreen()
        self.clear_widgets()
        self.add_widget(washing)

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)

class Living(BoxLayout):
    def __init__(self, **kwargs):
        super(Living, self).__init__(**kwargs)
        self.orientation = "vertical" # задаем ориентацию элементов

        living_label = Label(text="Гостиная", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None),
                         size=(100, 50), pos_hint={'x': 0, 'y': 1})
        self.add_widget(living_label)

        # добавляем вертикальный BoxLayout для изображений и надписей
        images_labels_layout = BoxLayout(size_hint=(1, 0.8), padding=200, spacing=150)
        self.add_widget(images_labels_layout)

        # добавляем контейнер для телевизора
        tv_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(tv_layout)

        # добавляем изображение телевизора
        tv_image = Image(source="tv.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        tv_layout.add_widget(tv_image)

        # добавляем надпись "Телевизор"
        tv_label = Label(text="Телевизор", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        tv_layout.add_widget(tv_label)

        # добавляем кнопки для телевизора
        tv_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        tv_layout.add_widget(tv_buttons_layout)

        tv_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                           color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        tv_on_button.bind(on_press=self.turn_on_tv)
        tv_buttons_layout.add_widget(tv_on_button)

        # добавляем контейнер для кондиционера
        kond_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(kond_layout)

        # добавляем изображение кондиционера
        kond_image = Image(source="kond.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        kond_layout.add_widget(kond_image)

        # добавляем надпись "Кондиционер"
        kond_label = Label(text="Кондиционер", font_size='20sp', bold=True, color=(0, 0, 0, 100),
                           size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        kond_layout.add_widget(kond_label)

        # добавляем кнопки для кондиционера
        kond_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50),
                                        pos_hint={'center_x': 0.5})
        kond_layout.add_widget(kond_buttons_layout)

        kond_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                                color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        kond_on_button.bind(on_press=self.turn_on_kond)
        kond_buttons_layout.add_widget(kond_on_button)

        # добавляем контейнер для освежителя воздуха
        airfresh_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150))
        images_labels_layout.add_widget(airfresh_layout)

        # добавляем изображение освежителя воздуха
        airfresh_image = Image(source="airfresh.png", size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        airfresh_layout.add_widget(airfresh_image)

        # добавляем надпись "освежитель воздуха"
        airfresh_label = Label(text="Освежитель воздуха", font_size='20sp', bold=True, color=(0, 0, 0, 100), size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        airfresh_layout.add_widget(airfresh_label)

        # добавляем кнопки для освежителя воздуха
        airfresh_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        airfresh_layout.add_widget(airfresh_buttons_layout)

        airfresh_on_button = Button(text="Выбрать", font_size='14sp', size_hint=(None, None), size=(200, 50),
                           color=(1, 1, 1, 100), background_color=(0, 1, 0, 1))
        airfresh_on_button.bind(on_press=self.turn_on_airfresh)
        airfresh_buttons_layout.add_widget(airfresh_on_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100),pos_hint = {'x': 0, 'y': 0.1})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_tv(self, instance):
        tv = TvScreen()
        self.clear_widgets()
        self.add_widget(tv)

    def turn_on_kond(self, instance):
        kond = KondScreen()
        self.clear_widgets()
        self.add_widget(kond)

    def turn_on_airfresh(self, instance):
        airfresh = AirfreshScreen()
        self.clear_widgets()
        self.add_widget(airfresh)

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)

class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        # установка ориентации и размера BoxLayout
        self.orientation = 'vertical'
        self.size_hint = (1, 1)

        # создание и добавление надписи "Умный дом"
        label = Label(text="Приложение - Умный дом", font_size='20sp', bold=True, color=(0, 0, 0, 100))
        self.add_widget(label)

        # создание и добавление кнопки "Кухня"
        kitchen_button = Button(text="Кухня", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 1, 1))
        kitchen_button.bind(on_press=self.go_to_kitchen)
        self.add_widget(kitchen_button)

        # создание и добавление кнопки "Гостиная"
        living_button = Button(text="Гостиная", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 1, 1))
        living_button.bind(on_press=self.go_to_living)
        self.add_widget(living_button)

        # создание и добавление кнопки "Гараж"
        garage_button = Button(text="Гараж", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 1, 1))
        garage_button.bind(on_press=self.go_to_garage)
        self.add_widget(garage_button)

        # создание и добавление кнопки "Спальня"
        bedroom_button = Button(text="Спальня", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 1, 1))
        bedroom_button.bind(on_press=self.go_to_bedroom)
        self.add_widget(bedroom_button)

        # создание и добавление кнопки "Санузел"
        bathroom_button = Button(text="Санузел", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 1, 1))
        bathroom_button.bind(on_press=self.go_to_bathroom)
        self.add_widget(bathroom_button)

        # создание и добавление кнопки выхода
        exit_button = Button(text="Выход", font_size='14sp',color=(1, 1, 1, 100),background_color=(0, 0, 0, 100))
        exit_button.bind(on_press=self.exit_app)
        self.add_widget(exit_button)

    def go_to_kitchen(self, *args):
        # создание экземпляра класса Kitchen и отображение его на экране
        kitchen = Kitchen()
        self.clear_widgets()
        self.add_widget(kitchen)

    def go_to_living(self, *args):
        # создание экземпляра класса Living Room и отображение его на экране
        living = Living()
        self.clear_widgets()
        self.add_widget(living)

    def go_to_garage(self, *args):
        # создание экземпляра класса Garage и отображение его на экране
        garage = Garage()
        self.clear_widgets()
        self.add_widget(garage)

    def go_to_bedroom(self, *args):
        # создание экземпляра класса Bedroom и отображение его на экране
        bedroom = Bedroom()
        self.clear_widgets()
        self.add_widget(bedroom)

    def go_to_bathroom(self, *args):
        # создание экземпляра класса Bathroom и отображение его на экране
        bathroom = Bathroom()
        self.clear_widgets()
        self.add_widget(bathroom)

    def exit_app(self, *args):
        App.get_running_app().stop()  # остановка приложения
        mqtt_client.disconnect()
        mqtt_thread.join()

class MyApp(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    MyApp().run()