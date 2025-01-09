import flet_easy as fs
import flet as ft
from loguru import logger

# todo x: global use to register router
app = fs.FletEasy(route_init="/", on_resize=True)


#
# todo x: 全局配置
#
@app.config
async def config(page: ft.Page):
    theme = ft.Theme()

    platforms = ["android", "ios", "macos", "linux", "windows"]
    for platform in platforms:  # Removing animation on route change.
        setattr(theme.page_transitions, platform, ft.PageTransitionTheme.NONE)

    theme.text_theme = ft.TextTheme()

    #
    # todo x: set locale
    #
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("en"), ft.Locale("zh")],
        current_locale=ft.Locale("en"),
    )

    # page.theme = ft.Theme()
    # page.theme_mode = ft.ThemeMode.LIGHT
    # await page.update_async()
    # page.update()

    logger.debug(f"app locale: {page.locale_configuration}")
    logger.debug("theme mode: ", page.theme_mode)
