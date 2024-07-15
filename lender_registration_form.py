import re
import os
import json
import base64
import tempfile

from anvil._server import LazyMedia
from kivy.graphics import Color, Line
# from Crypto.SelfTest.Cipher.test_CBC import file_name
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from anvil import media
from io import BytesIO
from kivy.core.image import Image as CoreImage
from anvil.tables import app_tables
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
import sqlite3
from datetime import datetime
from kivy import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.menu import MDDropdownMenu
import sqlite3
from kivymd.uix.pickers import MDDatePicker
from kivy.utils import platform
from kivy.clock import mainthread
from datetime import datetime
import anvil.server
from kivy.uix.modalview import ModalView
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.spinner import MDSpinner
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from lender_dashboard import LenderDashboard

# anvil.server.connect("server_6MFSRHQN7TZHDVGRHE4DACOS-MSES5HYVGRJ5LJH4") #published

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission
    )

KV = '''
<WindowManager>:
    LenderScreen:
    LenderScreen1:
    LenderScreen2:
    LenderScreen3:
    LenderScreen4:
    LenderScreen5:
    LenderScreen_Edu_Intermediate:
    LenderScreen_Edu_Bachelors:
    LenderScreen_Edu_Masters:
    LenderScreen_Edu_PHD:
    LenderScreenInstitutionalForm1:
    LenderScreenInstitutionalForm2:
    LenderScreenInstitutionalForm3:
    LenderScreen6:
    LenderScreen7:
    LenderScreen8:
    LenderScreen9:
    LenderScreen10:
    LenderScreen11:
    LenderScreen12:
    LenderScreen13:
    LenderScreen14:
    LenderScreenIndividualBankForm1:
    LenderScreenIndividualBankForm2:

<CustomSpinnerOption@SpinnerOption>:
    background_color:0, 0, 1, 1  
    color: 1, 1, 1, 1
<LenderScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_to_dashboard()]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(18)
                padding: dp(30)
                size_hint_y: None  # Ensure the layout fits within the ScrollView
                height: self.minimum_height  # Dynamically adjust the height
                canvas:
                    Color:
                        rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    Line:
                        width: 0.7  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
    
               
                MDLabel:
                    text: 'Lender Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(10)
                
                MDTextField:
                    id: username
                    hint_text: ' Enter Full Name *'
                    multiline: False
                    halign: 'left'
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    mode: "rectangle"
    
    
                Spinner:
                    id: spinner_id
                    text: "Select Gender *"
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "47dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    color: 0, 0, 0, 1
                    # on_release: root.validate_spinner()                  
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
                        
                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    padding: dp(10)
                    height: "48dp"
                    width: dp(200) 
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8     
                    MDLabel:
                        id: date_textfield
                        text: "Enter Date Of Birth *"
                        helper_text: 'YYYY-MM-DD'
                        helper_text_mode: "on_error"
                        font_size: "15dp"
                        width: dp(300)
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        on_touch_down: root.on_date_touch_down()
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"
                    MDIconButton:
                        icon: 'calendar'
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        on_release: root.show_date_picker()
    
    
                MDTextField:
                    id: mobile_number
                    hint_text: ' Enter mobile number *'
                    multiline: False
                    input_type: 'number'  
                    on_touch_down: root.on_mobile_number_touch_down()
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    on_text: root.validate_mobile(self)
                    mode: "rectangle"
    
                MDTextField:
                    id: alternate_email
                    hint_text: 'Enter Alternate Email ID '
                    multiline: False
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color_normal: 0, 0, 0, 1
                    text_color_normal: 0, 0, 0, 1
                    helper_text_color_normal: 0, 0, 0, 1
                    helper_text:''
                    helper_text_mode:'on_error'
                    radius: [0, 0, 0,0]
                    mode: "rectangle"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    on_text: root.check_alternate_email(self)
    
    
                MDBoxLayout:
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "10dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
    
                    MDIconButton:
                        icon: 'upload'
                        id: upload_icon1
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('LenderScreen').check_and_open_file_manager1()
    
                    MDLabel:
                        id: upload_label1
                        text: 'Upload Profile Photo *'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label1
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(48), dp(50)
                        height: dp(36)
                        halign: 'right'
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
    
                MDTextField:
                    id: aadhar_number
                    hint_text: ' Enter Government ID1 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_text: root.on_aadhar_number_text(self.text)
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    on_text: root.validate_aadhar_number(self)
                    mode: "rectangle"
    
                MDBoxLayout:
                    id: GovID1
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "3dp"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
    
                    MDIconButton:
                        icon: 'upload'
                        id: upload_icon2
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('LenderScreen').check_and_open_file_manager2()
                        disabled: True
    
                    MDLabel:
                        id: upload_label2
                        text: 'Upload Govt ID1 *'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label2
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(50), dp(50)
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
    
                MDTextField:
                    id: pan_number
                    hint_text: 'Enter Government ID2 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_text: root.on_pan_number_text(self.text)
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    on_text: root.validate_pan_number(self)
                    mode: "rectangle"
    
    
                MDBoxLayout:
                    id: GovID2
                    orientation: 'horizontal'
                    padding: "10dp"
                    spacing: "3dp"
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "48dp"
                    width: dp(200)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 
    
                    MDIconButton:
                        id: upload_icon3
                        icon: 'upload'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_x: None
                        width: dp(24)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_release: app.root.get_screen('LenderScreen').check_and_open_file_manager3()
                        disabled: True
    
                    MDLabel:
                        id: upload_label3
                        text: 'Upload Govt ID2 *'
                        halign: 'left'
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black text color
                        size_hint_y: None
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
                    Image:
                        id: image_label3
                        source: ''
                        allow_stretch: True
                        keep_ratio: True
                        size_hint_y: None
                        size: dp(50), dp(50)
                        height: dp(36)
                        valign: 'middle'  # Align the label text vertically in the center
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        on_touch_down: root.on_image_click(self, args[1])
                MDLabel:
                    text: 'Please fill * mandatory details'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 1, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(username.text, spinner_id.text, date_textfield.text, mobile_number.text, alternate_email.text,aadhar_number.text, pan_number.text)                                   
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"



<LenderScreen3>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(15)
                padding: dp(30)
                size_hint_y: None
                height: self.minimum_height
       
                MDLabel:
                    text: 'Lender Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    height: dp(10)
                    font_name: "Roboto-Bold"
                MDLabel:
                    text: 'Address Information'
                    halign: 'left'
                    height: dp(20)
                    bold: True

                MDTextField:
                    id: street_address1
                    hint_text: 'Enter Street Address1 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    font_size: "15dp"
                    mode: "rectangle"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    radius: [0, 0, 0,0]
                    on_text: root.validate_street_address1(self)

                MDTextField:
                    id: street_address2
                    hint_text: 'Enter Street Address2 *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
                    on_text: root.validate_street_address2(self)

                Spinner:
                    id: spinner_id1
                    text: "Select Present Address *"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    height: "45dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    font_size: "15dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 


                Spinner:
                    id: spinner_id2
                    text: "Select Staying Address *"
                    helper_text: "How Long You Are Staying At This Address"
                    multiline: False
                    size_hint: 1, None
                    halign: "left"
                    font_size: "15dp"
                    height: "45dp"
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1   # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.8 

                MDTextField:
                    id: city
                    hint_text: 'Enter City Name *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    font_size: "15dp"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
                    on_text: root.validate_city(self)
                    

                MDTextField:
                    id: zip_code
                    hint_text: 'Enter postal/zipcode *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    input_type: 'number'
                    on_touch_down: root.on_mobile_number_touch_down()
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    on_text: root.validate_zip_code(self) 
                    radius: [0, 0, 0,0]
                    

                MDTextField:
                    id: state
                    hint_text: 'Enter State Name *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
                    on_text: root.validate_state(self)

                MDTextField:
                    id: country
                    hint_text: 'Enter Country Name *'
                    multiline: False
                    size_hint_y: None
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    mode: "rectangle"
                    radius: [0, 0, 0,0]
                    on_text: root.validate_country(self)
                
                MDLabel:
                    text: 'Please fill * mandatory details'
                    halign: 'left'
                    theme_text_color: "Custom"
                    text_color: 1, 0, 0, 1  # Black text color
                    size_hint_y: None
                    height: dp(36)
                    valign: 'middle'  # Align the label text vertically in the center
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(street_address1.text, street_address2.text, spinner_id1.text, spinner_id2.text, city.text, zip_code.text, state.text, country.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"




<LenderScreen5>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen3')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            MDBoxLayout:
                id: parent_layout_id
                orientation: 'vertical'
                spacing: dp(5)
                padding: dp(30)
                size_hint_y: None
                height: self.minimum_height
                # dropdown details
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(200)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
                    MDLabel:
                        text: 'Lender Registration Form'
                        halign: 'center'
                        font_size: "15dp"
                        font_name: "Roboto-Bold"
                        bold: True
        
                    MDLabel:
                        text: 'Education Details'
                        halign: 'center'
                        font_size: "15dp"
                        bold: True
        
        
                    MDLabel:
                        text: "Select Education Details:"
                        halign: 'left'
                        font_size: "15dp"
                        # font_name: "Roboto-Bold"
                        bold: True
                    # MDBoxLayout:
                    #     orientation: 'horizontal'
                    #     canvas.before:
                    #         Color:
                    #             rgba: 0.5, 0.5, 0.5, 1
                    #         Line:
                    #             rectangle: self.x, self.y, self.width, self.height
                    #             width: 0.7
                    Spinner:
                        id: spinner_id
                        text: "Please Select Education Details"
                        multiline: False
                        size_hint: 1 , None
                        font_size: "15dp"
                        halign: "left"
                        height:"40dp"
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        background_color: 0,0,0,0
                        background_normal:''
                        option_cls: 'CustomSpinnerOption'
                        color: 0, 0, 0, 1
                        on_text: root.update_education_details(spinner_id.text)
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rectangle: (self.x, self.y, self.width, self.height)
                        
                        # MDIconButton:
                        #     icon: 'downarrow'
                        #     theme_text_color: "Custom"
                        #     text_color: 0, 0, 0, 1  # Black text color
                        #     size_hint_x: None
                        #     width: dp(24)
                # 10th details            
                MDBoxLayout:
                    id: box_10th
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(200)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
                    
        
                    MDLabel:
                        text: "Upload 10th standard certificate *"
                        halign: 'left'
                        bold: True
                        # size_hint_y: None
                        # height: dp(50)
                        font_size: "15dp"
        
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(63)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager1()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                    # MDLabel:
                    #     id: image_label1
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label1
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            on_touch_down: root.on_image_click(self, args[1])
                            size: dp(50), dp(50)
                            height: dp(36)
                    GridLayout:
                        cols: 1
                        spacing:dp(10)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_lender_screen_10()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"
                            
                # intermediate/puc
                MDBoxLayout:
                    id: box_12th
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(350)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        
                    MDLabel:
                        text: 'Intermediate/PUC Education Details'
                        halign: 'center'
                        bold: True
                        font_size: "15dp"
                        
                    MDLabel:
                        text: "Upload 10th standard *"
                        halign: 'left'
                        bold: True
                        # size_hint_y: None
                        # height: dp(50)
                        font_size: "15dp"
        
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(63)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager2()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            font_size: "15dp"
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    # MDLabel:
                    #     id: image_label1
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label2
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            on_touch_down: root.on_image_click(self, args[1])
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Intermediate/PUC *"
                        halign: 'left'
                        bold: True
                        font_size: "15dp"
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager3()
        
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    # MDLabel:
                    #     id: image_label2
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label3
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            on_touch_down: root.on_image_click(self, args[1])
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_lender_screen_11()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "20dp"
                            font_name: "Roboto-Bold"
                #for btech
                MDBoxLayout:
                    id: box_bachelors
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(500)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    MDLabel:
                        text: 'Bachelors Education Details'
                        halign: 'center'
                        font_size: "15dp"
                        bold: True
                        
                    MDLabel:
                        text: "Upload 10th standard Certificate *"
                        halign: 'left'
                        bold: True
        
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager4()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'center'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label4
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            on_touch_down: root.on_image_click(self, args[1])
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    # MDLabel:
                    #     id: image_label1
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
                        
        
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager5()
        
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label5
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            on_touch_down: root.on_image_click(self, args[1])
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    # MDLabel:
                    #     id: image_label2
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Bachelors certificate *"
                        halign: 'left'
                        bold: True
        
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
        
        
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager6()
        
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label6
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    # MDLabel:
                    #     id: image_label3
                    #     text: ''
                    #     halign: 'center'
                    #     theme_text_color: "Custom"
                    #     text_color: 0, 0, 0, 1  # Black text color
                    #     valign: 'middle'  # Align the label text vertically in the center
                    #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_lender_screen_btech()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"
                #master details 
                MDBoxLayout:
                    id: box_masters
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(540)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    # MDCard:
                    #     orientation: "vertical"
                    #     size_hint: None, None
                    #     size: "280dp", "480dp"
                    #     pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    
                    MDLabel:
                        text: 'Masters Education Details'
                        halign: 'center'
                        bold: True
                        font_size: "15dp"
                    MDLabel:
                        text: "Upload 10th standard Certificate *"
                        halign: 'left'
                        bold: True
            
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager7()
            
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label7
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            on_touch_down: root.on_image_click(self, args[1])
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        # MDLabel:
                        #     id: image_label1
                        #     text: ''
                        #     halign: 'center'
                        #     theme_text_color: "Custom"
                        #     text_color: 0, 0, 0, 1  # Black text color
                        #     valign: 'middle'  # Align the label text vertically in the center
                        #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
                            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager8()
            
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label8
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            on_touch_down: root.on_image_click(self, args[1])
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        # MDLabel:
                        #     id: image_label2
                        #     text: ''
                        #     halign: 'left'
                        #     theme_text_color: "Custom"
                        #     text_color: 0, 0, 0, 1  # Black text color
                        #     valign: 'middle'  # Align the label text vertically in the center
                        #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Bachelors certificate *"
                        halign: 'left'
                        bold: True
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager9()
        
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label9
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            on_touch_down: root.on_image_click(self, args[1])
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        # MDLabel:
                        #     id: image_label3
                        #     text: ''
                        #     halign: 'center'
                        #     theme_text_color: "Custom"
                        #     text_color: 0, 0, 0, 1  # Black text color
                        #     valign: 'middle'  # Align the label text vertically in the center
                        #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
                    MDLabel:
                        text: "Upload Masters Certificate *"
                        halign: 'left'
                        bold: True
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager10()
            
                        MDLabel:
                            id: upload_label4
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label10
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        # MDLabel:
                        #     id: image_label4
                        #     text: ''
                        #     halign: 'center'
                        #     theme_text_color: "Custom"
                        #     text_color: 0, 0, 0, 1  # Black text color
                        #     valign: 'middle'  # Align the label text vertically in the center
                        #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_lender_screen_mas()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"            
                
                #PHD details
                MDBoxLayout:
                    id: box_phd
                    orientation: 'vertical'
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(620)
                    # md_bg_color:253/255, 254/255, 254/255, 1
                    # canvas:
                    #     Color:
                    #         rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                    #     Line:
                    #         width: 0.7  # Border width
                    #         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                    # MDCard:
                    #     orientation: "vertical"
                    #     size_hint: None, None
                    #     size: "280dp", "550dp"
                    #     pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    MDLabel:
                        text: 'PHD Education Details'
                        halign: 'center'
                        bold: True
                    # MDLabel:
                    #     text: ''
                    #     halign: 'center'
                    #     bold: True
                    MDLabel:
                        text: "Upload 10th standard Certificate *"
                        halign: 'left'
                        bold: True
                    
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager11()
        
                        MDLabel:
                            id: upload_label1
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label11
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                
                    MDLabel:
                        text: "Upload Intermediate/PUC Certificate *"
                        halign: 'left'
                        bold: True
        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager12()
            
                        MDLabel:
                            id: upload_label2
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label12
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            on_touch_down: root.on_image_click(self, args[1])
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Bachelors certificate *"
                        halign: 'left'
                        bold: True
            
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager13()
            
                        MDLabel:
                            id: upload_label3
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label13
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: "Upload Masters Certificate *"
                        halign: 'left'
                        bold: True
            
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager14()
        
                        MDLabel:
                            id: upload_label4
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
                        Image:
                            id: image_label14
                            on_touch_down: root.on_image_click(self, args[1])
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            
                    MDLabel:
                        text: "Upload PHD Certificate *"
                        halign: 'left'
                        bold: True
            
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        # size_hint: None, None
                        # size: dp(250), dp(60)  # Adjust size as needed
                        # pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1 
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
            
                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen5').check_and_open_file_manager15()
                        MDLabel:
                            id: upload_label5
                            text: 'Upload Certificate'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label15
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    GridLayout:
                        cols: 1
                        spacing:dp(15)
                        padding: [0, "30dp", 0, 0]
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.go_to_lender_screen_phd()
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"

<CustomSpinnerOption@SpinnerOption>:
    background_color:0, 0, 1, 1  
    color: 1, 1, 1, 1  # Change the text color if needed

<LenderScreen6>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen5')]]
            right_action_items: [["icon8.png", lambda x: root.account()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            MDBoxLayout:
                id: parent_layout_id
                orientation: 'vertical'
                spacing: dp(18)
                padding: dp(30)
                size_hint_y: None
                height: dp(220)
                height: self.minimum_height
                MDLabel:
                    text: 'Lender Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"

                MDTextField:
                    id: investment
                    hint_text: ' Enter investment Amount *'
                    multiline: False
                    helper_text_mode: 'on_focus'
                    height: self.minimum_height
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                    line_color_focus: 0, 0, 0, 1
                    on_text: root.validate_zip_code(self)
                    radius: [0, 0, 0,0]
                    mode: "rectangle"

                Spinner:
                    id: lending_period
                    text: "Select Lending Period"
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1, None
                    height: "40dp"
                    width: dp(180)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1  #0.043, 0.145, 0.278, 1
                    option_cls: 'CustomSpinnerOption'
                    canvas:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.7 

                # dropdown details

                Spinner:
                    id: loan_type
                    text: "Select Loan Type"
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1, None
                    height: "40dp"
                    width: dp(180)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1  #0.043, 0.145, 0.278, 1
                    option_cls: 'CustomSpinnerOption'
                    on_text: root.update_person_details(loan_type.text)
                    canvas.before:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 0.7

                # Employee Details
                MDBoxLayout:
                    id: employee_details_box
                    orientation: 'vertical'
                    spacing: dp(18)
                    #padding: dp(10)
                    size_hint_y: None
                    height: dp(930)

                    MDLabel:
                        text: 'Employment Details '
                        halign: 'center'
                        size_hint_y: None
                        height: dp(20)
                        bold: True

                    MDTextField:
                        id:company_name
                        hint_text: ' Enter company name *'
                        on_text: root.validate_zip_code_text(self)
                        multiline: False
                        height: self.minimum_height
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    Spinner:
                        id: organisation_type
                        text: " Select Organisation Type *"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1, None
                        halign: "left"
                        height: "48dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        text_size: self.width - dp(20), None
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7 

                    #screen14

                    Spinner:
                        id: occupation_type
                        text: "Select Occupation type *"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1, None
                        halign: "left"
                        height: "48dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        text_size: self.width - dp(20), None
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'
                        # on_text: root.self_employment(spinner.text)
                        canvas.before:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7
                    MDTextField:              
                        id:company_address
                        hint_text: ' Enter company address *'
                        on_text: root.validate_zip_code_numchar(self)
                        multiline: False
                        height: self.minimum_height
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle" 

                    MDTextField:              
                        id:landmark
                        hint_text: ' Enter landmark *'
                        on_text: root.validate_zip_code_numchar(self)
                        multiline: False
                        height: self.minimum_height
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    Spinner:
                        id: employment_type
                        text: " Select Employment Type *"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1, None
                        halign: "left"
                        height: "48dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        text_size: self.width - dp(20), None
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'

                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7 

                    #screen13
                    MDTextField:              
                        id: annual_salary
                        hint_text: ' Enter Annual Salary *'
                        on_text: root.validate_zip_code(self)
                        multiline: False
                        height: self.minimum_height
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    Spinner:
                        id: salary_type
                        text: " Select Salary type *"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1, None
                        halign: "left"
                        height: "48dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        text_size: self.width - dp(20), None
                        color: 0, 0, 0, 1
                        option_cls: 'CustomSpinnerOption'
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7 
                    MDTextField:              
                        id: designation
                        hint_text: ' Enter Designation *'
                        on_text: root.validate_zip_code_text(self)
                        multiline: False
                        height: self.minimum_height
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        size_hint: 1, None
                        halign: "left"
                        font_size: "15dp"
                        height: "60dp"
                        width: dp(200)
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.8 

                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen6').check_and_open_file_manager_emp1()

                        MDLabel:
                            id: upload_label1
                            text: 'Upload Employee ID'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                        Image:
                            id: image_label1
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_touch_down: root.on_image_click(self, args[1])

                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        size_hint: 1, None
                        halign: "left"
                        font_size: "15dp"
                        height: "70dp"
                        width: dp(200)
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.8 

                        MDIconButton:
                            icon: 'upload'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen6').check_and_open_file_manager_emp2()

                        MDLabel:
                            id: upload_label2
                            text: 'Upload Last 6 months Bank Statements'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(42)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                        Image:
                            id: image_label2
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_touch_down: root.on_image_click(self, args[1])


                    MDTextField:              
                        id:business_number
                        hint_text: ' Enter Company Phone Number *'
                        multiline: False
                        height: self.minimum_height
                        on_text: root.validate_zip_code(self)
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        line_color_normal: 0, 0, 0, 1  # Red color for the line when not focused
                        line_color_focus: 0, 0, 0, 1
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    MDLabel:
                        id: error_message
                        text: "Pleas fill all details! *"
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 150, 0, 0, 1
                        halign: "left" 

                    GridLayout:
                        cols: 1
                        spacing:dp(5)
                        padding: [0, "30dp", 0, 0]        
                        MDRectangleFlatButton:
                            text: "Next"
                            on_release: root.add_data_employment_details(investment.text,loan_type.text,lending_period.text,company_name.text,organisation_type.text,occupation_type.text,company_address.text,landmark.text,employment_type.text,annual_salary.text,salary_type.text,designation.text,business_number.text)
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "20dp"
                            font_name: "Roboto-Bold"    

                # Business Details
                MDBoxLayout:
                    id: business_details_box
                    orientation: 'vertical'
                    spacing: dp(18)
                    #padding: dp(10)
                    size_hint_y: None
                    height: dp(950)

                    MDLabel:
                        text: 'Business Details'
                        halign: 'center'
                        bold: True
                        size_hint_y: None
                        # height:dp(50)

                    MDTextField:
                        id: business_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: ' Enter Business Name *'
                        
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    Spinner:
                        id: spin
                        text: " Select Business Type *"
                        multiline: False
                        font_size: "15dp"
                        size_hint: 1 , None
                        option_cls: 'CustomSpinnerOption'
                        height:"40dp"
                        # width: dp(200)
                        text_size: self.width - dp(20), None
                        background_color: 0,0,0,0
                        background_normal:''
                        color: 0, 0, 0, 1
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7

                    MDTextField:
                        id:  business_address
                        on_text: root.validate_zip_code_numchar(self)
                        hint_text: ' Enter Business Address *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    Spinner:
                        id: no_of_employees_working
                        text: "No of Employees Working *"
                        font_size: "15dp"
                        multiline: False
                        size_hint: 1 , None
                        height:"40dp"
                        # width: dp(200)
                        option_cls: 'CustomSpinnerOption'
                        text_size: self.width - dp(20), None
                        background_color: 0,0,0,0
                        background_normal:''
                        color: 0, 0, 0, 1
                        canvas:
                            Color:
                                rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7

                    MDTextField:
                        id: industry_type
                        on_text: root.validate_zip_code_text(self)
                        hint_text: ' Enter Industry Type *'
                        on_text: root.validate_zip_code_text(self)
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    # MDTextField:
                    #     id: year_of_estd
                    #     hint_text: 'Enter Year of Estd'
                    #     font_size: "15dp"
                    #     height: dp(40)
                    #     width: dp(300)
                    #     theme_text_color: "Custom"
                    #     hint_text_color: 0, 0, 0, 1
                    #     hint_text_color_normal: "black"
                    #     text_color_normal: "black"
                    #     helper_text_color_normal: "black"
                    #     on_touch_down: root.on_date_touch_down()
                    #     mode: "rectangle"
                    #     radius: [0, 0, 0,0]
                    # MDIconButton:
                    #     icon: 'calendar'
                    #     pos_hint: {'center_x': .5, 'center_y': .5}
                    #     on_release: root.show_date_picker()
                    MDBoxLayout:
                        orientation: 'horizontal'
                        spacing: "10dp"
                        size_hint: 1, None
                        halign: "left"
                        font_size: "15dp"
                        padding: dp(10)
                        height: "48dp"
                        # width: dp(200)  
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1   # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7    
                        MDLabel:
                            id: year_of_estd
                            text: "Enter Year of Estd *"
                            font_size: "15dp"
                            height: dp(40)
                            width: dp(300)
                            theme_text_color: "Custom"
                            hint_text_color: 0, 0, 0, 1
                            hint_text_color_normal: "black"
                            text_color_normal: "black"
                            helper_text_color_normal: "black"
                            # on_touch_down: root.on_date_touch_down()
                            mode: "rectangle"
                            radius: [0, 0, 0,0]
                        MDIconButton:
                            icon: 'calendar'
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            on_release: root.show_date_picker()

                    MDTextField:
                        id: last_six_months_turnover
                        on_text: root.validate_zip_code(self)
                        hint_text: ' Enter Last Six Months Turnover *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        size_hint: 1, None
                        halign: "left"
                        font_size: "15dp"
                        height: "70dp"
                        # width: dp(200)
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7

                        MDIconButton:
                            icon: 'upload'
                            id: upload_icon1
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen6').check_and_open_file_manager_bus_1()

                        MDLabel:
                            id: upload_label1
                            text: 'Upload last 6 months statments *' 
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        Image:
                            id: image_label1
                            source: ''
                            allow_stretch: True
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            on_touch_down: root.on_image_click(self, args[1])
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}  

                    MDTextField:
                        id: cin
                        on_text: root.validate_zip_code(self)
                        hint_text: ' Enter CIN Value *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    MDTextField:
                        id: din
                        on_text: root.validate_zip_code(self)
                        hint_text: ' Enter DIN Value *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    MDTextField:
                        id: reg_office_address
                        hint_text: ' Enter Registered Office Address *'
                        on_text: root.validate_zip_code_numchar(self)
                        multiline: False
                        helper_text_mode: 'on_focus'
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        hint_text_color_normal: "black"
                        text_color_normal: "black"
                        helper_text_color_normal: "black"
                        radius: [0, 0, 0,0]
                        mode: "rectangle"

                    BoxLayout:
                        orientation: 'horizontal'
                        padding: "10dp"
                        spacing: "10dp"
                        size_hint: 1, None
                        halign: "left"
                        font_size: "15dp"
                        height: "70dp"
                        # width: dp(200)
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1  # Black color for the line
                            Line:
                                rectangle: self.x, self.y, self.width, self.height
                                width: 0.7

                        MDIconButton:
                            icon: 'upload'
                            id: upload1
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_x: None
                            width: dp(24)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            on_release: app.root.get_screen('LenderScreen6').check_and_open_file_manager_bus_2()

                        MDLabel:
                            id: upload_label_veri
                            text: 'Upload Verified Document *'
                            halign: 'left'
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1  # Black text color
                            size_hint_y: None
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                        Image:
                            id: upload_label_verification_document
                            source: ''
                            allow_stretch: True
                            on_touch_down: root.on_image_click(self, args[1])
                            keep_ratio: True
                            size_hint_y: None
                            size: dp(50), dp(50)
                            height: dp(36)
                            valign: 'middle'  # Align the label text vertically in the center
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDLabel:
                        id: error_message
                        text: "Pleas fill all details! *"
                        # size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 150, 0, 0, 1
                        halign: "left"
                    GridLayout:
                        cols: 1
                        spacing:dp(10)
                        padding: [0, "10dp", 0, 0]
                        MDRaisedButton:
                            text: "Next"
                            on_release: root.add_data_business_details(business_name.text,spin.text,business_address.text,no_of_employees_working.text,industry_type.text,year_of_estd.text,last_six_months_turnover.text,cin.text,din.text,reg_office_address.text,investment.text,loan_type.text,lending_period.text)
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"


# <LenderScreenInstitutionalForm1>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(20)
#         padding: dp(50)

#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(30)

#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(20)
#             padding: dp(30) 
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Lender Registration Form'
#                 halign: 'center'
#                 font_size: "20dp"
#                 font_name: "Roboto-Bold"
#             MDLabel:
#                 text: 'Business Information'
#                 halign: 'center'
#                 bold: True

#             MDTextField:
#                 id: business_name
#                 hint_text: 'Enter Business Name '
#                 multiline: False
#                 helper_text: 'Enter Your Business Name'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#                 font_size: "15dp"

#             MDTextField:
#                 id: business_address
#                 hint_text: 'Enter Business Address'
#                 multiline: False
#                 helper_text: 'Enter Your Business Address'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"

#             MDLabel:
#                 text: 'Select Business Type:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)
#             Spinner:
#                 id: spin
#                 text: "Select Business Type"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 color: 0, 0, 0, 1
#                 font_size: "15dp"
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Select No.Of Employees Working:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             Spinner:
#                 id: spinner_id
#                 text: "Select No.Of Employees Working"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 font_size: "15dp"
#                 color: 0, 0, 0, 1
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(business_name.text,spin.text,spinner_id.text, business_address.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"


# <LenderScreenInstitutionalForm2>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm1')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(20)
#         padding: dp(50)

#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(40)

#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(10)
#             padding: dp(30) 
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Lender Registration Form'
#                 halign: 'center'
#                 font_size: "20dp"
#                 font_name: "Roboto-Bold"
#             MDLabel:
#                 text: 'Business Information'
#                 halign: 'center'
#                 bold: True

#             MDTextField:
#                 id: year_of_estd
#                 hint_text:'Enter Year of Estd'
#                 multiline: False
#                 helper_text: 'YYYY-MM-DD'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 input_type: 'number'
#                 on_touch_down: root.on_estd_touch_down()
#                 helper_text_color_normal: "black"
#                 font_size: "15dp"

#             MDTextField:
#                 id: industry_type
#                 hint_text: 'Enter Industry Type'
#                 multiline: False
#                 helper_text: 'Enter Your Industry Type'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#             MDTextField:
#                 id: last_six_months_turnover
#                 hint_text: 'Enter last 6 months turnover'
#                 multiline: False
#                 helper_text: 'Enter Your last 6 months turnover'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#                 input_type: 'number'
#                 on_touch_down: root.on_last_six_months_turnover_touch_down()

#             MDLabel:
#                 text: 'Last 6 months bank statements:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             BoxLayout:
#                 orientation: 'horizontal'
#                 padding: "10dp"
#                 spacing: "10dp"
#                 size_hint: None, None
#                 size: dp(270), dp(60)  # Adjust size as needed
#                 pos_hint: {'center_x': 0.5, 'center_y': 0.5}

#                 canvas:
#                     Color:
#                         rgba: 0, 0, 0, 1  # Border color (black in this example)
#                     Line:
#                         width: 0.4  # Border width
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#                 MDIconButton:
#                     icon: 'upload'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_x: None
#                     width: dp(24)
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                     on_release: app.root.get_screen('LenderScreenInstitutionalForm2').check_and_open_file_manager1()

#                 MDLabel:
#                     id: upload_label1
#                     text: 'Upload Document'
#                     halign: 'left'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_y: None
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                 Image:
#                     id: image_label1
#                     source: ''
#                     allow_stretch: True
#                     keep_ratio: True
#                     size_hint_y: None
#                     size: dp(50), dp(50)
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             # MDLabel:
#             #     id: image_label1
#             #     text: ''
#             #     halign: 'center'
#             #     theme_text_color: "Custom"
#             #     text_color: 0, 0, 0, 1  # Black text color
#             #     valign: 'middle'  # Align the label text vertically in the center
#             #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}

#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(industry_type.text,last_six_months_turnover.text,year_of_estd.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"

# <LenderScreenInstitutionalForm3>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenInstitutionalForm2')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(20)
#         padding: dp(50)

#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(40)

#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(20)
#             padding: dp(30)
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


#             MDLabel:
#                 text: 'Business Information'
#                 halign: 'center'
#                 bold: True

#             MDTextField:
#                 id: din
#                 hint_text:'Enter DIN'
#                 multiline: False
#                 helper_text: 'Enter DIN'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#                 font_size: "15dp"

#             MDTextField:
#                 id: cin
#                 hint_text: 'Enter CIN'
#                 multiline: False
#                 helper_text: 'Enter CIN'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#             MDTextField:
#                 id: reg_office_address
#                 hint_text: 'Enter Registered Office Address'
#                 multiline: False
#                 helper_text: 'Enter Valid Registered Office Address'
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 height: self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#             MDLabel:
#                 text: 'Upload Proof Of Verification:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             BoxLayout:
#                 orientation: 'horizontal'
#                 padding: "10dp"
#                 spacing: "10dp"
#                 size_hint: None, None
#                 size: dp(270), dp(60)  # Adjust size as needed
#                 pos_hint: {'center_x': 0.5, 'center_y': 0.5}

#                 canvas:
#                     Color:
#                         rgba: 0, 0, 0, 1  # Border color (black in this example)
#                     Line:
#                         width: 0.4  # Border width
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#                 MDIconButton:
#                     icon: 'upload'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_x: None
#                     width: dp(24)
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                     on_release: app.root.get_screen('LenderScreenInstitutionalForm3').check_and_open_file_manager1()

#                 MDLabel:
#                     id: upload_label1
#                     text: 'Upload Document'
#                     halign: 'left'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_y: None
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                 Image:
#                     id: image_label1
#                     source: ''
#                     allow_stretch: True
#                     keep_ratio: True
#                     size_hint_y: None
#                     size: dp(50), dp(50)
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             # MDLabel:
#             #     id: image_label1
#             #     text: ''
#             #     halign: 'center'
#             #     theme_text_color: "Custom"
#             #     text_color: 0, 0, 0, 1  # Black text color
#             #     valign: 'middle'  # Align the label text vertically in the center
#             #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}

#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(din.text,cin.text,reg_office_address.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"


# <LenderScreenIndividualForm1>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(10)
#         padding: dp(20)
#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(50)
#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(10)
#             padding: dp(20)
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Lender Registration Form'
#                 halign: 'center'
#                 font_size: "20dp"
#                 font_name: "Roboto-Bold"

#             MDLabel:
#                 text: 'Employment Details'
#                 halign: 'center'
#                 bold: True
#                 size_hint_y: None
#                 height:dp(50)

#             MDLabel:
#                 text: 'Select Employment Type:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             Spinner:
#                 id: spinner1
#                 text: "Select Employment Type"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 font_size: "15dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 color: 0, 0, 0, 1
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDTextField:
#                 id: company_name
#                 hint_text: 'Enter company Name'
#                 multiline: False
#                 helper_text: "Enter Valid company Name"
#                 helper_text_mode: 'on_focus'
#                 height:self.minimum_height
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#             MDLabel:
#                 text: 'Select Organisation Type:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             Spinner:
#                 id: spinner2
#                 text: "Select Organisation Type"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 font_size: "15dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 color: 0, 0, 0, 1
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
#             MDLabel:
#                 text: 'Select Occupation Type:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             Spinner:
#                 id: spinner3
#                 text: "Select Occupation Type"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 font_size: "15dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 color: 0, 0, 0, 1
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(spinner1.text,spinner3.text, company_name.text, spinner2.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"

# <LenderScreenIndividualForm2>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm1')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(20)
#         padding: dp(30)

#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(35)

#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(5)
#             padding: dp(30) 
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Lender Registration Forms'
#                 halign: 'center'
#                 font_size: "20dp"
#                 font_name: "Roboto-Bold"

#             MDLabel:
#                 text: 'Employment Details'
#                 halign: 'center'
#                 bold: True
#                 size_hint_y: None
#                 height:dp(15)

#             MDTextField:
#                 id: annual_salary
#                 hint_text: 'Enter annual salary'
#                 multiline: False
#                 helper_text: "Enter Valid Annual Salary"
#                 helper_text_mode: 'on_focus'
#                 height:self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 input_type: 'number'
#                 on_touch_down: root.on_annual_salary_touch_down()
#                 helper_text_color_normal: "black"
            
#             MDLabel:
#                 text:"Select Your Salary Type:"
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#             MDLabel:
#                 text:""
#             Spinner:
#                 id: salary_type_id
#                 text: " Select Salary type"
#                 font_size: "15dp"
#                 multiline: False
#                 size_hint: 1 , None
#                 height:"40dp"
#                 width: dp(200)
#                 text_size: self.width - dp(20), None
#                 background_color: 0,0,0,0
#                 background_normal:''
#                 color: 0, 0, 0, 1
#                 canvas.before:
#                     Color:
#                         rgba: 0, 0, 0, 1  
#                     Line:
#                         width: 0.7
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDTextField:
#                 id: designation
#                 hint_text: 'Enter Designation'
#                 multiline: False
#                 helper_text: "Enter Valid designation"
#                 helper_text_mode: 'on_focus'
#                 height:self.minimum_height
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"

#             MDLabel:
#                 text: 'Upload Employee ID:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             BoxLayout:
#                 orientation: 'horizontal'
#                 padding: "10dp"
#                 spacing: "10dp"
#                 size_hint: None, None
#                 size: dp(270), dp(60)  # Adjust size as needed
#                 pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                 canvas:
#                     Color:
#                         rgba: 0, 0, 0, 1  # Border color (black in this example)
#                     Line:
#                         width: 0.4  # Border width
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


#                 MDIconButton:
#                     icon: 'upload'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_x: None
#                     width: dp(24)
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                     on_release: app.root.get_screen('LenderScreenIndividualForm2').check_and_open_file_manager1()

#                 MDLabel:
#                     id: upload_label1
#                     text: 'Upload Document'
#                     halign: 'left'
#                     theme_text_color: "Custom"
#                 Image:
#                     id: image_label1
#                     source: ''
#                     allow_stretch: True
#                     keep_ratio: True
#                     size_hint_y: None
#                     size: dp(50), dp(50)
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             # MDLabel:
#             #     id: image_label1
#             #     text: ''
#             #     halign: 'center'
#             #     theme_text_color: "Custom"
#             #     text_color: 0, 0, 0, 1  # Black text color
#             #     valign: 'middle'  # Align the label text vertically in the center
#             #     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#             #     height:dp(15)
#             #     size_hint_y: None

#             MDLabel:
#                 text: 'Select Upload last 6 months bank statements:'
#                 halign: 'left'
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"
#                 ize_hint_y: None
#                 height:dp(20)

#             BoxLayout:
#                 orientation: 'horizontal'
#                 padding: "10dp"
#                 spacing: "10dp"
#                 size_hint: None, None
#                 size: dp(270), dp(60)  # Adjust size as needed
#                 pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                 canvas:
#                     Color:
#                         rgba: 0, 0, 0, 1  # Border color (black in this example)
#                     Line:
#                         width: 0.4  # Border width
#                         rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


#                 MDIconButton:
#                     icon: 'upload'
#                     theme_text_color: "Custom"
#                     text_color: 0, 0, 0, 1  # Black text color
#                     size_hint_x: None
#                     width: dp(24)
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}
#                     on_release: app.root.get_screen('LenderScreenIndividualForm2').check_and_open_file_manager2()

#                 MDLabel:
#                     id: upload_label1
#                     text: 'Upload Document'
#                     halign: 'left'
#                     theme_text_color: "Custom"

#                 Image:
#                     id: image_label2
#                     source: ''
#                     allow_stretch: True
#                     keep_ratio: True
#                     size_hint_y: None
#                     size: dp(50), dp(50)
#                     height: dp(36)
#                     valign: 'middle'  # Align the label text vertically in the center
#                     pos_hint: {'center_x': 0.5, 'center_y': 0.5}

#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(salary_type_id.text, designation.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"
#             MDLabel:
#                 text: ''
#             MDLabel:
#                 text: ''

# <LenderScreenIndividualForm3>:
#     MDTopAppBar:
#         title: "P2P LENDING"
#         elevation: 2
#         pos_hint: {'top': 1}
#         left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreenIndividualForm2')]]
#         right_action_items: [['home', lambda x: root.go_to_dashboard()]]
#         title_align: 'center'  # Center-align the title
#         md_bg_color: 0.043, 0.145, 0.278, 1

#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(30)
#         padding: dp(30)

#         MDLabel:
#             text:""
#             size_hint_y: None
#             height:dp(50)

#         MDBoxLayout:
#             orientation: 'vertical'
#             spacing: dp(10)
#             padding: dp(30)  # Reduce the top padding
#             md_bg_color:253/255, 254/255, 254/255, 1
#             canvas:
#                 Color:
#                     rgba: 174/255, 214/255, 241/255, 1 # Dull background color
#                 Line:
#                     width: 0.7  # Border width
#                     rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

#             MDLabel:
#                 text: 'Lender Registration Form'
#                 halign: 'center'
#                 font_size: "20dp"
#                 font_name: "Roboto-Bold"

#             MDLabel:
#                 text: 'Employment Details'
#                 halign: 'center'
#                 bold: True
#                 size_hint_y: None
#                 height:dp(50)

#             MDTextField:
#                 id: company_address
#                 hint_text: 'Enter company address'
#                 helper_text: 'Enter valid company address'
#                 multiline: False
#                 helper_text_mode: 'on_focus'
#                 hint_text_color: 0,0,0, 1
#                 font_name: "Roboto-Bold"
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"

#             MDTextField:
#                 id: company_pin_code
#                 hint_text: 'Enter Company Pincode'
#                 helper_text: 'Enter valid Company Pincode'
#                 multiline: False
#                 helper_text_mode: 'on_focus'
#                 hint_text_color: 0,0,0, 1
#                 font_size: "15dp"
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 font_name: "Roboto-Bold"
#                 input_type: 'number'  
#                 on_touch_down: root.on_company_pin_code_touch_down()


#             MDTextField:
#                 id: company_country
#                 hint_text: 'Enter Company Country'
#                 helper_text: 'Enter valid Company Country'
#                 multiline: False
#                 helper_text_mode: 'on_focus'
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 font_size: "15dp"
#                 font_name: "Roboto-Bold"

#             MDTextField:
#                 id: landmark
#                 hint_text: 'Enter landmark'
#                 multiline: False
#                 font_size: "15dp"
#                 helper_text: 'Enter valid landmark'
#                 helper_text_mode: 'on_focus'
#                 theme_text_color: "Custom"
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 font_name: "Roboto-Bold"

#             MDTextField:
#                 id:business_phone_number
#                 hint_text: 'Enter business phone number'
#                 multiline: False
#                 helper_text_mode: 'on_focus'
#                 size_hint_y: None
#                 input_type: 'number'
#                 hint_text_color: 0, 0, 0, 1
#                 hint_text_color_normal: "black"
#                 text_color_normal: "black"
#                 helper_text_color_normal: "black"
#                 font_size: "15dp"
#                 on_touch_down: root.on_business_phone_number_touch_down()
#                 input_type: 'number'


#             MDRectangleFlatButton:
#                 text: "Next"
#                 on_release: root.add_data(company_address.text, company_pin_code.text, company_country.text, landmark.text, business_phone_number.text)
#                 md_bg_color: 0.043, 0.145, 0.278, 1
#                 pos_hint: {'right': 1, 'y': 0.5}
#                 text_color: 1, 1, 1, 1
#                 size_hint: 1, None
#                 height: "50dp"
#                 font_name: "Roboto-Bold"


<LenderScreen7>:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: bar
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen6')]]
            right_action_items: [["icon8.png", lambda x: root.account()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
    
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(30)
                spacing: dp(20)
    
                MDLabel:
                    text: 'Lender Registration Form'
                    halign: 'center'
                    font_size: "20dp"
                    font_name: "Roboto-Bold"
    
                MDLabel:
                    text: ''
                    halign: 'center'
                    size_hint_y: None
                    height: dp(0)
    
                MDLabel:
                    text: "Select Marital Status Type:"
                    halign: 'left'
                    font_size: "15dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(20)
    
                Spinner:
                    id: marital_status_id
                    text: "Marital Status"
                    values: ["Married", "Unmarried", "Others"]
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1, None
                    height: "40dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'
                    on_text: root.update_details(marital_status_id.text)
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rectangle: (self.x, self.y, self.width, self.height)
    
                MDLabel:
                    text:"Select Your Guaranter:"
                    halign: 'left'
                    font_size: "15dp"
                    font_name: "Roboto-Bold"
                    size_hint_y: None
                    height: dp(20)
    
                Spinner:
                    id: relation_name
                    text: "How is the person related to you"
                    font_size: "15dp"
                    multiline: False
                    size_hint: 1 , None
                    height: "40dp"
                    width: dp(200)
                    text_size: self.width - dp(20), None
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    color: 0, 0, 0, 1
                    option_cls: 'CustomSpinnerOption'  
                    on_text: root.update_person_details_visibility(relation_name.text)
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rectangle: (self.x, self.y, self.width, self.height)
                            
                MDBoxLayout:
                    id: box
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    opacity: 1
                    spacing: dp(22)
    
    
                GridLayout:
                    cols: 1
                    spacing: dp(30)
                    padding: [0, "30dp", 0, 0]
    
                    MDRaisedButton:
                        text: "Next"
                        on_release: root.add_data(marital_status_id.text)
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        pos_hint: {'right': 1, 'y': 0.5}
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None
                        height: "50dp"
                        font_name: "Roboto-Bold"
    
                MDLabel:
                    text: ''
                    halign: 'center'
                    size_hint_y: None
                    height: dp(50)

<LenderScreen8>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        padding: dp(30)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(50)

            MDLabel:
                text: 'Father Information'
                halign: 'center'
                bold: True

            MDTextField:
                id: father_name
                hint_text: 'Enter Father Name'
                helper_text: 'Enter valid Father Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                font_size: "15dp"

            MDTextField:
                id: father_dob
                hint_text: "Enter Father D.O.B"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: "on_error"
                font_name: "Roboto-Bold"
                theme_text_color: 'Custom'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"
                input_type:'number'
                on_touch_down: root.on_date_touch_down()

            MDTextField:
                id: father_address
                hint_text: 'Enter Father Address'
                helper_text: 'Enter valid Father Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_occupation
                hint_text: 'Enter Father Occupation'
                helper_text: 'Enter valid Father Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: father_ph_no
                hint_text: 'Enter Father Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_father_ph_no_touch_down()


            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(father_name.text, father_address.text, father_occupation.text, father_ph_no.text, father_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen9>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30) # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Mother Information'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)

            MDTextField:
                id: mother_name
                hint_text: 'Enter Mother Name'
                helper_text: 'Enter valid Mother Name'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0,0,0, 1
                font_name: "Roboto-Bold"
                font_size: "15dp"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: mother_dob
                hint_text: "Enter Father D.O.B"
                helper_text: 'YYYY-MM-DD'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                input_type:'number'
                font_size: "15dp"
                on_touch_down: root.on_date_touch_down()
            MDTextField:
                id: mother_address
                hint_text: 'Enter Mother Address'
                helper_text: 'Enter valid Mother Address'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_occupation
                hint_text: 'Enter Mother Occupation'
                helper_text: 'Enter valid Mother Occupation'
                multiline: False
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                font_name: "Roboto-Bold"

            MDTextField:
                id: mother_ph_no
                hint_text: 'Enter Mother Phone NO'
                multiline: False
                font_size: "15dp"
                helper_text: 'Enter valid PH No'
                helper_text_mode: 'on_focus'
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_name: "Roboto-Bold"
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()

            MDRectangleFlatButton:
                text: "Next"
                on_release: root.add_data(mother_name.text, mother_address.text, mother_occupation.text, mother_ph_no.text, mother_dob.text)
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"


<LenderScreen10>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDTextField:
                id: spouse_name
                hint_text: 'Enter Spouse Name'
                multiline: False
                helper_text: "Enter Valid Spouse Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"

            MDTextField:
                id: spouse_marriage_date
                hint_text: "Enter Spouse Marriage Date"
                helper_text: 'YYYY-MM-DD'
                helper_text_mode: "on_error"
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"
                input_type:'number'
                on_touch_down: root.on_date_touch_down()

            MDTextField:
                id: spouse_mobile
                hint_text: 'Enter Spouse Mobile No'
                multiline: False
                helper_text: "Enter Valid Spouse Mobile No"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                height:self.minimum_height
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                font_size: "15dp"
                input_type: 'number'
                on_touch_down: root.on_spouse_mobile_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: 'Next'
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.add_data(spouse_name.text, spouse_marriage_date.text, spouse_mobile.text)


<LenderScreen11>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen10')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(25)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Spouse Details'
                halign: 'center'
                bold:True

            MDLabel:
                text:"Select Spouse Profession Type:"
                halign: 'left'
                font_size: "15dp"
                font_name: "Roboto-Bold"
                size_hint_y: None
                height:dp(20)

            Spinner:
                id: spouse_profession
                text: "Select Spouse Profession"
                multiline: False
                size_hint: 1 , None
                font_size: "15dp"
                height:"40dp"
                width: dp(200)
                text_size: self.width - dp(20), None
                background_color: 0,0,0,0
                background_normal:''
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  
                    Line:
                        width: 0.7
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDTextField:
                id: spouse_company_name
                hint_text: 'Enter Spouse Company Name'
                multiline: False
                helper_text: "Enter Valid Spouse Company Name (if working)"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                height:self.minimum_height
                font_size: "15dp"

            MDTextField:
                id: spouse_annual_salary
                hint_text: 'Enter Annual Salary'
                font_size: "15dp"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"
                multiline: False
                helper_text: 'Enter valid Annual Salary (if working)'
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                input_type: 'number'
                on_touch_down: root.on_spouse_annual_salary_touch_down()

            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: 'Next'
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"
                    on_release: root.add_data(spouse_company_name.text, spouse_profession.text, spouse_annual_salary.text)

<LenderScreen12>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]  # Padding: [left, top, right, bottom]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"
        BoxLayout:
            orientation: "vertical"
            spacing: "7dp"
            padding: "15dp"

            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)

            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.3, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()
                MDFillRoundFlatButton:
                    id: id3
                    text: "Spouse"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed3()
                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"

<LenderScreen13>:
    MDTopAppBar:
        title: "P2P LENDING"
        elevation: 2
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text: "Family Members Details"
            size_hint_y: None
            height: dp(40)
            padding: [0, dp(40), 0, 0]
            halign: "center"
            bold: True
            font_name: "Roboto-Bold"

        BoxLayout:
            orientation: "vertical"
            spacing: dp(10)
            padding: dp(10)

            MDLabel:
                text: "Provide Another Person Details"
                halign: "center"
                size_hint_y: None
                height: dp(70)
            MDGridLayout:
                cols: 4
                spacing: dp(10)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Fixed the typo here
                MDFillRoundFlatButton:
                    id: id1
                    text: "Father"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed1()
                MDFillRoundFlatButton:
                    id: id2
                    text: "Mother"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed2()

                MDFillRoundFlatButton:
                    id: id4
                    text: "Other"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    on_release: root.on_yes_button_pressed4()

            MDRaisedButton:
                text: "Next"
                on_release: root.add_data()
                md_bg_color: 0.043, 0.145, 0.278, 1
                pos_hint: {'right': 1, 'y': 0.5}
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
<LenderScreen14>:
    MDTopAppBar:
        title: "P2P LENDING"
        pos_hint: {'top': 1}
        left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
        right_action_items: [['home', lambda x: root.go_to_dashboard()]]
        title_align: 'center'  # Center-align the title
        md_bg_color: 0.043, 0.145, 0.278, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)

        MDLabel:
            text:""
            size_hint_y: None
            height:dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(30)  # Reduce the top padding
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Lender Registration Form'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"

            MDLabel:
                text: 'Person Details'
                halign: 'center'
                bold: True
                size_hint_y: None
                height:dp(50)


            MDTextField:
                id: relation_name
                hint_text: 'How is the person related to you'
                helper_text: 'Enter Valid Person Relation'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_name
                hint_text: 'Enter Person Name'
                helper_text: 'Enter Valid Person Name'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_dob
                hint_text: 'Enter Person D.O.B'
                helper_text: 'YYYY-MM-DD'
                multiline: False
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type:'number'
                on_touch_down: root.on_date_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"


            MDTextField:
                id: person_ph_no
                hint_text: 'Enter Person Phone No'
                helper_text: 'Enter Valid Person Phone No'
                helper_text_mode: 'on_focus'
                halign: 'left'
                input_type: 'number'  
                on_touch_down: root.on_mother_ph_no_touch_down()
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            MDTextField:
                id: person_proffission
                hint_text: 'Enter Person Profession'
                helper_text: 'Enter valid Person Profession'
                multiline: False
                helper_text_mode: 'on_focus'
                font_size: "15dp"
                theme_text_color: "Custom"
                hint_text_color: 0, 0, 0, 1
                hint_text_color_normal: "black"
                text_color_normal: "black"
                helper_text_color_normal: "black"

            GridLayout:
                cols: 1
                spacing: dp(30)
                padding: [0, "30dp", 0, 0]
                MDRectangleFlatButton:
                    text: "Next"
                    on_release: root.add_data(relation_name.text, person_name.text, person_dob.text, person_ph_no.text, person_proffission.text)
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold"

<LenderScreenIndividualBankForm1>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "P2P LENDING"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderScreen7')]]
            right_action_items: [['home', lambda x: root.go_to_dashboard()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: self.minimum_height 
        
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(15)
                    padding: dp(10)
                    size_hint_y: None
                    height: dp(600)
        
                    MDLabel:
                        text: 'Applicant Bank Details'
                        halign: 'center'
                        font_size: "15dp"
                        font_name: "Roboto-Bold"
                    MDTextField:
                        id: account_holder_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter account holder name *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
                        
        
                    MDBoxLayout:
                        size_hint_y:None
                        height:"50dp"
                        Spinner:
                            id: account_type
                            text: "Select Account Type *"
                            font_size: "15dp"
                            multiline: False
                            size_hint: 1 , None
                            height:"40dp"
                            width: dp(200)
                            text_size: self.width - dp(20), None
                            background_color: 0,0,0,0
                            option_cls: 'CustomSpinnerOption'
                            background_normal:''
                            color: 0, 0, 0, 1
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1  
                                Line:
                                    rectangle: self.x, self.y, self.width, self.height
                                    width: 0.7
                            
                            
                    MDTextField:
                        id: account_number
                        on_text: root.validate_zip_code(self)
                        hint_text: 'Enter account number *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y: None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        input_type: 'number'
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDTextField:
                        id: bank_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter bank name *'
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
                        
                    MDTextField:
                        id: ifsc_code
                        hint_text: 'Enter Ifsc_code * '
                        on_text: root.validate_zip_code_numchar(self)
                        multiline: False
                        helper_text_mode: 'on_focus'
                        size_hint_y:None
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
        
                    MDTextField:
                        id: branch_name
                        on_text: root.validate_zip_code_text(self)
                        hint_text: 'Enter branch name *'
                        hint_text_mode: 'on_focus'
                        multiline: False
                        halign: 'left'
                        multiline: False
                        font_size: "15dp"
                        theme_text_color: "Custom"
                        hint_text_color: 0, 0, 0, 1
                        text_color_normal: "black"
                        mode: "rectangle"
                        radius: [0, 0, 0, 0]  # Makes the corners square
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: "32dp"
                        spacing:dp(10)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDCheckbox:
                            id: check
                            size_hint: None, None
                            size: "30dp", "30dp"
                            active: False
                            on_active: root.on_checkbox_active(self, self.active)
        
                        MDLabel:
                            text: "I Agree Terms and Conditions *"
                            size: "30dp", "30dp"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "left"
                            valign: "center"
                            on_touch_down: app.root.get_screen("LenderScreenIndividualBankForm1").show_terms_dialog() if self.collide_point(*args[1].pos) else None
        
                    MDLabel:
                        id: error_message
                        text: "Pleas fill all details! *"
                        size: "30dp", "30dp"
                        theme_text_color: "Custom"
                        text_color: 150, 0, 0, 1
                        halign: "left"
                    GridLayout:
                        cols: 1
                        spacing:dp(30)
                        MDRectangleFlatButton:
                            id: submit
                            text: "Submit"
                            on_release: root.go_to_lender_dashboard(ifsc_code.text, branch_name.text,account_holder_name.text, account_type.text, account_number.text, bank_name.text)
                            md_bg_color: 0.043, 0.145, 0.278, 1
                            pos_hint: {'right': 1, 'y': 0.5}
                            text_color: 1, 1, 1, 1
                            size_hint: 1, None
                            height: "50dp"
                            font_name: "Roboto-Bold"
                            disabled: root.all_fields_filled

'''

conn = sqlite3.connect("fin_user.db")
cursor = conn.cursor()


class LenderScreen(Screen):
    Builder.load_string(KV)
    MAX_IMAGE_SIZE_MB = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        spinner_data = app_tables.fin_gender.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['gender'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spinner_id.values =  unique_list
        else:
            self.ids.spinner_id.values = ['Select Gender']

        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search(email_user=user_email)

        id_list = []
        for i in data:
            id_list.append(i['email_user'])
        if user_email in id_list:
            index = id_list.index(user_email)
            self.ids.username.text = data[index]['full_name']
            self.ids.mobile_number.text = data[index]['mobile']
        else:
            print('email not found')

    def validate_image_loaded(self, image_label):
        if not image_label.source or 'error.png' in image_label.source:  # Adjust 'error.png' as per your placeholder image
            return False
        return True


    def on_aadhar_number_text(self, text):
        upload_icon = self.ids.upload_icon2
        upload_icon.disabled = not bool(text)

    def on_pan_number_text(self, text):
        upload_icon = self.ids.upload_icon3
        upload_icon.disabled = not bool(text)


    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.date_textfield.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, name, gender, date,mobile_number, alternate_email, aadhar_number, pan_number,):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(name, gender, date,mobile_number, alternate_email, aadhar_number, pan_number,modal_view), 2)

    def calculate_age(self, date):
        today = datetime.today()
        dob = datetime.strptime(date, '%Y-%m-%d')
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def perform_data_addition_action(self, name, gender, date, mobile_number, alternate_email, aadhar_number,
                                     pan_number, modal_view):
        # Cancel any animations and dismiss the modal view
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        validation_errors = []

        if not self.validate_image_loaded(self.ids.image_label1):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Profile Pic.")
        elif not self.validate_image_loaded(self.ids.image_label2):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Gov ID1.")
        elif not self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Gov ID2.")
        elif not self.validate_image_loaded(self.ids.image_label3) and self.validate_image_loaded(
                self.ids.image_label2) and self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload all Images.")
        else:
            pass

        # Check for mandatory fields
        if not name:
            validation_errors.append((self.ids.username, ""))
        if not date:
            validation_errors.append(
                (self.ids.date_textfield, ""))  # Corrected to date_textfield
        if not gender or gender == 'Select Gender *':
            self.show_validation_error("Please select your gender.")
            return
        if not mobile_number:
            validation_errors.append((self.ids.mobile_number, ""))

        if not aadhar_number:
            validation_errors.append((self.ids.aadhar_number, ""))

        if not pan_number:
            validation_errors.append((self.ids.pan_number, ""))

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return  # Prevent further execution if there are missing fields

        # Validate mobile number
        if not re.match(r'^\d{10}$|^\d{12}$', mobile_number):
            validation_errors.append(
                (self.ids.mobile_number, ""))


        # Validate date of birth
        try:
            dob = datetime.strptime(date, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                self.show_validation_error("Enter a Valid Date of Birth Age must be Greater Than 18")
                return

        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        # Fetch user data
        cursor.execute('SELECT * FROM fin_users')
        rows = cursor.fetchall()
        row_id_list = [row[0] for row in rows]
        email_list = [row[2] for row in rows]
        status = [row[-1] for row in rows]

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET name = ?, gender = ?, date_of_birth = ?, mobile_number = ?, alternate_email = ?, aadhar_number = ?, pan_number = ? WHERE customer_id = ?",
                (name, gender, date, mobile_number, alternate_email, aadhar_number, pan_number, row_id_list[log_index])
            )
            conn.commit()
        else:
            print("User is not logged in.")

        # Update user profile
        user_email = anvil.server.call('another_method')
        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]

        if user_email in id_list:
            if user_email in id_list:
                index = id_list.index(user_email)
                data[index]['full_name'] = name
                data[index]['gender'] = gender
                data[index]['date_of_birth'] = date
                age = self.calculate_age(date)
                data[index]['user_age'] = age
                data[index]['mobile'] = mobile_number
                data[index]['another_email'] = alternate_email
                data[index]['aadhaar_no'] = aadhar_number
                data[index]['pan_number'] = pan_number
        else:
            print("Email not found")

        # Transition to the next screen
        sm = self.manager
        lender_screen3 = LenderScreen3(name='LenderScreen3')
        sm.add_widget(lender_screen3)
        sm.transition.direction = 'left'
        sm.current = 'LenderScreen3'

        self.show_validation_errors(validation_errors)

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            widget.line_color_normal = (1, 0, 0, 1)
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'

    def check_alternate_email(self, alternate_email):
        alternate_email_text = alternate_email.text

        # Regular expression for validating an email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Check the alternate email field

        if not re.match(email_regex, alternate_email_text):
            alternate_email.helper_text = "Invalid email format"
            alternate_email.error = True
        else:
            alternate_email.helper_text = ""
            alternate_email.line_color_normal = (0, 0, 0, 1)
            alternate_email.error = False

    # def validate_spinner(self, spinner):
    #     # Assuming an empty or default value is considered invalid
    #     if spinner.text == "" or spinner.text == "Select Gender":
    #         return False
    #     return True
    def validate_aadhar_number(self, aadhar_number):
        aadhar_number_text = aadhar_number.text
        if not aadhar_number_text:
            aadhar_number.helper_text = ""
            aadhar_number.error = True
        else:
            aadhar_number.helper_text = ""
            aadhar_number.line_color_normal = (0, 0, 0, 1)
            aadhar_number.error = False

    def validate_pan_number(self, pan_number):
        pan_number_text = pan_number.text
        if not pan_number_text:
            pan_number.helper_text = ""
            pan_number.error = True
        else:
            pan_number.helper_text = ""
            pan_number.line_color_normal = (0, 0, 0, 1)
            pan_number.error = False
    def validate_mobile(self, mobile_number):
        mobile_number_text = mobile_number.text

        # Regular expression for validating a mobile number
        # This example assumes a 10-digit number format, adjust it according to your requirements
        mobile_regex = r'^\d{10}$'

        # Check the mobile number field
        if not mobile_number_text:
            mobile_number.helper_text = "Mobile number cannot be empty"
            mobile_number.error = True
        elif not re.match(mobile_regex, mobile_number_text):
            mobile_number.helper_text = "Format should contain 10 numbers"
            mobile_number.error = True
        else:
            mobile_number.helper_text = ""
            mobile_number.line_color_normal = (0, 0, 0, 1)
            mobile_number.error = False

    def get_email(self):
        return anvil.server.call('another_method')
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mobile_number.input_type = 'number'
    def upload_file(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['user_photo'] = user_photo_media

            print("File uploaded successfully.")
            if file_extension in ['.png', '.jpg', '.jpeg']:
                self.ids.image_label1.source = file_path
                print(f"Set image source to: {file_path}")

        except Exception as e:
            print(f"Error uploading file: {e}")
    def upload_file1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['aadhaar_photo'] = user_photo_media

            print("File uploaded successfully.")
            if file_extension in ['.png', '.jpg', '.jpeg']:
                self.ids.image_label2.source = file_path
                print(f"Set image source to: {file_path}")

        except Exception as e:
            print(f"Error uploading file: {e}")

    def upload_file2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['pan_photo'] = user_photo_media

            print("File uploaded successfully.")
            if file_extension in ['.png', '.jpg', '.jpeg']:
                self.ids.image_label3.source = file_path
                print(f"Set image source to: {file_path}")

        except Exception as e:
            print(f"Error uploading file: {e}")

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_file)
    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label2", self.upload_file1)

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label3", self.upload_file2)
    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image using the provided function
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        self.file_manager.close()
        # self.manager.get_screen('LenderScreen1').ids[image_label_id].text = file_name  # Update the label text
        # self.file_manager.close()

    def on_image_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.show_image_popup(instance.source)

    def show_image_popup(self, image_source):
        layout = BoxLayout(orientation='vertical')

        popup_img = Image(source=image_source)
        layout.add_widget(popup_img)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        self.popup = Popup(title='Image Preview',
                           content=layout,
                           size_hint=(0.8, 0.8))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()
    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET upload_photo = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label1.text = 'Upload Successfully'
    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label2.text = 'Upload Successfully'
    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET aadhar_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()

        self.ids.upload_label3.text = 'Upload Successfully'
    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        self.ids.date_textfield.text = str(value)

    # Cancel
    def on_cancel(self, instance, time):
        self.ids.date_textfield.text = "You Clicked Cancel!"

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderLanding'  # Replace with the actual name of your previous screen

    def refresh(self):
        pass

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'


class LenderScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_present_address.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['present_address'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id1.values = ['Select Present Address'] + self.unique_list
        else:
            self.ids.spinner_id1.values = ['Select Present Address']

        spinner_data = app_tables.fin_duration_at_address.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['duration_at_address'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id2.values = ['Select Staying Address'] + self.unique_list
        else:
            self.ids.spinner_id2.values = ['Select Staying Address']

    def refresh(self):
        pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, street_address1, street_address2, spinner_id1, spinner_id2,city, zip_code, state, country):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(street_address1, street_address2, spinner_id1, spinner_id2, city, zip_code, state, country,
                                                          modal_view), 2)

    def perform_data_addition_action4(self, street_address1, street_address2, spinner_id1, spinner_id2, city, zip_code, state, country, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        validation_errors = []
        # Check for missing fields

        if not street_address1:
            validation_errors.append((self.ids.street_address1, ""))
        if not street_address2:
            validation_errors.append((self.ids.street_address2, ""))
        if not spinner_id1 or spinner_id1 == 'Select Present Address *':
            self.show_validation_errors("Please Select Your Present Address.")
            return
        if not spinner_id2 or spinner_id2 == 'Select Staying Address *':
            self.show_validation_errors("Please Select Your Duration At Address.")
            return
        if not city:
            validation_errors.append((self.ids.city, ""))
        if not zip_code:
            validation_errors.append((self.ids.zip_code, ""))
        if not state:
            validation_errors.append((self.ids.state, ""))
        if not country:
            validation_errors.append((self.ids.country, ""))
        if validation_errors:
            self.show_validation_error(validation_errors)
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')


        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = []
        for i in data:
            id_list.append(i['email_user'])

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['street_adress_1'] = street_address1
            data[index]['street_address_2'] = street_address2
            data[index]['present_address'] = spinner_id1
            data[index]['duration_at_address'] = spinner_id2
            data[index]['city'] = city
            data[index]['pincode'] = zip_code
            data[index]['state'] = state
            data[index]['country'] = country
        else:
            print('no email found')
        sm = self.manager
        lender_screen = LenderScreen5(name='LenderScreen5')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen5'
    def on_mobile_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.zip_code.input_type = 'number'

    # def show_validation_errors(self, validation_errors):
    #     for widget, error_message in validation_errors:
    #         widget.error = True
    #         widget.helper_text_color = (1, 0, 0, 1)
    #         widget.helper_text = error_message
    #         widget.helper_text_mode = "on_error"
    #         if isinstance(widget, MDCheckbox):
    #             widget.line_color_normal = (1, 0, 0, 1)
    #         if isinstance(widget, MDCheckbox):
    #             widget.line_color_normal = 'Error'
    def validate_zip_code(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only numeric characters
        if not zip_code_text.isdigit():
            zip_code.helper_text = "ZIP Code should contain only numbers"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.line_color_normal = (0, 0, 0, 1)
            zip_code.error = False

    def show_validation_error(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            widget.line_color_normal = (1, 0, 0, 1)
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'
    def validate_street_address1(self, street_address1):
        street_address1_text = street_address1.text
        if not street_address1_text:
            street_address1.helper_text = ""
            street_address1.error = True
        else:
            street_address1.helper_text = ""
            street_address1.line_color_normal = (0, 0, 0, 1)
            street_address1.error = False
    def validate_street_address2(self, street_address2):
        street_address2_text = street_address2.text
        if not street_address2_text:
            street_address2.helper_text = ""
            street_address2.error = True
        else:
            street_address2.helper_text = ""
            street_address2.line_color_normal = (0, 0, 0, 1)
            street_address2.error = False
    def validate_city(self, city):
        city_text = city.text
        if not city_text:
            city.helper_text = ""
            city.error = True
        else:
            city.helper_text = ""
            city.line_color_normal = (0, 0, 0, 1)
            city.error = False
    def validate_state(self, state):
        state_text = state.text
        if not state_text:
            state.helper_text = ""
            state.error = True
        else:
            state.helper_text = ""
            state.line_color_normal = (0, 0, 0, 1)
            state.error = False

    def validate_country(self, country):
        country_text = country.text
        if not country_text:
            country.helper_text = ""
            country.error = True
        else:
            country.helper_text = ""
            country.line_color_normal = (0, 0, 0, 1)
            country.error = False

    def show_validation_errors(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen'

class LenderScreen5(Screen):
    MAX_IMAGE_SIZE_MB = 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_qualification.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_qualification'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.spinner_id.values = self.unique_list
        else:
            self.ids.spinner_id.values = ['Select Education Details']

        self.ids.box_10th.opacity = 0
        self.ids.box_12th.opacity = 0
        self.ids.box_bachelors.opacity = 0
        self.ids.box_masters.opacity = 0
        self.ids.box_phd.opacity = 0

    def validate_image_loaded(self, image_label):
        if not image_label.source or 'error.png' in image_label.source:  # Adjust 'error.png' as per your placeholder image
            return False
        return True

    def on_image_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.show_image_popup(instance.source)

    def show_image_popup(self, image_source):
        layout = BoxLayout(orientation='vertical')

        popup_img = Image(source=image_source)
        layout.add_widget(popup_img)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        self.popup = Popup(title='Image Preview',
                           content=layout,
                           size_hint=(0.8, 0.8))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()
    # def animate_loading_text(self, loading_label, modal_height):
    #     # Define the animation to move the label vertically
    #     anim = Animation(y=modal_height - loading_label.height, duration=1) + \
    #            Animation(y=0, duration=1)
    #     # Loop the animation
    #     anim.repeat = True
    #     anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
    #     anim.start(loading_label)
    #     # Store the animation object
    #     loading_label.animation = anim  # Store the animation object in a custom attribute

    # def update_education_details(self, id):
        # modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])
        #
        # # Create MDLabel with white text color, increased font size, and bold text
        # loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
        #                         theme_text_color="Custom", text_color=[1, 1, 1, 1],
        #                         font_size="50sp", bold=True)
        #
        # # Set initial y-position off-screen
        # loading_label.y = -loading_label.height
        #
        # modal_view.add_widget(loading_label)
        # modal_view.open()
        #
        # # Perform the animation
        # self.animate_loading_text(loading_label, modal_view.height)
        #
        # # Perform the actual action (e.g., fetching loan requests)
        # # You can replace the sleep with your actual logic
        # Clock.schedule_once(lambda dt: self.perform_data_addition_action(id, modal_view))

    def update_education_details(self, id):
        # modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # modal_view.dismiss()
        spinner_id = self.ids.spinner_id.text
        print(spinner_id)
        if spinner_id not in self.unique_list:
            self.show_validation_error('Select a Valid Education Type')
            return

        all_boxes = ['box_10th', 'box_12th', 'box_bachelors', 'box_masters', 'box_phd']

        # Map spinner_id to the corresponding box id
        spinner_to_box = {
            '10th class': 'box_10th',
            '10th standard': 'box_10th',
            'Intermediate': 'box_12th',
            '12th standard': 'box_12th',
            'Bachelors': 'box_bachelors',
            "Bachelor's degree": 'box_bachelors',
            'Masters': 'box_masters',
            "Master's degree": 'box_masters',
            'PHD': 'box_phd',
            'PhD': 'box_phd'
        }

        selected_box_id = spinner_to_box.get(spinner_id)

        # Get the parent layout of the boxes
        parent_layout = self.ids.parent_layout_id  # Replace with the actual id of the parent layout

        # Hide all boxes
        for box_id in all_boxes:
            box = self.ids[box_id]
            box.opacity = 0

        # Show the selected box
        if selected_box_id:
            selected_box = self.ids[selected_box_id]
            selected_box.opacity = 1

        # Remove all boxes from the parent layout
        for box_id in all_boxes:
            box = self.ids[box_id]
            if box.parent:
                parent_layout.remove_widget(box)

        # Re-add boxes to the parent layout in order, with the visible box on top
        if selected_box_id:
            parent_layout.add_widget(self.ids[selected_box_id])
        for box_id in all_boxes:
            if box_id != selected_box_id:
                parent_layout.add_widget(self.ids[box_id])

        self.adjust_screen_height()
    #     if not id or id == 'Select Education Details':
    #         self.show_validation_error("Please Select Your Education Details.")
    #         return
    #     if id == '10th class' or id == '10th standard':
    #         LenderScreen_Edu_10th()
    #         sm = self.manager
    #         lender_screen = LenderScreen_Edu_10th(name='LenderScreen_Edu_10th')
    #         sm.add_widget(lender_screen)
    #         sm.transition.direction = 'left'  # Set the transition direction explicitly
    #         sm.current = 'LenderScreen_Edu_10th'
    #     elif id == 'Intermediate' or id == '12th standard':
    #         LenderScreen_Edu_Intermediate()
    #         sm = self.manager
    #         lender_screen = LenderScreen_Edu_Intermediate(name='LenderScreen_Edu_Intermediate')
    #         sm.add_widget(lender_screen)
    #         sm.transition.direction = 'left'  # Set the transition direction explicitly
    #         sm.current = 'LenderScreen_Edu_Intermediate'
    #     elif id == 'Bachelors' or id == "Bachelor's degree":
    #
    #         sm = self.manager
    #         lender_screen = LenderScreen_Edu_Bachelors(name='LenderScreen_Edu_Bachelors')
    #         sm.add_widget(lender_screen)
    #         sm.transition.direction = 'left'  # Set the transition direction explicitly
    #         sm.current = 'LenderScreen_Edu_Bachelors'
    #     elif id == 'Masters' or id == "Master's degree":
    #
    #         sm = self.manager
    #         lender_screen = LenderScreen_Edu_Masters(name='LenderScreen_Edu_Masters')
    #         sm.add_widget(lender_screen)
    #         sm.transition.direction = 'left'  # Set the transition direction explicitly
    #         sm.current = 'LenderScreen_Edu_Masters'
    #     elif id == 'PHD' or id == 'PhD':
    #
    #         sm = self.manager
    #         lender_screen = LenderScreen_Edu_PHD(name='LenderScreen_Edu_PHD')
    #         sm.add_widget(lender_screen)
    #         sm.transition.direction = 'left'  # Set the transition direction explicitly
    #         sm.current = 'LenderScreen_Edu_PHD'
        print(id)
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET highest_qualification = ? WHERE customer_id = ?",
                           (id, row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')
        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]

        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['qualification'] = id
        else:
            print('email not found')
    # def update_education_details(self, ):
    #     spinner_id=self.ids.spinner_id.text
    #     print(spinner_id)
    #     if spinner_id not in self.unique_list:
    #         self.show_validation_error('Select a Valid Education Type')
    #         return
    #
    #     all_boxes = ['box_10th', 'box_12th', 'box_bachelors', 'box_masters', 'box_phd']
    #
    #     # Map spinner_id to the corresponding box id
    #     spinner_to_box = {
    #         '10th class': 'box_10th',
    #         '10th standard': 'box_10th',
    #         'Intermediate': 'box_12th',
    #         '12th standard': 'box_12th',
    #         'Bachelors': 'box_bachelors',
    #         "Bachelor's degree": 'box_bachelors',
    #         'Masters': 'box_masters',
    #         "Master's degree": 'box_masters',
    #         'PHD': 'box_phd',
    #         'PhD': 'box_phd'
    #     }
    #
    #     selected_box_id = spinner_to_box.get(spinner_id)
    #
    #     # Get the parent layout of the boxes
    #     parent_layout = self.ids.parent_layout_id  # Replace with the actual id of the parent layout
    #
    #     # Hide all boxes
    #     for box_id in all_boxes:
    #         box = self.ids[box_id]
    #         box.opacity = 0
    #
    #     # Show the selected box
    #     if selected_box_id:
    #         selected_box = self.ids[selected_box_id]
    #         selected_box.opacity = 1
    #
    #     # Remove all boxes from the parent layout
    #     for box_id in all_boxes:
    #         box = self.ids[box_id]
    #         if box.parent:
    #             parent_layout.remove_widget(box)
    #
    #     # Re-add boxes to the parent layout in order, with the visible box on top
    #     if selected_box_id:
    #         parent_layout.add_widget(self.ids[selected_box_id])
    #     for box_id in all_boxes:
    #         if box_id != selected_box_id:
    #             parent_layout.add_widget(self.ids[box_id])
    #
    #     self.adjust_screen_height()

    def adjust_screen_height(self):
        height = 0
        for box_id in ['box_10th', 'box_12th', 'box_bachelors', 'box_masters', 'box_phd']:
            box = self.ids[box_id]
            if box.opacity == 1:
                height += box.height
        self.height = height
    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        pass

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen3'

# ================================================================================
# class LenderScreen_Edu_10th(Screen):
#     MAX_IMAGE_SIZE_MB = 2
#
#     def refresh(self):
#         pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1",
                                         "selected_file_label1", "selected_image1",
                                         "image_label1", self.upload_image)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_image):
    #     upload_image(path)  # Upload the selected image using the provided function
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     self.file_manager.close()
    #     self.manager.get_screen('LenderScreen5').ids[image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        else:
            print('User is not logged in.')

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return

            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media
            print("Image uploaded successfully.")
            # self.ids['image_label1'].source = user_photo_media

        except Exception as e:
            print(f"Error uploading image: {e}")
    def get_email(self):
        return anvil.server.call('another_method')
    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()


    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen_10(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action10th(modal_view), 2)

    def perform_loan_request_action10th(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label1):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        else:
            lender_screen4 = LenderScreen6(name='LenderScreen6')
            sm.add_widget(lender_screen4)
            sm.current = 'LenderScreen6'

#===============================================================================
# class LenderScreen_Edu_Intermediate(Screen):
#     MAX_IMAGE_SIZE_MB = 2
#
#     def refresh(self):
#         pass

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label2", self.upload_image1)

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label3", self.upload_image2)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     upload_function(path)  # Upload the selected image using the provided function
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     self.file_manager.close()
    #     self.manager.get_screen('LenderScreen5').ids[image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_3(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label1'].source = ''

        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label2'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()



    # def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.upload_image2(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Intermediate').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()


    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen_11(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action11th(modal_view), 2)

    def perform_loan_request_action11th(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label2):
            validation_errors.append((self.ids.image_label2, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificates.")
        # Create a new instance of the LoginScreen
        elif not self.validate_image_loaded(self.ids.image_label3):
            validation_errors.append((self.ids.image_label3, "Image not loaded."))
            self.show_validation_error("Please Upload 11th Certificates.")
        else:
            lender_screen4 = LenderScreen6(name='LenderScreen6')
            sm.add_widget(lender_screen4)
            sm.current = 'LenderScreen6'

# ================================================================================
# class LenderScreen_Edu_Bachelors(Screen):
#     MAX_IMAGE_SIZE_MB = 2
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager4(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label4", self.upload_image3)

    def check_and_open_file_manager5(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label5", self.upload_image4)

    def check_and_open_file_manager6(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label6", self.upload_image5)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     upload_function(path)  # Upload the selected image using the provided function
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     self.file_manager.close()
    #     self.manager.get_screen('LenderScreen5').ids[image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_4(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_5(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_6(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def upload_image3(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label1'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image4(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label2'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image5(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label3'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def refresh(self):
        pass


    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path3(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')



    # def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     self.upload_image2(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Bachelors').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()
    #
    # def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     self.upload_image3(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Bachelors').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()


    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen_btech(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action_bachelors(modal_view), 2)

    def perform_loan_request_action_bachelors(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        # Create a new instance of the LoginScreen
        if not self.validate_image_loaded(self.ids.image_label4):
            validation_errors.append((self.ids.image_label4, "Image not loaded."))
            self.show_validation_error("Please Upload 10 Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label5):
            validation_errors.append((self.ids.image_label5, "Image not loaded."))
            self.show_validation_error("Please Upload 11 Certificates.")
        elif not self.validate_image_loaded(self.ids.image_label6):
            validation_errors.append((self.ids.image_label6, "Image not loaded."))
            self.show_validation_error("Please Upload B.tech Certificates.")
        else:
            lender_screen4 = LenderScreen6(name='LenderScreen6')
            sm.add_widget(lender_screen4)
            sm.current = 'LenderScreen6'

#========================================================================
# class LenderScreen_Edu_Masters(Screen):
#     MAX_IMAGE_SIZE_MB = 2

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager7(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label7", self.upload_image8)

    def check_and_open_file_manager8(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label8", self.upload_image9)

    def check_and_open_file_manager9(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label9", self.upload_image10)

    def check_and_open_file_manager10(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label10", self.upload_image11)

    # def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     if platform == 'android':
    #         if check_permission(Permission.READ_MEDIA_IMAGES):
    #             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #         else:
    #             self.request_media_images_permission()
    #     else:
    #         # For non-Android platforms, directly open the file manager
    #         self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id, upload_function),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')

    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')
    #
    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path3(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')

    def upload_image6(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label1'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image7(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label2'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image8(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['image_label3'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image9(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['mtech'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['image_label4'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path4(path, icon_id, label_id, file_label_id, image_id,
    #                                                    image_label_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         # For other platforms, show the file manager from the root directory
    #         self.file_manager.show('/')

    # def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     upload_function(path)  # Upload the selected image using the provided function
    #     self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     self.file_manager.close()
    #     self.manager.get_screen('LenderScreen5').ids[image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    # def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     self.upload_image2(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Masters').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()
    #
    # def select_path3(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     self.upload_image3(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Masters').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()
    #
    # def select_path4(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
    #     # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
    #     self.upload_image4(path)  # Upload the selected image
    #     self.ids[image_label_id].source = path
    #     file_name = os.path.basename(path)  # Extract file name from the path
    #     self.manager.get_screen('LenderScreen_Edu_Masters').ids[
    #         image_label_id].text = file_name  # Update the label text
    #     self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_7(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_8(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_9(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_10(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen_mas(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_masters_action_mas(modal_view), 2)

    def refresh(self):
        pass

    def perform_masters_action_mas(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        # Create a new instance of the LoginScreen
        if not self.validate_image_loaded(self.ids.image_label7):
            validation_errors.append((self.ids.image_label7, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label8):
            validation_errors.append((self.ids.image_label8, "Image not loaded."))
            self.show_validation_error("Please Upload 11th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label9):
            validation_errors.append((self.ids.image_label9, "Image not loaded."))
            self.show_validation_error("Please Upload B.tech Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label10):
            validation_errors.append((self.ids.image_label10, "Image not loaded."))
            self.show_validation_error("Please Upload Mtech Certificate.")
        else:
            lender_screen4 = LenderScreen6(name='LenderScreen6')
            sm.add_widget(lender_screen4)
            sm.current = 'LenderScreen6'

#=====================================================================
# class LenderScreen_Edu_PHD(Screen):
#     MAX_IMAGE_SIZE_MB = 2
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def check_and_open_file_manager11(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label11",self.upload_image10)

    def check_and_open_file_manager12(self):
        self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label12",self.upload_image11)

    def check_and_open_file_manager13(self):
        self.check_and_open_file_manager("upload_icon3", "upload_label3", "selected_file_label3", "selected_image3",
                                         "image_label13",self.upload_image12)

    def check_and_open_file_manager14(self):
        self.check_and_open_file_manager("upload_icon4", "upload_label4", "selected_file_label4", "selected_image4",
                                         "image_label14",self.upload_image13)

    def check_and_open_file_manager15(self):
        self.check_and_open_file_manager("upload_icon5", "upload_label5", "selected_file_label5", "selected_image5",
                                         "image_label15",self.upload_image14)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id,upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id,upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id,upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id,upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id,upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id,upload_function):
        # self.manager.get_screen('LenderScreen2').ids[image_id].source = path  # Set the source of the Image widget
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen5').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def refresh(self):
        pass

    def update_data_with_file_11(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')
            cursor.execute("UPDATE fin_registration_table SET tenth_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label1.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_12(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET inter_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label2.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_13(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET bachelors_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label3.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_14(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET masters_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label4.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def update_data_with_file_15(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        try:
            log_index = status.index('logged')

            cursor.execute("UPDATE fin_registration_table SET phd_certificate = ? WHERE customer_id = ?",
                           (file_path, row_id_list[log_index]))
            conn.commit()
            self.ids.upload_label5.text = 'Upload Successfully'
        except ValueError:
            print('User is not logged in.')

    def upload_image10(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['tenth_class'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label1'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image11(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['intermediate'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label2'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image12(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['btech'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label3'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image13(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['mtech'] = user_photo_media

            print("Image uploaded successfully.")
            # self.ids['image_label4'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image14(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension not in ['.png', '.jpg', '.jpeg', '.pdf']:
                self.show_validation_error("Unsupported file type. Please upload an image or a PDF.")
                return

            if file_extension in ['.png', '.jpg', '.jpeg']:
                mime_type = 'image/png' if file_extension == '.png' else 'image/jpeg'
            elif file_extension == '.pdf':
                mime_type = 'application/pdf'

            user_photo_media = media.from_file(file_path, mime_type=mime_type)
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['phd'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'

    def go_to_lender_screen_phd(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_phd_action_phd(modal_view), 2)

    def perform_phd_action_phd(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        # Close the modal view after performing the action
        modal_view.dismiss()
        # Get the existing ScreenManager
        sm = self.manager

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label11):
            validation_errors.append((self.ids.image_label11, "Image not loaded."))
            self.show_validation_error("Please Upload 10th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label12):
            validation_errors.append((self.ids.image_label12, "Image not loaded."))
            self.show_validation_error("Please Upload 11th Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label13):
            validation_errors.append((self.ids.image_label13, "Image not loaded."))
            self.show_validation_error("Please Upload B.Tech Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label14):
            validation_errors.append((self.ids.image_label14, "Image not loaded."))
            self.show_validation_error("Please Upload Masters Certificate.")
        elif not self.validate_image_loaded(self.ids.image_label15):
            validation_errors.append((self.ids.image_label15, "Image not loaded."))
            self.show_validation_error("Please Upload PHD Certificate.")
        else:
            lender_screen4 = LenderScreen6(name='LenderScreen6')
            sm.add_widget(lender_screen4)
            sm.current = 'LenderScreen6'


class LenderScreen6(Screen):
    MAX_IMAGE_SIZE_MB = 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.employee_details_box.opacity = 0
        self.ids.business_details_box.opacity = 0
        spinner_data_type = app_tables.fin_lendor_lending_type.search()
        data_list_type = []
        for i in spinner_data_type:
            data_list_type.append(i['lendor_lending_type'])
        self.unique_list_type = []
        for i in data_list_type:
            if i not in self.unique_list_type:
                self.unique_list_type.append(i)
        print(self.unique_list_type)
        if len(self.unique_list_type) >= 1:
            self.ids.loan_type.values = self.unique_list_type
        else:
            self.ids.loan_type.values = ''

        spinner_data_period = app_tables.fin_lendor_lending_period.search()
        data_list_period = []
        for i in spinner_data_period:
            data_list_period.append(i['lendor_lending_period'])
        unique_list_period = []
        for i in data_list_period:
            if i not in unique_list_period:
                unique_list_period.append(i)
        print(unique_list_period)
        if len(unique_list_period) >= 1:
            self.ids.lending_period.values = unique_list_period
        else:
            self.ids.lending_period.values = ''

        spinner_data_employee = app_tables.fin_lendor_employee_type.search()
        data_list_employee = []
        for i in spinner_data_employee:
            data_list_employee.append(i['lendor_employee_type'])
        self.unique_list_employment_type = []
        for i in data_list_employee:
            if i not in self.unique_list_employment_type:
                self.unique_list_employment_type.append(i)
        print(self.unique_list_employment_type)
        if len(self.unique_list_employment_type) >= 1:
            self.ids.employment_type.values = self.unique_list_employment_type
        else:
            self.ids.employment_type.values = ''

        spinner_data_bus = app_tables.fin_lendor_business_type.search()
        data_list_bus = []
        for i in spinner_data_bus:
            data_list_bus.append(i['lendor_business_type'])
        self.unique_list_business_type = []
        for i in data_list_bus:
            if i not in self.unique_list_business_type:
                self.unique_list_business_type.append(i)
        print(self.unique_list_business_type)
        if len(self.unique_list_business_type) >= 1:
            self.ids.spin.values = self.unique_list_business_type
        else:
            self.ids.spin.values = ''
        spinner_data_no = app_tables.fin_lendor_no_of_employees.search()
        data_list_no_of = []
        for i in spinner_data_no:
            data_list_no_of.append(i['lendor_no_of_employees'])
        self.unique_list_no_of_emp = []
        for i in data_list_no_of:
            if i not in self.unique_list_no_of_emp:
                self.unique_list_no_of_emp.append(i)
        print(self.unique_list_no_of_emp)
        if len(self.unique_list_no_of_emp) >= 1:
            self.ids.no_of_employees_working.values = self.unique_list_no_of_emp
        else:
            self.ids.no_of_employees_working.values = ''

        # -----------------------------------------------------------------------------------------------
        # Select Organisation Type
        spinner_data1 = app_tables.fin_lendor_organization_type.search()
        data_list1 = []
        for i in spinner_data1:
            data_list1.append(i['lendor_organization_type'])
        self.unique_list_organisation = []
        for i in data_list1:
            if i not in self.unique_list_organisation:
                self.unique_list_organisation.append(i)
        print(self.unique_list_organisation)
        if len(self.unique_list_organisation) >= 1:
            self.ids.organisation_type.values = self.unique_list_organisation
        else:
            self.ids.organisation_type.values = ''
        # -------------------------------------------------------------------------------------------------
        # Select Salary type
        gender_data = app_tables.fin_lendor_salary_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_salary_type'])
        self.unique_sal = []
        for i in gender_list:
            if i not in self.unique_sal:
                self.unique_sal.append(i)
        print(self.unique_sal)
        if len(self.unique_sal) >= 1:
            self.ids.salary_type.values = self.unique_sal
        else:
            self.ids.salary_type.values = ''
        # =======================================================================
        # Occupation type spinner
        spinner_data_occu = app_tables.fin_occupation_type.search()
        data_list_occu = []
        for i in spinner_data_occu:
            data_list_occu.append(i['occupation_type'])
        self.unique_list_occu = []
        for i in data_list_occu:
            if i not in self.unique_list_occu:
                self.unique_list_occu.append(i)
        print(self.unique_list_occu)
        if len(self.unique_list_occu) >= 1:
            self.ids.occupation_type.values = self.unique_list_occu
        else:
            self.ids.occupation_type.values = ''

        self.update_top_bar_image()
        Clock.schedule_once(self.setup_menu, 0.5)  # Schedule menu setup after a delay

    def update_top_bar_image(self):
        # Replace with your Anvil server call to fetch email
        log_email = anvil.server.call("another_method")

        # Replace with your Anvil table search method to fetch profile data
        profile = app_tables.fin_user_profile.search()

        # Initialize lists to store profile data
        email_user = []
        name_list = []
        investment = []
        user_age = []
        p_customer_id = []
        ascend_score = []
        emp_type = []
        profile_list = []

        # Extract data from the profile list
        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            investment.append(i['investment'])
            user_age.append(i['user_age'])
            p_customer_id.append(i['customer_id'])
            ascend_score.append(i['ascend_value'])
            emp_type.append(i['profession'])
            profile_list.append(i['user_photo'])  # Assuming 'user_photo' is the key for the photo

        # Find the index of log_email in email_user list
        log_index = email_user.index(log_email) if log_email in email_user else 0

        top_bar = self.ids.bar

        if profile_list[log_index] is not None:
            image_data = profile_list[log_index]
            try:
                # Load image data into CoreImage texture
                print(isinstance(image_data, bytes), isinstance(image_data, str), image_data)
                if isinstance(image_data, bytes):
                    profile_texture_io = BytesIO(image_data)
                elif isinstance(image_data, str):
                    image_data_binary = base64.b64decode(image_data)
                    profile_texture_io = BytesIO(image_data_binary)
                elif isinstance(image_data, LazyMedia):
                    image_data_bytes = image_data.get_bytes()
                    profile_texture_io = BytesIO(image_data_bytes)
                else:
                    raise ValueError("Unsupported image data type")

                # Create CoreImage texture
                photo_texture = CoreImage(profile_texture_io, ext='png').texture

                # Save the texture to a temporary file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                    temp_file.write(profile_texture_io.getvalue())
                    temp_file_path = temp_file.name

                # Update right_action_items with the temp file path
                top_bar.right_action_items = [
                    [temp_file_path, lambda x: self.account()]
                ]

            except Exception as e:
                print(f"Error loading photo texture: {e}")

        else:
            # No profile picture available, set a default image or action
            top_bar.right_action_items = [
                ['icon8.png', lambda x: self.account()]
            ]

    def setup_menu(self, *args):
        menu_items = [
            {
                "text": "Profile",
                "viewclass": "IconListItem",
                "icon": "account-circle",
                "on_release": lambda x="Profile": self.menu_callback(x),
            },
            {
                "viewclass": "IconListItem",
                "text": "Logout",
                "icon": "logout",
                "on_release": lambda x="Logout": self.logout(),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.bar.ids.right_actions,
            items=menu_items,
            position="bottom",
            width_mult=3,
        )

    def menu_callback(self, item):
        print(f"Menu item clicked: {item}")

    def account(self):
        self.menu.open()
    def update_person_details(self, spinner):
        spinner = self.ids.loan_type.text
        print(spinner)
        if spinner not in self.unique_list_type:
            self.show_validation_error('Select valid Loan type')
            return

        # List of all box layouts
        all_boxes = ['employee_details_box', 'business_details_box']

        # Map spinner_id to the corresponding box id
        spinner_to_box = {
            'individual': 'employee_details_box',
            'Individual': 'employee_details_box',
            'institutional': 'business_details_box',
            'Institutional': 'business_details_box'
        }

        selected_box_id = spinner_to_box.get(spinner)

        # Get the parent layout of the boxes
        parent_layout = self.ids.parent_layout_id  # Replace with the actual id of the parent layout

        # Hide all boxes
        for box_id in all_boxes:
            box = self.ids[box_id]
            box.opacity = 0

        # Show the selected box
        if selected_box_id:
            selected_box = self.ids[selected_box_id]
            selected_box.opacity = 1

        # Remove all boxes from the parent layout
        for box_id in all_boxes:
            box = self.ids[box_id]
            if box.parent:
                parent_layout.remove_widget(box)

        # Re-add boxes to the parent layout in order, with the visible box on top
        if selected_box_id:
            parent_layout.add_widget(self.ids[selected_box_id])
        for box_id in all_boxes:
            if box_id != selected_box_id:
                parent_layout.add_widget(self.ids[box_id])

        self.adjust_screen_height()
        print(spinner)

    def adjust_screen_height(self):
        height = 0
        for box_id in ['employee_details_box', 'business_details_box']:
            box = self.ids[box_id]
            if box.opacity == 1:
                height += box.height
        self.height = height

    def validate_zip_code_text(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only alphabetic characters
        if not zip_code_text.isalpha():
            zip_code.helper_text = "Should contain only alphabetic characters"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def validate_zip_code_numchar(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains both alphabetic characters and numeric digits
        has_alpha = any(char.isalpha() for char in zip_code_text)
        has_digit = any(char.isdigit() for char in zip_code_text)

        if has_alpha or has_digit:
            zip_code.helper_text = ""
            zip_code.error = False
        else:
            zip_code.helper_text = "Contain characters and numbers."
            zip_code.error = True

    def on_image_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.show_image_popup(instance.source)

    def show_image_popup(self, image_source):
        layout = BoxLayout(orientation='vertical')

        popup_img = Image(source=image_source)
        layout.add_widget(popup_img)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.close_popup)
        layout.add_widget(close_button)

        self.popup = Popup(title='Image Preview',
                           content=layout,
                           size_hint=(0.8, 0.8))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

    def validate_zip_code(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only numeric characters
        if not zip_code_text.isdigit():
            zip_code.helper_text = "Should contain only numbers"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def next_pressed(self, spinner, investment, spinner2):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(spinner, investment, spinner2, modal_view), 2)

    def perform_data_addition_action4(self, spinner, spinner2, investment, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([spinner, spinner2, investment]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if there are missing fields

        if spinner not in spinner == 'Select Loan Type':
            self.show_validation_error('Select valid Loan type')
            return
        if spinner2 not in spinner2 == 'Select Lending Period':
            self.show_validation_error('Select valid Lending Period')
            return
        if investment.isdigit():
            investment = float(investment)
            if investment <= 100000:
                self.show_validation_error("Investment amount must be greater than or equal to 1 lakh.")
            else:
                self.show_validation_error("Invalid investment amount.")

    # ===============================================================================================

    # Business Details
    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_last_six_months_turnover_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.last_six_months_turnover.input_type = 'number'

    def check_and_open_file_manager_bus_1(self):
        self.check_and_open_file_manager_bus1("upload_icon1", "upload_label1", "selected_file_label1",
                                              "selected_image1",
                                              "image_label1", self.upload_image_bus_1)

    def check_and_open_file_manager_bus_2(self):
        self.check_and_open_file_manager_bus2("upload1", "upload_label_veri", "selected_file_label1", "selected_image1",
                                              "upload_label_verification_document", self.upload_image_bus_2)

    def check_and_open_file_manager_bus1(self, icon_id, label_id, file_label_id, image_id, image_label_id,
                                         upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def check_and_open_file_manager_bus2(self, icon_id, label_id, file_label_id, image_id, image_label_id,
                                         upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image_bus_1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image_bus_2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['proof_verification'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen7').ids[
            image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')
        cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data_business_details(self, business_name, business_location, business_address, no_of_emp, industry_type,
                                  last_six_months_turnover, year_of_estd, cin, din, reg_addres, investment, loan_type,
                                  lending_period):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action_bus(business_name, business_location, business_address,
                                                             no_of_emp, industry_type, last_six_months_turnover,
                                                             year_of_estd, cin, din, reg_addres, investment, loan_type,
                                                             lending_period,
                                                             modal_view), 2)

    def calculate_age(self, last_six_months_turnover):
        today = datetime.today()
        dob = datetime.strptime(last_six_months_turnover, '%Y-%m-%d')
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_cancel(self, instance, time):
        self.ids.date_textfield.text = "You Clicked Cancel!"

    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        self.ids.year_of_estd.text = str(value)

    def perform_data_addition_action_bus(self, business_name, business_location, business_address, no_of_emp,
                                         industry_type, last_six_months_turnover, year_of_estd, cin, din, reg_addres,
                                         investment, loan_type, lending_period, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        if not all(
                [business_name, business_location, business_address, no_of_emp, industry_type, last_six_months_turnover,
                 cin, din, reg_addres, year_of_estd]):
            # Display a validation error dialog
            self.show_validation_error("Please fill all mandatory fields.")
            return  # Prevent further execution if any field is missing

        if last_six_months_turnover == 'Enter Year of Estd *':
            self.show_validation_error('Select Year of ESTD *')
            return
        print(last_six_months_turnover)
        if len(business_name) < 3:
            self.show_validation_error('Enter a valid business Name')
            return
        if business_location not in self.unique_list_business_type:
            self.show_validation_error('Select valid business type')
            return
        if len(business_address) < 3:
            self.show_validation_error('Enter a valid business address')
            return
        if no_of_emp not in self.unique_list_no_of_emp:
            self.show_validation_error('Select a valid no of employees')
            return
        if len(industry_type) < 3:
            self.show_validation_error('Select a valid industry type')
            return
        if len(last_six_months_turnover) < 3:
            self.show_validation_error('Enter a valid last six months turnover')
            return
        if len(cin) < 3:
            self.show_validation_error("Enter a valid CIN.")
            return
        if len(din) < 3:
            self.show_validation_error("Enter a valid DIN")
            return
        if len(reg_addres) < 3:
            self.show_validation_error("Enter a valid Registration Address")
            return

        # try:
        #     dob = datetime.strptime(year_of_estd, "%Y-%m-%d")
        # except ValueError:
        #     self.show_validation_error("Please enter a valid Year of Establishment in the format YYYY-MM-DD")
        #     return

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET business_name = ?, business_type = ?, business_address = ?, no_of_employees_working=?,industry_type = ?, last_six_months_turnover = ?, year_of_estd = ?,CIN = ?, DIN = ?, registered_office_address = ?,self_employment = ? WHERE customer_id = ?",
                (business_name, business_location, business_address, no_of_emp, industry_type, last_six_months_turnover,
                 year_of_estd, cin, din, reg_addres, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        # id_list = []
        id_list = [i['email_user'] for i in data]
        investment = ""
        email_id=""
        customer_id= ""
        lending_period = ""
        lending_type = ""
        # for i in data:
        #     id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['business_name'] = business_name
            data[index]['business_add'] = business_address
            data[index]['business_type'] = business_location
            data[index]['employees_working'] = no_of_emp
            data[index]['industry_type'] = industry_type
            data[index]['six_month_turnover'] = year_of_estd
            data[index]['year_of_estd'] = last_six_months_turnover
            age = self.calculate_age(last_six_months_turnover)
            data[index]['business_age'] = age
            data[index]['cin'] = cin
            data[index]['din'] = din
            data[index]['registered_off_add'] = reg_addres

            existing_record = app_tables.fin_lender.get(email_id=email_id,)
            if not existing_record:
                app_tables.fin_lender.add_row(investment=investment,
                                              lending_period=lending_period,
                                              lending_type=lending_type)
            else:
                # Optionally, update the existing record if needed
                # existing_record.update(user_name=data[index]['full_name'], ...)
                print(f"Record for {user_email} already exists. Skipping insertion.")
        else:
            print('no email found')

        if not self.validate_image_loaded(self.ids.image_label1):
            validation_errors.append((self.ids.image_label1, "Image not loaded."))
            self.show_validation_error("Please Upload Last 6 Months Bank Statements.")
        elif not self.validate_image_loaded(self.ids.upload_label_verification_document):
            validation_errors.append((self.ids.upload_label_verification_document, "Image not loaded."))
            self.show_validation_error("Please Upload verified certificate.")
        else:
            sm = self.manager
            borrower_screen = LenderScreen7(name='LenderScreen7')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen7'

    # ===============================================================================================================================
    # Employe(screen12)
    def get_email(self):
        return anvil.server.call('another_method')

    def upload_image_emp1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['emp_id_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image_emp2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')
            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")

        except Exception as e:
            print(f"Error uploading image: {e}")

    def on_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.annual_salary.input_type = 'number'

    def check_and_open_file_manager_emp1(self):
        self.check_and_open_file_manager("emp1", "upload_label1", "selected_file_label1", "selected_image1",
                                         "image_label_emp1", self.upload_image_emp1)

    def check_and_open_file_manager_emp2(self):
        self.check_and_open_file_manager("emp2", "upload_label2", "selected_file_label2", "selected_image2",
                                         "image_label_emp2", self.upload_image_emp2)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
                                                       image_label_id, upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
        upload_function(path)  # Upload the selected image
        self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        file_name = os.path.basename(path)  # Extract file name from the path
        self.manager.get_screen('LenderScreen6').ids[image_label_id].text = file_name  # Update the label text
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants):
            # All grants are truthy, permission granted, open the file manager
            self.file_manager_open()
        else:
            # At least one grant is falsy, permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def update_data_with_file_1(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label1.text = 'Upload Successfully'

    def update_data_with_file_2(self, file_path):
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        log_index = status.index('logged')

        cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
                       (file_path, row_id_list[log_index]))
        conn.commit()
        self.ids.upload_label2.text = 'Upload Successfully'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data_employment_details(self, investment, loan_type, lending_period, company_name, organisation_type,
                                    occupation_type, company_address, landmark,
                                    employment_type, annual_salary, salary_type, designation, business_number):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action_employment(investment, loan_type, lending_period, company_name,
                                                                    organisation_type, occupation_type,
                                                                    company_address, landmark, employment_type,
                                                                    annual_salary, salary_type, designation,
                                                                    business_number, modal_view), 2)

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            widget.line_color_normal = (1, 0, 0, 1)  # Red color for the line when not focused
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'

    def validate_image_loaded(self, image_label):
        if not image_label.source or 'error.png' in image_label.source:  # Adjust 'error.png' as per your placeholder image
            return False
        return True

    def perform_data_addition_action_employment(self, company_name, organisation_type, occupation_type, company_address,
                                                landmark, employment_type, annual_salary, salary_type, designation,
                                                business_number, investment, loan_type, lending_period, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([company_name, organisation_type, occupation_type, company_address, landmark, employment_type,
                    annual_salary, salary_type, designation, business_number]):
            # Display a validation error dialog
            self.show_validation_error("Please fill all mandatory fields.")
            return  # Prevent further execution if any field is missing
        if employment_type not in self.unique_list_employment_type:
            self.show_validation_error('Select a valid employment type')
            return
        if len(company_name) < 3:
            self.show_validation_error('Enter a valid company name')
            return
        if organisation_type not in self.unique_list_organisation:
            self.show_validation_error('Select a valid organisation type')
            return
        if len(annual_salary) < 3 and not annual_salary.isdigit():
            self.show_validation_error("Please Enter Annual Salary.")
            return
        if len(designation) < 3:
            self.show_validation_error("Please Enter Valid Designation.")
            return
        if len(company_address) < 3:
            self.show_validation_error("Please Enter Valid Company Address.")
            return
        if len(landmark) < 3:
            self.show_validation_error("Please Enter Valid Landmark.")
            return
        if occupation_type not in self.unique_list_occu:
            self.show_validation_error('Select a Occupation type')
            return
        if salary_type not in self.unique_sal:
            self.show_validation_error('Select a valid salary type')
            return
        if not business_number.isdigit() or len(business_number) != 10:
            self.show_validation_error("Please Enter Valid Business Number.")
            return
        # if not all([salary_type]):
        #     # Display a validation error dialog
        #     self.show_validation_error("Please fill in all fields.")
        #     return  # Prevent further execution if any field is missing

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET annual_salary = ?, designation = ?, company_name = ?, employment_type = ?,salary_type = ?,organization_type = ?,company_address = ?, landmark = ?, business_number = ?, occupation_type = ? WHERE customer_id = ?",
                (company_name, organisation_type, occupation_type, company_address, landmark, employment_type,
                 annual_salary, salary_type, designation, business_number, annual_salary, designation,
                 row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        investment = ""
        customer_id= ""
        email_id=""
        lending_period = ""
        lending_type = ""
        if user_email in id_list:
            index = id_list.index(user_email)
            print(company_name)
            print(occupation_type)
            print(organisation_type)
            print(company_address)
            print(landmark)
            print(employment_type)
            print(annual_salary)
            print(salary_type)
            print(business_number)

            data[index]['company_name'] = company_name
            data[index]['occupation_type'] = occupation_type
            data[index]['organization_type'] = organisation_type
            data[index]['company_address'] = company_address
            data[index]['company_landmark'] = landmark
            data[index]['employment_type'] = employment_type
            data[index]['annual_salary'] = annual_salary
            data[index]['salary_type'] = salary_type
            data[index]['designation'] = designation
            data[index]['business_no'] = business_number

            existing_record = app_tables.fin_lender.get(email_id=email_id,)
            if not existing_record:
                app_tables.fin_lender.add_row(investment=investment,
                                              lending_period=lending_period,
                                              lending_type=lending_type)
            else:
                # Optionally, update the existing record if needed
                # existing_record.update(user_name=data[index]['full_name'], ...)
                print(f"Record for {user_email} already exists. Skipping insertion.")
        else:
            print('email not found')

        validation_errors = []

        if validation_errors:
            self.show_validation_errors(validation_errors)
            return

        if not self.validate_image_loaded(self.ids.image_label_emp1):
            validation_errors.append((self.ids.image_label_emp1, "Image not loaded."))
            self.show_validation_error("Please Upload Employee ID.")
        elif not self.validate_image_loaded(self.ids.image_label_emp2):
            validation_errors.append((self.ids.image_label_emp2, "Image not loaded."))
            self.show_validation_error("Please Upload 6 Months Bank Statements.")
        else:
            sm = self.manager
            borrower_screen = LenderScreen7(name='LenderScreen7')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreen7'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_company_pincode_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.company_pincode.input_type = 'number'

    def on_business_phone_number_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.business_number.input_type = 'number'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def on_investment_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.investment.input_type = 'number'

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen5'


# class LenderScreenInstitutionalForm1(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         spinner_data = app_tables.fin_lendor_business_type.search()
#         data_list = []
#         for i in spinner_data:
#             data_list.append(i['lendor_business_type'])
#         unique_list = []
#         for i in data_list:
#             if i not in unique_list:
#                 unique_list.append(i)
#         print(unique_list)
#         if len(unique_list) >= 1:
#             self.ids.spin.values = ['Select Business Type'] + unique_list
#         else:
#             self.ids.spin.values = ['Select Business Type']

#         spinner_data = app_tables.fin_lendor_no_of_employees.search()
#         data_list = []
#         for i in spinner_data:
#             data_list.append(i['lendor_no_of_employees'])
#         unique_list = []
#         for i in data_list:
#             if i not in unique_list:
#                 unique_list.append(i)
#         print(unique_list)
#         if len(unique_list) >= 1:
#             self.ids.spinner_id.values = ['Select No.Of Employees Working'] + unique_list
#         else:
#             self.ids.spinner_id.values = ['Select No.Of Employees Working']

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def add_data(self, business_name, business_address, business_type, no_of_employees_working):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(
#             lambda dt: self.perform_data_addition_action4(business_name, business_type, no_of_employees_working,
#                                                           business_address,
#                                                           modal_view), 2)

#     def perform_data_addition_action4(self, business_name, business_type, no_of_employees_working, business_address,
#                                       modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([business_name, business_address, business_type, no_of_employees_working]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if there are missing fields
#         if not re.match(r'^[a-zA-Z\s]+$', business_name):
#             self.show_validation_error('Enter a valid business Name')
#             return
#         if len(business_address) < 3:
#             self.show_validation_error('Enter a valid business address')
#             return
#         if business_type not in business_type == 'Select Business Type':
#             self.show_validation_error('Select valid business type')
#             return
#         if no_of_employees_working not in no_of_employees_working == 'Select No.Of Employees Working':
#             self.show_validation_error('Select valid no of employees')
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute(
#                 "UPDATE fin_registration_table SET business_name = ?, business_address = ? WHERE customer_id = ?",
#                 (business_name, business_address, row_id_list[log_index]))
#             conn.commit()
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])

#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['business_name'] = business_name
#             data[index]['business_add'] = business_address
#             data[index]['business_type'] = business_type
#             data[index]['employees_working'] = no_of_employees_working
#         else:
#             print('no email found')
#         sm = self.manager
#         lender_screen = LenderScreenInstitutionalForm2(name='LenderScreenInstitutionalForm2')
#         sm.add_widget(lender_screen)
#         sm.transition.direction = 'left'  # Set the transition direction explicitly
#         sm.current = 'LenderScreenInstitutionalForm2'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreen6'


# class LenderScreenInstitutionalForm2(Screen):
#     MAX_IMAGE_SIZE_MB = 2

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def calculate_age(self, year_of_estd):
#         today = datetime.today()
#         dob = datetime.strptime(year_of_estd, '%Y-%m-%d')
#         age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
#         return age

#     def add_data(self, industry_type, last_six_months_turnover, year_of_estd):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(
#             lambda dt: self.perform_data_addition_action4(industry_type, last_six_months_turnover, year_of_estd,
#                                                           modal_view), 2)

#     def check_and_open_file_manager1(self):
#         self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
#                                          "image_label1", self.upload_image)

#     def get_email(self):
#         return anvil.server.call('another_method')

#     def upload_image(self, file_path):
#         try:
#             if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
#                 self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
#                 return
#             user_photo_media = media.from_file(file_path, mime_type='image/png')
#             email = self.get_email()
#             data = app_tables.fin_user_profile.search(email_user=email)

#             if not data:
#                 print("No data found for email:", email)
#                 return

#             user_data = data[0]

#             # Update user_photo column with the media object
#             user_data['last_six_month_bank_proof'] = user_photo_media

#             print("Image uploaded successfully.")
#             self.ids['image_label1'].source = ''

#         except Exception as e:
#             print(f"Error uploading image: {e}")

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         if platform == 'android':
#             if check_permission(Permission.READ_MEDIA_IMAGES):
#                 self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
#             else:
#                 self.request_media_images_permission()
#         else:
#             # For non-Android platforms, directly open the file manager
#             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

#     def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         self.file_manager = MDFileManager(
#             exit_manager=self.exit_manager,
#             select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
#                                                        image_label_id, upload_function),
#         )
#         if platform == 'android':
#             primary_external_storage = "/storage/emulated/0"
#             self.file_manager.show(primary_external_storage)
#         else:
#             # For other platforms, show the file manager from the root directory
#             self.file_manager.show('/')

#     def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         upload_function(path)  # Upload the selected image using the provided function
#         self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
#         self.file_manager.close()
#         # self.manager.get_screen('LenderScreenInstitutionalForm2').ids[
#         #     image_label_id].text = file_name  # Update the label text
#         # self.file_manager.close()

#     def exit_manager(self, *args):
#         self.file_manager.close()

#     def on_estd_touch_down(self):
#         self.ids.year_of_estd.input_type = 'number'

#     def request_media_images_permission(self):
#         request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

#     def permission_callback(self, permissions, grants):
#         if all(grants.values()):
#             # Permission granted, open the file manager
#             self.file_manager_open()
#         else:
#             # Permission denied, show a modal view
#             self.show_permission_denied()

#     def show_permission_denied(self):
#         view = ModalView()
#         view.add_widget(Button(
#             text='Permission NOT granted.\n\n' +
#                  'Tap to quit app.\n\n\n' +
#                  'If you selected "Don\'t Allow",\n' +
#                  'enable permission with App Settings.',
#             on_press=self.bye)
#         )
#         view.open()

#     def update_data_with_file_1(self, file_path):
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#         log_index = status.index('logged')
#         cursor.execute("UPDATE fin_registration_table SET last_six_months_turnover_file = ? WHERE customer_id = ?",
#                        (file_path, row_id_list[log_index]))
#         conn.commit()
#         self.ids.upload_label1.text = 'Upload Successfully'

#     def perform_data_addition_action4(self, industry_type, last_six_months_turnover, year_of_estd,
#                                       modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([industry_type, last_six_months_turnover, year_of_estd]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if there are missing fields
#         if not re.match(r'^[a-zA-Z]{3,}$', industry_type):
#             self.show_validation_error("Enter a valid industryy type.")
#             return
#         if len(last_six_months_turnover) < 3 or not last_six_months_turnover.isdigit():
#             self.show_validation_error("Enter a valid last six months turnover.")
#             return
#         try:
#             dob = datetime.strptime(year_of_estd, "%Y-%m-%d")

#         except ValueError:
#             self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute(
#                 "UPDATE fin_registration_table SET year_of_estd = ? WHERE customer_id = ?",
#                 (year_of_estd, row_id_list[log_index]))
#             conn.commit()
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])
#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['year_of_estd'] = year_of_estd
#             age = self.calculate_age(year_of_estd)
#             data[index]['business_age'] = age
#             data[index]['industry_type'] = industry_type
#             data[index]['six_month_turnover'] = last_six_months_turnover
#         else:
#             print('email not found')
#         # self.manager.current = 'LenderScreenInstitutionalForm3'
#         sm = self.manager
#         lender_screen = LenderScreenInstitutionalForm3(name='LenderScreenInstitutionalForm3')
#         sm.add_widget(lender_screen)
#         sm.transition.direction = 'left'  # Set the transition direction explicitly
#         sm.current = 'LenderScreenInstitutionalForm3'

#     def on_last_six_months_turnover_touch_down(self):
#         # Change keyboard mode to numeric when the mobile number text input is touched
#         self.ids.last_six_months_turnover.input_type = 'number'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreenInstitutionalForm1'


# class LenderScreenInstitutionalForm3(Screen):
#     MAX_IMAGE_SIZE_MB = 2

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     def check_and_open_file_manager1(self):
#         self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
#                                          "image_label1", self.upload_image)

#     def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         if platform == 'android':
#             if check_permission(Permission.READ_MEDIA_IMAGES):
#                 self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
#             else:
#                 self.request_media_images_permission()
#         else:
#             # For non-Android platforms, directly open the file manager
#             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

#     def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         self.file_manager = MDFileManager(
#             exit_manager=self.exit_manager,
#             select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
#                                                        image_label_id, upload_function),
#         )
#         if platform == 'android':
#             primary_external_storage = "/storage/emulated/0"
#             self.file_manager.show(primary_external_storage)
#         else:
#             # For other platforms, show the file manager from the root directory
#             self.file_manager.show('/')

#     def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         upload_function(path)  # Upload the selected image using the provided function
#         self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
#         self.file_manager.close()  # Extract file name from the path
#         # self.manager.get_screen('LenderScreenInstitutionalForm3').ids[
#         #     image_label_id].text = file_name  # Update the label text
#         # self.file_manager.close()

#     def get_email(self):
#         return anvil.server.call('another_method')

#     def upload_image(self, file_path):
#         try:
#             if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
#                 self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
#                 return
#             user_photo_media = media.from_file(file_path, mime_type='image/png')
#             email = self.get_email()
#             data = app_tables.fin_user_profile.search(email_user=email)

#             if not data:
#                 print("No data found for email:", email)
#                 return

#             user_data = data[0]

#             # Update user_photo column with the media object
#             user_data['proof_verification'] = user_photo_media

#             print("Image uploaded successfully.")
#             self.ids['image_label1'].source = ''

#         except Exception as e:
#             print(f"Error uploading image: {e}")

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def exit_manager(self, *args):
#         self.file_manager.close()

#     def request_media_images_permission(self):
#         request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

#     def permission_callback(self, permissions, grants):
#         if all(grants.values()):
#             # Permission granted, open the file manager
#             self.file_manager_open()
#         else:
#             # Permission denied, show a modal view
#             self.show_permission_denied()

#     def show_permission_denied(self):
#         view = ModalView()
#         view.add_widget(Button(
#             text='Permission NOT granted.\n\n' +
#                  'Tap to quit app.\n\n\n' +
#                  'If you selected "Don\'t Allow",\n' +
#                  'enable permission with App Settings.',
#             on_press=self.bye)
#         )
#         view.open()

#     def update_data_with_file_1(self, file_path):
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#         log_index = status.index('logged')

#         cursor.execute("UPDATE fin_registration_table SET proof_of_verification_file = ? WHERE customer_id = ?",
#                        (file_path, row_id_list[log_index]))
#         conn.commit()
#         self.ids.upload_label1.text = 'Upload Successfully'

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def add_data(self, cin, din, registered_office_address):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(
#             lambda dt: self.perform_data_addition_action4(registered_office_address, cin, din, modal_view), 2)

#     def perform_data_addition_action4(self, cin, din, registered_office_address, modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([cin, din, registered_office_address]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if there are missing fields
#         if len(cin) < 3:
#             self.show_validation_error("Enter a valid cin.")
#             return
#         if len(din) < 3:
#             self.show_validation_error("Enter a valid din.")
#             return
#         if len(registered_office_address) < 3:
#             self.show_validation_error("Enter a valid registered_office_address.")
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute(
#                 "UPDATE fin_registration_table SET cin = ?,registered_office_address = ?, din = ? WHERE customer_id = ?",
#                 (cin, din, registered_office_address, row_id_list[log_index]))
#             conn.commit()
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])
#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['cin'] = cin
#             data[index]['din'] = din
#             data[index]['registered_off_add'] = registered_office_address

#         else:
#             print('email not found')
#         # self.manager.current = 'LenderScreenInstitutionalForm4'
#         sm = self.manager
#         lender_screen = LenderScreen7(name='LenderScreen7')
#         sm.add_widget(lender_screen)
#         sm.transition.direction = 'left'  # Set the transition direction explicitly
#         sm.current = 'LenderScreen7'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreenInstitutionalForm2'


# class LenderScreenIndividualForm1(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         spinner_data = app_tables.fin_lendor_employee_type.search()
#         data_list = []
#         for i in spinner_data:
#             data_list.append(i['lendor_employee_type'])
#         unique_list = []
#         for i in data_list:
#             if i not in unique_list:
#                 unique_list.append(i)
#         print(unique_list)
#         if len(unique_list) >= 1:
#             self.ids.spinner1.values = ['Select Employment Type'] + unique_list
#         else:
#             self.ids.spinner1.values = ['Select Employment Type']

#         spinner_data = app_tables.fin_lendor_organization_type.search()
#         data_list = []
#         for i in spinner_data:
#             data_list.append(i['lendor_organization_type'])
#         unique_list = []
#         for i in data_list:
#             if i not in unique_list:
#                 unique_list.append(i)
#         print(unique_list)
#         if len(unique_list) >= 1:
#             self.ids.spinner2.values = ['Select Organisation Type'] + unique_list
#         else:
#             self.ids.spinner2.values = ['Select Organisation Type']

#         spinner_data = app_tables.fin_occupation_type.search()
#         data_list = []
#         for i in spinner_data:
#             data_list.append(i['occupation_type'])
#         unique_list = []
#         for i in data_list:
#             if i not in unique_list:
#                 unique_list.append(i)
#         print(unique_list)
#         if len(unique_list) >= 1:
#             self.ids.spinner3.values = ['Select Occupation Type'] + unique_list
#         else:
#             self.ids.spinner3.values = ['Select Occupation Type']

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def add_data(self, spinner1, company_name, spinner2, spinner3):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(
#             lambda dt: self.perform_data_addition_action4(spinner1, company_name, spinner2, spinner3, modal_view), 2)

#     def perform_data_addition_action4(self, spinner1, company_name, spinner2, spinner3, modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([spinner1, company_name, spinner2, spinner3]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if any field is missing
#         if spinner1 not in spinner1 == 'Select Employment Type':
#             self.show_validation_error('Select a valid employment type')
#             return
#         if not re.match(r'^[a-zA-Z\s]{3,}$', company_name):
#             self.show_validation_error('Enter a valid company name')
#             return
#         if spinner2 not in spinner2 == 'Select Organisation Type':
#             self.show_validation_error('Select a valid organisation type')
#             return
#         if spinner3 not in spinner3 == 'Select Occupation Type':
#             self.show_validation_error('Select a valid occupation  type')
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute(
#                 "UPDATE fin_registration_table SET employment_type = ?, company_name = ?, organization_type = ? WHERE customer_id = ?",
#                 (spinner1, company_name, spinner2, row_id_list[log_index]))
#             conn.commit()
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])
#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['employment_type'] = spinner1
#             data[index]['company_name'] = company_name
#             data[index]['organization_type'] = spinner2
#             data[index]['occupation_type'] = spinner3
#         else:
#             print('email not found')
#         sm = self.manager
#         lender_screen = LenderScreenIndividualForm2(name='LenderScreenIndividualForm2')
#         sm.add_widget(lender_screen)
#         sm.transition.direction = 'left'  # Set the transition direction explicitly
#         sm.current = 'LenderScreenIndividualForm2'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreen6'


# class LenderScreenIndividualForm2(Screen):
#     MAX_IMAGE_SIZE_MB = 2
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         gender_data = app_tables.fin_borrower_salary_type.search()
#         gender_list = []
#         for i in gender_data:
#             gender_list.append(i['borrower_salary_type'])
#         self.unique_gender = []
#         for i in gender_list:
#             if i not in self.unique_gender:
#                 self.unique_gender.append(i)
#         print(self.unique_gender)
#         if len(self.unique_gender) >= 1:
#             self.ids.salary_type_id.values = ['Select Salary type'] + self.unique_gender
#         else:
#             self.ids.salary_type_id.values = ['Select Salary type']

#     def get_email(self):
#         return anvil.server.call('another_method')

#     def upload_image(self, file_path):
#         try:
#             if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
#                 self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
#                 return
#             user_photo_media = media.from_file(file_path, mime_type='image/png')
#             email = self.get_email()
#             data = app_tables.fin_user_profile.search(email_user=email)

#             if not data:
#                 print("No data found for email:", email)
#                 return

#             user_data = data[0]

#             # Update user_photo column with the media object
#             user_data['emp_id_proof'] = user_photo_media

#             print("Image uploaded successfully.")
#             self.ids['image_label1'].source = ''
#         except Exception as e:
#             print(f"Error uploading image: {e}")

#     def upload_image1(self, file_path):
#         try:
#             if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
#                 self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
#                 return
#             user_photo_media = media.from_file(file_path, mime_type='image/png')
#             email = self.get_email()
#             data = app_tables.fin_user_profile.search(email_user=email)

#             if not data:
#                 print("No data found for email:", email)
#                 return

#             user_data = data[0]

#             # Update user_photo column with the media object
#             user_data['last_six_month_bank_proof'] = user_photo_media

#             print("Image uploaded successfully.")
#             self.ids['image_label2'].source = ''

#         except Exception as e:
#             print(f"Error uploading image: {e}")

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def check_and_open_file_manager1(self):
#         self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1",
#                                          "image_label1", self.upload_image)

#     def check_and_open_file_manager2(self):
#         self.check_and_open_file_manager("upload_icon2", "upload_label2", "selected_file_label2", "selected_image2",
#                                          "image_label2", self.upload_image1)

#     def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         if platform == 'android':
#             if check_permission(Permission.READ_MEDIA_IMAGES):
#                 self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)
#             else:
#                 self.request_media_images_permission()
#         else:
#             # For non-Android platforms, directly open the file manager
#             self.file_manager_open(icon_id, label_id, file_label_id, image_id, image_label_id, upload_function)

#     def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         self.file_manager = MDFileManager(
#             exit_manager=self.exit_manager,
#             select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,
#                                                        image_label_id, upload_function),
#         )
#         if platform == 'android':
#             primary_external_storage = "/storage/emulated/0"
#             self.file_manager.show(primary_external_storage)
#         else:
#             # For other platforms, show the file manager from the root directory
#             self.file_manager.show('/')

#     # def file_manager_open(self, icon_id, label_id, file_label_id, image_id, image_label_id):
#     #     self.file_manager = MDFileManager(
#     #         exit_manager=self.exit_manager,
#     #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id,
#     #                                                    image_label_id),
#     #     )
#     #     if platform == 'android':
#     #         primary_external_storage = "/storage/emulated/0"
#     #         self.file_manager.show(primary_external_storage)
#     #     else:
#     #         # For other platforms, show the file manager from the root directory
#     #         self.file_manager.show('/')

#     def select_path1(self, path, icon_id, label_id, file_label_id, image_id, image_label_id, upload_function):
#         upload_function(path)  # Upload the selected image using the provided function
#         self.ids[image_label_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
#         self.file_manager.close()
#         # self.manager.get_screen('LenderScreenIndividualForm2').ids[
#         #     image_label_id].text = file_name  # Update the label text
#         # self.file_manager.close()

#     # def select_path2(self, path, icon_id, label_id, file_label_id, image_id, image_label_id):
#     #     self.upload_image1(path)  # Upload the selected image
#     #     self.ids[image_label_id].source = path
#     #     file_name = os.path.basename(path)  # Extract file name from the path
#     #     self.manager.get_screen('LenderScreenIndividualForm2').ids[
#     #         image_label_id].text = file_name  # Update the label text
#     #     self.file_manager.close()

#     def exit_manager(self, *args):
#         self.file_manager.close()

#     def request_media_images_permission(self):
#         request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

#     def permission_callback(self, permissions, grants):
#         if all(grants.values()):
#             # Permission granted, open the file manager
#             self.file_manager_open()
#         else:
#             # Permission denied, show a modal view
#             self.show_permission_denied()

#     def show_permission_denied(self):
#         view = ModalView()
#         view.add_widget(Button(
#             text='Permission NOT granted.\n\n' +
#                  'Tap to quit app.\n\n\n' +
#                  'If you selected "Don\'t Allow",\n' +
#                  'enable permission with App Settings.',
#             on_press=self.bye)
#         )
#         view.open()

#     def update_data_with_file_1(self, file_path):
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute("UPDATE fin_registration_table SET employee_id_file = ? WHERE customer_id = ?",
#                            (file_path, row_id_list[log_index]))
#             conn.commit()
#             self.ids.upload_label1.text = 'Upload Successfully'
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")

#     def update_data_with_file_2(self, file_path):
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#         log_index = status.index('logged')

#         cursor.execute("UPDATE fin_registration_table SET six_months_bank_statement_file = ? WHERE customer_id = ?",
#                        (file_path, row_id_list[log_index]))
#         conn.commit()
#         self.ids.upload_label2.text = 'Upload Successfully'

#     def add_data(self, annual_salary, designation):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(lambda dt: self.perform_data_addition_action4(annual_salary, designation, modal_view), 2)

#     def perform_data_addition_action4(self, annual_salary, designation, modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([annual_salary, designation]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if any field is missing
#         if not re.match(r'^[a-zA-Z\s]{2,}$', designation):
#             self.show_validation_error("Please Enter Valid designation.")
#             return
#         if len(annual_salary) < 3 and not annual_salary.isdigit():
#             self.show_validation_error("Please Enter Valid Company Number.")
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')

#             cursor.execute(
#                 "UPDATE fin_registration_table SET annual_salary = ?, designation = ? WHERE customer_id = ?",
#                 (annual_salary, designation, row_id_list[log_index]))
#             conn.commit()
#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])
#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['annual_salary'] = annual_salary
#             data[index]['designation'] = designation
#         else:
#             print('email not found')
#         sm = self.manager

#         # Create a new instance of the LenderScreenIndividualForm3
#         lender_screen = LenderScreenIndividualForm3(name='LenderScreenIndividualForm3')

#         # Add the LenderScreenIndividualForm3 to the existing ScreenManager
#         sm.add_widget(lender_screen)

#         # Switch to the LenderScreenIndividualForm3
#         sm.current = 'LenderScreenIndividualForm3'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def on_annual_salary_touch_down(self):
#         # Change keyboard mode to numeric when the mobile number text input is touched
#         self.ids.annual_salary.input_type = 'number'

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreenIndividualForm1'


# class LenderScreenIndividualForm3(Screen):

#     def animate_loading_text(self, loading_label, modal_height):
#         # Define the animation to move the label vertically
#         anim = Animation(y=modal_height - loading_label.height, duration=1) + \
#                Animation(y=0, duration=1)
#         # Loop the animation
#         anim.repeat = True
#         anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
#         anim.start(loading_label)
#         # Store the animation object
#         loading_label.animation = anim  # Store the animation object in a custom attribute

#     def add_data(self, company_address, company_pincode, company_country, landmark, business_number):
#         modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

#         # Create MDLabel with white text color, increased font size, and bold text
#         loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
#                                 theme_text_color="Custom", text_color=[1, 1, 1, 1],
#                                 font_size="50sp", bold=True)

#         # Set initial y-position off-screen
#         loading_label.y = -loading_label.height

#         modal_view.add_widget(loading_label)
#         modal_view.open()

#         # Perform the animation
#         self.animate_loading_text(loading_label, modal_view.height)

#         # Perform the actual action (e.g., fetching loan requests)
#         # You can replace the sleep with your actual logic
#         Clock.schedule_once(
#             lambda dt: self.perform_data_addition_action4(company_address, company_pincode, company_country, landmark,
#                                                           business_number, modal_view), 2)

#     def perform_data_addition_action4(self, company_address, company_pincode, company_country, landmark,
#                                       business_number, modal_view):
#         modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
#         modal_view.dismiss()

#         # Check for missing fields
#         if not all([company_address, company_pincode, company_country, landmark, business_number]):
#             # Display a validation error dialog
#             self.show_validation_error("Please fill in all fields.")
#             return  # Prevent further execution if any field is missing
#         if len(company_address) < 3:
#             self.show_validation_error("Please Enter Valid Company Address.")
#             return
#         if len(company_pincode) < 3 or not company_pincode.isdigit():
#             self.show_validation_error("Please Enter Valid Company Pincode.")
#             return
#         if len(company_country) < 3 or not re.match(r'^[a-zA-Z]+$', company_country):
#             self.show_validation_error("Please Enter Valid Company Country.")
#             return
#         if len(landmark) < 3:
#             self.show_validation_error("Please Enter Valid Landmark.")
#             return
#         if not business_number.isdigit() or len(business_number) not in (10, 12):
#             self.show_validation_error("Please Enter Valid Business Number.")
#             return
#         cursor.execute('select * from fin_users')
#         rows = cursor.fetchall()
#         row_id_list = []
#         status = []
#         email_list = []
#         for row in rows:
#             row_id_list.append(row[0])
#             status.append(row[-1])
#             email_list.append(row[2])
#         if 'logged' in status:
#             log_index = status.index('logged')
#             cursor.execute(
#                 "UPDATE fin_registration_table SET company_address = ?, company_pincode = ?, company_country = ?, landmark = ?, business_number = ? WHERE customer_id = ?",
#                 (company_address, company_pincode, company_country, landmark, business_number, row_id_list[log_index]))
#             conn.commit()

#         else:
#             # Handle the case where the user is not logged in
#             print("User is not logged in.")
#         data = app_tables.fin_user_profile.search()
#         id_list = []
#         for i in data:
#             id_list.append(i['email_user'])
#         user_email = anvil.server.call('another_method')
#         if user_email in id_list:
#             index = id_list.index(user_email)
#             data[index]['company_address'] = company_address
#             data[index]['company_landmark'] = landmark
#             data[index]['business_no'] = business_number
#             data[index]['company_country'] = company_country
#             data[index]['company_pincode'] = company_pincode
#         else:
#             print('email not found')
#         sm = self.manager

#         # Create a new instance of the LenderScreenIndividualBankForm1
#         lender_screen = LenderScreen7(name='LenderScreen7')

#         # Add the LenderScreenIndividualBankForm1 to the existing ScreenManager
#         sm.add_widget(lender_screen)

#         # Switch to the LenderScreenIndividualBankForm1
#         sm.current = 'LenderScreen7'

#     def show_validation_error(self, error_message):
#         dialog = MDDialog(
#             title="Validation Error",
#             text=error_message,
#             size_hint=(0.8, None),
#             height=dp(200),
#             buttons=[
#                 MDRectangleFlatButton(
#                     text="OK",
#                     text_color=(0.043, 0.145, 0.278, 1),
#                     on_release=lambda x: dialog.dismiss()
#                 )
#             ]
#         )
#         dialog.open()

#     def on_company_pin_code_touch_down(self):
#         # Change keyboard mode to numeric when the mobile number text input is touched
#         self.ids.company_pin_code.input_type = 'number'

#     def on_business_phone_number_touch_down(self):
#         # Change keyboard mode to numeric when the mobile number text input is touched
#         self.ids.business_phone_number.input_type = 'number'

#     def go_to_dashboard(self):
#         self.manager.current = 'DashScreen'

#     def on_pre_enter(self):
#         Window.bind(on_keyboard=self.on_back_button)

#     def on_pre_leave(self):
#         Window.unbind(on_keyboard=self.on_back_button)

#     def on_back_button(self, instance, key, scancode, codepoint, modifier):
#         if key == 27:
#             self.go_back()
#             return True
#         return False

#     def go_back(self):
#         self.manager.transition = SlideTransition(direction='right')
#         self.manager.current = 'LenderScreenIndividualForm2'


class LenderScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_marrital_status.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_marrital_status'])
        self.unique_list = []
        for i in data_list:
            if i not in self.unique_list:
                self.unique_list.append(i)
        print(self.unique_list)
        if len(self.unique_list) >= 1:
            self.ids.marital_status_id.values = ['Select Marital Status'] + self.unique_list
        else:
            self.ids.marital_status_id.values = ['Select Marital Status']

        self.update_top_bar_image()
        Clock.schedule_once(self.setup_menu, 0.5)  # Schedule menu setup after a delay


    def update_top_bar_image(self):
        # Replace with your Anvil server call to fetch email
        log_email = anvil.server.call("another_method")

        # Replace with your Anvil table search method to fetch profile data
        profile = app_tables.fin_user_profile.search()

        # Initialize lists to store profile data
        email_user = []
        name_list = []
        investment = []
        user_age = []
        p_customer_id = []
        ascend_score = []
        emp_type = []
        profile_list = []

        # Extract data from the profile list
        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            investment.append(i['investment'])
            user_age.append(i['user_age'])
            p_customer_id.append(i['customer_id'])
            ascend_score.append(i['ascend_value'])
            emp_type.append(i['profession'])
            profile_list.append(i['user_photo'])  # Assuming 'user_photo' is the key for the photo

        # Find the index of log_email in email_user list
        log_index = email_user.index(log_email) if log_email in email_user else 0

        top_bar = self.ids.bar

        if profile_list[log_index] is not None:
            image_data = profile_list[log_index]
            try:
                # Load image data into CoreImage texture
                print(isinstance(image_data, bytes), isinstance(image_data, str), image_data)
                if isinstance(image_data, bytes):
                    profile_texture_io = BytesIO(image_data)
                elif isinstance(image_data, str):
                    image_data_binary = base64.b64decode(image_data)
                    profile_texture_io = BytesIO(image_data_binary)
                elif isinstance(image_data, LazyMedia):
                    image_data_bytes = image_data.get_bytes()
                    profile_texture_io = BytesIO(image_data_bytes)
                else:
                    raise ValueError("Unsupported image data type")

                # Create CoreImage texture
                photo_texture = CoreImage(profile_texture_io, ext='png').texture

                # Save the texture to a temporary file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                    temp_file.write(profile_texture_io.getvalue())
                    temp_file_path = temp_file.name

                # Update right_action_items with the temp file path
                top_bar.right_action_items = [
                    [temp_file_path, lambda x: self.account()]
                ]

            except Exception as e:
                print(f"Error loading photo texture: {e}")

        else:
            # No profile picture available, set a default image or action
            top_bar.right_action_items = [
                ['icon8.png', lambda x: self.account()]
            ]


    def setup_menu(self, *args):
        menu_items = [
            {
                "text": "Profile",
                "viewclass": "IconListItem",
                "icon": "account-circle",
                "on_release": lambda x="Profile": self.menu_callback(x),
            },
            {
                "viewclass": "IconListItem",
                "text": "Logout",
                "icon": "logout",
                "on_release": lambda x="Logout": self.logout(),
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.bar.ids.right_actions,
            items=menu_items,
            position="bottom",
            width_mult=3,
        )


    def menu_callback(self, item):
        print(f"Menu item clicked: {item}")


    def account(self):
        self.menu.open()


    def update_details(self, marital_status_id):
        if marital_status_id == "Married":
            self.ids.relation_name.values = ["Father", "Mother", "Spouse", "Others"]
        else:
            self.ids.relation_name.values = ["Father", "Mother", "Others"]


    def update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black with full opacity
            Line(width=0.7, rectangle=(instance.x, instance.y, instance.width, instance.height))


    def logout(self):
        # Implement logout functionality here
        print("Logout clicked")
        with open("emails.json", "r+") as file:
            user_data = json.load(file)
            # Check if user_data is a dictionary
            if isinstance(user_data, dict):
                for email, data in user_data.items():
                    if isinstance(data, dict) and data.get("logged_status", False):
                        data["logged_status"] = False
                        data["user_type"] = ""
                        break
                # Move the cursor to the beginning of the file
                file.seek(0)
                # Write the updated data back to the file
                json.dump(user_data, file, indent=4)
                # Truncate any remaining data in the file
                file.truncate()

        # Switch to MainScreen
        self.manager.current = 'prelogin'
        self.menu.dismiss()


    def update_person_details_visibility(self, relation):
        # Remove any existing spouse details box
        self.ids.box.clear_widgets()

        if relation == "Spouse":
            spouse_details = self.ids.box

            self.spouse_name = MDTextField(id='spouse_name', hint_text='Enter Spouse Name *', multiline=False,
                                           helper_text_mode='on_focus', font_size=15, mode="rectangle",
                                           radius=[0, 0, 0, 0])
            self.spouse_name.bind(text=self.spouse_name_validation)
            spouse_details.add_widget(self.spouse_name)

            self.date_box = BoxLayout(
                orientation='horizontal',
                spacing="10dp",
                size_hint=(1, None),
                height=dp(48),
                width=dp(200)
            )

            # Bind the update method to the BoxLayout's size and position updates
            self.date_box.bind(pos=self.update_canvas, size=self.update_canvas)

            self.date_textfield = MDLabel(
                id='date_textfield',
                text=" Enter Marriage Date *",
                font_size="15dp",
                height=dp(40),
                width=dp(200),
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),  # Use text_color instead of hint_text_color
                halign="left",
                valign="middle",
            )

            calendar_button = MDIconButton(
                icon='calendar',
                pos_hint={'center_x': .5, 'center_y': .5}
            )

            calendar_button.bind(on_release=self.show_date_picker)

            self.date_box.add_widget(self.date_textfield)
            self.date_box.add_widget(calendar_button)

            spouse_details.add_widget(self.date_box)

            self.spouse_mobile = MDTextField(id='spouse_mobile', hint_text='Enter Spouse Mobile No *', multiline=False,
                                             helper_text_mode='on_focus',
                                             input_type='number', font_size=15, mode="rectangle")
            self.spouse_mobile.bind(text=self.spouse_mobile_validation)
            spouse_details.add_widget(self.spouse_mobile)

            spouse_profession_label = MDLabel(text='Spouse Profession Type:', halign='left', font_size=15,
                                              font_name='Roboto-Bold', size_hint_y=None, height=dp(20))
            spouse_details.add_widget(spouse_profession_label)

            self.spouse_profession = Spinner(
                text="Select Spouse Profession",
                font_size="15dp",
                multiline=False,
                size_hint=(1, None),
                height=dp(40),
                width=dp(200),  # Adjust color as needed
                background_normal='',
                color=(0, 0, 0, 1),
                values=['Nothing'],
                option_cls='CustomSpinnerOption'

            )
            self.spouse_profession.bind(size=self.update_rect, pos=self.update_rect)

            # Configure canvas for border
            self.spouse_profession.text_size = (self.spouse_profession.width - dp(20), None)

            with self.spouse_profession.canvas.before:
                Color(0, 0, 0, 1)  # Set the color to black with full opacity
                Line(width=0.7, rectangle=(
                    self.spouse_profession.x, self.spouse_profession.y, self.spouse_profession.width,
                    self.spouse_profession.height))

            spouse_details.add_widget(self.spouse_profession)

            self.spouse_company_name = MDTextField(id='spouse_company_name', hint_text='Enter Spouse Company Name *',
                                                   multiline=False,
                                                   helper_text_mode='on_focus', font_size=15, mode="rectangle")
            spouse_details.add_widget(self.spouse_company_name)

            self.spouse_annual_salary = MDTextField(id='spouse_annual_salary', hint_text='Enter Annual Salary *',
                                                    multiline=False,
                                                    helper_text_mode='on_focus', input_type='number', font_size=15,
                                                    mode="rectangle")
            spouse_details.add_widget(self.spouse_annual_salary)

            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            spouse_details.add_widget(self.error_msg)
            spinner_data1 = app_tables.fin_spouse_profession.search()
            data_list1 = []
            for i in spinner_data1:
                data_list1.append(i['spouse_profession'])
            self.unique_list1 = []
            for i in data_list1:
                if i not in self.unique_list1:
                    self.unique_list1.append(i)
            print(self.unique_list1)
            if len(self.unique_list1) >= 1:
                self.spouse_profession.values = self.unique_list1
            else:
                self.spouse_profession.values = []

        # Add other person details widgets based on selected relation
        elif relation == "Father" or relation == "Mother":
            # Add details for father
            person_details_box1 = self.ids.box

            self.person_name = MDTextField(id='person_name', hint_text='Enter Full Name *', multiline=False,
                                           helper_text_mode='on_focus',
                                           halign='left', font_size=15, mode='rectangle')
            self.person_name.bind(text=self.person_name_validtion)
            person_details_box1.add_widget(self.person_name)

            self.date_box1 = BoxLayout(
                orientation='horizontal',
                spacing="10dp",
                size_hint=(1, None),
                height=dp(48),
                width=dp(200)
            )

            # Bind the update method to the BoxLayout's size and position updates
            self.date_box1.bind(pos=self.update_canvas, size=self.update_canvas)

            self.date_textfield1 = MDLabel(
                id='date_textfield',
                text=" Enter Valid Date Of Birth *",
                font_size="15dp",
                height=dp(40),
                width=dp(200),
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),  # Use text_color instead of hint_text_color
                halign="left",
                valign="middle",
            )

            calendar_button = MDIconButton(
                icon='calendar',
                pos_hint={'center_x': .5, 'center_y': .5}
            )

            calendar_button.bind(on_release=self.show_date_picker)

            self.date_box1.add_widget(self.date_textfield1)
            self.date_box1.add_widget(calendar_button)

            person_details_box1.add_widget(self.date_box1)

            self.person_ph_no = MDTextField(id='person_ph_no', hint_text='Enter Phone No *',
                                            helper_text_mode='on_focus', halign='left', input_type='number',
                                            font_size=15, mode='rectangle')
            self.person_ph_no.bind(text=self.person_ph_no_validtion)
            person_details_box1.add_widget(self.person_ph_no)

            self.person_profession = MDTextField(id='person_profession', hint_text='Enter Profession *',
                                                 multiline=False,
                                                 helper_text_mode='on_focus', font_size=15, mode='rectangle')
            self.person_profession.bind(text=self.person_profession_validtion)
            person_details_box1.add_widget(self.person_profession)
            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            person_details_box1.add_widget(self.error_msg)

        elif relation == "Others":
            # Add details for other relations
            person_details_box1 = self.ids.box

            self.relation_name1 = MDTextField(id='relation_name1', hint_text='How is the person related to you',
                                              multiline=False,
                                              helper_text_mode='on_focus', halign='left', font_size=15,
                                              mode='rectangle')
            self.relation_name1.bind(text=self.relation_name1_validation)
            person_details_box1.add_widget(self.relation_name1)

            person_details_box1 = self.ids.box

            self.person_name = MDTextField(id='person_name', hint_text='Enter Full Name *', multiline=False,
                                           helper_text_mode='on_focus',
                                           halign='left', font_size=15, mode='rectangle')
            self.person_name.bind(text=self.person_name_validtion)
            person_details_box1.add_widget(self.person_name)

            self.date_box1 = BoxLayout(
                orientation='horizontal',
                spacing="10dp",
                size_hint=(1, None),
                height=dp(48),
                width=dp(200)
            )

            # Bind the update method to the BoxLayout's size and position updates
            self.date_box1.bind(pos=self.update_canvas, size=self.update_canvas)

            self.date_textfield1 = MDLabel(
                id='date_textfield',
                text=" Enter Valid Date Of Birth *",
                font_size="15dp",
                height=dp(40),
                width=dp(200),
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),  # Use text_color instead of hint_text_color
                halign="left",
                valign="middle",
            )

            calendar_button = MDIconButton(
                icon='calendar',
                pos_hint={'center_x': .5, 'center_y': .5}
            )

            calendar_button.bind(on_release=self.show_date_picker)

            self.date_box1.add_widget(self.date_textfield1)
            self.date_box1.add_widget(calendar_button)

            person_details_box1.add_widget(self.date_box1)

            self.person_ph_no = MDTextField(id='person_ph_no', hint_text='Enter Phone No *',
                                            helper_text_mode='on_focus', halign='left', input_type='number',
                                            font_size=15, mode='rectangle')
            self.person_ph_no.bind(text=self.person_ph_no_validtion)
            person_details_box1.add_widget(self.person_ph_no)

            self.person_profession = MDTextField(id='person_profession', hint_text='Enter Profession *',
                                                 multiline=False,
                                                 helper_text_mode='on_focus', font_size=15, mode='rectangle')
            self.person_profession.bind(text=self.person_profession_validtion)
            person_details_box1.add_widget(self.person_profession)
            self.error_msg = MDLabel(text='', halign='left', font_size=15,
                                     font_name='Roboto-Bold', size_hint_y=None, height=dp(20),
                                     theme_text_color="Custom", text_color='red')
            person_details_box1.add_widget(self.error_msg)

        # Add widgets for other relations as needed


    def update_canvas(self, *args):
        if self.ids.relation_name.text == 'Spouse':
            self.date_box.canvas.before.clear()
            with self.date_box.canvas.before:
                Color(0, 0, 0, 1)  # Black color for the line
                Line(width=0.6, rectangle=(self.date_box.x, self.date_box.y, self.date_box.width, self.date_box.height))
        else:
            self.date_box1.canvas.before.clear()
            with self.date_box1.canvas.before:
                Color(0, 0, 0, 1)  # Black color for the line
                Line(width=0.6,
                     rectangle=(self.date_box1.x, self.date_box1.y, self.date_box1.width, self.date_box1.height))


    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        if self.ids.relation_name.text == 'Spouse':
            self.date_textfield.text = "  " + str(value)
        else:
            self.date_textfield1.text = "  " + str(value)

        # Cancel


    def on_cancel(self, instance, time):
        if self.ids.relation_name.text == 'Spouse':
            self.date_textfield.text = "You Clicked Cancel!"
        else:
            self.date_textfield1.text = "You Clicked Cancel!"


    def show_date_picker(self, instance):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


    def update_rect(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black with full opacity
            Line(width=0.7, rectangle=(instance.x, instance.y, instance.width, instance.height))


    def spouse_name_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_name.helper_text = 'Enter Correct Name'
            self.spouse_name._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_name.helper_text = ''


    def spouse_mobile_validation(self, instance, value):
        if not value.isdigit() or len(value) != 10:
            instance.error = True
            self.spouse_mobile.helper_text = 'Mobile Number should be ten digits'
            self.spouse_mobile._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_mobile.helper_text = ''

    def show_validation_errors(self, validation_errors):
        for widget, error_message in validation_errors:
            widget.error = True
            widget.helper_text_color = (1, 0, 0, 1)
            widget.helper_text = error_message
            widget.helper_text_mode = "on_error"
            widget.line_color_normal = (1, 0, 0, 1)
            if isinstance(widget, MDCheckbox):
                widget.theme_text_color = 'Error'

    def spouse_date_validation(self, instance, value):
        try:
            dob = datetime.strptime(value, "%Y-%m-%d").date()  # Convert to date object
            today = datetime.now().date()
            if dob > today:
                instance.error = True
                self.spouse_date_textfield.helper_text = ' Enter Correct Date Must be greater than today'
                self.spouse_date_textfield._helper_text_color = 'red'
                return
            else:
                instance.error = False
                self.spouse_date_textfield.helper_text = ''
        except ValueError:
            instance.error = True
            self.spouse_date_textfield.helper_text = 'Enter Correct Date like YYYY-MM_DD'
            self.spouse_date_textfield._helper_text_color = 'red'
            return


    def spouse_company_name_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_company_name.helper_text = 'Enter Correct Name'
            self.spouse_company_name._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_company_name.helper_text = ''


    def spouse_annual_salary_validation(self, instance, value):
        if not value.isdigit() or len(value) < 3:
            instance.error = True
            self.spouse_annual_salary.helper_text = 'Enter Correct Annual Salary'
            self.spouse_annual_salary._helper_text_color = 'red'
            return
        else:
            instance.error = False
            self.spouse_company_name.helper_text = ''


    def person_name_validtion(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.person_name.helper_text = 'Enter Correct Name'
            self.person_name._helper_text_color = 'red'
            return
        else:
            self.person_name.helper_text = ''
            instance.error = False


    def person_ph_no_validtion(self, instance, value):
        if not value.isdigit() or len(value) != 10:
            instance.error = True
            self.person_ph_no.helper_text = 'Mobile Number should be ten digits'
            self.person_ph_no._helper_text_color = 'red'
            return
        else:
            self.person_ph_no.helper_text = ''
            instance.error = False


    def person_dob_validtion(self, instance, value):
        try:
            dob = datetime.strptime(value, "%Y-%m-%d")
            today = datetime.now()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                instance.error = True
                self.person_dob.helper_text = 'Enter Correct Date Must Greater than 18'
                self.person_dob._helper_text_color = 'red'
                return
            else:
                self.person_dob.helper_text = ''
                instance.error = False

        except ValueError:
            instance.error = True
            self.person_dob.helper_text = 'Enter Correct Date like YYYY-MM-DD'
            self.person_dob._helper_text_color = 'red'
            return


    def person_profession_validtion(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.person_profession.helper_text = 'Enter Correct Profession'
            self.person_profession._helper_text_color = 'red'
            return
        else:
            self.person_profession.helper_text = ''
            instance.error = False


    def relation_name1_validation(self, instance, value):
        if value.isdigit() or len(value) < 3:
            instance.error = True
            self.relation_name1.helper_text = 'Enter Correct Relation Name'
            self.relation_name1._helper_text_color = 'red'
            return
        else:
            self.relation_name1.helper_text = ''
            instance.error = False


    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_dob.input_type = 'number'


    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_ph_no.input_type = 'number'


    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute


    def add_data(self, marital_status_id):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(marital_status_id, modal_view), 2)


    def perform_data_addition_action(self, marital_status_id, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([marital_status_id]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if marital_status_id not in self.unique_list:
            self.show_validation_error('Select a valid Marital status')
            return

        relation_name = self.ids.relation_name.text
        if relation_name not in self.ids.relation_name.values:
            self.show_validation_error('Select a valid Relation Name')
            return

        if relation_name == 'Father' or relation_name == 'Mother':
            person_name = self.person_name.text
            person_dob = self.date_textfield1.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text
            if not all([person_name, person_dob, person_ph_no, person_proffession]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.person_name.error = True
                # self.person_dob.error = True
                self.person_ph_no.error = True
                self.person_profession.error = True
            else:
                self.error_msg.text = ''
            if len(self.person_name.text) < 3:
                self.person_name.helper_text = ''
                self.person_name._helper_text_color = 'red'
                self.person_name.error = True
                return
            if self.date_textfield1.text == " Enter Valid Date Of Birth *" or self.date_textfield1.text == "You Clicked Cancel!":
                self.show_validation_error('Select a valid Date Of Birth')
                return

            # try:
            #     dob = datetime.strptime(person_dob, "%Y-%m-%d")
            #     today = datetime.now()
            #     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            #     if age < 18:
            #         self.date_textfield1.text = 'Must Select Date Grater Than  18'
            #         self.date_textfield1.text_color = 'red'
            #         return
            #     else:
            #         self.relation_name1.text = ''
            #
            # except ValueError:
            #     self.date_textfield1.text = 'Must Select Date Grater Than  18'
            #     self.date_textfield1.text_color = 'red'
            #     return

            if len(self.person_ph_no.text) != 10 or not self.person_ph_no.text.isdigit():
                self.person_ph_no.helper_text = ''
                self.person_ph_no._helper_text_color = 'red'
                self.person_ph_no.error = True
                return

            if len(self.person_profession.text) < 3:
                self.person_profession.helper_text = ''
                self.person_profession._helper_text_color = 'red'
                self.person_profession.error = True
                return

        elif relation_name == 'Others':
            person_name = self.person_name.text
            person_dob = self.date_textfield1.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text
            relation_name1 = self.relation_name1.text
            if not all([relation_name1, person_name, person_dob, person_ph_no, person_proffession]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.person_name.error = True
                # self.person_dob.error = True
                self.person_ph_no.error = True
                self.person_profession.error = True
                self.relation_name1.error = True
            else:
                self.error_msg.text = ''
            if len(self.person_name.text) < 3:
                self.person_name.helper_text = ''
                self.person_name._helper_text_color = 'red'
                self.person_name.error = True
            if self.date_textfield1.text == " Enter Valid Date Of Birth *" or self.date_textfield1.text == "You Clicked Cancel!":
                self.show_validation_error('Select a valid Date Of Birth')
                return

            # try:
            #     dob = datetime.strptime(person_dob, "%Y-%m-%d")
            #     today = datetime.now()
            #     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            #     if age < 18:
            #         self.date_textfield1.text = 'Must Select Date Grater Than  18'
            #         self.date_textfield1.text_color = 'red'
            #         return
            #     else:
            #         self.relation_name1.text = ''
            #
            # except ValueError:
            #     self.date_textfield1.text = 'Must Select Date Grater Than  18'
            #     self.date_textfield1.text_color = 'red'
            #     return

            if len(self.person_ph_no.text) != 10 or not self.person_ph_no.text.isdigit():
                self.person_ph_no.helper_text = ''
                self.person_ph_no._helper_text_color = 'red'
                self.person_ph_no.error = True
                return

            if len(self.person_profession.text) < 3:
                self.person_profession.helper_text = ''
                self.person_profession._helper_text_color = 'red'
                self.person_profession.error = True
                return


        elif relation_name == 'Spouse':
            spouse_name = self.spouse_name.text
            spouse_date_textfield = self.date_textfield.text
            spouse_mobile = self.spouse_mobile.text
            spouse_company_name = self.spouse_company_name.text
            spouse_company_address = self.spouse_profession.text
            spouse_annual_salary = self.spouse_annual_salary.text
            if not all([spouse_name, spouse_date_textfield, spouse_mobile, spouse_company_name, spouse_company_address,
                        spouse_annual_salary]):
                self.error_msg.text = 'Please Fill All Mandatory * Values'
                self.spouse_name.error = True
                self.spouse_mobile.error = True
                self.spouse_company_name.error = True
                self.spouse_annual_salary.error = True
            else:
                self.error_msg.text = ''

            if len(self.spouse_name.text) < 3:
                self.spouse_name.helper_text = ''
                self.spouse_name._helper_text_color = 'red'
                self.spouse_name.error = True
                return
            if len(self.spouse_mobile.text) != 10 or not self.spouse_mobile.text.isdigit():
                self.spouse_mobile.helper_text = ''
                self.spouse_mobile._helper_text_color = 'red'
                self.spouse_mobile.error = True
                return
            if self.spouse_profession.text not in self.unique_list1:
                self.show_validation_error('Select a valid Spouse Profession')
                return
            if self.date_textfield.text == " Enter Marriage Date *" or self.date_textfield.text == "You Clicked Cancel!":
                self.show_validation_error('Select a valid Marriage Date')
                return
            # try:
            #     dob = datetime.strptime(self.date_textfield.text, "%Y-%m-%d").date()  # Convert to date object
            #     today = datetime.now().date()
            #     if dob > today:
            #         self.date_textfield.text = 'Must Select Date like YYYY-MM-DD'
            #         self.date_textfield.text_color = 'red'
            #         return
            #     else:
            #         self.date_textfield.text = 'Must Select Date like YYYY-MM-DD'
            # except ValueError:
            #     self.date_textfield.text = 'Must Select Date like YYYY-MM-DD'
            #     self.date_textfield.text_color = 'red'
            #     return
            if len(self.spouse_company_name.text) < 3:
                self.spouse_company_name.helper_text = ''
                self.spouse_company_name._helper_text_color = 'red'
                self.spouse_company_name.error = True
                return
            if not self.spouse_annual_salary.text.isdigit():
                self.spouse_annual_salary.helper_text = ''
                self.spouse_annual_salary._helper_text_color = 'red'
                self.spouse_annual_salary.error = True
                return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET marital_status = ? WHERE customer_id = ?",
                (marital_status_id, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        id_list = [i['email_user'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['marital_status'] = marital_status_id
        else:
            print('email not found')

        if self.ids.marital_status_id.text == "Married" and self.ids.relation_name.text == "Spouse":
            spouse_name = self.spouse_name.text
            spouse_date_textfield = self.date_textfield.text
            spouse_mobile = self.spouse_mobile.text
            spouse_company_name = self.spouse_company_name.text
            spouse_company_address = self.spouse_profession.text
            spouse_annual_salary = self.spouse_annual_salary.text

            cursor.execute('select * from fin_users')
            rows = cursor.fetchall()
            row_id_list = []
            status = []
            for row in rows:
                row_id_list.append(row[0])
                status.append(row[-1])

            if 'logged' in status:
                log_index = status.index('logged')
                cursor.execute(
                    "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ? WHERE customer_id = ?",
                    (spouse_name, spouse_date_textfield, spouse_mobile, row_id_list[log_index]))
                conn.commit()
            else:
                # Handle the case where the user is not logged in
                print("User is not logged in.")

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = spouse_name
                    data2[index2]['guarantor_mobile_no'] = int(spouse_mobile)
                    data2[index2]['guarantor_marriage_dates'] = str(spouse_date_textfield)
                    data2[index2]['guarantor_company_name'] = spouse_company_name
                    data2[index2]['guarantor_annual_earning'] = spouse_annual_salary
                    data2[index2]['guarantor_profession'] = spouse_company_address
                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')
        elif self.ids.relation_name.text == "Mother" or self.ids.relation_name.text == "Father":
            relation_name = self.ids.relation_name.text
            person_name = self.person_name.text
            person_dob = self.date_textfield1.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = person_name
                    data2[index2]['guarantor_person_relation'] = relation_name
                    data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                    data2[index2]['guarantor_profession'] = person_proffession
                    data2[index2]['guarantor_date_of_births'] = person_dob

                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')
        elif self.ids.relation_name.text == "Others":

            relation_name = self.ids.relation_name.text
            person_name = self.person_name.text
            person_dob = self.date_textfield.text
            person_ph_no = self.person_ph_no.text
            person_proffession = self.person_profession.text

            data = app_tables.fin_user_profile.search()
            data2 = app_tables.fin_guarantor_details.search()
            cus_id_list2 = [i['customer_id'] for i in data2]
            id_list = [i['email_user'] for i in data]
            cus_id_list = [i['customer_id'] for i in data]
            user_email = anvil.server.call('another_method')
            if user_email in id_list:
                index = id_list.index(user_email)
                if cus_id_list[index] in cus_id_list2:
                    index2 = cus_id_list2.index(cus_id_list[index])
                    data2[index2]['guarantor_name'] = person_name
                    data2[index2]['guarantor_person_relation'] = relation_name
                    data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                    data2[index2]['guarantor_profession'] = person_proffession
                    data2[index2]['guarantor_date_of_births'] = person_dob

                else:
                    print('customer_id is not valid')

            else:
                print('email not valid')

        if marital_status_id == 'Un-Married' or marital_status_id == 'Not Married':
            sm = self.manager
            borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualBankForm1'

        elif marital_status_id == 'Married':
            sm = self.manager
            borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualBankForm1'

        elif marital_status_id == 'Divorced':
            sm = self.manager
            borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualBankForm1'
        elif marital_status_id == 'Other':
            sm = self.manager
            borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualBankForm1'
        else:
            sm = self.manager
            borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'
            sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen6'


class LenderScreen8(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_dob.input_type = 'number'

    def on_father_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.father_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, father_name, father_address, father_occupation, father_ph_no, father_dob):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(father_name, father_address, father_occupation, father_ph_no,
                                                         father_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, father_name, father_address, father_occupation, father_ph_no, father_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([father_name, father_address, father_occupation, father_ph_no, father_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not father_ph_no.isdigit() or len(father_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Father Number.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_name):
            self.show_validation_error("Please Enter Valid Father Name.")
            return
        if len(father_occupation) < 3:
            self.show_validation_error("Please Enter Valid Father Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', father_address):
            self.show_validation_error("Please enter valid father Age.")
            return
        try:
            dob = datetime.strptime(father_dob, "%Y-%m-%d")


        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET father_name = ?, father_address = ?, father_occupation = ?, father_ph_no = ? WHERE customer_id = ?",
                (father_name, father_address, father_occupation, father_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = father_name
                data2[index2]['guarantor_address'] = father_address
                data2[index2]['guarantor_mobile_no'] = int(father_ph_no)
                data2[index2]['guarantor_profession'] = father_occupation
                data2[index2]['guarantor_date_of_births'] = father_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen9(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.mother_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(mother_name, mother_address, mother_occupation, mother_ph_no,
                                                         mother_dob,
                                                         modal_view), 2)

    def perform_data_addition_action(self, mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([mother_name, mother_address, mother_occupation, mother_ph_no, mother_dob]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not mother_ph_no.isdigit() and len(mother_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Mother Number.")
            return

        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_name):
            self.show_validation_error("Please Enter Valid Mother Name.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_occupation):
            self.show_validation_error("Please Enter Valid Mother Occupation.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', mother_address):
            self.show_validation_error("Please Enter Valid Mother Address.")
            return
        try:
            dob = datetime.strptime(mother_dob, "%Y-%m-%d")


        except ValueError:
            self.show_validation_error("Please enter a valid date of birth in the format YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET mother_name = ?, mother_address = ?, mother_occupation = ?, mother_ph_no = ? WHERE customer_id = ?",
                (mother_name, mother_address, mother_occupation, mother_ph_no, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = mother_name
                data2[index2]['guarantor_address'] = mother_address
                data2[index2]['guarantor_mobile_no'] = int(mother_ph_no)
                data2[index2]['guarantor_profession'] = mother_occupation
                data2[index2]['guarantor_date_of_births'] = mother_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen10(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_marriage_date.input_type = 'number'

    def on_spouse_mobile_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_mobile.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, spouse_name, spouse_marriage_date, spouse_mobile):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(spouse_name, spouse_marriage_date, spouse_mobile
                                                         , modal_view), 2)

    def perform_data_addition_action(self, spouse_name, spouse_marriage_date, spouse_mobile,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_name, spouse_marriage_date, spouse_mobile]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^[a-zA-Z\s]{3,}$', spouse_name):
            self.show_validation_error("Please Enter Valid Name.")
            return
        if not spouse_mobile.isdigit() or len(spouse_mobile) not in (10, 12):
            self.show_validation_error("Please Enter Valid Number.")
            return
        try:
            dob = datetime.strptime(spouse_marriage_date, "%Y-%m-%d").date()
            today = datetime.today().date()

            # Check if dob is less than today's date
            if dob > today:
                self.show_validation_error("Spouse's marriage date must be less than today's date.")
                return


        except ValueError:
            self.show_validation_error("Invalid date format. Please use YYYY-MM-DD")
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_name = ?,spouse_date_textfield = ?, spouse_mobile = ? WHERE customer_id = ?",
                (spouse_name, spouse_marriage_date, spouse_mobile, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = spouse_name
                data2[index2]['guarantor_mobile_no'] = int(spouse_mobile)
                data2[index2]['guarantor_marriage_dates'] = str(spouse_marriage_date)
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreen11(name='LenderScreen11')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreen11'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen11(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_spouse_profession.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['spouse_profession'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type'] + unique_list
        else:
            self.ids.spouse_profession.values = ['Select Spouse Profession Type']

    def on_spouse_annual_salary_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_annual_salary.input_type = 'number'

    def on_spouse_office_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.spouse_office_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, spouse_company_name, spouse_profession, spouse_annual_salary):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_data_addition_action(spouse_company_name, spouse_profession,
                                                                         spouse_annual_salary,
                                                                         modal_view), 2)

    def perform_data_addition_action(self, spouse_company_name, spouse_profession, spouse_annual_salary
                                     , modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if not all([spouse_profession]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if spouse_profession not in spouse_profession == 'Select Spouse Profession':
            self.show_validation_error('Select a valid Spouse Profession')
            return

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')
            cursor.execute(
                "UPDATE fin_registration_table SET spouse_company_name = ?,spouse_company_address = ?, spouse_annual_salary = ? WHERE customer_id = ?",
                (spouse_company_name, spouse_profession, spouse_annual_salary,
                 row_id_list[log_index]))
            conn.commit()
        else:
            print('User is not logged in.')

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_company_name'] = spouse_company_name
                data2[index2]['guarantor_annual_earning'] = spouse_annual_salary
                data2[index2]['guarantor_profession'] = spouse_profession
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen10'


class LenderScreen12(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed3(self):
        self.ids.id3.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Spouse"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id3.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id3.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = LenderScreen8(name='LenderScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen8'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = LenderScreen9(name='LenderScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen9'
        elif self.type == "Spouse":
            sm = self.manager
            borrower_screen = LenderScreen10(name='LenderScreen10')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen10'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = LenderScreen14(name='LenderScreen14')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen14'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen13(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = None

    def on_yes_button_pressed1(self):
        self.ids.id1.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Father"

    def on_yes_button_pressed2(self):
        self.ids.id2.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.ids.id4.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.type = "Mother"

    def on_yes_button_pressed4(self):
        self.ids.id4.md_bg_color = 0.043, 0.145, 0.278, 1
        self.ids.id4.text_color = (1, 1, 1, 1)
        self.ids.id2.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id2.text_color = (1, 1, 1, 1)
        self.ids.id1.md_bg_color = 192 / 262, 209 / 262, 203 / 262
        self.ids.id1.text_color = (1, 1, 1, 1)
        self.type = "Other"

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(modal_view), 2)

    def perform_data_addition_action(self, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        if self.type == None:
            # Display a validation error dialog
            self.show_validation_error("Please Select Valid Type.")
            return  # Prevent further execution if any field is missing

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['another_person'] = self.type
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        if self.type == 'Father':
            sm = self.manager
            borrower_screen = LenderScreen8(name='LenderScreen8')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen8'
        elif self.type == 'Mother':
            sm = self.manager
            borrower_screen = LenderScreen9(name='LenderScreen9')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen9'
        elif self.type == 'Other':
            sm = self.manager
            borrower_screen = LenderScreen14(name='LenderScreen14')
            sm.add_widget(borrower_screen)
            sm.transition.direction = 'left'  # Set the transition direction explicitly
            sm.current = 'LenderScreen14'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreen14(Screen):
    def on_date_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_dob.input_type = 'number'

    def on_mother_ph_no_touch_down(self):
        # Change keyboard mode to numeric when the mobile number text input is touched
        self.ids.person_ph_no.input_type = 'number'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def add_data(self, relation_name, person_name, person_dob, person_ph_no, person_proffession):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action(relation_name, person_name, person_dob, person_ph_no,
                                                         person_proffession,
                                                         modal_view), 2)

    def perform_data_addition_action(self, relation_name, person_name, person_dob, person_ph_no, person_proffession,
                                     modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()
        # Check for missing fields
        if not all([relation_name, person_name, person_dob, person_ph_no, person_proffession]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing

        if not person_ph_no.isdigit() and len(person_ph_no) not in (10, 12):
            self.show_validation_error("Please Enter Valid Mother Number.")
            return
        if not re.match(r'^[a-zA-Z\s]{3,}$', relation_name):
            self.show_validation_error("Relation name should contain only letters and spaces.")
            return

        # Validate person_name
        if not re.match(r'^[a-zA-Z\s]{3,}$', person_name):
            self.show_validation_error("Person name should contain only letters.")
            return
        try:
            dob = datetime.strptime(person_dob, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            # Check if age is less than 18
            if age < 18:
                self.show_validation_error("You must be at least 18 years old to register.")
                return

        except ValueError:
            self.show_validation_error("Invalid date format. Please use YYYY-MM-DD")
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])

        if 'logged' in status:
            log_index = status.index('logged')

        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        data2 = app_tables.fin_guarantor_details.search()
        cus_id_list2 = [i['customer_id'] for i in data2]
        id_list = [i['email_user'] for i in data]
        cus_id_list = [i['customer_id'] for i in data]
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            if cus_id_list[index] in cus_id_list2:
                index2 = cus_id_list2.index(cus_id_list[index])
                data2[index2]['guarantor_name'] = person_name
                data2[index2]['guarantor_person_relation'] = relation_name
                data2[index2]['guarantor_mobile_no'] = int(person_ph_no)
                data2[index2]['guarantor_profession'] = person_proffession
                data2[index2]['guarantor_date_of_births'] = person_dob
            else:
                print('customer_id is not valid')

        else:
            print('email not valid')

        sm = self.manager
        borrower_screen = LenderScreenIndividualBankForm1(name='LenderScreenIndividualBankForm1')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderScreenIndividualBankForm1'

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'


class LenderScreenIndividualBankForm1(Screen):
    all_fields_filled = BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner_data = app_tables.fin_lendor_account_type.search()
        data_list = []
        for i in spinner_data:
            data_list.append(i['lendor_account_type'])
        unique_list = []
        for i in data_list:
            if i not in unique_list:
                unique_list.append(i)
        print(unique_list)
        if len(unique_list) >= 1:
            self.ids.account_type.values = unique_list
        else:
            self.ids.account_type.values = ['Select Account Type']

        self.check = None

    def validate_zip_code(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only numeric characters
        if not zip_code_text.isdigit():
            zip_code.helper_text = "Should contain only numbers"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def validate_zip_code_text(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains only alphabetic characters
        if not zip_code_text.isalpha():
            zip_code.helper_text = "Should contain only alphabetic characters"
            zip_code.error = True
        else:
            zip_code.helper_text = ""
            zip_code.error = False

    def validate_zip_code_numchar(self, zip_code):
        zip_code_text = zip_code.text

        # Check if the input contains both alphabetic characters and numeric digits
        has_alpha = any(char.isalpha() for char in zip_code_text)
        has_digit = any(char.isdigit() for char in zip_code_text)

        if has_alpha and has_digit:
            zip_code.helper_text = ""
            zip_code.error = False
        else:
            zip_code.helper_text = "Should Contain characters and numbers."
            zip_code.error = True

    def go_to_dashboard(self):
        self.manager.current = 'DashScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderScreen7'

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.check = True
            self.all_fields_filled = not all([
                self.ids.ifsc_code.text,
                self.ids.branch_name.text,
                self.ids.account_holder_name.text,
                self.ids.account_type.text,
                self.ids.account_number.text,
                self.ids.bank_name.text
            ])
        else:
            self.check = False

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        # Loop the animation
        anim.repeat = True
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label, modal_height))
        anim.start(loading_label)
        # Store the animation object
        loading_label.animation = anim  # Store the animation object in a custom attribute

    def go_to_lender_dashboard(self, bank_id, branch_name,account_holder_name, account_type, account_number, bank_name):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()


        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(
            lambda dt: self.perform_data_addition_action4(bank_id, branch_name,account_holder_name, account_type, account_number, bank_name, modal_view), 2)

    def perform_data_addition_action4(self, bank_id, branch_name,account_holder_name, account_type, account_number, bank_name, modal_view):
        modal_view.children[0].animation.cancel_all(modal_view.children[0].animation)
        modal_view.dismiss()

        # Check for missing fields
        if not all([bank_id, branch_name,account_holder_name, account_type, account_number, bank_name]):
            # Display a validation error dialog
            self.show_validation_error("Please fill in all fields.")
            return  # Prevent further execution if any field is missing
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{3,}$', bank_id):
            self.show_validation_error(
                "IFSC Code should contain at least 3 characters, including both numbers and letters.")
            return
        if not branch_name.isalpha() or len(branch_name) < 3:
            self.show_validation_error('Enter a valid branch name')
            return
        if not re.match(r'^[a-zA-Z]{3,}$', account_holder_name) or not account_holder_name[0].isupper():
            self.show_validation_error('Enter a valid account holder name and first letter should be capital')
            return
        if account_type not in account_type == 'Select Account Type':
            self.show_validation_error('Enter a valid account type')
            return
        if len(account_number) < 3 or not account_number.isdigit():
            self.show_validation_error('Enter a valid account number')
            return
        if not re.match(r'^[a-zA-Z]{3,}$', bank_name):
            self.show_validation_error('Enter a valid bank name')
            return
        if self.check != True:
            self.show_validation_error('Select The Terms and Conditions')
            return
        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        email_list = []
        b = 'lender'
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
            email_list.append(row[2])
        if 'logged' in status:
            log_index = status.index('logged')

            cursor.execute(
                "UPDATE fin_registration_table SET bank_id = ?, branch_name = ?,account_holder_name = ?, account_type = ?, account_number = ?, bank_name = ?, user_type = ? WHERE customer_id = ?",
                (bank_id, branch_name,account_holder_name, account_type, account_number, bank_name, b, row_id_list[log_index]))
            conn.commit()
        else:
            # Handle the case where the user is not logged in
            print("User is not logged in.")

        data = app_tables.fin_user_profile.search()
        member = app_tables.fin_membership.search()
        user_email = anvil.server.call('another_method')
        id_list = []
        email_id = ""
        user_name = ""
        customer_id = ""
        investment = ""
        membership = ""
        lending_period = ""
        lending_type = ""

        today = datetime.now().date()
        if data:
            email_id = data[0]['email_user']
            user_name = data[0]['full_name']
            customer_id = data[0]['customer_id']
            investment = data[0]['investment']
            lending_period = data[0]['lending_period']
            lending_type = data[0]['loan_type']
        if member:
            membership = member[0]['membership_type']

        for i in data:
            id_list.append(i['email_user'])
        user_email = anvil.server.call('another_method')
        if user_email in id_list:
            index = id_list.index(user_email)
            data[index]['bank_id'] = bank_id
            data[index]['account_bank_branch'] = branch_name
            data[index]['account_name'] = account_holder_name
            data[index]['account_type'] = account_type
            data[index]['account_number'] = account_number
            data[index]['bank_name'] = bank_name
            data[index]['usertype'] = b
            data[index]['registration_approve'] = True
            data[index]['last_confirm'] = True
            data[index]['profile_status'] = True
            data[index]['mobile_check'] = True

            existing_record = app_tables.fin_lender.get(email_id=email_id)
            if not existing_record:
                app_tables.fin_lender.add_row(user_name=user_name,
                                              email_id=email_id,
                                              customer_id=customer_id,
                                              investment=investment,
                                              membership=membership,
                                              lending_period=lending_period,
                                              lending_type=lending_type,
                                              member_since=today)
            else:
                # Optionally, update the existing record if needed
                # existing_record.update(user_name=data[index]['full_name'], ...)
                print(f"Record for {user_email} already exists. Skipping insertion.")
        else:
            print('email not found')
        self.save_user_info(user_email, b)
        sm = self.manager
        lender_screen = LenderDashboard(name='LenderDashboard')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'LenderDashboard'

    def save_user_info(self, email, b):
        with open("emails.json", "r") as file:
            data = json.load(file)

        # Update or create entry for the current user
        data[email] = {"user_type": b, "logged_status": True}
        print(data)
        # Write updated data back to the file
        with open("emails.json", "w") as file:
            json.dump(data, file)
    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def show_terms_dialog(self):
        dialog = MDDialog(
            title="Terms and Conditions",
            text="Agreements, Privacy Policy and Applicant should accept following:Please note that any information concealed (as what we ask for), would be construed as illegitimate action on your part and an intentional attempt to hide material information which if found in future, would attract necessary action (s) at your sole cost. Hence, request to be truthful to your best knowledge while sharing your details)",
            size_hint=(0.8, 0.5),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

from kivy.uix.spinner import SpinnerOption, Spinner


class CustomSpinnerOption(SpinnerOption):
    pass

from kivy.uix.spinner import SpinnerOption
class CustomSpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        super(CustomSpinnerOption, self).__init__(**kwargs)
        self.background_color = (0.043, 0.145, 0.278, 1)  # Set the desired background color
        self.color = (1, 1, 1, 1)  # Set the text color