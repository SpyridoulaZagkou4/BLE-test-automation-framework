### HEADER ##############################################################################
#
# @name gap_bcm_p2p_tc_04
# @grp p2p
# @sgrp bcm
# @type f
# @role peripheral / central
# @feat 39-0028
# @brief Directed connectable
# @param no specific
# @time 2
#
### END ##################################################################################

##########################################################################################
# IMPORTS
##########################################################################################
from user_interface import Ui_MainWindow
#, XStream
from PyQt4 import QtCore, QtGui
import sys
import threading
try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


from api.fe.fe_def import DISCGEN
from api.fe.fe_def import hl_err
from api.fe.fe_def import TASK_API
from api.fe.fe_def import TASK_GAPC
from api.fe.fe_def import TASK_GAPM
from api.fe.fe_gap import gap_role
from api.fe.fe_gap import gapc
from api.fe.fe_gap import gapm
from api.hci.hci_def import A_PUB
from api.hci.hci_def import ADV3789
from api.hci.hci_def import ADVALL
from api.hci.hci_def import ERR_LHTERMCON
from api.hci.hci_def import ERR_RTERMCON
from api.hci.hci_def import SCNACT
from api.hci.hci_def import SCNALL
from api.hci.hci_def import SCNDUPEN
from co.wvt_exc import TC_END
from co.wvt_log import wvt_log
from co.wvt_hdr import H1
from api.hci.hci_def import RECV_TO
from co.wvt_types import CStruct
from co.wvt_types import uint8_t
import time
from threading import Timer
import socket

import xlrd
import xl_read
import struct
#import user_interface
from PyQt4 import QtCore, QtGui
import threading
import sys
import logging
import logging
Signal = QtCore.pyqtSignal
Slot = QtCore.pyqtSlot

#appGUI=0
#global appGUI
#mpes=True
#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Signaller(QtCore.QObject):
    signal = Signal(str, logging.LogRecord)

class QtHandler(logging.Handler):

    def __init__(self, slotfunc, *args, **kwargs):
        super(QtHandler, self).__init__(*args, **kwargs)

        self.signaller = Signaller()

        self.signaller.signal.connect(slotfunc)

    def emit(self, record):
        s = self.format(record)

        self.signaller.signal.emit(s, record)

   
##########################################################################################
##@brief Test Case class GGAP Basic Connection Modes and Procedures testing TC04.
##########################################################################################
class ble_test_automation():

    ######################################################################################
    ##@brief Class Constructor - Initialization of Test Case.
    #
    # @param env Environment with device instances and log
    ######################################################################################
    def __init__(self, env):
        # at least one device needed
        assert env.devs != []

        # TC name for titles
        self.tcname = "[" + self.__class__.__name__ + "]"

        # init log
        self.logfile = None

        # recover the device instance - the 1st in environment
        self.dut = env.devs[0]
        self.rtd = env.devs[0]

        # For final print out checks ok per device
        self.nbdevs = 1

        # log file descriptor
        if env.dirpath != None:
            self.logfile = env.dirpath + "log_" + self.tcname + ".txt"
        self.log = wvt_log(self.logfile, "a")

        # change log for device
        self.dut.set_log(self.log)
        self.rtd.set_log(self.log)

        # reset device checks_ok
        self.dut.checks_ok = 0
        self.rtd.checks_ok = 0

        # DUT parameters-------------------------------------------------------------------
        # Central
        self.dut.disc_type = DISCGEN
        self.nb_resp = 10

        self.dut.le_scan_filtduplic = SCNDUPEN
        self.dut.le_scan_type = SCNACT
        self.dut.le_scan_intv = 0x640
        self.dut.le_scan_win = 0x320
        self.dut.le_scan_pol = SCNALL

        self.dut.own_addr_type = A_PUB
        self.dut.con_intv_min = 0xA0
        self.dut.con_intv_max = 0xA0
        self.dut.con_latency = 0x0
        self.dut.le_superv_to = 0x1F4
        self.dut.ce_len_min = 0x0
        self.dut.ce_len_max = 0x140

        # RTD parameters-------------------------------------------------------------------
        # Peripherals
        self.rtd.own_addr_type = A_PUB
        self.rtd.adv_chnl_map = ADV3789
        self.rtd.adv_pol = ADVALL
        self.rtd.adv_intv_min = 0xA0 #0.16 sec
        self.rtd.adv_intv_max = 0x140 #0.32 sec
        self.rtd.adv_data = "\x0A\x09\x41\x64\x76\x52\x65\x70\x6F\x72\x74"
        self.rtd.le_scanrsp_data = "\x09\xFF\x00\x60\x52\x57\x2D\x42\x4C\x45"
        #self.rtd.orig_bd_addr = "\x12\x34\x56\x35\x23\x48"
        #self.rtd.orig_bd_addr = "0x482335563412"

        self.rtd.orig_bd_addr=["\x12\x34\x56\x35\x23\x48" , "\x09\xF4\xF4\x35\x23\x48"]

        # States
        self.Idle='idle'
        self.Connecting='connecting'
        self.Failed='failed'
        self.Connected='connected'
        
        self.Device_Update='Device parameter updating'
        self.Trying_to_connect='trying to connect'
        self.Trying_to_reconnect='trying to reconnect'
        self.Trying_to_update_parameters='trying to update parameters'		
        #self.Sleep_mode='sleep mode'
        self.Disconnected_device='device is disconnected'
        self.Wait_Disconnect_Indication='waiting for disconnect indication'

        # Initial States
        self.states=[self.Idle,self.Idle]
        # Connection Indexes
        self.con_idxs=[0x00,0x01]
        # Number of retries
        self.MAX_RETRY_COUNT=3
        
        self.circles=[0,0]

        self.ip='10.44.24.16'
        self.clientSocket=0
        # Definition of all parameters
        self.all_tests=[]
        self.rtd.bd_address=""
        self.rtd.ble_params=[]
        self.ci_col=0
        self.latency_col=0
        self.tout_col=0
        
        self.retry=0        
        #self.num_of_disconnected_devices=0       
        self.item=0

        self.temp1=0
        self.temp2=0
        self.time_out_1=0
        self.time_out_2=0
        self.first_time_1=True
        self.first_time_2=True
         
       
        self.ui = Ui_MainWindow()
        appGUI = self.ui
        self.app=0    
        #self.excel_path='C:/Users/ptlab1/Desktop/test_spyridoula/TestPlan_tests.xlsx'
        self.excel_path='C:/Users/ptlab1/Documents/sp_zagkou/TestPlan_tests.xlsx'

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)-15s: %(message)s ')

        self.file_handler = logging.FileHandler('c:\\temp\\debug3.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)

        self.qt_handler=QtHandler(self.update_status)
        self.qt_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.qt_handler)

    def cancel_connection_when_time_passes(self):
       # TBC 
       #self.logger.info("Cancel try for connection".format())
       if(self.retry< self.MAX_RETRY_COUNT):
            self.dut.fe.gapm.h2f_cancel_cmd(0)
            # den prolavainei na to tupwsei
            self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Trying_to_reconnect),None))

            self.states[self.cur_peripheral_id]= self.Trying_to_reconnect
            H1(self.log, "Cancel Connection ...")
       else:
            self.state=self.Failed
            H1(self.log, "Failure to Connect")   

    def disconnect_when_time_passes(self,con_idx):
        H1(self.log, "Disconnect Command")     
        #TBH

        for index in range(len(self.con_idxs)):
            if self.con_idxs[index] == con_idx:    
                self.dut.fe.gapc.h2f_disconnect_cmd(index, ERR_RTERMCON)
                self.states[index]=self.Wait_Disconnect_Indication
                self.circles[index]+=1


        if(self.circles[self.cur_peripheral_id]< len(self.rtd.ble_params)):
            timer = Timer(self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.timeout_col], self.disconnect_when_time_passes,[con_idx])
            timer.start()

    def update_parameters_when_time_passes(self):
        #TBH
        #self.logger.info("Start test case Parameter Update for Peripheral {}".format(self.cur_peripheral_id))
        H1(self.log, "Start Desired Test Case Parameters")
        j=float(1.25)
        con_intv_min = self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.ci_col]   #2sec
        con_intv_max = self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.ci_col]   #2sec
        con_latency = self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.latency_col]
        superv_to = self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.tout_col] #8sec
        

        self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Trying_to_update_parameters),None))
        # central requests a connection parameters update
        self.dut.fe.gapc.h2f_param_update_cmd(self.con_idxs[self.cur_peripheral_id], (con_intv_min/j), (con_intv_max/j), con_latency, superv_to/10)   
        self.states[self.cur_peripheral_id]=self.Trying_to_update_parameters


    #def get_current_peripheral(self,peripheral_id,test_id):
    def get_current_peripheral(self,peripheral_id):
        device_object=self.all_tests[peripheral_id]
        self.rtd.bd_address=device_object.bd_address
        self.rtd.ble_params=device_object.ble_params

    ######################################################################################
    ##@brief TC Scenario
    ######################################################################################
    def run_test(self):

        # title of TC
        H1(self.log, self.tcname)
        H1(self.log, "Direct Connection Establishment")

        self.dut.fe_set_config(role=gap_role.GAP_CENTRAL)
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # EXCEL MAIN
        inputWorkbook = xlrd.open_workbook(self.excel_path)
        inputWorksheet = inputWorkbook.sheet_by_name('TestSetup')
        
        # Find Device Set Up Block position
        dev_row, dev_col = xl_read.find_params_position(inputWorksheet, 'Device Setup')
        # Find position of db address attribute
        title_bd_address_col = xl_read.find_title_index(inputWorksheet, 'DB_Address', dev_row, dev_col)
        # Find position of test indexes attribute
        title_test_index_col = xl_read.find_title_index(inputWorksheet, 'Test Setup Index', dev_row, dev_col)
 
        # Find Ble_Params Block position
        ble_row, ble_col = xl_read.find_params_position(inputWorksheet, 'BLE Params')
        # Find position of connection interval attribute
        self.ci_col = xl_read.find_title_index(inputWorksheet, 'CI', ble_row, ble_col)
        # Find position of latency attribute
        self.latency_col = xl_read.find_title_index(inputWorksheet, 'Latency', ble_row, ble_col)
        # Find position of to attribute
        self.tout_col = xl_read.find_title_index(inputWorksheet, 'Tout', ble_row, ble_col)
        
        # Find position of test timeout attribute
        self.timeout_col = xl_read.find_title_index(inputWorksheet, 'Timeout', ble_row, ble_col)
        
        self.all_tests = xl_read.make_list_of_tests(inputWorksheet, dev_row, dev_col,title_bd_address_col,title_test_index_col)
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.cur_peripheral_id=0      
        count=0

        self.clientSocket=self.init_socket()
        self.connect_socket(self.ip,self.clientSocket)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while 1:


            self.get_current_peripheral(self.cur_peripheral_id)

            if self.states[self.cur_peripheral_id] == self.Idle:
                timer1 = Timer(10, self.cancel_connection_when_time_passes)
                timer1.start()
                H1(self.log, "Start Direct Connection procedure")

                self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Idle),None))

                self.logger.info("Central Sends Connection Command".format())
                self.dut.fe_connect(gapm.op.GAPM_CONNECTION_DIRECT, (self.rtd.orig_bd_addr[self.cur_peripheral_id], self.rtd.own_addr_type))

                data = 'A0' # A0=take temperature
                self.clientSocket.sendall(data)
                dataFromServer = self.receive_from_socket(self.clientSocket)
                self.ui.textEdit_2.append(_translate("MainWindow", str('Connection try with peripheral {}.Actual oven temperature: {}{}'.format(self.cur_peripheral_id,dataFromServer[4],dataFromServer[5])), None))
                #self.close_socket(self.clientSocket)             

                # TBH
                #print(self.rtd.bd_address)
                #self.dut.fe_connect(gapm.op.GAPM_CONNECTION_DIRECT,(self.rtd.bd_address, self.rtd.own_addr_type))

                self.retry+=1
                
                self.states[self.cur_peripheral_id]=self.Trying_to_connect

            elif self.states[self.cur_peripheral_id] == self.Failed:

                self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Failed),None))

                H1(self.log, "Connection Failure")
                break

            elif self.states[self.cur_peripheral_id] == self.Connecting: 
                timer2 = Timer(10, self.update_parameters_when_time_passes)
                timer2.start()

                self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Connecting),None))               

                self.states[self.cur_peripheral_id]=self.Trying_to_update_parameters 

            elif self.states[self.cur_peripheral_id] == self.Connected:
                self.logger.info("Peripheral {} on Connected State".format(self.cur_peripheral_id))
                self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Connected),None))

                if self.cur_peripheral_id < len(self.all_tests)-1:
                    self.temp1=self.con_idxs[self.cur_peripheral_id]
                    self.time_out_1=self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.timeout_col]

                    if self.first_time_1 is True:
                        timer = Timer(self.time_out_1, self.disconnect_when_time_passes,[self.temp1])
                        timer.start()
                        self.first_time_1=False

                    H1(self.log, "Sleep Connected State")
                    self.cur_peripheral_id+=1
                    self.get_current_peripheral(self.cur_peripheral_id) 
                elif self.cur_peripheral_id == len(self.all_tests)-1:                   
                    self.temp2=self.con_idxs[self.cur_peripheral_id]
                    self.time_out_2=self.rtd.ble_params[self.circles[self.cur_peripheral_id]][self.timeout_col]

                    if self.first_time_2 is True:
                        timer = Timer(self.time_out_2, self.disconnect_when_time_passes,[self.temp2])
                        timer.start()
                        self.first_time_2=False


                    H1(self.log, "All devices on Connected State")
                    self.cur_peripheral_id=0
                    
                    continue

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            H1(self.log, "Central waits for indication")
            lrx = self.dut.recv_evt()  #8 sec perimenei peripou

            if lrx[0]== gapc.GAPC_CONNECTION_REQ_IND:
                timer1.cancel()
                self.logger.info("Peripheral {} with bd_address {} sends Connection indication".format(self.cur_peripheral_id, self.rtd.bd_address))

                H1(self.log, "Central sends confirmation for connection")
                self.logger.info("Central sends Connection confirmation for peripheral {} with bd_address {}".format(self.cur_peripheral_id, self.rtd.bd_address))
                conidx_ct = lrx[3]
                conhdl_ct = lrx[4]   

                self.dut.fe.gapc.h2f_connection_cfm(conidx_ct)
            
                lrx = self.dut.recv_evt()                
                if lrx[0] == gapc.GAPC_DISCONNECT_IND:
                    continue
                elif lrx[0]== gapm.GAPM_CMP_EVT:
                    self.states[self.cur_peripheral_id]=self.Connecting
                    continue

            elif lrx[0]== gapm.GAPM_CMP_EVT:
                self.states[self.cur_peripheral_id]=self.Idle
                continue

            elif lrx[0]== gapc.GAPC_PARAM_UPDATE_REQ_IND:
                self.logger.info("Peripheral {} send command for parameter update".format(self.cur_peripheral_id))

                H1(self.log, "Connection Parameters confirmation for Update Request")    
                self.ui.treeWidget.topLevelItem(self.cur_peripheral_id).child(self.circles[self.cur_peripheral_id]).setText(3, _translate("MainWindow",str(self.Device_Update),None))
                self.logger.info("Central sends confirmation to Peripheral {} for updating".format(self.cur_peripheral_id))

                self.dut.fe.gapc.h2f_param_update_cfm(conidx_ct, True, self.dut.ce_len_min, self.dut.ce_len_max)
                    
                lrx = self.dut.recv_evt()
                if lrx[0] == gapc.GAPC_DISCONNECT_IND:
                     self.states[self.cur_peripheral_id]=self.Idle
                     continue
                elif lrx[0]== gapc.GAPC_PARAM_UPDATED_IND:
                     continue
                continue

            elif lrx[0] == gapc.GAPC_PARAM_UPDATED_IND:
                self.logger.info("TEST CASE:Peripheral {} sends Indication for Test Parameter Updating".format(self.cur_peripheral_id))

                self.states[self.cur_peripheral_id]=self.Connected
                lrx = self.dut.recv_evt()

                if lrx[0]== gapm.GAPM_CMP_EVT:
                    continue
                continue

            elif lrx[0]== gapc.GAPC_DISCONNECT_IND:
                data = 'A0' # A0=take temperature
                self.clientSocket.sendall(data)
                dataFromServer = self.receive_from_socket(self.clientSocket)
                self.ui.textEdit_2.append(_translate("MainWindow", str('Disconnection.Actual oven temperature: {}{}'.format(dataFromServer[4],dataFromServer[5])), None))

                if self.circles[self.cur_peripheral_id] < len(self.rtd.ble_params):
                    discon_idx = lrx[3]
                    if self.con_idxs[self.cur_peripheral_id] == discon_idx:
                        self.logger.critical("DISCONNECTION! Peripheral {} with connection index {} sends disconnection indication".format(self.cur_peripheral_id,discon_idx))

                        timer2.cancel()
                        self.states[self.cur_peripheral_id]=self.Idle


                        self.retry=0
                    elif discon_idx != self.con_idxs[self.cur_peripheral_id]:
                        for index in range(len(self.con_idxs)):
                            if self.con_idxs[index] == discon_idx:    
                                self.logger.critical("DISCONNECTION! Peripheral {} with connection index {} sends disconnection indication".format(index,self.con_idxs[index])) 

                                self.states[index]= self.Idle
                                self.retry=0
                    
                    print("Disconnection")
                    continue
                else:
                    #timer.cancel()
                    print("end of test")
                    self.logger.critical("END OF ALL TESTS".format())
                    self.states[self.cur_peripheral_id]=self.Failed
                    #break    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def init_socket(self): 
        # Create a client Socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        return clientSocket

    def connect_socket(self,ip,clientSocket):
        try:
            # Connect to the server
            clientSocket.connect((ip, 1080))
        except:
            print("Connection failed")

    def receive_from_socket(self,clientSocket):
        # Receive data from Socket
        dataFromServer = clientSocket.recv(1024)
        return dataFromServer

    def close_socket(self,clientSocket):
        clientSocket.close()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def update_status( self,status):
    
        if (self.ui):    
            if (len(self.ui.textEdit.toPlainText()) > 500000):
    
                self.ui.textEdit.clear()
            self.ui.textEdit.append(_translate("MainWindow", str("\n" +status), None))
    
            self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())

    def open_win(self):
        self.app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        
        self.ui.setupUi(MainWindow)
        
        MainWindow.show()
        self.app.exec_()

   
        
    def run(self): 
        thread = threading.Thread(target=self.open_win, args=())
        thread.deamon = True
        thread.start()
         
        self.run_test()
        while(True):
           pass

# @}