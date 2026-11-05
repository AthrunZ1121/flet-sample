import flet as ft
info = ["ICS4U", "12345"]
#This stores the correct password and username

def main(page: ft.Page):
    page.title = "Zhang Test"
    page.window_width = 400
    page.window_height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def main_page():
        page.controls.clear()
        greeting = ft.Text(value="Hello, welcome to Mr. Zhang's Class!")
        username = ft.TextField(label = "Name", hint_text="Please enter your user name")
        password = ft.TextField(label = "Password", password=True,can_reveal_password=True)
       
        def submit_click(e):
            collected_name = username.value
            collected_password = password.value
            if (collected_name == info[0] and collected_password == info[1]):
                print("password collected successfully, going into the next page")
                question_page()
                #notice here!!! If the username and password is correct
                #we will call the question_page function which initializes a new page.
            else:
                print("Wrong password")


        page.floating_action_button = ft.FloatingActionButton("Log In", on_click=submit_click)
       
        page.add(
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls = [
                        greeting,
                        username,
                        password,
                    ]
                ),
                alignment=ft.Alignment.CENTER,
            )
           
        )
     
    def question_page():
        questions = {
            "What's 1+1": 2,
            "What's 2-2": 0,
            "what's 10-56": -46,
            "what's 11*10": 110,
            "what's 52+48": 100
        }
        page.controls.clear()
        questioncontrols= [
            ft.TextField(label= x, hint_text = "Enter your answer") for x in questions
        ]
       
        def submit(e):
            score = 0
            for x in questioncontrols:
                if (int(x.value) == questions[x.label]):
                    score += 20
            print("Your final score is ", score)
        page.floating_action_button = ft.FloatingActionButton(content = "Submit",on_click = submit)
        page.add(
            ft.Container(
                content=ft.Column(
                    controls = questioncontrols
                ),
                alignment=ft.Alignment.CENTER,
            )            
        )

    #calling the main_page() function when main() is executed
    main_page()

#running the main
ft.run(main)



