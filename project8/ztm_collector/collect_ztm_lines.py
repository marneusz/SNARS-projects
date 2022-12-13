import sys, time, json, random, os, re
from typing import Callable, Sequence, Iterator, Dict, Set
from math import cos, asin, sqrt, ceil
from collections import defaultdict


def download_ftp(path: str, output_path: str):
    if os.path.exists(output_path):
        return
    import ftplib

    ftp = ftplib.FTP(path)
    ftp.login("anonymous", "")
    files = ftp.nlst()

    pattern = re.compile(r"RA(\d+)\.7z")
    files = [f for f in files if re.match(pattern, f)]
    files.sort(key=lambda x: int(pattern.match(x).group(1)), reverse=True)

    with open(output_path, "wb") as output_file:
        ftp.retrbinary("RETR %s" % (files[0],), output_file.write)
    ftp.quit()


def decompress_data(path: str, output_path: str):
    if os.path.exists(output_path):
        return
    os.system("7z x %s -o%s" % (path, output_path))


if __name__ == "__main__":
    download_ftp("rozklady.ztm.waw.pl", "downloaded.7z")
    dir_path = "/home/marneusz/msc/SNARS/repo/SNARS-projects/project8"
    decompress_data("downloaded.7z", os.path.join(dir_path, "ztm_collector"))
