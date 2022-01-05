import xlrd
import argparse
import sys

# Index = 0
Duration = 0
Retry = 0
CI = 0
Latency = 0
Tout = 0
Rate = 0
PDU = 0


class TestObject():
    def __init__(self):
        self.bd_address = ''
        self.ble_params = []
        # self.current_test=0


def find_params_position(worksheet, des_name):
    for row in range(worksheet.nrows):
        for col in range(worksheet.ncols):
            if worksheet.cell_value(row, col) == des_name:
                params_pos_row = row + 1
                param_pos_col = col
                break
    return params_pos_row, param_pos_col


def find_title_index(worksheet, title_name, params_pos_row, param_pos_col):
    titles = []
    for col in range(param_pos_col, worksheet.ncols):
        temp = worksheet.cell_value(params_pos_row, col)
        if temp != "":
            titles.append(temp)
        else:
            break
    for index in range(len(titles)):
        if titles[index] == title_name:
            title_col = index
    return title_col


def get_params_data(worksheet, params_pos_row, param_pos_col):
    params = []
    for row in range(params_pos_row + 1, worksheet.nrows):
        row_data = []
        for col in range(param_pos_col, worksheet.ncols):
            temp = worksheet.cell_value(row, col)
            if temp != "":
                row_data.append(temp)
            else:
                break
        if col == param_pos_col:
            break
        params.append(row_data)
    return params


def get_ble_params_data(worksheet, params_pos_row, param_pos_col, test_index):
    for row in range(params_pos_row + 1, worksheet.nrows):
        row_data = []
        temp2 = str(int(worksheet.cell_value(row, param_pos_col)))
        if temp2 == test_index:
            for col in range(param_pos_col, worksheet.ncols):
                temp = worksheet.cell_value(row, col)
                if temp != "":
                    row_data.append(temp)
                else:
                    break

            break
        else:
            continue

    params = row_data

    return params


def make_list_of_tests(worksheet, row, col, title_bd_col, title_index_col):
    tests = []
    device_set_up_params = get_params_data(worksheet, row, col)
    for params_row in range(len(device_set_up_params)):
        Test_Case = TestObject()
        Test_Case.bd_address = device_set_up_params[params_row][title_bd_col]
        for ble_index in str(device_set_up_params[params_row][title_index_col]).split(','):
            if ble_index == '0.0': ble_index = '0'
            ble_row, ble_col = find_params_position(worksheet, 'BLE Params')
            device_ble_params = get_ble_params_data(worksheet, ble_row, ble_col, ble_index)
            Test_Case.ble_params.append(device_ble_params)

        tests.append(Test_Case)
    return tests


# if __name__ == '__main__':
#     inputWorkbook = xlrd.open_workbook('C:/Users/ptlab1/Documents/sp_zagkou/TestPlan_tests.xlsx')
#     inputWorksheet = inputWorkbook.sheet_by_name('TestSetup')
# 
#     # Find Device Set Up Block position
#     dev_row, dev_col =find_params_position(inputWorksheet, 'Device Setup')
#     # Find position of db address attribute
#     title_bd_address_col = find_title_index(inputWorksheet, 'DB_Address', dev_row, dev_col)
#     # Find position of test indexes attribute
#     title_test_index_col = find_title_index(inputWorksheet, 'Test Setup Index', dev_row, dev_col)
# 
#     # Find Ble_Params Block position
#     ble_row, ble_col = find_params_position(inputWorksheet, 'BLE Params')
#     # Find position of connection interval attribute
#     ci_col = find_title_index(inputWorksheet, 'CI', ble_row, ble_col)
#     # Find position of latency attribute
#     latency_col = find_title_index(inputWorksheet, 'Latency', ble_row, ble_col)
#     # Find position of to attribute
#     tout_col = find_title_index(inputWorksheet, 'Tout', ble_row, ble_col)
# 
#     # Find position of test timeout attribute
#     timeout_col = find_title_index(inputWorksheet, 'Timeout', ble_row, ble_col)
# 
#     all_tests = make_list_of_tests(inputWorksheet, dev_row, dev_col, title_bd_address_col,
#                                                 title_test_index_col)
