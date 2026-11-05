import flet as ft


def main(page: ft.Page):
    #Define options inside a RadioGroup
    quiz_group = ft.RadioGroup(
        content=ft.Column(controls = [
            ft.Radio(value="list", label="list"),
            ft.Radio(value="tuple", label="tuple"),
            ft.Radio(value="array", label="array (primitive keyword)"),
            ft.Radio(value="dict", label="dict"),
        ])
    )

    feedback = ft.Text(size=16)

    def check_answer(e):
        if quiz_group.value == "array":
            with open("data.txt", "w") as f:
                f.write(quiz_group.value + "\n")
            feedback.value = "Correct!"
            feedback.color = ft.Colors.GREEN
        else:
            with open("data.txt", "w") as f:
                f.write(quiz_group.value + "\n")
            feedback.value = "Incorrect. Try again!"
            feedback.color = ft.Colors.RED
       
    page.floating_action_button = ft.FloatingActionButton("Submit", on_click=check_answer)

    page.add(
        ft.Text("Which of these is NOT a built-in Python type?", size=18, weight=ft.FontWeight.BOLD),
        quiz_group,
        feedback,
    )

ft.run(main)

