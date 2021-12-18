import os
import sys

args = list(sys.argv)
try:
    name = args[1]
    run = 1
except:
    print("No search specified")
    run = 0

def fetch(name):
    os.system(f"wget 'https://pypi.org/search/?q={name}' -O /tmp/pypi-search -q")

def readnames(tmpfile):
    names_list = []
    with open(tmpfile, 'r') as fopen:
        while True:
            line = fopen.readline()
            if not line:
                break
            if "package-snippet__name" in str(line):
                names_list.append(line)
    names_list_stripped = []
    for sname in names_list:
        sname = str(sname.replace('      <span class="package-snippet__name">',""))
        sname = sname.replace('</span>',"")
        sname = sname.rstrip("\n")
        names_list_stripped.append(sname)
    return(names_list_stripped)

def readdesc(tmpfile):
    names_list = []
    with open(tmpfile, 'r') as fopen:
        while True:
            line = fopen.readline()
            if not line:
                break
            if "package-snippet__description" in str(line):
                names_list.append(line)
    names_list_stripped = []
    for sname in names_list:
        sname = str(sname.replace('    <p class="package-snippet__description">',""))
        sname = sname.replace('</p>',"")
        sname = sname.rstrip("\n")
        names_list_stripped.append(sname)
    return(names_list_stripped)

def main():
    tmpfile = ("/tmp/pypi-search")
    fetch(name)
    names_list = readnames(tmpfile)
    desc_list = readdesc(tmpfile)
    pstr = str("")
    ps = 0
    results = []
    for cname in names_list:
        cdesc = desc_list[ps]
        if cdesc != "":
            pstr = str(f"{cname} - {cdesc}")
        else:
            pstr = str(f"{cname}")
        ps+=1
        results.append(pstr)
    print("\n".join(results))

if run == 1:
    main()