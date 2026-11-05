import flet as ft

def main(page: ft.Page):
    page.title = "Scrollable Column Example"
    
    scrollable_column = ft.Column(
        
        controls=[ft.Text(f"Item {i}", size=20) for i in range(100)],
        scroll = ft.ScrollMode.ALWAYS,
        expand=True                 
    )

    page.add(scrollable_column)

ft.run(main)