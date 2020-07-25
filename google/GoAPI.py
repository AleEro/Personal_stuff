import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# # авторизация
CREDENTIALS_FILE = r'google_key\gosheetsapi-bdc92f985a74.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())


# results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
#   "requests": [
#
#     # Задать ширину столбца A: 317 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": 0,
#           "dimension": "COLUMNS",  # COLUMNS - потому что столбец
#           "startIndex": 0,         # Столбцы нумеруются с нуля
#           "endIndex": 1            # startIndex берётся включительно, endIndex - НЕ включительно,
#                                    # т.е. размер будет применён к столбцам в диапазоне [0,1), т.е. только к столбцу A
#         },
#         "properties": {
#           "pixelSize": 317     # размер в пикселях
#         },
#         "fields": "pixelSize"  # нужно задать только pixelSize и не трогать другие параметры столбца
#       }
#     },
#
#     # Задать ширину столбца B: 200 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": 0,
#           "dimension": "COLUMNS",
#           "startIndex": 1,
#           "endIndex": 2
#         },
#         "properties": {
#           "pixelSize": 200
#         },
#         "fields": "pixelSize"
#       }
#     },
#
#     # Задать ширину столбцов C и D: 165 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": 0,
#           "dimension": "COLUMNS",
#           "startIndex": 2,
#           "endIndex": 4
#         },
#         "properties": {
#           "pixelSize": 165
#         },
#         "fields": "pixelSize"
#       }
#     },
#
#     # Задать ширину столбца E: 100 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": 0,
#           "dimension": "COLUMNS",
#           "startIndex": 4,
#           "endIndex": 5
#         },
#         "properties": {
#           "pixelSize": 100
#         },
#         "fields": "pixelSize"
#       }
#     }
#   ]
# }).execute()


class Spreadsheet:
    def __init__(self):
        self.sheetId = 0
        self.requests = []
        # self.sheetTitle = '0'
        self.service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
        self.valueRanges = []
        self.spreadsheet = None
        self.spreadsheetId = None
        self.sheetTitle = None

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

    def get_data(self, table_id=None, tb_min=None, tb_max=None):
        if table_id is None:
            results = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet['spreadsheetId'],
                                                               range=f'{self.sheetTitle}!A1:E8').execute()
            values = results.get('values', [])
        else:
            self.get_table(table_id)
            results = self.service.spreadsheets().values().get(spreadsheetId=table_id,
                                                               range=f'{self.sheetTitle}!{tb_min}:{tb_max}',
                                                               dateTimeRenderOption='FORMATTED_STRING',
                                                               valueRenderOption='FORMULA'
                                                               ).execute()
            values = results.get('values', [])
        pprint(values)

    def give_access(self, role='writer', email_address='paradox.wolf95@gmail.com'):
        # предоставление доступа к таблице
        googleapiclient.discovery.build('drive', 'v3', http=httpAuth).permissions().create(
            fileId=self.spreadsheet['spreadsheetId'],
            body={'type': 'user',
                  'role': f'{role}',
                  'emailAddress': f'{email_address}'},
            fields='id').execute()

        # доступ на чтение(reader) /запись(writer)
        # в данном случае это paradox.wolf95@gmail.com

    def prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize):
        self.requests.append({"updateDimensionProperties": {"range": {"sheetId": self.sheetId,
                                                                      "dimension": dimension,
                                                                      "startIndex": startIndex,
                                                                      "endIndex": endIndex},
                                                            "properties": {"pixelSize": pixelSize},
                                                            "fields": "pixelSize"}})

    def prepare_setColumnsWidth(self, startCol, endCol, width):
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col, width):
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setValues(self, cellsRange, values, majorDimension="ROWS"):
        self.valueRanges.append(
            {"range": self.sheetTitle + "!" + cellsRange, "majorDimension": majorDimension, "values": values})

        # spreadsheets.batchUpdate and spreadsheets.values.batchUpdate

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
        try:
            self.get_data()
        finally:
            pass
        return upd1_res['replies'], upd2_res['responses']


# ss - экземпляр нашего класса Spreadsheet
ss = Spreadsheet()
# ss.create_table()
#  https://docs.google.com/spreadsheets/d/1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE/edit?usp=sharing
# ss.get_table('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE')
ss.get_data('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_max=6,tb_min=16)
ss.get_data('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_max=23,tb_min=57)
ss.get_data('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_max=71,tb_min=76)
# ss.give_access()
# ss.prepare_setColumnWidth(0, 317)
# ss.prepare_setColumnWidth(1, 200)
# ss.prepare_setColumnsWidth(2, 3, 165)
# ss.prepare_setColumnWidth(4, 100)
# ss.prepare_setValues("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
# ss.prepare_setValues("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], "COLUMNS")
# ss.runPrepared()
