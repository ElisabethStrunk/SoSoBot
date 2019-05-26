#***************************************************************
#	Imports
#***************************************************************
import os

#***************************************************************
#	Globals
#***************************************************************

#***************************************************************
#	Class definition
#***************************************************************
class HornCtrl:

  """Control of the horn.

  Keyword arguments:
  """

  def __init__(self, name):
    self.name = 'Horn_' + name

  def backward(self):
    self._play('/home/pi/SoSoBot/rasppi_software/resources/horn1.mp3')

  def stop(self):
    self._play('/home/pi/SoSoBot/rasppi_software/resources/horn1.mp3')

  def _play(self, path_mp3):
    os.system('mpg321 ' +  path_mp3 + ' &')


#***************************************************************
#	Objects
#***************************************************************
horn_1 = HornCtrl('1')
