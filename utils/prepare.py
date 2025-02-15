import os
import shutil

from loguru import logger

VERSION = "2.18.0"

need_dir_list = [
    "./output",
    "./output/t2i",
    "./output/t2i/grids",
    "./output/vibe",
    "./output/i2i",
    "./output/enhance",
    "./output/inpaint",
    "./output/inpaint/img",
    "./output/inpaint/mask",
    "./output/pixiv",
    "./output/upscale",
    "./output/mosaic",
    "./output/water",
    "./files/else_upscale_engine",
    "./files/prompt",
    "./files/prompt/done",
    "./plugins",
    "./plugins/t2i",
    "./plugins/i2i",
    "./plugins/webui",
]


if not os.path.exists(".env"):
    shutil.copyfile(".env.example", ".env")
for dir in need_dir_list:
    if not os.path.exists(dir):
        os.mkdir(dir)


if not os.path.exists("./files/prompt/example.txt") and not os.path.exists("./files/prompt/done/example.txt"):
    with open("./files/prompt/example.txt", "w") as f:
        f.write(
            "[suimya, muririn], artist:ciloranko,[artist:sho_(sho_lwlw)],[[tianliang duohe fangdongye]], [eip (pepai)], [rukako], [[[memmo]]], [[[[[hoshi (snacherubi)]]]]], year 2023, 1girl, cute, loli,"
        )

if not os.path.exists("./files/favorite.json"):
    shutil.copyfile("./files/favorite_example.json", "./files/favorite.json")


if __name__ == "__main__":
    from env import env

    logger.opt(colors=True).success(
        f"""<c>
███████╗ █████╗ ███╗   ██╗██████╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗
███████╗███████║██╔██╗ ██║██████╔╝
╚════██║██╔══██║██║╚██╗██║██╔═══╝     Version:    {VERSION}
███████║██║  ██║██║ ╚████║██║         Author:     https://github.com/zhulinyv
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝         Repository: https://github.com/zhulinyv/Semi-Auto-NovelAI-to-Pixiv</c>"""
    )
    if env.skip_start_sound:
        pass
    else:
        from playsound import playsound

        playsound("./files/webui/llss.mp3")
