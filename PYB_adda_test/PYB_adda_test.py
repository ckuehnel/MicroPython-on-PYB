 # PYB_adda_test.pyb 
 
 # PyBoard Test of DAC & ADC
 # (c) Claus Kuehnel 2019-02-17 info@ckuehnel.ch

 # PyBoard v1.1 has two DAC channels, connected to X5 and X6
 # There are 16 ADC channels. The ADC channel connected to X19 is used here.
 # Connect X5 & X19 for this test.

import time
from pyb import Pin,DAC, ADC
dac = DAC(Pin('X5'))
adc = ADC(Pin('X19'))

print('\nTesting ADDA subsystem of PyBoard\n')

print('DAC\t ADC\t Diff')
print('-----------------------')

for i in range(256):
  dac.write(i)
  time.sleep_ms(100)
  adcvalue = adc.read()
  time.sleep_ms(50)
  diff = 16 * i
  diff = adcvalue - diff
  print('{0:3d}\t{1:4d}\t{2:4d}'.format(i, adcvalue, diff))
   


