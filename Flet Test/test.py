import flet as ft
import json

def main(page: ft.Page):
    page.title = "Zhang Test"
    page.window_width = 400
    page.window_height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def main_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Hello, welcome to Mr. Zhang's Class!")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True,can_reveal_password=True)
       
        def submit_click(e):
            data = {}
            
            with open("data.json", 'r') as f:
                data = json.load(f)
            if data[username.value] == password.value:
                print("Login successfully")


        def register_click(e):
            register_page()

        page.floating_action_button = ft.FloatingActionButton("Register", on_click=register_click)
        Login = ft.Button(content = "Login", on_click=submit_click)
        page.add(
            ft.Container(
                expand = True,
                content = ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        Login
                ]
                )
            )
        )

    def register_page():
        page.controls.clear()
        page.floating_action_button = None
        greeting = ft.Text(value="Please register for a new account")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True,can_reveal_password=True)
        passwordconfirm = ft.TextField(label = "Confirm your Password", password=True,can_reveal_password=True)
        feedback = ft.Text(size=16)
        def register_click(e):
            if password.value == passwordconfirm.value:
                data: dict = {}
                
                with open('data.json', 'r') as f:
                    data = json.load(f)
                    
                data[username.value] = password.value
                with open('data.json', 'w') as f:
                    json.dump(data, f)

                main_page()
            else:
                feedback.value = ("Passwords do not match")


        page.floating_action_button = ft.FloatingActionButton("Proceed", on_click=register_click)
        page.add(
            ft.Container(
                expand = True,
                content = ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                        passwordconfirm,
                        feedback
                ]
                )
            )
        )

    main_page()

ft.run(main)



        