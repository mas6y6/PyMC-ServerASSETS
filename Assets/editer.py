class server:
    def __init__(self, dir):
        self.directory = dir
        self.file = open(f"{dir}/server.properties","r+")
        self.lines = open(f"{dir}/server.properties","r").readlines()

    def difficulty(self, value):
        self.lines[7] = f"difficulty={value}\n"
    
    def gamemode(self, value):
        self.lines[18] = f"gamemode={value}\n"
    
    def hardcore(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[21] = f"hardcore={value2}\n"
    
    def motd(self, value):
        self.lines[32] = f"motd={value}\n"

    def max_players(self, value):
        self.lines[29] = f"max-players={value}\n"
    
    def seed(self, value):
        self.lines[26] = f"level-seed={value}\n"
    
    def server_port(self, value):
        self.lines[48] = f"server-port={value}\n"
    
    def server_ip(self, value):
        self.lines[47] = f"server-ip={value}\n"

    def get(self, value):
        self._update()
        d = self.lines[value].split('=')[1]
        return d.replace('\n','')
    
    def white_list(self, value: bool):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[58] = f"white_list={value2}\n"
    
    def force_gamemode(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[16] = f"force-gamemode={value2}\n"
    
    def allow_nether(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[3] = f"allow-nether={value2}\n"
    
    def allow_flying(self, value):
        if value == True:
            value2 = "false"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[2] = f"allow-flight={value2}\n"

    def enforce_secure_profile(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[13] = f"enforce-secure-profile={value2}\n"
    
    def generate_structures(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[19] = f"generate-structures={value2}\n"
    
    def pvp(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[38] = f"pvp={value2}\n"
    
    def summon_animals(self, value):
        if value == True:
            value2 = "true"
        elif value == True:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[50] = f"spawn-animals={value2}\n"
    
    def summon_monsters(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[51] = f"spawn-monsters={value2}\n"
    
    def summon_npcs(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[52] = f"spawn-npcs={value2}\n"
    
    def enable_command_block(self, value):
        if value == True:
            value2 = "true"
        elif value == False:
            value2 = "false"
        else:
            raise TypeError(value)
        self.lines[8] = f"enable-command-block={value2}\n"

    def save(self):
        self.file.seek(0)
        self.file.writelines(self.lines)
        self.file.truncate()
        self._update()

    def _update(self):
        self.lines = open(f"{self.directory}/server.properties","r").readlines()

    def close(self):
        self.save()
        self.file.close()