#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)
import os

from dependency import Log, json, log_path

log = Log(
    "main",
    log_output_to_file_path=f"{log_path}main.log",
)
exe_all = json.load("exe_all")
if exe_all is False:
    log.error("exe_all.json not found")
    exe_all: dict[str, dict[str, str | None]] = {
        "name_compare": {

        },
        "demo": {
            "path": None,
            "cmd": None
        }
    }
    json.dump(exe_all, "exe_all")


def open_exe(exe_path: str, cmd: str = None):
    log.info(f'open_exit: "{exe_path}" {cmd}')
    if exe_path is None:
        log.error("exe_path is None")
        return
    if cmd is None:
        cmd = ""
    os.system(f'"{exe_path}" {cmd}')


if __name__ == '__main__':
    while True:
        t = input("输入应用程序名")
        if t == "exit":
            break
        elif t == "name_compare":
            print("此为对照表,不可启动")
            continue
        elif t in exe_all.keys():
            open_exe(exe_all[t]["path"], exe_all[t]["cmd"])
        elif t in exe_all["name_compare"].keys():
            name = exe_all["name_compare"][t]
            open_exe(exe_all[name]["path"], exe_all[name]["cmd"])
