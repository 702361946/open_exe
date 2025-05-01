#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)
import subprocess
import time
import tkinter.messagebox as mbox

from dependency import Log, json, log_path
from dependency.modules._tkinter import Window

log = Log(
    "main",
    log_output_to_file_path=f"{log_path}main.log",
)
config = json.load("config")
if config is False:
    log.error("config.json not found")
    config: dict[str, dict[str, str | None]] = {
        "name_compare": {

        },
        "Force Start": False,
        "demo": {
            "path": None,
            "cmd": None
        }
    }
    json.dump(config, "config")


def open_exe(exe_path: str, cmd: str = None, box: bool = False, sleep: float = 1):
    log.info(f'open_exit: "{exe_path}" {cmd}')
    if_open = True
    if exe_path is None:
        log.error("exe_path is None")
        if_open = False
    if cmd is None:
        cmd = ""

    if if_open:
        a = subprocess.Popen(f'"{exe_path}" {cmd}', shell=True)

        time.sleep(sleep)

        if a.poll() is None:
            log.info(f'open_exit: "{exe_path}" {cmd} success')
            if box:
                mbox.showinfo("提示", "启动成功")
        else:
            log.info(f'open_exit: "{exe_path}" {cmd} exit')
            if box:
                mbox.showerror("提示", "启动失败")
    else:
        log.info(f'open_exit: "{exe_path}" {cmd} exit')
        if box:
            mbox.showerror("提示", "启动失败")


def compare(name: str, return_as_is: bool = None):
    if return_as_is is None:
        return_as_is = config["Force Start"]

    if name in config.keys():
        t = name

    elif name in config["name_compare"].keys():
        name = config["name_compare"][name]
        t = name
    else:
        log.info(f"not compare: {name}")
        t = None

    if t == "name_compare":
        log.info("compare error: name compare == name_compare")
        return None, None

    elif t in config.keys():
        return config[t]["path"], config[t]["cmd"]

    else:
        log.info(f"not compare: {t}")
        if return_as_is:
            return name, None
        return None, None


def run():
    win = Window(
        title="Main",
        geometry="150x50",
        resizable=(False, False),
    )
    win.entry(
        "input_path",
        default_text="在此输入应用程序名",
        pack_mode="place",
    )
    win.button(
        "open",
        text="确认",
        pack_mode="place",
        command=lambda: open_exe(
            *compare(
                win.get(
                    "input_path",
                    "entry",
                    entry_return_type="get"
                )
            ),
            box=True
        ),
        y=20
    )

    win.run()


if __name__ == '__main__':
    run()
