import flet as ft


def main(page: ft.Page):
    page.title = "Background image"

    page.bgcolor = ft.Colors.TRANSPARENT 
    #if you wish to use background images, you must set the background color to transparent first

    #this is how you can set background image
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src="background.png",
            fit= ft.BoxFit.FILL, 
            #ft.BoxFit.FILL distorts the image to fit the entire screen.
        )
    )


ft.run(main)