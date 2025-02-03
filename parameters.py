"""
Created on Mon Feb 03 2025, 11:33:03

@author: Amoy Ashesh
"""
class instruct:
    load_data = True
    load_models = True

class file_paths:
    raw_data_file = 'data\\1725606664466O-result.fits'
    catalogue_file = 'data\\binary_catalog.fits'

class training:
    test_split = 0.2
    training_random_state = 42
    drop_columns = ['solution_id', 'designation', 'source_id', 'target']
    target_column = 'target'

# class ml:
    