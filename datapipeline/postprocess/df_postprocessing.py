from datapipeline.postprocess.data_postprocessing import AbstractFactoryDataPipeline
from IPython import embed
import pandas as pd
import re
import numpy as np
from scipy.spatial import distance_matrix


class DfPostprocessingSimple(AbstractFactoryDataPipeline):
    """
    TODO
    """

    def __init__(self, df):
        self.df = df


    def run(self, resize_factor=1):
        df = self.df       
        df = df[df['conf'] != -1]
        df['text'] = df['text'].apply(lambda x: x.strip())
        df = df[df['text']!=""]
        df['text'] = df['text'].apply(lambda x: x.upper())
        return df


class DfPostprocessingComplete(AbstractFactoryDataPipeline):
    """
    TODO
    """

    def __init__(self, df):
        self.df = df
    
    def run(self):

        room_side_regex = r"[0-9]+[.][0-9]+"

        default_rooms_set = {"DINING ROOM", "KITCHEN", "LIVING ROOM", "BALCONY", "BEDROOM",
                             "BEDROOM 1", "BEDROOM 2", "BEDROOM 3", "BEDROOM 4", "GARAGE", 
                             "MASTER BEDROOM", "SITTING ROOM", "UTILITY", "CONSERVATORY", "RECEPTION ROOM", 
                             "GARDEN","STUDY", "KITCHEN/DINER", "GARAGE/STORE", "KITCHEN/BREAKFAST ROOM"}
                             
        df = self.df       
        df = df[df['conf'] != -1]
        df['text'] = df['text'].apply(lambda x: x.strip())
        df = df[df['text']!=""]
        df['text'] = df['text'].apply(lambda x: x.upper())

        # rooms might be split across multiple rows, need to split
        shifted_text_col = list(df['text'].iloc[1:])
        shifted_text_col.append("")
        df['text_2row'] = df['text'] + " " + shifted_text_col

        # manual fixes of strings that are always misread
        # this list is gathered with experience
        df['text'] = df['text'].apply(lambda x: x.replace("./", ".7"))
        df['text'] = df['text'].apply(lambda x: x.replace("/.", "7."))

        # loop through lines, decide if they contain a room or a side
        df['class'] = ""
        df['side_number'] = ""

        class_list = []
        i = 0
        while i < len(df):
            curr_class = ""
            
            if df['text_2row'].iloc[i] in default_rooms_set:
                curr_class = "room"
                class_list.append(curr_class)
                df['text'].iloc[i] = df['text_2row'].iloc[i]
                i += 1
                curr_class = "DEL"
                class_list.append(curr_class)
                i += 1 # find this more readable this way
            elif df['text'].iloc[i] in default_rooms_set:
                curr_class = "room"
                class_list.append(curr_class)
                i += 1
            
            if curr_class == "":
                regex_list = re.findall(room_side_regex,df['text'].iloc[i])
                if len(regex_list) > 0:
                    curr_class = "room_side"
                    df['side_number'].iloc[i] = float(regex_list[0])
                    class_list.append(curr_class)
                    i += 1
            
            if curr_class == "":
                class_list.append(curr_class)
                i += 1
                
        df['class'] = class_list

        # some column adjustment
        df['value'] = ""
        df['value'][df['class']=="room"] = df['text']
        df['value'][df['class']=="room_side"] = df['side_number']
        df.drop(['text', 'text_2row', 'side_number'], inplace = True, axis = 1)

        # select the two closest distances to the rooms
        df_rooms = df[['left', 'top', 'value']][df['class'] == "room"]
        df_sides = df[['left', 'top', 'value']][df['class'] == "room_side"]

        dist = distance_matrix(df_rooms[['left', 'top']], df_sides[['left', 'top']])

        df_rooms['side_a'] = ""
        df_rooms['side_b'] = ""

        side_a = []
        side_b = []

        for i in range(len(df_rooms)):
            curr_argpart = np.argpartition(dist[i],2)
            curr_side_a = df_sides['value'].iloc[curr_argpart[0]]
            curr_side_b = df_sides['value'].iloc[curr_argpart[1]]
            side_a.append(curr_side_a)
            side_b.append(curr_side_b)
            
        df_rooms['side_a'] = side_a
        df_rooms['side_b'] = side_b

        # finalise formatting

        df_rooms.drop(['left','top'], inplace = True, axis = 1)
        df_rooms['size'] = round(df_rooms['side_a'] * df_rooms['side_b'],2)

        df_rooms.rename(columns = {"value": "room"}, inplace = True)

        df_rooms.reset_index(inplace = True, drop = True)

        return df_rooms



"""
room_side_regex = r'[0-9]+[.][0-9]+'

        default_rooms_set = {"DINING ROOM", "KITCHEN", "LIVING ROOM", 
                             "BEDROOM 1", "BEDROOM 2", "BEDROOM 3", "BEDROOM 4", "GARAGE", 
                             "MASTER BEDROOM", "SITTING ROOM", "UTILITY", "CONSERVATORY", "RECEPTION ROOM", 
                             "GARDEN","STUDY", "KITCHEN/DINER", "GARAGE/STORE", "KITCHEN/BREAKFAST ROOM"}

"""