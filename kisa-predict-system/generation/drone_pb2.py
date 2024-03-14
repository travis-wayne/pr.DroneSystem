# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drone.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x64rone.proto\x12\x18kisa_gcs_system.Services\x1a\x1fgoogle/protobuf/timestamp.proto\"\\\n\x18UpdateDroneStatusPayload\x12@\n\rdroneStatuses\x18\x01 \x03(\x0b\x32).kisa_gcs_system.Services.GrpcDroneStatus\"\xe7\x02\n\x0fGrpcDroneStatus\x12\x14\n\x07\x44roneId\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x46lightId\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08IsOnline\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x15\n\x08IsLanded\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x18\n\x0b\x43ontrollStt\x18\x05 \x01(\tH\x04\x88\x01\x01\x12=\n\x08\x44roneStt\x18\x06 \x01(\x0b\x32&.kisa_gcs_system.Services.GrpcDroneSttH\x05\x88\x01\x01\x12\x41\n\nSensorData\x18\x07 \x01(\x0b\x32(.kisa_gcs_system.Services.GrpcSensorDataH\x06\x88\x01\x01\x42\n\n\x08_DroneIdB\x0b\n\t_FlightIdB\x0b\n\t_IsOnlineB\x0b\n\t_IsLandedB\x0e\n\x0c_ControllSttB\x0b\n\t_DroneSttB\r\n\x0b_SensorData\"\x96\x04\n\x0cGrpcDroneStt\x12\x13\n\x06PowerV\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x17\n\nBatteryStt\x18\x02 \x01(\x11H\x01\x88\x01\x01\x12\x13\n\x06GpsStt\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05TempC\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x10\n\x03Lat\x18\x05 \x01(\x01H\x04\x88\x01\x01\x12\x10\n\x03Lon\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x10\n\x03\x41lt\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x16\n\tGlobalAlt\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12\x11\n\x04Roll\x18\t \x01(\x01H\x08\x88\x01\x01\x12\x12\n\x05Pitch\x18\n \x01(\x01H\t\x88\x01\x01\x12\x11\n\x04Head\x18\x0b \x01(\x05H\n\x88\x01\x01\x12\x12\n\x05Speed\x18\x0c \x01(\x02H\x0b\x88\x01\x01\x12\x15\n\x08HoverStt\x18\r \x01(\tH\x0c\x88\x01\x01\x12\x11\n\x04HDOP\x18\x0e \x01(\x01H\r\x88\x01\x01\x12\x1c\n\x0fSatellitesCount\x18\x0f \x01(\x05H\x0e\x88\x01\x01\x12\x17\n\nFlightMode\x18\x10 \x01(\x05H\x0f\x88\x01\x01\x42\t\n\x07_PowerVB\r\n\x0b_BatterySttB\t\n\x07_GpsSttB\x08\n\x06_TempCB\x06\n\x04_LatB\x06\n\x04_LonB\x06\n\x04_AltB\x0c\n\n_GlobalAltB\x07\n\x05_RollB\x08\n\x06_PitchB\x07\n\x05_HeadB\x08\n\x06_SpeedB\x0b\n\t_HoverSttB\x07\n\x05_HDOPB\x12\n\x10_SatellitesCountB\r\n\x0b_FlightMode\"\xea\x12\n\x0eGrpcSensorData\x12\x1a\n\rroll_ATTITUDE\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0epitch_ATTITUDE\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x19\n\x0cyaw_ATTITUDE\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x19\n\x0cxacc_RAW_IMU\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x19\n\x0cyacc_RAW_IMU\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x19\n\x0czacc_RAW_IMU\x18\x06 \x01(\x05H\x05\x88\x01\x01\x12\x1a\n\rxgyro_RAW_IMU\x18\x07 \x01(\x05H\x06\x88\x01\x01\x12\x1a\n\rygyro_RAW_IMU\x18\x08 \x01(\x05H\x07\x88\x01\x01\x12\x1a\n\rzgyro_RAW_IMU\x18\t \x01(\x05H\x08\x88\x01\x01\x12\x19\n\x0cxmag_RAW_IMU\x18\n \x01(\x05H\t\x88\x01\x01\x12\x19\n\x0cymag_RAW_IMU\x18\x0b \x01(\x05H\n\x88\x01\x01\x12\x19\n\x0czmag_RAW_IMU\x18\x0c \x01(\x05H\x0b\x88\x01\x01\x12\"\n\x15vibration_x_VIBRATION\x18\r \x01(\x02H\x0c\x88\x01\x01\x12\"\n\x15vibration_y_VIBRATION\x18\x0e \x01(\x02H\r\x88\x01\x01\x12\"\n\x15vibration_z_VIBRATION\x18\x0f \x01(\x02H\x0e\x88\x01\x01\x12\'\n\x1a\x61\x63\x63\x65l_cal_x_SENSOR_OFFSETS\x18\x10 \x01(\x02H\x0f\x88\x01\x01\x12\'\n\x1a\x61\x63\x63\x65l_cal_y_SENSOR_OFFSETS\x18\x11 \x01(\x02H\x10\x88\x01\x01\x12\'\n\x1a\x61\x63\x63\x65l_cal_z_SENSOR_OFFSETS\x18\x12 \x01(\x02H\x11\x88\x01\x01\x12%\n\x18mag_ofs_x_SENSOR_OFFSETS\x18\x13 \x01(\x05H\x12\x88\x01\x01\x12%\n\x18mag_ofs_y_SENSOR_OFFSETS\x18\x14 \x01(\x05H\x13\x88\x01\x01\x12#\n\x16vx_GLOBAL_POSITION_INT\x18\x15 \x01(\x05H\x14\x88\x01\x01\x12#\n\x16vy_GLOBAL_POSITION_INT\x18\x16 \x01(\x05H\x15\x88\x01\x01\x12!\n\x14x_LOCAL_POSITION_NED\x18\x17 \x01(\x02H\x16\x88\x01\x01\x12\"\n\x15vx_LOCAL_POSITION_NED\x18\x18 \x01(\x02H\x17\x88\x01\x01\x12\"\n\x15vy_LOCAL_POSITION_NED\x18\x19 \x01(\x02H\x18\x88\x01\x01\x12,\n\x1fnav_pitch_NAV_CONTROLLER_OUTPUT\x18\x1a \x01(\x02H\x19\x88\x01\x01\x12.\n!nav_bearing_NAV_CONTROLLER_OUTPUT\x18\x1b \x01(\x05H\x1a\x88\x01\x01\x12(\n\x1bservo3_raw_SERVO_OUTPUT_RAW\x18\x1c \x01(\rH\x1b\x88\x01\x01\x12(\n\x1bservo8_raw_SERVO_OUTPUT_RAW\x18\x1d \x01(\rH\x1c\x88\x01\x01\x12 \n\x13groundspeed_VFR_HUD\x18\x1e \x01(\x02H\x1d\x88\x01\x01\x12\x1d\n\x10\x61irspeed_VFR_HUD\x18\x1f \x01(\x02H\x1e\x88\x01\x01\x12&\n\x19press_abs_SCALED_PRESSURE\x18  \x01(\x02H\x1f\x88\x01\x01\x12 \n\x13Vservo_POWER_STATUS\x18! \x01(\rH \x88\x01\x01\x12%\n\x18voltages1_BATTERY_STATUS\x18\" \x01(\x01H!\x88\x01\x01\x12\"\n\x15\x63hancount_RC_CHANNELS\x18# \x01(\x05H\"\x88\x01\x01\x12#\n\x16\x63han12_raw_RC_CHANNELS\x18$ \x01(\rH#\x88\x01\x01\x12#\n\x16\x63han13_raw_RC_CHANNELS\x18% \x01(\rH$\x88\x01\x01\x12#\n\x16\x63han14_raw_RC_CHANNELS\x18& \x01(\rH%\x88\x01\x01\x12#\n\x16\x63han15_raw_RC_CHANNELS\x18\' \x01(\rH&\x88\x01\x01\x12#\n\x16\x63han16_raw_RC_CHANNELS\x18( \x01(\rH\'\x88\x01\x01\x42\x10\n\x0e_roll_ATTITUDEB\x11\n\x0f_pitch_ATTITUDEB\x0f\n\r_yaw_ATTITUDEB\x0f\n\r_xacc_RAW_IMUB\x0f\n\r_yacc_RAW_IMUB\x0f\n\r_zacc_RAW_IMUB\x10\n\x0e_xgyro_RAW_IMUB\x10\n\x0e_ygyro_RAW_IMUB\x10\n\x0e_zgyro_RAW_IMUB\x0f\n\r_xmag_RAW_IMUB\x0f\n\r_ymag_RAW_IMUB\x0f\n\r_zmag_RAW_IMUB\x18\n\x16_vibration_x_VIBRATIONB\x18\n\x16_vibration_y_VIBRATIONB\x18\n\x16_vibration_z_VIBRATIONB\x1d\n\x1b_accel_cal_x_SENSOR_OFFSETSB\x1d\n\x1b_accel_cal_y_SENSOR_OFFSETSB\x1d\n\x1b_accel_cal_z_SENSOR_OFFSETSB\x1b\n\x19_mag_ofs_x_SENSOR_OFFSETSB\x1b\n\x19_mag_ofs_y_SENSOR_OFFSETSB\x19\n\x17_vx_GLOBAL_POSITION_INTB\x19\n\x17_vy_GLOBAL_POSITION_INTB\x17\n\x15_x_LOCAL_POSITION_NEDB\x18\n\x16_vx_LOCAL_POSITION_NEDB\x18\n\x16_vy_LOCAL_POSITION_NEDB\"\n _nav_pitch_NAV_CONTROLLER_OUTPUTB$\n\"_nav_bearing_NAV_CONTROLLER_OUTPUTB\x1e\n\x1c_servo3_raw_SERVO_OUTPUT_RAWB\x1e\n\x1c_servo8_raw_SERVO_OUTPUT_RAWB\x16\n\x14_groundspeed_VFR_HUDB\x13\n\x11_airspeed_VFR_HUDB\x1c\n\x1a_press_abs_SCALED_PRESSUREB\x16\n\x14_Vservo_POWER_STATUSB\x1b\n\x19_voltages1_BATTERY_STATUSB\x18\n\x16_chancount_RC_CHANNELSB\x19\n\x17_chan12_raw_RC_CHANNELSB\x19\n\x17_chan13_raw_RC_CHANNELSB\x19\n\x17_chan14_raw_RC_CHANNELSB\x19\n\x17_chan15_raw_RC_CHANNELSB\x19\n\x17_chan16_raw_RC_CHANNELS\"\xa1\x01\n\x0eStatusResponse\x12\x0f\n\x07\x44roneId\x18\x01 \x01(\t\x12>\n\x0bPredictData\x18\x02 \x01(\x0b\x32).kisa_gcs_system.Services.GrpcPredictData\x12>\n\x0bWarningData\x18\x03 \x01(\x0b\x32).kisa_gcs_system.Services.GrpcWarningData\"\xf4\x03\n\x0fGrpcPredictData\x12\x1d\n\x15roll_ATTITUDE_PREDICT\x18\x01 \x01(\x01\x12\x1c\n\x14yaw_ATTITUDE_PREDICT\x18\x02 \x01(\x01\x12\x1e\n\x16pitch_ATTITUDE_PREDICT\x18\x03 \x01(\x01\x12\x1c\n\x14xacc_RAW_IMU_PREDICT\x18\x04 \x01(\x01\x12\x1c\n\x14yacc_RAW_IMU_PREDICT\x18\x05 \x01(\x01\x12\x1c\n\x14zacc_RAW_IMU_PREDICT\x18\x06 \x01(\x01\x12\x1d\n\x15xgyro_RAW_IMU_PREDICT\x18\x07 \x01(\x01\x12\x1d\n\x15ygyro_RAW_IMU_PREDICT\x18\x08 \x01(\x01\x12\x1d\n\x15zgyro_RAW_IMU_PREDICT\x18\t \x01(\x01\x12\x1c\n\x14xmag_RAW_IMU_PREDICT\x18\n \x01(\x01\x12\x1c\n\x14ymag_RAW_IMU_PREDICT\x18\x0b \x01(\x01\x12\x1c\n\x14zmag_RAW_IMU_PREDICT\x18\x0c \x01(\x01\x12%\n\x1dvibration_x_VIBRATION_PREDICT\x18\r \x01(\x01\x12%\n\x1dvibration_y_VIBRATION_PREDICT\x18\x0e \x01(\x01\x12%\n\x1dvibration_z_VIBRATION_PREDICT\x18\x0f \x01(\x01\"\x8b\x04\n\x0fGrpcWarningData\x12\x15\n\rwarning_count\x18\x01 \x01(\x05\x12\x1d\n\x15roll_ATTITUDE_WARNING\x18\x02 \x01(\x08\x12\x1e\n\x16pitch_ATTITUDE_WARNING\x18\x03 \x01(\x08\x12\x1c\n\x14yaw_ATTITUDE_WARNING\x18\x04 \x01(\x08\x12\x1c\n\x14xacc_RAW_IMU_WARNING\x18\x05 \x01(\x08\x12\x1c\n\x14yacc_RAW_IMU_WARNING\x18\x06 \x01(\x08\x12\x1c\n\x14zacc_RAW_IMU_WARNING\x18\x07 \x01(\x08\x12\x1d\n\x15xgyro_RAW_IMU_WARNING\x18\x08 \x01(\x08\x12\x1d\n\x15ygyro_RAW_IMU_WARNING\x18\t \x01(\x08\x12\x1d\n\x15zgyro_RAW_IMU_WARNING\x18\n \x01(\x08\x12\x1c\n\x14xmag_RAW_IMU_WARNING\x18\x0b \x01(\x08\x12\x1c\n\x14ymag_RAW_IMU_WARNING\x18\x0c \x01(\x08\x12\x1c\n\x14zmag_RAW_IMU_WARNING\x18\r \x01(\x08\x12%\n\x1dvibration_x_VIBRATION_WARNING\x18\x0e \x01(\x08\x12%\n\x1dvibration_y_VIBRATION_WARNING\x18\x0f \x01(\x08\x12%\n\x1dvibration_z_VIBRATION_WARNING\x18\x10 \x01(\x08\x32\x86\x01\n\x11\x44roneStatusUpdate\x12q\n\x11UpdateDroneStatus\x12\x32.kisa_gcs_system.Services.UpdateDroneStatusPayload\x1a(.kisa_gcs_system.Services.StatusResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'drone_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_UPDATEDRONESTATUSPAYLOAD']._serialized_start=74
  _globals['_UPDATEDRONESTATUSPAYLOAD']._serialized_end=166
  _globals['_GRPCDRONESTATUS']._serialized_start=169
  _globals['_GRPCDRONESTATUS']._serialized_end=528
  _globals['_GRPCDRONESTT']._serialized_start=531
  _globals['_GRPCDRONESTT']._serialized_end=1065
  _globals['_GRPCSENSORDATA']._serialized_start=1068
  _globals['_GRPCSENSORDATA']._serialized_end=3478
  _globals['_STATUSRESPONSE']._serialized_start=3481
  _globals['_STATUSRESPONSE']._serialized_end=3642
  _globals['_GRPCPREDICTDATA']._serialized_start=3645
  _globals['_GRPCPREDICTDATA']._serialized_end=4145
  _globals['_GRPCWARNINGDATA']._serialized_start=4148
  _globals['_GRPCWARNINGDATA']._serialized_end=4671
  _globals['_DRONESTATUSUPDATE']._serialized_start=4674
  _globals['_DRONESTATUSUPDATE']._serialized_end=4808
# @@protoc_insertion_point(module_scope)
