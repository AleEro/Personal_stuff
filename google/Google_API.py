import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:
    def __init__(self):
        # # авторизация
        CREDENTIALS_FILE = r'gosheetsapi-785538c330cd.json'  # имя файла с закрытым ключом

        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                       ['https://www.googleapis.com/auth/spreadsheets',
                                                                        'https://www.googleapis.com/auth/drive'])

        self.httpAuth = credentials.authorize(httplib2.Http())
        self.sheetId = 0
        self.requests = []
        self.service = googleapiclient.discovery.build('sheets', 'v4', http=self.httpAuth)
        self.valueRanges = []
        self.spreadsheet = None
        self.spreadsheetId = None
        self.sheetTitle = None
        self.table_values = None

    def create_table(self, spreadsheet_title='Сие есть название документа', sheet_title='Сие есть название листа'):
        self.spreadsheet = self.service.spreadsheets().create(
            body={'properties': {'autoRecalc': 'ON_CHANGE',
                                 'defaultFormat': {
                                     'backgroundColor': {'blue': 1,
                                                         'green': 1,
                                                         'red': 1},
                                     'padding': {'bottom': 2,
                                                 'left': 3,
                                                 'right': 3,
                                                 'top': 2},
                                     'textFormat': {'bold': False,
                                                    'fontFamily': 'arial,sans,sans-serif',
                                                    'fontSize': 10,
                                                    'foregroundColor': {},
                                                    'italic': False,
                                                    'strikethrough': False,
                                                    'underline': False},
                                     'verticalAlignment': 'BOTTOM',
                                     'wrapStrategy': 'OVERFLOW_CELL'},
                                 'locale': 'ru_RU',
                                 'timeZone': 'Etc/GMT',
                                 'title': f'{spreadsheet_title}'},
                  'sheets': [
                      {'properties': {
                          'gridProperties': {'columnCount': 5,
                                             'rowCount': 8},
                          'index': 0,
                          'sheetId': 0,
                          'sheetType': 'GRID',
                          'title': f'{sheet_title}'}}],
                  'spreadsheetId': ''}).execute()

        self.spreadsheetId = self.spreadsheet['spreadsheetId']
        self.sheetTitle = self.spreadsheet['sheets'][0]['properties']['title']

    def get_table(self, table_id):
        self.spreadsheet = self.service.spreadsheets().get(spreadsheetId=table_id).execute()
        self.spreadsheetId = self.spreadsheet['spreadsheetId']
        self.sheetTitle = self.spreadsheet['sheets'][0]['properties']['title']
        # pprint(self.spreadsheet)

    def get_values(self, table_id=None, tb_min=None, tb_max=None):
        """
        get the table values in range from tb_min to tb_max
        :param str table_id:
        :param int tb_min:
        :param int tb_max:
        :return:
        """

        if table_id is None:
            results = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet['spreadsheetId'],
                                                               range=f'{self.sheetTitle}!A1:E8'
                                                               ).execute()
        else:
            self.get_table(table_id)
            results = self.service.spreadsheets().values().get(spreadsheetId=table_id,
                                                               range=f'{self.sheetTitle}!{tb_min}:{tb_max}',
                                                               dateTimeRenderOption='FORMATTED_STRING',
                                                               valueRenderOption='FORMULA'
                                                               ).execute()
        self.table_values = results.get('values', [])
        return self.table_values

    def give_access(self, role='writer', email_address='paradox.wolf95@gmail.com'):
        """
            access to read / write
            :param role: reader / writer
            :param email_address: now it's paradox.wolf95@gmail.com
            :return:
        """
        googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth).permissions().create(
            fileId=self.spreadsheet['spreadsheetId'],
            body={'type': 'user',
                  'role': f'{role}',
                  'emailAddress': f'{email_address}'},
            fields='id').execute()

    def prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize):
        self.requests.append({"updateDimensionProperties": {"range": {"sheetId": self.sheetId,
                                                                      "dimension": dimension,
                                                                      "startIndex": startIndex,
                                                                      "endIndex": endIndex},
                                                            "properties": {"pixelSize": pixelSize},
                                                            "fields": "pixelSize"}})

    def insert_dimension(self, startIndex, endIndex, sheetId=None, dimension="COLUMNS", inheritFromBefore=True):
        """
            Add row or column
            :param str sheetId: id of sheet in spreadsheet
            :param str dimension: "ROWS" or "COLUMNS"
            :param int startIndex: from 0 to any
            :param int endIndex: from 0 to any but(-1)
            :param bool inheritFromBefore: make new cell same as previous cell
            :return:
        """

        if sheetId is None:
            sheetId = self.sheetId

        self.requests.append({"insertDimension": {"range": {"sheetId": sheetId,
                                                            "dimension": dimension,
                                                            "startIndex": startIndex,
                                                            "endIndex": endIndex
                                                            },
                                                  "inheritFromBefore": inheritFromBefore}})

    def prepare_setColumnsWidth(self, startCol, endCol, width):
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col, width):
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setValues(self, cellsRange, values, majorDimension="ROWS"):
        self.valueRanges.append(
            {"range": self.sheetTitle + "!" + cellsRange,
             "majorDimension": majorDimension,
             "values": values})

    def prepare_setValue(self, cell, value):
        self.prepare_setValues(cellsRange=f'{cell}',
                               majorDimension="ROWS",
                               values=value)

    def set_color(self, cell, hex_color):
        pass

    def runPrepared(self, value_input_option="USER_ENTERED"):
        upd1_res = {'replies': []}
        upd2_res = {'responses': []}
        try:
            if len(self.requests) > 0:
                upd1_res = self.service.spreadsheets().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                   body={
                                                                       "requests": self.requests}).execute()
            if len(self.valueRanges) > 0:
                upd2_res = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                            body={
                                                                                "valueInputOption": value_input_option,
                                                                                "data": self.valueRanges}).execute()
        finally:
            self.requests = []
            self.valueRanges = []
        return upd1_res['replies'], upd2_res['responses']
