import flet_easy as fs
import flet as ft

# todo x: global use to register router
app = fs.FletEasy(route_init="/", on_resize=True)


@app.config
async def config(page: ft.Page):
    theme = ft.Theme()

    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    theme.text_theme = ft.TextTheme()

    # page.theme = ft.Theme()
    # page.theme_mode = ft.ThemeMode.LIGHT
    # await page.update_async()
    # page.update()
    print("theme mode: ", page.theme_mode)

    print("update config done")
