# Bluetooth monitoring

```ssh -lpi raspi-moonboard sudo btmon```

## Example
sudo btmon
Bluetooth monitor ver 5.50
= Note: Linux version 5.10.63+ (armv6l)                                0.749830
= Note: Bluetooth subsystem version 2.22                               0.749846
= New Index: B8:27:EB:78:4B:E9 (Primary,UART,hci0)              [hci0] 0.749853
= Open Index: B8:27:EB:78:4B:E9                                 [hci0] 0.749858
= Index Info: B8:27:EB:78:4B:E9 (Broadcom Corporation)          [hci0] 0.749862
@ MGMT Open: btmon (privileged) version 1.18                  {0x0002} 0.749868
@ MGMT Open: bluetoothd (privileged) version 1.18             {0x0001} 0.749873
@ MGMT Open: btmon (privileged) version 1.18                  {0x0003} 0.750001
> ACL Data RX: Handle 64 flags 0x02 dlen 27                  #1 [hci0] 3.977273
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c23533138332c533133392c5039392c5038372c
< ACL Data TX: Handle 64 flags 0x00 dlen 5                   #2 [hci0] 3.988939
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 27                  #3 [hci0] 4.037460
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 5038342c5037382c50332c5032352c503136342c
< ACL Data TX: Handle 64 flags 0x00 dlen 5                   #4 [hci0] 4.048985
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 12                  #5 [hci0] 4.097163
      ATT: Write Request (0x12) len 7
        Handle: 0x000c
          Data: 4531363223
> HCI Event: Number of Completed Packets (0x13) plen 5       #6 [hci0] 4.097906
        Num handles: 1
        Handle: 64
        Count: 2
< ACL Data TX: Handle 64 flags 0x00 dlen 5                   #7 [hci0] 4.107769
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5       #8 [hci0] 4.351125
        Num handles: 1
        Handle: 64
        Count: 1
> ACL Data RX: Handle 64 flags 0x02 dlen 27                  #9 [hci0] 5.777284
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c235333322c5036312c5035372c503130302c45
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #10 [hci0] 5.784852
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 10                 #11 [hci0] 5.837187
      ATT: Write Request (0x12) len 5
        Handle: 0x000c
          Data: 353423
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #12 [hci0] 5.847927
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5      #13 [hci0] 5.897103
        Num handles: 1
        Handle: 64
        Count: 2
> ACL Data RX: Handle 64 flags 0x02 dlen 27                 #14 [hci0] 6.917365
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c235333342c5037392c5036302c5033302c5031
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #15 [hci0] 6.928987
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 25                 #16 [hci0] 6.977342
      ATT: Write Request (0x12) len 20
        Handle: 0x000c
          Data: 38372c503135362c503132372c4531393723
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #17 [hci0] 6.988511
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5      #18 [hci0] 7.037108
        Num handles: 1
        Handle: 64
        Count: 2
> ACL Data RX: Handle 64 flags 0x02 dlen 27                 #19 [hci0] 8.327395
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c2353332c533130392c5036342c5036312c5031
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #20 [hci0] 8.338614
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 19                 #21 [hci0] 8.387308
      ATT: Write Request (0x12) len 14
        Handle: 0x000c
          Data: 37302c503136362c45393023
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #22 [hci0] 8.396136
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5      #23 [hci0] 8.447137
        Num handles: 1
        Handle: 64
        Count: 2
> ACL Data RX: Handle 64 flags 0x02 dlen 27                 #24 [hci0] 9.227406
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c2353342c5333392c5039382c5032382c503137
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #25 [hci0] 9.239194
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 27                 #26 [hci0] 9.287598
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 362c503136392c503136342c503133302c503131
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #27 [hci0] 9.297212
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5      #28 [hci0] 9.347156
        Num handles: 1
        Handle: 64
        Count: 2
> ACL Data RX: Handle 64 flags 0x02 dlen 13                 #29 [hci0] 9.407244
      ATT: Write Request (0x12) len 8
        Handle: 0x000c
          Data: 352c45393023
< ACL Data TX: Handle 64 flags 0x00 dlen 5                  #30 [hci0] 9.418438
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5      #31 [hci0] 9.601239
        Num handles: 1
        Handle: 64
        Count: 1
> ACL Data RX: Handle 64 flags 0x02 dlen 27                #32 [hci0] 10.937405
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c23533138322c533137362c503139352c503138
< ACL Data TX: Handle 64 flags 0x00 dlen 5                 #33 [hci0] 10.945771
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 27                #34 [hci0] 10.997617
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 372c503135352c503133352c503133302c453132
< ACL Data TX: Handle 64 flags 0x00 dlen 5                 #35 [hci0] 11.005984
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5     #36 [hci0] 11.087199
        Num handles: 1
        Handle: 64
        Count: 2
> ACL Data RX: Handle 64 flags 0x02 dlen 9                 #37 [hci0] 11.117202
      ATT: Write Request (0x12) len 4
        Handle: 0x000c
          Data: 3623
< ACL Data TX: Handle 64 flags 0x00 dlen 5                 #38 [hci0] 11.124590
      ATT: Write Response (0x13) len 0
> HCI Event: Number of Completed Packets (0x13) plen 5     #39 [hci0] 11.351131
        Num handles: 1
        Handle: 64
        Count: 1
> HCI Event: LE Meta Event (0x3e) plen 10                  #40 [hci0] 12.002693
      LE Connection Update Complete (0x03)
        Status: Success (0x00)
        Handle: 64
        Connection interval: 30.00 msec (0x0018)
        Connection latency: 0 (0x0000)
        Supervision timeout: 720 msec (0x0048)
> ACL Data RX: Handle 64 flags 0x02 dlen 27                #41 [hci0] 13.892482
      ATT: Write Request (0x12) len 22
        Handle: 0x000c
          Data: 6c235333392c533131332c5039312c5036342c50
< ACL Data TX: Handle 64 flags 0x00 dlen 5                 #42 [hci0] 13.905726
      ATT: Write Response (0x13) len 0
> ACL Data RX: Handle 64 flags 0x02 dlen 19                #43 [hci0] 13.982417
      ATT: Write Request (0x12) len 14
        Handle: 0x000c
          Data: 35382c503133322c45313823
< ACL Data TX: Handle 64 flags 0x00 dlen 5                 #44 [hci0] 13.993446
      ATT: Write Response (0x13) len 0


# DBUS Monitoring
```ssh -lpi raspi-moonboard sudo dbus-monitor --system|less```

## Example

signal time=1638195833.267233 sender=org.freedesktop.DBus -> destination=:1.105 serial=2 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
   string ":1.105"
signal time=1638195833.270379 sender=org.freedesktop.DBus -> destination=:1.105 serial=4 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameLost
   string ":1.105"
method call time=1638195834.405055 sender=:1.13 -> destination=:1.34 serial=191 path=/com/moonboard/service0/char1; interface=org.bluez.GattCharacteristic1; member=WriteValue
   array of bytes "l#S3,S105,P60,P28,P1"
   array [
      dict entry(
         string "device"
         variant             object path "/org/bluez/hci0/dev_F0_A3_5A_A4_70_7F"
      )
      dict entry(
         string "link"
         variant             string "LE"
      )
   ]
method return time=1638195834.417610 sender=:1.34 -> destination=:1.13 serial=108 reply_serial=191
method call time=1638195834.463586 sender=:1.13 -> destination=:1.34 serial=192 path=/com/moonboard/service0/char1; interface=org.bluez.GattCharacteristic1; member=WriteValue
   array of bytes "4,E90#"
   array [
      dict entry(
         string "device"
         variant             object path "/org/bluez/hci0/dev_F0_A3_5A_A4_70_7F"
      )
      dict entry(
         string "link"
         variant             string "LE"
      )
   ]
method return time=1638195834.471207 sender=:1.34 -> destination=:1.13 serial=109 reply_serial=192