import os
import json
import shutil

class SavesManager:
    def __init__(self):
        self.SAVES = {}
        self.profiles = []
        with open('saves.sv', 'r', encoding='utf-8') as file:
            self.saves_data = json.loads(file.read())
        self.init_all_saves()
        self.Init_profiles()

    def init_all_saves(self):
        for save in self.saves_data:
            self.SAVES.update({save['name'] : Save(save['name'], save['path'], save['profile_path'])})

    def Delete_save(self, name):
        self.SAVES[name].Delete()
        self.SAVES.pop(name)
        num = 0
        for save_data in self.saves_data:
            if save_data["name"] == name:
                break
            num += 1
        self.saves_data.pop(num)

        self.Save_saves_data()

    def Create_save(self, name, profile_path):
        new_save = Save(name, os.path.join("SAVES", name), profile_path)
        new_save.Save()
        self.SAVES.update({name : new_save})

        self.saves_data.append({
            "name" : name,
            "path" : new_save.path,
            "profile_path" : profile_path
        })
        self.Save_saves_data()

    def Save_saves_data(self):
        with open('saves.sv', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.saves_data))

    def Get_saves_names(self):
        saves = [save for save in self.SAVES.keys()]
        return saves
    
    def Get_profiles(self):
        return self.profiles
    
    def Init_profiles(self):
        for file in os.listdir(os.path.join("PROFILES")):
            if os.path.isdir(os.path.join("PROFILES", file)) == False:
                self.profiles.append(file)
    def Get_profile_path(self, profile_name):
        return os.path.join("PROFILES", profile_name)
    
    def Load_save(self, name):
        self.SAVES[name].Load()

    def Reset(self, name):
        self.SAVES[name].delete_location_files()
                

class Save:
    def __init__(self, name, path, profile_path):
        self.name = name
        self.path = path
        self.profile = None
        self.profile_path = profile_path
        self.load_data(self.profile_path)

    def load_data(self, profile_path):
        with open(f"PROFILES//{profile_path}", 'r', encoding='utf-8') as file:
            self.profile = json.loads(file.read())
            if self.profile["expand_user"] == True:
                self.profile["location"] = os.path.expanduser(self.profile["location"])
    
    def Load(self):
        self.delete_location_files()

        if self.profile['copy_all'] == True:
            for file in os.listdir(self.path):
                if os.path.isdir(os.path.join(self.path, file)):
                    shutil.copytree(os.path.join(self.path, file), os.path.join(self.profile['location'], file))
                else:
                    shutil.copyfile(os.path.join(self.path, file), os.path.join(self.profile['location'], file))
        else:
            for file in self.profile['files']:
                if os.path.isdir(os.path.join(self.path, file)):
                    shutil.copytree(os.path.join(self.path, file), os.path.join(self.profile['location'], file))
                else:
                    shutil.copyfile(os.path.join(self.path, file), os.path.join(self.profile['location'], file))

    def delete_location_files(self):
        if self.profile["copy_all"] == True:
            for file in os.listdir(self.profile['location']):
                if os.path.isdir(os.path.join(self.profile['location'], file)):
                    shutil.rmtree(os.path.join(self.profile['location'], file))
                else:
                    os.remove(os.path.join(self.profile['location'], file))
        else:
            for file in self.profile["files"]:
                try:
                    if os.path.isdir(os.path.join(self.profile['location'], file)):
                        shutil.rmtree(os.path.join(self.profile['location'], file))
                    else:
                        os.remove(os.path.join(self.profile['location'], file))
                except:
                    pass

    def Delete(self):
        shutil.rmtree(os.path.join(self.path))
    
    def Save(self):
        dir = os.path.join("SAVES", self.name)
        os.makedirs(dir)
        game_save_path = self.profile['location']
        
        if self.profile['copy_all'] == True:
            for file in os.listdir(game_save_path):
                if os.path.isdir(os.path.join(game_save_path, file)):
                    shutil.copytree(os.path.join(game_save_path, file), os.path.join(self.path, file))
                else:
                    shutil.copyfile(os.path.join(game_save_path, file), os.path.join(self.path, file))
        else:
            for file in self.profile['files']:
                if os.path.isdir(os.path.join(game_save_path, file)):
                    shutil.copytree(os.path.join(game_save_path, file), os.path.join(self.path, file))
                else:
                    shutil.copyfile(os.path.join(game_save_path, file), os.path.join(self.path, file))