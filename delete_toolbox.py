import os
import sys
import glob
from pathlib import Path

### ERRORS ###
class RobloxStudioNotFoundError(Exception):
   """Raised when Roblox Studio does not exist"""
   pass

class ToolboxPluginNotFoundError(Exception):
    """Raised when Toolbox Plugin does not exist"""
    pass

class RobloxStudioRibbonNotFoundError(Exception):
    """Raised when Roblox Studio Ribbon does not exist"""
    pass

### find functions ###
def find(refpath, name):
    pathnames = []
    for path in Path(refpath).rglob(name):
        pathnames.append(path.as_posix())
    return pathnames

def findRobloxStudioPath():
    homePath = os.path.expanduser("~")
    robloxPath = os.path.join(homePath, "Appdata\\Local\\Roblox")
    # should return a list with just one element - there should be only one 
    # RobloxStudioBeta.exe in one of the version folders in \Roblox\Versions
    robloxStudioPaths = find(robloxPath, "RobloxStudioBeta.exe")
    if not robloxStudioPaths:
        raise RobloxStudioNotFoundError("RobloxStudioBeta.exe cannot be found in path " + robloxPath)
    return os.path.dirname(robloxStudioPaths[0])

ROBLOX_STUDIO_PATH = findRobloxStudioPath()

def findToolboxPluginPath():
    # should return a list with just one element - there should be only one 
    # Toolbox.rbxm in \BuiltinPlugins
    # refpath = findRobloxStudioPath()
    toolboxPluginPaths = find(ROBLOX_STUDIO_PATH, "Toolbox.rbxm")
    if not toolboxPluginPaths:
        return None
        # raise ToolboxPluginNotFoundError("Toolbox Plugins cannot be found in path " + ROBLOX_STUDIO_PATH)
    return os.path.dirname(toolboxPluginPaths[0])

def findRobloxStudioRibbonFile():
    pass

### toolbox actions ###
def hideToolboxIcons():
    # refpath = findRobloxStudioPath()
    ribbonFile = os.path.join(ROBLOX_STUDIO_PATH, "RobloxStudioRibbon.xml")
    if not os.path.exists(ribbonFile):
        raise RobloxStudioRibbonNotFoundError("RobloxStudioRibbon.xml cannot be found in path " + ROBLOX_STUDIO_PATH)

    with open(ribbonFile, "r") as f:
        lines = f.readlines()
    f.close()

    for i, line in enumerate(lines):
        containsRSeq = True if "\r" in line else False

        if "toolbox" in line.lower():
            if "<!--" not in line and "--!>" not in line:
                line = line.rstrip()
                commentedLine = "<!-- " + line + " --!>"
                commentedLine += ("\r" if containsRSeq else "")
                commentedLine += "\n"
                lines[i] = commentedLine

    with open(ribbonFile, "w") as f:
        f.writelines(lines)
    f.close()

def showToolboxIcons():
    # refpath = findRobloxStudioPath()
    ribbonFile = os.path.join(ROBLOX_STUDIO_PATH, "RobloxStudioRibbon.xml")
    if not os.path.exists(ribbonFile):
        raise RobloxStudioRibbonNotFoundError("RobloxStudioRibbon.xml cannot be found in path " + refpath)

    with open(ribbonFile, "r") as f:
        lines = f.readlines()
    f.close()

    for i, line in enumerate(lines):
        containsRSeq = True if "\r" in line else False

        if "toolbox" in line.lower():
            if "<!--" in line and "--!>" in line:
                line = line.rstrip()
                commentedLine = line[4:-5]
                commentedLine += ("\r" if containsRSeq else "")
                commentedLine += "\n"
                lines[i] = commentedLine

    with open(ribbonFile, "w") as f:
        f.writelines(lines)
    f.close()

def removeToolboxIcons():
    # refpath = findRobloxStudioPath()
    ribbonFile = os.path.join(ROBLOX_STUDIO_PATH, "RobloxStudioRibbon.xml")
    if not os.path.exists(ribbonFile):
        raise RobloxStudioRibbonNotFoundError("RobloxStudioRibbon.xml cannot be found in path " + ROBLOX_STUDIO_PATH)

    with open(ribbonFile, "r") as f:
        lines = f.readlines()
    f.close()

    for line in lines:
        if "toolbox" in line.lower():
            lines.remove(line)

    with open(ribbonFile, "w") as f:
        f.writelines(lines)
    f.close()

def areToolboxIconsShown():
    status = []
    # refpath = findRobloxStudioPath()
    ribbonFile = os.path.join(ROBLOX_STUDIO_PATH, "RobloxStudioRibbon.xml")
    if not os.path.exists(ribbonFile):
        raise RobloxStudioRibbonNotFoundError("RobloxStudioRibbon.xml cannot be found in path " + ROBLOX_STUDIO_PATH)

    with open(ribbonFile, "r") as f:
        lines = f.readlines()
    f.close()

    for i, line in enumerate(lines):
        if "toolbox" in line.lower():
            if "<!--" not in line and "--!>" not in line:
                status.append(i)
    
    return (True, status) if status else (False, None)

def removeToolboxPlugins():
    # refpath = findRobloxStudioPath()
    status = 0
    toolboxPluginPath = findToolboxPluginPath()
    if not toolboxPluginPath:
        print("failed to find toolbox plugin path try again")
        return
    toolboxPlugin = os.path.join(toolboxPluginPath, "Toolbox.rbxm")
    if not os.path.exists(toolboxPlugin):
        print("failed to find toolbox.rbxm")
        status += 1 << 1
        # raise ToolboxPluginNotFoundError("Toolbox.rbxm cannot be found in path " + toolboxPluginPath)
    toolboxPlugin_sig = os.path.join(toolboxPluginPath, "Toolbox.rbxm.sig")
    if not os.path.exists(toolboxPlugin_sig):
        print("failed to find toolbox.rbxm.sig")
        # raise ToolboxPluginNotFoundError("Toolbox.rbxm.sig cannot be found in path " + toolboxPluginPath)
        status += 1 << 2

    if status == 3:
        return
    if status & 1 != 1:
        os.remove(toolboxPlugin)
    if status & 2 != 2:
        os.remove(toolboxPlugin_sig)

if __name__ == "__main__":
    pass
