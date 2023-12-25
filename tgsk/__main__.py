# -*- coding: utf-8 -*-

from flet import *
import asyncio
import logging
# logging.basicConfig(level=logging.DEBUG)

simple_animation = Animation(duration=500, curve=AnimationCurve.EASE_OUT_CUBIC)


def make_animated_control(ctl: Control) -> Control:
    ctl.animate_opacity = simple_animation
    ctl.animate_offset = simple_animation
    ctl.offset = Offset(0, 1)
    ctl.opacity = 0
    return ctl


def animate_control(ctl: Control, opacity: float = 1) -> None:
    ctl.offset = Offset(0, 0)
    ctl.opacity = opacity
    return


title_welcome_message_row = Ref[Row]()
subtitle_text = Ref[Text]()


async def main(page: Page):
    page.title = 'TGSK'
    print('--')
    if page.platform_brightness == ThemeMode.DARK:
        page.appbar = AppBar(
            leading=Image(src='/icons/appbar-icon-dark.png'),
            title=Text('TGSK')
        )
    else:
        page.appbar = AppBar(
            leading=Image(src='/icons/appbar-icon-light.png'),
            title=Text('TGSK')
        )

    core_icon = Image(
        src='/icons/core-icon-light.png',
        height=28,
        fit=ImageFit.FIT_HEIGHT
    )
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    async def on_platform_brightness_change(_):
        nonlocal core_icon
        print('amogus')
        if page.platform_brightness == ThemeMode.DARK:
            title_welcome_message_row.current.controls[0] = Image(
                src='/icons/core-icon-light.png',
                height=28,
                fit=ImageFit.FIT_HEIGHT
            )
            page.appbar = AppBar(
                leading=Image(src='/icons/appbar-icon-dark.png'),
                title=Text('TGSK')
            )
        else:
            title_welcome_message_row.current.controls[0] = Image(
                src='/icons/core-icon-dark.png',
                height=28,
                fit=ImageFit.FIT_HEIGHT
            )
            page.appbar = AppBar(
                leading=Image(src='/icons/appbar-icon-light.png'),
                title=Text('TGSK')
            )

        await title_welcome_message_row.current.update_async()
        # await page.appbar.leading.update_async()
        await page.appbar.update_async()
        await page.update_async()
    page.on_platform_brightness_change = on_platform_brightness_change

    await page.add_async(
        Card(
            width=640,
            height=480,
            content=Container(
                padding=12,
                content=Column(
                    controls=[
                        make_animated_control(
                            Row(
                                controls=[
                                    core_icon,
                                    Text('Добро пожаловать, Дмитрий!', size=28)
                                ],
                                tight=True,
                                wrap=True,
                                ref=title_welcome_message_row
                            )
                        ),
                        make_animated_control(
                            Text(
                                value='Чём займёшься сегодня?',
                                size=18,
                                ref=subtitle_text
                            )
                        )
                    ]
                )
            )
        )
    )
    await asyncio.sleep(0.1)
    animate_control(title_welcome_message_row.current)
    await page.update_async()
    await asyncio.sleep(0.15)
    animate_control(subtitle_text.current, opacity=0.5)
    await page.update_async()


if __name__ == '__main__':
    asyncio.run(
        app_async(
            target=main,
            assets_dir='./assets/',
            port=52244
        )
    )
