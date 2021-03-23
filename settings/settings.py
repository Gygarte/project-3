
'''
Settings, so many setings!

'''

project_name = 'sine' #insert a name -- string type
data_file_path = './data/sine.xlsx' #insert a path --string type
data_index_name = 'time' #insert the index column head name --string type

# is True if you want to use more layers 
multilayer = False 

#for training your hypermodel
epochs = 0 #some number -- int type

__all__ = [project_name, data_file_path, data_index_name, multilayer, epochs]