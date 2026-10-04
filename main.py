from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.camera import Camera
from kivy.lang import Builder
import json, os

DATA_FILE = "products.json"

def load_products():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [
        {"name": "شاحن 65 واط سريع", "price": "8500", "barcode": "1001"},
        {"name": "سماعة بلوتوث رويال", "price": "12000", "barcode": "1002"}
    ]

def save_all(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

KV = '''
ScreenManager:
    MainScreen:
    AddScreen:
    ScannerScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color: rgba: 0.05,0.05,0.07,1
            Rectangle: pos: self.pos; size: self.size
        Label:
            text: 'رويال كوش \\nللتجهيزات الكهربائية'
            font_size: '22sp'
            color: 0.9,0.76,0.33,1
            size_hint_y: 0.2
            halign: 'center'
        ScrollView:
            BoxLayout:
                id: box_list
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: 8
        BoxLayout:
            size_hint_y: 0.12
            spacing: 10
            Button:
                text: 'اضافة صنف جديد +'
                background_color: 0.9,0.76,0.33,1
                on_press: app.root.current = 'add'
            Button:
                text: 'مسح باركود'
                background_color: 0.2,0.5,0.9,1
                on_press: app.root.current = 'scanner'

<AddScreen>:
    name: 'add'
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 12
        Label:
            text: 'اضافة / تعديل صنف'
            color: 0.9,0.76,0.33,1
            font_size: '20sp'
            size_hint_y: 0.15
        TextInput:
            id: t_name
            hint_text: 'اسم الصنف'
            multiline: False
            font_size: '16sp'
        TextInput:
            id: t_price
            hint_text: 'السعر بالجنيه'
            input_filter: 'float'
            multiline: False
        TextInput:
            id: t_barcode
            hint_text: 'رقم الباركود'
            multiline: False
        Button:
            text: 'حفظ'
            background_color: 0,0.7,0.3,1
            size_hint_y: 0.18
            on_press: root.save_item()
        Button:
            text: 'رجوع للقائمة'
            size_hint_y: 0.12
            on_press: app.root.current = 'main'

<ScannerScreen>:
    name: 'scanner'
    BoxLayout:
        orientation: 'vertical'
        Camera:
            id: cam
            resolution: (640,480)
            play: True
        Label:
            text: 'وجه الكاميرا للباركود ثم اكتب الرقم'
            size_hint_y: 0.15
        BoxLayout:
            size_hint_y: 0.15
            spacing: 5
            TextInput:
                id: t_scan
                hint_text: 'رقم الباركود هنا'
                multiline: False
            Button:
                text: 'استخدام'
                on_press: root.use_code()
        Button:
            text: 'رجوع'
            size_hint_y: 0.1
            on_press: app.root.current = 'main'
'''

class MainScreen(Screen):
    def on_enter(self):
        box = self.ids.box_list
        box.clear_widgets()
        for idx, p in enumerate(load_products()):
            row = BoxLayout(size_hint_y=None, height=80, spacing=5)
            row.add_widget(Label(text=f"{p['name']}\nالسعر: {p['price']} - باركود: {p['barcode']}", font_size='13sp'))
            b1 = Button(text='تعديل', size_hint_x=0.25, background_color=(0.9,0.76,0.33,1))
            b1.bind(on_press=lambda x, i=idx: self.edit(i))
            b2 = Button(text='حذف', size_hint_x=0.2, background_color=(0.9,0.2,0.2,1))
            b2.bind(on_press=lambda x, i=idx: self.delete(i))
            row.add_widget(b1)
            row.add_widget(b2)
            box.add_widget(row)
    def edit(self, i):
        s = self.manager.get_screen('add')
        s.edit_index = i
        data = load_products()[i]
        s.ids.t_name.text = data['name']
        s.ids.t_price.text = data['price']
        s.ids.t_barcode.text = data['barcode']
        self.manager.current = 'add'
    def delete(self, i):
        d = load_products()
        d.pop(i)
        save_all(d)
        self.on_enter()

class AddScreen(Screen):
    edit_index = None
    def save_item(self):
        name = self.ids.t_name.text.strip()
        price = self.ids.t_price.text.strip()
        barcode = self.ids.t_barcode.text.strip()
        if not name: return
        data = load_products()
        item = {"name": name, "price": price, "barcode": barcode}
        if self.edit_index is not None:
            data[self.edit_index] = item
            self.edit_index = None
        else:
            data.append(item)
        save_all(data)
        self.ids.t_name.text = ""
        self.ids.t_price.text = ""
        self.ids.t_barcode.text = ""
        self.manager.current = 'main'

class ScannerScreen(Screen):
    def use_code(self):
        code = self.ids.t_scan.text.strip()
        if code:
            self.manager.get_screen('add').ids.t_barcode.text = code
            self.ids.t_scan.text = ""
            self.manager.current = 'add'

class RoyalKushApp(App):
    def build(self):
        return Builder.load_string(KV)

RoyalKushApp().run()
