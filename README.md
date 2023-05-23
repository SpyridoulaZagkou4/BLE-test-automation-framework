
# REQUIREMENTS
This framework requires the 3VT testing tool library used by the company to run that is not provided in this repository. The Waves Validation Tool (WVT) – hereafter called 3VT – is a tool for the testing and validation of the RW Bluetooth IP systems.


The other libraries used are:
1. xlrd
2. PyQt4 
3. threading
4. logging
5. struct
6. socket

# USAGE
## 1st step 
Add parameters (DB address, Connection Interval, Latency, TO, ...) to an excel file that test will take as input as is illustrated in the picture. The only restriction is to have block titles and titles for attributes and parameters.

![image](https://user-images.githubusercontent.com/81852029/208056061-4ec360dd-1da6-4ead-863f-77eec1d91800.png)

## 2nd step 
Save excel file and add the destination path to notebook ```ble_test_automation.py``` in self.excel_path variable.
Then, run python main script:
```python ble_test_automation.py```

The overall process of the test is described from the below schemas where there is one central device and other peripherals where they exchange parameters and each peripheral follows a state machine pipeline until they reach a connected state.
![Screenshot 2022-12-16 104230](https://user-images.githubusercontent.com/81852029/208058886-f7d7951a-52e3-4760-a511-77276db494fb.png)
![Screenshot 2022-12-16 104253](https://user-images.githubusercontent.com/81852029/208058936-1afa2b37-abf8-4bad-92b8-a37825ac5381.png)


# RESULTS
The user interface (UI) that we can monitor the test flow is depicted here: 
![image](https://user-images.githubusercontent.com/81852029/204503591-c94f567b-1d66-41c8-afbc-e3e996bc11fd.png)

And the 3 different log destinations (Qt, console, file):
![image](https://user-images.githubusercontent.com/81852029/204503666-507a0d1b-4afe-4bb2-8f0a-286369d0bc87.png)
