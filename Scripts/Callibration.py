from BaumyClient import BaumyClient as Client
from Picture import Picture

pic = Picture()

class Calibration:
    def __init__(self):
        self.database_1 = None

    def startLedCalibration(self):
        client = Client()

        for i in range(0,49):

            client.sendMessage("next")


            pic.takePicture("/dev/video0")
            pic.calculate_brightest_pixel()
            pic.show_brightest_pixel()





cali = Calibration()
cali.startLedCalibration()