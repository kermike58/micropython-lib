"""
The MIT License (MIT)

Copyright (c) 2023 Arduino SA
Copyright (c) 2018 KPN (Jan Bogaerts)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


from senml import *
import utime as time


pack = SenmlPack("device_name")
temp = SenmlRecord("temperature", unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
int_val = SenmlRecord("int_val", sum=100)

pack.add(temp)
pack.add(door_pos)
pack.add(int_val)

pack.base_time = time.time()
pack.base_value = 5
pack.base_sum = 50
time.sleep(2)
temp.time = time.time()


print(pack.to_json())
