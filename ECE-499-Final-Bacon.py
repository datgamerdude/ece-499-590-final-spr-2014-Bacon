#!/usr/bin/env python
import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

#ha = hubo_ach

s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
s.flush()
r.flush()
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()

left_leg = 0
right_leg = 1
angle = 0.0
cur_angle = 0.0
rad_angle = 0.131
cur_rad = 0.0
count = 0

HP_rad=0
KN_rad=0
AP_rad=0

RHP_rad=0
RKN_rad=0
RAP_rad=0

LHP_rad=0
LKN_rad=0
LAP_rad=0

HP_rad_max=0.376
KN_rad_max=0.75
AP_rad_max=0.376

HP_rad_max2=1.09
KN_rad_max2=2.17
AP_rad_max2=1.09

HP_rad_max3=0.88
KN_rad_max3=1.76
AP_rad_max3=0.88

AP_rad_max4=1

t_speed = 0.25

while(angle<=0.571):
	ref.ref[ha.LHR] = 0
	ref.ref[ha.RHR] = 0
	
	ref.ref[ha.LAR] = 0
	ref.ref[ha.RAR] = 0

	ref.ref[ha.LSR] = angle
	ref.ref[ha.RSR] = -angle
	angle = angle + 0.1
	r.put(ref)	
	time.sleep(t_speed)

cur_rad = 0
while(KN_rad<KN_rad_max):
	if(HP_rad<HP_rad_max):
		HP_rad = HP_rad + 0.01
		ref.ref[ha.LHP] = -HP_rad
		ref.ref[ha.RHP] = -HP_rad
	if(KN_rad<KN_rad_max):
		KN_rad = KN_rad + 0.02
		ref.ref[ha.LKN] = KN_rad
		ref.ref[ha.RKN] = KN_rad
	if(AP_rad<AP_rad_max):
		AP_rad = AP_rad + 0.01
		ref.ref[ha.LAP] = -AP_rad
		ref.ref[ha.RAP] = -AP_rad
	r.put(ref)
	time.sleep(t_speed)

cur_angle = 0
while(cur_rad<rad_angle):
	cur_rad = cur_rad + 0.01
	ref.ref[ha.LHR] = -cur_rad
	ref.ref[ha.RHR] = -cur_rad

	ref.ref[ha.LAR] = cur_rad
	ref.ref[ha.RAR] = cur_rad
	r.put(ref)
	time.sleep(t_speed)

RHP_rad=HP_rad_max
RKN_rad=KN_rad_max
RAP_rad=AP_rad_max
while(RKN_rad<KN_rad_max2):
	if(RHP_rad<HP_rad_max2):
		RHP_rad = RHP_rad + 0.01
		ref.ref[ha.RHP] = -RHP_rad
	if(RKN_rad<KN_rad_max2):
		RKN_rad = RKN_rad + 0.02
		ref.ref[ha.RKN] = RKN_rad
	if(RAP_rad<AP_rad_max2):
		RAP_rad = RAP_rad + 0.01
		ref.ref[ha.RAP] = -RAP_rad
	r.put(ref)
	time.sleep(t_speed)

while(count<5):
	LHP_rad=HP_rad_max
	LKN_rad=KN_rad_max
	LAP_rad=AP_rad_max
	while(LKN_rad<KN_rad_max3):
		if(LHP_rad<HP_rad_max3):
			LHP_rad = LHP_rad + 0.01
			ref.ref[ha.LHP] = -LHP_rad
		if(LKN_rad<KN_rad_max3):
			LKN_rad = LKN_rad + 0.02
			ref.ref[ha.LKN] = LKN_rad
		if(LAP_rad<AP_rad_max3):
			LAP_rad = LAP_rad + 0.01
			ref.ref[ha.LAP] = -LAP_rad
		r.put(ref)
		time.sleep(t_speed)
	
	LHP_rad=HP_rad_max3
	LKN_rad=KN_rad_max3
	LAP_rad=AP_rad_max3
	while(LKN_rad>KN_rad_max):
		if(LHP_rad>HP_rad_max):
			LHP_rad = LHP_rad - 0.01
			ref.ref[ha.LHP] = -LHP_rad
		if(LKN_rad>KN_rad_max):
			LKN_rad = LKN_rad - 0.02
			ref.ref[ha.LKN] = LKN_rad
		if(LAP_rad>AP_rad_max):
			LAP_rad = LAP_rad - 0.01
			ref.ref[ha.LAP] = -LAP_rad
		r.put(ref)
		time.sleep(t_speed)
	
	count = count+1
	print "Count  = ", count

RHP_rad=HP_rad_max2
RKN_rad=KN_rad_max2
RAP_rad=AP_rad_max2
while(RKN_rad>KN_rad_max):
	if(RHP_rad>HP_rad_max):
		RHP_rad = RHP_rad - 0.01
		ref.ref[ha.RHP] = -RHP_rad
	if(RKN_rad>KN_rad_max):
		RKN_rad = RKN_rad - 0.02
		ref.ref[ha.RKN] = RKN_rad
	if(RAP_rad>AP_rad_max):
		RAP_rad = RAP_rad - 0.01
		ref.ref[ha.RAP] = -RAP_rad
	r.put(ref)
	time.sleep(t_speed)

cur_angle = rad_angle
while(cur_rad>0):
	cur_rad = cur_rad - 0.01
	ref.ref[ha.LHR] = -cur_rad
	ref.ref[ha.RHR] = -cur_rad

	ref.ref[ha.LAR] = cur_rad
	ref.ref[ha.RAR] = cur_rad
	
	r.put(ref)
	time.sleep(t_speed)

cur_rad = 0
KN_rad = KN_rad_max
while(KN_rad>0):
	if(HP_rad>0):
		HP_rad = HP_rad - 0.01
		ref.ref[ha.LHP] = -HP_rad
		ref.ref[ha.RHP] = -HP_rad
	if(KN_rad>0):
		KN_rad = KN_rad - 0.02
		ref.ref[ha.LKN] = KN_rad
		ref.ref[ha.RKN] = KN_rad
	if(AP_rad>0):
		AP_rad = AP_rad - 0.01
		ref.ref[ha.LAP] = -AP_rad
		ref.ref[ha.RAP] = -AP_rad
	r.put(ref)
	time.sleep(t_speed)

angle=0.571
while(angle>0):
	angle = angle - 0.1
	ref.ref[ha.LSR] = angle
	ref.ref[ha.RSR] = -angle
	r.put(ref)	
	time.sleep(t_speed)

time.sleep(1.0)
r.close()
s.close()

