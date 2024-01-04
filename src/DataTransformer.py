from abc import ABC,abstractmethod
import pandas as pd

class DataTransformer(ABC):
    @abstractmethod
    def load_data(filepath, sep):
        pass 
    
    @abstractmethod
    def transform_data(initial_data, columns_to_drop=None):
        pass 
    
    @abstractmethod
    def get_transformed_data(transformed_data):
        pass
    

class TecanDataTransformer(DataTransformer):
    @staticmethod
    def load_data(file_path, sep="\t"):
        return pd.read_csv(file_path, sep=sep)
    
    @staticmethod
    def transform_data(initial_data, columns_to_drop=['Cycle','Temp. [°C]','Time_individual[s]']):
        # Transpose the dataframe so that each row represents a cycle
        transposed_data = initial_data.set_index('Cycle Nr.').T

        # Reset index to make it a proper column
        transposed_data = transposed_data.reset_index().rename(columns={'index': 'Cycle'})

        return transposed_data.loc[:, ~transposed_data.columns.isin(columns_to_drop)]
        
    @staticmethod
    def get_transformed_data(transformed_data):
        return transformed_data

    
