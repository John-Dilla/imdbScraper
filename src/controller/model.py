from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import pandas as pd
from pandas.core.frame import DataFrame

class PandasModel(QtCore.QAbstractTableModel):
    """Class for the data model of all dataframes.
    """

    def __init__(self, df = pd.DataFrame(), parent=None): 
        """Initialization method for the class

        Args:
            df (DataFrame): The dataframe which is passed. Defaults to pd.DataFrame().
            parent (optional): Defaults to None.
        """
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """Defines the header data.

        Args:
            section (): The secton in the dataframe.
            orientation (): The orientation of the header.
            role (optional): Defaults to QtCore.Qt.DisplayRole.

        Returns:
            : Returns, based on orientation, the indices.
        """

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """Returns the data of cell.

        Args:
            index (int): Returns the index of the data row.
            role (optional): [description]. Defaults to QtCore.Qt.DisplayRole.

        Returns:
            (QtCore.QVariant): The value at a specific cell position of the dataframe. 
        """

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        """Sets the data in the model at a specific index.

        Args:
            index (): The index at which the value is stored.
            value (): The value designated to the position at the index.
            role (): Not used.

        Returns:
            (bool): Bool type if the operation on the model was successful.
        """

        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        self._df.hideColumns(0)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        """Counts the rows of the model.

        Args:
            parent (optional): Defaults to QtCore.QModelIndex().

        Returns:
            (int): Number of total rows.
        """

        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        """Counts the columns of the model.

        Args:
            parent (optional): Defaults to QtCore.QModelIndex().

        Returns:
            (int): Number of total columns.
        """

        return len(self._df.columns)

    def sort(self, column, order):
        """Sorts the data for a specific column in the model.

        Args:
            column (): The column which is sorted.
            order (): Order in which the column is sorted.
        """

        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()