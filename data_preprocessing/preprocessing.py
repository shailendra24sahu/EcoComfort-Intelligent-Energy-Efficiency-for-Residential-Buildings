import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA




class Preprocessor:
    """
        This class shall  be used to clean and transform the data before training.

        Version: 1.0
        Revisions: None

        """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object

    def remove_columns(self,data,columns):
        """
                Method Name: remove_columns
                Description: This method removes the given columns from a pandas dataframe.
                Output: A pandas DataFrame after removing the specified columns.
                On Failure: Raise Exception

                Version: 1.0
                Revisions: None

        """
        self.logger_object.log(self.file_object, 'Entered the remove_columns method of the Preprocessor class')
        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(labels=self.columns, axis=1) # drop the labels specified in the columns
            self.logger_object.log(self.file_object,
                                   'Column removal Successful.Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in remove_columns method of the Preprocessor class. Exception message:  '+str(e))
            self.logger_object.log(self.file_object,
                                   'Column removal Unsuccessful. Exited the remove_columns method of the Preprocessor class')
            raise Exception()

    def separate_label_feature(self, data, label_column_name):
        """
                        Method Name: separate_label_feature
                        Description: This method separates the features and a Label Coulmns.
                        Output: Returns two separate Dataframes, one containing features and the other containing Labels .
                        On Failure: Raise Exception

                        Version: 1.0
                        Revisions: None

                """
        self.logger_object.log(self.file_object, 'Entered the separate_label_feature method of the Preprocessor class')
        try:
            self.X=data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y=data[label_column_name] # Filter the Label columns
            self.logger_object.log(self.file_object,
                                   'Label Separation Successful. Exited the separate_label_feature method of the Preprocessor class')
            return self.X,self.Y
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()

    def dropUnnecessaryColumns(self,data,columnNameList):
        """
                        Method Name: dropUnnecessaryColumns
                        Description: This method drops the unwanted columns.

                        Version: 1.0
                        Revisions: None

                                """
        data = data.drop(columnNameList,axis=1)
        return data


    def replaceInvalidValuesWithNull(self,data):

        """
                               Method Name: is_null_present
                               Description: This method replaces invalid values i.e. '?' with null.

                               Version: 1.0
                               Revisions: None

                                       """

        for column in data.columns:
            count = data[column][data[column] == '?'].count()
            if count != 0:
                data[column] = data[column].replace('?', np.nan)
        return data

    def is_null_present(self,data):
        """
                                Method Name: is_null_present
                                Description: This method checks whether there are null values present in the pandas Dataframe or not.
                                Output: Returns True if null values are present in the DataFrame, False if they are not present and
                                        returns the list of columns for which null values are present.
                                On Failure: Raise Exception

                                Version: 1.0
                                Revisions: None

                        """
        self.logger_object.log(self.file_object, 'Entered the is_null_present method of the Preprocessor class')
        self.null_present = False
        self.cols_with_missing_values=[]
        self.cols = data.columns
        try:
            self.null_counts=data.isna().sum() # check for the count of null values per column
            for i in range(len(self.null_counts)):
                if self.null_counts[i]>0:
                    self.null_present=True
                    self.cols_with_missing_values.append(self.cols[i])
            if(self.null_present): # write the logs to see which columns have null values
                self.dataframe_with_null = pd.DataFrame()
                self.dataframe_with_null['columns'] = data.columns
                self.dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
                self.dataframe_with_null.to_csv('preprocessing_data/null_values.csv') # storing the null column information into file
            self.logger_object.log(self.file_object,'Finding missing values is a success.Data written to the null values file. Exited the is_null_present method of the Preprocessor class')
            return self.null_present, self.cols_with_missing_values
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in is_null_present method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Finding missing values failed. Exited the is_null_present method of the Preprocessor class')
            raise Exception()


    def standardScalingData(self,X):
        """
                                Method Name: standardScalingData
                                Description: This method scales all the columns of the pandas Dataframe.
                                Output: Returns scaled pandas dataframe.
                                On Failure: Raise Exception

                                Version: 1.0
                                Revisions: None
        """
        self.logger_object.log(self.file_object, 'Entered the standardScalingData method of the Preprocessor class')
        try:
            
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            X_scaled = pd.DataFrame(X_scaled,columns = X.columns, index=X.index )
            self.logger_object.log(self.file_object, 'Scaling of the data Successful. Exited the standardScalingData method of the Preprocessor class')
            return X_scaled
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in standardScalingData method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Scaling the data failed. Exited the standardScalingData method of the Preprocessor class')
            raise Exception()
            

    def logTransformation(self,X):
        """
                                Method Name: ogTransformation
                                Description: This method transforms all the columns of the pandas Dataframe into log values.
                                Output: Returns pandas dataframe.
                                On Failure: Raise Exception

                                Version: 1.0
                                Revisions: None
        """
        self.logger_object.log(self.file_object, 'Entered the logTransformation method of the Preprocessor class')
        try:
            for column in X.columns:
                X[column] += 1
                X[column] = np.log(X[column])
            
            self.logger_object.log(self.file_object, 'Log transformation Successful. Exited the logTransformation method of the Preprocessor class')
            return X
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in logTransformation method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Log transformation failed. Exited the logTransformation method of the Preprocessor class')
            raise Exception()


    def principal_components(self,X):
        """
                                Method Name: principal_components
                                Description: This method transforms the dataset into n principal components.
                                Output: Returns pandas dataframe.
                                On Failure: Raise Exception

                                Version: 1.0
                                Revisions: None
        """
        self.logger_object.log(self.file_object, 'Entered the principal_components method of the Preprocessor class')
        try:
            self.pca = PCA(n_components=3)
            new_data = self.pca.fit_transform(X)
            self.principal_df = pd.DataFrame(data = new_data,
                            columns = ['principal component 1', 'principal component 2','principal component 3'])
            
            self.logger_object.log(self.file_object, 'principal_components Successful. Exited the principal_components method of the Preprocessor class')
            return self.principal_df
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in principal_components method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'principal_components failed. Exited the principal_components method of the Preprocessor class')
            raise Exception()
        

    def impute_missing_values(self, data):
        """
                                        Method Name: impute_missing_values
                                        Description: This method replaces all the missing values in the Dataframe using KNN Imputer.
                                        Output: A Dataframe which has all the missing values imputed.
                                        On Failure: Raise Exception

                                        Version: 1.0
                                        Revisions: None
                     """
        self.logger_object.log(self.file_object, 'Entered the impute_missing_values method of the Preprocessor class')
        self.data= data
        try:
            imputer=KNNImputer(n_neighbors=3, weights='uniform',missing_values=np.nan)
            self.new_array=imputer.fit_transform(self.data) # impute the missing values
            # convert the nd-array returned in the step above to a Dataframe
            self.new_data=pd.DataFrame(data=(self.new_array), columns=self.data.columns)
            self.logger_object.log(self.file_object, 'Imputing missing values Successful. Exited the impute_missing_values method of the Preprocessor class')
            return self.new_data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
            raise Exception()

    def get_columns_with_zero_std_deviation(self,data):
        """
                                                Method Name: get_columns_with_zero_std_deviation
                                                Description: This method finds out the columns which have a standard deviation of zero.
                                                Output: List of the columns with standard deviation of zero
                                                On Failure: Raise Exception

                                                Version: 1.0
                                                Revisions: None
                             """
        self.logger_object.log(self.file_object, 'Entered the get_columns_with_zero_std_deviation method of the Preprocessor class')
        self.columns=data.columns
        self.data_n = data.describe()
        self.col_to_drop=[]
        try:
            for x in self.columns:
                if (self.data_n[x]['std'] == 0): # check if standard deviation is zero
                    self.col_to_drop.append(x)  # prepare the list of columns with standard deviation zero
            self.logger_object.log(self.file_object, 'Column search for Standard Deviation of Zero Successful. Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            return self.col_to_drop

        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_columns_with_zero_std_deviation method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'Column search for Standard Deviation of Zero Failed. Exited the get_columns_with_zero_std_deviation method of the Preprocessor class')
            raise Exception()